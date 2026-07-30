---
type: index
tags: [vault-intake, raw-sources, documents-root, provenance, pharos]
created: 2026-04-28
updated: 2026-04-28
---

# Documents Root Loose Files Intake — 2026-04-28

Preservation-first intake of files found directly under `C:\Users\softinfo\Documents` rather than inside a project folder. This pass answered the question "are they in the vault?" and then captured the source-bearing files that were not already present as exact vault files.

## Verdict

- Loose root files inspected: 80.
- Byte-for-byte duplicates already inside EMERAULD: 0.
- Exact basename matches already inside EMERAULD: 0.
- Source-bearing files copied into this intake: 45.
- Converted Markdown sidecars produced: 47.
- Excluded files documented but not ingested: 35.

The vault already had partial synthesis for several items — especially the Hermes trackers, [[Alchemy of the Wound — Novel]], [[The Returning Light — Monograph]], [[CORPUS ou le génie de l'insistance — Novel]], [[Governance by Denial]], [[Complete Paper List — Martin Lepage Corpus]], and [[Recursive Governance Protocol — Theseus, Auryn, Hopf]] — but it did not preserve exact root-folder source copies.

## Raw Intake Root

- Raw copied files: `raw sources/Documents_root_loose_intake_2026-04-28/`
- Converted Markdown sidecars: `raw sources/Documents_root_loose_intake_2026-04-28/converted/`
- Copy manifest: `raw sources/Documents_root_loose_intake_2026-04-28/COPIED_FILES.tsv`
- Checksums: `raw sources/Documents_root_loose_intake_2026-04-28/SHA256SUMS.txt`
- Exclusion record: `raw sources/Documents_root_loose_intake_2026-04-28/EXCLUDED_FILES.md`

## Captured Clusters

### Protocols and Governance Stress Tests

Captured the complete Theseus/Auryn/Hopf protocol packet, the Argus audit tracker, and both provisional arbitration charter versions.

- `protocols/00_MASTER_EXPLAINER.txt`
- `protocols/01_THESEUS_TEMPLATE.txt`
- `protocols/02_THESEUS_ARCHIVE.txt`
- `protocols/03_THESEUS_QUESTIONS.txt`
- `protocols/04_AURYN_TEMPLATE.txt`
- `protocols/05_AURYN_ARCHIVE.txt`
- `protocols/06_AURYN_QUESTIONS.txt`
- `protocols/07_HOPF_TEMPLATE.txt`
- `protocols/08_HOPF_ARCHIVE.txt`
- `protocols/09_HOPF_QUESTIONS.txt`
- `protocols/ARGUS AUDIT TRACKER.md`
- `protocols/provisional-arbitration-charter.md`
- `protocols/provisional-arbitration-charter-v1.1.md`

Synthesis notes: [[Recursive Governance Protocol — Theseus, Auryn, Hopf]], [[Provisional Arbitration Charter — Argus Layer 9.5]], [[AGATHA Failure Pack — Theseus Continuity Stress Test]].

### Governance Public Market Pack

Captured public-positioning drafts, market-impact analysis, AI & Society title-page material, governance reference PDFs, and a root-folder ODT version of the Governance by Denial draft.

- `governance-public-market/ai_governance_public_statement.txt`
- `governance-public-market/ai_governance_public_statementlong.txt`
- `governance-public-market/if-gov-ai-2027-2028.md`
- `governance-public-market/FR-QC-.txt`
- `governance-public-market/Governance%20by%20Denial%20-%20revised%20working%20draft.docx_0.odt`
- `governance-public-market/Spec-1-ai Governance Engine.pdf`
- `governance-public-market/Agentic_AI_Autonomous_Intelligence_for_Complex_GoalsA_Comprehensive_Survey.pdf`
- `governance-public-market/Turing AI Ethics and Governance.pdf`
- `governance-public-market/untitled_2.odt`

Synthesis note: [[AI Governance Public Statement and Market Impact Pack]].

### Papers and Manuscripts

Captured root-folder copies or excerpts tied to the paper/creative corpus.

- `papers-and-manuscripts/Complete Paper List — Martin Lepage.txt`
- `papers-and-manuscripts/Alchemy of the Wound.docx`
- `papers-and-manuscripts/2025%20-%20Martin%20Lepage%20-%20THE%20RETURNING%20LIGHT%20-%20book_or_monograph.docx_0.odt`
- `papers-and-manuscripts/CORPUS ou le génie de l’insistance (1).md`
- `papers-and-manuscripts/Material CultureCharging Objects: Ritual, Artistic Practice, and the Crisis of Legitimacy`
- `papers-and-manuscripts/Ahmed, Sara. The Promise of Happine.txt`
- `papers-and-manuscripts/The_Kybalion.pdf`
- `papers-and-manuscripts/Hair.enw`

Existing graph anchors: [[Complete Paper List — Martin Lepage Corpus]], [[Alchemy of the Wound — Novel]], [[The Returning Light — Monograph]], [[CORPUS ou le génie de l'insistance — Novel]], [[Sealed Card Protocol — Legitimacy, Glitch, and Charging]], [[Historical Academic Portfolio — Pre-PHAROS Scholarly Work]].

### PHAROS Ops and Publishing

Captured cross-AI strategy trace material, April 2026 LinkedIn scheduling files, and a skill audit snapshot.

- `pharos-ops-publishing/Gemini a dit.txt`
- `pharos-ops-publishing/SKILL_AUDIT_2026-04-06.md`
- `pharos-ops-publishing/PHAROS_LinkedIn_Monthly_Routine_2026-04.md`
- `pharos-ops-publishing/LINKEDIN-SCHEDULE-NOW.md`
- `pharos-ops-publishing/linkedin-schedule.js`

Synthesis note: [[PHAROS LinkedIn April 2026 Publishing Routine]].

### AGATHA Stress Tests

Captured two failure transcripts from the root-level NEW AGATHA stress-test material.

- `agatha-stress-tests/FULL ST NEW AGATHA-FAIL.txt`
- `agatha-stress-tests/stress0test NEW AGATHA - FAIL.txt`

Synthesis note: [[AGATHA Failure Pack — Theseus Continuity Stress Test]].

### Hardware and Discovery

Captured the laptop hardware snapshot and a WSL discovery inventory that points back to PHAROS / AI / deterministic recursion artifacts.

- `hardware-system-reference/Laptop A.txt`
- `hardware-system-reference/& $envUSERPROFILEDesktopcompact_wsl.txt`

Synthesis note: [[Local Hardware and Discovery Snapshot — Laptop A]].

### Canonical Tracker Snapshots

The live tracker files remain canonical in `C:\Users\softinfo\Documents`; these copies are dated evidence snapshots only.

- `canonical-tracker-snapshots/CLIENT ACCOUNTS TRACKER.md`
- `canonical-tracker-snapshots/MASTER TRACKER (recreated from MASTER PACK 4).md`
- `canonical-tracker-snapshots/MASTER TRACKER (recreated from MASTER PACK 4).csv`
- `canonical-tracker-snapshots/PHAROS-AI CHANGE TRACKER.md`
- `canonical-tracker-snapshots/METHOD TRACKER.md`
- `canonical-tracker-snapshots/MARTIN-SITE CHANGE TRACKER.md`

Existing mirrors: [[CLIENT ACCOUNTS]], [[PHAROS SURFACE]], [[MARTIN SURFACE]], [[Hermes Dashboard — Professional Governance Tool]], [[Master Project Tracker — 2026]].

## Classification pass — 2026-07-10

The 51 captured Markdown files (originals + `converted/` sidecars) were **classified in place**: each now carries frontmatter (`type: raw-source`, `documents-root-intake` + a per-cluster tag, provenance, `classified: 2026-07-10`) and a `## Source classification` section backlinking its cluster synthesis note, MOC, and this intake index. All 51 are now **connected in the graph independent of the Orphan Index** (verified: loose intake 51/51 connected, 0 index-held). Bodies were preserved untouched (raw-source rule). Files were **not physically relocated** — moving raw/OCR captures into the curated `wiki/` corpus would degrade it and break the intake manifest/checksums; classification here is by tag + backlink, which is what removes them from "loose" in graph terms.

## Important Boundary

This was not a cleanup or deletion pass. Nothing was moved out of Documents, and excluded files were not deleted. The intake separates vault-worthy corpus material from private records, local utility byproducts, and untriaged visual assets.

## Whole-Vault Bridges

- [[L99 PHAROS Migration Artifacts 2026-04-19]] — This intake answers the earlier L99 gap where Theseus/Auryn/Hopf topology vocabulary had no archival footprint in the 116-file migration bundle.
- [[PHAROS Workspace Inventory 2026-04-18]] — The root-level AGATHA and home-directory sprawl flagged there now have exact intake evidence.
- [[SYSTEM CHECK]] and [[Local Hardware and Discovery Snapshot — Laptop A]] — local machine and WSL discovery context for the same Windows/WSL operating surface.
- [[PHAROS AI Lineage — Source of Truth]] and [[PHAROS Cross-AI Strategy Matrix]] — cross-AI prompt-forging traces, especially `Gemini a dit.txt`.
- [[PHAROS Licensing Prospectus]], [[First Method Paper — Recursive AI Governance as Executable Method]], and [[Recursive Governance Protocol — Theseus, Auryn, Hopf]] — the method/commercial route for the complete protocol packet.
- [[RECURSO — Recursive Governance Test Archive]], [[HELIX Session — Vaisseau de Thésée and the Tressed Lie (Live Run 2026-04-26)]], and [[AGATHA Failure Pack — Theseus Continuity Stress Test]] — stress-test/run-trace route.
- [[Historical Academic Portfolio — Pre-PHAROS Scholarly Work]], [[AI Society Manuscript — From AI Anxiety to Recursive Governance]], and [[APEX Papers — Research Archive Map]] — paper/manuscript and submission-apparatus route.

## Related

- [[Governance and PHAROS MOC]]
- [[Research and Papers MOC]]
- [[Writing and Novels MOC]]
- [[Personal and Projects MOC]]
- [[VAULT ADDITIONS TRACKER]]

## Wiki orphan repair — 2026-06-26 (council zero-orphan pass)

Inbound links added to clear wiki orphans:

- [[2026-04-25 — DG waiting on client picks — Source Note]]
- [[2026-04-25 — Reflexive Inhabitation Audit needs a live X — Source Note]]
- [[2026-04-25 — Santé-France Phase 0 — I am the blocker — Source Note]]
- [[2026-04-25 — Stop coding, clean, package, send — Source Note]]
- [[2026-04-25 — The lost-loop pattern — Source Note]]
- [[2026-05-06 — Patent agent email — provisional application contract + notes — Source Note]]
- [[24 Profitable Digital Products to Sell in 2026 (Start Selling Today) — Source Note]]
- [[AI is speeding into healthcare. Who should regulate it? — Source Note]]
- [[Alchimie et Histoire des Sciences — Source Note]]
- [[Cloudflare Workers Build Source Note 2026-05-13]]
- [[Complete solutions, not compromises — Source Note]]
- [[Email Député Guilbault AE — Source Note]]
- [[Formal-PHAROS-method-formal-structure-invention_disclosure — Source Note]]
- [[MIA PAPERS planes lyrics — Source Note]]
- [[REVISIONS - BRAIN PAPER JOURNAL — Source Note]]
- [[Reddit Data API Wiki — Source Note]]
- [[Skills as self-operators — Source Note]]
- [[The Ballad of the Witches' Road — Source Note]]
- [[WIP recruso paper — Source Note]]
- [[gaga gisease lyrics — Source Note]]
