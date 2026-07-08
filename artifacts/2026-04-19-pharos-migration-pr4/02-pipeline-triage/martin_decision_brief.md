---
type: artifact
title: PHAROS Diagnostic — Martin's Decision Brief
aliases:
- artifacts/2026-04-19-pharos-migration-pr4/02-pipeline-triage/martin_decision_brief
tags:
- artifact
- pharos
- artifacts
- 2026-04-19-pharos-migration-pr4
- option
- merge
- defer
- regulatory
- manifest
- color-green
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/2026-04-19-pharos-migration-pr4/02-pipeline-triage/martin_decision_brief.md
backlink_count: 2
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# PHAROS Diagnostic — Martin's Decision Brief
**Date:** 2026-04-19  
**Source:** CSV_DIAGNOSTIC_REPORT.md  
**Format:** Three decisions. All context included. No tabling.

---

## Decision 1 — The AI & Society manuscript

**File:** `ai-anxiety-recursive-governance-ai-society-aligned-2026-03-11.md`  
**Current action flag:** `MERGE_WITH_RELATED_FILE`  
**Actual status:** `source_bearing_artifact`, `high` confidence, `near_final`, submitted to *AI & Society*

### The conflict
The pipeline has this file queued for automated merge. It is the wrong call for this file.  
This is not a cleanup artifact. It is your highest-confidence primary evidence document —  
the only peer-review submission in the archive — and merging it into another file would:
- Destroy its provenance as a standalone submission document
- Eliminate its ability to be cited by DOI once published
- Remove it from the `source_bearing_artifact` evidence set (from 17 down to 16)

The `pharos_pipeline_filter.py` script will hard-exit with code 1 if it encounters  
this file in a merge queue without `human_gate_cleared=true` in the manifest.

### Your decision

**Option A — Override the merge, preserve as standalone (recommended)**  
Change `action` to `PRESERVE_AND_LIGHTLY_CLEAN` in `00_ARCHIVE_METADATA_MANIFEST.csv`.  
Add `human_gate_cleared=true` and a note: `"Standalone submission document — merge prohibited until DOI assigned"`.  
If published: update to `PRESERVE_AS_IS` with the DOI.

**Option B — Merge is intentional (you know something the diagnostic doesn't)**  
If the merge target is a *superset* document that subsumes the manuscript  
(e.g., a book chapter or expanded patent annex), then:
1. Record the merge target explicitly in the manifest
2. Set `human_gate_cleared=true`
3. Preserve a copy under a `_SUBMISSION_ARCHIVE/` path before merging
4. Update the manifest entry to `MERGED_INTO: [target file]` after completion

**Recommended: Option A.** Unless *AI & Society* has already rejected it and you  
are reabsorbing it into the corpus, this file should not merge.

---

## Decision 2 — The Master Tracker

**File:** `MASTER_PROJECT_TRACKER.csv`  
**Finding:** 54 rows with no outcome. 10 case slugs repeating 6× each, all resolving to DEFER.  
The tracker accurately records history. The problem it documents is that the run  
architecture did not change between restarts.

### Your decision

The tracker has two possible futures:

**Option A — Archive as append-only run log (recommended)**  
The tracker is doing its job: it's an accurate, append-only record of what happened.  
Change its role designation from "active decision surface" to "historical run log."  
- Add a header row: `# ARCHIVED — historical run log as of [date]. Not an active tracker.`  
- Create a fresh `PHAROS_TRACKER_V2.csv` with only the cases that are not DEFER-locked
- The V2 tracker starts from the resolved state, not from the restart history

**Option B — Attempt to resolve the DEFER cases**  
The 24 DEFER outcomes all share `contracts_missing_count: 8` — a fixed structural gap  
the v5 method could not close. The Consequence Binding Layer in v6.0 was designed  
specifically for this. If v6.0 is operational, the 10 unique slug cases could be  
re-evaluated under v6.0 rules and the DEFER outcomes potentially resolved.

This is a larger investment. Only pursue Option B if:
- v6.0 is fully specified and testable
- The DEFER cases are still relevant to the current patent or publication scope
- You want to demonstrate the method resolving cases it previously could not

**Recommended: Option A first, Option B if the DEFER cases matter to the patent scope.**

---

## Decision 3 — The regulatory corpus

**File:** `ai_governance_regulatory_docs.csv`  
**Finding:** Empty. Zero rows. The regulatory document evidence base does not exist.

### What this means
If PHAROS makes regulatory compliance claims (ISO 42001, EU AI Act, NIST AI RMF,  
Canadian AIDA/Voluntary Code), and those claims are not grounded in ingested  
regulatory text, they are assertion-only. In a patent or peer-review context,  
an assertion without a traceable corpus is a gap an examiner or reviewer will flag.

### Your decision

**Option A — Defer (regulatory corpus is not in scope)**  
If the current patent application or manuscript does not make specific regulatory  
compliance claims, the empty CSV is benign. Flag it: `out_of_scope_v1`.  
Do not spend time on it now.

**Option B — Build the corpus (regulatory claims are in scope)**  
If PHAROS makes or will make regulatory compliance claims:
1. Identify the 3–5 regulatory documents that matter most to the claim  
   (e.g., EU AI Act Article 13 on transparency, NIST AI RMF Govern function,  
   ISO 42001 Section 6 on AI risk management)
2. Ingest those documents into the archive inventory
3. Re-run the keyword extraction pass against them
4. Map PHAROS method components to specific regulatory requirements

This is a bounded task — 3–5 documents, one extraction pass. Not a research project.

**Recommended: Decide scope first. If the answer is "PHAROS positions against regulatory  
frameworks," do Option B. It is a bounded task and the gap is real.**

---

## Summary table

| Decision | File | Recommended | Blocks pipeline? |
|----------|------|-------------|-----------------|
| 1 — ai-anxiety manuscript | `ai-anxiety-*-2026-03-11.md` | Option A: PRESERVE, no merge | Yes — hard exit |
| 2 — Master Tracker | `MASTER_PROJECT_TRACKER.csv` | Option A: archive as run log, create V2 | No |
| 3 — Regulatory corpus | `ai_governance_regulatory_docs.csv` | Determine scope first | No |

---

## What's already done (no decision needed from you)

The following P1/P2 Codex items have been produced as part of this response:

| Item | Script | Status |
|------|--------|--------|
| Contamination filter — excludes 43 redistributed_copy + REVISE files | `pharos_pipeline_filter.py` | ✅ Ready |
| CompassAI/AurorAI extractor — preserves moving_parts.txt refs before merge | `compassai_aurorai_extractor.py` | ✅ Ready |
| Topology audit — determines if gap is missing ingestion or keyword mismatch | `topology_audit.py` | ✅ Ready |

Run order:
```bash
# 1. Topology audit (determine the nature of the gap)
python topology_audit.py \
  --inventory 00_archive_inventory.csv \
  --manifest  00_ARCHIVE_METADATA_MANIFEST.csv \
  --archive-dir /path/to/archive \
  --output topology_audit_report.md

# 2. Extract CompassAI/AurorAI refs BEFORE any merge of moving parts.txt
python compassai_aurorai_extractor.py \
  --source "moving parts.txt" \
  --output-dir ./extracted_evidence

# 3. Run pipeline filter on next evidence scan (dry-run first)
python pharos_pipeline_filter.py \
  --manifest 00_ARCHIVE_METADATA_MANIFEST.csv \
  --inventory 00_archive_inventory.csv \
  --output pharos_clean_manifest.csv \
  --dry-run
```

---

*Nothing tabled. Nothing deferred without a named decision. Three gates, three options each.*  
*The pipeline won't move until Decision 1 is recorded in the manifest.*

## Related

- [[Governance and PHAROS MOC]]
- [[SHOW-ME-WHAT-TO-DO]]
