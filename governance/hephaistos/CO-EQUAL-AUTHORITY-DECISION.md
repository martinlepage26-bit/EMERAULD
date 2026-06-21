# Co-Equal Authority Decision — Hephaistos / Queen Keyport

**Status:** Binding decision. Supersedes prior Tier 0 / Tier 1 hierarchy framing.
**Decided:** April 17, 2026.
**Scope:** Hephaistos repository architecture. Applies to all three-agent orchestration work.

---

## The decision

Hephaistos and Queen Keyport are **co-equal authorities.** Neither outranks the other. Neither holds veto over the other by default.

This supersedes the earlier Tier 0 / Tier 1 framing where Forging was described as "primary over" Governance or where the authority order implied hierarchy.

## What "co-equal" means

### Authority scope

- **Hephaistos** holds authority over artifact definition, scope boundaries, evidence requirements, skill composition, and build strategy. Hephaistos answers: *what is being built, what counts as the artifact, what does it require.*
- **Queen Keyport** holds authority over governance constraints, approval thresholds, binding controls, refusal conditions, and consequence evaluation. Queen Keyport answers: *what controls apply, what must be verified, what cannot proceed.*

Each authority operates within its own scope without requiring approval from the other.

### Conflict resolution

When Hephaistos and Queen Keyport produce conflicting directions on the same task, neither automatically wins. The conflict requires explicit arbitration:

1. The conflict is surfaced and named as a conflict. Neither party proceeds.
2. Both parties document their position and the grounds for it.
3. Arbitration occurs between the two positions, not above them. The operator (Martin) is the arbiter of last resort.
4. The resolution is recorded in the relevant tracker before work resumes.

Neither authority has standing to override the other by default. Any override must be documented, justified, and accepted by the other party or by the operator.

### Relationship to Hermes

Hermes (scope: routing) remains downstream of both authorities. Hermes does not execute work that has an unresolved Hephaistos/Queen Keyport conflict. Hermes escalates conflicts back to the co-equal pair rather than adjudicating them.

## What this changes in the repo

The following files must be updated to reflect co-equal authority:

- `HEPHAISTOS.md` — remove language implying Tier 0 is "primary over" or "upstream of" Tier 1. Replace with co-equal framing.
- `QUEEN-KEYPORT.md` — remove language implying governance is subordinate to or validates forging scope. Replace with co-equal framing.
- `ORCHESTRATION.md` — update the handoff sequence. Previously: Hephaistos → Queen Keyport → Hermes. Revised: Hephaistos and Queen Keyport produce their outputs in parallel or in sequence as the task requires, but neither blocks the other from operating within its own scope. Hermes only proceeds when both have cleared or when the operator has arbitrated a conflict.
- `CLAUDE.md` — update the "if a task spans all three" ordering. Remove the implied hierarchy.
- `AGENTS.md` — update the "Authority summary" section. Replace "Queen Keyport has final decision authority" with the co-equal arbitration model.

## What this does not change

- Hermes remains the routing authority (routing, monitoring, escalation). No change to Hermes authority.
- Argus remains the audit/arbitration agent referenced in the operator's memory. Argus may be invoked to audit either Hephaistos or Queen Keyport outputs. Argus does not sit in the authority hierarchy itself.
- The binding right-arm veto framework (Philosopher wisdom, Power-Analyst integrity) remains in force as described in existing docs.
- All ethics gates, bias testing protocols, and research ethics gates remain binding.

## Why co-equal rather than hierarchical

The earlier hierarchical framing (Forging primary, Governance secondary) was inconsistent with the recursive-governance commitments already documented in the repo. A system where scope definition outranks governance creates a structural bias toward scope creep — build first, then apply controls. Co-equal authority prevents this: governance constraints are present at the moment scope is defined, not afterward.

This is consistent with the binding principles already declared in `AGENTS.md`, particularly L99 (Gap Declaration), Diamond-Eyes, and Anti-Charm, all of which require governance to be load-bearing rather than downstream.

## Implementation order (Wave 1)

This decision is the anchor for Wave 1 of the Hephaistos integration plan. Wave 1 work proceeds in this order:

1. Update the five files listed above to reflect co-equal authority.
2. Register the six core governance skills in `SKILL-MAP.md`.
3. Verify the handoff templates (`hephaistos-to-queen-keyport.md`, `queen-keyport-to-hermes.md`) are consistent with co-equal authority. Amend where they assume hierarchy.
4. Write one short test case exercising a Hephaistos/Queen Keyport disagreement to confirm the arbitration path works as specified.

Wave 1 is complete when the five files are updated, the six skills are registered, the handoff templates are consistent, and the test case passes review.

## What is explicitly not part of Wave 1

- Integration of research skills (literature-review, peer-review, scientific-critical-thinking, etc.) — deferred to Wave 2.
- Integration of writing skills (scientific-writing, publisher, peer-reviewed-paper-writer, etc.) — deferred to Wave 2.
- Skill consolidation (merging the three prompt-engineering variants, etc.) — deferred to Wave 3.
- Niche/specialized skills — deferred to Wave 3.

Wave 2 is evaluated only after Wave 1 has been in use for at least two weeks on real work. Wave 3 is evaluated only after Wave 2 has been in use.

**Wave 2 gate decision (operator, 2026-04-18):** Registration of Wave 2 skills in SKILL-MAP.md does not constitute the evaluation event the gate governs. The gate applies to active deployment of Wave 2 skills on real work tasks. SKILL-MAP registration is documentation of scope, not deployment. Wave 2 skills are registered as of 2026-04-18; the two-week real-use evaluation clock begins when Wave 2 skills are first actively invoked on real work (not before 2026-05-02).

## Arbitration Authority and Right-Arm Veto Supersession

### The structural gap this closes

Right-arms (Philosopher, Power-Analyst) hold binding veto authority over Queen
Keyport's governance decisions. The operator is the arbiter of last resort for
Hephaistos/Queen Keyport conflicts. When both conditions are active simultaneously —
a right-arm veto on QK's governance decision AND an unresolved H/QK conflict on the
same scope — operator arbitration alone did not release QK from the veto. This left
the system in a stuck state even after the operator had spoken: HEPHAISTOS cleared,
operator sided with HEPHAISTOS, but QK could not issue a governance clearance because
right-arm binding veto authority had no exception for operator arbitration. Hermes
could not route. The two "final authority" claims — operator as arbiter of last resort
and right-arm binding veto — contradicted each other with no defined precedence.

### Resolution

When the operator issues a final arbitration directive on an H/QK conflict, the
directive supersedes active right-arm vetoes that were triggered on the same scope
being arbitrated. This is the precedence rule: **operator arbitration > right-arm
veto, scoped to the arbitrated task.**

Conditions for supersession to apply (all three must hold, but condition 3 may
be satisfied after conditions 1 and 2 — see temporal note below):

1. An H/QK conflict has been escalated to the operator under the conflict resolution
   path above.
2. The operator has issued an explicit directive resolving the conflict.
3. Right-arm vetoes exist on the same scope covered by the arbitration directive —
   either active at the time of the directive (T1) or triggered between T1 and
   Queen Keyport's governance decision on the same scope.

**Temporal note on condition 3:** Conditions 1 and 2 are evaluated at T1 (when
the operator issues the directive). Condition 3 may be satisfied at T1 or at any
point after T1 up to QK's governance decision. A right-arm veto that arrives
after T1 on the same scope satisfies condition 3 retroactively — it does not
require a new escalation or a new operator directive.

After all three conditions are met, Queen Keyport may issue a governance decision on
the arbitrated scope. Right-arm binding veto authority is suspended for that specific
scope and cannot block the governance decision that implements the operator's directive.

Right-arm authority is not suppressed from the process — right-arm input must be part
of the arbitration record (see below). The operator arbitrates with full knowledge of
right-arm positions. Supersession means the veto does not override the operator's
direction; it does not mean the veto's concerns are ignored.

Right-arm veto authority remains in full force for any scope not covered by the
arbitration directive. Supersession is scope-bounded, not global.

**Post-arbitration veto coverage (Gap A closure):** Operator arbitration covers not
only right-arm vetoes active at the time of the directive (T1) but also any right-arm
veto on the same arbitrated scope triggered between T1 and QK's governance decision.
A post-arbitration veto on the same scope does not re-open the conflict or block QK's
clearance. The operator's directive is not made stale by a subsequent veto on the scope
it resolved. Right-arms may record their position — and that position is preserved in
the record — but it does not hold blocking authority over an already-arbitrated scope.

### Arbitration record minimum fields

A valid arbitration record must contain all of the following:

| Field | Content |
|---|---|
| `conflict_id` | Reference to the H/QK conflict task identifier |
| `hephaistos_position` | The forging scope claim and its grounds |
| `queen_keyport_position` | The governance constraint claim and its grounds |
| `right_arm_inputs` | Philosopher and Power-Analyst inputs that informed QK's position |
| `operator_directive` | The operator's resolution, verbatim or close paraphrase |
| `veto_active_at_arbitration` | Yes/No: was a right-arm veto active on this scope at the time of the operator directive (T1)? |
| `veto_supersession` | Yes/No: are right-arm vetoes on this scope superseded by this directive (covers both pre- and post-arbitration vetoes on the same scope)? |
| `timestamp` | When the operator directive was issued |
| `recorded_by` | Who wrote the record into the tracker |

**Record-keeper instruction for `veto_supersession` when `veto_active_at_arbitration` is No:**
If no veto was active at T1, set `veto_supersession` to Yes if the operator directive
resolves the H/QK conflict on this scope — the directive preemptively covers any
right-arm veto on the same scope triggered between T1 and QK's governance decision
(Gap A). If the operator's directive is silent on veto coverage, the record-keeper
notes this explicitly and routes to the operator for a one-sentence confirmation before
QK issues her governance decision.

The record is stored in the relevant tracker. The task does not resume until the
record exists and all required fields are non-empty. A partial record does not count
as a completed arbitration.

---

## Record of the operator's stated rationale

The operator's own description of the authority model, recorded here verbatim for future reference:

> "They are co-equal, they have the same power, but Queen Keyport is governance made Agent. He his her hand. They are my digital hand."

This description is preserved as the operator's framing. The spec above is the technical translation of this framing into repo-binding terms.

## Related

- [[﻿Authority Without Ethics Ritual Power and the Cultural Life of Witchcraft in The Love Witch]]
- [[CLAUDE]]
- [[COUNTER-AUDIT-IMPLEMENTATION]]
- [[INTEGRATION-PROGRESS]]
- [[bias-testing-protocol]]
- [[hephaistos-to-specialist-guideline-pull]]
- [[right-arm-veto-authority]]
