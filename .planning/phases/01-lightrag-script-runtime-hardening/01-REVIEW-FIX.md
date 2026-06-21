---
phase: "01"
name: "LightRAG Script Runtime Hardening"
created: 2026-04-23
updated: 2026-04-23
status: fixed
review_source: ".planning/phases/01-lightrag-script-runtime-hardening/01-REVIEW.md"
---

# Phase 1 Review Fix

## Applied Fixes

- `scripts/ingest.py`
  Added `note_id()` so LightRAG ingest IDs are derived from the path relative to `wiki/` instead of filename stem only.
  Wrapped both ingestion paths in `try/finally` so `finalize_storages()` always runs.

- `scripts/query.py`
  Wrapped query execution in `try/finally` so LightRAG storage cleanup runs even if `aquery()` raises.

- `scripts/lightrag_config.py`
  Hardened Claude OAuth loading by validating the presence of the credential block and access token.
  Changed refresh behavior to raise a clear error when the refresh call fails or returns no token.
  Persist refreshed credentials with explicit UTF-8 encoding and indentation.
  Replaced the mutable `history_messages` default with `None`.

## Verification

- `node "$HOME/.codex/get-shit-done/bin/gsd-tools.cjs" init phase-op 1`
  Confirmed local GSD bootstrap is recognized and Phase 1 resolves correctly.

- `python3 -m py_compile scripts/*.py`
  Confirmed the updated Python scripts compile cleanly.

## Notes

- No git commit was created in this pass.
  The repo already had unrelated local edits in `AGENTS.md`, `session-state.md`, and an untracked `.claude/` directory, so this run stayed additive and uncommitted.

## Related

- [[Governance and PHAROS MOC]]
- [[Events]]
