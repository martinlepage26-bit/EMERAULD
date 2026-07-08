---
type: Dataset
title: session-state.md + memory/agents/ registers
tags:
- dataset
- graph
- nodes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/nodes/unmapped/session_state_registers_dataset.md
backlink_count: 1
backlinks:
- '[[graph/nodes/unmapped/archive_register_py]]'
id: session_state_registers_dataset
canonical_name: session-state.md + memory/agents/ registers
confidence: high
sources:
- EMERAULD/CLAUDE.md
created_from: graphify_pass
---

# session-state.md + memory/agents/ registers

## Summary

Vault persistence layer: active threads, decisions, blockers. 600-line archive threshold for session-state.md; 300-line threshold for memory/agents/ registers.

## Known Relationships

### Incoming

- [[Trismégiste]] → writes → This Node
- [[archive_register.py]] → transforms → This Node

### Outgoing

- (none found in this pass)

## Related Files

- EMERAULD/CLAUDE.md

## Evidence

- "Thresholds: session-state.md → 600 lines. All memory/agents/ registers → 300 lines." — EMERAULD/CLAUDE.md

## Open Questions

- None identified in this pass.
