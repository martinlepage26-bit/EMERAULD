---
type: raw-source
title: Structure Check
aliases:
- raw/D-drive-scan-2026-05-12/elemental-agents/validation/01-structure-check
tags:
- raw
- agents
- intake
- raw-source
- d-drive-scan-2026-05-12
- maxdepth
- elemental
- find
- readme
- color-lime
status: preserved
created: '2026-05-12'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/D-drive-scan-2026-05-12/elemental-agents/validation/01-structure-check.md
backlink_count: 1
backlinks:
- '[[wiki/Manuscript Pipeline MOC]]'
---

# Structure Check

See also [[Manuscript Pipeline MOC]].
## Required counts

- `agents/`: 10 markdown files
- `orchestration/`: 6 markdown files
- `examples/`: 6 markdown files
- `validation/`: 3 markdown files
- Framework root: `README.md`

## Commands

```bash
find elemental-agents -type f | sort
find elemental-agents/agents -maxdepth 1 -type f -name '*.md' | wc -l
find elemental-agents/orchestration -maxdepth 1 -type f -name '*.md' | wc -l
find elemental-agents/examples -maxdepth 1 -type f -name '*.md' | wc -l
find elemental-agents/validation -maxdepth 1 -type f -name '*.md' | wc -l
```

## Pass criteria

All counts match required values and README exists.
