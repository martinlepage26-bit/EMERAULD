---
type: project-planning
title: Phase 1 Review
aliases:
- .planning/phases/01-lightrag-script-runtime-hardening/01-REVIEW
tags:
- planning
- project-planning
- phases
- opportunistically
- lightrag
- scripts
- storages
- info
- color-orange
status: issues_found
created: '2026-04-23'
updated: '2026-06-26'
vault_area: .planning
canonical_path: .planning/phases/01-lightrag-script-runtime-hardening/01-REVIEW.md
backlink_count: 3
backlinks:
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[wiki/Writing and Novels MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
phase: '01'
name: LightRAG Script Runtime Hardening
depth: standard
files_reviewed_list:
- scripts/ingest.py
- scripts/query.py
- scripts/lightrag_config.py
---

# Phase 1 Review

## Findings

### Warning

1. `scripts/ingest.py` initializes LightRAG storages but only finalizes them on the happy path. Any exception during batch insert leaves cleanup to process exit instead of an explicit shutdown path.

2. `scripts/ingest.py` uses `Path.stem` as the LightRAG document ID. Notes with the same filename in different folders collide, which risks overwriting or aliasing ingested content.

3. `scripts/query.py` does not finalize storages when `rag.aquery()` raises, so query failures can leave the runtime in an indeterminate state.

4. `scripts/lightrag_config.py` refreshes Claude OAuth credentials opportunistically but falls through to the prior token even if refresh fails. When the on-disk token is expired, that behavior turns a refresh problem into a later opaque API failure.

### Info

1. `scripts/lightrag_config.py` uses a mutable default for `history_messages`, which is easy to fix while touching the same call path.

## Fix Scope

Apply Critical + Warning findings now. Info finding can be fixed opportunistically if the surrounding function is already changing.

## Related

- [[Writing and Novels MOC]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
