> **Hierarchical Decision Mamba**\
> André Correia, Luís A. Alexandre\
> Paper: 

## Information

This is a Mamba backbone version of the original HierarchicalDecisionTransformer.

# Install Anaconda
```
sudo apt-get install libgl1-mesa-glx libegl1-mesa libxrandr2 libxrandr2 libxss1 libxcursor1 libxcomposite1 libasound2 libxi6 libxtst6

curl -O https://repo.anaconda.com/archive/Anaconda3-2024.02-1-Linux-x86_64.sh

bash Anaconda3-2024.02-1-Linux-x86_64.sh

conda init
```

# Create and activate environment
```
conda create --name DecisionMamba

conda activate DecisionMamba
```

# Install Dependencies
```
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

pip3 install numpy

pip install causal-conv1d>=1.2.0

pip install mamba-ssm
```

# Train

Train Hierarchical Decision Mamba

```
python3 train_hierarchical_decision_mamba.py --seed 99 --env_name ant --dataset medium-expert --high_n_layer 6 --high_d_model 128 --low_n_layer 6 --low_d_model 128 --K 20
```

## Citation

If you use this codebase, or otherwise found our work valuable, please cite HDM:
```
Coming Soon.
```
