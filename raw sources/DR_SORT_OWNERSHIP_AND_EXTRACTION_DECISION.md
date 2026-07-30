---
type: source
aliases: []
tags: [raw-source, orphan-repair, ai-governance, docsort]
status: raw
created: 2026-07-10
updated: 2026-07-10
source: "DR_SORT_OWNERSHIP_AND_EXTRACTION_DECISION"
---
# Dr. Sort Ownership And Extraction Decision

Date: 2026-03-14

## 1. Canonical Owner Summary

- `Agency` is the canonical LOTUS repo.
- `Agency/scriptorium_v3` remains the canonical LOTUS desktop anchor and compatibility path.
- `flowerapp`, `scriptorium_v3`, and Agency-era launchers are compatibility surfaces that must stay stable for now.
- Dr. Sort is real extraction debt, but it is not justified to restore it into PHAROS.
- `pharos-ai/pharos_governance_suite/lotus_dr_sort` is migration residue, not a canonical PHAROS surface.

Important qualifier:

- PHAROS residue still contains LOTUS delta that Agency does not fully carry yet, so ownership is clear but full feature reconciliation is not.

## 2. File-Level Inventory

### Agency canonical tree

- sorter core:
  - `Agency/scriptorium_v3/document_sorter.py`
  - `Agency/scriptorium_v3/dr_sort_academic_helper.py`
  - `Agency/scriptorium_v3/run_document_sorter.ps1`
  - `Agency/scriptorium_v3/pdf_rename_sort.py`
- LOTUS core and app:
  - `Agency/scriptorium_v3/lotus_core.py`
  - `Agency/scriptorium_v3/lotus_app.py`
  - `Agency/scriptorium_v3/LOTUS_UPLOADS/README.lotus`
  - `Agency/scriptorium_v3/LOTUS_PREMIUM_SPEC.md`
  - `Agency/scriptorium_v3/MASTER BIBLIOGRAPHY.txt`
  - `Agency/scriptorium_v3/lotus_rules.example.txt`
- compatibility shims:
  - `Agency/scriptorium_v3/agency_lotus_app.py`
  - `Agency/scriptorium_v3/agency_lotus_core.py`
  - `Agency/scriptorium_v3/Agency LOTUS.bat`
  - `Agency/scriptorium_v3/launch_agency_lotus.vbs`
  - `Agency/scriptorium_v3/create_agency_lotus_desktop_shortcuts.ps1`
- package and legacy CLI surface:
  - `Agency/pyproject.toml`
  - `Agency/src/flowerapp/*`

### PHAROS residue tree

- duplicated desktop bundle:
  - `pharos-ai/pharos_governance_suite/lotus_dr_sort/document_sorter.py`
  - `pharos-ai/pharos_governance_suite/lotus_dr_sort/dr_sort_academic_helper.py`
  - `pharos-ai/pharos_governance_suite/lotus_dr_sort/lotus_core.py`
  - `pharos-ai/pharos_governance_suite/lotus_dr_sort/lotus_app.py`
- residue-only scaffolding and assets:
  - `requirements.txt`
  - `capture_app_window.ps1`
  - `capture_tk_window.py`
  - `LOTUS_preview.png`
  - `Dr_Sort_preview.png`
  - `INBOX/.gitkeep`
  - `LOTUS_UPLOADS/.gitkeep`

## 3. Dependency Map

### Imports

- `dr_sort_academic_helper.py` imports both `lotus_core` and `document_sorter`.
- `lotus_core.py` imports `document_sorter`.
- `lotus_app.py` imports `lotus_core`.

This proves the current desktop behavior is tightly coupled inside `scriptorium_v3`.

### Launchers

The launcher chain is path-bound and explicit:

- shortcut script -> `.vbs` launcher -> `.bat` launcher -> Python app

Both Dr. Sort and LOTUS launch each other through sibling-file assumptions.

### Upload roots and note roots

- LOTUS uses `script_dir/LOTUS_UPLOADS`
- Dr. Sort also points at the same LOTUS root
- Dr. Sort can write a `dr_sort_feed` into LOTUS storage

### Scoring logic

- LOTUS scoring is local and shared through `score_lotus_text`
- Dr. Sort consumes the same LOTUS library and feed root

### CLI entrypoints

- `Agency/pyproject.toml` still exposes `lotus = flowerapp.main:main`
- `flowerapp` is a legacy compatibility package and is not the same thing as the desktop LOTUS + Dr. Sort tree

### Package manifest assumptions

- package name must remain `flowerapp`
- `scriptorium_v3` path remains part of local workflow compatibility
- desktop scripts assume local relative folders for reports, quarantine, and outputs

### Local user workflow assumptions

- default roots are path-based under `scriptorium_v3`
- code still supports browse-based workflow even if a default inbox is absent on disk
- operator workflow is therefore not proven dead; it remains unknown rather than inactive

## 4. Residue Map Under pharos-ai

- `pharos_governance_suite/lotus_dr_sort` is a residue copy of the Agency desktop bundle.
- Some files are byte-identical across Agency and PHAROS residue:
  - `document_sorter.py`
  - `LOTUS.bat`
  - `Dr. Sort-Academic Helper.bat`
  - `launch_lotus.vbs`
  - `launch_dr_sort.vbs`
  - `create_lotus_desktop_shortcuts.ps1`
  - `run_document_sorter.ps1`
- Some files diverge and therefore block broad deletion:
  - `lotus_core.py`
  - `lotus_app.py`
  - `dr_sort_academic_helper.py`
- `MASTER BIBLIOGRAPHY.txt` differs at the byte level between the two trees, but CR-normalized content matched in the reviewed scope, so no substantive bibliography-content drift is proven
- Agency-only files in the compared desktop tree:
  - `README.md`
  - `Agency LOTUS.bat`
  - `agency_lotus_app.py`
  - `agency_lotus_core.py`
  - `create_agency_lotus_desktop_shortcuts.ps1`
  - `launch_agency_lotus.vbs`
  - `pdf_rename_sort.py`
  - `LOTUS_UPLOADS/README.lotus`
- PHAROS-only files in the residue tree:
  - `capture_app_window.ps1`
  - `capture_tk_window.py`
  - `Dr_Sort_preview.png`
  - `LOTUS_preview.png`
  - `INBOX/`
  - `LOTUS_UPLOADS/.gitkeep`
  - `requirements.txt`

File-level delta categories from the compared source files:

- `lotus_core.py`
  - PHAROS residue adds `LOTUS_SCORE_SECTION_ORDER`
  - PHAROS residue returns `matched_terms` from scoring
  - PHAROS residue adds `build_structured_note_markdown(...)`
  - PHAROS residue adds `save_structured_note(...)`
  - feed tag text differs from Agency in the Dr. Sort feed export
- `lotus_app.py`
  - PHAROS residue carries a darker visual shell and larger window/layout changes
  - PHAROS residue adds structured intake tabs and section help text
  - PHAROS residue adds draft preview, projected-score display, and manual-entry save flow into `LOTUS_UPLOADS/manual_entries`
  - PHAROS residue tracks note rows by item id rather than simple list index alone
- `dr_sort_academic_helper.py`
  - PHAROS residue carries a darker visual shell and revised summary/status language
  - PHAROS residue adds a sorted-documents viewer tab with tree/preview support
  - PHAROS residue refreshes the sorted viewer after sort, scan reset, and undo flows
  - PHAROS residue widens LOTUS score language to include operational signals in UI copy
- `MASTER BIBLIOGRAPHY.txt`
  - byte-level variance exists between the two copies
  - CR-normalized content matched in the reviewed scope
  - no substantive bibliography-content delta is currently proven

Most important residue finding:

- PHAROS contains LOTUS feature delta around structured-note authoring, scoring-studio/manual-entry behavior, and some Dr. Sort UI differences.

## 5. What Can Stay Where It Is for Now

- `Agency/scriptorium_v3`
- `Agency/src/flowerapp`
- Agency LOTUS and Dr. Sort side by side
- Agency-era launcher and shortcut shims
- PHAROS residue as read-only quarantine/reference until delta is adjudicated

## 6. What Would Need Shims If Extracted

- cross-launch shims between `LOTUS` and `Dr. Sort-Academic Helper`
- shared-root shim for `LOTUS_UPLOADS` and `dr_sort_feed`
- relative path shims for:
  - `SORTED_LIBRARY_V2`
  - `QUARANTINE/V2`
  - `REPORTS_V2`
- asset and rule-path shims for:
  - `MASTER BIBLIOGRAPHY.txt`
  - `lotus_rules.example.txt`
  - OCR lookup assumptions
- wrapper or merge plan for PHAROS-only structured-note authoring and sorted-viewer features
- decision on whether PHAROS-only capture utilities and preview assets are operational tooling, documentation assets, or disposable residue
- if PHAROS-only LOTUS delta is kept, Agency needs a merge or wrapper before residue can be removed

## 7. What Must Not Be Moved Yet

- `Agency/scriptorium_v3`
- `Agency/src/flowerapp`
- `Agency/scriptorium_v3/Agency LOTUS.bat`
- Agency compatibility launchers and shortcut scripts
- `document_sorter.py` by itself
- PHAROS `lotus_core.py` or `lotus_app.py` before delta ownership is decided
- PHAROS `dr_sort_academic_helper.py` before the sorted-viewer delta is either merged or rejected
- `MASTER BIBLIOGRAPHY.txt` until bibliography path ownership is decided if the residue tree is reorganized

## 8. Recommended Ownership Path

1. Keep canonical LOTUS ownership bounded in `Agency`.
2. Keep `pharos-ai/pharos_governance_suite/lotus_dr_sort` quarantined as residue.
3. Resolve PHAROS-only LOTUS delta first:
- merge into Agency, or
- explicitly reject and archive it
4. Only after that, decide whether Dr. Sort:
- stays coupled in Agency for now
- extracts later to a dedicated repo
- or archives if later proven inactive

Current best path:

- keep bounded in `Agency` now
- defer any extraction decision until the PHAROS residue delta and shim plan are explicit
- do not archive yet because active operator workflow is not disproven
- this record does not authorize extraction, deletion, or archive execution by itself

## 9. Validation and Rollback Notes

### Validation

Before any move or extraction:

- confirm LOTUS desktop launch still works
- confirm Dr. Sort launch still works
- confirm cross-launch between the two still works
- confirm `dr_sort_feed` still lands in the expected LOTUS root
- confirm `flowerapp` console-script behavior still resolves
- confirm PHAROS backend still starts and still fail-closes LOTUS routes as intended

### Rollback

- use copy-first and shim-first rollback, not rename-first rollback
- keep the original Agency tree intact until replacement paths are proven
- restore removed files, launchers, and root-path shims if any extraction breaks the desktop workflow
- if PHAROS backend still needs optional residue imports, restore the prior residue path before retrying structural cleanup

## Related

- [[Governance and PHAROS MOC]]
- [[Dr. Sort and LOTUS Ownership Decision — March 2026]]


---
## Backlinks
Provenance artifact de-orphaned via graph repair (frontmatter + backlinks added 2026-07-10). Original content preserved above, unaltered.

- Indexed in: [[Home]]
