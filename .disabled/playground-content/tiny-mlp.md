---
title: A 3-layer MLP
description: Stack a few linear layers with ReLU, forward a batch through it, count parameters. Bare minimum nn.Sequential.
notebook: tiny-mlp
order: 2
---

`nn.Sequential` is the right thing to reach for when you just want to compose a handful of layers without writing a `Module` subclass. This example builds a 3-layer MLP, forwards a batch through it, and tells you how many parameters you ended up with. Edit the code in the panel below and hit Run.
