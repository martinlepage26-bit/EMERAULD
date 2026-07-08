---
type: governance-doc
title: 'Phase 2 Integration Roadmap: Observability & Incident Response'
aliases:
- 'Phase 2 Integration Roadmap: Observability & Incident Response'
- governance/hephaistos/PHASE-2-INTEGRATION-ROADMAP
tags:
- governance
- ai
- hephaistos
- governance-doc
- runbooks
- runbook
- observability
- phase
- incident
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/PHASE-2-INTEGRATION-ROADMAP.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HERMES]]'
---

# Phase 2 Integration Roadmap: Observability & Incident Response

**Dated:** 2026-05-02  
**Status:** Phase 1 complete; Phase 2 ready for intake  
**Scope:** Wiring two new skills into operational systems

---

## Phase 1 Complete

**Deliverables (2026-05-02):**
- `observability-governance` skill spec (production-ready, 450+ lines)
- `incident-response-runbooks` skill spec (production-ready, 380+ lines)
- Registry updates: SKILL-MAP.md, HERMES.md, dispatch-map-canonical.md, EMERAULD/CLAUDE.md
- Skills now canonical; auto-triggered in Hermes routing scope

**Artifact Locations:**
- `/home/cerebrhoe/.codex/skills/observability-governance/SKILL.md`
- `/home/cerebrhoe/.codex/skills/incident-response-runbooks/SKILL.md`

---

## Phase 2 Integration — By Skill

### observability-governance

**Goal:** Three-layer log schema operational in if.blackboard Relay Ledger.

| Phase | Component | Owner | Dependencies | T-Shirt |
|-------|-----------|-------|---|---|
| **2a** | Schema implementation (Agent Execution Trace, Governance Decision Record, Routing & Escalation Log) | Infrastructure/Data (Codex/if.context) | None | M |
| **2b** | if.blackboard Relay Ledger storage binding | Infrastructure/Data | 2a complete | M |
| **2c** | Hermes monitoring integration (read constraint baselines, emit escalation signals) | Hermes implementer | 2b complete | L |
| **2d** | Trismégiste memory ingest (post-session log analysis) | Trismégiste/Memory | 2b complete | S |
| **2e** | Argus audit integration (authority chain verification from logs) | Argus/Audit | 2b + 2c complete | M |

**Phase 2a Inputs:**
- Schema file from observability-governance SKILL.md § Runbook Design: Three Components (lines ~60–95)
- JSON structure for trace_id, governance_decision_id, routing_decision_id
- Baseline constraint format (metric, baseline_min, baseline_max, escalation_threshold)

**Phase 2c Trigger:** When Hermes routes work, Hermes queries observability-governance schema for:
- Active constraints on this task scope
- Baseline expectation (metric, min/max)
- Escalation threshold

**Phase 2d Trigger:** Post-session, Trismégiste queries: "What constraints were violated? What escalations occurred? What root causes were identified?" Writes to operator continuity log.

**Phase 2e Trigger:** Argus audits: "Can I trace each escalation back through governance decision → routing → constraint?" Validates causality.

---

### incident-response-runbooks

**Goal:** Runbooks operational in Hermes escalation handler; chaos test framework validated.

| Phase | Component | Owner | Dependencies | T-Shirt |
|-------|-----------|-------|---|---|
| **2f** | Runbook authoring for critical constraints (latency, throughput, resource quota, data consistency, availability) | Domain expert (engineering lead or SRE) | None | M |
| **2g** | Hermes escalation handler integration (receive signal → lookup runbook → execute decision tree) | Hermes implementer | 2f complete | M |
| **2h** | Recovery procedure validation (manual test of each runbook in staging) | QA/SRE | 2f + 2g complete | M |
| **2i** | Chaos testing framework (automated failure injection, runbook execution, constraint restoration verification) | QA/Testing | 2f + 2g + 2h complete | L |
| **2j** | Post-mortem ingest pipeline (capture timeline, root cause, corrective actions → Trismégiste) | Data/Trismégiste | 2g complete | S |
| **2k** | Governance feedback loop (analyze incident frequency, recommend constraint changes) | Queen Keyport/Analytics | 2i + 2j complete | M |

**Phase 2f Inputs:**
- Incident types from observability-governance (constraint violations detected)
- Decision tree template from incident-response-runbooks SKILL.md § Runbook Design: Component 1
- Recovery procedure template from § Component 2

**Phase 2g Trigger:** When observability-governance emits escalation_flag = "critical", Hermes:
1. Looks up constraint name in runbook registry
2. Executes decision tree (diagnosis → recovery or escalation)
3. If recovery: execute steps, rollback if needed, verify constraint
4. If escalation: hand to Queen Keyport or Operator with full context

**Phase 2j Trigger:** After runbook resolution, capture:
- Timeline (T+0: baseline, T+Xs: violation detected, T+Ys: action taken, T+Zs: constraint restored)
- Root cause analysis (primary + contributing factors)
- Recovery evaluation (which runbook? success or failure? manual interventions?)
- Corrective actions (prevent recurrence, improve detection, improve runbook)

**Phase 2k Trigger:** Post-mortem summary fed to Queen Keyport for governance re-evaluation: "Is this constraint still correct? Should it change?"

---

## Phase 2 Sequencing

**Critical path:**
```
2a (schema) → 2b (storage) → {2c, 2d, 2e} (parallel monitoring/memory/audit)
2f (runbooks) → 2g (handler) → 2h (validation) → {2i, 2j} (parallel chaos/capture) → 2k (feedback)
```

**Recommended intake order:**
1. **Week 1:** 2a + 2f (schema + runbook authoring in parallel)
2. **Week 2:** 2b + 2g (storage + handler wiring in parallel)
3. **Week 3:** 2c + 2h (Hermes monitoring + manual validation in parallel)
4. **Week 4:** 2d + 2i + 2j (Trismégiste ingest + chaos framework + post-mortem capture in parallel)
5. **Week 5:** 2e + 2k (Argus audit + governance feedback loop in parallel)

**No-Op Dependency:** 2c, 2d, 2e can start after 2b without waiting for 2g/2h to complete (observability is independent of incident handling).

---

## Go/No-Go Criteria — Phase 2 Entry

Before Phase 2a intake, verify:

- [ ] observability-governance and incident-response-runbooks specs are locked (no schema changes)
- [ ] Hermes implementer committed to 2g (escalation handler work)
- [ ] QA/SRE team committed to 2h (manual runbook validation)
- [ ] if.blackboard Relay Ledger storage is available (check infra readiness)
- [ ] Trismégiste memory system ready for 2d ingest (session-state.md working)
- [ ] Argus audit framework ready for 2e integration (seven-layer audit active)

---

## Success Criteria — Phase 2 Complete

- ✅ Three-layer log schema fully operational (logs written and readable)
- ✅ Hermes routes with observability baseline (knows what "normal" looks like)
- ✅ Escalations are self-explaining (context includes constraint + baseline + actual + recovery attempted)
- ✅ Runbooks tested in chaos (all critical constraints have validated runbooks)
- ✅ Post-mortems captured (timeline, root cause, corrective actions in operator continuity log)
- ✅ Queen Keyport can re-evaluate constraints based on incident history
- ✅ Argus can audit full escalation chain without reconstruction

---

## Implementation Notes

**Schema Stability:** The three-layer log schema is locked in SKILL.md (lines ~60–95 observability-governance, lines ~110–190 incident-response-runbooks). Do not change field names or JSON structure without re-gating through governance.

**Runbook Registry:** Central registry needed (location TBD, likely in if.blackboard or a Hermes-accessible store) mapping constraint_name → runbook_spec. Design in Phase 2f.

**Chaos Test Coverage:** Minimum viable set = 5 runbooks (latency, throughput, quota, consistency, availability) tested. Start there; expand as needed.

**Feedback Loop Frequency:** Governance feedback loop runs post-incident (reactive) or monthly (proactive). Design frequency in Phase 2k.

---

## Phase 3 & Beyond (Not Scope of This Roadmap)

- Expansion of runbook coverage (beyond 5 critical constraints)
- Automation of recovery procedures (currently manual via runbook steps)
- Advanced chaos testing (multi-failure scenarios, cascading constraints)
- Cost-governance and performance-engineering skills (lower priority; defer to Phase 3 planning)

---

## References

- `/home/cerebrhoe/.codex/skills/observability-governance/SKILL.md` — three-layer schema design
- `/home/cerebrhoe/.codex/skills/incident-response-runbooks/SKILL.md` — runbook templates and integration points
- `/home/cerebrhoe/hephaistos/SKILL-MAP.md` — canonical skill registry
- `/home/cerebrhoe/hephaistos/HERMES.md` — Hermes contract and escalation model

## Related

- [[Governance and PHAROS MOC]]
- [[HERMES]]
