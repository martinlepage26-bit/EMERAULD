---
type: raw-source
title: README
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/D_LIBRARY_ingest_2026-04-26/henry/README.md
---

# Henry Intake — D:\LIBRARY Candidates (2026-04-26)

See also [[Manuscript Pipeline MOC]].
This intake produces reference candidates for Henry to add into the master reference lists (vault-side), with provenance paths back to the raw converted artifacts.

## Source material (vault paths)

- Base intake root: `raw sources/D_LIBRARY_ingest_2026-04-26/`
- Base candidate list (non-OCR scan): `raw sources/D_LIBRARY_ingest_2026-04-26/henry/MASTER_REFERENCE_CANDIDATES.csv`
- OCR candidate list (from `Review/Unreadable/` pass): `raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/henry/MASTER_REFERENCE_CANDIDATES_OCR.csv`
- Combined list (recommended): `raw sources/D_LIBRARY_ingest_2026-04-26/henry/MASTER_REFERENCE_CANDIDATES_ALL.csv`

## How to use

- Prefer `MASTER_REFERENCE_CANDIDATES_ALL.csv` as the intake queue.
- For each row, open `converted_md` to confirm title/author/year and resolve to the canonical citation format for the destination master list.
- Use `ocr_text` when present to validate bibliographic fields when the PDF is scanned/image-based.
