import argparse
import json
import os

import d4rl
import gym
import numpy as np
import torch
from torch.nn import MSELoss

from dataset import Dataset
from models.high_decision_mamba import HighDecisionMamba
from models.low_decision_mamba import LowDecisionMamba

RESULTS_PATH = "./Results/HierarchicalDecisionMamba"

def eval_episodes(env, high_model : HighDecisionMamba, low_model : LowDecisionMamba, num_eval_episodes, max_ep_len, action_range : float, action_size : int, state_size : int, state_mean : float, state_std : float, sequence_length : int,device):
    high_model.eval()
    high_model.to(device = device)
    low_model.eval()
    low_model.to(device = device)

    state_mean = torch.from_numpy(state_mean).to(device = device)
    state_std = torch.from_numpy(state_std).to(device = device)
    soa = np.zeros((1, action_size), dtype = np.float32)
    sos = np.zeros((1, state_size), dtype = np.float32)

    episode_returns, episode_lengths = [], []
    for episode_i in range(num_eval_episodes):
        state = env.reset()

        actions = torch.from_numpy(soa).reshape(1, 1, action_size).to(device = device, dtype = torch.float32)
        subgoals = torch.from_numpy(sos).reshape(1, 1, state_size).to(device = device, dtype = torch.float32)
        states = torch.from_numpy(state).reshape(1, 1, state_size).to(device = device, dtype = torch.float32)
        
        episode_return, episode_length = 0, 0

        for episode_t in range(max_ep_len):
            subgoal_preds = high_model.forward(
                states = (states.to(dtype = torch.float32) - state_mean) / state_std, 
                subgoals = subgoals.to(dtype = torch.float32)
            )
            subgoal = subgoal_preds[0][-1]
            subgoals = torch.cat([subgoals, subgoal.reshape(1, 1, state_size)], dim=1)

            action_preds = low_model.forward(
                states = (states.to(dtype = torch.float32) - state_mean) / state_std, 
                actions = actions.to(dtype = torch.float32), 
                subgoals = subgoals[:,1:].to(dtype = torch.float32)
            )
            action = action_preds[0][-1] * action_range
            actions = torch.cat([actions, action.reshape(1, 1, action_size)], dim=1)
            action = action.detach().cpu().numpy()

            state, reward, done, _ = env.step(action)

            cur_state = torch.from_numpy(state).to(device = device).reshape(1, 1, state_size)
            states = torch.cat([states, cur_state], dim = 1)

            episode_return += reward
            episode_length += 1

            states = states[:,-sequence_length:]
            actions = actions[:,-sequence_length:]
            subgoals = subgoals[:,-sequence_length:]

            if done:
                break

        episode_returns.append(episode_return)
        episode_lengths.append(episode_length)
    return episode_returns, episode_lengths


def train(env_name : str, dataset_name : str, batch_size : int, high_d_model : int, high_n_layer : int, low_d_model : int, low_n_layer : int, eval_every : int, iterations : int, lr : float, num_eval_episodes : int, sequence_length : int, weight_decay : float, warmup_steps : int):
    experiment_name = f'{env_name}_{dataset_name}_E{iterations}_HD{high_d_model}_HL{high_n_layer}_LD{low_d_model}_LL{low_n_layer}_K{sequence_length}'
    os.makedirs(RESULTS_PATH, exist_ok = True)

    dtype = torch.float32
    dataset : Dataset = Dataset(env_name = env_name, dataset = dataset_name, scale = 1000, dtype = dtype)
    action_range : float = dataset.action_range
    action_size : int = dataset.action_size
    state_size : int = dataset.state_size

    env = gym.make(dataset.full_env_name)

    high_model = HighDecisionMamba(state_size = state_size, action_size = action_size, d_model = high_d_model, n_layer = high_n_layer, device = "cuda", dtype = dtype)
    high_model = high_model.to(device = dataset.device)
    low_model = LowDecisionMamba(state_size = state_size, action_size = action_size, d_model = low_d_model, n_layer = low_n_layer, device = "cuda", dtype = dtype)
    low_model = low_model.to(device = dataset.device)

    # Optimizers + Schedulers
    high_optimizer = torch.optim.AdamW(high_model.parameters(), lr = lr, weight_decay = weight_decay)
    high_scheduler = torch.optim.lr_scheduler.LambdaLR(high_optimizer, lambda steps: min((steps + 1) / warmup_steps, 1))
    low_optimizer = torch.optim.AdamW(low_model.parameters(), lr = lr, weight_decay = weight_decay)
    low_scheduler = torch.optim.lr_scheduler.LambdaLR(low_optimizer, lambda steps: min((steps + 1) / warmup_steps, 1))

    # Loss Function
    loss_fn = MSELoss(reduction = 'none').to(device = dataset.device)

    # Loop
    high_train_losses, low_train_losses, val_rewards_mean, val_rewards_std, val_lengths_mean, val_lengths_std = [], [], [], [], [], []

    for iteration in range(iterations):
        high_model.train()
        low_model.train()

        states, actions, action_labels, subgoals, subgoal_labels, rtg, mask = dataset.get_batch(batch_size = batch_size, sequence_length = sequence_length)
        
        loss_mask = mask.reshape(batch_size, sequence_length) 
        
        subgoal_preds = high_model.forward(
            states = states, 
            subgoals = subgoals
        )

        high_loss = loss_fn(subgoal_preds, subgoal_labels)
        high_loss = high_loss[loss_mask > 0].mean() # (Batch, Seq_len)

        high_optimizer.zero_grad()
        high_loss.backward()
        torch.nn.utils.clip_grad_norm_(high_model.parameters(), .25)
        high_optimizer.step()
        high_scheduler.step()

        high_train_losses.append(high_loss.detach().cpu().item())

        action_preds = low_model.forward(
            states = states, 
            actions = actions, 
            subgoals = subgoal_labels
        )
        action_preds = action_preds * action_range

        low_loss = loss_fn(action_preds, action_labels)
        low_loss = low_loss[loss_mask > 0].mean() # (Batch, Seq_len)
        
        low_optimizer.zero_grad()
        low_loss.backward()
        torch.nn.utils.clip_grad_norm_(low_model.parameters(), .25)
        low_optimizer.step()
        low_scheduler.step()

        low_train_losses.append(low_loss.detach().cpu().item())

        # Eval
        if (iteration + 1) % eval_every == 0:
            rewards, lengths = eval_episodes(max_ep_len = dataset.max_ep_len, high_model = high_model, low_model = low_model, num_eval_episodes = num_eval_episodes, env = env, state_mean = dataset.state_mean, state_std = dataset.state_std, action_range = action_range, action_size = action_size, state_size = state_size, sequence_length = sequence_length, device = dataset.device)
            val_rewards_mean.append(np.mean(rewards))
            val_rewards_std.append(np.std(rewards))
            val_lengths_mean.append(np.mean(lengths))
            val_lengths_std.append(np.std(lengths))

            print(f"{env_name}-{dataset_name} | {iteration + 1} / {iterations} | Val = {val_rewards_mean[-1]:.2f} | Total = {dataset.max_ep_rew}")

    # Save Results
    with open(os.path.join(RESULTS_PATH, f"{experiment_name}.json"), "w") as f:
        json.dump({
            "high_train_losses" : high_train_losses,
            "low_train_losses" : low_train_losses,
            "val_rewards_mean" : val_rewards_mean,
            "val_rewards_std" : val_rewards_std,
            "val_lengths_mean" : val_lengths_mean,
            "val_lengths_std" : val_lengths_std
        },fp = f, indent = 4)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--env_name", type = str)
    parser.add_argument("--dataset", type = str)
    parser.add_argument("--batch_size", type = int, default = 16)
    parser.add_argument("--eval_every", type = int, default = 1000)
    parser.add_argument("--high_d_model", type = int)
    parser.add_argument("--high_n_layer", type = int)
    parser.add_argument("--iterations", type = int, default = 100000)
    parser.add_argument("--K", type = int)
    parser.add_argument("--low_d_model", type = int)
    parser.add_argument("--low_n_layer", type = int)
    parser.add_argument("--lr", type = float, default = 1e-4)
    parser.add_argument("--num_eval_episodes", type = int, default = 10)
    parser.add_argument("--weight_decay", type = float, default = 1e-4)
    parser.add_argument("--warmup_steps", type = int, default = 10000)
    args = parser.parse_args()

    train(
        env_name = args.env_name, 
        dataset_name = args.dataset, 
        batch_size = args.batch_size, 
        eval_every = args.eval_every, 
        high_d_model = args.high_d_model, 
        high_n_layer = args.high_n_layer, 
        iterations = args.iterations, 
        low_d_model = args.low_d_model, 
        low_n_layer = args.low_n_layer, 
        lr = args.lr, 
        num_eval_episodes = args.num_eval_episodes, 
        sequence_length = args.K, 
        weight_decay = args.weight_decay, 
        warmup_steps = args.warmup_steps
    )
