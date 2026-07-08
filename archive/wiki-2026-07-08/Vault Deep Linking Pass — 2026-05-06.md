---
type: wiki
title: Vault Deep Linking Pass — 2026-05-06
aliases:
- EMERAULD deep linking pass 2026-05-06
- Vault graph repair pass 2026-05-06
tags:
- vault-linking
- graph-maintenance
- obsidian
- backlinks
- retrieval
- archive
- vault-deep-linking-pass-2026-05-06-md
- orphan
- inbound
- loose
- anchored
- relinking
- color-teal
status: complete
created: '2026-05-06'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/Vault Deep Linking Pass — 2026-05-06.md
backlink_count: 10
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Home]]'
- '[[Areas/PHAROS/Obsidian Second Brain Product]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[archive/wiki-2026-07-08/Vault Cluster Pass — Trismégiste x Hermes (2026-05-06)]]'
- '[[archive/wiki-2026-07-08/Vault Delta Interconnectivity Atlas — 2026-05-06]]'
- '[[archive/wiki-2026-07-08/Vault Topic Coverage Matrix — 2026-05-06]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[wiki/archive/Governance Stress-Test Protocols Index]]'
- '[[projects/Second Brain — Fisher King Project State]]'
---

# Vault Deep Linking Pass — 2026-05-06

## Summary

Deep linking pass over the EMERAULD `wiki/` graph after the Phase 3A/3B/3C/3D relinking campaign and the HELIX/prospecting/skill notes added on 2026-05-06. This pass keeps the existing MOC/TOPIC architecture intact and adds missing high-value anchors for low-inbound notes, graph-maintenance records, and client/design notes.

Scope was intentionally conservative: no files moved, renamed, deleted, or merged. Raw sources were left untouched. The pass focused on durable wiki surfaces and canonical hubs.

## Graph Findings

- `wiki/` contained 411 Markdown notes at scan time.
- The graph already has a strong MOC/TOPIC architecture: [[Home]], [[Governance and PHAROS MOC]], [[Research and Papers MOC]], [[Writing and Novels MOC]], [[Personal and Projects MOC]], and 26 TOPIC hubs.
- Low-inbound notes were concentrated in three groups: graph-maintenance records, new 2026-05-06 operational notes, and one client-design lesson note.
- The Argus audit record is path-sensitive because the note path contains slash-separated segments: [[Argus Audit — Phase 3A-3B-3C-3D Relinking Campaign (2026-05-06)|Argus Audit — Phase 3A/3B/3C/3D Relinking Campaign]]. Link to it with the full path-aware wikilink instead of treating the title as a flat filename.

## Orphan Audit Follow-Up

Closer title/path-aware scan after the first relinking pass found **zero true wiki orphans**. The operator-visible Obsidian graph, however, includes the whole vault, not only `wiki/`. A full-vault scan found **1,156 true vault-level orphans** across raw sources, artifacts, runtime/agent folders, governance mirrors, memory files, and loose root notes.

To make the Obsidian graph honest without pretending raw captures are synthesized notes, this pass generated [[Orphan Index — Vault-Level Graph Repair 2026-05-06]] plus six category indexes under `wiki/orphan-index/`. These indexes create explicit inbound links to all vault-level orphans while preserving their status as raw/source/runtime/provenance artifacts.

Follow-up verification found 107 raw-source filenames with graph-hostile characters such as leading `#`, `##`, and `]`. These do not register cleanly through normal path wikilinks because Obsidian/link parsers treat `#` as a heading separator and `]` as link syntax. Those files received stable `orphan-raw-2026-05-06-###` aliases in frontmatter, and the raw-source orphan index now links through those aliases. Source bodies were not moved, renamed, deleted, or synthesized.

Final full-vault verification after index + alias repair: **0 true Obsidian-visible orphans** across 1,687 Markdown files. Many files remain low-inbound by design because raw/provenance/runtime artifacts are linked from generated indexes rather than conceptually integrated into MOCs.

## Dr. Sort Filename Normalization

Follow-up filename hygiene pass: [[Dr. Sort Filename Normalization — 2026-05-06]] records 524 Markdown notes renamed after the Dr. Sort pass duplicated source titles and extensions in filenames. Each renamed file keeps its original name and path in frontmatter provenance fields, and valid Obsidian wikilinks were updated after the rename.

Because some cleaned filenames still contain graph-hostile characters such as `#` or `]`, the pass also created [[archive/Orphan Index — Post Dr Sort Rename Residuals — 2026-05-06]] and alias-stamped the hostile residuals needed for Obsidian-visible inbound links.

The curated `wiki/` concern set was 17 low-inbound notes, all at one or two inbound anchors. These were classified as follows:

| Class | Notes | Action |
|---|---|---|
| Reusable operational knowledge | [[Sales Objection Handling — Diagnosing Fog Without Coercion]], [[Awesome Design Resources — Curated UI-UX Reference List]], [[Agatha Grant Post-Mortem — First Assessment]], [[D Library — Review Unreadable Cleanup (2026-05-04)]], [[Red Team Handbook — Offensive Security Reference]] | Added or reinforced hub/TOPIC anchors. |
| Research/corpus stubs | [[Glitching the Sacred]], [[Halberstam — The Queer Art of Failure (2011)]], [[Masculinités et ritualités — La magie chez les Radical Faeries]], [[Paper 25 — Pre-Draft Artifacts (Pharos Frame Capstone)]] | Added or reinforced Research, Academic Pipeline, Queer Theory, and PHAROS Scholarly anchors. |
| Governance/agent records | [[Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation (2026-04-18)]], [[Trismégiste Eval v2 — Argus Closure and Redesign (2026-05-05)]], governance-control checkpoint notes | Reinforced from HEPHAISTOS and controls hubs. |
| Provenance scan artifacts | [[Vault Linking Session Summary — 2026-05-01]], [[Vault Linking Session 2 Summary — 2026-05-01]], [[Vault Linking Scan — 2026-05-01, 15-XX (Loop Iteration 1)]] | Left lightly linked as historical scan/provenance artifacts. |
| Test stub | [[test]] | Left as explicit non-claim test stub; do not count as content-bearing orphan. |

## Full-Vault Orphan Indexes

- [[archive/Orphan Index — Raw Sources — 2026-05-06]] — 889 raw/clipping/inbox source notes.
- [[archive/Orphan Index — Artifacts And Archives — 2026-05-06]] — 88 artifact/archive notes.
- [[archive/Orphan Index — Runtime And Agents — 2026-05-06]] — 133 runtime, governance, agent, and planning notes.
- [[archive/Orphan Index — Operations And Misc — 2026-05-06]] — 37 memory, hub, template, and map notes.
- [[archive/Orphan Index — Root Loose Notes — 2026-05-06]] — 17 loose root notes.
- [[Workspace Cleanup Ledger — 2026-05-31]] — workspace cleanup and entropy-reduction ledger for the 2026-05-31 pass.

## Root Loose Outlier Follow-Up

Follow-up title-aware scan after the Desktop ingest found seven new true zero-degree root notes and a small set of one-inbound loose/stub notes. [[Root Loose Notes Cluster Map — 2026-05-06]] classifies them into HELIX protocol/prototype sources, PHAROS commercial offer scratchpads, writing-craft phrase-origin material, infrastructure/operator checklists, RIA provenance, and low-value empty board/test stubs.

This follow-up keeps the earlier non-destructive rule: no source note was moved, renamed, deleted, or merged. Content-bearing root notes now have semantic inbound links; durable interpretation still belongs in `wiki/` synthesis notes.

## Links Added This Pass

- [[Client Logo Strategy — Monogram Pivot and SMB Branding Lessons]] anchored from [[Personal and Projects MOC]], [[PHAROS Commercial Strategy]], and [[Obsidian Second Brain Product]] as a reusable SMB/client-delivery lesson.
- [[Argus Audit — Phase 3A-3B-3C-3D Relinking Campaign (2026-05-06)|Argus Audit — Phase 3A/3B/3C/3D Relinking Campaign]] anchored from [[Governance and PHAROS MOC]], [[HEPHAISTOS Agent Architecture]], and this pass record.
- [[CODEX HANDOFF — 2026-05-03 Trismégiste Keystone Cycle]] anchored from [[AI Infrastructure Stack]] and [[Personal and Projects MOC]] as an operator-continuity handoff.
- [[Vault Linking Gaps & Bridge Opportunities — 2026-05-01]], [[Vault Cluster Discovery and Linking Opportunities — 2026-05-01]], [[Vault Linking Session Summary — 2026-05-01]], [[Vault Linking Session 2 Summary — 2026-05-01]], and [[Vault Linking Scan — 2026-05-01, 15-XX (Loop Iteration 1)]] anchored from [[AI Infrastructure Stack]], [[Obsidian Second Brain Product]], [[Home]], and this note.
- [[HELIX Healthcare Prospect Deep Dive - Canada 2026-05-06]] and [[PHAROS Commercial Brief — Pre-Launch Draft (Q2 2026)]] anchored into [[PHAROS Commercial Strategy]], with the HELIX healthcare note also added to [[Governance and PHAROS MOC]].
- [[Root Loose Notes Cluster Map — 2026-05-06]] added as the semantic cluster surface for loose root outliers: HELIX raw/prototype captures, PHAROS offer scratchpads, phrase-origin material, infrastructure checklists, RIA provenance, and empty stubs.
- [[Peer Review — Recursive AI Governance as Executable Method (AI & Society)]] anchored into [[Research and Papers MOC]] and [[Governance and PHAROS MOC]] so revision work can find the blocker record from both scholarly and governance entrypoints.
- [[Regulatory Standards Reference Stack — Governance Controls Grounding]], [[Governance Controls — Phase 1 Completion Checklist]], and [[Governance Controls — Incident Response (Control Failure Procedures)]] reinforced inside [[Governance Controls and Mechanisms]].
- [[Literary References — Craft Guide]] anchored into [[Writing and Novels MOC]] under Publishing Work and Consultations.
- [[Agatha Grant Post-Mortem — First Assessment]], [[Awesome Design Resources — Curated UI-UX Reference List]], [[D Library — Review Unreadable Cleanup (2026-05-04)]], [[Red Team Handbook — Offensive Security Reference]], [[Sales Objection Handling — Diagnosing Fog Without Coercion]], [[Glitching the Sacred]], [[Halberstam — The Queer Art of Failure (2011)]], [[Masculinités et ritualités — La magie chez les Radical Faeries]], [[Paper 25 — Pre-Draft Artifacts (Pharos Frame Capstone)]], [[Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation (2026-04-18)]], and [[Trismégiste Eval v2 — Argus Closure and Redesign (2026-05-05)]] received closer low-inbound review and targeted hub reinforcement.

## Follow-Up Leads

- The empty test stub [[test]] should remain excluded from quality claims unless it becomes a real genealogy note.
- Empty Kanban/test stubs in the root-loose cluster should remain visible but not counted as knowledge assets unless the operator confirms they still serve a workflow.
- Several older low-inbound records are not urgent because they are narrow technical references or version genealogies already discoverable through their domain hub.
- A future pass could normalize path-sensitive slash titles, but that should be a separate operator-approved rename/move action.

## Related

- [[Home]]
- [[AI Infrastructure Stack]]
- [[Obsidian Second Brain Product]]
- [[HEPHAISTOS Agent Architecture]]
- [[Root Loose Notes Cluster Map — 2026-05-06]]
- [[VAULT ADDITIONS TRACKER]]
- [[Cookies]]
