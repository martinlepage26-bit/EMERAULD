---
type: audit-doc
title: ARCHIVE CANDIDATES
tags:
- audit
- vault
- archive
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _AUDIT
canonical_path: _AUDIT/ARCHIVE_CANDIDATES.md
---

# ARCHIVE CANDIDATES

This file lists **likely archive or quarantine candidates**, not automatic moves.

## High-confidence navigation demotion candidates

| Path or class | Why it is a candidate | Suggested treatment |
|---|---|---|
| `graphify-out/` root generated runtime files | high file count, low human browsing value, machine-generated | remove from human-first navigation; consider archive/quarantine by batch later |
| `wiki/GRAPHIFY-OUT MOC.md` | generated directory MOC with weak retrieval value | stop surfacing from home; archive later if unused |
| `wiki/RAW MOC.md` | generated directory MOC, low-value human hub | stop surfacing from home; leave searchable |
| `wiki/RESOURCES MOC.md` | useful references exist in `Resources/`; this MOC is a weak legacy wrapper | keep searchable, demote from primary navigation |

## Historical but useful

| Path or class | Why it is a candidate | Suggested treatment |
|---|---|---|
| `archive/wiki-2026-07-08/` | already functioning as historical retention for pre-migration material | keep in `archive/` |
| `archive/session-state/` | historical continuity evidence | keep in `archive/` |
| `artifacts/stale-projects-*.md` | generated maintenance reports, time-bounded value | searchable artifact lane; archive if they accumulate further |

## Quarantine-first candidates

| Path or class | Why it is a candidate | Suggested treatment |
|---|---|---|
| `graphify-out/converted/AI_Hallucination_Risk_Scorecard_v1_e7e4f5c1.md` | lone editable Markdown file in graphify output lacking frontmatter | quarantine before deletion if later judged unnecessary |
| residual generated runtime manifests in `graphify-out/` root | probably useful only during graph-generation sessions | `_QUARANTINE/graphify-out/` in a later pass if no active dependency is confirmed |
| malformed or low-value recovery surfaces in `wiki/` created by orphan repair | some are structurally valid but poor human interfaces | review one by one; quarantine if superseded |

## Not archive candidates in this pass

- `projects/` as a whole
- `raw sources/` as a whole
- `memory/`
- `Areas/`
- embedded repos

Those surfaces create noise, but they also still carry live value. They should be demoted before being moved.
