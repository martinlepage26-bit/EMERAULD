---
type: inbox-routing
title: Inbox — Routing Rules
tags:
- inbox-routing
- inbox
- destination
- clips
- templates
- drops
status: active
created: '2026-06-29'
updated: '2026-06-29'
vault_area: Inbox
canonical_path: Inbox/README.md
backlink_count: 1
backlinks:
- '[[index]]'
---

# Inbox — Routing Rules

All new captures land here first. Nothing stays in Inbox permanently.

## Routing decision tree

| Note is about… | Move to |
|----------------|---------|
| A project with a deliverable and deadline | `projects/` |
| An ongoing responsibility (PHAROS ops, Lavoie, writing practice) | `Areas/<domain>/` |
| Reference material, a concept, a framework | `Resources/` |
| Finished work, old session state | `archive/` |

## What NOT to put in Inbox
- Notes you already know where they belong — route them directly.
- Templates — they live in `templates/`.
- Raw web clips — put those in `raw/` until processed.

## Agent rule
When an agent drops a new note and the destination is unclear, it writes here with `status: inbox`. A routing skill reads `status: inbox` and proposes a destination for human confirmation before moving.
