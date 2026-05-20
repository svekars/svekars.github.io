# svekars.github.io

Personal site, built with [Astro](https://astro.build/). Deployed to GitHub Pages on every push to `main`.

## Develop

```sh
npm install
npm run dev
```

Then open http://localhost:4321.

## Build

```sh
npm run build
npm run preview
```

## Write a post

Drop a markdown file in `src/content/writing/`. Frontmatter:

```md
---
title: Post title
description: Optional one-liner.
date: 2026-05-20
draft: false
---
```

Set `draft: true` to keep an entry out of the index.

## Layout

- `src/pages/index.astro` is the resume page.
- `src/pages/writing/` is the blog list and post template.
- `src/content/writing/` holds the markdown posts.
- `src/pages/playground/` is the playground list and per-example page.
- `src/content/playground/` holds the per-example metadata + intro.
- `notebooks/` holds the runnable jupytext notebooks (`.py` source + paired `.ipynb`).
- `src/styles/global.css` carries the design tokens and most styles.
- `.github/workflows/deploy.yml` builds and publishes to GitHub Pages.

## Add a playground example

Each playground entry pairs static source code (shown on the page) with an embedded Replit (where the code actually runs).

1. Write the source as a `.py` notebook under `notebooks/` using jupytext "percent" cells (`# %% [markdown]` and `# %%`). This is the source of truth for what's displayed on the page.
2. Create a public Replit (Python template). Paste the code in. Make sure `torch` is installed (Replit's package manager picks it up automatically the first time you `import torch`).
3. Grab the Replit URL. It looks like `https://replit.com/@<user>/<repl-name>`.
4. Add a metadata file at `src/content/playground/<slug>.md`:
   ```yaml
   ---
   title: ...
   description: ...
   notebook: <slug>          # matches notebooks/<slug>.py
   replit: https://replit.com/@<user>/<repl-name>
   order: 5
   ---
   ```
5. Commit and push. Astro reads the metadata at build time, embeds the Replit as an iframe, and falls back to a "not configured" card if `replit` is omitted.
