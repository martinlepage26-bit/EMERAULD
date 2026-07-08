---
type: governance-registry
title: Supersession Registry
aliases:
- Supersession Registry
- wiki/Supersession Registry
tags:
- governance-registry
- wiki
- supersession-registry-md
- forging
- tier
- eight
- operators
- supersession
- color-purple
status: active
created: '2026-04-27'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Supersession Registry.md
backlink_count: 6
backlinks:
- '[[Areas/PHAROS/Architecture Translation Guide — Eight Operators to Three-Agent Stack]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Phase 1 Completion Checklist]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Phase 1 Progress Checkpoint (2026-04-26)]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[governance/hephaistos/WAVE2-CLEANUP]]'
- '[[memory]]'
phase: Phase 1 Infrastructure
---

# Supersession Registry

**Purpose:** Central record of all known architecture transitions, superseded methods, and deprecation dates. Prevents duplicate documentation and ensures clear mapping between old and new approaches.

**Status:** 2 documented transitions; registry seeded 2026-04-27.

---

## Active Supersessions

### Transition 1: Eight Operators → Three-Agent Stack

| Field | Value |
|-------|-------|
| **Old Architecture** | Eight Sovereign Operators (Signal Judgment, Control Interpretation, Structured Memory, Publication Transformation, Structure and Lineage Audit, System Mapping, Design Coherence, Skill Governance) |
| **New Architecture** | Three-Agent Stack (HEPHAISTOS, Queen Keyport, Hermes) with Argus meta-governance layer |
| **Effective Date** | 2026-03-01 |
| **Superseded Note** | [[Agatha Unified Skill System — Eight Sovereign Operators]] |
| **Current Architecture Note** | [[HEPHAISTOS Agent Architecture]] |
| **Rationale** | Eight operators were a preliminary unified skill system. The three-agent model provides clearer scope separation (forging, governance, routing) and co-equal authority enforcement. Eight operators had unresolved tensions (truth vs. trace split, authority duplication, Structured Memory underpowered). Migration distributes operator functions across the three agents + Argus. |
| **Migration Guide** | [[Architecture Translation Guide — Eight Operators to Three-Agent Stack]] |
| **Migration Status** | Draft (2026-04-27) |
| **Notes** | The transition occurred in early March 2026; deprecation marker added retroactively during Phase 1 governance controls build (2026-04-26). Eight operators remain reference material for governance patterns but are not current operating model. |

---

### Transition 2: Linear Authority → Co-Equal Authority

| Field | Value |
|-------|-------|
| **Old Authority Model** | Tier-based hierarchy: Tier 0 (HEPHAISTOS/forging) upstream of Tier 1 (Queen Keyport/governance), both upstream of Tier 2 (Hermes/routing) |
| **New Authority Model** | Co-Equal Authority: HEPHAISTOS and Queen Keyport operate in separate, non-hierarchical scopes (forging vs. governance). Neither outranks the other. Hermes receives work only after both clear their scopes or after operator arbitration. |
| **Effective Date** | 2026-04-23 |
| **Binding Specification** | `CO-EQUAL-AUTHORITY-DECISION.md` (external to vault; canonical source: `/home/cerebrhoe/hephaistos/CO-EQUAL-AUTHORITY-DECISION.md`) |
| **Superseded Terminology** | "Tier 0/1/2" hierarchy; "forging is upstream of governance"; "governance has final word" |
| **Rationale** | The tier model implied forging defines scope first, governance reviews it second. This inverts the requirement that governance constraints must be present at the moment scope is defined. Co-equal authority enforces this simultaneity: both forging scope and governance constraints are developed in parallel. Conflicts between them are arbitrated by the operator, not resolved by ranking. |
| **Scope-Based Replacement Language** | `scope: forging`, `scope: governance`, `scope: routing` (replaces `Authority Tier N` labels) |
| **Migration Guide** | [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]] |
| **Migration Status** | Complete (2026-04-23). All files transitioned; tier vocabulary decommissioned. |
| **Right-Arm Ownership Correction** | Philosopher and fully-rounded-power-analyst are right-arms to Queen Keyport (governance scope), not to HEPHAISTOS (forging scope). This ensures governance receives input from conceptual vetting (philosopher) and power/incentive analysis (power-analyst) — inputs that belong to governance decisions, not forging decisions. |
| **Notes** | Wave 1 (2026-04-18) and Wave 2 (same day) cleanup completed all identified contradictions. Wave 3 items (4 remaining references) closed during follow-on registry normalization on same day. Tier language fully purged from operational files. |

---

## Schema

Every supersession entry includes:

| Field | Required | Notes |
|-------|----------|-------|
| Old Architecture / Model | Yes | What existed before |
| New Architecture / Model | Yes | What replaced it |
| Effective Date | Yes | When the transition took effect (absolute date, not relative) |
| Superseded Note(s) | Yes | Wiki links to notes that are now deprecated |
| Current Architecture Note(s) | Yes | Wiki links to notes that describe the new approach |
| Rationale | Yes | Why the change was made; what problem was solved |
| Migration Guide | Conditional | Link to detailed translation guide (required if translation is complex or non-obvious) |
| Migration Status | Yes | Draft / In Progress / Complete |
| Notes | No | Historical context, open questions, or implementation notes |

---

## Integration with Governance Workflow

**Before approving a governance decision:**
1. Check the decision's architectural assumptions
2. If the assumption references an entry in the Supersession Registry, verify it uses the NEW architecture, not the OLD one
3. If the decision is based on a superseded approach, flag for re-assessment before approval

**When creating a new note on a topic that has a supersession entry:**
1. Link to the relevant current architecture note
2. Do NOT reference the superseded approach unless providing historical context
3. If the old approach has value as reference material, create a separate "Historical Context" section and link clearly

---

## Related

- [[Governance Controls Integration Dashboard]] — Layer 0.5 gate includes deprecation validation
- [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]] — operational protocol for handling deprecated architectures
- [[Governance and PHAROS MOC]] — primary index for governance notes
- [[HEPHAISTOS Agent Architecture]] — current three-agent model description

---

- [[WAVE2-CLEANUP]]
## Open Questions

1. Should the registry track supersession _candidates_ (architecture revisions that may be coming but not yet effective), or only completed transitions?
2. If a superseded architecture is still in use in some components (intentionally or accidentally), should the registry entry flag this as a "partial transition" or require that all uses be migrated before effective date?
3. How often should the registry be audited to ensure no new supersessions are missing from this document?
