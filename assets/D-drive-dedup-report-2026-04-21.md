---
type: report
title: 'D: Drive Deduplication Report — 2026-04-21'
aliases:
- assets/D-drive-dedup-report-2026-04-21
tags:
- report
- assets
- d-drive-dedup-report-2026-04-21-md
- library
- groups
- spotlight
- drive
- mine
- color-purple
status: manifest-only / no-deletion-executed
created: '2026-04-21'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/D-drive-dedup-report-2026-04-21.md
backlink_count: 2
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[tmp/drive-audit-2026-04-18/deletion-shortlist]]'
drive: 'D: (BACKEND, 2TB)'
scanned_files: 3342
---

# D: Drive Deduplication Report — 2026-04-21

## Executive Decision

**No files were deleted.** The manifest is durable; approval is required before any removal. D: is a backup/archive drive labelled `BACKEND`, and governance rules (MASTER PACK / MASTER REFERENCE SAFE / CODEX/hephaistos-pass / LIBRARY/Mine) make autonomous deletion the wrong call.

## Scope

- Drive: `D:\` (BACKEND, 2 TB physical, ~3 GB used)
- Files hashed (SHA-256): **3,342**
- Excluded directories during hash: `.git`, `.obsidian`, `__pycache__`, `node_modules`, `venv`, `.venv`, `dist`, `build`, `cache`, `.cache`, `.idea`, `.vscode`, `.vs`
- Top-level inventory:

| Folder | Files | Size (MB) | Note |
|---|---|---|---|
| `LIBRARY` | 793 | 1433.3 | subfolders: `Mine`, `Not_Mine`, `Review` |
| `MASTER PACK` | 1647 | 244.7 | governance — `RECURSO`, `MASTERxMASTERxMASTER`, `POST-RECURS`, `APEX_PAPERS_COMMON` |
| `MASTER REFERENCE SAFE` | 62 | 6.5 | governance — name explicitly `SAFE` |
| `CODEX` | 791 | 1163.6 | writings, papers, books; contains `hephaistos-pass` |
| `MODELS` | 0 | 0 | empty |
| `Agatha-Dottie-Mobi` | 0 | 0 | empty |
| `Zipped` | 5 | 37.9 | archive blobs |

## Duplicate Findings (Exact SHA-256)

- **363** duplicate groups (≥ 2 identical copies)
- **891** redundant copies (count − 1 per group)
- **126.8 MB** theoretically recoverable if every redundant copy were removed

### Distribution by risk

| Risk | Redundant copies | Size (MB) |
|---|---|---|
| `HIGH-governance-group` (any group touching MASTER PACK / MASTER REFERENCE SAFE / hephaistos-pass / LIBRARY/Mine) | 872 | 122.14 |
| `LOW-macOS-artifact` (`.Spotlight-V100` index files) | 14 | 0.19 |
| `MEDIUM-library-curated` (LIBRARY/Review/Unreadable — garbled filenames, retained copy in CODEX) | 4 | 3.87 |
| `MEDIUM-codex` (CODEX Papers/Soumis/REJECTED — dup pair with LIBRARY, retention ambiguous) | 1 | 0.61 |

### Cross-area groups

- 23 groups span `LIBRARY` + `MASTER PACK`
- 5 groups span `LIBRARY` + `CODEX`
- 4 groups span `MASTER PACK` + `CODEX`
- All other cross-area duplicates are **intra-MASTER PACK** (316 groups) — i.e., MASTER PACK contains internal redundancy by itself

## Why Nothing Was Deleted

1. **Backup drive**: redundancy is the point of `BACKEND`. "Duplicate" here may mean "intended second copy," not waste.
2. **Governance lock**: 97% of redundant bytes (872/891 copies) are in groups where at least one copy lives under `MASTER PACK`, `MASTER REFERENCE SAFE`, `CODEX/hephaistos-pass`, or `LIBRARY/Mine`. Your rule 4 requires a newer file *properly dated, traceable, and stored elsewhere* before any governance copy is removed — a condition a second copy on the same backup drive cannot satisfy.
3. **Retention heuristic is fragile**: the `LIBRARY\Review\Unreadable\` folder contains files with concatenated/corrupted filenames (apparent prior-dedup artifacts). A newest-mtime-wins rule picks those over the clean CODEX original in at least one group — exactly the opposite of what you'd want.
4. **Upside is minimal**: max recoverable 127 MB on a 2 TB drive with 1.99 TB free. Not worth a single wrong delete.

## Non-Governance Candidates (14 files, ~200 KB) — macOS Spotlight Indices

These are filesystem metadata left by macOS when this drive was previously connected to a Mac. They have no content value.

Path root: `D:\.Spotlight-V100\Store-V1\Stores\17650748-...` and `D:\.Spotlight-V100\Store-V2\505F3790-...`

Recommended action: delete the entire `D:\.Spotlight-V100\` tree (not just the duplicate entries). Pending your go-ahead.

## Medium-Risk Candidates (5 files) — Require Your Review

All involve `LIBRARY\Review\Unreadable\` files with garbled concatenated filenames of the form `YYYY - thing.ext - YYYY - thing.ext.ext - ... .ext.ext`. In 4 of 5 cases the clean canonical lives in CODEX; in 1 case the retention pairing is ambiguous. Review list:

| Group | Size | Broken (LIBRARY/Review/Unreadable) → Clean (CODEX) |
|---|---|---|
| 21 | 38 KB | `1999 - journal_article.docx...` → `CODEX\Publications\Submissions\REBOOT\Reboot_Performance_Gender_Identity__6FC1EE89.docx` |
| 23 | 162 KB | `2012 - Martin Lepage - Chapter 8_1.pdf...` → `CODEX\Papers\Old\The_Avatar_animated_series_a_queer_readi.pdf` |
| 28 | 3.56 MB | `2017 - thesis_or_dissertation [2].pdf...` → `CODEX\Papers\Old\LEPAGE-Why Be King-Thesis-UQAM.pdf` |
| 30 | 197 KB | `2023 - Martin Lepage - thesis_or_dissertation_1.pdf...` → `CODEX\BOOKS\BUFFY BOOK\cvmartinlepage2025ENG.pdf` |
| 29 | 620 KB | `CODEX\Papers\Soumis\REJECTED\CircleRemainsOpenREV.docx` ↔ `LIBRARY\Review\Unreadable\2020 - legal_or_contract.docx...` (retention ambiguous) |

Recommendation: drop the entire `D:\LIBRARY\Review\Unreadable\` folder after you confirm every file in it has a clean twin elsewhere. Low intrinsic value (broken filenames) but it is inside `LIBRARY` so I defer.

## Deliverables

- **Hash index (full)**: `C:\Users\softinfo\Documents\EMERAULD\assets\D-drive-hash-index-2026-04-21.csv` — 3342 rows, every file hashed with path/size/modified/toplevel
- **Dedup manifest (per-group)**: `C:\Users\softinfo\Documents\EMERAULD\assets\D-drive-dedup-manifest-2026-04-21.csv` — 1254 rows (every member of every duplicate group, tagged `KEEP` / `CANDIDATE-DELETE`, with risk class and retained-path pointer)
- **This report**: `assets/D-drive-dedup-report-2026-04-21.md`

## Folders Removed

None. No deletion executed.

## Preserved (Governance-Relevant, Never Auto-Touch)

- `D:\MASTER PACK\*` (all 1647 files, including 316 intra-folder duplicate groups)
- `D:\MASTER REFERENCE SAFE\*` (all 62 files)
- `D:\CODEX\hephaistos-pass\*` (all 21 files)
- `D:\LIBRARY\Mine\*` (1 file)
- Any group containing even one copy under the above paths (flagged `HIGH-governance-group`)

## Next Decisions I Need From You

Pick any/all:

1. **OK to remove `D:\.Spotlight-V100\` entirely?** (macOS filesystem junk, ~200 KB)
2. **OK to remove `D:\LIBRARY\Review\Unreadable\` entirely?** (broken filenames, all appear to be duplicates of clean CODEX originals — but sits under `LIBRARY`)
3. **Intra-MASTER PACK duplicates (316 groups, ~120 MB)**: open the manifest and approve specific groups individually, or leave as-is. I recommend leave-as-is — this is a backup; the storage is free.
4. Anything else you want me to cut from `Zipped`, `MODELS` (empty), `Agatha-Dottie-Mobi` (empty) — the empty ones can be dropped with no content risk.

## Related

- `[[session-state]]` — vault persistence
- `[[memory]]` — live business state
- Original task prompt: user-invoked from EMERAULD working dir, 2026-04-21 ~07:10 EDT
- [[deletion-shortlist]]
