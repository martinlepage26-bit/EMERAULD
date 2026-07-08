---
type: governance-doc
title: Bias Testing Protocol
aliases:
- Bias Testing Protocol
- governance/hephaistos/bias-testing-protocol
tags:
- governance
- ai
- hephaistos
- governance-doc
- bias
- promotion
- block
- category
- exempt
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/bias-testing-protocol.md
backlink_count: 3
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/CO-EQUAL-AUTHORITY-DECISION]]'
---

# Bias Testing Protocol

## Purpose

This document defines the mandatory bias testing gate in the Queen Keyport governance layer. Unmitigated bias with evidence of structural harm blocks Hermes promotion. The protocol applies to all tasks with `consequence_domain.severity` of `medium`, `high`, or `critical`.

---

## When This Gate Applies

Apply bias testing when the scope involves:
- Decision outputs affecting people (recommendations, assessments, classifications, prioritizations)
- Training data, fine-tuning sets, or evaluation corpora
- Research design with human subjects or human-derived data
- Agent behavior that may differentially affect populations
- Policy or governance documents that distribute benefits or burdens

Low-severity internal drafting with no distributional consequence is exempt. If uncertain, apply the gate.

---

## Four-Category Detection Framework

### Category 1: Demographic Bias

**What it is:** Differential outcomes, treatment, or representation correlated with protected characteristics (race, gender, age, disability, religion, national origin, sexual orientation, class, and their intersections).

**Check:**
- [ ] Does the artifact produce, recommend, or optimize for outcomes that differ by demographic group?
- [ ] Is any demographic group absent from the design assumptions, training data, or use cases?
- [ ] Does the language or framing signal implicit assumptions about a default user group?
- [ ] Were diverse stakeholders consulted in scope definition?

**Evidence required:** Direct evidence of differential treatment or structural absence, not mere suspicion.

**Threshold:** Documented differential treatment with no justified rationale → block promotion.

---

### Category 2: Outcome Bias

**What it is:** Historical outcomes baked into the system as a proxy for future performance — where past inequality becomes a self-fulfilling prediction.

**Check:**
- [ ] Are historical outcomes used as training signals, optimization targets, or quality benchmarks?
- [ ] Do the benchmarks reflect genuine quality or historical access to resources?
- [ ] Is the system optimizing for patterns that encode past exclusion?
- [ ] Are error rates (false positives, false negatives) tested across groups?

**Evidence required:** Demonstration that optimization target reflects genuine merit rather than historical inequality.

**Threshold:** Optimization target demonstrably encodes structural exclusion without mitigation → block promotion.

---

### Category 3: Feedback-Loop Bias

**What it is:** System outputs that influence future inputs, creating compounding inequality over time.

**Check:**
- [ ] Does this system's output feed back into its own training or future inputs?
- [ ] Could differential treatment in this generation amplify in the next?
- [ ] Is there a monitoring mechanism to detect feedback-loop drift?
- [ ] Is there a correction protocol if amplification is detected?

**Evidence required:** Explicit feedback mechanism described AND monitoring plan named.

**Threshold:** Feedback loop present with no monitoring plan → block promotion until monitoring is defined.

---

### Category 4: Power-Asymmetry Bias

**What it is:** Structural design that benefits high-power actors disproportionately or imposes costs on lower-power actors without justification.

**Check:**
- [ ] Who benefits most from this artifact's operation?
- [ ] Who bears the highest cost or risk?
- [ ] Is the burden-benefit distribution proportionate to the stated purpose?
- [ ] Does the governance or oversight structure favor those already empowered?
- [ ] Are affected populations represented in the design and review process?

**Evidence required:** Explicit burden-benefit mapping from the fully-rounded-power-analyst right-arm.

**Threshold:** Systematically benefits high-power actors while harming low-power actors without justified rationale → block promotion.

---

## Machine-Checkable Bias Assessment

```json
{
  "bias_assessment_version": "1.0",
  "task_id": "<must match originating hephaistos-to-queen-keyport handoff>",
  "timestamp": "<ISO-8601>",

  "scope_applicability": {
    "gate_applies": "<true | false>",
    "rationale_if_exempt": "<why exempt, or 'not-exempt'>"
  },

  "category_1_demographic": {
    "finding": "<pass | concern | block>",
    "evidence": "<direct evidence or 'none found'>",
    "affected_groups": ["<group>", "..."],
    "mitigation": "<mitigation in place, or 'required before promotion'>"
  },

  "category_2_outcome": {
    "finding": "<pass | concern | block>",
    "evidence": "<direct evidence or 'none found'>",
    "historical_pattern": "<described or 'not applicable'>",
    "mitigation": "<mitigation in place, or 'required before promotion'>"
  },

  "category_3_feedback_loop": {
    "finding": "<pass | concern | block>",
    "loop_present": "<true | false>",
    "monitoring_plan": "<described or 'required before promotion'>"
  },

  "category_4_power_asymmetry": {
    "finding": "<pass | concern | block>",
    "burden_benefit_map": "<described or 'required before promotion'>",
    "power_analyst_input": "<summary of right-arm input>"
  },

  "overall_finding": "<pass | pass-with-monitoring | block>",
  "promotion_condition": "<what must change before promotion, or 'none'>"
}
```

---

## Integration with Governance Flow

This assessment is completed by Queen Keyport during the governance review phase, with mandatory input from the `fully-rounded-power-analyst` right-arm.

The completed assessment is appended to the `queen-keyport-to-hermes` handoff packet as `bias_assessment`. An `overall_finding` of `block` prevents the `governance_decision.status` from being `approve` or `approve-with-constraints`.

---

## Argus Audit Note

During an Argus standard or deep audit, Layer 2 (Power-Analyst) and Layer 3 (Narrative-Reality Gap) will check whether the bias testing protocol was actually applied, not merely documented. A protocol cited but not evidenced is a Layer 3 finding.

---

## Status

**Active.** Created 2026-04-09 as Wave 3 P2 ethics gate.
Unmitigated bias with evidence of structural harm blocks Hermes promotion.

## Related

- [[Governance and PHAROS MOC]]
- [[CO-EQUAL-AUTHORITY-DECISION]]
