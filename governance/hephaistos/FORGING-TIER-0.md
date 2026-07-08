---
type: governance-doc
title: 'Tier 0 — Forging: The Foundational Authority Layer'
aliases:
- 'Tier 0 — Forging: The Foundational Authority Layer'
- governance/hephaistos/FORGING-TIER-0
tags:
- governance
- ai
- hephaistos
- governance-doc
- tier
- forging
- scope
- constraints
- authority
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/FORGING-TIER-0.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HEPHAISTOS]]'
---

> **HISTORICAL DOCUMENT — Pre-Wave-1 Architecture (superseded 2026-04-17)**
> Contains Tier 0/Tier 1/Tier 2 hierarchy language that does not reflect the current co-equal authority model.
> Binding authority: `CO-EQUAL-AUTHORITY-DECISION.md`, `AGENTS.md`, `HEPHAISTOS.md`, `QUEEN-KEYPORT.md`, `ORCHESTRATION.md`.
> Do not treat tier language in this document as current.

# Tier 0 — Forging: The Foundational Authority Layer

**Established:** 2026-04-05 (Phase 3.2, PHAROS-SUITE Remediation)  
**Authority:** HEPHAISTOS  
**Role in Architecture:** Upstream of Governance. Defines WHAT is being built, BY WHOM, under WHAT CONSTRAINTS, with WHAT EVIDENCE or STRUCTURE is required.

---

## Core Function

Forging is the **entrypoint decision layer** that determines:
- **Artifact type:** What kind of thing is being built (system, dataset, narrative, agent, analysis, policy, process)?
- **Consequence domain:** What is at stake (none, internal, operational, external, regulatory, legal, clinical, reputational)?
- **Scope definition:** What is included/excluded, what success looks like, who is affected?
- **Evidence basis:** What evidence or structure grounds this artifact?
- **Authority order:** Who decides what, and under what constraints from governance?

Once Forging establishes these, **Governance (Tier 1) becomes primary** for that artifact.

---

## Tier 0 Forging Skills (Authority Order)

### 1. ai-agents-architect (Tier 0)
**Function:** Design AI agent systems and coordination patterns. Multi-agent orchestration, reasoning strategies, tool integration, failure modes, observability.

**Authority:** Determines what kind of agent is needed, what coordination pattern is required, what failure modes are unacceptable.

**Typical pairing:** Upstream of `agent-development` (builds it) and `recursive-governance-method` (Tier 1, validates controls).

---

### 2. agent-development (Tier 0)
**Function:** Build and implement AI agents. Code structure, reasoning loops, memory systems, tool integration, testing, refinement.

**Authority:** Translates architect design into implementation. Determines if design is feasible, identifies engineering constraints.

**Typical pairing:** Follows `ai-agents-architect` design. Feeds to `recursive-governance-method` (Tier 1) for control design. Evaluated by `agent-evaluation` (Tier 3).

---

### 3. ai-product (Tier 0)
**Function:** Productionize agents and AI systems. Deployment, scaling, monitoring, versioning, user onboarding, operational readiness.

**Authority:** Determines production requirements, operational constraints, user-facing design, deployment architecture.

**Typical pairing:** Works from `agent-development` output. Feeds operational requirements back to governance for constraint validation.

---

### 4. architecture (Tier 0)
**Function:** Design system architecture. Multi-component systems, integration patterns, data flow, scalability, resilience, trade-off analysis.

**Authority:** Determines what architecture is needed for the artifact, what scalability targets matter, what integration patterns are required.

**Typical pairing:** Upstream of governance for architectural constraints. Coordinates with `database-schema-designer` for data architecture.

---

### 5. database-schema-designer (Tier 0)
**Function:** Design robust database schemas. Data structure, relationships, constraints, scalability, integrity.

**Authority:** Determines what data structure is required before governance review. Establishes schema constraints that affect governance decisions about data access, privacy, integrity.

**Typical pairing:** Part of system architecture (Tier 0). Feeds data constraints to governance (Tier 1) for access control and privacy validation.

---

### 6. lead-research-assistant (Tier 0)
**Function:** Lead research projects. Scope definition, hypothesis formation, methodology selection, prioritization, team coordination.

**Authority:** Determines what research is needed, what scope is appropriate, what questions matter, what evidence is required.

**Typical pairing:** Upstream of research methodology (Tier 3). Defines scope for `qualitative` and `deep-research-notebooklm` to execute.

---

## Relationship to Other Tiers

```
TIER 0 FORGING (Defines WHAT)
  ↓ (feeds scope/artifact definition)
TIER 1 GOVERNANCE (Adds constraints, right-arm review)
  ↓ (implements constraints)
TIER 3-5 EXECUTION (Builds/writes/publishes)
  ↓ (feedback if implementation reveals scope problems)
HERMES DEPLOYMENT & MONITORING
```

---

## Authority Boundaries

### What Forging Authority Covers

- Artifact type and consequence domain classification
- Scope boundaries (what's in, what's out)
- Success criteria for the artifact
- Stakeholder and audience analysis
- Evidence or structure basis
- Upstream decision-making

### What Forging Authority Does NOT Cover

- Governance constraints or policy controls (that's Tier 1)
- Implementation details or execution patterns (that's Tier 3-5)
- Ethical review of governance decisions (that's right-arms in Tier 2)
- Deployment or operational readiness (handled in execution tiers)

**Note:** Forging feeds Governance, which may override or constrain Forging decisions. When they conflict, Governance (with right-arm input) has final authority.

---

## Integration with Governance Tiers

### At HEPHAISTOS → Queen Keyport Handoff

Forging scope goes to Governance with:
- Clear artifact type and consequence domain
- Scope boundaries and success criteria
- Stakeholder analysis
- Evidence basis or structure requirements
- Upstream dependencies (what must be true for this artifact to succeed?)

**Governance adds:** Constraints, right-arm review, bias/ethics gates

---

### At Governance → Execution Tier Handoff

Forging decisions (now constrained by governance) go to execution tiers with:
- Artifact definition (from Forging)
- Governance constraints (from Tier 1)
- Right-arm wisdom assessment (from Tier 2)
- Methodology guidance (from execution tiers)

**Execution tiers implement:** What Forging defined, under Governance constraints

---

## Tier 0 Decision Authority Pattern

When Forging skills are used:

1. **Forging skill defines scope:** "What kind of system/agent/research is needed?"
2. **Governance skill reviews scope:** "Does this serve flourishing? What constraints apply?"
3. **Right-arms assess scope:**
   - Philosopher: Does this system serve wisdom and care?
   - Power-Analyst: Is this structurally feasible? What power asymmetries exist?
4. **Governance synthesizes:** Issues governance decision with constraints
5. **Execution tiers implement:** Build according to scope + constraints
6. **Hermes monitors:** Track if scope definition was accurate

---

## Tier 0 Cross-Linking Patterns

### Agent Development Stack
```
Forging (Tier 0):
  - ai-agents-architect: Design agent architecture
  - agent-development: Build agent
  - ai-product: Productionize agent

Governance (Tier 1):
  - recursive-governance-method: Validate controls and safety

Execution (Tier 3-4):
  - agent-evaluation: Benchmark performance
  - red-team: Identify failure modes
```

### Research Stack
```
Forging (Tier 0):
  - lead-research-assistant: Define research scope

Execution (Tier 3):
  - qualitative: Design research methodology
  - deep-research-notebooklm: Execute research
  - statistical-analysis: Analyze results

Publishing (Tier 4):
  - scientific-writing: Write results
  - peer-reviewed-paper-writer: Prepare for publication
```

### System Architecture Stack
```
Forging (Tier 0):
  - architecture: Design system
  - database-schema-designer: Design data structure

Governance (Tier 1):
  - recursive-governance-method: Validate architecture against policy

Execution (Tier 3-5):
  - Domain-specific implementation skills
```

---

## Tier 0 Documentation Requirements

Every Forging skill assessment must answer:

```
forging_assessment:
  artifact_type: <system|dataset|narrative|agent|analysis|policy|process|other>
  consequence_domain: <none|internal|operational|external|regulatory|legal|clinical|reputational>
  
  scope_definition:
    what_is_included: [list]
    what_is_excluded: [list]
    success_criteria: [list measurable outcomes]
  
  stakeholder_analysis:
    primary_audience: [who will use this]
    secondary_stakeholders: [who else is affected]
    vulnerable_populations: [list any at-risk groups]
  
  evidence_basis:
    what_grounds_this_artifact: [research, structure, requirement]
    evidence_gaps: [what is unknown]
    evidence_threshold: <minimal|moderate|rigorous|scientific|expert|unanimous>
  
  upstream_dependencies:
    depends_on: [what must be true for this to work]
    blocks: [what cannot proceed until this is approved]
  
  forging_authority_verdicts:
    artifact_type_clear: <yes|no>
    scope_boundaries_clear: <yes|no>
    success_criteria_measurable: <yes|no>
    stakeholder_analysis_complete: <yes|no>
    evidence_basis_adequate: <yes|no>
```

This feeds directly to Governance for constraint review.

---

## When Forging Authority is Insufficient

If execution tiers discover that **Forging's scope definition was inaccurate**:

1. **Execution tier escalates to Governance** (Tier 1)
2. **Governance consults Forging** (Tier 0)
3. **Forging reassesses scope** 
4. **Governance issues revised constraints or halts implementation**

This ensures Forging remains accountable for the initial artifact definition.

---

## Tier 0 Authority & Right-Arm Review

**Important:** Forging defines scope, but does NOT bypass right-arm review.

- Philosopher reviews: Does this artifact serve flourishing? Are people dignified?
- Power-Analyst reviews: Is this structurally feasible? Are there power asymmetries?

If right-arms veto Forging scope:
- Forging must redesign scope
- OR HEPHAISTOS escalates for explicit decision on scope viability

This ensures Tier 0 Forging authority is not weaponized to create unwise or unjust artifacts.

---

## Tier 0 as Gatekeeping Authority

Tier 0 Forging is a **gatekeeping layer** that filters what gets defined as an artifact worth Governance review:

- **Bad faith scope?** → Forging flags it; governance doesn't waste time
- **Unclear artifact type?** → Forging clarifies before governance
- **Insufficient evidence?** → Forging identifies gaps before governance
- **Vulnerable populations at risk?** → Forging surfaces before governance (where right-arms review)

This keeps Governance focused on constraints and policy, not foundational scope questions.

---

## Historical Note

**Prior to P3.2 (2026-04-05):**
- Tier 0 was called "Forging" but not formally documented as a tier
- Forging skills were scattered across Tier 1-5 registries
- Authority order was ambiguous (was `ai-agents-architect` governance or forging?)

**P3.2 Consolidation:**
- Established Tier 0 as formal authority layer
- Consolidated Forging skills under clear authority pattern
- Clarified relationship to Governance (Tier 1 is downstream, not parallel)
- Cross-linked skills across tiers with explicit composition patterns

This is the consolidated, authoritative Tier 0 documentation as of 2026-04-05.

## Related

- [[Governance and PHAROS MOC]]
- [[HEPHAISTOS]]
