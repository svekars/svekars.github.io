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
# # Tensor basics
#
# A tour of the moves you do with PyTorch tensors every day: create them,
# inspect them, do element-wise math, multiply matrices.

# %%
import torch

# %% [markdown]
# Create tensors a few different ways.

# %%
zeros = torch.zeros(3, 4)
randoms = torch.randn(2, 3)
from_list = torch.tensor([[1.0, 2.0], [3.0, 4.0]])

print("zeros:\n", zeros)
print("randoms:\n", randoms)
print("from_list:\n", from_list)

# %% [markdown]
# Shape and dtype tell you what you have.

# %%
print("shape:", from_list.shape)
print("dtype:", from_list.dtype)

# %% [markdown]
# Broadcasting and element-wise ops:

# %%
x = torch.arange(6).reshape(2, 3).float()
print("x:\n", x)
print("x + 10:\n", x + 10)
print("x * x:\n", x * x)

# %% [markdown]
# Matrix multiplication with the `@` operator:

# %%
a = torch.randn(3, 4)
b = torch.randn(4, 2)
c = a @ b
print("a @ b shape:", c.shape)
