---
type: Dataset
title: raw/ intake lane
tags:
- dataset
- graph
- nodes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/nodes/unmapped/raw_intake_dataset.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
id: raw_intake_dataset
canonical_name: raw/ intake lane
confidence: high
sources:
- EMERAULD/CLAUDE.md
- governance/hephaistos/AGENTS.md
created_from: graphify_pass
---

# raw/ intake lane

## Summary

Canonical intake lane for newly scanned and verified source files (hard-move destination). Distinct from the legacy `raw sources/` directory, which is preserved as-is and is not the default target for new scan runs.

## Known Relationships

### Incoming

- [[verify_and_hardmove_to_raw.py]] → writes → This Node

### Outgoing

(none)

## Related Files

- EMERAULD/CLAUDE.md
- governance/hephaistos/AGENTS.md

## Evidence

- "raw/ — canonical intake lane for newly scanned and verified source files (hard-move destination)" — EMERAULD/CLAUDE.md
- "hard-move verified source files into /mnt/c/users/softinfo/documents/emerauld/raw... raw sources/ remains legacy provenance storage and is not the default target for new scan runs unless Martin explicitly overrides." — governance/hephaistos/AGENTS.md

## Open Questions

- None identified in this pass. Added 2026-07-02 correcting a pass-1 error that conflated raw/ with raw sources/.
