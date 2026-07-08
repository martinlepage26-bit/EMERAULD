---
type: artifact
title: Auth Migration - Firebase to Supabase
aliases:
- artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/wiki/_example_wiki_note
tags:
- artifact
- agents
- artifacts
- marketplace
- firebase
- auth
- rollover
- supabase
- migration
- color-green
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/wiki/_example_wiki_note.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

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
