---
type: source
aliases: []
tags: [raw-source, orphan-repair, methods]
status: raw
created: 2026-07-10
updated: 2026-07-10
source: "provisional-arbitration-charter-v1.1"
---
# PHAROS METHOD — PROVISIONAL ARBITRATION CHARTER

**Document type:** Constitutional provisional (Layer 9.5)
**Version:** 1.1 (revised post-adversarial review)
**Status:** Active — provisional pending empirical review
**Owner:** Martin (Operator)
**Audit agent:** Argus v1.1 ("The Hundred-Eyed")
**Adversarial reviewer:** Henry / Reviewer #2
**Review trigger:** After 15 logged conflict instances, or 6 months from installation, whichever comes first

---

## 1. Governing problem

The Pharos Method operates as a recursive stack of 20 layers, each of which inherits, reinterprets, and constrains the layers beneath it. This architecture produces a structural ambiguity: when Layer X contradicts Layer Y, no formalized rule currently determines which prevails.

Four candidates for final arbitration authority exist within the stack. Each has a legitimate claim. None has been constitutionally installed as supreme. The stack's apex is ungoverned.

This charter does not resolve the arbitration question. It formalizes the question as a governed provisional — stating the current de facto hierarchy, routing all layer conflicts through a recorded process, and generating the case history from which the permanent rule will be derived empirically.

---

## 2. The four authority candidates

### 2.1 The Constitution (Layer 13)

**Claim:** The constitution is the foundational normative document. All layers operate under it. Constitutional provisions cannot be overridden by operational convenience, agent preference, or recursive drift.

**Weakness:** The constitution was authored at a specific moment in the stack's development. It may contain provisions that later layers have rendered incoherent — not through violation but through legitimate structural evolution. A constitution that cannot be amended is not supreme; it is brittle.

### 2.2 The Operator (Martin)

**Claim:** The human operator retains sovereign decision authority. No layer, agent, or protocol binds the operator against their judgment. The stack is advisory; the operator is decisive.

**Weakness:** Unconstrained operator sovereignty makes the governance stack decorative. If the operator can override any layer at will without record or justification, the stack has no binding force — and PHAROS cannot credibly sell governance to clients whose own systems exhibit the same deficiency.

### 2.3 The Adversarial Gate (Henry / Reviewer #2)

**Claim:** The adversarial review function exists to catch precisely the failures that operator bias and constitutional rigidity miss. Henry's veto is the stack's immune system.

**Weakness:** A veto is not a decision rule. Henry can block but cannot resolve. Adversarial authority without a positive decision mechanism produces gridlock or, worse, creates a de facto veto player whose preferences become the operative rule by default.

### 2.4 The Latest Layer

**Claim:** The stack is recursive. Each layer inherits and reinterprets the previous ones. The latest layer has the most complete view of the system's state and therefore represents the most evolved governance position.

**Weakness:** Recency is not legitimacy. Latest-layer priority creates governance drift with no anchor — each new layer can rewrite the terms of all prior layers, and the system loses constitutional memory. This is the mechanism by which governance-on-governance drift becomes undetectable.

---

## 3. The de facto hierarchy (current practice)

As of installation, the Pharos Method operates under the following implicit hierarchy. This section names what is, not what should be.

**Primary authority: Operator sovereignty with constitutional aspiration.**

In practice, Martin decides. The constitution constrains his decisions normatively but not procedurally — there is no mechanism that prevents an operator override, and no record is kept when one occurs. Henry functions as an advisory challenge, not a binding gate. The latest layer is treated as authoritative unless it visibly contradicts an earlier layer the operator still values, at which point the operator adjudicates informally.

**Failure modes observable under this arrangement:**

- Constitutional erosion by accumulated informal overrides
- Adversarial gate degradation (Henry's challenges are heard but not binding, which over time trains the system to treat them as optional)
- Invisible precedent (conflicts are resolved but not recorded, so the same conflict recurs without institutional memory)
- Legitimacy gap (PHAROS advises clients on governance while its own apex is ungoverned)

---

## 4. Bootstrapping acknowledgment

This charter is an exercise of the ungoverned operator sovereignty it claims to constrain. No prior layer or constitutional provision authorized the creation of a Layer 9.5 artifact. The operator created this document, positioned it in the stack, and defined its authority — which is precisely the mode of governance the document diagnoses as insufficient.

This is not a defect. It is the initial condition. Every constitution originates in an extra-constitutional act: a founding moment that cannot derive its authority from the system it creates, because that system does not yet exist. The charter inherits this structural paradox honestly rather than concealing it behind procedural language.

What converts an extra-constitutional founding into a legitimate governance instrument is not the act of creation but what follows: whether the system submits to its own constraints once they are installed, or whether it treats them as advisory. The test of this charter is not its drafting. It is the first time the operator is constrained by it and does not override.

---

## 5. Provisional arbitration rule

Until the permanent rule is derived from case history, the following provisional hierarchy governs all layer conflicts:

### 5.1 Tiered authority

**Tier 1 — Constitutional floor.** The constitution (Layer 13) sets the normative floor. No layer, agent, or operator decision may violate a constitutional provision without triggering a formal constitutional amendment process (Section 5.3). The floor is not the ceiling: the constitution constrains but does not resolve.

**Tier 2 — Operator decision within constitutional bounds.** The operator retains decision authority for all conflicts that do not breach the constitutional floor. Operator decisions must be recorded in the decision log (Section 6) with stated rationale. Operator decisions are subject to adversarial hold (Section 5.2) where applicable.

**Tier 3 — Adversarial challenge with hold authority.** Henry / Reviewer #2 retains the right to challenge any Tier 2 decision. In standard cases, the operator must respond to the substance of the challenge and log both the challenge and the response. In hold-trigger cases (Section 5.2), Henry's challenge suspends the operator's decision for a defined period.

**Tier 4 — Latest-layer presumption.** In the absence of conflict, the latest layer's interpretation of prior layers is presumed valid. This presumption is rebuttable by any of the three higher tiers.

### 5.2 Adversarial hold

Henry's challenge function is not advisory in all cases. The following categories trigger a **mandatory hold** — the operator's decision is suspended for 48 hours from the time Henry's challenge is logged:

**Hold-trigger categories:**

1. **Constitutional override.** Any operator decision that Argus or Henry identifies as contradicting a constitutional provision. The decision is suspended pending completion of the amendment process (Section 5.3) or withdrawal of the decision.

2. **Entrenched provision modification.** Any proposed change to the entrenched provisions defined in Section 8. The hold is mandatory and cannot be shortened by the operator.

3. **Precedent-setting conflict.** Any conflict where the operator's proposed resolution would establish a new general rule — not a one-time decision but a standing override of how two layers relate. Henry determines whether a decision is precedent-setting; if the operator disagrees with that classification, the disagreement itself is logged and the hold applies while the classification is contested.

**During a hold:**

- The operator may not implement the suspended decision.
- The operator must produce a written response to the substance of Henry's challenge.
- If after 48 hours the operator maintains the decision, the operator may proceed — but the hold, the challenge, the response, and the override are archived as a single package in the decision log. The entry is tagged `HOLD-OVERRIDE`.
- Argus tracks the frequency of `HOLD-OVERRIDE` entries. If the ratio of hold-overrides to total holds exceeds 80% over any rolling window of 10 holds, Argus flags a **Category 6 defect: adversarial gate bypass pattern** (Section 7.2).

**Outside hold-trigger categories:**

Henry's challenge triggers a mandatory log entry in which the operator must respond to the substance of the challenge. The operator may proceed with the decision while responding. Unanswered challenges are flagged by Argus as governance defects.

### 5.3 Constitutional amendment

The constitution may be amended, but only through an explicit process:

1. The proposed amendment is drafted and logged.
2. Henry is required to produce an adversarial review of the amendment. This triggers a mandatory hold (Section 5.2, category 1).
3. The 48-hour hold period runs from the filing of Henry's review.
4. The operator decides after the hold period expires.
5. The amendment, the adversarial review, the operator's rationale, and the hold record are all archived as a single package.
6. Argus logs the amendment as a constitutional event.

Informal operator overrides that contradict constitutional provisions without following this process are classified as **unrecorded constitutional erosion** and are flagged by Argus as a Category 1 governance defect (Section 7.2). See Section 7.3 for escalation.

### 5.4 Override conditions

| Override type | Permitted? | Conditions | Hold? | Log requirement |
|---|---|---|---|---|
| Operator overrides constitution | Yes, via amendment | Section 5.3 steps 1–6 completed | Yes — mandatory | Full package archived |
| Operator overrides Henry (standard) | Yes | Operator responds to substance | No | Rationale entry in decision log |
| Operator overrides Henry (hold-trigger) | Yes, after hold | 48-hour hold completed; response filed | Yes — mandatory | Full package archived, tagged `HOLD-OVERRIDE` |
| Operator overrides latest layer | Yes | Operator names which prior layer is preserved and why | No | Rationale entry in decision log |
| Henry triggers hold | Yes, in defined categories | Section 5.2 categories 1–3 | N/A — Henry initiates | Hold entry logged |
| Henry vetoes operator permanently | No | Challenge and hold rights only | N/A | N/A |
| Latest layer overrides constitution | No | Must trigger amendment or be rejected | N/A | Conflict flagged by Argus |
| Latest layer overrides operator | No | Operator retains Tier 2 authority | N/A | N/A |
| Constitution overrides operator | Yes — floor function | Decision void without amendment process | N/A | Argus flags Category 1 defect |
| Any actor modifies entrenched provisions | Via supermajority process only | Section 8.2 | Yes — mandatory | Full package archived |

---

## 6. The decision log

### 6.1 Purpose

The decision log is the empirical engine of this charter. Its purpose is not to enforce the provisional rule rigidly but to generate the case record from which the permanent arbitration rule will be derived.

### 6.2 Entry sources

The decision log is populated from two independent channels:

**Operator-initiated entries.** The operator identifies a layer conflict and logs it. This is the primary channel for conflicts that surface during deliberate governance work.

**Argus-initiated entries.** Argus independently detects layer conflicts through its defined data sources (Section 7.1) and opens decision log entries. Argus-initiated entries are tagged `ARGUS-DETECTED` and require operator response within 7 days. Unresponded entries are escalated per Section 7.3.

Both channels produce entries with identical structure and authority. An Argus-detected conflict is not subordinate to an operator-detected conflict. The decision log is not a self-report mechanism; it is a dual-source record.

### 6.3 Entry format

Each conflict instance is logged with the following fields:

`
ENTRY ID:           [sequential, e.g., ARB-001]
DATE:               [YYYY-MM-DD]
SOURCE:             [OPERATOR-INITIATED | ARGUS-DETECTED]
LAYERS IN CONFLICT: [e.g., Layer 7 (skill formalization) vs. Layer 13 (constitution)]
NATURE OF CONFLICT: [one sentence stating the contradiction]
AUTHORITY INVOKED:  [which tier was applied]
DECISION:           [what was decided]
OPERATOR RATIONALE: [why — substantive, not procedural]
HENRY CHALLENGE:    [yes/no; if yes, substance of challenge]
HOLD TRIGGERED:     [yes/no; if yes, category and duration]
HOLD-OVERRIDE:      [yes/no — did the operator override after hold?]
OPERATOR RESPONSE:  [response to challenge, if applicable]
PRECEDENT EFFECT:   [does this create a rule for future conflicts? yes/no/uncertain]
ARGUS FLAGS:        [any governance defect detected]
`

### 6.4 Log location

The decision log is maintained in the Obsidian vault under a dedicated `arbitration/` folder. Each entry is a single note. Argus reviews all entries as part of its Layer 9 audit function. Entries are also indexed in the skills ecosystem so that agents can reference arbitration precedent during sessions.

### 6.5 Pattern extraction

After every fifth entry, the operator reviews the accumulated log for emerging patterns:

- Are certain layers consistently overriding others?
- Is the constitutional floor holding or eroding?
- Is Henry's challenge function producing substantive corrections or becoming ritual?
- Is the adversarial hold being systematically overridden?
- Are operator rationales converging on an implicit rule that should be made explicit?
- Are Argus-detected conflicts revealing blind spots in operator self-reporting?

Pattern extraction notes are logged separately under `arbitration/patterns/`. Henry reviews each pattern extraction and files a response. Pattern extraction is not a solo operator exercise.

---

## 7. Argus operating brief

This charter serves as Argus v1.1's operating brief for arbitration governance. Argus audits against this document, not against an undefined standard.

### 7.1 Data sources

Argus independently detects layer conflicts by inspecting:

- **Session logs.** Recorded interactions in which agent outputs or skill invocations produce contradictory directives.
- **Skill invocation records.** Instances where two skills are invoked in the same session and produce conflicting governance outputs.
- **Agent output archives.** Outputs from Agatha, DOTTIE, MOBI, and Henry that contradict each other or contradict constitutional provisions.
- **Operator directives.** Explicit operator decisions that override agent recommendations, skill outputs, or prior arbitration precedent.
- **Decision log history.** Prior entries, pattern extraction notes, and hold records — inspected for consistency and for precedent conflicts.

If a data source is not yet operational (e.g., session logs are not systematically archived), Argus flags the gap as a **Category 7 defect: audit input unavailable** and the operator must address the gap or formally accept the audit limitation.

### 7.2 Defect categories

| Category | Description | Trigger |
|---|---|---|
| **1 — Constitutional erosion** | Operator override without amendment process | Immediate flag; escalation per 7.3 |
| **2 — Unlogged conflict** | Layer conflict resolved without decision log entry | Flag at next audit cycle |
| **3 — Unanswered challenge** | Henry challenge with no substantive operator response | Flag after 7 days |
| **4 — Pattern extraction overdue** | 5+ entries accumulated without pattern review | Flag at entry threshold |
| **5 — Charter drift** | Arbitration process modified without formal charter revision | Flag when detected |
| **6 — Adversarial gate bypass** | Hold-override ratio exceeds 80% over 10 holds | Flag when threshold crossed |
| **7 — Audit input unavailable** | A defined data source (Section 7.1) is non-operational | Flag when detected |

### 7.3 Escalation path

When Argus flags a defect, the following escalation sequence applies. The sequence does not terminate at the operator.

**Step 1 — Operator notification.** Argus logs the defect and notifies the operator. The operator has 7 days to respond with either a remediation action or a substantive justification for the current state.

**Step 2 — Henry review.** If the operator responds, Henry reviews the response for adequacy. If Henry finds the response adequate, the defect is closed. If Henry finds it inadequate, the defect remains open and is re-flagged.

**Step 3 — Integrity notice.** If a Category 1, 5, or 6 defect remains open for 30 days without adequate resolution, Argus generates a **method integrity notice** — a formal record stating that the Pharos Method's internal governance has an unresolved structural defect. The notice is archived in `arbitration/integrity/` and is dated.

**Step 4 — Disclosure obligation.** Open method integrity notices are part of the Pharos Method's operational record. If PHAROS represents its method as internally governed to clients, prospects, or the public, the existence of unresolved integrity notices must be disclosed upon inquiry. The operator may not represent the method as fully self-governing while integrity notices remain open.

**Rationale:** The escalation path does not give any agent the power to overrule the operator. The operator remains sovereign in decision. What the operator cannot do is act without record, ignore structural defects without consequence, or claim governance credibility that the system's own audit function has flagged as unearned. The constraint is not on the operator's authority but on the operator's claims.

---

## 8. Entrenched provisions

### 8.1 Purpose

Henry's adversarial review identified that a charter which can be revised into its own negation has not established anything. The provisionality clause (Section 9.3) permits the permanent rule to take any form — but not any form without limit. The following provisions are entrenched: they cannot be abolished by the permanent rule, by constitutional amendment, or by operator override.

### 8.2 The entrenched minimum

**Provision A — The decision log cannot be abolished.** The arbitration rule may change. The requirement to record how layer conflicts are resolved may not. Any future governance arrangement must include a written record of arbitration decisions with stated rationale. The log format may evolve. The existence of the log is non-negotiable.

**Provision B — The adversarial function cannot be abolished.** The identity, scope, and authority of the adversarial reviewer may change. The existence of a structurally adversarial position within the governance stack may not. Any future governance arrangement must include at least one agent or process whose defined role is to challenge operator decisions and governance outputs. The adversarial function may be renamed, reassigned, or restructured. It may not be eliminated.

**Provision C — The audit function cannot be abolished.** The identity, scope, and data sources of the auditor may change. The existence of an independent audit function within the governance stack may not. Any future governance arrangement must include at least one agent or process that inspects governance compliance against a defined standard and reports defects. The audit function may be renamed, reassigned, or restructured. It may not be eliminated.

**Provision D — The escalation path cannot terminate at the operator.** The specific escalation steps may change. The principle that governance defects have consequences beyond operator discretion may not. Any future governance arrangement must include at least one consequence for unresolved governance defects that the operator cannot unilaterally suppress. The consequence may be reputational, procedural, or structural. It may not be null.

### 8.3 Modification of entrenched provisions

Entrenched provisions may be modified (but not abolished) through a supermajority process:

1. The proposed modification is drafted with a rationale explaining why modification (not abolition) is necessary.
2. Henry produces an adversarial review focused specifically on whether the modification functionally abolishes the provision while nominally preserving it.
3. A mandatory 48-hour hold applies.
4. The operator decides after the hold, with the full package archived.
5. Argus reviews the modification at the next audit cycle for functional abolition. If Argus determines that the modification has effectively abolished the provision, a Category 1 defect is flagged and the escalation path (Section 7.3) applies.

The distinction between modification and abolition is substantive, not cosmetic. Renaming Henry is modification. Removing the adversarial function and calling it "streamlining" is abolition. Argus audits the distinction.

---

## 9. Scope and limitations

### 9.1 What this charter governs

- Conflicts between named layers of the Pharos Method stack
- Override authority and its conditions
- Adversarial hold and its trigger categories
- The decision log as an empirical governance instrument
- Argus's audit scope, data sources, and escalation path for arbitration
- Entrenched provisions and their modification process

### 9.2 What this charter does not govern

- Inter-model relay risk (requires live infrastructure, not a decision rule)
- Agent instantiation protocols (governed by their own specifications)
- Client-facing governance deliverables (governed by engagement-specific terms)
- HERMES operational decisions (governed by the operations dashboard)
- The content of any individual layer (each layer governs its own domain)

### 9.3 Provisionality

This charter is explicitly provisional. It will be superseded by a permanent arbitration rule once the decision log yields sufficient empirical basis — defined as 15 logged conflict instances with pattern extraction, or the operator's judgment that the pattern is clear before that threshold, subject to Henry's review of the operator's reasoning.

The permanent rule may confirm, revise, or replace the tiered hierarchy established here, subject to the entrenched provisions (Section 8). The charter does not presuppose its own conclusions — but it does presuppose that the conclusions will be arrived at through a recorded, adversarially reviewed, and audited process. That presupposition is itself entrenched.

---

## 10. Installation

### 10.1 Authorization

This charter is created by operator authority in the absence of a prior constitutional or procedural mechanism for creating Layer 9.5 artifacts. Section 4 of this document acknowledges the bootstrapping problem: the charter is an exercise of the ungoverned sovereignty it claims to constrain. Its legitimacy is not derived from a prior authorization but from its subsequent observance.

### 10.2 Position in stack

This document is installed as a Layer 9.5 artifact — positioned between Argus (Layer 9, audit) and the agent instantiation layer (Layer 10). It inherits the audit function's authority to inspect and the instantiation layer's scope of applicability.

### 10.3 Installation checklist

- [ ] Charter reviewed by operator
- [ ] Henry adversarial review completed (v1.0 review on file)
- [ ] Structural revisions addressing Henry's challenges completed (this version)
- [ ] Henry review of revised charter completed
- [ ] Argus operating brief acknowledged
- [ ] Decision log initialized (first entry: ARB-000, charter installation)
- [ ] Obsidian vault `arbitration/` folder created
- [ ] Obsidian vault `arbitration/patterns/` subfolder created
- [ ] Obsidian vault `arbitration/integrity/` subfolder created
- [ ] Pattern extraction schedule set (every 5 entries)
- [ ] Argus data source availability assessed; Category 7 defects filed for any gaps

---

## Appendix A: Henry's adversarial review (v1.0) — summary of challenges

The following challenges were filed against v1.0 of this charter and are preserved as part of the governance record.

1. **Operator self-governance.** Every constraint in v1.0 was operator-authored and operator-adjudicated. *Addressed by:* Section 5.2 (adversarial hold), Section 7.3 (escalation path), Section 8 (entrenched provisions).

2. **Adversarial gate neutered.** Henry's authority was reduced to advisory in all cases. *Addressed by:* Section 5.2 (mandatory hold in defined categories), Section 7.3 Step 2 (Henry reviews operator responses to defects).

3. **Constitutional floor unenforced.** No consequence existed for operator breach beyond an Argus flag that the operator reviewed. *Addressed by:* Section 7.3 (escalation path through integrity notice and disclosure obligation).

4. **Decision log self-reported.** Argus had no independent conflict detection capability. *Addressed by:* Section 6.2 (dual-source logging), Section 7.1 (defined data sources for Argus).

5. **Layer 9.5 self-authorizing.** No prior authority cited for the charter's position. *Addressed by:* Section 4 (bootstrapping acknowledgment), Section 10.1 (authorization statement).

6. **Provisionality as escape hatch.** The charter could be revised into its own negation. *Addressed by:* Section 8 (entrenched provisions defining what the permanent rule cannot abolish).

---

*Drafted as a governed provisional. Revised under adversarial constraint. The rule is not yet known. The process for discovering it is now constituted, and its minimum conditions are entrenched.*

## Related

- [[Governance and PHAROS MOC]]
- [[Provisional Arbitration Charter — Argus Layer 9.5]]


---
## Backlinks
Provenance artifact de-orphaned via graph repair (frontmatter + backlinks added 2026-07-10). Original content preserved above, unaltered.

- Indexed in: [[Home]]
