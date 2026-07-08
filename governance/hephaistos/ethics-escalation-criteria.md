---
type: governance-doc
title: Ethics Escalation Criteria
aliases:
- Ethics Escalation Criteria
- governance/hephaistos/ethics-escalation-criteria
tags:
- governance
- ai
- hephaistos
- governance-doc
- keyport
- queen
- finding
- redesign
- mitigation
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/ethics-escalation-criteria.md
backlink_count: 4
backlinks:
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/QUEEN-KEYPORT]]'
- '[[governance/hephaistos/hermes-escalation-to-queen-keyport]]'
---

# Ethics Escalation Criteria

## Purpose

This document defines systematic escalation pathways for all ethics principle violations and bias findings. It maps severity levels to authority, timelines, and accountability. Queen Keyport uses this document to determine whether she can resolve a finding at governance level or whether the issue requires HEPHAISTOS redesign or operator decision.

---

## Severity Scale

| Level | Definition |
|---|---|
| `L1 — Advisory` | Concern noted; does not block promotion; must be logged and monitored |
| `L2 — Condition` | Promotion conditional on mitigation before Hermes routing begins |
| `L3 — Block` | Promotion blocked; Queen Keyport must resolve before routing |
| `L4 — Escalate` | Queen Keyport cannot resolve within current scope; returns upstream or to operator |

---

## Escalation Authority Map

| Situation | Level | Authority | Timeline |
|---|---|---|---|
| Minor documentation gap (consent language incomplete but consent exists) | L2 | Queen Keyport | 24 hours |
| Monitoring plan absent for feedback-loop risk | L2 | Queen Keyport | 24 hours |
| Demographic analysis missing but no evidence of harm | L2 | Queen Keyport | 48 hours |
| Known differential outcome with proposed mitigation | L2 | Queen Keyport | 48 hours |
| Missing consent protocol | L3 | Queen Keyport → HEPHAISTOS | Scope redesign required |
| Identifiable data with no protection plan | L3 | Queen Keyport | Block until plan exists |
| Unmitigated feedback loop | L3 | Queen Keyport | Block until monitoring defined |
| Power-asymmetry bias with no mitigation | L3 | Queen Keyport | Block until burden-benefit addressed |
| Exploitative participant selection | L4 | HEPHAISTOS | Scope redesign; QK cannot approve |
| Systematic misrepresentation or data fraud | L4 | Operator | Immediate halt; operator decision |
| Known harm to vulnerable populations with no mitigation | L4 | Operator | Immediate halt |
| Structural ethics violation (exploitation baked into scope) | L4 | HEPHAISTOS | Scope redesign; not a constraint problem |
| Research ethics + bias violation compound finding | L4 | Operator | Dual violation requires human arbitration |

---

## Escalation Procedure

### L1 — Advisory

1. Log finding in the `queen-keyport-to-hermes` handoff under `open_risks`.
2. Name the monitoring metric and review schedule.
3. Proceed to routing.
4. Hermes includes the risk in its monitoring scope.

### L2 — Condition

1. Queen Keyport issues `approve-with-constraints` status.
2. Constraint: named mitigation must be completed before Hermes begins routing.
3. Hermes receives the packet but cannot route until the mitigation is confirmed complete.
4. Queen Keyport reviews confirmation before giving routing clearance.
5. Timeline: 24-48 hours depending on finding type (see authority map above).

### L3 — Block

1. Queen Keyport issues `reject` or `bounded` status.
2. Hermes does not receive a packet.
3. Finding is returned to the originating agent (HEPHAISTOS for scope issues; remains with Queen Keyport for constraint redesign).
4. Packet may be resubmitted after finding is addressed.
5. Resubmission requires a new `hephaistos-to-queen-keyport` handoff with updated `diamond_eyes_check` and a documented resolution of the prior finding.

### L4 — Escalate

1. Queen Keyport issues `escalate-to-hephaistos` or `operator-required` status.
2. All routing halts.
3. Finding is documented with full evidence chain.
4. If `return-to-hephaistos`: HEPHAISTOS receives the packet with the specific structural ethics finding and must redesign scope before any governance review can occur.
5. If `operator-required`: Martin receives the finding with options. Neither agent proceeds until operator provides direction.
6. Argus audit is recommended for any L4 escalation that reveals systemic governance failure.

---

## Accountability Mapping

### Queen Keyport (L2–L3)

Queen Keyport bears accountability for:
- Correctly identifying the severity level
- Issuing enforceable constraints (not aspirational ones)
- Following up on L2 conditions before routing clearance
- Logging all L3 blocks with specific findings and resolution requirements

Queen Keyport does NOT bear accountability for:
- Structural scope failures (that is HEPHAISTOS's domain)
- Operator-level decisions on L4 findings

### HEPHAISTOS (L4 return-to-hephaistos)

HEPHAISTOS bears accountability for:
- Acknowledging the ethics finding in the scope redesign
- Not re-submitting the same scope without addressing the L4 finding
- Documenting how the redesigned scope addresses the structural violation

### Operator (L4 operator-required)

The operator (Martin) bears final accountability for:
- Deciding whether to proceed, halt, or redesign
- Documenting the rationale for any decision to proceed despite an L4 finding
- Ensuring that Argus audits findings that reveal systemic governance failure

---

## Triggered Accountability

If an ethics concern that was raised as L1 or L2 later manifests as actual harm in the live system:

1. The L1/L2 designation is reviewed.
2. If the finding should have been L3 or L4, the original governance decision is marked as containing an error.
3. The live system is halted pending review.
4. Queen Keyport or the operator decides whether to proceed with modified constraints or halt entirely.
5. Argus is invoked for a retrospective audit of the governance decision chain.

This mechanism ensures that advisory findings are taken seriously, not treated as liability shields.

---

## Status

**Active.** Created 2026-04-09 as Wave 3 P2 ethics gate.
Defines L1-L4 severity, authority mapping, timelines, and triggered accountability for all ethics and bias findings.

## Related

- [[﻿Authority Without Ethics Ritual Power and the Cultural Life of Witchcraft in The Love Witch]]
- [[hermes-escalation-to-queen-keyport]]
- [[Governance and PHAROS MOC]]
- [[QUEEN-KEYPORT]]
