# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown]
# # A 3-layer MLP in 10 lines
#
# `nn.Sequential` gives you a stack of layers with no boilerplate. This is
# usually the right thing to reach for when you just want to compose a few
# layers and move on.

# %%
import torch
import torch.nn as nn

# %% [markdown]
# Define the model.

# %%
model = nn.Sequential(
    nn.Linear(16, 32),
    nn.ReLU(),
    nn.Linear(32, 32),
    nn.ReLU(),
    nn.Linear(32, 4),
)
print(model)

# %% [markdown]
# Forward a batch of 8 examples through it.

# %%
x = torch.randn(8, 16)
y = model(x)
print("input shape: ", x.shape)
print("output shape:", y.shape)

# %% [markdown]
# Parameter count, just to know what you're working with.

# %%
total = sum(p.numel() for p in model.parameters())
print(f"{total:,} parameters")
