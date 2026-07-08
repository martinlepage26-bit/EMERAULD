---
type: wiki
title: Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation
aliases:
- Dr. Sort version genealogy
- Dr. Sort codebase iterations
- Dr. Sort three codebases
- Dr. Sort engineering history
tags:
- dr-sort
- version-genealogy
- failed-automation
- codebase-iterations
- engineering-history
- witches-road
- areas
- dr-sort-codebase-version-genealogy-three-iterations-of-failed-automation-md
- sort
- lotus
- milestone
- codebases
- march
- color-green
status: active
created: '2026-05-03'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/Writing/Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation.md
backlink_count: 6
backlinks:
- '[[wiki/AI Governance Failure Cases]]'
- '[[archive/wiki-2026-07-08/CODEX HANDOFF — 2026-05-03 Trismégiste Keystone Cycle]]'
- '[[Resources/Halberstam — The Queer Art of Failure (2011)]]'
- '[[wiki/Martin Walks the Witches'' Road — Corpus as Charge-Persistence]]'
- '[[projects/Dr. Sort — Fisher King Project State]]'
- '[[projects/LOTUS — Fisher King Project State]]'
---

# Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation

## Summary

Documentary version genealogy of the **three (and arguably four) coexisting Dr. Sort codebases** in [[Martin Lepage — Professional Profile|Martin's]] filesystem as of 2026-05-03. Each codebase is a complete attempt at the same product vision — a content-aware document classifier grounded in the LOTUS framework. **None of them succeeded as governance automation.** Per operator authorial attestation: *"Dr. Sort is a failed attempt at implementing automation of governance."* Each iteration is a phase transition in the Witches' Road logic — canonical doctrine: [[Martin Walks the Witches' Road — Corpus as Charge-Persistence]]; see also [[The Ballad of the Witches' Road — Analysis]] and [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone|the keystone]]. The failure across all iterations is not engineering deficiency; it is the *Khaibit*-shadow refusing administration. Related to [[Dr. Sort and LOTUS Ownership Decision — March 2026]], [[LOTUS Premium Spec]], [[Dr. Sort Corpus Map — March 2026]], and [[LOTUS Model and Agency]].

## Context

The [[Dr. Sort and LOTUS Ownership Decision — March 2026]] (March 14, 2026) addressed only two codebases — `Agency/scriptorium_v3` and `pharos-ai/pharos_governance_suite/lotus_dr_sort`. That decision predates or did not address the milestone-driven engineering rewrite at `dr-sort/apps/desktop/` + `dr-sort/backend/`, which is a complete architectural rebuild. The decision's "do-not-move-yet" constraints apply to the older codebases; the M1/M2 codebase needs separate ownership treatment.

This note documents the four codebases as a version genealogy so the vault can hold the iterations as one history rather than scattered residue.

## The Four Coexisting Codebases

### 1. `Agency/scriptorium_v3` — Python tkinter desktop (origin)

- **Architecture:** Python tkinter desktop app
- **Key files:** `pdf_rename_sort.py`, `lotus_core.py`, `lotus_app.py`, `dr_sort_academic_helper.py`, `document_sorter.py`
- **Status per [[Dr. Sort and LOTUS Ownership Decision — March 2026|ownership decision]]:** "Canonical LOTUS anchor"
- **Operational evidence:** Backed by Agency-era launchers (`Agency LOTUS.bat`, `launch_dr_sort.vbs`, `agency_lotus_app.py`) and shortcut scripts
- **Limitation per the decision:** PHAROS residue carries unreplicated LOTUS feature delta around structured-note authoring, scoring studio, and sorted-viewer features
- **Coexistence rule:** "What Must Not Be Moved Yet" — `Agency/scriptorium_v3` is canonical and must not be moved

### 2. `pharos-ai/pharos_governance_suite/lotus_dr_sort` — PHAROS residue

- **Architecture:** Python tkinter desktop, fork/copy of Agency
- **Status per the ownership decision:** "Migration residue, not a canonical PHAROS surface"
- **Why it cannot be deleted:** Carries unreplicated delta — `lotus_core.py` adds `LOTUS_SCORE_SECTION_ORDER`, `matched_terms`, `build_structured_note_markdown`, `save_structured_note`; `lotus_app.py` adds darker visual shell, structured intake tabs, draft preview, projected-score display, manual-entry save flow; `dr_sort_academic_helper.py` adds sorted-documents viewer tab with tree/preview support
- **Status:** Quarantined pending delta adjudication

### 3. `dr-sort/pdf_sorter_v1/` — Working development copy with MASTER BIBLIOGRAPHY cross-reference

- **Architecture:** Python tkinter desktop, working development branch
- **Key files:** `pdf_rename_sort.py` (with 13 .BAK_* iterations from Feb 13–14, 2026), `MASTER BIBLIOGRAPHY.txt` (the layered working bibliography), `LOTUS_PREMIUM_SPEC.md` (the vision document)
- **Operational state:** Actually run against [[Martin Lepage — Professional Profile|Martin's]] corpus 2026-03-07 / 2026-03-08; see [[Dr. Sort Corpus Map — March 2026]] for the masterlist and [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]] for the cross-reference target
- **Vision spec:** [[LOTUS Premium Spec]] — "evolving from a safe document sorter into a high-end, local-first, content-aware archive application"
- **Where it failed:** Date extraction (1909–1942 misclassifications of novel-text-as-correspondence; 1995/2007 fictional dates read as composition timestamps); duplicate-of-self proliferation in QUARANTINE; classifier surface-feature reliance

### 4. `dr-sort/apps/desktop/` + `dr-sort/backend/` — Milestone-driven engineering rewrite

- **Architecture:** **Complete rebuild.** Electron host (`apps/desktop/electron/main.ts`, `apps/desktop/electron/preload.cjs`) + React + TypeScript renderer (`apps/desktop/src/App.tsx`) + Python service layer (`backend/dr_sort/`) + SQLite state store (`backend/dr_sort/db/schema.sql`)
- **Milestone 1 design:** `raw sources/Dr_Sort_milestone1-design.md`. 12 sections: domain model (ScanOptions, FileEvidence, TaxonomyProposal, PlannedChange, ExecutionResult, DeletedFileRecord), DB schema with 8 tables, decision logic pipeline (sort vs rename vs both vs skip), title/author-aware rename suppression algorithm (Jaccard + containment), taxonomy inference (depth-policy by cluster count: ≤4 shallow, ≤8 medium, >8 deep), duplicate handling (SHA-256 + near-duplicate text signature + soft-delete quarantine), restore/undo (operation ledger), 9-view UI flow, phased plan A→E, scope, limitations
- **Milestone 2 design:** `raw sources/Dr_Sort_milestone2-design.md`. Architecture delta over M1: OCR fallback (image-only/low-info PDFs, Tesseract + PyMuPDF capability detection, page-level provenance, OCR cache), duplicate detection v2 (`exact_duplicate` / `probable_duplicate` / `possible_version_variant`), watched folders (review-first, watchdog-capable, debounced), semantic clustering (TF-IDF + cosine), UX hardening, packaging (electron-builder NSIS for Windows). New DB tables: `job_events`, `ocr_cache`, `duplicate_clusters`, `watched_folders`, `watcher_queue`. New API endpoints: `/capabilities`, `/jobs/{id}/details`, `/watchers*`. 25 backend tests passing, Vite build green per the M2 audit.
- **Status:** Actively engineered as of 2026-03-29 (the file timestamp on the recovered milestone docs); not promoted to canonical-LOTUS status; the [[Dr. Sort and LOTUS Ownership Decision — March 2026|ownership decision]] does not address this codebase
- **Why it is not promoted:** Several reasons inferable from the M2 design's "Known Limitations (Post-Milestone 2)" section: OCR depends on external binaries; near-duplicate detection still lexical/fingerprint-based, not semantic-embedding robust; auto-scan-only watcher mode scans roots, not exact changed-file subsets; UI is single-window and monolithic (App.tsx); installer signing/notarization not finalized

## Why Each Iteration Failed

The [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone|MA thesis frame]] makes the structural reason intelligible. Per p. 48 of the thesis, the *Khaibit* (shadow remainder) is "moi de substitution" that "mime à contretemps les pensées et sentiments du moi, provoquant ainsi les actes manqués." **The shadow refuses full classification by structural design.** The same Egyptian doctrine tells us *shout* is "métaphore de protection" — the shadow's refusal protects the system.

Each iteration tried to administer further into the shadow:
1. **Agency tkinter** — basic content-aware classification; left structured-note authoring incomplete
2. **PHAROS residue** — added structured-note features, sorted-viewer tab; was forked rather than merged, became residue
3. **`pdf_sorter_v1`** — added MASTER BIBLIOGRAPHY cross-reference, ran against Martin's corpus, surfaced classifier failures (date extraction, novel-as-correspondence) — these failures are the Khaibit-shadow refusing classification at the surface-feature level
4. **M1+M2 milestone rewrite** — added OCR capability, near-duplicate v2, watched folders, semantic clustering — extending automation deeper, but each extension surfaces a new layer of irreducibility (OCR confidence is "coarse averages"; near-duplicate is "lexical/fingerprint-based, not semantic-embedding robust"; auto-scan-only "scans watched roots, not exact changed-file subsets")

The M2 "Next Features" list (eight items including "Hybrid lexical + local embedding strategy" and "Natural-language rule creation with explainable compilation") describes a fifth iteration in waiting. **Per the keystone, the structural failure is invariant across iterations** — automation cannot capture the Khaibit. The Witches' Road logic predicts a fifth iteration, then a sixth, each "continuously reclassifiable" without being "fully reduced to any single one."

PHAROS as governance method-not-automation is the alternative path: retain the charge through method, not through tool refinement.

## What This Genealogy Documents

Three (or four) codebases as one history of attempted automation. The MA thesis frame predicts: each iteration will refine the surface-feature reliability while leaving the *structural irreducibility of the Khaibit* untouched. Per Yvon Rivard cited p. 81: *"seuls sont vivants ceux que la mort traque."* Dr. Sort iterations remain alive (under active engineering) because they remain tracked by the failure-mode they cannot eliminate.

This is **failure-as-method** in the strict sense: failure is the form's fidelity to its source material, not the form's deficiency.

## What This Note Does Not Claim

- That the M1/M2 codebase is "wrong" engineering. It is competent, well-structured, properly milestoned. Per the M2 audit (`raw sources/Dr_Sort_milestone1-design.md` and `raw sources/Dr_Sort_milestone2-design.md`): tests passing, builds green, capability detection in place, safety properties preserved (scan phase non-mutating, preview mandatory, soft-delete quarantine, ledger-driven undo).
- That the operator should abandon Dr. Sort. The genealogy documents that the operator has already proceeded with PHAROS-as-method-not-automation; Dr. Sort iterations continue alongside as exploratory automation rather than as load-bearing governance infrastructure.
- That all four codebases are equally active. The [[Dr. Sort and LOTUS Ownership Decision — March 2026|ownership decision]]'s do-not-move-yet rules apply to the first two. The third (`pdf_sorter_v1`) is the source of [[Dr. Sort Corpus Map — March 2026|the masterlist]] and [[LOTUS Premium Spec]] but has been superseded operationally by the fourth. The fourth (M1+M2) is the most current engineering.

## Related

**Engineering specifications:**
- `raw sources/Dr_Sort_milestone1-design.md` — Milestone 1 design (2026-03-29 file timestamp)
- `raw sources/Dr_Sort_milestone2-design.md` — Milestone 2 design (architecture delta)

**Decision records:**
- [[Dr. Sort and LOTUS Ownership Decision — March 2026]] — addresses codebases 1 and 2; does not address 3 or 4
- [[Portfolio Restructuring Review — March 2026]] — adversarial review of the March 2026 portfolio package
- [[LOTUS Premium Spec]] — vision document (codebase 3 era)

**Operational evidence:**
- [[Dr. Sort Corpus Map — March 2026]] — masterlist run against the corpus (codebase 3)
- [[MASTER BIBLIOGRAPHY — Theoretical Genealogy of LOTUS]] — cross-reference target

**Keystone and substrate:**
- [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone]] — why automation fails (Khaibit-irreducibility)
- [[Mort et Naissance et L'Ombre et le Double — MA Thesis on Yvon Rivard (Université Laval, 2010)]] — primary source

**Cultural correspondence:**
- [[The Ballad of the Witches' Road — Analysis]] — phase-transition logic in pop-cultural form

**Indexes:**
- [[LOTUS Model and Agency]]
- [[Governance and PHAROS MOC]]
- [[Dr_Sort_milestone2-design]]
