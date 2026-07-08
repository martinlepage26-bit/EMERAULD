---
type: raw-source
title: provisional-arbitration-charter
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/Documents_root_loose_intake_2026-04-28/protocols/provisional-arbitration-charter.md
---

# PHAROS METHOD — PROVISIONAL ARBITRATION CHARTER

**Document type:** Constitutional provisional (Layer 9.5)
**Status:** Active — provisional pending empirical review
**Owner:** Martin (Operator)
**Audit agent:** Argus v1.1 ("The Hundred-Eyed")
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

## 4. Provisional arbitration rule

Until the permanent rule is derived from case history, the following provisional hierarchy governs all layer conflicts:

### 4.1 Tiered authority

**Tier 1 — Constitutional floor.** The constitution (Layer 13) sets the normative floor. No layer, agent, or operator decision may violate a constitutional provision without triggering a formal constitutional amendment process. The floor is not the ceiling: the constitution constrains but does not resolve.

**Tier 2 — Operator decision within constitutional bounds.** The operator retains decision authority for all conflicts that do not breach the constitutional floor. Operator decisions must be recorded in the decision log (Section 5) with stated rationale.

**Tier 3 — Adversarial challenge right.** Henry / Reviewer #2 retains the right to challenge any Tier 2 decision. A challenge does not suspend the operator's decision but triggers a mandatory log entry in which the operator must respond to the substance of the challenge. Unanswered challenges are flagged by Argus as governance defects.

**Tier 4 — Latest-layer presumption.** In the absence of conflict, the latest layer's interpretation of prior layers is presumed valid. This presumption is rebuttable by any of the three higher tiers.

### 4.2 Constitutional amendment

The constitution may be amended, but only through an explicit process:

1. The proposed amendment is drafted and logged.
2. Henry is required to produce an adversarial review of the amendment.
3. The operator decides after review.
4. The amendment, the adversarial review, and the operator's rationale are all archived as a single package.
5. Argus logs the amendment as a constitutional event.

Informal operator overrides that contradict constitutional provisions without following this process are classified as **unrecorded constitutional erosion** and are flagged by Argus as a Category 1 governance defect.

### 4.3 Override conditions

| Override type | Permitted? | Conditions | Log requirement |
|---|---|---|---|
| Operator overrides constitution | Yes, via amendment process | Sections 4.2 steps 1–5 completed | Full package archived |
| Operator overrides Henry | Yes | Operator responds to substance of challenge | Rationale entry in decision log |
| Operator overrides latest layer | Yes | Operator names which prior layer is being preserved and why | Rationale entry in decision log |
| Henry vetoes operator | No — challenge right only | Challenge is logged; operator must respond | Challenge + response archived |
| Latest layer overrides constitution | No | Must trigger amendment process or be rejected | Conflict flagged by Argus |
| Latest layer overrides operator | No | Operator retains Tier 2 authority | N/A |
| Constitution overrides operator | Yes — floor function | Operator decision is void if it breaches a constitutional provision without amendment | Argus flags as Category 1 defect |

---

## 5. The decision log

### 5.1 Purpose

The decision log is the empirical engine of this charter. Its purpose is not to enforce the provisional rule rigidly but to generate the case record from which the permanent arbitration rule will be derived.

### 5.2 Entry format

Each conflict instance is logged with the following fields:

```
ENTRY ID:          [sequential, e.g., ARB-001]
DATE:              [YYYY-MM-DD]
LAYERS IN CONFLICT: [e.g., Layer 7 (skill formalization) vs. Layer 13 (constitution)]
NATURE OF CONFLICT: [one sentence stating the contradiction]
AUTHORITY INVOKED:  [which tier was applied]
DECISION:          [what was decided]
OPERATOR RATIONALE: [why — substantive, not procedural]
HENRY CHALLENGE:   [yes/no; if yes, substance of challenge]
OPERATOR RESPONSE TO CHALLENGE: [if applicable]
PRECEDENT EFFECT:  [does this decision create a rule for future similar conflicts? yes/no/uncertain]
ARGUS FLAG:        [any governance defect detected]
```

### 5.3 Log location

The decision log is maintained in the Obsidian vault under a dedicated `arbitration/` folder. Each entry is a single note. Argus reviews all entries as part of its Layer 9 audit function.

### 5.4 Pattern extraction

After every fifth entry, the operator reviews the accumulated log for emerging patterns:

- Are certain layers consistently overriding others?
- Is the constitutional floor holding or eroding?
- Is Henry's challenge function producing substantive corrections or becoming ritual?
- Are operator rationales converging on an implicit rule that should be made explicit?

Pattern extraction notes are logged separately under `arbitration/patterns/`.

---

## 6. Argus operating brief

This charter serves as Argus v1.1's operating brief for arbitration governance. Argus audits against this document, not against an undefined standard.

### 6.1 Argus audit responsibilities

1. **Conflict detection.** Flag any instance where two layers produce contradictory outputs or directives.
2. **Log compliance.** Verify that every detected conflict has a corresponding decision log entry.
3. **Challenge tracking.** Track whether Henry challenges are being answered substantively.
4. **Erosion detection.** Flag any operator decision that contradicts a constitutional provision without a completed amendment process.
5. **Pattern reporting.** After every fifth log entry, prompt the operator to run pattern extraction.
6. **Drift monitoring.** Detect governance-on-governance drift — instances where the arbitration process itself is being informally modified without a charter revision.

### 6.2 Defect categories

| Category | Description | Trigger |
|---|---|---|
| **1 — Constitutional erosion** | Operator override without amendment process | Immediate flag |
| **2 — Unlogged conflict** | Layer conflict resolved without decision log entry | Flag at next audit cycle |
| **3 — Unanswered challenge** | Henry challenge with no substantive operator response | Flag after 7 days |
| **4 — Pattern extraction overdue** | 5+ entries accumulated without pattern review | Flag at entry threshold |
| **5 — Charter drift** | Arbitration process modified without formal charter revision | Flag when detected |

---

## 7. Scope and limitations

### 7.1 What this charter governs

- Conflicts between named layers of the Pharos Method stack
- Override authority and its conditions
- The decision log as an empirical governance instrument
- Argus's audit scope for arbitration

### 7.2 What this charter does not govern

- Inter-model relay risk (requires live infrastructure, not a decision rule)
- Agent instantiation protocols (governed by their own specifications)
- Client-facing governance deliverables (governed by engagement-specific terms)
- HERMES operational decisions (governed by the operations dashboard)
- The content of any individual layer (each layer governs its own domain)

### 7.3 Provisionality

This charter is explicitly provisional. It will be superseded by a permanent arbitration rule once the decision log yields sufficient empirical basis — defined as 15 logged conflict instances with pattern extraction, or the operator's judgment that the pattern is clear before that threshold.

The permanent rule may confirm, revise, or replace the tiered hierarchy established here. The charter does not presuppose its own conclusions.

---

## 8. Installation

This document is installed as a Layer 9.5 artifact — positioned between Argus (Layer 9, audit) and the agent instantiation layer (Layer 10). It inherits the audit function's authority to inspect and the instantiation layer's scope of applicability.

**Installation checklist:**

- [ ] Charter reviewed by operator
- [ ] Henry adversarial review completed
- [ ] Argus operating brief acknowledged
- [ ] Decision log initialized (first entry: ARB-000, charter installation)
- [ ] Obsidian vault `arbitration/` folder created
- [ ] Pattern extraction schedule set (every 5 entries)

---

*Drafted as a governed provisional. The rule is not yet known. The process for discovering it is now constituted.*

## Related

- [[Governance and PHAROS MOC]]
- [[Provisional Arbitration Charter — Argus Layer 9.5]]
