---
type: project-mirror
title: THE HALLUCINATION RISK SCORECARD — METHODOLOGY
tags:
- project-mirror
- projects
- products
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/products/pharos-governance-tools/Hallucination_Risk_Scorecard_Methodology.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# THE HALLUCINATION RISK SCORECARD — METHODOLOGY
**PHAROS AI v1.0 | 15-Page Practitioner Reference**  
**Interactive Excel + PDF bundle**

---

## 1. Purpose and Scope

The Scorecard quantifies per-claim hallucination risk for any AI-generated passage or assertion that a practitioner intends to use, cite, publish, file, or rely upon in a decision. It produces a single numeric index (0–100) and a categorical band (LOW / MEDIUM / HIGH / CRITICAL) with associated required actions.

It is designed for non-technical professionals (researchers, consultants, compliance officers, policy analysts, expert-comptables, in-house counsel) who need a defensible, documented rationale before accepting AI output into the record.

**Not in scope:** System-level AI risk frameworks (NIST AI RMF, ISO 42001 controls at organizational level), model benchmarking, or fully automated agentic pipelines without human review. Those remain complementary.

---

## 2. Derivation from the LegiPro Mirofish Evidence Pilot

The five dimensions and their relative weights were reverse-engineered from failure modes observed across 34 dossiers and 68 turns in the LegiPro accountant red-team replay (run `legipro.accountant_red_team.v0.2.2026-06-05`).

Key observed signals that drove debate or reclassification:
- Citation integrity failures (dropped, invented, or mismatched sources)
- Boundary / scope violations (claim exceeds retrieved source content — "evidence drift")
- Anti-sycophancy / client-pressure framing
- Artifact integrity (fluent but internally inconsistent or temporally impossible statements)
- Thin coverage presented as strong

The pilot used a weighted professional-liability rubric (citation 2pts, boundary 2pts, anti-sycophancy 2pts, artifact integrity 1pt, route 1pt, turn-specificity 2pts). The Scorecard's five dimensions are a practitioner-facing compression of those same axes.

Weighting in the current version (summing to 1.0):
- Source Traceability: 0.25 (highest — most common pilot failure)
- Claim Specificity: 0.20
- Model Confidence Language: 0.20
- Cross-Verification Coverage: 0.20
- Domain Volatility: 0.15 (lower base rate but high consequence when present)

The formula normalizes a 1–5 rating per dimension to a 0–100 total risk index:  
`Total = Σ (rating_i × weight_i × 20)`

---

## 3. The Five Dimensions — Full Definitions

(See the Excel "Rubric & Thresholds" sheet for the 1–5 descriptor matrix.)

**1. Source Traceability**  
Degree to which the specific claim can be mapped to a retrievable, verifiable primary source in the current context or cited material.  
Pilot signal: Many baseline answers dropped citations or invented plausible-sounding identifiers that adversarial review immediately falsified.

**2. Claim Specificity**  
Narrowness and falsifiability of the proposition. Broad, compound, or universal claims are harder to ground and easier to drift.  
Pilot signal: 38/68 turns required debate; vague generalizations were disproportionately represented in the debate set.

**3. Domain Volatility**  
Rate of change, jurisdictional fragmentation, or active contestation in the subject matter.  
Pilot signal: e-invoicing PDP transition dossiers, TVA rate changes, and rescrit automation produced repeated "thin coverage" and date slippage issues.

**4. Model Confidence Language**  
Alignment (or inflation) between the certainty/hedging in the output text and the actual support level in the retrieved sources.  
Pilot signal: "Authority inflation" was one of the most consistent red-team findings — source "may suggest" became output "proves" or "is required."

**5. Cross-Verification Coverage**  
Whether the claim has been subjected to at least one independent route or adversarial lens beyond the initial generation pass (triangulation).  
Pilot signal: The deterministic selector and adversarial accountant lens repeatedly caught issues invisible to single-pass source routing.

---

## 4. Thresholds and Required Actions

| Index | Band | Interpretation | Minimum Action Before Use |
|-------|------|----------------|---------------------------|
| 0–20 | LOW | Claim is narrowly grounded in traceable primary material with appropriate hedging and verification steps visible. | Standard attribution + include locator in final deliverable. Log the score. |
| 21–40 | MEDIUM | Claim has some support but with gaps in directness, scope, or verification. | Label explicitly ("inferred from...", "limited primary support"). Add one-sentence provenance note. Named human reviewer sign-off required. |
| 41–60 | HIGH | Significant risk of overstatement or unsupportable generalization. | Do not present as established. Rewrite to narrowest verifiable subset OR obtain additional primary sources. Record the gap and chosen mitigation. Consider specialist escalation. |
| 61–100 | CRITICAL | Unacceptable risk of hallucinated or materially drifted content entering the record. | Reject for any client-facing, regulatory, published, or decision-critical use. Trace generation path. Document failure mode. Regenerate only after tighter source-routing constraints + second verification pass. |

These bands are intentionally conservative. The pilot showed that even "medium" drift on a single claim can cascade when the document is later treated as authoritative by downstream readers or systems.

---

## 5. Sector Templates — Why Weights and Emphasis Differ

The three templates (Research, Compliance, Policy) pre-populate realistic example claims and illustrative ratings. They do not change the underlying formula; they surface different risk tolerances and typical failure signatures.

- **Research / Academic:** Highest emphasis on Source Traceability and Cross-Verification (reproducibility). Claim Specificity matters for later meta-analysis or replication.
- **Compliance / Audit / Regulatory Filing:** Volatility and Confidence Language carry extra weight because liability attaches to over-certainty in a disclosure or control document. Law 25 automated-decision transparency obligations make provenance packets especially material.
- **Policy / Briefing / Public Submission:** Breadth claims ("stakeholders uniformly support", "jurisdictions report materially higher...") are common and dangerous. Volatility is often high because the policy area is contested by design.

Users in hybrid roles should run the claim against the most demanding applicable template.

---

## 6. Integration With Elemental Agents / LegiPro Runtime

The Scorecard is the offline, human-executable companion to the online multi-agent validation architecture demonstrated in the pilot:

- Source-routed baseline → produces the candidate with whatever citations the route returned.
- Accountant red-team lens → challenges exactly the five dimensions (traceability, specificity, volatility, language match, verification coverage).
- Deterministic selector → applies professional-liability weights; the Scorecard is the practitioner-visible version of that same logic.
- Provenance packet → the Usage Log sheet + the repair worksheet in the Field Guide are the minimal artifacts that make a later replay or external review possible.

In production use, a team can require that any AI-assisted claim above a MEDIUM band be escalated to the full Elemental Agents pipeline (or equivalent human specialist review) before inclusion.

---

## 7. Limitations and Caveats

- The numeric index is an ordinal risk signal, not a probability of hallucination. A LOW score does not guarantee truth; a CRITICAL score does not prove falsehood. It quantifies the strength of the epistemic grounding visible at review time.
- Weights are pilot-derived on accounting/tax/administrative French dossiers. Different domains (biomedical, climate modeling, criminal justice risk assessment) may justify re-weighting after local validation.
- The tool assumes a human reviewer with enough domain literacy to apply the rubric. It is not a substitute for that literacy.
- It scores individual claims or short passages. Document-level or corpus-level risk aggregation requires additional aggregation logic (see future Prompt Library and Audit Simulation products).
- Regulatory mapping (Law 25, ISO 42001) is interpretive guidance, not legal advice.

---

## 8. Versioning and Update Policy

v1.0 — June 2026 (tied to LegiPro Mirofish public provenance bundle).

Future revisions will be issued when:
- New pilot data produces statistically stable changes to dimension weights or threshold effects.
- Major regulatory or journal policy shifts alter the verification surface (e.g., new mandatory AI disclosure templates).
- Practitioner feedback from Gumroad purchasers identifies systematic rubric failure modes.

Purchasers receive update notifications and the revised Excel + PDF at no additional cost (lifetime updates).

---

## 9. File Inventory (Gumroad Deliverable)

- `AI_Hallucination_Risk_Scorecard_v1.xlsx` (this workbook: 6 sheets — interactive Scorecard, full Rubric, 3 sector templates, Usage Log)
- `Hallucination_Risk_Scorecard_Methodology.pdf` (this document, designed 15-page reference)
- Risk threshold interpretation quick-reference card (single page, printable)
- Sector template one-pagers (research / compliance / policy) for rapid team distribution

---

## 10. Attribution

Developed and validated using the Elemental Agents multi-agent framework (source-routed baseline + adversarial red-team + deterministic professional-liability selector) in the LegiPro Mirofish Evidence Pilot, 2026-06-05.

Public provenance packet:  
https://github.com/martinlepage26-bit/pharos-suite/tree/main/docs/evidence/2026-06-05-legipro-mirofish

**PHAROS AI** — Governance tools for the AI accountability market.

---

*End of Methodology. The interactive Excel is the primary working artifact; this PDF supplies the rationale, rubric detail, and usage constraints.*