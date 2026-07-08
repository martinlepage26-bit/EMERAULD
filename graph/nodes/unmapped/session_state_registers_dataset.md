---
id: session_state_registers_dataset
type: Dataset
canonical_name: "session-state.md + memory/agents/ registers"
aliases: []
status: active
confidence: high
sources: ['EMERAULD/CLAUDE.md']
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
