---
type: wiki
title: PROTOCOLS — Debate and Red-Team Runbook
aliases:
- PROTOCOLS
- debate runbook
- red-team
- five-lane review
- wiki/PROTOCOLS — Debate and Red-Team Runbook
tags:
- governance
- red-team
- debate
- hephaistos
- review-process
- wiki
- protocols-debate-and-red-team-runbook-md
- lane
- protocols
- delta
- redteam
- color-purple
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/PROTOCOLS — Debate and Red-Team Runbook.md
backlink_count: 15
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Consent and Boundary Frameworks]]'
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[Areas/PHAROS/Emotional Alliance vs. Evidentiary Discipline in AI]]'
- '[[Resources/Evidence Discipline and Epistemics]]'
- '[[wiki/Fluency and Interruption Theory]]'
- '[[wiki/Fluency, Interruption, and Institutional Accountability]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Governance Stress-Test Protocols — Index]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/Writing/HENRY — Research Paper Writing System]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[Resources/Red Team Handbook — Offensive Security Reference]]'
- '[[wiki/archive/red-team]]'
- '[[hephaistos/agents/hephaistos]]'
---

# PROTOCOLS — Debate and Red-Team Runbook

## Summary

PROTOCOLS is a directory at `/home/cerebrhoe/PROTOCOLS/` containing the operational reference for activating debate and red-team review processes within the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|HEPHAISTOS governance stack]]. It specifies when the full five-lane review fires, how lanes map, and how findings are handed off. Owned jointly by ORCHESTRATION (escalation triggers) and HEPHAISTOS (skill composition).

## Context

PROTOCOLS defines the escalation path from delta-first (lightweight) review to full five-lane governance review. It integrates the `$red-team` skill, `$philosopher`, and `$fully-rounded-power-analyst` in a sequenced pre-execution setup. Directly relevant to [[PHAROS Method — Technical Reference|PHAROS evidence discipline]] and the [[Fluency, Interruption, and Institutional Accountability|fluency/interruption framework]] — governance review is an interruption mechanism. See also [[RECURSO — Final Audit and Ethical Review]] for the full audit layer.

## Details

### Primary runbooks

- `/root/docs/2256_debates_and_redteams_orchestration_runbook_v1.2_2026-02-27.md` — primary
- `/root/docs/687-if-debate-redteam-structure-optimization-whitepaper-v1.2-2026-02-22T115251Z.md` — optimization overlay (delta-first scheduling, stop gates, finding-to-task write-through)

### Activation triggers (full review fires when)

- Externally exposed outputs
- Publish-target outputs
- Regulated or jurisdiction-sensitive tasks
- Safety-critical topics
- Claim-boundary reviews or production-readiness assertions
- Requests implying exhaustive coverage
- Unresolved ambiguity after a lighter delta-first pass

**Do not activate** for low-consequence internal drafting unless explicitly requested.

### Five-lane review mapping

| Lane | Focus |
|---|---|
| L1 | Claims and boundary (admissibility) |
| L2 | Runtime / implementation correctness |
| L3 | Adversarial / abuse potential |
| L4 | Operations and recovery |
| L5 | External-reviewer clarity |

Each lane must return: concrete finding with severity + owner + next action, OR explicit `none`. No empty lanes.

### Skill routing

| Skill | Role in process |
|---|---|
| `$red-team` | Authorized security exercise design, rules of engagement, purple-team validation, adversary emulation, executive reporting |
| `$philosopher` | Failure mode framing (Goodhart, Foucauldian capture, Ricorso) — runs before red-team execution |
| `$fully-rounded-power-analyst` | Structural power map, stakeholder analysis — pre-red-team context |

Do not route security exercise design through `$fully-rounded-power-analyst`. Hand off to `$red-team` when the task becomes an authorized engagement.

### Governance handoff requirements

Before any debate or red-team run is promoted:
1. HEPHAISTOS must have set scope and artifact type
2. Queen Keyport must have approved or bounded the engagement
3. P0/P1 findings must carry owner + next action before session close

## Key Ideas

- Default mode is delta-first; escalation is triggered, not assumed
- The five-lane structure prevents empty ceremonial review (each lane must produce a finding or explicit `none`)
- Philosophy (failure mode framing) precedes red-team execution — sequencing is load-bearing

## Sources

- `/home/cerebrhoe/PROTOCOLS/debate-redteam.md`

## Related

- [[Control Protocols MOC]]
- [[RECURSO — Final Audit and Ethical Review]]
- [[PHAROS Method — Technical Reference]]
- [[Fluency, Interruption, and Institutional Accountability]]
- [[Emotional Alliance vs. Evidentiary Discipline in AI]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
- [[hephaistos]]
- [[Agent Rook Full Explainer v1.4 (IF-2308 Air-Gap Autonomous Hardening)]]
- [[IF-2086 - Debate Structure and Triple Red-Team Optimization Whitepaper (v1.2)]]
