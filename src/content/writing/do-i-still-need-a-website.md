---
title: "My code is open-source and LLMs can read it, why do I need a website?"
description: The fact that models can read everything published online doesn't make personal websites redundant. It makes them more important than they used to be.
date: 2026-05-20
---

It's a question I hear a lot lately, in some form or another. "Why bother with a personal site? My work is on GitHub. Anyone who wants to know what I do can just ask a model to summarize my repos."

It's a fair question. The answer that holds up is the opposite of what most people expect. The fact that LLMs can now read everything published online doesn't make personal websites redundant. It makes them more important than they used to be.

The direct readership of doc pages is going down. People who would have read a tutorial three years ago now ask a model. That part is real and not a blip. What it doesn't mean is that the writing has stopped mattering. The consumption shifted. It didn't disappear.

## Code shows what, prose shows why

LLMs are good at telling you what a piece of code does. They are not as reliable at telling you why it does that, what was considered and rejected, what's load-bearing for a project's design, and what's a historical accident waiting to be cleaned up. That information lives in the writer's head, and in the writing they did about the project. If no one writes it down, no one, human or model, can recover it from the code alone.

This used to be an internal-team problem. It is now the public version of your work that an LLM hands to a stranger. The cost of unwritten intent has gone up.

## Models need anchors

The "just ask an LLM" workflow leans on the model finding useful chunks to ground its answer. Code is a noisy training signal. It optimizes for execution, not explanation, and the comments that exist are usually sparse and pragmatic. Prose written for human readers gives the model something better to retrieve and cite. A blog post explaining a design decision is what makes the LLM's answer about a project accurate instead of plausible-sounding.

It also works in reverse. A wrong page used to mislead one developer; now it misleads everyone who asks a model about your project. Errors are amplified, not absorbed.

<figure class="infographic">
<svg viewBox="0 0 720 320" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Diagram showing that both code and prose feed into an LLM answer, with prose highlighted as the part you control">
  <defs>
    <style>
      .lbl-a { font: 600 11px ui-monospace, SFMono-Regular, monospace; fill: #6b6b6b; letter-spacing: 0.1em; }
      .box-text-a { font: 600 13px ui-sans-serif, system-ui, sans-serif; fill: #1a1a1a; }
      .box-text-light-a { font: 600 13px ui-sans-serif, system-ui, sans-serif; fill: #fbfaf7; }
      .src-dim-a { fill: #e6e3dc; }
      .src-hl-a { fill: #1f3864; }
      .neutral-a { fill: #fbfaf7; stroke: #d9d3c4; stroke-width: 1; }
      .arrow-a { stroke: #6b6b6b; stroke-width: 1.5; fill: none; }
      .cap-a { font: 12px ui-sans-serif, system-ui, sans-serif; fill: #6b6b6b; }
    </style>
    <marker id="arr-a" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#6b6b6b"/>
    </marker>
  </defs>
  <text x="130" y="50" text-anchor="middle" class="lbl-a">SOURCES</text>
  <rect class="src-dim-a" x="40" y="70" width="180" height="60" rx="4"/>
  <text x="130" y="105" text-anchor="middle" class="box-text-a">Code</text>
  <rect class="src-hl-a" x="40" y="170" width="180" height="60" rx="4"/>
  <text x="130" y="205" text-anchor="middle" class="box-text-light-a">Docs</text>
  <text x="380" y="50" text-anchor="middle" class="lbl-a">MODEL</text>
  <rect class="neutral-a" x="300" y="120" width="160" height="60" rx="4"/>
  <text x="380" y="155" text-anchor="middle" class="box-text-a">LLM</text>
  <text x="610" y="50" text-anchor="middle" class="lbl-a">OUTPUT</text>
  <rect class="neutral-a" x="520" y="120" width="160" height="60" rx="4"/>
  <text x="600" y="155" text-anchor="middle" class="box-text-a">Answer to user</text>
  <path class="arrow-a" d="M 220 100 Q 260 100, 300 140" marker-end="url(#arr-a)"/>
  <path class="arrow-a" d="M 220 200 Q 260 200, 300 160" marker-end="url(#arr-a)"/>
  <path class="arrow-a" d="M 460 150 L 520 150" marker-end="url(#arr-a)"/>
  <text x="360" y="270" text-anchor="middle" class="cap-a">Docs are half the input to every LLM-mediated answer about your work.</text>
  <text x="360" y="288" text-anchor="middle" class="cap-a">Without them, the model fills the gap with whatever it can infer from code alone.</text>
</svg>
<figcaption>Code is one input. Prose is the other. The part you actually control is the second one.</figcaption>
</figure>

## You own the page, you don't own the model's output

If you don't write the canonical version of your work, something else will. An LLM summary built from your code and GitHub activity is one option, and it will be plausibly correct and slightly wrong about everything, the way those summaries usually are. Once the canonical version exists, that's what humans cite, what future models train on, and what shows up when someone searches your name. The website is how you get a say.

<figure class="infographic">
<svg viewBox="0 0 640 360" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Hub-and-spoke diagram showing a personal page as the canonical source feeding human readers, LLM answers, search snippets, and training data">
  <defs>
    <style>
      .ttl-b { font: 600 16px Georgia, serif; fill: #1a1a1a; }
      .center-text-b { font: 600 14px ui-sans-serif, system-ui, sans-serif; fill: #fbfaf7; }
      .spoke-text-b { font: 600 12px ui-sans-serif, system-ui, sans-serif; fill: #1a1a1a; }
      .center-b { fill: #1f3864; }
      .spoke-b { fill: #fbfaf7; stroke: #d9d3c4; stroke-width: 1; }
      .arrow-b { stroke: #6b6b6b; stroke-width: 1.5; fill: none; }
      .cap-b { font: 12px ui-sans-serif, system-ui, sans-serif; fill: #6b6b6b; }
    </style>
    <marker id="arr-b" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">
      <path d="M 0 0 L 10 5 L 0 10 z" fill="#6b6b6b"/>
    </marker>
  </defs>
  <text x="320" y="30" text-anchor="middle" class="ttl-b">What one canonical site feeds</text>
  <rect class="center-b" x="240" y="160" width="160" height="60" rx="4"/>
  <text x="320" y="195" text-anchor="middle" class="center-text-b">Site</text>
  <rect class="spoke-b" x="240" y="70" width="160" height="40" rx="4"/>
  <text x="320" y="95" text-anchor="middle" class="spoke-text-b">Human readers</text>
  <path class="arrow-b" d="M 320 160 L 320 115" marker-end="url(#arr-b)"/>
  <rect class="spoke-b" x="460" y="170" width="160" height="40" rx="4"/>
  <text x="540" y="195" text-anchor="middle" class="spoke-text-b">LLM answers</text>
  <path class="arrow-b" d="M 400 190 L 455 190" marker-end="url(#arr-b)"/>
  <rect class="spoke-b" x="20" y="170" width="160" height="40" rx="4"/>
  <text x="100" y="195" text-anchor="middle" class="spoke-text-b">Search snippets</text>
  <path class="arrow-b" d="M 240 190 L 185 190" marker-end="url(#arr-b)"/>
  <rect class="spoke-b" x="240" y="270" width="160" height="40" rx="4"/>
  <text x="320" y="295" text-anchor="middle" class="spoke-text-b">Training data</text>
  <path class="arrow-b" d="M 320 220 L 320 265" marker-end="url(#arr-b)"/>
  <text x="320" y="345" text-anchor="middle" class="cap-b">Without a canonical version, each downstream use builds its own, plausibly wrong.</text>
</svg>
<figcaption>One source, four readers. None of them are you, but all of them quote you.</figcaption>
</figure>

## Some readers still read pages

The other half of the half-LLM audience is still human. Hiring managers preparing for an interview. A peer deciding whether to invite someone to collaborate. A partner's exec trying to figure out if someone is worth a meeting. None of those people are going to chat with a model about your GitHub. They are going to open a tab.

## What's worth writing now

Not every kind of writing is worth the effort it used to be. The 30-step screenshot walkthrough is dying because models compress it to five lines. What's getting more valuable: high-precision reference content (because models cite it), conceptual writing about design intent (because models can't reconstruct it), and interactive, runnable content like notebooks and sandboxes (because models can guide a developer through them but can't replace doing the work).

## So the page stays

Personal websites aren't going anywhere. The cost of maintaining one is low, and the alternative is letting someone else, or no one, write the canonical version of your work. LLMs aren't replacing the personal website. They are another reader you're writing for, and probably the most demanding one.
