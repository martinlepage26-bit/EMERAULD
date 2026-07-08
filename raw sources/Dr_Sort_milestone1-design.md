---
type: raw-source
title: Dr_Sort_milestone1-design
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/Dr_Sort_milestone1-design.md
---

# Dr.Sort Milestone 1 Design and Implementation

## 1. Product Architecture
Dr.Sort uses a local-first split architecture:
- Electron host process (`apps/desktop/electron`) for desktop lifecycle, safe local IPC, and backend process control.
- React + TypeScript renderer (`apps/desktop/src`) for all UX views.
- Python service layer (`backend/dr_sort`) for discovery, parsing, classification, planning, execution, undo, restore, and rule evaluation.
- SQLite state store (`backend/dr_sort/db/schema.sql`) for jobs, evidence, plan entries, operation ledger, rules, and deleted-file records.
- No cloud dependencies for core functionality.

## 2. Domain Model
Core entities:
- `ScanOptions`: roots, library root, exclusions, scan policy flags.
- `FileEvidence`: extraction and classification evidence per file.
- `TaxonomyProposal`: inferred corpus-level folder hierarchy with rationale.
- `PlannedChange`: preview diff row with action, old/new paths, confidence, review flag.
- `ExecutionResult`: operation totals and warnings.
- `DeletedFileRecord`: soft-delete payload needed for restore.

Enums:
- `ActionType`: `sort_only`, `rename_only`, `sort_and_rename`, `skip`.
- `ParseStatus`: `ok`, `unreadable`, `corrupted`, `encrypted`, `ocr_deferred`, `unsupported`.
- `JobStatus`: `discovery_complete`, `planned`, `executed`, `failed`.

## 3. Codebase Folder Structure
```
dr-sort/
  apps/desktop/
    electron/main.ts
    electron/preload.cjs
    src/App.tsx
    src/services/api.ts
    src/styles/app.css
    src/types/
  backend/
    dr_sort/api/
    dr_sort/core/
    dr_sort/db/
    dr_sort/parsers/
    dr_sort/tests/
    dr_sort/fixtures/sample_corpus/
    scripts/seed_sample_corpus.py
  docs/milestone1-design.md
```

## 4. Database Schema
Implemented in `backend/dr_sort/db/schema.sql`.
Tables:
- `jobs`
- `taxonomy_proposals`
- `evidence`
- `plan_entries`
- `operations`
- `deleted_files`
- `rules`
- `settings`

Key safety properties:
- foreign keys enabled
- WAL mode
- plan + operation ledger for diff/undo
- deleted payload tracking for restore

## 5. Decision Logic (sort vs rename vs both vs skip)
Pipeline:
1. Discover supported files under selected roots, honoring exclusion rules.
2. Parse file by extension adapter.
3. Build evidence: title/author inference, keywords, topic, confidence, flags, duplicate signals.
4. Skip conditions:
   - unreadable/corrupted/encrypted
   - low-information with insufficient title signal
   - OCR-deferred image-only PDF without reliable metadata
5. Compute move need from inferred target folder.
6. Compute rename need from rename decision engine.
7. Final action:
   - move + rename => `sort_and_rename`
   - move only => `sort_only`
   - rename only => `rename_only`
   - no delta or low-confidence unsafe => `skip`

## 6. Title/Author-Aware Rename Suppression Algorithm
Implemented in `backend/dr_sort/core/rename_rules.py`.
Method:
- tokenize and normalize filename stem, detected title, and detected author
- remove punctuation, stopwords, year tokens, and extension artifacts
- compute title/author similarity using max of Jaccard and containment
- detect generic/machine filename patterns (`scan001`, `document_final_v2`, `untitled`, numeric IDs, copy variants)
- suppress rename when filename-title or filename-author confidence exceeds thresholds and name is not machine-like
- force rename for machine/generic names when a better suggestion exists

## 7. Taxonomy Inference Strategy
Implemented in `backend/dr_sort/core/taxonomy.py`.
Approach:
- infer stable categories from corpus-level topic frequencies
- depth policy:
  - <=4 active clusters => shallow
  - <=8 => medium
  - >8 => deep
- stable top-level mappings (Finance, Legal, Research, Reports, Notes, Reference, etc.)
- optional author deepening for books/research in deep mode
- low-confidence items route to `Review Queue/Uncategorized`
- pinned categories override inferred mappings

## 8. Duplicate Handling Strategy
Implemented in `backend/dr_sort/core/duplicates.py` and execution engine.
- exact duplicates by SHA-256 file hash
- probable duplicates by near-duplicate text signature
- preview marks duplicate candidates with reason badge
- optional execution flag quarantines duplicate candidates to internal trash
- no hard-delete by default

## 9. Restore and Undo Design
Implemented in `backend/dr_sort/core/executor.py`.
- every move/rename/delete operation writes inverse paths to `operations`
- per-job undo replays inverse operations in reverse order
- duplicate quarantine writes `deleted_files` records
- restore endpoint moves payload from internal trash back to original path
- collision-safe restore naming (`(restored n)` suffix)
- double-click restore wired in desktop Deleted Files view

## 10. UI Flow and Screen Specs
Implemented in `apps/desktop/src/App.tsx`.
Views:
- Dashboard
- Scan Setup
- Review Queue
- Proposed Library
- Preview Diff
- Activity History
- Deleted Files / Restore
- Rules
- Settings

Milestone 1 interactions:
- run scan from Scan Setup
- inspect diff and review queue
- execute plan and undo
- view operation history
- restore deleted item by double-click row
- create topic-to-folder rules

## 11. Phased Implementation Plan
- Phase A (done): backend schema + parser adapters + evidence model
- Phase B (done): decision engine + rename suppression + taxonomy proposal
- Phase C (done): preview planner + execution + undo + restore
- Phase D (done): desktop shell + core milestone views
- Phase E (next): watcher service, advanced overrides, richer analytics, OCR worker

## 12. Milestone 1 Production-Ready Scope (Implemented)
- scan selected folders recursively with exclusions
- parse `pdf`, `txt`, `doc`, `docx`, `odt`
- classify into all four action buckets
- infer title and author
- suppress rename when filename already contains title/author
- infer target folder and build preview diff
- execute move/rename safely
- persist history and operation ledger in SQLite
- soft-delete duplicate candidates
- restore deleted files through API and double-click UI
- tests:
  - rename suppression unit tests
  - parser coverage tests
  - integration tests for scan/execute/undo/restore
  - snapshot test for preview diff

## Known Limitations
- DOC extraction is heuristic for legacy binaries and should be upgraded with a dedicated converter.
- OCR fallback is deferred for image-only PDFs.
- Near-duplicate detection currently uses lightweight text signatures, not semantic embedding.
- Review Queue overrides are visible but persistent per-item override UX is limited in Milestone 1.
- Desktop packaging/signing and installer workflow are not finalized in this milestone.

## Next Features
- OCR fallback worker pipeline for image-only PDFs.
- semantic clustering for higher-quality topic inference on mixed corpora.
- watched folders with incremental, resumable scans.
- user roles and multi-operator policy controls.
- cloud drive connectors (OneDrive, Google Drive, Dropbox) with local cache safety.
- plugin parser interface for new file formats.
- improved near-duplicate detection via hybrid lexical + embedding similarity.
- natural-language rule creation that compiles to explicit rule JSON.

## Related

- [[Governance and PHAROS MOC]]
- [[LOTUS Premium Spec]]
