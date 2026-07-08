---
type: artifact
title: I tried 4 approaches to AI agent memory. Here's what actually worked.
aliases:
- artifacts/marketplace/promo/devto-iter9-comparison
tags:
- ai
- obsidian
- productivity
- claudeai
- artifact
- artifacts
- marketplace
- similarity
- everything
- agent
- retrieved
- approach
- color-orange
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/devto-iter9-comparison.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
published: false
canonical_url: null
description: Long context files, RAG, embeddings, knowledge graphs — I ran all four
  on a real 6-month project. Only one held up past 100 notes.
---

# I tried 4 approaches to AI agent memory. Here's what actually worked.

Six months ago I started building a governance SaaS product with Claude Code as my primary dev partner. The codebase grew. The context problem grew faster.

I tried four approaches to keeping the agent oriented across sessions. Three of them failed in predictable ways. Here's what I learned from each.

---

## Approach 1: Long CLAUDE.md

The obvious starting point. One file, everything in it — project description, architectural decisions, tech stack, naming conventions, open questions, constraints, active tasks.

**What happened:** It worked for the first two months. Then the file hit ~600 lines and started failing silently. The agent would read it, acknowledge constraints, then propose something that violated a constraint buried in paragraph 14. It wasn't hallucinating — it was attending correctly to the first ~300 tokens and poorly to the rest.

**The failure mode:** Flat context doesn't scale. The most relevant information competes with everything else. As the file grows, the signal-to-noise ratio drops and you can't fix it by curating better — the file just becomes a negotiation between what you cut and what the agent needs.

**When it works:** Projects with a short, stable context that fits in ~200 lines and doesn't evolve much. Anything living longer than a month will outgrow it.

---

## Approach 2: Raw note dump + grep/search

Second attempt: put everything in a directory of Markdown files, let the agent search when it needs context.

**What happened:** The agent searched correctly but retrieved fragments. A decision log retrieved in isolation — without the surrounding context of what problem it was solving, what came before it, what constraints shaped it — is almost useless. The agent would find the "what" without the "why."

**The failure mode:** Full-text search retrieves by keyword match, not by meaning. And even when it retrieves the right note, a standalone note without links to adjacent concepts gives the agent a fragment, not understanding.

**When it works:** Narrow, well-scoped queries where the right answer is self-contained. Not for architectural context that depends on a web of prior decisions.

---

## Approach 3: Embeddings + semantic search (RAG)

Third attempt: embed all notes with `sentence-transformers`, query by cosine similarity, feed top-k results as context.

**What happened:** Better recall than keyword search, but a new failure mode appeared — similarity isn't relevance. A note about your authentication design and a note about your deployment checklist can be equally "similar" to a query about your API architecture. The model retrieved plausible-sounding context that wasn't actually the right context.

More importantly, RAG returns chunks. Chunks don't have relationships. The agent got the right paragraph but not the connected decision that made that paragraph meaningful.

**The failure mode:** Semantic similarity measures distance in embedding space, not logical relevance in your project. And chunked retrieval destroys the graph structure that makes notes meaningful to each other.

**When it works:** Finding notes you forgot existed, surfacing material you didn't know to search for. Good as a discovery layer, bad as the primary retrieval mechanism for agent context.

---

## Approach 4: Structured knowledge graph with mandatory inline linking

What finally held up: restructuring all project knowledge as a linked graph, where the agent navigates by traversal rather than by reading or searching.

**The structure:**

```
raw/       unsynthesized captures, never modified
wiki/      synthesized notes — each requires ≥2 inline [[links]]
CLAUDE.md  ~50 lines pointing to the project hub
```

**The key constraint:** every note in `wiki/` must link to at least two related notes *in the body* — not in a trailing "Related" section. A link in the body means the connection is part of the reasoning, not an afterthought. Orphan notes don't exist to the agent.

**Why traversal beats retrieval:** The agent starts at `CLAUDE.md`, follows the link to the project hub, follows links from there to the decision log and active constraints, and reaches relevant context in 3 hops — without searching, without reading everything, without similarity scoring.

**The note type that changed everything:** Decision logs with a "Rejected Alternatives" section. Not just what was decided, but what was explicitly ruled out and why. The agent reads this before suggesting anything architectural. It doesn't re-propose the rejected approach because it already knows why it was rejected.

**What broke the pattern:** Notes without links. An insight captured in isolation is invisible to traversal. The discipline of linking before saving — finding the related project, person, concept, or decision and wiring the new note into the graph — is what makes the whole system work. It takes 30 extra seconds per note. It saves 15 minutes per session.

---

## What I'd do differently

Start with the graph structure from session one, not after the context problem appears. The worst time to restructure your knowledge is when you're 150 notes in with no backlinks.

The minimum viable version: one project hub note, one decision log, one active constraints note, wired together. Three notes, all linked. Everything else can come later.

---

I packaged the vault structure — skeleton, templates, note types, skill guides, optional local runtime — as a $49 template: **[Obsidian Agent Vault](https://pharosml.gumroad.com/l/kvbhdo)**

The four approaches above are what I went through before landing on the graph structure. Hopefully this saves you the same six-month detour.

## Related

- [[Governance and PHAROS MOC]]
- [[hashnode-iter34-skill-guides]]
