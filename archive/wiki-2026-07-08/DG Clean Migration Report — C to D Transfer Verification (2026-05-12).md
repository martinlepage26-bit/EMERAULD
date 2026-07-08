---
type: wiki
title: DG Clean Migration Report — C to D Transfer Verification (2026-05-12)
tags:
- archive
- migration
- count
- mismatch
- report
- drive
- wiki
- wiki-2026-07-08
status: active
created: '2026-05-12'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/DG Clean Migration Report — C to D Transfer Verification (2026-05-12).md
backlink_count: 10
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[archive/wiki-2026-07-08/D Drive Scan — 2026-05-12]]'
- '[[archive/wiki-2026-07-08/DG Website Logo Rebrand & Governance Audit — 2026-05-01]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# DG Clean Migration Report — C to D Transfer Verification (2026-05-12)

## Summary

Migration artifact from `C:\Users\softinfo\DG` to `D:\DG` documenting a clean, verification-first transfer policy:

- Preview/classify before copy.
- Detect conflicts before copy.
- Do not overwrite destination files.
- Exclude secret-bearing/runtime surfaces.
- Verify destination with size + SHA-256 checks.

Primary verified source files are preserved in `raw/D-drive-scan-2026-05-12/dg-migration/`.

Verification report: `raw/intake-report-d-drive-scan-2026-05-12.json`.

---

## Key Results

From `summary.txt` and `MIGRATION_REPORT.md`:

- `approved_count=82`
- `copied_count=82`
- `skipped_existing_count=0`
- `precopy_conflict_count=0`
- `size_mismatch_count=0`
- `hash_mismatch_count=0`
- timestamp: `2026-05-12T17:51:31Z`

Classification highlights:

- approved: 82
- node_modules: 52870
- git internals: 381
- frontend build output: 55
- env secret files: 2
- sensitive credential doc: 1

---

## Governance-Relevant Signal

- Shows strong migration hygiene: keep only deployable artifacts, not volatile/runtime baggage.
- Makes exclusion policy explicit (`.env`, runtime state, credential docs).
- Produces auditable summary ledgers instead of implicit trust. The zero-conflict/zero-mismatch claims should be read through verified `summary.json`, `summary.txt`, and `MIGRATION_REPORT.md`; empty marker files were rejected by the fail-closed verifier and left in legacy staging.

---

## Related

- [[DG Website Logo Rebrand & Governance Audit — 2026-05-01]]
- [[Governance Controls and Mechanisms]]
- [[Personal and Projects MOC]]
- [[D Drive Scan — 2026-05-12]]
- [[MIGRATION_REPORT]]
