---
type: raw-lane-policy
title: /raw Intake Lane
aliases:
- raw/README
tags:
- raw-lane-policy
- raw
- readme-md
- scan
- label
- softinfo
- verified
- users
- color-lime
status: active
created: '2026-05-12'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/README.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# /raw Intake Lane

Canonical path:
- Windows: `C:\Users\softinfo\Documents\EMERAULD\raw`
- WSL: `/mnt/c/users/softinfo/documents/emerauld/raw`

## Default protocol for knowledge scans

1. Scan broadly for new source material.
2. Verify first: integrity, readability, provenance, duplicate check.
3. Hard-move verified source artifacts into `/raw/`.
4. Write or update wiki notes from verified sources.
5. Link notes into relevant MOCs and adjacent pages.
6. Report outputs split into `verified` and `inferred`.

## Hardening rules (fail-closed)

- No wiki synthesis from unverified artifacts.
- If verification fails for an artifact, it is excluded from wiki claims until resolved.
- Duplicate matches are reported and excluded from hard-move by default.
- Every intake run must emit a machine-readable verification report.
- Verified-source claims must cite only artifacts that passed verification in that run.

## Operational tool

Use the verifier/mover script:

```bash
python /mnt/c/users/softinfo/documents/emerauld/scripts/verify_and_hardmove_to_raw.py \
  --source "scan-label" \
  /path/to/file1 /path/to/file2
```

For folder-based scan packs, preserve the source tree under a scan-label folder:

```bash
python /mnt/c/users/softinfo/documents/emerauld/scripts/verify_and_hardmove_to_raw.py \
  --source "scan-label" \
  --raw-dir "/mnt/c/users/softinfo/documents/emerauld/raw/scan-label" \
  --preserve-relative-to "/path/to/staging/scan-label" \
  /path/to/staging/scan-label/file1
```

Use `--dry-run` first when previewing a move.

Outputs:
- moved files in `/raw/` (verified, non-duplicate)
- report JSON in `/raw/` with `verified` and `rejected` sections
- duplicate ledger in `/raw/.intake-manifest.jsonl`

## Legacy lanes

`raw sources/` and `raw\ sources/` are legacy provenance lanes. Preserve historical content there; do not use those lanes as the default destination for new scan runs unless Martin explicitly requests it.

## Related

- [[Research and Papers MOC]]
- [[session-state]]
