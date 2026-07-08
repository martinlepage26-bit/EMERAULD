---
type: domain
title: Domain — Projects
tags:
- projects
- blocked
- archived
- project
- yyyy
status: active
created: '2026-06-29'
updated: '2026-06-29'
vault_area: projects
canonical_path: projects/DOMAIN.md
backlink_count: 2
backlinks:
- '[[Logs/2026-06-29]]'
- '[[index]]'
---

# Domain — Projects

## What this domain is
A project has a **deliverable**, a **deadline**, and an **end state**. When it's done, it archives. Ongoing responsibilities without an end belong in `Areas/`.

## Where things live
- All project notes: `projects/`
- Archived projects: `archive/` (keep the note, set `status: archived`)
- Project state files follow the naming convention: `<ProductName> — Fisher King Project State.md`

## Status vocabulary (canonical — use only these values)

| Status | Meaning |
|--------|---------|
| `draft` | Conceived, not yet started |
| `in-progress` | Actively being worked |
| `blocked` | Waiting on something external (specify in note body) |
| `on-ice` | Intentionally paused, will resume |
| `complete` | Deliverable shipped |
| `archived` | Done and filed; no further action |

**The status field drives everything.** Bases views group by it. Agents read it to find what to work on next. Never use free-text status values outside this list.

## Field schema for project notes

```yaml
---
type: project
title: '<Project Name> — Fisher King Project State'
status: <draft|in-progress|blocked|on-ice|complete|archived>
priority: <high|medium|low>
created: '<YYYY-MM-DD>'
updated: '<YYYY-MM-DD>'
vault_area: projects
canonical_path: projects/<filename>.md
tags:
  - project
  - <product-tag>
deadline: '<YYYY-MM-DD>'       # omit if unknown
blocked_by: '<reason>'         # only if status: blocked
---
```

## Migration note (2026-06-29)
Existing project notes use `status: active`. The new canonical values replace `active` with `in-progress`. Update on next touch — no bulk migration needed.

## Agent rules
- Read this file before writing any note into `projects/`.
- Never invent a status value not in the table above.
- When setting `status: blocked`, always fill `blocked_by:` in frontmatter.
- On project completion, set `status: complete`, then move to `archive/` and set `status: archived`.
