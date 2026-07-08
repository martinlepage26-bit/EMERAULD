---
type: wiki
title: D Drive Scan — 2026-05-12
aliases:
- D Drive Scan — 2026-05-12
- wiki/D Drive Scan — 2026-05-12
tags:
- wiki
- intake
- d-drive-scan-2026-05-12-md
- migration
- schizophrenia
- neuroimaging
- elemental
- promoted
- color-lime
status: active
created: '2026-05-12'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/D Drive Scan — 2026-05-12.md
backlink_count: 11
backlinks:
- '[[wiki/DG Clean Migration Report — C to D Transfer Verification (2026-05-12)]]'
- '[[wiki/Diagnostic Accuracy of Multimodal Neuroimaging + Eye-Tracking in Schizophrenia
  — Draft Snapshot (2026-05-10)]]'
- '[[wiki/Elemental Agents Framework — Multi-Agent Role and Validation Architecture
  (2026-05-12)]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/Home]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[memory/agents/Decisions]]'
- '[[memory/agents/Events]]'
- '[[memory/daily/2026-05-13]]'
- '[[raw/D-drive-scan-2026-05-12/MANIFEST]]'
---

# D Drive Scan — 2026-05-12

## Summary

Selective D: intake focused on recent high-signal text artifacts after pruning dependency/runtime noise. This pass promoted three main lanes:

- DG migration verification artifacts (C: -> D: transfer with conflict/hash/size checks).
- Elemental Agents framework docs (role contracts, orchestration loop, validation gates).
- External manuscript draft snapshot (schizophrenia multimodal neuroimaging + eye-tracking meta-analysis draft).

Verified raw pack: `raw/D-drive-scan-2026-05-12/`.

Hard-move report: `raw/intake-report-d-drive-scan-2026-05-12.json`.

- Verified: 41 files moved into `/raw/`.
- Rejected: 5 files left in the legacy staging lane: four empty migration marker files and one duplicate hash (`copied_files.txt`, duplicate of `approved_files.txt`).
- Evidence boundary: promoted-note claims should rely on verified non-empty sources and the report; rejected marker files remain audit/provenance leftovers, not evidence anchors.

---

## Scanned Roots

- `/mnt/d/DG`
- `/mnt/d/backend/Documents`
- `/mnt/d/Patent Workbench`
- `/mnt/d/elemental-agents`
- `/mnt/d/softinfo/Documents`

Exclusions: `node_modules`, `.venv`, build artifacts, caches, git internals, runtime state.

---

## Promoted Notes

- [[DG Clean Migration Report — C to D Transfer Verification (2026-05-12)]]
- [[Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]]
- [[Diagnostic Accuracy of Multimodal Neuroimaging + Eye-Tracking in Schizophrenia — Draft Snapshot (2026-05-10)]]

---

## Why These Were Ingested

- They are recent (2026-05-10 to 2026-05-12) and operationally meaningful for current agent/governance workflow.
- They contain explicit process controls, validation logic, or research claims worth preserving for retrieval.
- They have reusable structure for future execution (especially migration discipline and multi-agent validation).

---

## Related

- [[Home]]
- [[Governance and PHAROS MOC]]
- [[Research and Papers MOC]]
- [[Personal and Projects MOC]]
- [[MANIFEST]]
