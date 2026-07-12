---
type: note
title: Quarantine Boundary
tags:
- quarantine
- vault
- boundary
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _QUARANTINE
canonical_path: _QUARANTINE/README.md
---

# Quarantine Boundary

`_QUARANTINE/` is the recovery-first lane for vault material that is:

- likely low-value
- structurally uncertain
- probably removable later
- not safe to delete immediately

Rules for this lane:

- quarantine before delete
- preserve provenance
- record the reason for each move in `_AUDIT/CHANGE_MANIFEST.md` or a later manifest
- do not use this lane as a silent trash can

This pass establishes the boundary but does not perform a broad quarantine move.
