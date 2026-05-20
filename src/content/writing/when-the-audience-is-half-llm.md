---
title: When the audience is half-LLM
description: What changes about documentation when models are reading it on behalf of developers, and why most of the old assumptions break.
date: 2026-05-03
---

For most of the history of technical documentation, the reader was a human. Now they often aren't, or not entirely. A meaningful fraction of the people who would have read docs.pytorch.org never see the page. They see whatever an LLM pulled out of it: a paragraph in a chat reply, a snippet behind a code completion, a chunk buried inside a longer answer. The page is still there. The reader is not.

This breaks a lot of conventional doc wisdom in ways that aren't obvious until you start looking.

## Chunks, not pages

The first thing it breaks is information architecture as we usually mean it. Hierarchy, sidebars, breadcrumbs, those are for people who navigate. Models don't navigate, they retrieve. They grab the chunk that scored highest against the query and run with it. So the question is no longer "how do I help a reader find this page" but "is each chunk, severed from its page, still useful?" If your conceptual overview lives 800 words above the code sample the model retrieved, the code arrives without the concept, and the model fills the gap with whatever it remembers from pretraining. That gap is where hallucinations live.

<figure class="infographic">
<svg viewBox="0 0 640 300" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Comparison of how a human reader sees an entire documentation page while a model sees only the retrieved chunk">
  <defs>
    <style>
      .ttl-x { font: 600 11px ui-monospace, SFMono-Regular, monospace; fill: #6b6b6b; letter-spacing: 0.1em; }
      .lbl-x { font: 13px ui-sans-serif, system-ui, sans-serif; fill: #1a1a1a; }
      .doc-x { fill: #fbfaf7; stroke: #d9d3c4; stroke-width: 1; }
      .chunk-faded-x { fill: #e6e3dc; }
      .chunk-hl-x { fill: #1f3864; }
      .doc-dim-x { fill: #fbfaf7; stroke: #d9d3c4; stroke-width: 1; opacity: 0.35; }
      .chunk-dim-x { fill: #e6e3dc; opacity: 0.35; }
    </style>
  </defs>
  <text x="160" y="30" text-anchor="middle" class="ttl-x">HUMAN READER</text>
  <rect x="80" y="50" width="160" height="180" rx="4" class="doc-x"/>
  <rect x="92" y="62" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="80" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="98" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="116" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="134" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="152" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="170" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="188" width="136" height="14" class="chunk-faded-x"/>
  <rect x="92" y="206" width="136" height="14" class="chunk-faded-x"/>
  <text x="160" y="254" text-anchor="middle" class="lbl-x">Sees the whole page</text>
  <text x="480" y="30" text-anchor="middle" class="ttl-x">MODEL</text>
  <rect x="400" y="50" width="160" height="180" rx="4" class="doc-dim-x"/>
  <rect x="412" y="62" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="80" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="98" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="116" width="136" height="14" class="chunk-hl-x"/>
  <rect x="412" y="134" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="152" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="170" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="188" width="136" height="14" class="chunk-dim-x"/>
  <rect x="412" y="206" width="136" height="14" class="chunk-dim-x"/>
  <text x="480" y="254" text-anchor="middle" class="lbl-x">Sees one retrieved chunk</text>
</svg>
<figcaption>A page with surrounding context is not the same artifact as the single chunk a retriever returns.</figcaption>
</figure>

## Recall doesn't measure what you think

The second thing it breaks is what success looks like. A paper I co-authored last year, [The 99% Success Paradox](https://arxiv.org/abs/2605.18857), made this concrete. Standard retrievers report >99% success rates on common benchmarks while actually selecting documents at random. The dashboards look fine. The answers don't.

<figure class="infographic">
<svg viewBox="0 0 640 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Chart showing high coverage and near-zero selectivity for the same retriever at K=100">
  <defs>
    <style>
      .ttl-c { font: 600 17px Georgia, serif; fill: #1a1a1a; }
      .pnl-c { font: 600 11px ui-monospace, SFMono-Regular, monospace; fill: #6b6b6b; letter-spacing: 0.1em; }
      .ax-c { font: 11px ui-sans-serif, system-ui, sans-serif; fill: #6b6b6b; }
      .val-c { font: 600 16px ui-sans-serif, system-ui, sans-serif; fill: #1f3864; }
      .cap-c { font: 12px ui-sans-serif, system-ui, sans-serif; fill: #6b6b6b; }
      .bar-c { fill: #1f3864; }
      .axline-c { stroke: #d9d3c4; stroke-width: 1; }
      .base-c { stroke: #d9d3c4; stroke-width: 1; stroke-dasharray: 3 3; }
    </style>
  </defs>
  <text x="320" y="30" text-anchor="middle" class="ttl-c">Same retriever, two metrics</text>
  <text x="160" y="58" text-anchor="middle" class="pnl-c">COVERAGE AT K=100</text>
  <line x1="80" y1="80" x2="80" y2="280" class="axline-c"/>
  <text x="74" y="84" text-anchor="end" class="ax-c">100%</text>
  <text x="74" y="284" text-anchor="end" class="ax-c">0</text>
  <rect class="bar-c" x="120" y="82" width="80" height="198"/>
  <text x="160" y="74" text-anchor="middle" class="val-c">&gt;99%</text>
  <line x1="80" y1="280" x2="240" y2="280" class="base-c"/>
  <text x="480" y="58" text-anchor="middle" class="pnl-c">SELECTIVITY (BOR)</text>
  <line x1="400" y1="80" x2="400" y2="280" class="axline-c"/>
  <text x="394" y="84" text-anchor="end" class="ax-c">~5 bits</text>
  <text x="394" y="284" text-anchor="end" class="ax-c">0</text>
  <rect class="bar-c" x="440" y="276" width="80" height="4"/>
  <text x="480" y="268" text-anchor="middle" class="val-c">&#8776; 0</text>
  <line x1="400" y1="280" x2="560" y2="280" class="base-c"/>
  <text x="320" y="318" text-anchor="middle" class="cap-c">On 20 Newsgroups, BM25 and SPLADE report &gt;99% coverage at K=100</text>
  <text x="320" y="336" text-anchor="middle" class="cap-c">while chance-corrected selectivity sits near zero.</text>
</svg>
<figcaption>The same retriever scores near-perfect by one metric and near-random by another. Which one you watch decides what you ship.</figcaption>
</figure>

Recall is not the right scoreboard for docs that feed an LLM, and a lot of teams haven't realized that yet. You need a chance-corrected metric, or you need an eval set where the gold answer is wrong if the wrong chunks are retrieved. Otherwise you're flying blind on the failure mode that matters most.

## Repetition is load-bearing now

The third thing it breaks is the style guide. "Don't repeat yourself" was good advice for readers who could scroll back. It is bad advice for readers who only see the fragment they retrieved. A chunk that says "as described in the previous section" is useless out of context. A chunk that briefly re-states the context is useful in any setting. Repetition is load-bearing now. So is version awareness, code blocks that include their imports, and prose that names the API instead of aliasing it as "the function."

## Drift matters more

If a model is going to ground its answer in your docs, the bar for accuracy moves up. A stale code sample that a human would notice and work around becomes an authoritative-sounding lie when it's quoted inside a chatbot reply. The half-life of "good enough" doc content is shorter than it used to be.

## What stays the same

None of this is a call to rewrite everything. Most of what makes docs good for humans makes them good for models too: precise language, working code, a clear answer to the question someone actually asked. What changes is the assumptions you can lean on. You can no longer assume the reader will see what's around the thing they retrieved. You can no longer trust your old metrics. And you can no longer treat the chunk as the unit of writing while treating the page as the unit of quality.

At PyTorch I treat the doc corpus as something an LLM is going to read at scale, every day, on behalf of developers I'll never see. That changes what gets prioritized in audits, what gets added to the publishing pipeline, and which failure modes I worry about most. The job is still writing docs. The reader changed.
