---
type: raw-source
title: D Drive Scan Manifest — 2026-05-12
aliases:
- raw/D-drive-scan-2026-05-12/MANIFEST
tags:
- raw
- intake
- raw-source
- d-drive-scan-2026-05-12
- drive
- elemental
- scan
- agents
- sources
- color-lime
status: preserved
created: '2026-05-12'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/D-drive-scan-2026-05-12/MANIFEST.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# D Drive Scan Manifest — 2026-05-12

## Scope
Selective high-signal ingest from D: after pruning dependency/runtime noise.

## Source Roots Scanned
- /mnt/d/DG
- /mnt/d/backend/Documents
- /mnt/d/Patent Workbench
- /mnt/d/elemental-agents
- /mnt/d/softinfo/Documents

## Included Bundles
- dg-migration/: DG C->D migration verification artifacts (report, summary, counts, conflict/hash/size ledgers).
- elemental-agents/: role contracts, orchestration playbooks, validation gates, combination rules, helper scripts.
- softinfo-manuscript/: manuscript-to-review.docx + plain-text extraction.

## Exclusions
- node_modules, .venv, dist/build output, git internals, cache/runtime state.
- Non-text media noise unless directly tied to governance intake.

## File Inventory
- raw sources/D-drive-scan-2026-05-12/MANIFEST.md
- raw sources/D-drive-scan-2026-05-12/dg-migration/MIGRATION_REPORT.md
- raw sources/D-drive-scan-2026-05-12/dg-migration/approved_files.txt
- raw sources/D-drive-scan-2026-05-12/dg-migration/classification_counts.tsv
- raw sources/D-drive-scan-2026-05-12/dg-migration/conflicts_existing_files.txt
- raw sources/D-drive-scan-2026-05-12/dg-migration/copied_files.txt
- raw sources/D-drive-scan-2026-05-12/dg-migration/hash_mismatch.txt
- raw sources/D-drive-scan-2026-05-12/dg-migration/size_mismatch.txt
- raw sources/D-drive-scan-2026-05-12/dg-migration/skipped_files.txt
- raw sources/D-drive-scan-2026-05-12/dg-migration/summary.json
- raw sources/D-drive-scan-2026-05-12/dg-migration/summary.txt
- raw sources/D-drive-scan-2026-05-12/elemental-agents/README.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/01-prime-coordinator.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/02-context-cartographer.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/03-requirements-architect.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/04-implementation-engineer.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/05-quality-auditor.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/06-test-operator.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/07-security-guardian.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/08-observability-sentinel.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/09-governance-steward.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/agents/10-delivery-operator.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/combinations/README.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/combinations/combination-validation.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/combinations/dual-combinations.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/combinations/manifestation-rules.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/combinations/triple-combinations.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/combinations/validate-combinations.sh
- raw sources/D-drive-scan-2026-05-12/elemental-agents/examples/01-feature-request-implementation.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/examples/02-code-review-workflow.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/examples/03-api-design-pass.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/examples/04-incident-response.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/examples/05-documentation-hardening.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/examples/06-release-readiness.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/install-hooks.sh
- raw sources/D-drive-scan-2026-05-12/elemental-agents/orchestration/01-intake-and-routing.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/orchestration/02-context-assembly.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/orchestration/03-planning-to-execution-bridge.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/orchestration/04-execution-loop.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/orchestration/05-validation-gates.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/orchestration/06-recovery-and-escalation.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/validation/01-structure-check.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/validation/02-operational-content-check.md
- raw sources/D-drive-scan-2026-05-12/elemental-agents/validation/03-triangulated-verification.md
- raw sources/D-drive-scan-2026-05-12/softinfo-manuscript/manuscript-to-review.docx
- raw sources/D-drive-scan-2026-05-12/softinfo-manuscript/manuscript-to-review.extracted.txt

## Related

- [[Research and Papers MOC]]
- [[D Drive Scan — 2026-05-12]]
