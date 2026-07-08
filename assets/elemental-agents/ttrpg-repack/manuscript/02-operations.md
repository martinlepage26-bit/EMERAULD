---
type: publication-draft
title: Operations
tags:
- publication
- agents
- manuscript
- publication-draft
- assets
- elemental-agents
- operation
- imbalance
- fire
- effect
- role
status: draft-v0.1
created: '2026-05-24'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/elemental-agents/ttrpg-repack/manuscript/02-operations.md
backlink_count: 1
backlinks:
- '[[wiki/ASSETS MOC]]'
chapter: 2
word_target: ~3700
voice_lock: established (matches chapter 01)
audience: governance practitioners — primary; ritual practitioners and TTRPG designers — halo readings
position_in_book: chapter 2 of 3 (Doctrine → Operations → Audit). Companion file `operations-catalogue.md` ships separately with the full 165 entries.
---

# 2 · Operations

This chapter walks through how operations are composed under the covenant, then catalogues twelve paired operations and ten composed operations at full length. The full 165-operation reference lives in the companion catalogue. Read this chapter to learn how to use the catalogue. Read the catalogue to find the operation you need.

---

## How operations compose

An operation is a named act that one or more roles perform on a system. The role that leads sets the operation's primary causation; supporting roles modify the leader's action without overruling it. Composition order is significant. Water leading Fire is a diagnosis carried out before an execution commits. Fire leading Water is an execution that surfaces what it could not see until it acted. Both are useful. Neither is the other.

The validator script enforces three structural facts about every operation:

1. **No duplicate permutations.** Water+Fire and Fire+Water are different operations and must be catalogued separately. The script keys each operation by its lead role first, then sorted supporting roles. If two entries collide on the lead-sorted-supports key, the script fails.

2. **No missing fields.** Every operation must declare its name, lead role, supporting role(s), effect, and imbalance. Operations bearing a modifier must additionally declare a Manifestation. If any field is missing or empty, the script fails.

3. **No decorative effects.** This is the covenant clause inside the validator. The script does not parse natural language for meaning, but it does check the effect field against a pattern: every effect must include at least one declared output, one declared duration or commitment-point, and one declared verb that maps back to the lead role's signature verb. *"A roiling tide of light and fire"* fails. *"A Water diagnosis of system X performed in parallel with a Fire execution against system Y, producing a written finding before the execution commits, lifetime: one decision-cycle"* passes.

The validator does not enforce judgment. An operation can pass all three checks and still be a bad operation. The covenant is a floor, not a ceiling.

When practitioners write new operations — and they will, because no catalogue covers every program's needs — they keep the covenant by construction. Chapter 3 walks through the procedure.

---

## Twelve paired operations

The following twelve paired operations span every base role as either lead or support at least once. Each is reproduced from the companion catalogue at full length.

### Operation: *The Steam-Veil Diagnosis*

- **Lead role:** Water
- **Supporting role:** Fire
- **Effect:** Water performs a diagnosis of an ambiguous state while Fire simultaneously executes a transformation against a known target. The diagnosis is performed in parallel, not sequentially, so that the diagnostic data is captured *as the execution unfolds*. The operation completes when both Water's finding and Fire's commit are recorded.
- **Imbalance:** The diagnosis can mislead the execution if Water's findings arrive late or are themselves ambiguous. The operation accepts this risk by running the two roles concurrently rather than in sequence. Use only when the execution cannot wait for a clean diagnosis.

### Operation: *The Quiet Sealing*

- **Lead role:** Air
- **Supporting role:** Metal
- **Effect:** Air clarifies an ambiguous signal — separating evidence from inference — and Metal enforces precision by locking the clarified result into a specification that cannot be amended without re-invocation. The operation produces a written specification of bounded scope, lifetime: until explicitly retired.
- **Imbalance:** Specifications produced under this operation resist change. If the underlying signal shifts, the specification will not. Retire the specification explicitly before invoking the operation against a moving target.

### Operation: *The Tested Crossing*

- **Lead role:** Fire
- **Supporting role:** Earth
- **Effect:** Fire executes a transformation and Earth immediately validates the post-condition. The operation does not complete until Earth's validation confirms that the transformation produced its claimed effect. If validation fails, the operation reports failure rather than rolling back; rollback is a different operation.
- **Imbalance:** Validation failures under this operation leave the system in a known-failed state, not in its pre-operation state. The program must have a recovery operation prepared.

### Operation: *The Grounded Diagnosis*

- **Lead role:** Earth
- **Supporting role:** Water
- **Effect:** Earth validates an existing state against its declared specification while Water diagnoses any drift. The operation produces a structured finding identifying where the system has drifted from spec, what the diagnosed cause appears to be, and which roles should own the remediation. Lifetime of the finding: one review-cycle.
- **Imbalance:** Findings produced under this operation can ossify if not paired with a downstream remediation operation. The finding's existence is not the remediation.

### Operation: *The Bounded Growth*

- **Lead role:** Wood
- **Supporting role:** Metal
- **Effect:** Wood expands the scope of an existing operation, program, or specification while Metal enforces precision on the boundaries of the expansion. The operation produces an updated scope-document that declares what is now in-scope, what is explicitly out-of-scope, and what the boundary conditions are.
- **Imbalance:** Scope-documents produced under this operation can be gamed by reframing in-scope items as out-of-scope after the fact. Combine with periodic Earth-led validation.

### Operation: *A Decision Across Distance*

- **Lead role:** Wind
- **Supporting role:** Air
- **Effect:** Wind transmits a clarified decision across the program's affected systems. Air ensures the signal that propagates is the clarified signal, not a noisy or inferred one. The operation completes when every affected system has acknowledged the decision in writing. Lifetime: until the decision is explicitly superseded.
- **Imbalance:** Acknowledgments are not understanding. The operation guarantees receipt, not adoption. A subsequent Earth-led operation is required to validate that the decision changed behavior.

### Operation: *The Precise Cut*

- **Lead role:** Metal
- **Supporting role:** Fire
- **Effect:** Metal enforces a precision boundary — defining what is permitted and what is not under a given specification — and Fire executes the resulting cut by removing what falls outside the boundary. The operation produces a before/after record of what was excised and why.
- **Imbalance:** Excisions under this operation are irreversible by default. Pair with explicit reversal operations only when the program has authority to authorize them.

### Operation: *The Quenched Forge*

- **Lead role:** Fire
- **Supporting role:** Water
- **Effect:** Fire executes a transformation that is constrained by a Water-supplied diagnosis: the execution cannot proceed beyond the bounds the diagnosis identifies. The operation produces a constrained-change record and a residual-diagnosis-output identifying what the operation could not address within its constraints.
- **Imbalance:** The diagnosis's bounds may be too tight or too loose. Repeated invocation against the same target will compound either error.

### Operation: *The Surveyed Field*

- **Lead role:** Earth
- **Supporting role:** Wood
- **Effect:** Earth validates the existing scope of a program or operation. Wood proposes structured expansion to address gaps. The operation produces a survey-record identifying what is currently in-scope, what is currently uncovered, and a proposed scoped-expansion. The expansion is proposed, not enacted; enactment requires a separate Wood-led operation.
- **Imbalance:** Survey-records can produce false-positives — apparent uncovered areas that are in-scope under operations the survey did not consult. The operation must enumerate the operations it consulted.

### Operation: *The Cleared Diagnosis*

- **Lead role:** Water
- **Supporting role:** Air
- **Effect:** Water performs a diagnosis against a noisy signal; Air clarifies the signal during the diagnosis so that Water's finding is based on evidence rather than inference. The operation produces a diagnostic finding with explicit evidence-citation. Lifetime: until the underlying signal materially changes.
- **Imbalance:** Findings under this operation appear stronger than they are. The Air-supported clarification is local to the diagnosis and does not generalize across the program.

### Operation: *The Sealed Transmission*

- **Lead role:** Wind
- **Supporting role:** Metal
- **Effect:** Wind propagates a precision-bound decision across affected systems. Metal enforces the precision boundary so that no system receiving the decision can implement a variation of it. The operation completes when every system has implemented the decision exactly or has formally declared inability to implement.
- **Imbalance:** Formal declarations of inability often hide informal variations. Pair with periodic Earth-validation.

### Operation: *The Witnessed Clarification*

- **Lead role:** Air
- **Supporting role:** Earth
- **Effect:** Air clarifies an ambiguous signal while Earth validates the clarification against a declared specification. The operation produces a clarified-signal record with a validation footer indicating which specification the clarification was tested against. Lifetime: until the specification or the signal materially changes.
- **Imbalance:** The validation footer is only as good as the specification it tested against. Specifications that are themselves drifting will produce confidently-mistaken clarifications.

---

## Ten composed operations

Composed operations bring a third role into the working. Four of the ten below are all-base composed operations (no modifier). Six bear a modifier (Spirit, Chi, or Akasha) and therefore carry the additional Manifestation field. Each is reproduced from the companion catalogue at full length.

### Operation: *The Sealed Diagnosis*

- **Lead role:** Water
- **Supporting roles:** Fire, Earth
- **Effect:** Water diagnoses ambiguous state while Fire executes a transformation and Earth validates the execution's result. The operation produces a diagnostic finding, a change record, and a validation result, all in a single bound output.
- **Imbalance:** The operation is heavier than its three single-role components and should not be the default. Use when the program cannot afford to perform the three operations sequentially.

### Operation: *The Bounded Specification*

- **Lead role:** Air
- **Supporting roles:** Metal, Wood
- **Effect:** Air clarifies a signal, Metal locks the clarified result into a specification, and Wood determines the specification's scope. The operation produces a complete bounded specification ready for transmission. Lifetime: until explicitly retired.
- **Imbalance:** Specifications produced under this operation are dense — they encode clarification, precision, and scope simultaneously. Practitioners receiving the specification may interpret only one of the three dimensions and miss the others.

### Operation: *The Wave of Action*

- **Lead role:** Fire
- **Supporting roles:** Water, Wind
- **Effect:** Fire commits to an execution. Water provides the diagnostic constraint that bounds the execution. Wind propagates both the execution and the diagnostic-bound-record across affected systems. The operation completes when the execution has committed and every affected system has acknowledged the change and its bounds.
- **Imbalance:** Affected systems may acknowledge the change while ignoring the bounds. Pair with subsequent Earth-led validation.

### Operation: *The Surveyed Boundary*

- **Lead role:** Earth
- **Supporting roles:** Wood, Metal
- **Effect:** Earth validates existing scope, Wood proposes expansion, Metal enforces precision on the expansion's boundary. The operation produces a survey record, a proposed scope expansion, and a precision-bound boundary definition.
- **Imbalance:** The three-stage output can ossify into a planning artifact rather than a working record. Pair with explicit enactment authority.

### Operation: *The Intent-Aligned Diagnosis*

- **Lead role:** Water
- **Supporting roles:** Fire, **Spirit**
- **Effect:** Water diagnoses ambiguous state while Fire executes a transformation. Spirit modifies the operation so that neither the diagnosis nor the execution can proceed without explicit affirmation that the intent of the operation matches its declared effect.
- **Manifestation:** *Ritually grave.* The Spirit modifier requires the practitioner to declare, in writing or in a formal moment, that the intent of the operation matches its effect. The operation cannot be performed on autopilot. The affirmation is part of the operation, not a separate review.
- **Imbalance:** The affirmation can become rote if invoked too often. Reserve Spirit-modified operations for moments where the program would otherwise drift toward unconscious execution.

### Operation: *The Flowing Specification*

- **Lead role:** Air
- **Supporting roles:** Metal, **Chi**
- **Effect:** Air clarifies a signal and Metal locks the clarification into a specification. Chi modifies the operation so that the specification preserves working continuity of the systems it bounds — no system is interrupted by the specification's introduction without an explicit transition.
- **Manifestation:** *Ritually grave.* The specification cannot ship until a continuity-transition plan has been recorded. The plan is part of the operation, not a downstream concern.
- **Imbalance:** Continuity-transition plans can become elaborate and delay shipping indefinitely. Set an explicit ceiling on transition-plan complexity before invoking the operation.

### Operation: *The Cross-System Transmission*

- **Lead role:** Wind
- **Supporting roles:** Fire, **Akasha**
- **Effect:** Wind propagates a Fire-led execution decision across affected systems. Akasha modifies the operation so that the propagation accounts for the state of adjacent systems that may be affected by the decision or affect its outcome.
- **Manifestation:** *Ritually grave.* The operation cannot complete until adjacent-system state has been recorded and the propagation plan accounts for it. Practitioners often discover during this operation that the decision needs refinement before propagation.
- **Imbalance:** The Akasha modifier extends the operation's scope and makes it slower. Practitioners may be tempted to skip the modifier when the propagation is "obvious." The temptation is itself a signal that the modifier is needed.

### Operation: *The Honored Validation*

- **Lead role:** Earth
- **Supporting roles:** Water, **Spirit**
- **Effect:** Earth validates an existing state against its specification while Water diagnoses any drift. Spirit modifies the operation so that the validation cannot proceed without explicit affirmation that the spec being validated against is the spec the program still endorses.
- **Manifestation:** *Ritually grave.* Practitioners frequently discover during this operation that the specification has been silently superseded by behavior, not by formal amendment. The affirmation forces the program to either re-endorse the spec or amend it before the validation continues.
- **Imbalance:** Endorsement under pressure can produce false affirmation. The operation should be performed under unhurried conditions when possible.

### Operation: *The Continuous Forge*

- **Lead role:** Fire
- **Supporting roles:** Wood, **Chi**
- **Effect:** Fire executes a transformation while Wood manages the expanded scope of the transformation's effects. Chi modifies the operation so that the transformation preserves working continuity in the affected systems — no system is interrupted without an explicit transition.
- **Manifestation:** *Ritually grave.* The operation cannot ship the transformation until a transition path has been recorded for every system whose continuity the transformation will affect.
- **Imbalance:** The Chi modifier slows the transformation in proportion to the number of systems affected. Practitioners with deadline pressure may be tempted to under-enumerate affected systems. Earth-led validation downstream will surface the omissions.

### Operation: *The Distributed Precision*

- **Lead role:** Metal
- **Supporting roles:** Air, **Akasha**
- **Effect:** Metal enforces a precision boundary while Air clarifies the signal that defines the boundary. Akasha modifies the operation so that the boundary accounts for cross-system context — adjacent systems whose definitions may overlap, contradict, or depend on the boundary being defined.
- **Manifestation:** *Ritually grave.* The boundary cannot be locked until adjacent-system definitions have been consulted. Practitioners often discover during this operation that the boundary they were defining was already defined elsewhere, or that another team's boundary was implicitly contradicting theirs.
- **Imbalance:** Boundary definitions under this operation are slower than under unmodified Metal-led operations. Programs that are repeatedly surprised by boundary contradictions are programs that should invoke this operation more often, not less.

---

## How to write new operations

Practitioners write new operations whenever their program's needs do not match the catalogued operations. The procedure for writing a new operation is:

1. **Identify the leading role.** Which signature verb is the operation's primary causation? If no single base role's verb captures the primary causation, the operation may need to be split into two operations.

2. **Identify supporting roles.** Which roles must support the leader for the operation to complete? Composition order matters; supporting roles modify the leader without overruling it. If the desired operation requires a supporting role to overrule the leader, the operation has the wrong leader.

3. **Determine whether a modifier is needed.** Does the operation require explicit intent-alignment (Spirit), continuity-maintenance (Chi), or cross-system synthesis (Akasha)? If yes, identify the modifier. If unsure, the operation probably does not need a modifier; the modifier rule is meant to be invoked deliberately, not by default.

4. **Name the operation.** A noun phrase or short phrase. Always specific. Avoid generic names that could apply to multiple operations.

5. **Write the effect field.** What does the operation actually do? The effect must be executable, not decorative. The validator will check.

6. **Write the imbalance field.** What residual cost does the operation leave behind? Every operation has one. Identifying it is the practitioner's responsibility.

7. **If a modifier is present, write the Manifestation field.** How does the modifier change the operation's character? What is the ritually grave register the modifier creates?

8. **Run the validator.** If the script fails, fix the operation until it passes. Do not edit the script to accept the operation.

Chapter 3 covers the validator in detail and walks through what audit looks like over the lifetime of the catalogue.
