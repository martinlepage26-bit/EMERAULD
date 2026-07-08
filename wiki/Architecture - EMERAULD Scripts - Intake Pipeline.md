---
type: architecture-module
title: Architecture - EMERAULD Scripts - Intake Pipeline
aliases:
- EMERAULD intake pipeline
- wiki/Architecture - EMERAULD Scripts - Intake Pipeline
tags:
- architecture
- emerauld
- intake
- scripts
- raw-sources
- architecture-module
- wiki
- architecture-emerauld-scripts-intake-pipeline-md
- hardmove
- immutable
- library
- hardcoded
- color-lime
status: active
created: '2026-06-29'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Architecture - EMERAULD Scripts - Intake Pipeline.md
backlink_count: 8
backlinks:
- '[[wiki/Architecture - EMERAULD Scripts - Key Decisions]]'
- '[[wiki/Architecture - EMERAULD Scripts - Overview]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[index]]'
- '[[wiki/lightrag_config — EMERAULD Shared Config Module]]'
- '[[memory/agents/Events]]'
- '[[memory/daily/2026-06-29]]'
- '[[session-state]]'
scanned-commit: 96e6487
---

> For future Claude: Documents the source intake pipeline for [[EMERAULD]]: how external files move from `raw sources/` to `raw/` to `wiki/` and into the retrieval layers. Load this when ingesting new source material or when `verify_and_hardmove_to_raw.py` is mentioned. Critical bug: that script has a hardcoded WSL path that will silently fail on the current host.

<!-- @generated:start -->

## Summary

The intake pipeline moves source material from `raw sources/` (unsynthesized captures) through verification into `raw/` (immutable), then through human synthesis into `wiki/` notes that enter the [[Architecture - EMERAULD Scripts - Knowledge Layers]].

## Pipeline stages

```
External source / scan
        ↓
raw sources/       ← unsynthesized captures — NEVER delete or overwrite
        ↓  verify_and_hardmove_to_raw.py
raw/               ← verified, SHA-256 deduped, immutable
        ↓  manual synthesis (human or agent)
wiki/              ← durable linked knowledge notes
        ↓  embed.py + ingest.py + build_wikilink_graph.py
retrieval layers   ← searchable
```

## `verify_and_hardmove_to_raw.py`

**Purpose:** Fail-closed verifier + hard-move. Checks existence, readability, file type, size, and SHA-256 hash against a manifest. Non-duplicate, verified files are hard-moved (not copied) to `raw/`. Emits a JSON report.

**Invocation:**
```bash
python verify_and_hardmove_to_raw.py --source "<scan-label>" /path/to/file1 /path/to/file2
```

**Known bug (confidence: stated — observed in source):** `VAULT_ROOT` is hardcoded to `/mnt/c/users/softinfo/documents/emerauld` — the original WSL path on the previous machine. The current vault root is `/home/martin/EMERAULD`. This means `raw/` moves will silently target the wrong path unless the variable is patched. Fix: replace the hardcoded line with `VAULT_ROOT = resolve_vault_root()` from `lightrag_config`, matching the pattern every other script uses.

**Manifest:** `.raw/.intake-manifest.jsonl` — append-only JSONL log of all verified moves with UTC timestamp and SHA-256.

## `ingest.py`

**Purpose:** Async batch ingestion of wiki notes into LightRAG. Prepends each note's filename as context before ingestion. Uses `note_id()` (path relative to wiki root, no extension) as the stable document ID for deduplication on re-ingest.

**Batch size:** 20 notes per LightRAG call.

**`--changed` flag:** Processes only notes with `mtime` within the last 24 hours.

## Library-specific intake

`library_d_ingest.py` and `library_d_unreadable_ocr.py` handle a physical library scan corpus (`library_d_*`). These are separate from the main wiki intake and operate on a dedicated corpus directory. `library_d_unreadable_ocr.py` uses OCR to recover files that `markitdown` cannot parse.

## Raw source protection rule

Per `_CLAUDE.md`: `raw sources/` is NEVER overwritten, deleted, or modified. `raw/` files are immutable after hard-move. These are non-negotiable constraints — agents must not touch these directories except to read.

## Related

- [[Architecture - EMERAULD Scripts - Overview]]
- [[Architecture - EMERAULD Scripts - Knowledge Layers]]
- [[Architecture - EMERAULD Scripts - Key Decisions]]

<!-- @generated:end -->
