import collections
import pickle
import os
import random

import d4rl
import gym
import numpy as np
import torch

DATA_PATH = './data'

def sample_subgoals(states : list, rewards : list) -> np.array:
    N = len(states)
    si, sj = 0, 0
    subgoals = []

    while si < N:
        if si == N-1:
            sj = 0
        elif sj == si:
            weights = []
            for j in range(si + 1, N):
                tlen = j - si
                weights.append(sum(rewards[si : j]) / tlen + 0.0000001) #  Or current_state_idx + 1 : j + 1?
            sj = si + np.argmax(weights) + 1
        subgoals.append(states[sj])
        si += 1

    return np.array(subgoals)

def get_full_env_name(env_name : str, dataset : str) -> str:
    if env_name == 'kitchen':
        dataset_types = ['complete', 'partial', 'mixed']
        versions = ["v0", "v0", "v0"]
    elif env_name == 'maze2d':
        dataset_types = ['open', 'umaze', 'medium', 'large']
        versions = ["v0", "v1", "v1", "v1"]
    elif env_name == 'antmaze':
        dataset_types = ['umaze', 'umaze-diverse', 'medium-diverse', 'large-diverse']
        versions = ["v2", "v2", "v2","v2"]
    elif env_name in ['ant', 'halfcheetah', 'hopper', 'walker2d']:
        env_name = f'bullet-{env_name}'
        dataset_types = ['medium', 'medium-replay', 'medium-expert', 'expert']
        versions = ["v0", "v0", "v0", "v0"]
    else:
        raise NotImplementedError
    
    assert dataset in dataset_types, f"Invalid dataset name : '{dataset}'."

    index = dataset_types.index(dataset)
    return f'{env_name}-{dataset_types[index]}-{versions[index]}'

def download_dataset(env_name : str):
    os.makedirs(DATA_PATH, exist_ok = True)
    env = gym.make(env_name)
    dataset = env.get_dataset()
    
    # -------------------

    N = dataset['rewards'].shape[0]
    data_ = collections.defaultdict(list)

    use_timeouts = False
    if 'timeouts' in dataset:
        use_timeouts = True

    episode_step = 0
    demonstrations = []
    for i in range(N):
        done_bool = bool(dataset['terminals'][i])
        if use_timeouts:
            final_timestep = dataset['timeouts'][i]
        else:
            final_timestep = (episode_step == 1000-1)
        for k in ['observations', 'next_observations', 'actions', 'rewards', 'terminals']:
            if k == 'next_observations' and k not in dataset.keys():
                continue
            data_[k].append(dataset[k][i])
        if done_bool or final_timestep:
            episode_step = 0
            episode_data = {}
            for k in data_:
                episode_data[k] = np.array(data_[k])
            demonstrations.append(episode_data)
            data_ = collections.defaultdict(list)
        episode_step += 1

    # -------------------
        
    for demonstration in demonstrations:
        observations = np.array(demonstration['observations'])
        actions = np.array(demonstration['actions'])
        soa = (actions[0] * 0).reshape(1, -1)
        sos = (observations[0] * 0).reshape(1, -1)
        actions = np.concatenate([soa, actions])
        demonstration["actions"] = actions
        rewards = np.array(demonstration['rewards'])
        subgoals = sample_subgoals(states = observations, rewards = rewards)
        subgoals = np.concatenate([sos, subgoals])
        demonstration["sub_goals"] = subgoals

    with open(os.path.join(DATA_PATH, f'{env_name}.pkl'), 'wb') as f:
        pickle.dump(demonstrations, f)

    return demonstrations

class Dataset:
    def __init__(self, env_name : str, dataset : str, scale : int, dtype):
        self.scale : int = scale
        self.max_ep_rew : float = 0
        self.max_ep_len : int = 0
        self.device : torch.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.dtype = dtype

        # Load demonstrations from file
        self.full_env_name = get_full_env_name(env_name = env_name, dataset = dataset)
        dataset_path = os.path.join(DATA_PATH, f"{self.full_env_name}.pkl")
        if os.path.exists(dataset_path):
            print("Dataset exists, loading...")
            with open(dataset_path, 'rb') as f:
                self.trajectories = pickle.load(f)
        else:
            print("Dataset does not exist, downloading...")
            self.trajectories = download_dataset(env_name = self.full_env_name)

        # Process each demonstration
        self.states = []
        for trajectory in self.trajectories:
            self.states.append(trajectory['observations'])
            returns = trajectory['rewards'].sum()
            self.max_ep_rew = max(self.max_ep_rew, returns)
            self.max_ep_len = max(self.max_ep_len, len(trajectory["rewards"]))

        # Normalization : mean and std of states
        self.states = np.concatenate(self.states, axis = 0)
        self.state_mean, self.state_std = np.mean(self.states, axis = 0), np.std(self.states, axis = 0) + 1e-6

        env = gym.make(self.full_env_name)
        self.state_size : int = len(self.trajectories[0]['observations'][0])
        self.action_size : int = len(self.trajectories[0]['actions'][0])
        self.action_range : float = env.action_space.high[0]

    def discount_cumsum(self, x, gamma : float):
        discount_cumsum = np.zeros_like(x)
        discount_cumsum[-1] = x[-1]

        for t in reversed(range(x.shape[0]-1)):
            discount_cumsum[t] = x[t] + gamma * discount_cumsum[t+1]

        return discount_cumsum
    
    def get_batch(self, batch_size : int, sequence_length : int):
        batch_inds = np.random.choice(
            np.arange(len(self.trajectories)),
            size = batch_size,
            replace = True
        )

        s, a, a_, sg, sg_, rtg, mask = [], [], [], [], [], [], []
        for i in range(batch_size):
            traj = self.trajectories[batch_inds[i]]
            trajectory_length = traj['rewards'].shape[0]

            sf = random.randint(1, trajectory_length) # index 1 to index trajectory_length, so it just ignores 0
            si = max(0, sf - sequence_length)

            # get sequences from dataset
            states = traj['observations'][si : sf]
            all_subgoals = traj['sub_goals'][si : sf + 1]
            subgoals = all_subgoals[0 : -1]
            label_subgoals = all_subgoals[1 : ]
            all_actions = traj['actions'][si : sf + 1]
            actions = all_actions[0 : -1]
            label_actions = all_actions[1 : ]

            s.append(states.reshape(1, -1, self.state_size))
            sg.append(subgoals.reshape(1, -1, self.state_size))
            sg_.append(label_subgoals.reshape(1, -1, self.state_size))
            a.append(actions.reshape(1, -1, self.action_size))
            a_.append(label_actions.reshape(1, -1, self.action_size))

            rtg.append(self.discount_cumsum(traj['rewards'][si:], gamma=1.)[:s[-1].shape[1]].reshape(1, -1, 1)) #  + 1

            if rtg[-1].shape[1] < s[-1].shape[1]:
                rtg[-1] = np.concatenate([rtg[-1], np.zeros((1, 1, 1))], axis=1)

            # Padding and State + Reward Normalization
            tlen = s[-1].shape[1]
            s[-1] = np.concatenate([s[-1], np.zeros((1, sequence_length - tlen, self.state_size))], axis=1)
            s[-1] = (s[-1] - self.state_mean) / self.state_std
            sg[-1] = np.concatenate([sg[-1], np.zeros((1, sequence_length - tlen, self.state_size))], axis=1)
            sg[-1] = (sg[-1] - self.state_mean) / self.state_std
            sg_[-1] = np.concatenate([sg_[-1], np.zeros((1, sequence_length - tlen, self.state_size))], axis=1)
            sg_[-1] = (sg_[-1] - self.state_mean) / self.state_std
            a[-1] = np.concatenate([a[-1], np.zeros((1, sequence_length - tlen, self.action_size))], axis=1)
            a_[-1] = np.concatenate([a_[-1], np.zeros((1, sequence_length - tlen, self.action_size))], axis=1)
            rtg[-1] = np.concatenate([rtg[-1], np.zeros((1, sequence_length - tlen, 1))], axis=1) / self.scale
            mask.append(np.concatenate([np.ones((1, tlen)), np.zeros((1, sequence_length - tlen))], axis=1))

        s = torch.from_numpy(np.concatenate(s, axis=0)).to(dtype=torch.float32, device=self.device)
        sg = torch.from_numpy(np.concatenate(sg, axis=0)).to(dtype=torch.float32, device=self.device)
        sg_ = torch.from_numpy(np.concatenate(sg_, axis=0)).to(dtype=torch.float32, device=self.device)
        a = torch.from_numpy(np.concatenate(a, axis=0)).to(dtype=torch.float32, device=self.device)
        a_ = torch.from_numpy(np.concatenate(a_, axis=0)).to(dtype=torch.float32, device=self.device)
        rtg = torch.from_numpy(np.concatenate(rtg, axis=0)).to(dtype=torch.float32, device=self.device)
        mask = torch.from_numpy(np.concatenate(mask, axis=0)).to(device=self.device)

        return s, a, a_, sg, sg_, rtg, mask
    
if __name__ == '__main__':
    dataset = Dataset(env_name = 'hopper', dataset = 'expert', scale = 1000, dtype = torch.float32)

    for _ in range(10000):
        s, a, a_, sg, rtg, mask = dataset.get_batch(batch_size = 16, sequence_length = 20)
        print("-"*20)
        print(s.shape)
        print(a.shape)
        print(a_.shape)
        print(sg.shape)
        print(rtg.shape)
        print(mask.shape)
