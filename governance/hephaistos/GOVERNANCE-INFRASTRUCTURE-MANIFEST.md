---
type: governance-doc
title: Governance Infrastructure Manifest
aliases:
- Governance Infrastructure Manifest
tags:
- governance
- ai
- hephaistos
- governance-doc
- binding
- entrypoints
- agentname
- bowie
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/GOVERNANCE-INFRASTRUCTURE-MANIFEST.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Post Dr Sort Rename Residuals — 2026-05-06]]'
- '[[governance/governance-index]]'
- '[[governance/hephaistos/HERMES]]'
---

# Governance Infrastructure Manifest

**Date:** 2026-05-02  
**Consolidation Run:** BOWIE Session 3 (applied mode)  
**Authority:** HEPHAISTOS + Queen Keyport co-equal  
**Scope:** Canonical governance files, agent entrypoints, binding specifications, skill registry

---

## Canonical Entrypoints

The seven canonical agents operate through these entrypoints. No alternatives; no duplicates.

| Agent | Entrypoint | Role | Position | Last Updated |
|-------|-----------|------|----------|---|
| **HEPHAISTOS** | `/home/martin/.agents/hephaistos/HEPHAISTOS.md` | Scope, forging, artifact definition | Tier 0 (co-equal) | 2026-04-23 |
| **Queen Keyport** | `/home/martin/.agents/hephaistos/QUEEN-KEYPORT.md` | Governance, constraints, approval thresholds | Tier 1 (co-equal) | 2026-04-23 |
| **Hermes** | `/home/martin/.agents/hephaistos/HERMES.md` | Routing, integration, monitoring, escalation | Tier 2 (downstream) | 2026-04-23 |
| **Argus** | `/home/martin/.agents/hephaistos/argus/argus-contract.md` | Meta-governance audit, drift detection, authority-chain review | Independent | varies |
| **HENRY** | `/home/martin/.agents/hephaistos/HENRY.md` | Research writing, peer-review prep, long-form synthesis | Independent specialist | 2026-04-23 |
| **Gadget** | `/home/martin/.agents/hephaistos/GADGET.md` | Frontier scout, external integrations, MCPs, APIs, tool selection | Independent specialist | 2026-04-23 |
| **Trismégiste** | `/mnt/c/Users/softinfo/Documents/EMERAULD/CLAUDE.md` | Operator continuity, vault synthesis, personal knowledge graph | Independent parallel | 2026-04-23 |

---

## Root Dispatch Authority

**File:** `/home/martin/AGENTS.md`  
**Role:** Universal trigger-phrase dispatcher, dispatch rule interpreter, canonical agent identity registry  
**Last Updated:** 2026-04-23  
**Status:** authoritative; no overrides exist

Trigger pattern: `[AgentName], [verb]` OR `[verb] [AgentName]` OR `[AGENTNAME]:` (universal trigger verbs apply to all agents: load, come, spawn, invoke, please, help, activate, run)

---

## Binding Specifications

Non-negotiable governance rules that apply across all agents and all work.

| Document | Rule | Owner | Status |
|----------|------|-------|--------|
| `CO-EQUAL-AUTHORITY-DECISION.md` | HEPHAISTOS and Queen Keyport are co-equal; neither has veto by default | Martin | binding |
| `DIAMOND-EYES.md` | Wisdom and care validation gate (non-negotiable before promotion) | HEPHAISTOS | binding |
| `L99-DEMOTION-TO-ARGUS.md` | Meta-governance audit criterion; violation triggers Argus escalation | Argus | binding |
| `ORCHESTRATION.md` | Multi-agent handoff packets and composition patterns | Martin | binding |
| `SPECIALIST-GUIDELINE-AUTHORITY.md` | Binding vs advisory split for independent specialists consulting HEPHAISTOS | Martin | binding |

**Seven Ethical Ground Values** (binding, non-negotiable):
1. Equity promoting equality
2. Social justice
3. Representation of oppressed communities
4. Intersectionality
5. Anti-oppressive practice
6. Cultural safety
7. System answering to the human and the humane

---

## Skill Registry

**File:** `/home/martin/.agents/hephaistos/SKILL-MAP.md`  
**Last Updated:** 2026-05-02  
**Status:** production-ready; canonical source for all skill routing decisions

**Registry state:**
- **Total skills:** 52 (canonical, non-overlapping)
- **Primary skills (Hermes auto-triggers):** 9 (observability-governance + incident-response-runbooks registered 2026-05-02)
- **Forging skills:** 15+ (scope, artifact, evidence)
- **Governance skills:** 12+ (controls, approvals, consequence)
- **Routing skills:** 9 (coordination, monitoring, escalation)
- **Research skills:** 10+ (analysis, synthesis, evaluation)
- **Independent specialists:** 3 (HENRY, Gadget, Trismégiste)

**Canonical skill file structure:** `skills/[skill-name]/SKILL.md` (single source of truth; flat SKILL_*.md shortcuts deleted 2026-05-02)

**Gaps closed (2026-05-02):**
- ✅ Observability (HIGH) — observability-governance skill produced and registered
- ✅ Incident Response (MEDIUM) — incident-response-runbooks skill produced and registered
- ○ Cost Governance (LOW) — identified, not yet prioritized
- ○ Performance Engineering (MEDIUM) — identified, not yet prioritized

---

## Support Agent (BOWIE)

**File:** `/home/martin/.agents/hephaistos/BOWIE.md`  
**Status:** active (not a canonical root-dispatch agent; consolidation operator)  
**Role:** System entropy reduction, file/memory/tracker/index consolidation, redundancy elimination  
**Default mode:** proposed (no irreversible changes without explicit approval)  
**Automation:** monthly thirds (1st, 11th, 21st) + trigger-based runs

**Authority boundaries:**
- ✅ May consolidate system state, deduplicate, archive, index, record
- ❌ May not take over build, routing, governance, audit, or memory ownership

---

## Historical Archive

**Location:** `/mnt/d/HEPHAISTOS-ARCHIVE/`  
**Contents:**
- 8 phase-completion files (PHASE-1-PLAN through PHASE-7-FINAL-REPORT) — archived 2026-05-02
- 80 legacy skill files (`extracted/`) — archived 2026-05-02
- SECRETS-SETUP.md (contained live Cloudflare token) — removed 2026-05-02 after rotation

**Retention:** Archive is read-only reference; no active dependencies

---

## Governance Topology

**Surface separation (canonical per SKILL-MAP):**
- `pharos-suite` → `https://pharos-ai.ca` (PHAROS public product)
- `martinlepage26-bit.github.io` → `https://martin.govern-ai.ca` (Cloudflare Pages project: `martin-lepage-site`; Martin public identity + hephaistos narratives)

**Boundary rule:** PHAROS, COMPASSai, AurorA stay on PHAROS surface. Martin identity, standalone apps, governance/skill tree narratives stay on Martin surface. No cross-boundary publication without explicit routing decision.

---

## Verification Checklist

Before any governance work proceeds:

- [ ] All canonical entrypoints accessible and current
- [ ] SKILL-MAP reflects live skill registry
- [ ] DIAMOND-EYES gate applied before any promotion
- [ ] Queen Keyport + HEPHAISTOS co-equal authority maintained (no collapse)
- [ ] Seven ethical ground values honored
- [ ] L99 audit criteria applied (no narrative-reality gaps)
- [ ] Binding specifications observed (no evasion)
- [ ] Tracker updated at every major change

---

## Next Action

Use this manifest as the handoff packet for Phase 2 infrastructure intake. Verify canonical entrypoints, binding specs, and skill registry before any scaling or new agent integration work.

---

**BOWIE consolidation:** Applied 2026-05-02 15:30 UTC

## Related

- [[Governance and PHAROS MOC]]
- [[HERMES]]
