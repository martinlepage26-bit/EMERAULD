---
type: artifact
title: PHAROS Archive — CSV Diagnostic Report
aliases:
- artifacts/2026-04-19-pharos-migration-pr4/docs/CSV_DIAGNOSTIC_REPORT
tags:
- artifact
- pharos
- archive
- artifacts
- 2026-04-19-pharos-migration-pr4
- hits
- keyword
- topology
- paragraphs
- color-green
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/2026-04-19-pharos-migration-pr4/docs/CSV_DIAGNOSTIC_REPORT.md
backlink_count: 4
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/L99 PHAROS Migration Artifacts 2026-04-19]]'
- '[[wiki/archive/Orphan Index — Post Dr Sort Rename Residuals — 2026-05-06]]'
- '[[artifacts/2026-04-19-pharos-migration-pr4/_manifest/MANIFEST]]'
---

# PHAROS Archive — CSV Diagnostic Report
See also [[Governance and PHAROS MOC]].
**Generated:** 2026-04-19  
**Scope:** Five project CSVs — full read, cross-reference, anomaly detection, governance implications  
**Standard:** Direct evidence only. Inference labelled. Speculation excluded.

---

## 1. `00_archive_inventory.csv` — 116 files

### Composition
| Dimension | Value |
|-----------|-------|
| Total files inventoried | 116 |
| Parse status OK | 112 |
| Parse status `ok_zipxml` (ODT/DOCX treated as zip) | 3 |
| Parse status `skipped_unparsed` | 1 (PNG) |
| Files with no extracted text | 0 |

**Extensions:** `.md` (57), `.txt` (19), `.yaml` (14), `.html` (6), `.py` (5), `.pdf` (4), `.docx` (3), `.odt` (3), `.css` (3), `.svg` (1), `.png` (1)

### Structural observation
57 of 116 files are `.md` — over half the archive. This is consistent with the Codex/Claude division of labour where Claude outputs `.md` documents as governance artifacts. The 14 `.yaml` files align with the skill-distribution layer (SKILL.md ecosystem). The 3 ODT files (`Alambic`, `MASTER ETHICS METHODS`, `THE VIOLET GEM`) were parsed as zipxml — content is accessible but format detection cannot be trusted, which is consistent with the known principle that **file extensions cannot be relied upon in this archive.**

### Parse anomalies
- `speech/assets/speech.png` — skipped. Not a governance artifact. Benign.
- Three ODTs parsed as zipxml — successfully extracted, no content loss.

---

## 2. `00_ARCHIVE_METADATA_MANIFEST.csv` — 116 files, 21 columns

### Revision status distribution
| Status | Count |
|--------|-------|
| `redistributed_copy` | 43 |
| `original` | 40 |
| `revised` | 12 |
| `distributed_snapshot` | 12 |
| `superseded_but_important` | 3 |
| `cleaned_derivative` | 2 |
| `near_final` | 2 |
| `expanded` | 1 |
| `compressed_derivative` | 1 |

**Structural concern:** 43 files classified as `redistributed_copy`. This is the largest single category. Redistributed copies inflating the archive count is the same input-contamination problem documented in the governance storyboard (the Baseline Loop where historical `governance_master_runs`, `debug_runs`, etc., were scanned as fresh evidence). The archive's composition is majority-noise by revision status.

### Evidence status
| Status | Count |
|--------|-------|
| `supporting_implementation_artifact` | 47 |
| `supporting_archive_artifact` | 33 |
| `source_bearing_artifact` | 17 |
| `distribution_artifact` | 14 |
| `interpretive_or_generated_derivative` | 4 |
| `implementation_surface_evidence` | 1 |

Only **17 of 116 files** are `source_bearing_artifact` — the only category that can carry primary evidentiary weight in a patent or peer-review context. 80 files are purely supporting or implementation artifacts. The archive is structurally thin on primary evidence.

### Confidence
| Level | Count |
|-------|-------|
| `bounded_low` | 76 |
| `medium` | 22 |
| `high` | 18 |

**76 files (65.5%) are `bounded_low` confidence.** This is the dominant epistemic state of the archive. It is consistent with the Option B decision (patent the method architecture without performance numbers) — the evidence base cannot support performance claims.

### Action-required files

**REVISE_AND_STRENGTHEN (5 files)** — all `bounded_low` confidence:
- `CONSOLIDATED-PACK.txt` — supporting archive artifact
- `CODEX FINAL TRUE.txt` — superseded interpretive derivative
- `Grok INSERT MASTER PACK-AG.txt` — interpretive derivative
- `GROK+AGATAH=======Dottie qwjo do yo.txt` — interpretive derivative
- `Mobius_Protocol_Template.txt` — supporting archive artifact

**Inference:** The REVISE_AND_STRENGTHEN files are AI-output artifacts (Grok, Codex) that have not been brought into alignment with the locked PHAROS v5/v6 method. They remain in a superseded interpretive state. Risk: if these are scanned in future pipeline runs without filtering, they re-introduce method-drift into the evidence base (same contamination mechanism documented in the storyboard).

**MERGE_WITH_RELATED_FILE (4 files):**
- `EXPLAIN PHASE 1 PASS.txt` — `recurso` hits: 5. Substantive Phase 1 content.
- `ai-anxiety-recursive-governance-ai-society-aligned-2026-03-11.md` — **source_bearing, high confidence, MERGE flagged.** This is the *AI & Society* manuscript. It is flagged MERGE, but it is your highest-confidence source-bearing artifact. The merge decision warrants a human gate — this file should not be automatically merged into another without preserving its provenance as a standalone submission document.
- `Here's a one-page markdown version.txt` — cleaned derivative, medium confidence. Low risk.
- `moving parts.txt` — holds 8 hits for `impl_pharos_govern_ai` plus 1 each for `impl_compassai` and `impl_aurorai`. This is the only file in the archive with meaningful CompassAI/AurorAI coverage. Merging it without capturing those implementation references would delete the only keyword evidence for those implementation surfaces.

**DEPRECATED_BUT_RETAINED (2 files):**
- `BOOB codex resume 019d067d-e829-700.txt` — `implementation_surface_evidence`, high confidence. Retained as an implementation record. Correct decision.
- `This paper May NOT exist - DRAFTENDLOOP.txt` — `supporting_archive_artifact`, medium confidence. Retained as an archival trace. Correct decision.

### Source-bearing files, high confidence (17 total)
The full set of files that can carry primary evidentiary weight:

| File | Action | Recursive role |
|------|--------|----------------|
| `2017 - Charging Objects Ritual, Artistic Practice...docx` | PRESERVE_AND_LIGHTLY_CLEAN | corpus_substrate_or_ignition_signal |
| `SEALEDCARD.pdf` | PRESERVE_AS_IS | supporting_archive_layer |
| `MARTIN voice specs.pdf` | PRESERVE_AS_IS | supporting_archive_layer |
| `THE VIOLET GEM (1).odt` | PRESERVE_AS_IS | protocolizing_layer |
| `Alambic.odt` | PRESERVE_AS_IS | governance_rewrite_or_feedback_layer |
| `2004 - Title The Sealed Card Protocol...docx` | PRESERVE_AND_LIGHTLY_CLEAN | protocolizing_layer |
| `Agathav4.1.docx` | PRESERVE_AND_LIGHTLY_CLEAN | corpus_substrate_or_ignition_signal |
| `PEER_REVIEW_READY_MANUSCRIPT_EXPANDED_300.md` | PRESERVE_AND_LIGHTLY_CLEAN | governance_rewrite_or_feedback_layer |
| `MASTER ETHICS METHODS.odt` | PRESERVE_AS_IS | supporting_archive_layer |
| `ai-anxiety-recursive-governance-ai-society-aligned-2026-03-11.md` | **MERGE** ← human gate required | governance_rewrite_or_feedback_layer |
| `RDAIG_method_editorial_consolidation_2026-03-14.md` | PRESERVE_AS_IS | governance_rewrite_or_feedback_layer |
| `RDAIG_governance_test_2026-03-14.md` | PRESERVE_AS_IS | governance_rewrite_or_feedback_layer |
| `SCHOLARLY_PACKET_MANIFEST.md` | PRESERVE_AS_IS | supporting_archive_layer |
| `AI GOV CONSTITUTION.pdf` | PRESERVE_AS_IS | governance_rewrite_or_feedback_layer |
| `From AI Anxiety to Recursive Governance...md` | PRESERVE_AND_LIGHTLY_CLEAN | supporting_archive_layer |
| `AI_Governance_Whos_the_Boob_Whos_the_Trap_40k_Target.md` | PRESERVE_AS_IS | supporting_archive_layer |
| `discursive-authority-recursive-pressure-v2.docx.pdf` | PRESERVE_AND_LIGHTLY_CLEAN | implementation_surface_layer |

---

## 3. `00_KEYWORD_EVIDENCE_MATRIX.csv` — 116 files × 40 keywords

### Top 15 keywords by total archive hits
| Keyword | Total hits |
|---------|-----------|
| `first_order_charge` | 168 |
| `impl_pharos_govern_ai` | 75 |
| `forge_hephaistos` | 60 |
| `first_order_glitch` | 55 |
| `buffy` | 50 |
| `lab_wheels_of_will` | 42 |
| `recurso` | 37 |
| `distribution_skill_md` | 24 |
| `protocol_sealed_card` | 21 |
| `first_order_boobytrap` | 21 |
| `lab_hexa` | 20 |
| `ignition_witches_road` | 11 |
| `impl_echo` | 11 |
| `ignition_agatha_all_along` | 10 |
| `corpus_discursive_authority` | 9 |

### Critical coverage gaps
The following key terms have near-zero coverage across 116 files — meaning the concepts exist in the method but are barely traceable in the archive:

| Keyword | Files with hits | Files with zero hits |
|---------|-----------------|---------------------|
| `protocol_master_key` | **1** (`CODEX FINAL TRUE.txt`: 1 hit) | 115/116 |
| `impl_compassai` | **3** (`After reboot checklist.txt`, `Here's a one-page markdown version.txt`, `moving parts.txt`) | 113/116 |
| `impl_aurorai` | **3** (same files) | 113/116 |
| `protocol_sealed_card` | **3** (concentrated in 2004 docx) | 113/116 |
| `forge_hephaistos` | **2** files hold all 60 hits | 114/116 |
| `topology_theseus` | **0** | 116/116 |
| `topology_auryn` | **0** | 116/116 |
| `topology_hopf` | **0** | 116/116 |

**Critical finding:** `topology_theseus`, `topology_auryn`, and `topology_hopf` have **zero hits across the entire 116-file archive.** These are method-critical concepts (named in the method documentation as `03_TOPOLOGY_THESEUS_AURYN_HOPF_LIMIT_MAP.md`) that do not appear in any extracted text. Either (a) the files containing them were not ingested, or (b) the keyword terms used in extraction do not match the actual terminology in those files. This is a hard evidence gap, not a bounded gap.

**CompassAI/AurorAI coverage:** Only 3 files mention these implementation surfaces at all, and all three are in the SUPPORTING_ARCHIVE_ONLY or MERGE-flagged category. The implementation surfaces have almost no archival trace.

### Top evidence file by keyword spread
`2004 - Title The Sealed Card Protocol...docx` — 78 total hits across 9 keyword dimensions:
- `first_order_charge`: 27, `first_order_glitch`: 22, `protocol_sealed_card`: 12, `lab_wheels_of_will`: 4, `ignition_agatha_all_along`: 3, `lab_hexa`: 3, `impl_echo`: 3, `buffy`: 3, `impl_pharos_govern_ai`: 1

This is the single most multi-dimensional evidence file in the archive by keyword spread.

`index.html` — 43 hits across 13 keyword dimensions. The highest dimensional spread of any file. This is the website/SPA index, which suggests it contains method vocabulary embedded in UI layer — another reason the JS SPA architecture is a structural problem (method vocabulary is trapped in a non-indexable surface).

---

## 4. `MASTER_TRACKER_recreated_from_MASTER_PACK_4.csv` — 91 rows, 41 unique case slugs

### Outcome distribution
| Outcome | Count |
|---------|-------|
| Empty (no outcome recorded) | 54 |
| `DEFER` | 24 |
| `APPROVE_WITH_CONDITIONS` | 13 |

**54 of 91 rows have no outcome.** This is not a gap in recording — it is structural. The tracker was recreated from MASTER PACK 4, and the empty rows represent run groups that were iterated but never evaluated to a terminal state. The 54 empty rows are the fossil record of aborted or abandoned run cycles.

### Run group structure
The tracker records 12 distinct run groups, all under a `SCRIPTS/Paper outcomes` prefix plus `governance_runs`. The repetition pattern (RESTART-2, RESTART-3, RESTART-4, ROUND2, plus their TEST variants) confirms the storyboard finding: multiple restarts attempting the same master pass without resolving the underlying input contamination.

### Duplicate slug problem
Ten case slugs appear exactly 6 times each across different run groups. Every row for `ag-runner-md-with-readme-key-2426d4903d`, `kingmalek-md-readme-zip-afaf0136e9`, `parallel-kingmalek-wrapper-5861bc1349`, and `debug-kingmalek-smoke-16a6b2387f` resolves to DEFER. The same case, deferred six times across six run groups, is not a coverage gap — it is a structural failure that replicated itself. The outcome is not unknown; it is known and locked at DEFER across all six instances.

### Risk tier
All 24 DEFER outcomes are classified `critical` risk. All 13 APPROVE_WITH_CONDITIONS are `high` risk. There are no `medium` or `low` risk outcomes in the cases that have any outcome at all.

### Missing contracts
The DEFER cases consistently show `contracts_missing_count: 8` — the same number across all six instances of each slug. This is not random variation; it is a fixed structural gap that the method architecture at the time could not resolve. The Consequence Binding Layer introduced in v6.0 was specifically designed to address this: governance evaluations that terminate without binding findings to system-level operations cannot close contracts.

---

## 5. `RECURSIVE_VOICEPHASE1_paragraph_theme_vectors.csv` — 874 paragraphs

### Theme distribution
| Dominant theme | Paragraphs | Avg tokens |
|----------------|-----------|------------|
| `none` | 351 (40.2%) | 4 avg |
| `evidence_receipts` | 201 (23.0%) | 12 avg |
| `control_governance` | 74 (8.5%) | 10 avg |
| `consent_support` | 73 (8.4%) | 12 avg |
| `scientific_protocol` | 70 (8.0%) | 12 avg |
| `continuity_anchor` | 56 (6.4%) | 14 avg |
| `authorship_boundary` | 25 (2.9%) | 12 avg |
| `accessibility_pacing` | 24 (2.7%) | 10 avg |

**40.2% of paragraphs have dominant theme `none`**, but their average token count is only 4 — these are structural fragments (headers, whitespace, short transitions), not substantive unclassified content. The substantive paragraph set is approximately 523 paragraphs.

### Binary flag rates
| Flag | Paragraphs flagged | Rate |
|------|--------------------|------|
| `control_governance` | 172 | 19.7% |
| `evidence_receipts` | 151 | 17.3% |
| `scientific_protocol` | 86 | 9.8% |
| `consent_support` | 71 | 8.1% |
| `continuity_anchor` | 51 | 5.8% |
| `authorship_boundary` | 33 | 3.8% |
| `accessibility_pacing` | 26 | 3.0% |

`control_governance` and `evidence_receipts` are the two most frequently flagged dimensions. The binary flag rates differ substantially from the dominant-theme counts because paragraphs carry multiple flags simultaneously — the dominant-theme assignment selects one, but the binary columns record co-presence.

### High-density paragraphs (4+ flags simultaneously)
129 paragraphs carry 4 or more simultaneous flags. These are the structurally richest paragraphs — carrying control, evidence, consent, and continuity signals together. The opening paragraphs (ids 3, 5, 25, 36, 38) confirm the Phase 1 voice spec anchors continuity and evidence receipts at the document opening, consistent with the PHAROS standard of evidence-first structuring.

### Authorship boundary signal
33 paragraphs carry the `authorship_boundary` flag. Sampling these shows they cluster around:
- The Agatha system's role boundary ("says what the scholar may not say to themselves")
- The opt-in anchoring protocol ("Anchoring Mode only when scholar explicitly asks")
- Failure conditions for authorship drift ("system introduces claims, tone, or judgments that materially distort the principal")
- Periodic review requirements for the protocol itself

These are the operational authorship controls of the voice spec — they define where the AI agent's output authority terminates and the scholar's authority begins. Consistent with PHAROS Component requirements for operator-declared role boundaries.

---

## 6. `ai_governance_text_hits.csv` — 786 rows

### Structure finding
Every row has a unique `Path` value. This is **not** a file-level hit aggregator — it is a line-level hit log where each row records one matching line from one file. But since every Path appears exactly once, the 786 rows represent 786 unique file paths, each contributing one matching line.

The source files include:
- TeamViewer log files (system noise)
- VSCode extension localization bundles (system noise)
- Governance documents on the Desktop (`FINAL1gpt Prompt tp Codex.txt`, `MIRO-From AI Anxiety to Recursive Govern.txt`, `VOODOO-defered authority.txt`, `WHEN THE CAT STOPS THE LAST PASS.md`)
- Codex workspace files (`MASTER_PROJECT_TRACKER_2026-03-17.md`, `ComPassAI_VisualKnowledgeMap_README.md`, `deep-research-report.md`, `final_adjudication (1).md`)
- The `ai_governance_text_hits.csv` itself appears as a hit source — it contains a reference to AI governance content in its own header row (self-referential hit)

**`ai_governance_regulatory_docs.csv` is empty (0 rows).** The regulatory document corpus has no content. Either the collection step was not executed or the output file was generated with no input.

---

## Cross-archive findings

### 1. Topology terms are absent from the archive (hard gap)
`topology_theseus`, `topology_auryn`, `topology_hopf` — zero keyword hits across all 116 files. The `03_TOPOLOGY_*` documents in the project reference these terms but they were either not ingested into the keyword extraction pass or the extractor used different search strings. Until this is resolved, the topology layer has no archival keyword footprint. This is a stronger gap than the percentage claims (Option B already addresses those); the topology terms are architectural, not empirical.

### 2. CompassAI/AurorAI have effectively no archive trace
The two client-facing tools have keyword evidence in only 3 files, all of which are in the MERGE or SUPPORTING_ARCHIVE_ONLY category. `moving parts.txt` is the single file carrying meaningful implementation keyword density for both tools. If that file is merged and the merge is not done with explicit provenance preservation, the archive loses its only keyword-traceable evidence for those implementation surfaces.

### 3. The `ai-anxiety` manuscript is flagged MERGE but is source-bearing and high-confidence
This is a conflict in the action decisions. A MERGE decision on a source-bearing, high-confidence, near-final manuscript that has been submitted to *AI & Society* is not an ordinary merge operation. It requires a human gate, not automated pipeline execution.

### 4. Master Tracker slugs repeat 6x with identical outcomes
The tracker structure records the same 10 case slugs six times each, all resolving to DEFER (or empty). This is not a data integrity problem in the tracker itself — it is an accurate record of how many times the same runs were re-executed without resolving the underlying gap. The tracker is working correctly as an append-only log. The problem it documents is that the run architecture did not change between restarts.

### 5. Recursive Voice Phase 1 authorship boundary controls are operational
The 33 `authorship_boundary` paragraphs represent a functioning authorship-control protocol in the voice spec. The protocol contains explicit failure conditions, opt-in anchoring requirements, and periodic review triggers. These are not aspirational — they are implemented as paragraph-level governance constraints in the Phase 1 document corpus.

---

## Action summary

| Priority | Finding | Required action | Who |
|----------|---------|----------------|-----|
| **P1 — Hard gap** | `topology_theseus/auryn/hopf` zero hits | Verify whether topology docs were ingested; if yes, check keyword extraction strings; if no, ingest and re-run | Codex |
| **P1 — Evidence risk** | `ai-anxiety` manuscript flagged MERGE | Insert human gate before any merge; preserve as standalone submission document with provenance | Martin |
| **P1 — Coverage risk** | `moving parts.txt` MERGE-flagged but sole CompassAI/AurorAI keyword carrier | Extract and re-home CompassAI/AurorAI references before merge; do not merge and lose the only implementation trace | Codex |
| **P2 — Contamination** | 43 `redistributed_copy` files in archive | Apply systematic filter in future pipeline runs to exclude redistributed copies from fresh evidence scans | Codex |
| **P2 — Contamination** | REVISE_AND_STRENGTHEN files are Grok/Codex interpretive derivatives | Do not include these as source evidence in any patent or peer-review artifact; label as AI-interpretive derivatives with explicit agent attribution | Martin |
| **P2 — Tracker integrity** | 54 rows with no outcome, 10 slugs repeating 6× | Archive the MASTER_TRACKER as a historical run log, not an active decision surface | Martin |
| **P3 — Regulatory corpus** | `ai_governance_regulatory_docs.csv` is empty | Determine whether the regulatory document collection step was executed; if not, flag as a missing evidence source | Martin |
| **P3 — Archive enrichment** | `first_order_charge` dominates keyword hits (168) but topology terms are zero | The archive is heavily weighted toward first-order analysis and underweight on topological/formal method claims | Consider for patent framing |
