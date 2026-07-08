---
id: raw_intake_dataset
type: Dataset
canonical_name: "raw/ intake lane"
aliases: []
status: active
confidence: high
sources: ['EMERAULD/CLAUDE.md', 'governance/hephaistos/AGENTS.md']
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
