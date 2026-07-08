---
type: project-state
title: Workspace Cleanup Ledger — 2026-05-31
tags:
- project
- project-state
- archive
- uploads
- workspaces
- martin
- queering
- removed
- wiki-2026-07-08
status: active
created: '2026-05-31'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/Workspace Cleanup Ledger — 2026-05-31.md
backlink_count: 3
backlinks:
- '[[wiki/Argus Audit — Phase 3A-3B-3C-3D Relinking Campaign (2026-05-06)]]'
- '[[wiki/VAULT ADDITIONS TRACKER]]'
- '[[archive/wiki-2026-07-08/Vault Deep Linking Pass — 2026-05-06]]'
---

# Workspace Cleanup Ledger — 2026-05-31

## Scope

Linux-side cleanup performed from `/home/martin` after Martin explicitly approved moving beyond triage into high-confidence cleanup.

Blackboard task: `IF-3781`

## Completed

### PHAROS safety repair

- Restored `/home/martin/workspaces/PHAROS-SUITE/frontend/scripts/tracker-gate.sh` from `HEAD`.
- Removed the accidental credential assignment from `/home/martin/workspaces/PHAROS-SUITE/.gitignore`.
- Verified both files have no diff after repair.

### EMERAULD vault case duplicate consolidation

Canonical files kept:

- `/home/martin/EMERAULD/_vault/AGENTS.md`
- `/home/martin/EMERAULD/_vault/skill.md`

Duplicate exact copies removed:

- `/home/martin/EMERAULD/_vault/Agents.md`
- `/home/martin/EMERAULD/_vault/Skill.md`

Links normalized before deletion:

- `[[Agents]]` -> `[[AGENTS]]`
- `[[Skill]]` -> `[[skill]]`

Verification: no remaining `[[Agents]]` or `[[Skill]]` links found under `/home/martin/EMERAULD`.

### MRW paper duplicate cleanup

Vault canonicals kept:

- `/home/martin/EMERAULD/wiki/Queering Neo-Pagan Magic — FINAL FINAL PAPER.md`
- `/home/martin/EMERAULD/assets/manuscripts/queering-neo-pagan-magic-mrw-2026/Lepage--Queering Pagan Magic--FINAL FINAL PAPER.docx`
- `/home/martin/EMERAULD/assets/manuscripts/queering-neo-pagan-magic-mrw-2026/Lepage--Queering Pagan Magic--MRW cover page.docx`

Exact duplicate upload copies removed:

- `/home/martin/_uploads/Lepage--Queering Pagan Magic--FINAL FINAL PAPER.md`
- `/home/martin/_uploads/Lepage--Queering Pagan Magic--FINAL FINAL PAPER.docx`
- `/home/martin/_uploads/Lepage--Queering Pagan Magic--MRW cover page.docx`

Temporary extraction workdir removed:

- `/home/martin/_uploads/lepage_final_work`

### MASTER REFERENCE SAFE archive duplicate cleanup

Kept newest timestamped copy in each exact-hash group:

- `/home/martin/_uploads/MASTER REFERENCE SAFE/archive/2026-03/MASTER REFERENCE LIST pre-clean 20260331-001329.txt`
- `/home/martin/_uploads/MASTER REFERENCE SAFE/archive/2026-03/MASTER REFERENCE LIST pre-clean 20260331-001256.txt`

Older exact duplicates removed:

- `/home/martin/_uploads/MASTER REFERENCE SAFE/archive/2026-03/MASTER REFERENCE LIST pre-clean 20260331-001306.txt`
- `/home/martin/_uploads/MASTER REFERENCE SAFE/archive/2026-03/MASTER REFERENCE LIST pre-clean 20260331-001326.txt`
- `/home/martin/_uploads/MASTER REFERENCE SAFE/archive/2026-03/MASTER REFERENCE LIST pre-clean 20260331-001212.txt`

### Upload pollution removed

- Removed byte-identical duplicate `/home/martin/_uploads/compress-without-opacity_manuscript.docx`.
- Kept `/home/martin/_uploads/CompressOpaq_FINAL_CITED.docx`.
- Removed zero-byte `/home/martin/_uploads/DG_Extermination_4500px.svg`.
- Removed generated virtualenv `/home/martin/_uploads/pdf_repair_venv`.

### PHAROS generated artifact cleanup

Removed regenerable generated folders:

- `/home/martin/workspaces/PHAROS-SUITE/compassai/frontend/node_modules`
- `/home/martin/workspaces/PHAROS-SUITE/compassai/frontend/dist`
- `/home/martin/workspaces/PHAROS-SUITE/pharos_integrations/pharos_suite.egg-info`

Removed cache-only folders under PHAROS and uploads:

- `__pycache__`
- `.pytest_cache`
- `.mypy_cache`
- `.ruff_cache`
- `.vite`

### Version stack consolidation by newest mtime

Rule applied after Martin clarified the canonical policy: newest modified/opened file is canonical; older version-stack members are archived unless timestamps are genuinely ambiguous.

MRW paper:

- Canonical kept: `/home/martin/EMERAULD/wiki/Queering Neo-Pagan Magic — FINAL FINAL PAPER.md`
- Canonical kept: `/home/martin/EMERAULD/assets/manuscripts/queering-neo-pagan-magic-mrw-2026/Lepage--Queering Pagan Magic--FINAL FINAL PAPER.docx`
- Archived older source uploads under `/home/martin/EMERAULD/assets/manuscripts/queering-neo-pagan-magic-mrw-2026/_archive_superseded_2026-05-31/source_uploads/`:
  - `Lepage--Queering Pagan Magic--MRW final.docx`
  - `Lepage--Queering Pagan Magic--MRW revision.md`
  - `Lepage--Queering Pagan Magic--citation revision.docx`

Rivard2026:

- Canonical kept: `/home/martin/workspaces/Publications/Papers and Chapters/Rivard2026/Pourquoi rêver encore-@nalyses-REWRITE.md` (`2026-05-25 23:16`)
- Archived older stack member: `/home/martin/workspaces/Publications/Papers and Chapters/Rivard2026/_archive_superseded_2026-05-31/Pourquoi rêver encore-@nalyses-REV.docx` (`2026-05-25 19:23`)

Provisional Arbitration Charter v1.1:

- Canonical kept: `/home/martin/EMERAULD/raw sources/provisional-arbitration-charter-v1.1.md`
- Archived older exact duplicates under `/home/martin/EMERAULD/raw sources/_archive_superseded_2026-05-31/provisional-arbitration-charter-v1.1/`.

## Deferred

These were identified but deliberately not deleted in this pass:

- OCR and unreadable-source clusters under `/home/martin/EMERAULD/raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/`. Many have `(2)`, `(3)`, or repeated names, but content may represent OCR variants or source provenance.
- `/home/martin/workspaces/Publications` manuscript versions outside the Rivard stack. AgathaSC currently has only one Linux-side file, so no archive action was needed there.
- `/home/martin/workspaces/martinlepage26-bit.github.io/docs`. Current deployment uses `dist`, but inventory scripts still write to `docs`, so this needs a separate site-output decision.
- Windows-side targets named by Claude/Martin (`E:\` root, Documents root, Dossier Brevet Equinoxe, Séries Articles Pharos) are not mounted in this Linux session and still need the Windows-side scan.

## Verification Snapshot

- `/home/martin/_uploads`: `16M` after cleanup.
- `/home/martin/workspaces/PHAROS-SUITE`: `2.1G` after generated artifact/cache cleanup.
- No remaining removed duplicate paths found in the cleanup verification scan.
- PHAROS remaining `git status` entries are unrelated WIP and were not modified by this cleanup beyond generated/untracked artifacts.
