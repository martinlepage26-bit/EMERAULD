---
type: architecture-module
title: Architecture - EMERAULD Scripts - Knowledge Layers
aliases:
- EMERAULD knowledge retrieval layers
- wiki/Architecture - EMERAULD Scripts - Knowledge Layers
tags:
- architecture
- emerauld
- vector-search
- lightrag
- knowledge-graph
- scripts
- architecture-module
- wiki
- architecture-emerauld-scripts-knowledge-layers-md
- graph
- venvs
- store
- query
- json
- color-teal
status: active
created: '2026-06-29'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Architecture - EMERAULD Scripts - Knowledge Layers.md
backlink_count: 8
backlinks:
- '[[wiki/Architecture - EMERAULD Scripts - Intake Pipeline]]'
- '[[wiki/Architecture - EMERAULD Scripts - Key Decisions]]'
- '[[wiki/Architecture - EMERAULD Scripts - Overview]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[index]]'
- '[[wiki/lightrag_config — EMERAULD Shared Config Module]]'
- '[[memory/daily/2026-06-29]]'
- '[[session-state]]'
scanned-commit: 96e6487
---

> For future Claude: Documents the three parallel knowledge retrieval layers in [[EMERAULD]]: vector search (embed/vsearch), LightRAG semantic graph (ingest/query), and deterministic wikilink graph (build_wikilink_graph). Load this when choosing how to query the vault or when any retrieval script behaves unexpectedly. The layers are independent — a note added to wiki/ does not appear in any layer until that layer's rebuild command is run.

<!-- @generated:start -->

## Summary

Three retrieval strategies operate in parallel over `wiki/`, `maps/`, and `projects/`. They are not synchronized and serve different query types. All share [[lightrag_config]] as the config module.

## Layer 1 — Vector search (`embed.py` + `vsearch.py`)

**What it is:** Cosine similarity over sentence embeddings stored as a numpy matrix.

**Model:** `all-MiniLM-L6-v2` (sentence-transformers, 384 dimensions, fully local). Model is loaded from HuggingFace cache if available, hub otherwise. Cached at `~/.cache/huggingface/hub/models--sentence-transformers--all-MiniLM-L6-v2/`.

**Storage:** `.vector_store/embeddings.npy` (matrix), `.vector_store/paths.json` (path index), `.vector_store/meta.json`.

**Corpus:** `wiki/**/*.md`, `maps/**/*.md`, `projects/**/*.md` (hardcoded in `embed.py:CORPUS_DIRS`).

**Rebuild commands:**
```bash
cd /home/martin/EMERAULD/scripts
/home/martin/.venvs/emerauld/bin/python3 embed.py           # full rebuild
/home/martin/.venvs/emerauld/bin/python3 embed.py --changed # incremental (24h window)
/home/martin/.venvs/emerauld/bin/python3 embed.py --check   # status only
```

**Query:**
```bash
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "query" --top 10
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "query" --full  # returns note body
```

**Trade-off:** Fastest retrieval; no LLM call; works offline; no entity graph — returns semantically similar notes, not entity relationships.

**Current state (as of commit 96e6487):** 896 entries, last built 2026-06-21.

> [!warning] Contradiction detected
> As of 2026-06-29, `.vector_store/meta.json` reports **910 entries** — not 896. The architecture note was generated from commit 96e6487 state; the vector store was subsequently rebuilt (entries added from today's architecture notes and routing report). Trust `meta.json` for live count; trust this note for the design description.

---

## Layer 2 — LightRAG semantic graph (`ingest.py` + `lightrag_config.py` + `query.py`)

**What it is:** LightRAG ingests notes using an LLM to extract entities and relationships, stores them as a file-based graph (NetworkX + NanoVectorDB + JsonKV).

**LLM:** `claude-haiku-4-5-20251001` (Anthropic API) — pulled from `~/.claude/.credentials.json` via OAuth. OpenRouter fallback when `OPENROUTER_API_KEY` is set (default model: `openai/gpt-4o-mini`). Rate-limited at 1 call/second.

**Storage:** `.lightrag/storage/` — file-based; portable.

**Ingest command:**
```bash
/home/martin/.venvs/emerauld/bin/python3 ingest.py           # all wiki notes
/home/martin/.venvs/emerauld/bin/python3 ingest.py --changed # recently modified
```

**Query command:**
```bash
/home/martin/.venvs/emerauld/bin/python3 query.py "question"
```

**Trade-off:** Richest retrieval for entity- and relationship-level queries ("what decisions did Martin make about HELIX?"). Requires API call per note on ingest; slow; needs network. Not suitable for bulk rebuild on every session.

---

## Layer 3 — Deterministic wikilink graph (`build_wikilink_graph.py`)

**What it is:** Parses `[[wikilink]]` syntax across the corpus and builds a directed graph with resolved and unresolved link tracking.

**Storage:** `.graph_store/nodes.json`, `.graph_store/edges.json`, `.graph_store/unresolved_links.json`, `.graph_store/components.json`, `.graph_store/summary.json`, `.graph_store/graph_report.md`.

**Rebuild command:**
```bash
/home/martin/.venvs/emerauld/bin/python3 build_wikilink_graph.py
```

**Current state (as of commit 96e6487):** 901 nodes, 8672 edges. Zero-orphan rule enforced.

> [!warning] Contradiction detected
> As of 2026-06-29, `.graph_store/summary.json` reports **908 nodes, 9067 edges** (built 2026-06-27) — not 901/8672. The architecture note captured the state at commit 96e6487; the graph was rebuilt after that commit as new notes were added. Trust `summary.json` for live count; trust this note for the design description.

**Trade-off:** No LLM; deterministic; fast; captures explicit human-authored links only. Does not surface semantic relationships not expressed as wikilinks.

---

## Choosing a retrieval layer

| Query type | Best layer |
|------------|-----------|
| "Find notes about X" | Layer 1 (vsearch.py) |
| "What relationships exist between X and Y?" | Layer 2 (query.py) |
| "What notes link to X?" | Layer 3 (.graph_store) or Obsidian backlinks |
| "Which notes are orphans?" | Layer 3 (graph_report.md) |

## Related

- [[Architecture - EMERAULD Scripts - Overview]]
- [[Architecture - EMERAULD Scripts - Key Decisions]]
- [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]

<!-- @generated:end -->
