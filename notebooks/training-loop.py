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
# # Training a tiny model on synthetic data
#
# The whole training loop in one cell, no DataLoader required. The target
# is a noisy linear relationship and the model is a single linear layer,
# so this should converge fast.

# %%
import torch
import torch.nn as nn

# %% [markdown]
# Make some fake data: y = 3x + 2 with a bit of noise.

# %%
torch.manual_seed(0)
x = torch.linspace(-1, 1, 200).unsqueeze(1)
y = 3 * x + 2 + 0.1 * torch.randn_like(x)

# %% [markdown]
# Define a one-layer model, optimizer, and loss function.

# %%
model = nn.Linear(1, 1)
optimizer = torch.optim.SGD(model.parameters(), lr=0.1)
loss_fn = nn.MSELoss()

# %% [markdown]
# Loop. Print loss every 40 steps.

# %%
for step in range(200):
    optimizer.zero_grad()
    pred = model(x)
    loss = loss_fn(pred, y)
    loss.backward()
    optimizer.step()
    if step % 40 == 0:
        print(f"step {step:3d}  loss {loss.item():.4f}")

# %% [markdown]
# Inspect what the model learned. Should be roughly slope = 3, bias = 2.

# %%
w = model.weight.item()
b = model.bias.item()
print(f"learned: y = {w:.2f}x + {b:.2f}")
print(f"target:  y = 3.00x + 2.00")
