---
type: wiki
aliases: ["D Library cleanup leads", "D:\\LIBRARY genealogy flags"]
tags: [library, intake, genealogy, metadata, cleanup]
status: active
created: 2026-04-26
updated: 2026-04-26
---

# D Library — Genealogy Flags and Cleanup Leads (2026-04-26)

## Summary
This note converts the intake’s “metadata smell” into actionable cleanup leads so the archive genealogy can be corrected without losing provenance — a downstream task from [[D Library — LIBRARY Intake Index (2026-04-26)|the D:\LIBRARY intake index]] and a Henry-handoff dependency for [[Library Master Reference Intake (2026-04-26)|the master reference intake]]. Source-of-truth for the flags is the intake summary at `raw sources/D_LIBRARY_ingest_2026-04-26/inventory/SUMMARY.md`. Operational mate to [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)|Control 3]]: the same supersession discipline applies at the file-metadata layer as at the architecture layer.

## High-signal flags

### Misnamed PDFs (content header `%PDF-` but extension not `.pdf`)
These should be corrected in-place in `D:\LIBRARY` (rename extension) once provenance is confirmed.
- `%PDF-1.3.txt`
- `%PDF-1.4.txt`
- `%PDF-1.6.txt`
- `Review/Unreadable/%PDF-1.3.txt`
- `Review/Unreadable/%PDF-1.4 Sharp Scanned ImagePDF.txt`
- `Review/Unreadable/%PDF-1.4.txt`
- `Review/Unreadable/%PDF-1.5.txt`
- `Review/Unreadable/%PDF-1.6.txt`
- `Review/Unreadable/%PDF-1.7.txt`

### Repeated extensions (`.pdf.pdf`, `.txt.txt.txt`, etc.)
The intake logged **440** such paths; these are typically the result of automated “save as” or repeated renames.
- Cleanup goal: normalize filenames while preserving a reversible mapping (old path → new canonical path).
- Practical approach: generate a rename plan from `raw sources/D_LIBRARY_ingest_2026-04-26/inventory/files.csv` (do not rename blindly inside `Review/Unreadable` until OCR/provenance is stable).

### Misleading extensions (file content type != extension)
- `Review/Unreadable/2024 - review.pdf - 2024 - review.pdf.pdf - 2024 - review.pdf - 2024 - review.pdf.pdf.pdf` is **HTML saved from URL** but stored with a `.pdf` extension (captured as `ok_html` in OCR status).

### Duplicates (content-identical)
See `raw sources/D_LIBRARY_ingest_2026-04-26/inventory/duplicates_by_sha256.csv` for duplicates detected within the scanned tree (hash-based).

### Embedded-metadata drift (title/metadata != content)
Some PDFs have embedded metadata (e.g., `pdfinfo: Title`) that does not match the extracted text. Treat these as genealogy flags: do not rename/canonize until confirmed from content and (ideally) the original file.
- Example: the captured PDF whose embedded title is `ISO 15930 - Electronic document file format for prepress digital data exchange (PDF/X)` but whose content is Beach & Pedersen’s *Process‑Tracing Methods* (2nd ed.).

## OCR and unreadable surface
- The unreadable/OCR pass status lives at `raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/inventory/ocr_status.csv`.
- Current state (2026-04-26): all unreadable items produced a converted note; 1 item is `ok_html` (HTML saved from URL but misnamed as `.pdf`), and no OCR errors remain.

## Related
- [[D Library — LIBRARY Intake Index (2026-04-26)]]
- [[Library Master Reference Intake (2026-04-26)]]
- [[2026 - Mauss - The Gift]] — D-drive dedup manifest CSV artifact (2026-04-21 scan); the canonical wiki synthesis lives at [[The Gift — Mauss (Obligation, Reciprocity, Hau)]]
