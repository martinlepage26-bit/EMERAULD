---
type: wiki
title: Dr. Sort and LOTUS Ownership Decision — March 2026
aliases:
- DR_SORT_OWNERSHIP_AND_EXTRACTION_DECISION
- Dr. Sort extraction decision
- LOTUS ownership decision
- wiki/Dr. Sort and LOTUS Ownership Decision — March 2026
tags:
- project-decision
- lotus
- dr-sort
- agency-repo
- pharos-residue
- active-constraints
- wiki
- dr-sort-and-lotus-ownership-decision-march-2026-md
- sort
- agency
- march
- restructuring
- color-orange
status: active
created: '2026-05-03'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Dr. Sort and LOTUS Ownership Decision — March 2026.md
backlink_count: 18
backlinks:
- '[[archive/wiki-2026-07-08/CODEX HANDOFF — 2026-05-03 Trismégiste Keystone Cycle]]'
- '[[Areas/Writing/Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation]]'
- '[[wiki/Dr. Sort Corpus Map — March 2026]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/LOTUS Agency Scoring App GPT — ChatGPT Product Specification]]'
- '[[wiki/LOTUS Model and Agency]]'
- '[[wiki/LOTUS Model — Agency and Social Positioning]]'
- '[[wiki/LOTUS Premium Spec]]'
- '[[wiki/MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]]'
- '[[wiki/Mythocritique to PHAROS — The 2010 Master''s Thesis as Methodological Keystone]]'
- '[[wiki/Portfolio Restructuring Review — March 2026]]'
- '[[memory/daily/2026-06-22]]'
- '[[memory/daily/2026-06-23]]'
- '[[memory/daily/2026-06-24]]'
- '[[memory/daily/2026-06-25]]'
- '[[memory/daily/2026-06-26]]'
- '[[memory/daily/2026-06-27]]'
- '[[projects/Dr. Sort — Fisher King Project State]]'
---

# Dr. Sort and LOTUS Ownership Decision — March 2026

## Summary

Decision record establishing that canonical LOTUS and Dr. Sort ownership lives in `Agency/scriptorium_v3`, not in PHAROS. The PHAROS `lotus_dr_sort` residue is quarantined — not delete-ready — because it carries unreplicated LOTUS feature delta. This record does **not** authorize extraction, deletion, or archive execution. Related to [[LOTUS Model — Agency and Social Positioning]], [[Portfolio Restructuring Review — March 2026]], and the PHAROS project boundary work in [[Governance and PHAROS MOC]].

## Context

Raw source: `raw sources/DR_SORT_OWNERSHIP_AND_EXTRACTION_DECISION.md` (2026-03-14). Produced as part of the March portfolio restructuring package reviewed in [[Portfolio Restructuring Review — March 2026]]. Status per that review: "accept with edits." Active constraints still in force as of 2026-05-03.

## Active Constraints (Do Not Proceed Without)

- `Agency/scriptorium_v3` is canonical LOTUS anchor — do not move or extract
- `pharos-ai/pharos_governance_suite/lotus_dr_sort` is residue/quarantine — **not delete-ready**
- PHAROS residue carries unreplicated delta that Agency does not fully carry:
  - `lotus_core.py` — adds `LOTUS_SCORE_SECTION_ORDER`, `matched_terms`, `build_structured_note_markdown`, `save_structured_note`
  - `lotus_app.py` — darker shell, structured intake tabs, draft preview, projected-score display, manual-entry save flow
  - `dr_sort_academic_helper.py` — sorted-documents viewer tab with tree/preview, post-sort refresh
- MASTER BIBLIOGRAPHY.txt has byte-level variance between copies (CR-normalized content matched; no substantive drift proven)

## Missing Evidence Blocking Extraction

1. File-level delta disposition for all three divergent LOTUS residue files
2. Decision: merge PHAROS delta into Agency, or explicitly reject and archive
3. Only after (2): decide whether Dr. Sort stays in Agency, extracts, or archives

## Dependency Map (Key Points)

- `dr_sort_academic_helper.py` imports both `lotus_core` and `document_sorter`
- `lotus_core.py` imports `document_sorter`; `lotus_app.py` imports `lotus_core`
- LOTUS and Dr. Sort cross-launch through sibling-file assumptions
- Both share `LOTUS_UPLOADS` root and `dr_sort_feed`
- `Agency/pyproject.toml` exposes `lotus = flowerapp.main:main` (legacy CLI surface)

## Validation Required Before Any Move

- LOTUS desktop launch works
- Dr. Sort launch works
- Cross-launch between the two works
- `dr_sort_feed` lands in expected LOTUS root
- `flowerapp` console-script behavior resolves

## Related

- [[LOTUS Model — Agency and Social Positioning]] — LOTUS theoretical and product context
- [[LOTUS Premium Spec]] — product spec for `LOTUS | Dr. Sort-Academic Helper`
- [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]] — theoretical lineage of LOTUS
- [[Dr. Sort Corpus Map — March 2026]] — operational evidence of the tool's classification at scale
- [[LOTUS Model and Agency]] — topic index
- [[Bonded Intelligence Under Constraint — The LOTUS Processor Framework]] — LOTUS scientific grounding
- [[Portfolio Restructuring Review — March 2026]] — adversarial review of this decision record
- [[Governance and PHAROS MOC]] — primary index
- [[DR_SORT_OWNERSHIP_AND_EXTRACTION_DECISION]]
