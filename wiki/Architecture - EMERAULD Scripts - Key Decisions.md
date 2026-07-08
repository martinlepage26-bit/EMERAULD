---
type: adr
title: Architecture - EMERAULD Scripts - Key Decisions
aliases:
- EMERAULD scripts ADRs
- wiki/Architecture - EMERAULD Scripts - Key Decisions
tags:
- architecture
- adr
- emerauld
- scripts
- wiki
- architecture-emerauld-scripts-key-decisions-md
- lightrag
- evidenced
- embed
- config
- color-orange
status: active
created: '2026-06-29'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Architecture - EMERAULD Scripts - Key Decisions.md
backlink_count: 9
backlinks:
- '[[wiki/Architecture - EMERAULD Scripts - Intake Pipeline]]'
- '[[wiki/Architecture - EMERAULD Scripts - Knowledge Layers]]'
- '[[wiki/Architecture - EMERAULD Scripts - Overview]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[index]]'
- '[[wiki/lightrag_config — EMERAULD Shared Config Module]]'
- '[[memory/agents/Events]]'
- '[[memory/daily/2026-06-29]]'
- '[[session-state]]'
scanned-commit: 96e6487
---

> For future Claude: Architecture decision record for the [[EMERAULD]] scripts layer. Load this when evaluating a proposed change to any script, or when a script's behavior seems inconsistent with the rest of the system. Decisions 1–3 are confirmed (evidenced by code). Decisions 4–6 are inferred from structure (marked speculation).

<!-- @generated:start -->

## Decision 1 — Three parallel retrieval layers instead of one (confidence: stated)

**Context:** A knowledge vault needs fast lookup (for agent queries), entity-relationship queries (for synthesis), and structural link queries (for orphan detection and graph health).

**Decision:** Run three independent retrieval layers rather than one unified store: vector search, LightRAG semantic graph, and deterministic wikilink graph.

**Rationale evidenced in code:** Each layer has a separate store directory (`.vector_store/`, `.lightrag/storage/`, `.graph_store/`), separate rebuild commands, and separate output formats. `vsearch.py` explicitly documents "Build the store first with: python embed.py", confirming intentional separation.

**Consequence:** Retrieval is fast (vector) and rich (LightRAG) and structural (graph). Trade-off: the layers are not synchronized. A note added to `wiki/` is invisible to all three until each is rebuilt. This is an accepted operational cost — no auto-sync mechanism exists.

---

## Decision 2 — Local embeddings only, LLM only for LightRAG (confidence: stated)

**Context:** Vault ingest needs to work without network access. Embeddings run on every note; LLM calls run only for entity extraction.

**Decision:** `all-MiniLM-L6-v2` (sentence-transformers, 384-dim) for all vector embeddings — local, offline, free. LLM (`claude-haiku-4-5-20251001`) is called only for LightRAG ingest, where entity extraction justifies the cost and latency.

**Evidenced in:** `lightrag_config.py:resolve_embed_model_path()` — prefers HuggingFace local cache, with hub fallback. `embed.py` and `vsearch.py` call `get_embed_model()` only; never `llm_func()`.

---

## Decision 3 — `lightrag_config.py` as single shared config module (confidence: stated)

**Context:** Multiple scripts need the same vault root, embed model, and LLM function. Duplicating this across scripts creates drift.

**Decision:** One config module (`lightrag_config.py`) exports `VAULT_ROOT`, `get_embed_model()`, `llm_func()`, `embedding_func()`, and `make_rag()`. All scripts `import` from it via `sys.path.insert(0, str(Path(__file__).parent))`.

**Evidenced in:** 5 of 19 scripts have an explicit `from lightrag_config import ...` line. The pattern is the vault's equivalent of a shared constants file.

**Incomplete adoption:** `verify_and_hardmove_to_raw.py` has its own hardcoded `VAULT_ROOT = Path("/mnt/c/users/softinfo/documents/emerauld")` — the only script that did not adopt the shared pattern. This is the current known bug.

---

## Decision 4 — Fail-closed intake with SHA-256 deduplication (confidence: stated)

**Context:** Source files must not be silently duplicated or overwritten on re-ingest of the same scan.

**Decision:** `verify_and_hardmove_to_raw.py` computes SHA-256 on every candidate file and checks against a JSONL manifest before moving. Files with a matching hash are rejected as duplicates. The report distinguishes `verified` from `rejected` artifacts.

**Evidenced in:** `sha256_file()` function and `MANIFEST_PATH = DEFAULT_RAW_DIR / ".intake-manifest.jsonl"` in the script header.

---

## Decision 5 — File-based LightRAG storage (confidence: stated)

**Context:** A graph database would add operational complexity. The vault is a single-operator system.

**Decision:** LightRAG uses file-based storage (NetworkX graph, NanoVectorDB, JsonKV) under `.lightrag/storage/`. No database server required.

**Consequence:** Portable. No infra dependencies. Trade-off: not suitable for concurrent writes.

---

## Decision 6 — Rolling registers with line-threshold archiving (confidence: stated)

**Context:** Session registers (Journal, Decisions, Blockers, etc.) accumulate indefinitely and become slow for agents to read.

**Decision:** Each register has a line threshold (600 for session-state, 300 for others). `archive_register.py` rotates the file when the threshold is exceeded, moving old content to `archive/` with a dated filename and resetting the live file.

**Evidenced in:** `archive_register.py` `Register` dataclass with `threshold` field; 6 register definitions. Documented in vault `CLAUDE.md` session-close protocol.

---

## Open technical debt

| Item | Severity | Fix |
|------|----------|-----|
| `verify_and_hardmove_to_raw.py` hardcoded WSL path | High — silently uses wrong VAULT_ROOT | Replace with `resolve_vault_root()` from `lightrag_config` |
| Three layers require manual rebuild sync | Medium — notes invisible to search after creation | Add a `rebuild-all.sh` or `--changed` trigger in scheduled scripts |
| `ingest.py` 24h `--changed` window | Low — notes modified >24h ago after a gap won't be picked up | Use manifest-based change tracking like `embed.py` |

## Related

- [[Architecture - EMERAULD Scripts - Overview]]
- [[Architecture - EMERAULD Scripts - Knowledge Layers]]
- [[Architecture - EMERAULD Scripts - Intake Pipeline]]

<!-- @generated:end -->
