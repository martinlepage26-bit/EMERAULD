---
type: wiki
title: LightRAG — Graph-Based RAG System
aliases:
- LightRAG
- graph-based RAG
- HKUDS LightRAG
- wiki/LightRAG — Graph-Based RAG System
tags:
- ai-tooling
- retrieval
- knowledge-graph
- rag
- infrastructure
- wiki
- lightrag-graph-based-rag-system-md
- lightrag
- reranker
- wizard
- storage
- backend
- color-orange
status: active
created: '2026-04-16'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/LightRAG — Graph-Based RAG System.md
backlink_count: 14
backlinks:
- '[[.planning/ROADMAP]]'
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Desktop Obsidian and Personal Assistant Setup Logs — 2026-04-14]]'
- '[[wiki/GSD — Get Shit Done Context Engineering System]]'
- '[[wiki/GSD — Get-Shit-Done Claude Code System]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[wiki/Obsidian Agent Vault Launch — Commercial Skill]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/RAG-Anything — Multimodal RAG Framework]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[wiki/claude-mem — Persistent Memory Compression for Claude Code]]'
- '[[hephaistos/personal-assistant-agents/trismegiste/README]]'
- '[[memory/daily/2026-04-24]]'
---

# LightRAG — Graph-Based RAG System

## Summary

LightRAG (HKUDS/LightRAG, arXiv 2410.05779) is a graph-based Retrieval-Augmented Generation system that builds a knowledge graph from ingested documents and retrieves subgraphs per query rather than raw text chunks. It is the knowledge-graph backbone of the [[EMERAULD Second Brain — Project Context]] persistence stack, replacing naive chunk-based retrieval with coherent, relationship-aware context.

## Context

LightRAG is installed at `/home/cerebrhoe/.venvs/lightrag` and operates inside the [[EMERAULD Second Brain — Project Context]] vault at `/mnt/c/Users/softinfo/Documents/EMERAULD/`. It indexes all `wiki/` notes as a connected graph. Storage lives at `.lightrag/storage/` within the vault. The system is part of a two-layer persistence stack: LightRAG handles deep vault knowledge retrieval, while `session-state.md` handles session-level working memory. The [[GSD — Get Shit Done Context Engineering System]] and [[HEPHAISTOS]] governance work both benefit from structured retrieval over flat note search.

## Details

### What It Does

LightRAG extracts entities and relationships from documents, builds a knowledge graph, and retrieves subgraphs that are semantically and relationally relevant to a query. This produces more coherent answers than naive RAG because retrieved context respects entity relationships, not just keyword proximity.

### Installation

- Python 3.10+
- `pip install lightrag-hku`
- Installed in EMERAULD at: `/home/cerebrhoe/.venvs/lightrag`

### EMERAULD Commands

**Ingest changed wiki notes:**
```
cd /mnt/c/Users/softinfo/Documents/EMERAULD/scripts
/home/cerebrhoe/.venvs/lightrag/bin/python3.12 ingest.py --changed
```

**Full re-ingest:**
```
cd /mnt/c/Users/softinfo/Documents/EMERAULD/scripts
/home/cerebrhoe/.venvs/lightrag/bin/python3.12 ingest.py
```

**Query:**
```
cd /mnt/c/Users/softinfo/Documents/EMERAULD/scripts
/home/cerebrhoe/.venvs/lightrag/bin/python3.12 query.py "your question" --mode hybrid
```

### Query Modes (Cost Order, Low to High)

| Mode | Use Case |
|---|---|
| `local` | Specific entity lookup |
| `global` | Broad synthesis across the vault |
| `hybrid` | Default — best balance of precision and coverage |
| `naive` | Fallback chunk retrieval |
| `mix` | Combined strategy |

Prefer `local` for entity lookups, `hybrid` for most questions, `global` for broad synthesis.

### LLM and Stack Requirements

LightRAG makes heavier demands on the LLM than traditional RAG because it performs entity-relationship extraction during indexing.

- **LLM**: at least 32B parameters; context window 32KB minimum, 64KB recommended; avoid reasoning models during indexing; use a stronger model at query time than at indexing time
- **Embedding model**: must be chosen before indexing and held constant; changing it requires deleting and recreating vector tables; recommended: `BAAI/bge-m3` or `text-embedding-3-large`
- **Reranker**: significantly improves retrieval; enable `mix` mode when a reranker is active; recommended: `BAAI/bge-reranker-v2-m3` or Jina

### Storage Backends

| Backend | Notes |
|---|---|
| Local file store | Default for EMERAULD |
| PostgreSQL | All-in-one storage solution; vector dimension locked on table creation |
| MongoDB | All-in-one storage solution (added 2025) |
| Neo4j | Graph database backend |
| OpenSearch | Unified backend for all four storage types (added 2026) |

### Interactive Setup Wizard (2026)

LightRAG ships a `make`-based setup wizard that generates `.env` and `docker-compose.final.yml`:

```bash
make env-base           # Required: LLM, embedding, reranker
make env-storage        # Optional: storage backends
make env-server         # Optional: port, auth, SSL
make env-security-check # Audit current .env for security risks
```

Use `*-rewrite` variants to force-regenerate wizard-managed compose blocks. The wizard preserves unchanged blocks on re-run.

### Features Added Since Initial Release

| Date | Feature |
|---|---|
| 2026-03 | OpenSearch backend; Docker setup wizard |
| 2025-11 | RAGAS evaluation + Langfuse tracing; API returns retrieved contexts |
| 2025-10 | Large-scale dataset scalability improvements |
| 2025-09 | Better KG extraction for open-source LLMs (e.g., Qwen3-30B-A3B) |
| 2025-08 | Reranker support (now default `mix` mode); document deletion with KG regeneration |
| 2025-06 | [[RAG-Anything — Multimodal RAG Framework]] integration for multimodal docs |
| 2025-03 | Citation/source attribution |
| 2025-02 | MongoDB backend; PostgreSQL backend |
| 2024-11 | WebUI for insert/query/visualize; Neo4j backend |

### Ecosystem

LightRAG is the core of a broader HKUDS retrieval stack:

| Project | Role |
|---|---|
| [[RAG-Anything — Multimodal RAG Framework]] | Multimodal extension (PDFs, images, Office, tables, formulas) |
| VideoRAG | Extreme long-context video RAG |
| MiniRAG | Minimal RAG with small models |

### Performance vs Alternatives

LightRAG consistently outperforms NaiveRAG, RQ-RAG, HyDE, and GraphRAG across agriculture, CS, legal, and mixed domains on comprehensiveness, diversity, empowerment, and overall quality (pairwise evaluation). Largest gains in legal domain (~85% win rate vs NaiveRAG).

### Source Repository

- HKUDS/LightRAG on GitHub
- Paper: arXiv 2410.05779

## Key Ideas

- Graph retrieval produces more coherent context than chunk retrieval because relationships between entities are preserved.
- The `--changed` flag on ingest makes incremental updates efficient — only new or modified wiki notes are re-indexed.
- Query mode selection is a cost/coverage trade-off: `local` is cheap and precise; `global` is expensive and broad; `hybrid` is the safe default.
- [[RAG-Anything — Multimodal RAG Framework]] is built on top of LightRAG and extends it to non-text inputs.

## Open Questions

- Does the RAGAS eval integration work with the local storage backend, or does it require a hosted backend?
- Is Langfuse tracing configured for EMERAULD, or available but unused?
- At what vault size does full re-ingest become prohibitively slow?

## Sources

- `raw sources/lightrag-2026-04-16.md`
- arXiv 2410.05779

## Related

- [[RAG-Anything — Multimodal RAG Framework]]
- [[claude-mem — Persistent Memory Compression for Claude Code]]
- [[EMERAULD Second Brain — Project Context]]
- [[Recursive Continuity Without Memory — AI Identity Across Sessions]]
- [[Plugin Recommendations]]
- [[ROADMAP]]
- [[README]]
