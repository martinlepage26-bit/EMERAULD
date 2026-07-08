---
type: memory-register
title: project_aurorai_repo_split
aliases:
- project_aurorai_repo_split
- memory/local-session/project_aurorai_repo_split
tags:
- memory
- aurora
- ai
- memory-register
- local-session
- suite
- aurorai
- repos
- module
- color-green
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: memory
canonical_path: memory/local-session/project_aurorai_repo_split.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[wiki/archive/Orphan Index — Operations And Misc — 2026-05-06]]'
- '[[memory/local-session/feedback_aurorai_spelling]]'
---

See also [[Control Protocols MOC]].
See also [[feedback_aurorai_spelling]].
---
name: AurorA repo split — active module vs standalone snapshot
description: The active AurorA test suite lives in pharos-suite module, not the standalone AurorA repo; standalone has no test script
type: project
originSessionId: efdf373b-e124-4522-b435-bde821210106
---
The active AurorA module is at `PHAROS-SUITE/repos/pharos-suite/aurorai/`, not `PHAROS-SUITE/repos/AurorA/`.

**Why:** `PHAROS-SUITE/repos/AurorA/frontend/package.json` has no `test` script. The integrated module at `pharos-suite/aurorai/` is the one that matches documented commands and the PHAROS portal caveat.

**Verified passing (2026-04-11):**
- `pytest aurorai/tests` from `PHAROS-SUITE/repos/pharos-suite` → 20 passed in 25.33s
- `npm test` from `PHAROS-SUITE/repos/pharos-suite/aurorai/` (vitest) → 4 files, 37 tests in 2.60s

**How to apply:** Always run AurorA tests from `pharos-suite/aurorai/`, not the standalone snapshot. Do not expect a `test` script in `PHAROS-SUITE/repos/AurorA/frontend/package.json`.
