---
title: A training loop
description: Train a one-layer linear model on noisy synthetic data. Whole thing in one cell, no DataLoader.
notebook: training-loop
order: 3
---

Sometimes you just want to see a model train. This example fits a single linear layer to a noisy linear target, prints the loss every few steps, and inspects what the model learned at the end. Should converge in a couple hundred steps. Edit the code in the panel below and hit Run.
