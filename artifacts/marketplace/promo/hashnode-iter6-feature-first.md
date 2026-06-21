---
title: "Inside an AI-native Obsidian vault: the architecture of persistent agent memory"
subtitle: "How I designed a knowledge graph that gives AI coding agents reliable, traversable context — and why flat note dumps don't work."
tags: [obsidian, ai, productivity, developer-tools, knowledge-management]
published: false
canonical_url:
cover_image:
---

# Inside an AI-native Obsidian vault: the architecture of persistent agent memory

Most AI agent memory systems fall into one of two failure modes.

**Too flat:** A single `CLAUDE.md` or `AGENTS.md` that grows into a wall of text. The agent reads all of it on every session, attention dilutes, and the most relevant context competes with every other paragraph. Past a few hundred tokens it's noise, not signal.

**Too unstructured:** A directory of raw notes with semantic search on top. RAG retrieves the closest embeddings, but embeddings measure similarity, not relevance. A note about your API design and a note about your lunch order can be equally "similar" to the wrong query. And retrieved chunks have no graph — you get fragments without the connections that make them meaningful.

What works is a **structured knowledge graph** where the agent navigates by link traversal rather than reading everything or guessing by similarity. This post is a technical walkthrough of the architecture I settled on after six months of iteration.

---

## The three-zone structure

```
raw/        unsynthesized captures — preserved exactly as written
wiki/       synthesized, linked knowledge — the graph
CLAUDE.md   short entry point that bootstraps traversal
```

### Zone 1: `raw/`

Every capture goes here first, exactly as written. Paste from a conversation, a meeting note, a browser tab, a PDF extract — it lands in `raw/` and stays there unchanged.

The agent knows not to treat `raw/` as finished knowledge. It's a staging buffer. When something in `raw/` is worth keeping, it gets synthesized into a `wiki/` note and linked into the graph. The original raw file stays.

This separation matters: it prevents the agent from reasoning off half-formed captures and presenting them as established facts.

### Zone 2: `wiki/`

The graph. Every note here must meet three requirements before it's considered complete:

1. **Minimum two inline `[[links]]`** — in the body, not in a trailing "Related" section. A link in the body means the connection is part of the content, not an afterthought.
2. **Reachable from the entry point in three hops or fewer** — if you can't traverse from `CLAUDE.md` to the note via backlinks, the agent can't find it without searching every file.
3. **No near-duplicates** — if a related note already exists, update it rather than creating a variant.

These aren't aesthetic rules. They're the structural properties that make traversal reliable.

### Zone 3: `CLAUDE.md`

Deliberately short — typically under 50 lines. It does one thing: point to the project hub note.

```markdown
# Project Memory Entry

@wiki/Project Hub — MyApp.md
```

The project hub links outward to everything else: decision logs, architecture notes, constraints, open questions, people, systems. The agent reads the hub, follows relevant links, and stops when it has enough context. No monolithic file, no full-text scan.

---

## Note types that carry structure

### Project hub

The root node for a project. Links to every other note type that matters.

```markdown
# Project Hub — MyApp

## System
[[Architecture — API Layer]] · [[Deployment Target — Cloudflare]]

## Decisions
[[Decision — Auth Scope]] · [[Decision — DB Choice]]

## Constraints
[[Active Constraints — MyApp]]

## Open Questions
[[Open Questions — MyApp]]

## People
[[Danny Stocker]] · [[Lavoie — Prospect]]
```

One hub per project. When a project ends or pauses, archive the hub — the agent stops traversing it automatically.

### Decision log

The most important note type. Captures not just what was decided, but why, and what was ruled out.

```markdown
# Decision — Auth Layer Scope

**Status:** Locked
**Date:** 2026-03-12

## Decision
Keep auth separate from the API gateway layer.

## Reasoning
Latency isolation. Auth path and data path have different SLA requirements.
Allows independent scaling.

## Alternatives Rejected
- **Unified middleware** — couples deploy cycles; adds latency on every request.
- **Auth-in-gateway** — obscures auth logic; harder to test independently.

## Open Questions
- [ ] Whether internal service calls should bypass gateway or proxy through
```

The "Alternatives Rejected" section is load-bearing. Without it, the agent re-proposes rejected approaches because it has no record of why they were ruled out. With it, the agent reads this note before making architectural suggestions and doesn't propose unified middleware again.

### Active constraints

Short, linked, updated as constraints change.

```markdown
# Active Constraints — MyApp

- [[Deployment Target]]: Cloudflare Pages + Workers only
- [[Language]]: TypeScript frontend, Python backend
- [[Compliance]]: PIPEDA + Quebec Law 25 in scope; EU AI Act deferred to v2
- [[Timeline]]: Revenue-positive target 2026-06-22
- [[Budget]]: No paid infrastructure until first paying customer
```

Every entry links to a note that explains the constraint in more detail. The agent loads this note early in traversal and uses it to filter suggestions before proposing them.

### Open questions

The active uncertainty register. Replaces the ephemeral TODO you write at the end of a chat session.

```markdown
# Open Questions — MyApp

- [ ] Railway vs Hetzner for backend hosting — decision pending cost comparison
- [ ] Whether regulatory corpus ingestion is in scope for v1
- [ ] CF Pages recreate vs rename — CF dashboard action required
- [x] Auth token scope — RESOLVED: see [[Decision — Auth Scope]]
```

When a question is resolved, it becomes a decision log entry and gets checked off here. The agent reads this as part of session startup and knows what's currently undecided.

---

## The skill guide pattern

The vault ships with four instruction files called skill guides:

- **Caelir** — research synthesis: how to turn raw source material into linked wiki notes
- **Ilyris** — topic mapping: how to create map-of-content notes that index a domain
- **Ariun** — linking hygiene: how to audit orphan notes and repair broken graph connectivity
- **Mnara** — archival: how to identify and move stale notes out of the active graph

These are plain prose documents — not prompts, not code. When you invoke a guide by name in your session (`"run Ariun on the project wiki"`), the agent reads the instruction file and follows the steps. The behavior is procedural and explicit, not baked into a system prompt.

This matters for iteration: if a guide produces bad results, you edit the guide. The process is transparent and auditable.

---

## The optional local runtime

For users running local models, the vault ships with three Python scripts:

**`setup.sh`** — installs `sentence-transformers`, builds a vector index from all `wiki/` notes using `all-MiniLM-L6-v2`. Runs on CPU, takes ~2 minutes for 200+ notes.

**`ask.py`** — hybrid query: vector similarity narrows to the top-k candidates, then backlink traversal widens the result set to include directly-linked notes. Returns ranked results with snippets.

**`vault_watcher.py`** — watches `wiki/` for new or modified files and updates the index on save. No manual rebuild needed during active work.

No cloud dependency. The index is a local `.npy` file. Compatible with any agent framework that can read files and accept context — Ollama, LM Studio, llama.cpp via Continue, or anything else.

---

## What this replaces

Before this structure, my session startup looked like:
- Open `CLAUDE.md` (600 lines)
- Agent reads all of it
- Agent asks three questions it should already know the answers to
- I re-explain the auth decision for the fourth time

After:
- Agent reads 50-line entry file
- Traverses to project hub
- Pulls decision log + active constraints
- Starts with context

The difference isn't the AI model. It's the retrieval architecture.

---

## Template

I packaged the vault skeleton, all four skill guides, the hub templates, and the local runtime as a $49 template: **[Obsidian Agent Vault](https://pharosml.gumroad.com/l/kvbhdo)**

There's also a $299 guided setup if you want the structure adapted to your specific project type, and a $2,500 team license for shared memory across a small engineering team.

The technical decisions — three-zone structure, mandatory inline linking, hub-first traversal, decision log with rejected alternatives — are the part worth understanding. The template just gives you the scaffolding so you don't have to build it from scratch.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
