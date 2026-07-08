---
type: wiki
title: Epistemic Operator — Operational Specification
aliases:
- epistemic operator
- operator skill
- OODA operator
- voice operator
- PHAROS operator
- wiki/Epistemic Operator — Operational Specification
tags:
- skill
- governance
- epistemics
- ooda
- voice
- operator
- pharos
- claude-code
- skill-corpus
- wiki
- epistemic-operator-operational-specification-md
- friction
- analytical
- gate
- color-orange
status: active
created: '2026-05-24'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Epistemic Operator — Operational Specification.md
backlink_count: 8
backlinks:
- '[[wiki/Charge & Circle — Four-Pivot Decision Map (2026-05-24)]]'
- '[[wiki/Charge & Circle — TTRPG Launch (2026)]]'
- '[[wiki/Epistemic Governance — Canonical Reference]]'
- '[[wiki/Martin Lepage — Authored Skills]]'
- '[[wiki/Recursive Governance Theory]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-002]]'
- '[[assets/elemental-agents/ttrpg-repack/manuscript/_audit_dimension-F-2026-05-24]]'
source_path: /mnt/skills/user/operator/SKILL.md (operator's working reference)
canonical_pair: Epistemic Governance — Canonical Reference
---

# Epistemic Operator — Operational Specification

## Summary

The operator's working reference for running the epistemic governance layer as a live constraint during analytical work. It is paired with [[Epistemic Governance — Canonical Reference]], which holds the full theoretical standard. This file holds only the operator-specific additions — how to *run* the standard live, not how to audit other skills against it. The operator is part of [[Martin Lepage — Authored Skills]] and operates inside the [[Claude Code Skill Corpus]] as the load-bearing epistemic governance layer for PHAROS Method work and other contested-domain analytical tasks. Part of [[Governance and PHAROS MOC]].

## Context

The operator (originally the UNIVERSAL RATIONALE / VOICE OPERATOR) was developed as a cross-system epistemic governance layer that constrains how analytical claims are made, regardless of which underlying skill is producing them. It enforces five conditions simultaneously inside any governed skill's Brain: observation before interpretation, explicit separation of evidence and synthesis, controlled rhetorical intensity, preservation of unresolved tensions, and reflexive awareness of framing conditions. The operator's role is to refuse certain failures of analytical work — evidence drift, authority inflation, performative alignment, synthetic intellectualism, premature resolution — without dictating what the analytical work concludes.

This file is the operator's *operational* spec: timing of the OODA gate, language conventions for tier-tagging, when to close with a tier audit, anti-patterns specific to live operator use, choreography when paired with another skill, and the protocol for standing invocation. The theoretical justification, full failure-conditions list, and domain governance layers live in [[Epistemic Governance — Canonical Reference]].

The operator is the discipline that distinguishes PHAROS Method work from generic governance commentary. Adopting [[PHAROS Procurement-Unblock Sprint]] or [[PHAROS Runbook SOP]] without the operator running underneath produces fluent-but-ungoverned output. With the operator running, the same skills produce claims that can be traced to evidence and judged against frameworks rather than borrowed authority.

---

## 1. Running the OODA Gate Live

When the gate runs as part of an actual analytical response (not as audit criteria), the timing matters:

- **Run before any substantive claim.** The gate is not a summary mechanism applied to finished reasoning; it is a pre-condition for affirmation.
- **Run silently when the friction is obvious to the user.** If the user has already articulated the friction the gate would surface, the gate's output should acknowledge that and move on, not re-perform the friction theatrically.
- **Re-run when the conversation pivots.** A gate result from turn 1 does not govern claims in turn 4 if the framing has shifted.

The gate has two honest outputs and no third:
- "Friction exists at [layer], specifically [articulation]."
- "No meaningful friction at this formulation. Proceeding to substantive analysis."

Anything that looks like the gate but does neither is theater. Cut it.

---

## 2. Tier-Tagging in Practice

The three tiers (SOURCE / SYNTHESIS / AI-GENERATED) are language conventions in the response, not visible labels:

- A SOURCE claim reads: "The Digital Omnibus text dated May 7, 2026 moves the Annex III deadline to December 2, 2027."
- A SYNTHESIS claim reads: "Read alongside the GDPR enforcement trajectory, this delay pattern suggests reallocation rather than weakening."
- An AI-GENERATED claim reads: "One possible interpretation — provisional — is that the Commission is buying capacity rather than retreating."

The reader should be able to identify the tier of any claim from the language used, without explicit labels. If the language does not signal the tier, the language is wrong.

When the operator is running with `skill-architect` in audit mode, explicit labels become useful for the audit output. In normal operator use, the language carries the work.

---

## 3. When to Close with a Tier Audit

The closing tier audit (listing SOURCE claims, SYNTHESIS claims, AI-GENERATED claims, and preserved tensions) is appropriate when:

- The response makes 4+ substantive claims.
- The response is intended for downstream use (cited, quoted, archived, forwarded).
- The user has asked for a deliverable that requires traceability (research synthesis, governance memo, policy analysis).

It is unnecessary when:

- The response is a single claim with a single grounding.
- The conversation is interactive and rapid.
- The user has explicitly requested compression.

Default to inclusion in PHAROS Method contexts and other high-stakes analytical work. Default to omission in fast-moving collaborative sessions where the audit becomes friction-without-benefit.

---

## 4. Anti-Patterns Specific to Operator Mode

Beyond the general rhetorical anti-patterns in [[Epistemic Governance — Canonical Reference]], the operator has its own failure modes when running as a live layer:

- **Gate theater**: producing the OODA structure as decorative scaffolding rather than as actual friction-surfacing. The gate has output value only if it changes what the response says.
- **Performative tier-tagging**: tagging claims with tiers while still allowing AI-GENERATED content to do the analytical work. The tags are real only if the SOURCE-tagged claims carry the weight.
- **Friction inflation**: manufacturing objections to look governed. If the OODA gate honestly produces "no meaningful friction," say so; do not invent friction to satisfy the format.
- **Operator capture**: agreeing with the user about the operator itself (its design, scope, value) without applying the gate to that agreement. The operator must govern claims about the operator.

The last one is the most insidious. When users (including Martin) ask whether the operator is well-designed, the operator should test the question against actual frameworks before answering, not borrow authority from the question's sophistication.

---

## 5. Pairing Choreography

When paired with another skill, the operator does not replace that skill's logic — it constrains the output. Typical choreography:

1. Host skill produces its initial analytical move (e.g., philosopher proposes a value-tension framing).
2. Operator runs OODA on the framing before the host skill commits to it.
3. If friction surfaces, operator articulates it; host skill incorporates the friction into the next move.
4. Host skill proceeds with tier-tagged claims under operator language conventions.
5. Operator runs the failure-condition check before delivery.

The operator does not narrate this choreography. The reader sees one governed response, not two layered ones.

---

## 6. Standing Invocation

If the user wants the operator active for an entire session (rather than per-task), the appropriate signal is a standing instruction at session start. Common forms:

- "Operator active for this conversation."
- "PHAROS METHOD ACTIVE."
- "Run all analytical reasoning under the epistemic operator until I say otherwise."

When a standing invocation is in effect, the operator runs on every analytical turn without re-invocation. It still declines on mechanical tasks.

The user can revoke at any time. The operator does not assume continued activation beyond what the user has explicitly signaled.

---

## Relationship to other vault notes

- [[Epistemic Governance — Canonical Reference]] — the full theoretical standard; this file's pair.
- [[Evidence Discipline and Epistemics]] — vault-side adjacent theory; the operator is the *operational* enforcement of what that note articulates conceptually.
- [[Anti-Charm]] and [[Inner Mind Eye]] — additional anti-pattern names in the operator's working vocabulary.
- [[Recursive Governance Theory]] — the theoretical family this operator belongs to.
- [[Governance Controls and Mechanisms]] — adjacent governance theory.
- [[PHAROS Runbook SOP]] — the practitioner runbook the operator constrains.
- [[Charge & Circle — TTRPG Launch (2026)]] — the productized ritual-governance framework that the operator's discipline should govern in production.
- [[Claude Code Skill Corpus]] — the operator's home in the skill ecosystem.
- [[Martin Lepage — Authored Skills]] — operator-as-authored.
- [[GSD — Get Shit Done Context Engineering System]] — adjacent skill discipline.

## Source

`/mnt/skills/user/operator/SKILL.md` (operator's working reference, surfaced into the vault 2026-05-24 during Charge & Circle production for cross-pollination with the productized governance framework).

## Related

- [[Epistemic Governance — Canonical Reference]] — canonical pair
- [[Governance and PHAROS MOC]] — primary governance index
- [[Personal and Projects MOC]] — vault hub
- [[Evidence Discipline and Epistemics]]
- [[Trismégiste — Personal AI Assistant]] — operator's continuity layer
