---
type: raw-source
title: example_wiki_note
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/vault-product-scaffold/example_wiki_note.md
---

# Auth Migration — Firebase to Supabase

> Delete this file after you've seen how wiki notes work.

**Status:** Planning
**Project:** [[hub_project_template]]
**People:** [[hub_person_template]]

---

## Context

The team is evaluating a migration from Firebase Auth to Supabase Auth. Primary drivers: cost, session token flexibility, and alignment with the existing Postgres stack.

## Key Decisions

- Session token format needs to match the current JWT structure.
- 30-day rollover window is the hard constraint — no user should be logged out during migration.
- Jake owns the migration checklist (due Friday).

## Open Questions

- How do we handle users with Firebase-only OAuth providers?
- Do we run both auth systems in parallel during rollover, or cut over?

## Links

- Source: synthesized from [[_example_raw_note]]
- Related: [[hub_project_template]]
