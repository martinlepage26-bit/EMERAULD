---
type: wiki
title: PHAROS Recalibration — Unified Governance Architecture
aliases:
- PHAROS Recalibration — Unified Governance Architecture
tags:
- areas
- pharos
- governance
- pharos-recalibration-unified-governance-architecture-md
- runner
- dataset
- stage
- recalibration
- claim
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/PHAROS Recalibration — Unified Governance Architecture.md
backlink_count: 31
backlinks:
- '[[Areas/PHAROS/AI Governance Course — Ethics, Failure Modes, and Practice]]'
- '[[Areas/PHAROS/AI-2027 Critique — Relational AI and Vulnerability Monetization]]'
- '[[Areas/PHAROS/ANTHRO PHAROS — Anthropic vs PHAROS Governance Comparison]]'
- '[[Areas/Writing/Agatha Governance Memo — Recursive Governance Applied to Manuscript]]'
- '[[Areas/Writing/Algorithmic Agentic AI and Governance — From Hegemonic Fluency to the Ethics of Interruption]]'
- '[[Resources/Awesome Design Resources — Curated UI-UX Reference List]]'
- '[[Areas/PHAROS/Bonded Intelligence Under Constraint — The LOTUS Processor Framework]]'
- '[[Areas/Writing/First Method Paper — Recursive AI Governance as Executable Method]]'
- '[[wiki/Global Publication Search — PHAROS Method and Variants]]'
- '[[wiki/Governance Typology — Recursive AI Governance Taxonomy]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Governed Revision Loop — Responsible Self-Improving Agents]]'
- '[[wiki/Home]]'
- '[[wiki/LOTUS Model — Agency and Social Positioning]]'
- '[[wiki/Magic After Legitimacy — Charmed and the Governance of Female Power]]'
- '[[Resources/Master Bibliography — Références bibliographiques 2025]]'
- '[[wiki/OpenAI Governance Framework — Comparison with PHAROS]]'
- '[[wiki/PHAROS AI and Ethics Submission — Architecture Paper]]'
- '[[wiki/PHAROS Cross-AI Strategy Matrix]]'
- '[[Areas/PHAROS/PHAROS Method — Technical Reference]]'
- '[[wiki/PHAROS Scholarly Essay — Institutional Deployment Architecture]]'
- '[[wiki/Pourquoi rêver encore — Lecture allégorique et métaphysique d''Yvon Rivard]]'
- '[[wiki/Queering Neo-Pagan Magic — 2006 Paper]]'
- '[[wiki/RDAIG Method Editorial Consolidation — 2026]]'
- '[[wiki/Recursive AI Governance as Executable Method — The Very Long Narrative]]'
- '[[wiki/Recursive Governance Protocol — Theseus, Auryn, Hopf]]'
- '[[Resources/Recursive Governance Theory]]'
- '[[wiki/Social Compass Reviewer Response — Wicca and Agatha All Along]]'
- '[[wiki/Virtually Magical Literally — Queer Agency and the Digital Witch]]'
- '[[Areas/Writing/Why Be King Im Already a Queen — Book Project]]'
- '[[maps/PHAROS Method Map]]'
---

# PHAROS Recalibration — Unified Governance Architecture

## Summary
Technical governance specification comparing four PHAROS governance scripts (PHAROS-1, PHAROS-2, PHAROS-3, and governance_deterministic_runner) and producing a recalibration protocol that unifies them into a four-stage pipeline. Case reference: recurso-3c6266f59b. Key finding: the four scripts operate on fundamentally different governance objects (individual claims vs. file trees) with no formal handoff between them. Five structural gaps identified. Eight recalibration recommendations. Related to [[Recursive Deterministic AI Governance — Method and Paper]], [[PHAROS Invention Disclosure]], and [[RECURSO — Final Audit and Ethical Review]].

## Context
Source: `05_PHAROS_recalibration.docx`. This is an internal technical specification, attributed to Martin Lepage's governance system based on archive context and project fingerprint (3c6266f59b5a17f084fc1d241e8ec29d5bd67c7aa71ab63733f29eea1503d343). It reveals the engineering architecture behind the PHAROS method — the implementation layer appears Python-based (pandas DataFrames, `_tighten()` function); no CoffeeScript evidence appears in the script descriptions themselves. The methodological substrate underlying the four-stage unified architecture (Osirian death/rebirth recursion, gate-formula non-exception discipline) is documented in [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone]].

---

## Four Scripts Under Review

### PHAROS-1: Publication Gate Engine
- **Governance object**: Individual claim rows in a pandas DataFrame
- **Five deterministic gates**: Claim typing (R1/R2), consequence classification (R3/R4 with auto-escalation for legal and time-bound claims), hard blocking rules (Block 11.1-11.5), downgrade rules (R18/R19 language-evidence calibration), practice note labeling (R13)
- **Terminal states**: A (Publishable), B (Publishable with downgrade), C (Internal only), D (Blocked), E (Consent pending)
- **Structural weakness**: Monotonicity not enforced — later rules can loosen states set by earlier rules

### PHAROS-2: Drift, Stabilizer & Shadowmaster Engine
- **New mechanisms**:
  - Drift circuit breaker: quarantines claims whose token count exceeds 1.6x expected length
  - Stabilizer injection: forces "Applied Realism" data anchor on any E2 (conceptual) evidence claims
  - Shadowmaster prevention: scans audit notes for discretionary terminology ("vague," "clear enough," "consequential") — hard block if found
  - Automated triage: defers claims with missing source_id fields
- **New terminal states**: QUARANTINE (drift-isolated), AUTO_DEFER (missing mandatory field)
- **Structural limitation**: Runs as parallel track to PHAROS-1, not sequential — can produce contradictory terminal states with no arbitration mechanism

### PHAROS-3: Unified Superseding Engine
- **Key architectural advance**: The `_tighten()` function enforces **monotonic state progression**
  - Severity ordering: A=0, B=1, C=2, QUARANTINE=3, AUTO_DEFER=4, E=5, D=6
  - Once a claim reaches a restrictive state, no subsequent rule can loosen it
- **Ten stages** (complete pipeline): R1-R2 claim typing → R1-R2 Pass 2 re-derivation → full R1-R45 Agatha rule matrix → 9-point binary audit score → 14-layer routing → 7-dimensional governance basis vector → three-agent verification (Canon/Gov/Manuscript) → ethical triangulation (utilitarian/deontological/virtue) → dual-output generation → exception serialization
- **Additional enforcement**: R20 (absolute-term detection), R14 (hidden-factual splitting), R21 (authorship boundary checks), R25-R26 (recurring-claim validation against Master Reference List), X1-X7 exception routing with compensating controls

### governance_deterministic_runner: Dataset Intake Engine
- **Governance object**: File trees, not claims
- **Functions**: Deterministic inventory (sorted traversal, SHA-256 hashing, MIME classification), dataset fingerprint computation, risk factor detection (archives, executables, hidden files, duplicates, binaries, large files), risk-tier classification (low/medium/high/critical)
- **Output packet**: manifest, evidence packet, casefile, triage, votes, outcome, decision packet, pre-mortem, post-mortem
- **Terminal vocabulary**: APPROVE, APPROVE_WITH_CONDITIONS, DEFER, REJECT
- **Voting model**: Two voters — cabinet-epistemic-audit-rigor and voice-dissent-labor-legibility — currently always vote identically (structural flaw: dissent is impossible)

---

## Five Structural Gaps

**Gap 4.1 — The Granularity Seam**: No formal handoff between runner's dataset-level output and PHAROS claim-level input. Runner produces conditions and risk flags; PHAROS scripts expect evidence_class, claim_type, and source_level columns. A dataset can be APPROVE_WITH_CONDITIONS at the file level while containing individually-blocked claims.

**Gap 4.2 — Pass 1-2 Parallelism**: Without monotonic tightening, P1 and P2 can produce contradictory terminal states. Downstream consumers must choose which to honor — introducing exactly the kind of discretion the system is designed to eliminate.

**Gap 4.3 — Shadowmaster Vocabulary Drift**: PHAROS-2 scans for 3 loophole terms. PHAROS-3 expands to 6. If P2 runs standalone, narrower vocabulary permits discretionary language P3 would catch.

**Gap 4.4 — Runner Voting Model**: Both voters always vote identically — dissent is structurally impossible. The labor-legibility voice should be able to independently block or escalate when binary opacity conditions are met.

**Gap 4.5 — Missing Ethical Layer in Runner**: PHAROS-3 triangulates every claim against three ethical frameworks. Runner has no ethical dimension — passes ethically significant material (personal data, surveillance artifacts, contested IP) on structural criteria alone.

---

## Unified Severity Ordering (Post-Recalibration)

| Severity | Claim State | Dataset Equivalent |
|---|---|---|
| 0 | A (Publishable) | APPROVE |
| 1 | B (Publishable with downgrade) | APPROVE_WITH_CONDITIONS |
| 2 | C (Internal only) | (internal hold) |
| 3 | QUARANTINE | (no equivalent) |
| 4 | AUTO_DEFER | DEFER |
| 5 | E (Consent pending) | (consent gate) |
| 6 | D (Blocked) | REJECT |

---

## Recalibration Protocol — Four-Stage Unified Architecture

**Stage 0 (Dataset Intake)**: runner inventories file tree, computes fingerprints, detects structural risks, emits governance packet

**Stage 1 (Claim Extraction)**: New bridging module converts runner output into claim-ready rows — file records become claim rows with pre-populated evidence_class (from file category and hash receipt status), source_level (from file provenance), consequence (from risk tier)

**Stage 2 (Claim Governance)**: PHAROS-3 executes 10-stage pipeline (P1 and P2 no longer run independently)

**Stage 3 (Packet Reconciliation)**: Compares dataset-level outcome (Stage 0) against aggregate claim-level outcomes (Stage 2). If any claim is blocked (D) or consent-pending (E), dataset outcome is tightened to at minimum APPROVE_WITH_CONDITIONS

---

## Eight Recalibration Recommendations

1. Retire standalone execution of PHAROS-1 and PHAROS-2
2. Build Stage 1 bridging module (file records → claim rows)
3. Implement Stage 3 reconciliation module
4. Expand runner voting model for independent dissent
5. Add content_sensitivity_flags to runner file records
6. Canonicalize shadowmaster vocabulary as 6-term set
7. Publish unified severity ordering (0-6) as governance constant
8. Implement hash-chain continuity between governance runs

---

## Non-Exceptionable Gates

The following gates cannot be overridden by any exception routing or compensating control:
- R22 (consent)
- R9 (legal source hierarchy)
- R36 (fabrication/laundering/distortion)

These three gates enforce hard limits that no governance exception can bypass.

---

## Insights

- The Granularity Seam (Gap 4.1) is the most important finding: a file can be APPROVE_WITH_CONDITIONS at the dataset level while containing D-blocked claims. Without the bridging module, the governance system produces inconsistent decisions at different levels of analysis — and neither level is aware of the other's findings
- The identical-voting structural flaw (Gap 4.4) is the runner's version of the SHADOWMASTER problem: a system that cannot produce dissent is a system that cannot catch itself being wrong. The labor-legibility voice needs independent blocking authority precisely because the epistemic-audit voice may be blind to the same structural features that a labor perspective would catch
- PHAROS-3's monotonic `_tighten()` function is the most important architectural contribution in the script set: once a claim reaches a restrictive state, nothing can loosen it. This is the governance equivalent of the PHAROS pipeline's `blocked_not_ready` ceiling rule — severity escalates, never de-escalates, without explicit adjudication
- The 20-gate sequence (G0-G19) with three non-exceptionable gates (R22/R9/R36) provides the clearest picture of what "deterministic" means in the PHAROS implementation: 17 gates are exceptionable (compensating controls available), 3 are absolute. This is the right architecture — not everything can be exceptional

## Open Questions

- Has the Stage 1 bridging module been built? What is the implementation status of the recalibration recommendations?
- What is the "Agatha rule matrix" (R1-R45 referenced in PHAROS-3)? Is this related to the Agatha AI persona from [[Emotional Alliance vs. Evidentiary Discipline in AI]]?
- How does the 7-dimensional governance basis vector work? What are the seven dimensions?
- What is the current implementation language and deployment environment for the PHAROS scripts?

## Sources
- `raw sources/05_PHAROS_recalibration.docx`
- Related: [[Recursive Deterministic AI Governance — Method and Paper]]
- Related: [[PHAROS Invention Disclosure]]
- Related: [[RECURSO — Final Audit and Ethical Review]]
- Related: [[PHAROS Runbook SOP]]

## Related

- [[engine.py]]
