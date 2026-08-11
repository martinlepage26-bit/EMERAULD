# EMERAULD Vault — Frontmatter Schema

> **Status:** ACTIVE  
> **Owner:** Martin  
> **Created:** 2026-07-31  
> **Purpose:** Canonical frontmatter specification for all EMERAULD vault notes.  
> Enables automated classification, lifecycle tracking, and agent navigation.

---

## Core Fields (required on all non-index notes)

```yaml
---
title: "Human-readable title"
status: draft | active | superseded | archive
created: YYYY-MM-DD
modified: YYYY-MM-DD        # updated on every meaningful edit
area: governance | pharos | lavoie | personal | writing | research | health
---
```

### `status` values

| Value | Meaning | Navigation |
|---|---|---|
| `draft` | Work in progress — not stable | Included in active navigation |
| `active` | Current source of truth for this topic | Primary navigation |
| `superseded` | Replaced by another document | Points to canonical via `superseded_by` |
| `archive` | Retained for history, no longer navigated | Excluded from active indexes |

---

## Extended Fields (use when relevant)

```yaml
---
# Lifecycle
superseded_by: "[[path/to/canonical-note]]"   # if status: superseded
archived_date: YYYY-MM-DD                       # if status: archive
review_due: YYYY-MM-DD                          # for time-sensitive notes

# Classification
type: note | reference | template | log | spec | deliverable | agent-instructions
tags: [tag1, tag2]

# Project linkage
project: contremaitre | pharos | legipro | emerauld | personal
task_id: IF/task-XXXXX                          # Blackboard task if applicable

# Provenance
source: "URL or citation"                       # for reference notes
author: "name"                                  # for external content
canonical: true                                 # marks the single authoritative copy

# Agent
agent_maintained: true                          # set if an agent writes/updates this file
last_agent: "rook-XXXXXX"                      # callsign of last agent to edit
---
```

---

## Type Definitions

| `type` | Use for |
|---|---|
| `note` | General knowledge capture (default) |
| `reference` | Academic or external source stub |
| `template` | Obsidian note template |
| `log` | Session, scheduled, or event log |
| `spec` | Technical specification or architecture decision |
| `deliverable` | Client or public-facing output |
| `agent-instructions` | CLAUDE.md, AGENTS.md, agent operating rules |

---

## Minimal Valid Examples

### A knowledge note
```yaml
---
title: "Recursive Governance — Core Concepts"
status: active
created: 2026-07-15
modified: 2026-07-31
area: governance
type: note
---
```

### An academic reference stub
```yaml
---
title: "Foucault 1975 — Surveiller et punir"
status: active
created: 2026-06-01
modified: 2026-06-01
area: research
type: reference
source: "Gallimard, 1975"
author: "Michel Foucault"
---
```

### A superseded document
```yaml
---
title: "Old EMERAULD Operating Rules"
status: superseded
created: 2026-05-01
modified: 2026-07-30
superseded_by: "[[governance/vault-operating-rules]]"
---
```

---

## Enforcement Notes

- Files in `archive/`, `graphify-out/`, and `graph/` are **exempt** — they are generated or retired
- `references/` stubs use the minimal reference form above
- `templates/` files may omit `status` and `modified`
- Agents should set `agent_maintained: true` and `last_agent` on any file they update
- Files without frontmatter are treated as `status: draft` by convention

---

## Automated Classification Rules (for agent use)

```
IF modified < (today - 180 days) AND no open Blackboard task references this file:
  → propose status: superseded at next review

IF status == active AND superseded_by is set:
  → ERROR: inconsistent — resolve to superseded

IF canonical: true AND file count with same title > 1:
  → flag for manual deduplication review
```
