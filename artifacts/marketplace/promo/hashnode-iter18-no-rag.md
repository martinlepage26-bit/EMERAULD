---
type: artifact
title: How I Built an AI Second Brain Without RAG
aliases:
- artifacts/marketplace/promo/hashnode-iter18-no-rag
tags:
- artifact
- ai
- artifacts
- marketplace
- similarity
- session
- native
- vector
- retrieval
- color-orange
status: preserved
created: '2026-06-21'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/promo/hashnode-iter18-no-rag.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# How I Built an AI Second Brain Without RAG

*Hashnode — Iteration 18 — Cycle 4 — 2026-04-20*
*Angle: No-RAG architecture — file-native, structured, and fast*
*Product: https://pharosml.gumroad.com/l/kvbhdo*

---

When people say "AI second brain," they usually mean a RAG pipeline: chunk your documents, embed them, query by cosine similarity, retrieve relevant context, inject it into the prompt.

It works. It's also overkill for most personal knowledge work, introduces a fragile build step, requires an embedding model (and either a local GPU or an API call), and produces retrieval that's probabilistic rather than structural.

I built something different. It's faster to set up, fully local and free to run, and — for the specific problem of AI-assisted work — I think it produces better results.

Here's the architecture.

## The core insight

RAG optimises for *finding similar content*. The problem with AI-assisted work isn't usually finding similar content — it's maintaining *structured context* across sessions.

When I ask Claude to continue working on a governance document, I don't need it to retrieve notes that are semantically similar to "governance document." I need it to know:

- What decisions have already been made about this document
- What approaches were tried and rejected
- What the current open questions are
- What the next step is

That's structured context, not similarity search. A file with the right structure, read directly, does this better than a vector retrieval.

## The actual architecture

**Three zones, file-native, Obsidian-compatible:**

### Zone 1 — Raw sources
Everything you capture goes here first, unmodified. Journal entries, meeting notes, web clips, research dumps, voice transcripts. Nothing gets edited in raw. It's a staging area, not a knowledge base.

Rule: raw is for capture. It's never the source of truth.

### Zone 2 — Wiki (synthesized knowledge)
The permanent layer. Each note here:
- Has been deliberately created or synthesized from raw material
- Contains at least 2 meaningful `[[links]]` to related notes
- Is reachable from the graph (connected to at least one hub, MOC, or project node)

Notes here are designed to be read by an AI agent as context — structured with Summary, Context, and Details sections. The Summary is the most important part: it's what the AI sees first and what determines whether the note is worth loading in full.

### Zone 3 — Session state
A small set of files that carry live operational context:

- `session-state.md` — updated at session end, read at session start. Contains: active threads, decisions made this session, open questions, next actions.
- Hub notes per project — current state, active constraints, decisions log
- `memory/daily/` — timestamped logs of significant actions

The AI starts every session by reading session-state.md and the relevant hub note. That's it. No retrieval, no embedding, no build step.

## How it compares to RAG

| | RAG | This architecture |
|---|---|---|
| Setup time | Hours–days | 30 minutes |
| Running cost | API calls or local GPU | Free (file reads) |
| Retrieval type | Probabilistic similarity | Structural (read directly) |
| Context type | "Related content" | "Active state + decisions" |
| Breaks after reorganization? | Yes (re-embed) | No (links update) |
| Works offline | Depends on model | Yes (Ollama optional) |
| Auditable | Difficult | Native (it's just files) |

RAG is the right choice for large knowledge bases where you can't predict what you'll need. For AI-assisted work on specific ongoing projects, structured file-native context is faster and more predictable.

## The vector store I did eventually add

At 200+ notes, I added a lightweight vector store: sentence-transformers (`all-MiniLM-L6-v2`), numpy dot products, a 2-minute build time. Not for primary retrieval — for discovery. When I can't remember where a note lives, `vsearch.py "query"` finds it faster than manual graph traversal.

But the core AI workflow still runs on direct file reads. The vector store is a navigation tool, not the architecture.

## The vault template

The skeleton for this system — note types, hub templates, session-state protocol, linking rules, and optional local runtime with the vector store — is available as an Obsidian vault template.

→ [Obsidian Agent Vault on Gumroad](https://pharosml.gumroad.com/l/kvbhdo) — $49

It includes:
- 4 typed note templates (Wiki, Raw, Map, Session-state)
- Hub and MOC structure
- 4 named AI guide identities with distinct specializations
- Optional local runtime (setup script, query tool, vault watcher)
- Buyer rename script for personalizing the guide names

If you've been putting off building an AI memory system because RAG felt like too much infrastructure, this is the simpler path.

---

*Tags: `#obsidian` `#ai` `#pkm` `#productivity` `#llm` `#knowledgemanagement`*

## Related

- [[Governance and PHAROS MOC]]
- [[hashnode-iter34-skill-guides]]
