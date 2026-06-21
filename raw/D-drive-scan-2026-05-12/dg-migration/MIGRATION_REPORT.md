# DG Clean Migration Report

## Run context
- Skill posture loaded: `Gadget` (external/migration execution discipline)
- Elemental agent selected: `10-delivery-operator` (verification-first handoff)
- Source: `C:\Users\softinfo\DG` (`/mnt/c/Users/softinfo/DG`)
- Destination: `D:\DG` (`/mnt/d/DG`)
- Date (UTC): 2026-05-12

## Clean-migrate policy used
- Preview/classify first.
- Detect destination conflicts before copy.
- Do not overwrite existing destination files.
- Exclude generated/runtime state and secret-bearing env surfaces.
- Verify destination with size and SHA-256 checks.

## Classification summary (source files)
See `classification_counts.tsv`.

Key counts:
- approved: 82
- node_modules: 52870
- git internals: 381
- frontend build output: 55
- wrangler runtime state: 3
- env secret files: 2
- sensitive credential doc: 1
- local agent state: 1
- python cache: 1

## Transfer summary
See `summary.txt` and `summary.json`.

Results:
- approved files: 82
- copied: 82
- skipped existing: 0
- pre-copy conflicts: 0
- size mismatches: 0
- hash mismatches: 0

## Artifact inventory
- `approved_files.txt`
- `classification_counts.tsv`
- `copied_files.txt`
- `conflicts_existing_files.txt`
- `skipped_files.txt`
- `size_mismatch.txt`
- `hash_mismatch.txt`
- `summary.txt`
- `summary.json`

## Notes
- `memory/test_credentials.md` was intentionally excluded from migration.
- `.env` and `.env.production` were intentionally excluded from migration.
- Destination received clean project artifacts only (code, config, docs, static assets, migrations).

## Related

- [[Research and Papers MOC]]
- [[DG Clean Migration Report — C to D Transfer Verification (2026-05-12)]]
