---
type: wiki
aliases:
  - Trismégiste operator state
  - Operator state (Trismégiste)
tags: [agent, trismegiste, operator, continuity, state]
status: active
created: 2026-05-06
updated: 2026-05-06
source_of_truth:
  - /home/cerebrhoe/trismegiste-state.md
raw_capture:
  - raw sources/2026-05-06_trismegiste-operator-state.md
---

# Trismégiste — Operator State

## Summary

This note ingests the operator-continuity state file that Trismégiste reads at session start and updates at session close.

- **Source of truth (outside vault):** `/home/cerebrhoe/trismegiste-state.md`
- **Vault capture:** `raw sources/2026-05-06_trismegiste-operator-state.md`

Use this note as the vault-side entrypoint; use the raw capture when provenance or exact wording matters.

## How it relates to EMERAULD

- `session-state.md` is the vault persistence layer for current work.
- The operator state file is *operator continuity* (Trismégiste’s own “self state”) and can mention cross-project threads that may not yet be fully reflected in the vault graph.

## Related

- [[Trismégiste — Personal AI Assistant]]
- [[ROOK — Session Boundary Model]]
- [[Second Self System — Identity Kernel and Agent Routing Architecture]]

