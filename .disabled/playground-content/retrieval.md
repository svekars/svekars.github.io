---
title: Cosine similarity retrieval
description: Score a corpus of random embeddings against a query, take the top K. A toy version of what a real retrieval system does, and the setup behind the BoR paper.
notebook: retrieval
order: 4
---

A few lines of PyTorch and you have the core of an embedding-based retrieval system: score every document against the query with cosine similarity, return the highest scoring K. This example does it with random embeddings on purpose. That's the setup behind [The 99% Success Paradox](https://arxiv.org/abs/2605.18857), the paper this site links to, which shows how high reported success rates can mask near-random selectivity. Edit the code in the panel below and hit Run.
