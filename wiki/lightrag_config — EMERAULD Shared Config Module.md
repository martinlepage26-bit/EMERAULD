---
type: wiki
title: lightrag_config — EMERAULD Shared Config Module
aliases:
- lightrag_config
- lightrag_config.py
tags:
- architecture
- emerauld
- scripts
- vector-search
- lightrag
- wiki
- root
- func
- embedding
status: active
created: '2026-06-29'
updated: '2026-06-29'
vault_area: wiki
canonical_path: wiki/lightrag_config — EMERAULD Shared Config Module.md
backlink_count: 7
backlinks:
- '[[wiki/Architecture - EMERAULD Scripts - Knowledge Layers]]'
- '[[wiki/Architecture - EMERAULD Scripts - Overview]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

> For future Claude: `lightrag_config.py` is the single shared configuration module for all [[EMERAULD]] scripts. It provides vault root resolution, the local embedding model, the LLM function, and the `make_rag()` factory. Load this note before modifying any script in `scripts/` — every significant change to the vault's retrieval stack starts here.

## Summary

`lightrag_config.py` is the single source of configuration truth for the [[Architecture - EMERAULD Scripts - Overview]]. It exports `VAULT_ROOT`, `get_embed_model()`, `llm_func()`, `embedding_func()`, and `make_rag()`. Five of the nineteen scripts in `scripts/` import from it directly via `sys.path.insert(0, str(Path(__file__).parent))`.

## Context

The module was introduced to prevent configuration drift across scripts that all need the same vault root, embedding model, and LLM function. As documented in [[Architecture - EMERAULD Scripts - Key Decisions]] (Decision 3), this is a confirmed design decision evidenced by the shared import pattern across the codebase.

The one known exception is `verify_and_hardmove_to_raw.py`, which has a hardcoded `VAULT_ROOT = Path("/mnt/c/users/softinfo/documents/emerauld")` — the old WSL path. This is the only script that did not adopt the shared pattern and represents a high-severity bug.

## Key exports

| Export | Type | Purpose |
|--------|------|---------|
| `VAULT_ROOT` | `Path` | Resolved vault root — `EMERAULD_VAULT_ROOT` env var → git-relative fallback |
| `resolve_vault_root()` | function | The resolution logic, importable separately |
| `get_embed_model()` | function | Returns loaded `all-MiniLM-L6-v2` (384-dim, fully local) |
| `llm_func()` | async function | Calls `claude-haiku-4-5-20251001`; OpenRouter fallback |
| `embedding_func()` | async function | LightRAG-compatible embedding wrapper |
| `make_rag()` | function | Instantiates a `LightRAG` object with all config wired in |

## Vault root resolution rule

Resolution order: `EMERAULD_VAULT_ROOT` env var → git-relative discovery. This means the vault root is portable across machines as long as the env var is set or git is available. Set `EMERAULD_VAULT_ROOT=/home/martin/EMERAULD` to be explicit.

## Known issue

`verify_and_hardmove_to_raw.py` bypasses this module entirely. Fix: replace its hardcoded `VAULT_ROOT` line with `from lightrag_config import resolve_vault_root; VAULT_ROOT = resolve_vault_root()`. No other changes needed — the rest of the script is correct.

## Related

- [[Architecture - EMERAULD Scripts - Overview]]
- [[Architecture - EMERAULD Scripts - Knowledge Layers]]
- [[Architecture - EMERAULD Scripts - Key Decisions]]
- [[Architecture - EMERAULD Scripts - Intake Pipeline]]
