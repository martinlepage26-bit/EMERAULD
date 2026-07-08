---
type: wiki
title: Portfolio Restructuring Review — March 2026
aliases:
- PORTFOLIO_REVIEW_MEMO_2026-03-14
- Portfolio review memo March 2026
- Portfolio restructuring adversarial review
- wiki/Portfolio Restructuring Review — March 2026
tags:
- project-decision
- portfolio
- active-constraints
- adversarial-review
- govern-ai
- governess
- lotus
- wiki
- portfolio-restructuring-review-march-2026-md
- ownership
- sort
- caller
- color-purple
status: active
created: '2026-05-03'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Portfolio Restructuring Review — March 2026.md
backlink_count: 13
backlinks:
- '[[wiki/CODEX HANDOFF — 2026-05-03 Trismégiste Keystone Cycle]]'
- '[[wiki/Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation]]'
- '[[wiki/Dr. Sort and LOTUS Ownership Decision — March 2026]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/LOTUS Model and Agency]]'
- '[[memory/daily/2026-06-22]]'
- '[[memory/daily/2026-06-23]]'
- '[[memory/daily/2026-06-24]]'
- '[[memory/daily/2026-06-25]]'
- '[[memory/daily/2026-06-26]]'
- '[[memory/daily/2026-06-27]]'
- '[[projects/AurorA — Fisher King Project State]]'
- '[[projects/COMPASSai — Fisher King Project State]]'
---

# Portfolio Restructuring Review — March 2026

## Summary

Adversarial review of the March 14, 2026 portfolio restructuring package. Verdict: accepted with reservations — a valid stop-gate but not a clean authorization basis for execution. Contains active constraints still in force, including the govern-ai rename block, PHAROS lotus_dr_sort quarantine, and the Governess non-quarantine rule. Links to [[Dr. Sort and LOTUS Ownership Decision — March 2026]] as the primary decision record reviewed here, and feeds into ongoing work in [[Governance and PHAROS MOC]].

## Context

Raw source: `raw sources/PORTFOLIO_REVIEW_MEMO_2026-03-14.md`. Produced 2026-03-14 as adversarial review of the portfolio restructuring package (audit + registry + execution memo + dependency maps + disposition decisions). Active constraints confirmed still open as of 2026-05-03 — the missing evidence listed below has not been resolved.

## Active Do-Not-Do-Yet List

- **Do not** rename or remove the `govern-ai` repo path, Pages project, worker, preview host, or remote
- **Do not** treat PHAROS `lotus_dr_sort` residue as safe to delete (see [[Dr. Sort and LOTUS Ownership Decision — March 2026]])
- **Do not** convert current PHAROS operational ownership into long-term canonical publication/editorial ownership
- **Do not** present AurorA or CompassAI frontend trees as runnable standalone apps
- **Do not** quarantine or archive Governess backend or desktop on absence-of-proof alone

## Missing Evidence (Unresolved)

1. Caller map for publication/editorial surfaces
2. Caller map for `Governess/server.py`
3. Deployment-specific `MONGO_URL` / `DB_NAME` map
4. File-level delta adjudication for divergent LOTUS residue files (`lotus_core.py`, `lotus_app.py`, `dr_sort_academic_helper.py`)
5. External Pages/worker/DNS/remote inventory for govern-ai cutover work

## Governess Runtime Evidence

A local stack pass via `/home/cerebrhoe/repo-hosting` confirmed Governess is locally runnable with completed seeding (publications, FAQ, services). Log evidence at `/home/cerebrhoe/repo-hosting/logs/governess.log` (2026-03-14). This improves runtime confidence but does not resolve ownership, caller, or external deploy questions.

## Key Corrections Applied During Review

- Removed unsupported bibliography-content drift language (compared files matched after CR normalization)
- Narrowed DB/env wording to avoid conflating code defaults with deployed database identity
- Distinguished dormant PHAROS publication source residue from default runtime behavior (route-level blocks + backend fail-closed gating)
- Limited AurorA/CompassAI overstatement risk to stale summary wording and test artifacts, not current repo READMEs

## Related
- [[Dr. Sort and LOTUS Ownership Decision — March 2026]] — primary decision record reviewed here
- [[LOTUS Model — Agency and Social Positioning]] — LOTUS ownership context
- [[LOTUS Model and Agency]] — topic index
- [[PHAROS Commercial Strategy]] — portfolio context
- [[Governance and PHAROS MOC]] — primary index
