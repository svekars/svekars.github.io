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
# # Ranking documents by cosine similarity
#
# A toy version of what a real retrieval system does: score each document
# embedding against a query, return the top K.
#
# This is also the setup behind
# [The 99% Success Paradox](https://arxiv.org/abs/2605.18857). The example
# below uses random embeddings, so the rankings are random. That's the point
# the paper is making.

# %%
import torch
import torch.nn.functional as F

# %% [markdown]
# Make a fake corpus of 1000 documents with 128-dimensional embeddings.

# %%
torch.manual_seed(0)
n_docs = 1000
dim = 128
docs = torch.randn(n_docs, dim)
query = torch.randn(dim)

# %% [markdown]
# Cosine similarity of the query against every document.

# %%
scores = F.cosine_similarity(docs, query.unsqueeze(0), dim=1)
print("scores shape:", scores.shape)
print(f"score range: {scores.min().item():.3f} to {scores.max().item():.3f}")

# %% [markdown]
# Top-K retrieval.

# %%
K = 5
top_scores, top_idx = torch.topk(scores, K)
for rank, (s, i) in enumerate(zip(top_scores, top_idx), 1):
    print(f"rank {rank}: doc #{i.item():4d}  score {s.item():.3f}")

# %% [markdown]
# These ranks are random because the data is random. The point of
# Bits-over-Random (BoR) is to detect exactly that: when high reported
# success rates mask no real selectivity.
