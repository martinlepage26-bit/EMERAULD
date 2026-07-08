---
type: wiki
title: EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)
aliases:
- EMERAULD graph architecture
- EMERAULD retrieval layers
- EMERAULD link density
tags:
- emerauld
- graph
- retrieval
- vectors
- lightrag
- agent-bus
- tooling
- architecture
- wiki
- store
- backlink
- vector
status: active
created: '2026-05-25'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25).md
backlink_count: 18
backlinks:
- '[[wiki/Architecture - EMERAULD Scripts - Knowledge Layers]]'
- '[[wiki/Architecture - EMERAULD Scripts - Overview]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)]]'
- '[[wiki/EMERAULD]]'
- '[[wiki/EMERAULD Thematic Analysis — Claude-Codex Pass (2026-05-25)]]'
- '[[wiki/EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]'
- '[[wiki/Vault Health — 2026-06-28]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[archive/wiki-2026-07-08/Vault Cluster Pass — Trismégiste x Hermes (2026-05-06)]]'
- '[[archive/wiki-2026-07-08/WSL and System Storage Recovery — Quick Wins Checklist]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[memory/daily/2026-06-28]]'
---

# EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)

## Summary

EMERAULD has **five distinct “graph” layers** that often get conflated:

1. **Wiki-link layer** — Obsidian-style `[[wikilinks]]` across `wiki/` and other vault folders; this is the human-authored navigation graph.
2. **Vector layer** — a local semantic index (`.vector_store/`) built from `wiki/` notes for fast similarity search (`vsearch.py`).
3. **Generated wikilink graph layer** — a deterministic machine-readable graph (`.graph_store/`) built from the same wiki corpus as `.vector_store/`.
4. **LightRAG layer** — a separate, file-backed RAG graph+KV store (`.lightrag/storage/`) built via `scripts/ingest.py` / queried via `scripts/query.py`.
5. **agent_bus layer** — coordination state (`.agent_bus/`) for multi-agent workflows and handoffs.

This note pins down what each layer is, where it lives on disk, and how to reason about “link density” without confusing backlinks with embeddings or LightRAG queue state.

## Context

The vault is operated as a **governed knowledge system**, not “just notes”: link density (wiki backlinks), retrieval quality (vector + LightRAG), and coordination (agent_bus + session-state discipline) all affect whether the system stays inspectable under pressure.

This note is the tooling-side companion to [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]] and the infrastructure index [[AI Infrastructure Stack]].

## Details

### 1) Wiki-link layer (Obsidian graph)

**Where it lives:** Markdown files across the vault, especially `wiki/`, plus MOCs/maps and selected supporting folders.

**What counts as an edge:** a `[[Target Note]]` wikilink (including path links like `[[skills/foo|foo]]`).

**Current density snapshot (local scan on 2026-05-25):**

- `wiki/` notes excluding `wiki/archive/`: **816** markdown notes.
- Frontmatter `type:` breakdown (top categories):
  - `wiki`: 264
  - `skill`: 249
  - `unknown` (no `type:` in frontmatter): 199
  - `map`: 35
  - `moc`: 5
- Backlink histogram across `wiki/` (excluding `wiki/archive/`, all note types):
  - `0`: 45
  - `1`: 80
  - `2`: 125
  - `3–4`: 145
  - `5–6`: 109
  - `7–10`: 95
  - `11–20`: 122
  - `21–50`: 75
  - `51–100`: 12
  - `101+`: 6

**Interpretation rule:** backlinks measure *navigability*, not truth. A high-backlink note can still be wrong; a low-backlink note can still be authoritative.

**Current generated snapshot (local scan on 2026-06-26, `.vector_store/paths.json` corpus):**

- Nodes: **904**
- Directed edges: **8,980**
- Link mentions: **16,082**
- Connected components: **1**
- Largest component: **904**
- Unresolved wikilinks: **3,286** (mostly links to maps, raw files, READMEs, archive indexes, and non-wiki support files)
- Zero-backlink notes: **0**
- One-backlink notes: **20**
- Two-backlink notes: **261**

> [!warning] Contradiction detected
> The snapshot above (8,980 edges / 20 one-backlink / 261 two-backlink) reflects the graph state **after the council pass but before the backlink enrichment pass** run later on 2026-06-26. The final `.graph_store/summary.json` as of end-of-day shows **9,028 edges / 6 one-backlink / 260 two-backlink** because `scripts/enrich_frontmatter_backlinks.py` added 102 generated inbound links via the Orphan Index and the graph was rebuilt. Trust `.graph_store/summary.json` for current state.

2026-06-26 graph pass: tmux council loop requested Antigravity, Vibe, and Claude to use `/obsidian-second-brain`; the local skill directory was empty, so the pass used generated `.graph_store` artifacts and direct wikilink verification. The main structural repair was reframing PHAROS from a monolithic MOC cluster into an evidence-to-publication bridge: [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]], [[COMPASSai — Governance Engine]], [[AurorA — COMPASSai Input Module]], and [[Hermes Dashboard — Professional Governance Tool]] now route into manuscript and audit notes. Bare `[[PHAROS]]` alias resolution was corrected so it points to [[PHAROS]] rather than [[PHAROS Method — Technical Reference]]; method-specific links should use [[PHAROS Method — Technical Reference]] or the `PHAROS Method` alias. Follow-up zero-orphan enforcement cleared every wiki note and collapsed the generated graph into one connected component.

Generated artifacts:

- `.graph_store/nodes.json`
- `.graph_store/edges.json`
- `.graph_store/unresolved_links.json`
- `.graph_store/components.json`
- `.graph_store/summary.json`
- `.graph_store/graph_report.md`

### 2) Vector layer (local semantic index)

**Purpose:** fast “what’s most similar” retrieval for `wiki/` without requiring LightRAG.

**Where it lives:**
- `.vector_store/embeddings.npy` — float32 `(N × 384)` embedding matrix
- `.vector_store/paths.json` — ordered path list matching embedding rows
- `.vector_store/meta.json` — build timestamp and note count

**How it’s built:**
- `scripts/embed.py` (vault-local Python): builds `.vector_store/`
- `vsearch.py` (launcher) → `scripts/vsearch.py` (search)

**Model:** `sentence-transformers/all-MiniLM-L6-v2` (384-dim, local) with normalized cosine similarity.

**Important boundary:** the vector layer does **not** know about wiki backlinks; it only knows note text (minus YAML frontmatter stripping in `embed.py`).

### 3) Generated wikilink graph layer

**Purpose:** deterministic graph-health inspection without requiring LightRAG, an LLM, or Obsidian runtime state.

**Where it lives:** `.graph_store/`

**How it is built:**

```bash
/home/martin/.venvs/emerauld/bin/python scripts/build_wikilink_graph.py
```

The builder resolves Obsidian links against note paths, note stems, first `# H1` headings, and frontmatter aliases. It treats links as directed edges, stores duplicate mention counts, and also computes undirected connected components for cluster inspection.

**Important boundary:** this layer only sees explicit `[[wikilinks]]`. It does not infer semantic similarity, and it does not prove conceptual completeness.

### 4) LightRAG layer (graph + KV + vector, separate store)

**Purpose:** graph-aware retrieval and query answering, not just similarity search.

**Where it lives (default):** `.lightrag/storage/`
- Includes queue/process state such as `.lightrag/storage/kv_store_doc_status.json` (document ingest statuses).

**How it’s built and queried:**
- `scripts/ingest.py` — inserts wiki notes into LightRAG storage
- `scripts/query.py` — queries LightRAG with modes (`local`, `global`, `hybrid`, `naive`, `mix`)

**Known operational trap:** queue state can become stale (many docs `pending/processing/failed`) and should be repaired intentionally, not during a small ingest run. See references in [[Recursive Governance Memo — EMERAULD Control Packet (2026-05-12)]] and [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]].

### 5) agent_bus layer (coordination)

**Purpose:** lightweight, inspectable coordination between agents/sessions (handoffs, messages, continuity traces).

**Where it lives:** `.agent_bus/`
- `.agent_bus/messages.sqlite` — durable message log for coordination events
- `.agent_bus/agent_bus.py` and `.agent_bus/README.md` — local tooling surface

**Relationship to session-state:** agent_bus is not a replacement for `session-state.md`; it is a complementary coordination substrate. The vault’s durable continuity record remains `session-state.md` + `VAULT ADDITIONS TRACKER.md`.

## Related

- [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]
- [[AI Infrastructure Stack]]
- [[VAULT ADDITIONS TRACKER]]
- [[session-state]]
- [[Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)]]
- [[WSL and System Storage Recovery — Quick Wins Checklist]] — Disk-space recovery checklist identifying 40–50GB recoverable on WSL/Windows; directly relevant to the lightrag venv blocker and the `/home/martin/.venvs/emerauld` vector search setup noted in this note
