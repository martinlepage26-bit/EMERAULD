# Auth Migration - Firebase to Supabase

> Delete this file after you've seen how wiki notes work.

**Status:** Planning
**Project:** [[Example Project Hub]]
**People:** [[Example Person Hub]]

---

## Context

The team is evaluating a migration from Firebase Auth to Supabase Auth. Primary drivers: cost, session token flexibility, and alignment with the existing Postgres stack.

## Key Decisions

- Session token format needs to match the current JWT structure.
- 30-day rollover window is the hard constraint. No user should be logged out during migration.
- Jake owns the migration checklist (due Friday).

## Open Questions

- How do we handle users with Firebase-only OAuth providers?
- Do we run both auth systems in parallel during rollover, or cut over?

## Links

- Source: synthesized from [[_example_raw_note]]
- Related: [[Example Project Hub]]
