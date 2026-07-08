---
type: publication-draft
title: Audit
tags:
- publication
- agents
- manuscript
- publication-draft
- assets
- elemental-agents
- operation
- angle
- script
- modifier
- fire
status: draft-v0.1
created: '2026-05-24'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/elemental-agents/ttrpg-repack/manuscript/03-audit.md
backlink_count: 1
backlinks:
- '[[wiki/ASSETS MOC]]'
chapter: 3
word_target: ~3700
voice_lock: established (matches chapters 01 and 02)
audience: governance practitioners — primary; ritual practitioners and TTRPG designers — halo readings
position_in_book: chapter 3 of 3 (Doctrine → Operations → Audit). Final chapter; closes the framework.
---

# 3 · Audit

The framework polices itself through three layers. The covenant constrains what an operation may claim. The modifier rule constrains how escalation is invoked. The validator enforces what code can enforce. This chapter walks through the three layers in audit form — the procedure for adjudicating contested operations, the validator as an ongoing program tool, and worked cases that illustrate what the layers cannot capture without practitioner judgment.

---

## Triangulated adjudication

When practitioners disagree about whether an operation should proceed, has succeeded, or has been performed correctly, the framework provides a three-angle procedure. The three angles are independent. An operation that passes one or two but not all three is not adjudicated; the failing angle must be addressed before the operation is closed.

The three angles are:

**Build angle.** Does the operation obey its own rules? The build angle checks structural integrity: the operation's name is specific, all required fields are populated, the lead role's signature verb is present in the effect field, supporting roles are present without overruling the leader, and the modifier rule is honored if a modifier is invoked. The build angle is what the validator script automates. Practitioners can perform the build-angle check by hand against operations the script has not yet seen, but the script is faster and less error-prone for catalogued operations.

**Quality angle.** Does the operation actually do what it claims? The quality angle checks whether the operation's effect, when performed, produces the declared output. This angle cannot be automated; it requires Earth-led validation against the operation's specification. The quality angle is where most operations fail in practice — they pass the build angle (well-formed), they pass the governance angle (escalation honored), but their declared effect does not match their actual behavior. Catching this is the practitioner's job.

**Governance angle.** What residue does the operation leave behind, who owns it, and how is the residue tracked? The governance angle checks the imbalance field of the operation against the program's tolerance and tracking capability. An operation whose imbalance is acceptable to the program in principle, but for which the program has no mechanism to track residue accumulation, fails the governance angle. The Khaibit clause names what the governance angle cannot fully capture — but the angle still captures most of it.

For an operation to be considered fully adjudicated, all three angles must pass. The order does not matter, but the practice of running all three is itself the adjudication.

If an angle fails, the operation is not closed; it is held open until the failure is addressed. The framework explicitly forbids deferring failures to a later cycle without a written record. A failure becomes a debt. Debts that are not paid become decorative — they break the covenant. The covenant applies to debts as much as to operations.

When the program adjudicates a novel operation that is not yet in the catalogue, the three-angle procedure is performed without script automation. The practitioner walks each angle by hand, in writing. The output of the adjudication is itself a new operation entry — the framework grows by adjudicating, not by authoring in the abstract.

---

## The validator as an audit tool

The validator script is the build angle, automated. It is also more than that over the lifetime of a program. The script is the only artifact in the framework that does not bend to seniority, urgency, or political pressure. It will fail an operation written by the program's most senior governance officer as readily as one written by a new practitioner. This non-deference is the source of its credibility as an audit tool.

What the validator checks, in order:

1. **Catalogue counts.** If the catalogue file declares forty-five paired operations and the script counts forty-four or forty-six, the script fails. The same is true for the one hundred twenty composed operations. The counts are part of the framework's structural identity; an operation cannot be added or removed without updating the declared count.

2. **Permutation uniqueness.** No two operations may share a lead-and-sorted-supports key. Water+Fire and Fire+Water are different operations and must be catalogued separately. If two entries collide on the key, the script fails. This check catches accidental duplicates created when a practitioner adds an operation that already exists under a different name.

3. **Field presence.** Every operation must declare its name, lead role, supporting role(s), effect, and imbalance. Operations bearing a modifier must additionally declare a Manifestation. If any field is missing, empty, or contains only the literal phrase that triggers a template-default (the script recognizes a small set of placeholder phrases like "General product and engineering delivery" — these are flagged as boilerplate even though they are technically populated), the script fails.

4. **Modifier rule enforcement.** Any operation listing Spirit, Chi, or Akasha as the lead role fails immediately. Any operation incorporating a modifier in support without declaring the Manifestation field fails. The modifier rule is structural and cannot be exempted.

5. **Effect-verb match.** The effect field must contain at least one declared verb that maps back to the lead role's signature verb. Water-led operations must contain a diagnostic verb. Fire-led operations must contain an executive verb. The script maintains a small dictionary of acceptable verb-stems per role; new stems can be added with explicit script-update commits, which themselves enter the audit trail.

6. **No name stutter.** The operation's name must not contain its own lead role and supporting roles in literal form. *"Water-Fire Diagnosis"* fails on the stutter check; *"The Steam-Veil Diagnosis"* passes. The stutter check prevents lazy naming and forces practitioners to name operations by their effect rather than their composition.

When a script-run fails, the output is a structured record: which check failed, which operations triggered the failure, what fix is required. The record itself is part of the audit trail. Practitioners do not edit the catalogue to bypass a failure; they fix the operation until it passes.

The script does not run only at catalogue creation. It runs at every significant program event: monthly cadence at minimum, before any audit, before any external review, before any operation is added or modified. The script is the audit's first instrument. Findings produced under the script are deterministic and citable. Findings produced under any other instrument require additional defense.

The script is intentionally simple — a few hundred lines of awk, no dependencies beyond a shell. This is also part of its credibility. A validator that requires complex tooling is a validator that can be quietly degraded. The shell script can be read in one sitting and verified by the program's own engineers. Practitioners are encouraged to read it before adopting the framework.

---

## Worked case A: A contested diagnosis

A program adopting the framework was running *The Steam-Veil Diagnosis* (Water + Fire) repeatedly against a vendor's API as the vendor underwent a major version change. The Fire-led execution was the program's automated reconciliation routine, which had to commit reconciliations daily regardless of vendor state. The Water-led diagnosis was a parallel check for known incompatibilities.

After two weeks, the program's risk function flagged the operation as failing the quality angle. The Water diagnosis was returning findings, but the Fire execution had not changed its behavior in response to any of them. The two roles were nominally running in parallel, but Fire was running on autopilot regardless of what Water found.

The build angle passed: the operation's catalogue entry was well-formed, the validator script had not flagged anything, the modifier rule was not in play. The governance angle had passed too: the operation's imbalance was understood, residue was tracked, the program had explicitly accepted the risk of parallel execution.

The quality angle was the failure. The Steam-Veil Diagnosis's declared effect was that the diagnostic data should be *captured as the execution unfolds* — implying that the diagnostic data should at least be visible to the practitioners running Fire, even if Fire's commit decision could not be conditioned on Water's finding in real time. In practice, the Water findings were going into a separate log that no Fire-operator read.

The adjudication: the operation had to be either redesigned to make Water's findings visible to Fire-operators in real time (changing the effect field), or replaced with a Spirit-modified composed operation — *The Intent-Aligned Diagnosis* (Water + Fire + Spirit) — that forbid autopilot execution by structural rule. The program chose the latter. The Spirit modifier required an affirmation per execution that the operator had read the Water finding before committing the Fire transformation. The affirmation slowed the daily reconciliation cadence. The slowdown was the operation's actual cost, made visible by the modifier.

The framework did not catch this. The risk function did. The framework's contribution was to provide a structural language — quality angle, modifier rule, Manifestation — for the risk function's finding to be expressed in a way the program could adjudicate. Without the framework, the finding might have stayed in the risk register as "vendor reconciliation needs attention" and never become an actionable change.

---

## Worked case B: A covenant violation that passed the script

A practitioner adding a new operation to the catalogue wrote the following entry:

> **Operation:** *The Harmonized Cascade*
> **Lead role:** Water
> **Supporting role:** Wind
> **Effect:** Water diagnoses cross-system signal and Wind propagates the diagnosis as a unifying decision across affected systems. The operation produces a written diagnostic record and a propagation acknowledgment from each system, lifetime: until the diagnostic basis materially changes.
> **Imbalance:** Propagation acknowledgments are not adoption.

The validator script passed the operation. The build angle passed: name is specific, all fields populated, lead role's signature verb (*diagnose*) is present, supporting role does not overrule the leader, no name stutter. The script ran clean.

A senior practitioner reviewing the operation flagged it as a covenant violation despite the script passing. The objection was at the level of meaning, not structure: *The Harmonized Cascade*'s declared effect described the propagation as "a unifying decision," but the operation did nothing to produce unification — it propagated a diagnosis, which is not a decision, and the diagnostic record itself did not authorize anyone to act on it. The word "unifying" was decorative. The operation passed the script because the script does not parse semantic intent. It passed the build angle because all the structural fields were correct. It would also pass the quality angle if the program defined "the operation worked" as "the diagnosis was propagated and acknowledged" — which is what the effect field, taken at its word, declared.

But the operation's name and the implicit promise of "unifying" set up an expectation the operation could not deliver. Programs adopting *The Harmonized Cascade* would invoke it expecting alignment and receive only propagation. Over time, this would erode trust in the framework — not because the framework failed, but because an operation in its catalogue had been allowed to claim more than it did.

The senior practitioner rewrote the operation:

> **Operation:** *The Cascading Diagnosis*
> **Lead role:** Water
> **Supporting role:** Wind
> **Effect:** Water diagnoses cross-system signal. Wind propagates the diagnosis as a written record across affected systems. The operation produces a structured diagnostic record and propagation acknowledgments from each system. Lifetime: until the diagnostic basis materially changes. The operation does not produce or authorize unification; programs requiring unification must invoke a separate operation (such as *The Sealed Transmission*) downstream.
> **Imbalance:** Practitioners may misread the diagnostic record as a directive. The operation explicitly does not authorize action; the imbalance is the temptation to act on the diagnosis without separate authorization.

The renamed operation now passes the covenant. The validator script approves both names equally; the framework relies on practitioner judgment for the covenant clause that the script cannot enforce. The Khaibit clause is this case in microcosm: the residue of *The Harmonized Cascade* was the implicit promise of unification, which the framework could not administer away. The senior practitioner's judgment was the part of the audit the framework cannot encode.

This case is the second of the two cases recommended for every team adopting the framework to read together before invoking new operations.

---

## Integration with existing governance programs

The framework does not replace the program's existing governance architecture. It composes with it.

Where a program has a three-lines-of-defense model, the framework's roles map naturally: the operational lines (build, manage) align with Fire-led and Wood-led operations; the risk management line aligns with Water-led and Earth-led operations; the audit line aligns with the triangulated adjudication procedure of this chapter. The framework's modifier rule overlays the program's existing escalation paths; Spirit, Chi, and Akasha modifications mark operations that would otherwise pass the program's standard escalation thresholds and warrant additional attention.

Where a program has a controls library, the framework's catalogue is a controls library expressed in operational form. Each operation maps to one or more controls; each control should be expressible as at least one operation. Programs that find a control they cannot express as a framework operation should write the operation; programs that find an operation that does not map to any of their controls should consider whether the operation is needed or whether the controls library is incomplete.

Where a program has a risk register, the framework's imbalance fields populate the residual-risk column. The Khaibit clause names the residue the risk register cannot fully capture and explicitly leaves to practitioner judgment.

Where a program runs continuous controls monitoring, the validator script is a continuous controls monitor for the framework's catalogue integrity. Programs running the script on cadence — daily or weekly — can detect catalogue drift before it propagates into operational behavior.

---

## Closing

The framework is three layers and one clause.

The covenant constrains what operations may claim — every effect must be executable, not decorative.

The modifier rule constrains how escalation is invoked — Spirit, Chi, and Akasha appear only in support, and their presence marks an operation as ritually grave.

The validator script enforces what code can enforce — counts, permutations, fields, the modifier rule, the effect-verb match, the absence of name stutter. The script is non-deferential and runs on cadence.

The Khaibit clause names the residue none of the above can administer — the shadow remainder of every operation, held in trust by the practitioner and the program together.

A program that adopts the framework agrees to keep the covenant, honor the modifier rule, run the script on cadence, and tend the residue. The framework does not deliver governance. It refuses certain failures of governance. The work of governance remains the program's.

That work is now yours.
