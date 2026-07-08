---
type: register
title: PARA-MIGRATION-MANIFEST-2026-07-08
aliases:
- PARA Migration Manifest 2026-07-08
tags:
- register
- overhaul
- para-migration
- vault
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: _vault
canonical_path: _vault/PARA-MIGRATION-MANIFEST-2026-07-08.md
backlink_count: 7
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Logs/2026-07-08]]'
- '[[Resources/ROUTING]]'
- '[[wiki/WIKI-ROUTING-REPORT]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[governance/EMERAULD-OS-BUILD-ORDER]]'
- '[[index]]'
---

# PARA Migration Manifest — 2026-07-08

For future Claude: this documents the full wiki/ → PARA migration executed as Phase 2 of the 2026-07-08 overhaul (see [[OVERHAUL-BASELINE-2026-07-08]]). Machine-readable rows: `_vault/PARA-MIGRATION-MANIFEST-2026-07-08.csv` (source,dest,action,cluster). Executed by `scripts/para_migrate.py` in batches of 20 with a graph-regression gate per batch.

## Provenance

- Stage A (154 rows): every explicit table + rule-group in [[wiki/WIKI-ROUTING-REPORT|the 2026-06-29 routing report]], resolved against disk with zero unresolved names.
- Stage B (339 rows): the remaining 441 top-level wiki/ files classified by 4 parallel content-reading agents (uncertain → keep); 103 files kept in wiki/ (about the vault itself, skill-domain hubs, MOC-adjacent structure, bridge notes, ambiguous).
- Reviewer overrides: VoiceBridge Foundation → Areas/PHAROS (shipped product); Charge & Circle pair → keep (report flagged for human review).

## Distribution (493 moves)

| Destination | Rows |
|---|---|
| Areas/PHAROS | 213 |
| Areas/Writing | 146 |
| Resources | 65 |
| archive/wiki-2026-07-08 | 58 |
| Areas/Personal | 8 |
| Areas/Lavoie | 3 |

Total exceeds the report's ~310 estimate: classifiers read full note content and routed borderline governance/AI notes to Areas/PHAROS that the report's title-scan had left in the keep pool. Operator scope decision was "full migration".

## Gates

- Pre-migration extended-corpus graph baseline: 1,415 nodes / 13,142 edges / 3,193 unresolved / 46 components / 62 zero-backlink.
- Per batch: unresolved must not rise; git commit per batch (surgical rollback); final `para_migrate.py --verify-only` must report 0 stale path-form links.
- Consolidation rows (`action=consolidate`, 8 files) handled separately in Phase 2c — see [[wiki/WIKI-ROUTING-REPORT|routing report]] §6.

## Phase 2c consolidation verdict (revised on content inspection)

The routing report's §6 "consolidate 5 Queering versions into one canonical + one genealogy" was NOT executed as written. Content inspection showed the six Queering Neo-Pagan Magic notes have been curated since June into an intentional version genealogy: each carries explicit cross-references and distinct-role statements ("Source overlap note: … They are not duplicates — consult both"). Destructive merging would have destroyed curated structure and violated the standing full-length-preservation writing rule. Executed instead:

- Queering Neo-Pagan Magic ×5 remaining files → Areas/Writing/ (cluster kept together with the sixth, already moved).
- For Her Alone to Wield: Cover Letter + HENRY Draft → archive/wiki-2026-07-08/ (dated post-submission process artifacts, per report); main paper + Version Genealogy live in Areas/Writing/.
- Mauss pair: canonical [[Resources/The Gift — Mauss (Obligation, Reciprocity, Hau)|The Gift — Mauss]] stays in Resources/ and now links the recovered 1,293-line reading-notes file, archived unmerged.
- Second Self pair: canonical + Public Voice Examples → Areas/PHAROS/; the recovered duplicate (duplicate_of marker) → archive/wiki-2026-07-08/.

## Known pre-existing stem collisions (not worsened by moves)

- `CSV_DIAGNOSTIC_REPORT.md` also exists under artifacts/2026-04-19-pharos-migration-pr4/docs/.
- `Martin Voice Spec — Version Genealogy.md` also exists under wiki/genealogy/ — duplicate pair to dedup later.
