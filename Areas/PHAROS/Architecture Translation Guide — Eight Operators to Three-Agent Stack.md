---
type: migration-guide
title: Architecture Translation Guide — Eight Operators to Three-Agent Stack
aliases:
- Eight Operators migration
- operator to agent translation
- Architecture Translation Guide
tags:
- governance
- deprecation
- architecture
- migration-guide
- areas
- hephaistos
- argus
- keyport
- coherence
- queen
- pharos
status: active
domain: pharos
created: '2026-04-27'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Architecture Translation Guide — Eight Operators to Three-Agent Stack.md
backlink_count: 14
backlinks:
- '[[Areas/PHAROS/CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]]'
- '[[Areas/PHAROS/Provisional Arbitration Charter — Argus Layer 9.5]]'
- '[[Areas/PHAROS/Second Self System — Identity Kernel and Agent Routing Architecture]]'
- '[[wiki/EMERAULD Thematic Analysis — Claude-Codex Pass (2026-05-25)]]'
- '[[wiki/Supersession Registry]]'
- '[[archive/session-state/session-state-001]]'
- '[[archive/session-state/session-state-003]]'
- '[[archive/wiki-2026-07-08/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Phase 1 Completion Checklist]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Phase 1 Progress Checkpoint (2026-04-26)]]'
- '[[archive/wiki-2026-07-08/Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation (2026-04-18)]]'
- '[[archive/wiki-2026-07-08/Second Self System Identity Kernel and Agent Routing Architecture]]'
- '[[memory]]'
- '[[wiki/skills/architecture]]'
deprecated_predecessor:
- - Agatha Unified Skill System — Eight Sovereign Operators
---

# Architecture Translation Guide — Eight Operators to Three-Agent Stack

**Purpose:** Translate concepts, decision patterns, and authority claims from the Eight Sovereign Operators model (deprecated 2026-03-01) to the current Three-Agent Stack (HEPHAISTOS, Queen Keyport, Hermes, Argus).

**Audience:** Anyone reading old governance notes referencing the eight operators or encounter fragments of that mental model in conversation/code.

**Effective Date of Original Transition:** 2026-03-01  
**Deprecation Marker Added:** 2026-04-26  
**Migration Guide Created:** 2026-04-27

---

## Quick Translation Table

| **Eight Operator** | **Core Function** | **Migrated To** | **New Scope** | **Notes** |
|---|---|---|---|---|
| 1. Signal Judgment | Detects, judges, renders reality legible; resolves, does not pass forward | HEPHAISTOS scope (artifact definition) | Forging — what exists and what counts as evidence | Becomes the evidentiary discipline in scope-definition phase |
| 2. Control Interpretation | Translates reality into obligation; defines what must move, who owns it, what counts as proof | Queen Keyport scope (governance constraints) | Governance — obligation setting and control requirements | Direct mapping; Queen Keyport *is* the control interpreter |
| 3. Structured Memory | Holds the world in memory without flattening; preserves relation, trace, structure | Hermes + Argus (monitoring/audit layer) | Routing & meta-governance — maintaining system coherence across boundaries | Hermes monitors decision coherence; Argus audits narrative-reality gaps |
| 4. Publication Transformation | Transforms governed knowledge into public form without losing structure | HEPHAISTOS scope (artifact completion phase) | Forging — artifact quality/form discipline | Becomes the "publication-readiness" check inside forging scope |
| 5. Structure and Lineage Audit | Reveals structure and origin simultaneously; what is said and how it came to be | Argus layer (meta-governance audit) | Meta-governance — independent audit of claims, evidence chains, drift | Becomes independent audit function (outside the three-agent core stack) |
| 6. System Mapping | Turns sprawl into territory; defines what exists, where it lives, how it relates | HEPHAISTOS scope (scope/system definition) | Forging — initial scope/territory definition | Becomes the "system architecture" discipline inside forging |
| 7. Design Coherence | Enforces coherence across variation; allows difference only when anchored | HEPHAISTOS scope (artifact coherence discipline) | Forging — coherence enforcement across the artifact | Becomes the coherence-check during artifact construction |
| 8. Skill Governance | Maintains integrity of all other skills; prevents drift, evaluation collapse, silent substitution | Queen Keyport scope + Argus layer (governance constraints + audit) | Governance (constraints) + Meta-governance (audit) | Becomes the L99 anti-drift discipline (now called "L99 Demotion Clause") + Argus's coherence testing |

---

## Detailed Translation by Operator

### 1. Signal Judgment → HEPHAISTOS's Evidentiary Discipline

**Old claim:**
"Detects, judges, renders reality legible — resolves, does not pass forward."

**Translation:**
Signal Judgment's role becomes the evidentiary foundation of HEPHAISTOS's scope-definition work. When HEPHAISTOS defines an artifact boundary, it must:
- Detect what evidence counts as real
- Judge whether evidence meets action thresholds (Signal Judgment's criterion)
- Render the reality legible in the scope definition itself
- Resolve gaps before passing scope to Queen Keyport

**In practice:**
- HEPHAISTOS defines a feature boundary only if the underlying evidence (user need, technical feasibility, regulatory fit) is sufficient to justify the scope
- HEPHAISTOS does not pass vague or under-evidenced scope to Queen Keyport with the hope that governance constraints will clarify it
- The scope definition *itself* contains the evidentiary judgment

**Failure mode (unchanged):**
"Reports instead of adjudicates" — HEPHAISTOS must reach a judgment in the evidentiary phase, not hand off a list of options.

---

### 2. Control Interpretation → Queen Keyport's Core Function

**Old claim:**
"Translates reality into obligation — defines what must move, who owns it, what counts as proof."

**Translation:**
This role maps directly to Queen Keyport's governance scope. No structural change — Queen Keyport *is* the control interpreter.

**In practice:**
- Queen Keyport takes HEPHAISTOS's scope (what exists, what counts as evidence)
- Queen Keyport translates that reality into governance obligations (what must be verified, who is accountable, what proof is required for approval)
- Queen Keyport defines the control requirements that HEPHAISTOS's artifact must satisfy

**Failure mode (unchanged):**
"Lists frameworks without changing action" — Queen Keyport must define actual control requirements, not abstract governance postures.

---

### 3. Structured Memory → Hermes + Argus

**Old claim:**
"Holds the world in memory without flattening — preserves relation, trace, structure."

**Translation:**
Structural memory is now distributed across two layers:

**Hermes layer (routing/monitoring):**
- Maintains the coherence of decisions across the three agents
- Tracks decision dependencies and impact chains
- Alerts when a new decision conflicts with prior governance approvals
- Prevents isolated decisions from drifting out of coherence with the system

**Argus layer (meta-governance audit):**
- Maintains long-form audit trails (how decisions came to be made, what evidence was considered)
- Detects narrative-reality gaps (what we say our governance does vs. what it actually does)
- Audits memory integrity (are we remembering our prior decisions accurately, or forgetting constraints?)

**In practice:**
- Hermes asks: "Does this new decision cohere with the existing approval set?"
- Argus asks: "Are we *actually* following the governance patterns we documented?"

**Failure mode (changed):**
Old: "Memory becomes accumulation instead of structure" (passive)  
New: "Decision isolation without coherence checking" (active failure requiring Hermes intervention)

---

### 4. Publication Transformation → HEPHAISTOS's Artifact Completion Phase

**Old claim:**
"Transforms governed knowledge into public form without losing structure."

**Translation:**
Publication Transformation becomes a discipline inside HEPHAISTOS's artifact-completion phase. It is no longer a separate operator.

**In practice:**
- HEPHAISTOS, after HEPHAISTOS and Queen Keyport have both cleared their respective scopes, must transform the artifact into a form that can be safely published
- The transformation preserves the structural discipline (evidence chains, coherence, control mappings)
- The transformation does not hide constraints or distort control requirements for rhetorical effect

**Failure mode (unchanged):**
"Performance replaces proof" — artifact completion must not sacrifice structural integrity for polish or persuasiveness.

---

### 5. Structure and Lineage Audit → Argus Meta-Governance Layer

**Old claim:**
"Reveals structure and origin simultaneously — what is said and how it came to be."

**Translation:**
This becomes the independent audit function of the Argus layer.

**In practice:**
- Argus audits the Three-Agent Stack to ensure:
  - Claims made by HEPHAISTOS have defensible evidence chains
  - Governance constraints set by Queen Keyport are grounded in actual risks, not assumed ones
  - Decisions approved by Hermes are coherent with prior governance
- Argus reveals not just what decisions were made, but how they came to be made
- Argus is independent of the three-agent core (not subordinate to H, QK, or Hermes)

**Failure mode (unchanged):**
"Beautifies instead of exposing" — Argus must audit for truth, not for coherence-appearance.

---

### 6. System Mapping → HEPHAISTOS's Scope/Architecture Discipline

**Old claim:**
"Turns sprawl into territory — defines what exists, where it lives, how it relates."

**Translation:**
System Mapping becomes a discipline inside HEPHAISTOS's scope-definition phase.

**In practice:**
- HEPHAISTOS defines artifacts not in isolation, but as part of a coherent system
- HEPHAISTOS maps what exists (prior decisions, dependencies, constraints)
- HEPHAISTOS defines where the new artifact fits in that system
- HEPHAISTOS clarifies how the new artifact relates to existing components

**Failure mode (changed):**
Old: "Cleans without seeing" (passive ignoring of system structure)  
New: "Defines scope without mapping system fit" (active failure requiring HEPHAISTOS to validate against existing system)

---

### 7. Design Coherence → HEPHAISTOS's Coherence Discipline

**Old claim:**
"Enforces coherence across variation — allows difference only when anchored."

**Translation:**
Design Coherence becomes a discipline inside HEPHAISTOS's artifact-construction phase.

**In practice:**
- HEPHAISTOS allows variation in artifact design only when the variation is explicitly anchored (to evidence, to user need, to regulatory fit, or to existing system coherence)
- HEPHAISTOS enforces that all design choices are traceable to a reason, not arbitrary
- HEPHAISTOS prevents "drift by design decision" (unanchored variation that breaks system coherence)

**Failure mode (unchanged):**
"Either monotony or drift" — artifacts must be coherent without requiring uniformity.

---

### 8. Skill Governance → Queen Keyport Constraints + Argus L99 Audit

**Old claim:**
"Maintains integrity of all other skills — prevents drift, evaluation collapse, silent substitution."

**Translation:**
This function splits into two parts:

**Queen Keyport layer (constraints):**
- Sets governance constraints on how decisions are made (who can decide, what evidence is required, what approval gates apply)
- Prevents "evaluation collapse" by requiring that approval thresholds are declared in advance and held constant
- Prevents silent substitution by auditing when thresholds change (explicit post-evaluation review required)

**Argus layer (L99 audit):**
- Independent audit of whether the skill governance constraints are actually being honored
- Detects drift: are we still following the governance patterns we declared, or silently changing them?
- Detects evaluation collapse: have thresholds shifted mid-evaluation?
- Reports findings to operator; operator decides on consequence

**In practice:**
- Queen Keyport says: "This decision type requires X approval threshold; that is the rule from now on."
- Argus audits: "Is this decision actually being held to X, or have we silently moved to Y?"
- If Argus detects drift, the finding goes to Operator, not back through the three agents.

**Failure mode (changed):**
Old: "Fluency mistaken for improvement" (drift hidden by polished language)  
New: "Undeclared threshold-shift" (approval gate changes silently, detected by Argus L99 audit)

---

## Decision Re-Mapping Examples

### Example 1: Evaluating a Policy Change

**Old Eight-Operator Flow:**
1. Signal Judgment: "Is this policy real and actionable?" (yes) → pass to Control Interpretation
2. Control Interpretation: "What obligation does this create?" → pass to Skill Governance
3. Skill Governance: "Is this consistent with our prior decisions?" → signal Structured Memory
4. Structured Memory: "Document lineage" → complete

**New Three-Agent Flow:**
1. HEPHAISTOS: "What is the scope of this policy change?" (evidence, boundary, system fit)
2. Queen Keyport: "What governance constraints does this trigger?" (approval gates, control requirements)
3. Hermes: "Is this coherent with prior approvals?" (check decision precedent)
4. Argus (independent): "Are we actually following the process we said we would?" (audit L99 integrity)

**Key difference:** The new model forces governance constraints to be considered *alongside* scope definition (HEPHAISTOS and Queen Keyport in parallel), not *after* scope is defined. This prevents "scope creep by unexamined constraint."

---

### Example 2: Deprecating an Architecture Component

**Old Eight-Operator Flow:**
1. Signal Judgment: "Is the old component actually defunct?" (yes) → Design Coherence: "Will removing it break coherence?" → Skill Governance: "Do we have a deprecation rule?" → Structure and Lineage Audit: "Document why it's being removed"

**New Three-Agent Flow:**
1. HEPHAISTOS: "What is the new scope without this component? Does it cohere?" (scope redefinition)
2. Queen Keyport: "What deprecation protocol and migration requirements apply?" (governance constraints on removal)
3. Hermes: "Is there a prior decision that depends on this component?" (coherence check across system)
4. Argus: "Is the deprecation being handled according to our architecture deprecation protocol?" (independent audit)

**Key difference:** The new model requires a *governance decision* about deprecation (Queen Keyport sets the migration requirements and timeline), not just a scope or audit decision. This prevents "silent removal" of components that others depend on.

---

## Authority Resolution Under the New Model

### Old Eight-Operator Authority Rule

A claim was authoritative only if:
1. It met the **action threshold** (Signal Judgment: sufficient evidence), AND
2. Its reasoning **withstood audit** (Structure and Lineage Audit: no unresolved breaks)

**Problem:** This created two potential veto points (Signal Judgment and Audit) but no explicit mechanism for resolving disagreement between them.

### New Three-Agent Authority Rule

A decision proceeds to approval only if:
1. **HEPHAISTOS clears its scope:** The artifact boundary, evidence base, and system coherence are defensible.
2. **Queen Keyport clears its governance:** The control requirements are grounded in actual risks; approval thresholds are declared and non-negotiable.
3. **Hermes validates coherence:** The decision does not conflict with prior approvals or system dependencies.

**If HEPHAISTOS and Queen Keyport disagree:**
- The conflict is surfaced explicitly
- Both parties document their positions
- Hermes does not route until the conflict is resolved
- The **Operator arbitrates** and records the resolution
- Work resumes only after the operator's decision

**If Hermes flags a coherence problem:**
- Hermes escalates back to HEPHAISTOS and Queen Keyport (not operator-level)
- The scope or governance decision is revisited
- The system re-cleared by both before routing proceeds

**If Argus flags a drift issue:**
- Argus reports directly to Operator (not to the three agents)
- Operator evaluates severity and decides consequence
- If drift is material, prior decisions may be subject to re-audit

---

## Transition Timeline

| Date | Event |
|------|-------|
| 2026-03-01 | Eight Operators architecture became inactive; Three-Agent Stack became operational |
| 2026-03-02 to 2026-04-22 | Three-Agent Stack was operating, but old operator mental model persisted in conversation |
| 2026-04-23 | Linear Authority (Tier 0/1/2 hierarchy) was superseded by Co-Equal Authority model |
| 2026-04-26 | Eight Operators note marked deprecated retroactively; Phase 1 governance controls work initiated |
| 2026-04-27 | Migration guide created as part of Phase 1 Supersession Registry formalization |
| 2026-04-29 | [[Second Self System — Identity Kernel and Agent Routing Architecture]] added as operator-facing identity/routing layer: many specialists, one identity kernel, one public voice |

---

## Lessons from the Eight-Operator Model (Still Valid)

The Eight Operators model, though superseded, contributed three insights that survive in the Three-Agent Stack:

1. **Authority Resolution as Structural Lock:**
   The old rule "actionable AND defensible" prevented authorities from claiming final word based on one criterion alone. The new rule (HEPHAISTOS AND Queen Keyport AND Hermes coherence) keeps this principle: no single agent can override the others; all three must clear their scopes before routing.

2. **Threshold Fixation:**
   The old "declare thresholds in advance and hold them constant" rule is now enforced by Queen Keyport in the governance scope. Thresholds that change mid-decision are flagged by Argus (L99 audit). This prevents "evaluation creep" where approval criteria silently shift.

3. **Memory as Structural Integrity:**
   Structured Memory's discipline (preserve relation, trace, structure) survives as Hermes's coherence-checking function and Argus's audit trail. Decisions are not isolated artifacts; they are part of a coherent system.

---

## Open Questions from the Eight-Operator Model (Unresolved)

The old model had three unresolved tensions; the new model addresses them as follows:

| Old Tension | Old Problem | New Resolution |
|---|---|---|
| **Truth vs. Trace Split** | Signal Judgment and Audit both claimed authority over truth conditions | New model: Signal Judgment (evidence) lives in HEPHAISTOS; Structure and Lineage Audit becomes independent Argus function. Separated into different scopes; operator arbitrates if they conflict. |
| **Authority Duplication** | Control Interpretation and Skill Governance rhymed closely (obligation vs. authority, same structure) | New model: Control Interpretation (obligation setting) is Queen Keyport; Skill Governance (integrity checking) splits into Queen Keyport constraints + Argus L99 audit. Different scopes; no duplication. |
| **Structured Memory Underpowered** | Memory defined provenance/trace but not conflict resolution, version authority, or decay | New model: Hermes handles coherence/conflict resolution; Argus handles version authority and drift detection. Structured Memory becomes distributed across two functions with explicit authority boundaries. |

---

## Integration with Current Governance

**For readers of old notes referencing eight operators:**
1. Translate the operator concept using the table above
2. Find the corresponding agent (HEPHAISTOS, Queen Keyport, Hermes, Argus)
3. Note that the function may be narrower now (e.g., Signal Judgment is only evidentiary, not decision authority)
4. Check [[Supersession Registry]] for the full transition context

**For new governance work:**
1. Use the three-agent model, not the eight operators
2. Operator concepts are reference material for understanding the *why* of current discipline requirements, not prescriptive guidance
3. The migration guide above translates old patterns into new ones if needed

---

## Related

- [[EMERAULD Thematic Analysis — Claude-Codex Pass (2026-05-25)]] — thread 2 (second self) + recursion/agent practice
- [[Agatha Unified Skill System — Eight Sovereign Operators]] — deprecated predecessor
- [[HEPHAISTOS Agent Architecture]] — current three-agent model
- [[Supersession Registry]] — formal registry of all transitions
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]] — second transition (linear → co-equal authority)
- [[Governance Controls Integration Dashboard]] — current governance architecture
- [[Provisional Arbitration Charter — Argus Layer 9.5]] — provisional apex-conflict rule for cases where current layers collide
- [[Second Self System — Identity Kernel and Agent Routing Architecture]] — identity/routing architecture for using the agent ecosystem as specialist organs rather than competing selves

---

## References

- `raw sources/agatha-unified-skill-system-2026-04-18.md` — original eight-operator conversation
- `/home/cerebrhoe/hephaistos/CO-EQUAL-AUTHORITY-DECISION.md` — co-equal authority specification
- `/home/cerebrhoe/hephaistos/HEPHAISTOS.md` — current HEPHAISTOS specification
- `/home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md` — current Queen Keyport specification
- `/home/cerebrhoe/hephaistos/HERMES.md` — current Hermes specification
