---
type: wiki
aliases: [RDAIG, Recursive Deterministic AI Governance, Recursive Governance Method, PHAROS pipeline, "PHAROS Method — Recursive Governance", PHAROS, "Recursive Governance Method — Skill Corpus Entry"]
tags: [pharos, governance, method, reference]
status: active
created: 2026-04-16
updated: 2026-04-16
---

# PHAROS Method — Technical Reference

## Summary

PHAROS (Recursive Deterministic AI Governance) is a deterministic, auditable pipeline for governing AI inference outputs through recursive corpus transformation, bounded admissibility rules, and consequence-bound promotion decisions. Conceived by [[Martin Lepage — Professional Profile|Martin Lepage]] (method architecture) and [[Founder Charter — Lepage and Stocker|Danny Stocker]] (infrastructure binding); filed as a joint invention 2026-04-01. The canonical IP document is [[PHAROS Invention Disclosure]]. This note is the consolidated technical reference for the method — pipeline, target constructs, rollup logic, implementation state, and naming risk.

**Methodological substrate:** The recursive pipeline operationalizes the Osirian death/rebirth structure named in the [[Mort et Naissance et L'Ombre et le Double — MA Thesis on Yvon Rivard (Université Laval, 2010)|2010 MA thesis]] (p. 81); the trial structure of Thomas's *procès* before the Council (MA pp. 17–19) is the structural ancestor of the adjudication protocol. See [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone]] for the architectural genealogy.

## Context

PHAROS is the core output of the [[Governance and PHAROS MOC|PHAROS governance research program]]. It is not a scoring system, a safety filter, or a policy checklist. It is a *method* — a reproducible procedural pathway that produces the same governance decision from the same inputs regardless of who or what executes it. The practitioner-facing procedure is in [[PHAROS Runbook SOP]]; the scholarly treatment is in [[Recursive Deterministic AI Governance — Method and Paper]]; the engineering architecture is in [[PHAROS Recalibration — Unified Governance Architecture]].

The operational closure discipline is captured in [[Delta Closure Frame — Conditions, Actors, Constraints]]: a gap closes only when the current condition, target condition, metric, deadline, decision-maker, responsible actors, and constraints/dependencies are named.

The [[InfraFabric Architecture]] is the infrastructure layer that receives consequence bindings from the pipeline's promotion decisions.

## Details

### 10-Stage Pipeline

| Stage | Name | Function |
|---|---|---|
| 1 | Corpus Formation | Assemble bounded input corpus; apply admissibility boundary |
| 2 | Admissibility Classification | Classify each item: admissible / adjacent / excluded |
| 3 | Target Construct Mapping | Map corpus items to TC-1 through TC-5 |
| 4 | Recursive Transformation | Apply recursive rewriting passes; track drift across passes |
| 5 | Failure Harvesting | Extract and classify failures as positive governance evidence |
| 6 | Drift Detection | Identify authority drift, path-dependence, fluency inflation |
| 7 | Deterministic Rollup | Apply 12-rule rollup logic → promotion status |
| 8 | Adjudication | Apply 6-step adjudication protocol to contested items |
| 9 | Consequence Binding | Map promotion decision to [[InfraFabric Architecture]] module consequences |
| 10 | Promotion / No-Promote | Final dispositioned output with provenance chain |

---

### Four Target Constructs

- **TC-1 — Inferential Carry-Through**: does the inference chain remain intact across recursive passes? Tests whether the system reasons or pattern-matches to expected outputs.
- **TC-2 — Revision Fidelity**: does the system revise under new evidence without anchoring (refusing revision) or over-drifting (conforming to latest input)?
- **TC-3 — Perturbation Robustness**: do governance decisions hold under adversarial context-switch, rephrasing, or authority re-framing? Tests whether decisions are grounded in corpus or in presentation.
- **TC-5 — Terminal Path-Dependence**: is the final output shaped by input *sequence* more than input *content*? High path-dependence is a governance failure.

*TC-4 is absent in the official filing (2026-04-01); present as "Terminal Path-Dependence" in the v6 patent counsel draft before renumbering. The gap is a declared incomplete, not an oversight — `incomplete` status exists for exactly this purpose.*

---

### Six Promotion Statuses (12-rule deterministic rollup)

| Status | Meaning |
|---|---|
| `ready_full` | All TCs passed; full promotion authorized |
| `ready_with_bounded_gaps` | Passed with declared gaps; promotion authorized within named bounds |
| `needs_revision_before_promotion` | Failed one or more TCs; revision required before resubmission |
| `blocked_not_ready` | Active named blocker; must be resolved before any promotion |
| `failed` | Governance failure; output cannot be promoted in any form |
| `incomplete` | Pipeline not fully executed; no status can be assigned |

`blocked_not_ready` is the ceiling rule: it overrides all other statuses and hard-escalates to human operator via `if.switchboard`. Severity only escalates — the `_tighten()` function in [[PHAROS Recalibration — Unified Governance Architecture|PHAROS-3]] enforces monotonic state progression.

---

### Consequence Binding Map

Each promotion status triggers specific [[InfraFabric Architecture]] module responses automatically — governance is not advisory:

| Status | InfraFabric Consequence |
|---|---|
| `ready_full` | `if.gov` clears; `if.api` routes to production; `if.trace` logs provenance |
| `ready_with_bounded_gaps` | `if.gov` clears with gap annotation; `if.blackboard` holds gap declaration; `if.api` routes with bounded flag |
| `needs_revision_before_promotion` | `if.gov` holds; `if.bus` routes back to Stage 4; `if.trace` logs revision trigger |
| `blocked_not_ready` | `if.gov` hard-holds; `if.switchboard` escalates to human operator; `if.trace` logs blocker identity |
| `failed` | `if.gov` rejects; `if.knowledge` harvests failure as evidence; `if.trace` logs failure provenance |
| `incomplete` | `if.gov` holds pending completion; `if.context` preserves state for continuation |

---

### Three Non-Exceptionable Gates

From the PHAROS-3 implementation (see [[PHAROS Recalibration — Unified Governance Architecture]]):

- **R22** — consent
- **R9** — legal source hierarchy
- **R36** — fabrication / laundering / distortion

No compensating control can bypass these. 17 other gates are exceptionable; these three are absolute hard limits.

---

### Implementation Layer

Python-based. Four scripts currently in the system:

- **PHAROS-1** — Publication Gate Engine: 5 deterministic gates, terminal states A/B/C/D/E. Weakness: monotonicity not enforced.
- **PHAROS-2** — Drift, Stabilizer & Shadowmaster Engine: adds drift circuit breaker, stabilizer injection, shadowmaster term scan, auto-defer on missing fields. Runs as parallel track to PHAROS-1 — no arbitration mechanism between them.
- **PHAROS-3** — Unified Superseding Engine: 10-stage full pipeline; `_tighten()` enforces monotonic severity ordering; R20 (absolute-term detection), R25-R26 (recurring-claim validation against Master Reference List), X1-X7 exception routing with compensating controls.
- **governance_deterministic_runner** — Dataset Intake Engine: operates on file trees (not claims); produces manifest, evidence packet, casefile, triage, votes, outcome, decision packet, pre-mortem, post-mortem. Terminal vocabulary: APPROVE / APPROVE_WITH_CONDITIONS / DEFER / REJECT.

The recalibration proposes retiring standalone PHAROS-1 and PHAROS-2 in favor of a unified four-stage architecture: dataset intake → claim extraction bridging module → PHAROS-3 → packet reconciliation. See [[PHAROS Recalibration — Unified Governance Architecture]] for the five structural gaps and eight recommendations.

---

### Naming and Prior-Art Risk

The [[Global Publication Search — PHAROS Method and Variants]] documents:
- **Primary collision**: a patent family (US/WO/CA/EP/KR/TW) for "PhAROS" — polypharmaceutical analytics for research optimization at scale. Uses the exact phrase "the PhAROS method comprising…" with long publication history. Highest discoverability risk.
- **Secondary collisions**: independent naming collisions in optical networking, indoor localization, robotics, remote sensing, and computational holography — each unrelated.
- **Governance originality**: no prior publication of the recursive AI governance framing found at time of search (reference point: March 2026 draft).

Brand disambiguation from pharmaceutical/technical usages is flagged as a pre-publication task.

---

## Key Ideas

- The 6-status promotion taxonomy captures *degrees of readiness* instead of forcing a binary — this preserves governance information that pass/fail discards
- Delta closure is a state-change discipline, not a prose judgment: current state, target state, metric, deadline, decision-maker, responsible actors, and constraints/dependencies must be explicit before closure is claimed
- Consequence binding is the feature that separates PHAROS from advisory governance: infrastructure modules respond to decisions automatically
- `_tighten()` is the most important architectural contribution: once a claim reaches a restrictive state, nothing loosens it without explicit adjudication
- Failure harvesting (Stage 5) is an inventive claim — failures re-enter as positive evidence rather than being discarded
- The three absolute gates (R22/R9/R36) are the right architecture: not everything should be exceptionable

## Open Questions

- What are TC-4's intended contents — reserved, abandoned, or in progress?
- Has the Stage 1 bridging module (file records → claim rows) been built?
- What is the current deployment environment and execution status of PHAROS-3?
- Has v6 been submitted to patent counsel? What is the filing timeline?
- Has a disambiguation strategy been developed for the PHAROS brand given the pharmaceutical patent collision?

## Sources

- [[PHAROS Invention Disclosure]] — official IP filing 2026-04-01, v5 and v6 drafts
- [[PHAROS Recalibration — Unified Governance Architecture]] — four-script comparison, five gaps, eight recommendations
- [[Delta Closure Frame — Conditions, Actors, Constraints]] — operational frame for closing named gaps under named constraints
- [[PHAROS Runbook SOP]] — practitioner procedure
- [[Recursive Deterministic AI Governance — Method and Paper]] — primary scholarly output
- [[Global Publication Search — PHAROS Method and Variants]] — prior-art and naming-risk analysis
- [[Patent Research — Prior-Art Search and Free Tools]] — practical prior-art workflow and free-tool stack
- [[InfraFabric Architecture]] — consequence binding target
- [[Governance and PHAROS MOC]] — hub

## Related

- [[PHAROS AI Ethics Submission — Springer Draft]]
- [[PHAROS — Origin and Doctrine]] — the lived foundation; what the method is for, in plain language, before academic register
- [[RECURSO — Final Audit and Ethical Review]]
- [[Founder Charter — Lepage and Stocker]]
- [[PHAROS Evidentiary Gap Closure Bundle]]
