---
type: raw-source
title: Execution Loop
aliases:
- raw/D-drive-scan-2026-05-12/elemental-agents/orchestration/04-execution-loop
tags:
- raw
- agents
- intake
- raw-source
- d-drive-scan-2026-05-12
- slice
- defects
- unrelated
- verifiable
- loop
- color-lime
status: preserved
created: '2026-05-12'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/D-drive-scan-2026-05-12/elemental-agents/orchestration/04-execution-loop.md
backlink_count: 1
backlinks:
- '[[raw/D-drive-scan-2026-05-12/elemental-agents/agents/06-test-operator]]'
---

# Execution Loop

See also [[06-test-operator]].
## Goal

Drive implementation in short, verifiable cycles.

## Loop

1. Execute the next change slice.
2. Run immediate checks for that slice.
3. Record evidence and outcomes.
4. Resolve defects before next slice.

## Rules

- Do not batch unrelated changes.
- Do not proceed with unresolved critical defects.
- Keep command and file logs current.
