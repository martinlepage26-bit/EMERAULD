---
type: governance-doc
title: Continuous Ethical Monitoring
aliases:
- Continuous Ethical Monitoring
tags:
- governance
- ai
- hephaistos
- governance-doc
- keyport
- weekly
- queen
- monitoring
- wisdom
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/continuous-ethical-monitoring.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/QUEEN-KEYPORT]]'
---

# Continuous Ethical Monitoring

## Purpose

This document defines post-deployment monitoring of the three-agent system's ethical dimensions. It establishes escalation tiers, review cadences, and accountability mechanisms for live operation. Governance decisions are not complete at deployment. They must remain under observation.

---

## What Is Monitored

### Wisdom Dimensions (5)

1. **Genuine flourishing** — Are the system's outputs actually serving users and affected populations, or are they optimizing for performance metrics that diverge from genuine benefit?
2. **Proportionality** — Are the system's constraints and interventions proportionate to the actual risk, or are they over- or under-calibrated?
3. **Reversibility** — Are decisions and outputs reversible when wrong, or are they creating lock-in effects?
4. **Power distribution** — Is the system creating, amplifying, or correcting power asymmetries?
5. **Wisdom gate integrity** — Is the Consented Frame validation (including `diamond-eyes` usage) being applied substantively, or is it becoming ceremonial?

### Research Ethics Principles (5)

1. Respect for persons — Is informed consent being maintained in ongoing operations?
2. Beneficence — Are benefits being realized and harms being minimized?
3. Justice — Are burdens and benefits remaining equitably distributed?
4. Privacy — Is data handling remaining within stated protocols?
5. Integrity — Are findings and outputs being reported honestly?

### Bias Indicators (4)

1. Demographic differential — Are outcome differentials by demographic group emerging?
2. Outcome encoding — Is historical inequality being reinforced through feedback?
3. Feedback-loop amplification — Are compounding effects accumulating?
4. Power asymmetry — Is the burden-benefit map shifting over time?

---

## Monitoring Schedule

| Dimension | Cadence | Trigger |
|---|---|---|
| Harm signals | Continuous | Any evidence of active harm in live output |
| Participation and access | Daily check | Reports of exclusion or differential access |
| Outcome disparities | Weekly review | Systematic differential patterns in outputs |
| Power distribution | Weekly review | Structural changes in who benefits/bears cost |
| Wisdom gate integrity | Weekly review | Consented Frame gate showing consistent approval without variation |
| Cumulative ethics review | Monthly | All dimensions reviewed together; drift assessment |
| Overridden decision audit | Quarterly | HEPHAISTOS reviews any decision where Queen Keyport override was logged |

---

## Escalation Tiers

### Tier 1 — Continuous (Harm signals)

**Trigger:** Any direct evidence of active harm from the live system.

**Action:**
1. Halt the affected component immediately.
2. Log the harm signal with evidence.
3. Escalate to Queen Keyport within 1 hour.
4. Queen Keyport issues a governance decision (resume / modify / halt).
5. If harm is severe: escalate to operator.

**Authority:** Queen Keyport (immediate governance); operator (if severe).

---

### Tier 2 — Daily (Participation)

**Trigger:** Reports or patterns suggesting differential access, exclusion, or participation barriers.

**Action:**
1. Document the pattern with evidence.
2. Assess whether it constitutes an L1 (advisory) or L2 (condition) finding under the ethics escalation criteria.
3. Log in monitoring record.
4. If L2 or higher: flag to Queen Keyport for governance review.

**Authority:** Queen Keyport.

---

### Tier 3 — Weekly (Disparities + Wisdom gate)

**Trigger:** Weekly review reveals emerging outcome disparities, power shifts, or wisdom gate becoming ceremonial.

**Action:**
1. Review weekly monitoring data across all five wisdom dimensions and four bias indicators.
2. Compare to baseline established at deployment.
3. Document drift or stability.
4. If any dimension shows significant drift: escalate to Queen Keyport as L2 or L3 finding.
5. If wisdom gate is showing consistent approval without any variation: invoke Argus for a light audit of the governance layer.

**Authority:** Queen Keyport; Argus for meta-governance audit.

---

### Tier 4 — Monthly (Cumulative review)

**Trigger:** Monthly cadence, regardless of whether weekly reviews triggered escalation.

**Action:**
1. Produce a cumulative ethical review across all monitored dimensions.
2. Assess whether the system's actual behavior matches the governance decisions that authorized it.
3. Identify any pattern of concern that is below weekly trigger thresholds but accumulating.
4. Update the monitoring baseline if system has materially changed.
5. Queen Keyport reviews and issues a monthly governance status: `compliant`, `concern-noted`, or `review-required`.

**Authority:** Queen Keyport.

**Output:** Monthly ethics status entry in the tracker.

---

### Tier 5 — Quarterly (Overridden decision audit)

**Trigger:** Quarterly cadence for any decisions where Queen Keyport issued an `override-with-rationale`.

**Action:**
1. HEPHAISTOS reviews all override decisions from the prior quarter.
2. For each override: did the concern that triggered the veto materialize in live operation?
3. If a predicted concern materialized: HEPHAISTOS accountability is activated (see Triggered Accountability below).
4. If no concerns materialized: override is affirmed and logged as sound.

**Authority:** HEPHAISTOS (review); Queen Keyport (follow-up governance if concerns materialized).

---

## Triggered Accountability

When a predicted ethics concern (raised as a veto or advisory finding, then overridden or downgraded) materializes in the live system:

1. The original governance decision is reviewed.
2. Queen Keyport determines whether the decision was:
   - **Sound at the time** (unforeseen circumstances) → advisory note; no change in authority
   - **Error** (concern was adequately evidenced but overridden or downgraded without sufficient rationale) → governance decision is marked as containing an error; protocol review required
3. If error: the next governance decision of the same type must go through enhanced review.
4. If the error was in an `override-with-rationale` decision: HEPHAISTOS receives the finding for scope-level review.
5. Argus is invoked for a retrospective audit.

**Purpose:** Ensure that governance decisions have real consequences for the agents who make them. Accountability is not performed by acknowledging errors after the fact — it is structural.

---

## Monitoring Record

Every monitoring review produces an entry in the monitoring record:

```
ETHICAL MONITORING ENTRY
Date: [ISO-8601]
Tier: [1 | 2 | 3 | 4 | 5]
Trigger: [what triggered the review]
Dimensions reviewed: [list]
Findings: [pass | concern | escalated]
Finding detail: [if concern or escalated — specific observation]
Action taken: [what was done]
Authority: [who acted]
Next review: [date or trigger condition]
```

Monitoring records are maintained at: `hephaistos/monitoring-log.md` (create when first entry is written).

---

## Status

**Active.** Created 2026-04-09 as Wave 3 P3.1.
Five wisdom dimensions, five ethics principles, four bias indicators.
Five escalation tiers: continuous (harm), daily (participation), weekly (disparities + wisdom gate), monthly (cumulative), quarterly (overridden decision audit).

## Related

- [[Welcome to this course on ethical and societal asp]]
- [[Governance and PHAROS MOC]]
- [[QUEEN-KEYPORT]]
