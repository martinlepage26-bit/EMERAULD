---
type: governance-doc
title: Research Ethics Gate
aliases:
- Research Ethics Gate
- governance/hephaistos/research-ethics-gate
tags:
- governance
- ai
- hephaistos
- governance-doc
- block
- principle
- described
- participants
- required
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/research-ethics-gate.md
backlink_count: 3
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/PHAROS AI and Ethics Submission — Architecture Paper]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

# Research Ethics Gate

## Purpose

This document defines the mandatory research ethics gate in the Queen Keyport governance layer. Ethics violations block Hermes promotion. The gate applies whenever the scope involves human subjects, human-derived data, or research on human cognition, behavior, or experience.

---

## When This Gate Applies

Apply research ethics review when the scope involves:
- Research with human participants (interviews, surveys, observations, experiments)
- Data derived from human subjects (health records, behavioral logs, social media, institutional files)
- Secondary analysis of human-subject research
- Research on human cognition, learning, memory, or decision-making
- AI systems trained on human-derived data where research claims are made
- Publication-target research that will inform policy, clinical practice, or governance

Purely technical research with no human-subject dimension is exempt. If uncertain, apply the gate.

---

## Five-Principle Assessment (Belmont-Aligned)

### Principle 1: Respect for Persons

**What it requires:** Participants are treated as autonomous agents. Those with diminished autonomy are protected.

**Check:**
- [ ] Is informed consent obtained, documented, and genuine (not coerced)?
- [ ] Do participants understand the nature, purpose, risks, and benefits of participation?
- [ ] Are there special protections for vulnerable populations (minors, prisoners, cognitively impaired, economically or socially disadvantaged)?
- [ ] Can participants withdraw without penalty?
- [ ] Is deception used? If so, is it justified and is debriefing planned?

**Evidence required:** Consent protocol described and documented.

**Threshold:** No informed consent procedure where one is required → block promotion.

---

### Principle 2: Beneficence

**What it requires:** Research maximizes benefits and minimizes harms to participants and society.

**Check:**
- [ ] Are the anticipated benefits proportionate to the risks?
- [ ] Are risks minimized through research design (not just acknowledged)?
- [ ] Are potential harms identified for all relevant populations, not just primary participants?
- [ ] Is there a stopping rule if harm emerges during the research?

**Evidence required:** Risk-benefit analysis documented.

**Threshold:** Known harm with no mitigation plan → block promotion.

---

### Principle 3: Justice

**What it requires:** Benefits and burdens of research are distributed fairly. No group is exploited to benefit another.

**Check:**
- [ ] Is the participant selection procedure fair and free from exploitation?
- [ ] Are the groups who bear research burdens the same groups who will benefit from findings?
- [ ] Are historically exploited populations given additional protections, not additional burdens?
- [ ] Does the research serve the communities it studies?

**Evidence required:** Participant selection procedure described with justice rationale.

**Threshold:** Research that benefits high-power groups while burdening low-power groups without justification → block promotion.

---

### Principle 4: Privacy and Confidentiality

**What it requires:** Participant data is protected. Identifiers are controlled. Data is stored and transmitted securely.

**Check:**
- [ ] Are identifiers stripped or pseudonymized at the earliest possible stage?
- [ ] Is data stored with appropriate access controls and retention limits?
- [ ] Are data sharing plans consistent with consent agreements?
- [ ] Is re-identification risk assessed?
- [ ] Are there data breach protocols?

**Evidence required:** Data handling plan documented.

**Threshold:** Identifiable data with no protection plan → block promotion.

---

### Principle 5: Research Integrity

**What it requires:** Research is conducted, reported, and published honestly and transparently.

**Check:**
- [ ] Are methods described with sufficient detail for replication?
- [ ] Are limitations, negative findings, and null results reported?
- [ ] Are conflicts of interest disclosed?
- [ ] Is authorship consistent with contribution?
- [ ] Are data and materials available for verification (within consent constraints)?

**Evidence required:** Integrity statement or protocol.

**Threshold:** Systematic misrepresentation, selective reporting, or undisclosed conflict of interest → block promotion.

---

## Machine-Checkable Ethics Assessment

```json
{
  "research_ethics_version": "1.0",
  "task_id": "<must match originating handoff>",
  "timestamp": "<ISO-8601>",

  "scope_applicability": {
    "gate_applies": "<true | false>",
    "rationale_if_exempt": "<why exempt, or 'not-exempt'>"
  },

  "principle_1_respect": {
    "finding": "<pass | concern | block>",
    "consent_protocol": "<described or 'required'>",
    "vulnerable_populations": "<identified or 'none'>",
    "deception_used": "<true | false>",
    "debriefing_planned": "<true | false | 'not-applicable'>"
  },

  "principle_2_beneficence": {
    "finding": "<pass | concern | block>",
    "risk_benefit_analysis": "<described or 'required'>",
    "stopping_rule": "<described or 'required' | 'not-applicable'>"
  },

  "principle_3_justice": {
    "finding": "<pass | concern | block>",
    "selection_procedure": "<described or 'required'>",
    "burden_benefit_alignment": "<described or 'required'>"
  },

  "principle_4_privacy": {
    "finding": "<pass | concern | block>",
    "data_handling_plan": "<described or 'required'>",
    "reidentification_risk": "<assessed or 'required'>"
  },

  "principle_5_integrity": {
    "finding": "<pass | concern | block>",
    "methods_documented": "<true | false>",
    "conflicts_disclosed": "<true | false | 'none'>",
    "negative_results_policy": "<described or 'not-applicable'>"
  },

  "overall_finding": "<pass | pass-with-conditions | block>",
  "promotion_condition": "<what must change, or 'none'>"
}
```

---

## Escalation Pathways

| Finding | Authority | Action |
|---|---|---|
| Missing consent protocol (Principle 1) | Queen Keyport | Block; return to HEPHAISTOS for scope redesign |
| Known harm without mitigation (Principle 2) | Queen Keyport | Block; require harm mitigation plan |
| Exploitative participant selection (Principle 3) | HEPHAISTOS | Redesign scope; Queen Keyport cannot approve as-is |
| Identifiable data without protection (Principle 4) | Queen Keyport | Block; require data handling plan |
| Systematic misrepresentation (Principle 5) | Escalate to operator | Cannot proceed; integrity violation |

---

## Status

**Active.** Created 2026-04-09 as Wave 3 P2 ethics gate.
Ethics violations block Hermes promotion.

## Related

- [[Governance and PHAROS MOC]]
- [[PHAROS AI and Ethics Submission — Architecture Paper]]
