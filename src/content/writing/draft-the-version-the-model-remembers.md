---
title: The version the model remembers
description: Versioned APIs were a hard problem when humans read the docs. They're a worse problem when a model quotes them.
date: 2026-05-21
draft: true
---

Every framework I've worked on has a version mess buried somewhere in its docs. Two arguments swapped order in 1.8. A function moved modules in 2.0. A flag that used to default to True started defaulting to False and nobody updated the tutorial that depended on the old behavior. For years, the cost of that mess was bounded. A developer hit the error, searched the message, found a forum thread, and moved on. The bad page was a speed bump.

That bound is gone. When a model is the reader, the speed bump turns into a confident wrong answer delivered to someone who has no signal that anything was wrong.

## Versions are a context-window problem

The convention in technical docs is to put the version somewhere the human will see it. A version selector in the sidebar. A banner at the top of the page. A tag in the URL. None of that survives chunking. The retriever grabs a paragraph in the middle of the page, hands it to the model, and the model returns it without ever seeing the banner that said "this page documents 1.13 only."

This is not a hypothetical. I have watched a model paste a code sample from a four-year-old tutorial into a chat reply, with the confident tone of something that just ran. The chunk had no version string. The page had one. The retriever had no reason to care.

The lesson is unfun: if a piece of information is only true in version X, the chunk has to say so, not the page. That sounds like a small change. It is actually a different way of writing docs, because it pushes context that used to live in the chrome of the site down into the body of every paragraph that might be retrieved in isolation.

## Deprecation notices were already broken

The standard fix for "the API changed" is a deprecation notice. A box at the top of a function reference that says "removed in 2.0, use Y instead." This worked when the reader was scrolling. It fails the chunking test for the same reason version banners do. The deprecation lives in a different block than the code sample that demonstrates the deprecated call. A retriever happily returns the code without the notice.

I have started thinking about deprecation notices the way I think about disclaimers in pharmaceutical ads. They are not for the patient who reads carefully. They are for the model that grabs three sentences and runs. The notice has to be welded to the code, not floating above it.

In practice this means inline comments inside code blocks ("# removed in 2.0; see torch.foo"), prose paragraphs that re-name the version when they mention the API, and accepting that the same warning will appear in five places on the same page. Repetition was already load-bearing for chunked retrieval. Versioning makes that bill come due.

## The wrong version is worse than no version

When a tool returns "I don't know," a developer goes looking. When a tool returns a fluent, plausible answer that targets the wrong version, the developer types it in and waits for the traceback. There is a real cost gap between those two outcomes, and our doc pipelines aren't measuring it.

The eval sets I've seen for LLM-backed doc assistants almost all measure whether the model produced a correct answer when the correct page was retrieved. They do not measure what happens when an older version of the correct page is retrieved instead. The failure mode is silent in most metrics, and it's the failure mode that produces the worst user experience: confident, specific, wrong, and aimed at the API a beginner is least likely to second-guess.

A version-aware eval is not glamorous work. You take your gold answers, fork them by release, and check whether the assistant's reply is correct for the version the user implicitly asked about. Most teams have not done this. The teams that have done it have all told me a version of the same story: the numbers got worse before they got better, because the silent failures were finally visible.

## What to actually change

A short list of the things I have started pushing for, in roughly the order they pay off:

- Put the version in the chunk, not the chrome. If a code block is version-specific, the version goes inside the code block or in the sentence right next to it.
- Move deprecations inline. A box at the top of the page does not survive retrieval. A comment in the snippet does.
- Drop tutorials that document removed APIs. The cost of leaving them up used to be confusion for a few stragglers. The cost now is that they get cited as current.
- Build a versioned eval. Even a hand-curated set of 50 queries with the expected answer per release will catch the worst regressions.
- Treat the changelog as a doc artifact, not a release artifact. It is the most retrievable summary of what moved when, and it tends to be written carefully because release managers care. Index it. Let the model cite it.

None of these are exciting. Most of them are the kind of thing that gets deprioritized when a feature ships, because the doc fix is "we'll catch it in the next pass." The next pass is no longer the bottleneck. The bottleneck is that a model is going to read whatever is sitting on the site, today, and answer a stranger's question with it.

## The version is part of the answer

The frame I keep coming back to is this: the version is not metadata about the answer, it is part of the answer. A code sample without its version is incomplete in the same way a code sample without its imports is incomplete. We accepted the imports rule a long time ago, because we got tired of pasting things that didn't run. We have not yet accepted the version rule, because the failure mode hides under a layer of confident prose.

It will not stay hidden. The first time a high-profile model quotes a five-year-old default value to a paying customer, someone is going to ask whose job it was to keep that page current. The honest answer is that we wrote the page for a reader who could see the banner. We are going to need a different page now.
