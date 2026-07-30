---
type: source
aliases: []
tags: [raw-source, orphan-repair, queer-gender, docsort]
status: raw
created: 2026-07-10
updated: 2026-07-10
source: "Dr_Sort_milestone2-design"
---
# Dr.Sort Milestone 2 Architecture Delta

## Scope

Milestone 2 is an in-place upgrade over Milestone 1:

1. OCR fallback for image-only/low-information PDFs
2. stronger near-duplicate detection
3. watched folders with review-first safety
4. semantic clustering for better taxonomy inference
5. UX hardening for confidence/review/recoverability
6. packaging and developer ergonomics

No core subsystem was replaced; existing Milestone 1 pipeline was extended.

## Architecture Delta

### Backend Service Layer

- `backend/dr_sort/core/service.py`
  - integrated OCR settings/capability in scan flow
  - integrated semantic clusters into evidence + taxonomy proposal
  - integrated stronger duplicate annotations + persisted duplicate clusters
  - added job details endpoint data (state transitions, action/status counts, warnings, OCR usage)
  - added review bulk actions (`approve`, `defer`, `never rename`, `never move`, `rule from selection`)
  - added watched-folder CRUD, queue APIs, and optional auto-scan-only mode

### OCR Fallback

- `backend/dr_sort/core/ocr.py`
  - PDF-only OCR fallback gate
  - trigger conditions:
    - parser returns `ocr_deferred`
    - parser text below low-information threshold
  - capability detection:
    - `tesseract` binary
    - PyMuPDF renderer availability
  - page-level provenance persisted (`embedded_text`, `ocr_text`, `mixed`, `failed`)
  - OCR cache in SQLite keyed by content + OCR parameters
  - graceful degradation when dependencies are absent

### Duplicate Detection v2

- `backend/dr_sort/core/duplicates.py`
  - kept exact hash duplicates
  - added near-duplicate scoring with:
    - normalized text overlap
    - title similarity
    - author overlap
    - length/file-size/page proximity
    - filename similarity as weak evidence
    - content fingerprint boost
  - outputs:
    - `exact_duplicate`
    - `probable_duplicate`
    - `possible_version_variant`
  - false-positive guard for low-information files

### Watched Folders

- `backend/dr_sort/core/watcher.py`
  - optional `watchdog`-based runtime watcher
  - multi-folder support
  - per-folder debounce and event batching
  - per-folder filters:
    - include subfolders
    - exclusions
    - file-type filters
    - mode (`notify_only`, `auto_scan_only`)
  - all watcher events route to queue records first (review-safe)
  - no destructive auto-execution path

### Semantic Clustering Upgrade

- `backend/dr_sort/core/semantic_cluster.py`
  - local TF-IDF-like vectorization
  - cosine similarity clustering
  - cluster label synthesis from dominant terms + topic votes
  - confidence and rationale per cluster
- `backend/dr_sort/core/taxonomy.py`
  - semantic-cluster-driven taxonomy path when clusters are present
  - fallback to Milestone 1 topic strategy when semantic signal is insufficient

## Database Delta

`backend/dr_sort/db/schema.sql`:

- New `job_events` table for transition history
- `evidence` columns added:
  - `text_provenance`, `ocr_confidence`, `page_count`, `ocr_cache_hit`
  - `duplicate_kind`, `duplicate_cluster_id`, `duplicate_score`
  - `cluster_label`, `cluster_confidence`
- New `ocr_cache` table
- New `duplicate_clusters` table
- New `watched_folders` table
- New `watcher_queue` table

`backend/dr_sort/db/repository.py`:

- migration-safe evidence column bootstrap for older DBs
- job event persistence
- OCR cache CRUD
- duplicate cluster CRUD
- watched-folder + queue CRUD
- plan-entry update APIs for review bulk actions

## API Delta

`backend/dr_sort/api/app.py` + `backend/dr_sort/api/schemas.py` new endpoints:

- `GET /capabilities`
- `GET /settings`, `PUT /settings`
- `GET /jobs/{job_id}/details`
- `GET /jobs/{job_id}/duplicates`
- `POST /jobs/{job_id}/review-actions`
- `POST /deleted/restore-bulk`
- `GET/POST/PUT/DELETE /watchers*`
- `GET /watchers/queue`
- `POST /watchers/{id}/event`
- `POST /watchers/{id}/flush`

## Desktop UX Delta

`apps/desktop/src/App.tsx`:

- capability status cards (OCR, watcher, parser, DB)
- explicit confidence badges and reason badges in Review Queue + Preview Diff
- duplicate cluster review panel
- safer bulk review actions
- deleted-file bulk restore with status feedback
- job details panel with transitions/counters/warnings/OCR usage
- watcher management + queue monitoring in Settings
- diff pagination for larger corpora
- preserved double-click restore behavior

`apps/desktop/src/services/api.ts` + `src/types/models.ts`:
- expanded typed API contracts for Milestone 2 endpoints and payloads

## Packaging and Dev Ergonomics

- `apps/desktop/package.json`
  - added packaging scripts (`package:win`, `package:dir`)
  - added `electron-builder` config for NSIS
  - added convenience scripts (`dev:backend`, `start:desktop`)
- updated root `README.md` with:
  - setup
  - optional dependencies
  - seed/demo flow
  - test/build commands
  - packaging command

## Test Delta

New backend tests:

- `test_ocr.py`
  - image-only OCR fallback
  - missing Tesseract behavior
  - cache reuse
  - low-information threshold trigger
- `test_duplicates_v2.py`
  - exact duplicate
  - probable duplicate
  - version variant
  - false-positive guard
- `test_watchers.py`
  - watcher registration persistence
  - debounce batching
  - queue creation
  - exclusion handling
- `test_semantic_clustering.py`
  - stable clustering
  - taxonomy fallback when clustering is insufficient
  - label synthesis quality

Milestone 1 tests were preserved and snapshot updated for duplicate-review behavior.

## Safety Properties Preserved

- scan phase remains non-mutating
- preview remains mandatory for execution
- duplicate quarantine remains soft-delete
- undo/restore remain ledger-driven and reversible
- watcher flow is review-first and non-destructive
- app remains local-first/offline for core behavior

## Known Limitations (Post-Milestone 2)

- OCR quality heuristics are coarse averages; no per-token confidence UX yet.
- OCR still depends on external binaries/libraries (`tesseract`, `pymupdf`) when enabled.
- Near-duplicate detection is lexical/fingerprint based, not semantic-embedding robust.
- `auto_scan_only` watcher mode currently scans watched roots, not exact changed-file subsets.
- Desktop UI is single-window and still monolithic (`App.tsx`) pending component extraction.
- Installer signing/notarization and enterprise deployment policy hardening are not finalized.

## Next Features

1. OCR fallback enhancements
   - better page-quality scoring
   - adaptive page limits
   - language auto-detection
2. Semantic clustering improvements
   - stronger local vectorization and cluster validation
   - better separation of adjacent document intents
3. Watched folders
   - exact delta scans from queue payloads
   - richer notification UX
4. User roles
   - multi-user policy controls and review permissions
5. Cloud drives
   - OneDrive/Google Drive/Dropbox local-cache-safe connectors
6. Plugin parsers
   - parser SDK and signed plugin loading
7. Better near-duplicate detection
   - hybrid lexical + local embedding strategy
8. Natural-language rule creation
   - NL-to-rule compiler with explainable output and review step

## Related

- [[Research and Papers MOC]]
- [[Dr. Sort Codebase Version Genealogy — Three Iterations of Failed Automation]]


---
## Backlinks
Provenance artifact de-orphaned via graph repair (frontmatter + backlinks added 2026-07-10). Original content preserved above, unaltered.

- Indexed in: [[Home]]
