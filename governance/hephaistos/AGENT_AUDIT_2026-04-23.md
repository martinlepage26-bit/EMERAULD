---
type: governance-doc
title: Agent Ecosystem Audit — 2026-04-23
aliases:
- Agent Ecosystem Audit — 2026-04-23
- governance/hephaistos/AGENT_AUDIT_2026-04-23
tags:
- governance
- ai
- agents
- hephaistos
- governance-doc
- gadget
- argus
- henry
- color-orange
status: active
created: '2026-04-23'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/AGENT_AUDIT_2026-04-23.md
backlink_count: 4
backlinks:
- '[[wiki/Agent Ecosystem Audit — 2026-04-23]]'
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Post Dr Sort Rename Residuals — 2026-05-06]]'
- '[[governance/hephaistos/HEPHAISTOS]]'
---

# Agent Ecosystem Audit — 2026-04-23

**Auditor:** Claude (Opus 4.7, max-effort, OODA gating)
**Operator:** Martin Lepage, PhD
**Branch:** `audit/agents-2026-04-23` (hephaistos repo, branched from dirty `master`)
**Scope locked at audit start (operator confirmation):**
- `~/PHAROS-SUITE` (monorepo; `repos/CompassAI`, `repos/AurorA`, `PHAROS-NEWLOOK`)
- `/home/cerebrhoe/.claude/skills/` (99 skills) + `/home/cerebrhoe/.codex/skills/` (250) + `/home/cerebrhoe/hephaistos/skills/` (46) + `/home/cerebrhoe/PHAROS-SUITE/skills/` (18)
- `/mnt/d/MASTER PACK/APEX_PAPERS_COMMON` (D-drive)
- `/mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY`
- `/home/cerebrhoe/HEPHAISTOS_BUILD`, `/home/cerebrhoe/hephaistos`
- EMERAULD vault CLAUDE.md (Trismégiste entrypoint)

**Declared authority table (operator, this request):**

| Agent | Role | Position | Reports to |
|---|---|---|---|
| HEPHAISTOS | Artifact, scope, evidence | Co-equal with Queen Keyport | Operator (on conflict) |
| Queen Keyport | Governance, controls, constraints | Co-equal with Hephaistos | Operator (on conflict) |
| Hermes | Routing, monitoring, escalation | Downstream of H and QK | Both H and QK |
| Argus | Audit and meta-governance | Independent — not in the hierarchy | Operator |
| Trismégiste | Operator continuity and synthesis | Parallel — external to the hierarchy | Operator |
| HENRY | Research writing execution | Independent — at Argus level, follows Hephaistos's methodological guidelines | Operator |
| Gadget | External systems and APIs | Independent — at Argus level, follows Hephaistos's methodological guidelines | Operator |

---

## Executive Summary

The three-agent core (HEPHAISTOS / Queen Keyport / Hermes) is **correctly aligned** with the co-equal authority table on its canonical entrypoints in `/home/cerebrhoe/hephaistos/{HEPHAISTOS,QUEEN-KEYPORT,HERMES}.md`. Everything else drifts — materially and in multiple directions.

Four cross-surface drift vectors dominate:

1. **Tier-0/1/2 hierarchy language persists** on the `.claude/agents/*.md` dispatch configs for Hephaistos, Queen Keyport, and Hermes; and in the `Tier` column of the root `AGENTS.md` dispatch table. This contradicts `CO-EQUAL-AUTHORITY-DECISION.md` which was decided 2026-04-17 and explicitly lists these files as needing update.
2. **Argus is wired INTO the hierarchy** in `argus-contract.md §2.1` and `argus-manifest.md "Stack Integration"` — positioned at "Layer 9" under Queen Keyport's "governance umbrella." The declared table places Argus independent, reporting to Operator.
3. **HENRY and Gadget have no "Argus-level / reports-to-Operator" framing anywhere on disk.** Zero surfaces contain the declared position. The `.claude/agents/` configs place them "outside the governance stack (HEPHAISTOS, Queen Keyport, Hermes, Argus)" — which means "outside Argus too," not "at Argus level." The `hephaistos/{HENRY,GADGET}.md` entrypoints (edits I made earlier this session) position them as "Specialist" tier "subject to Queen Keyport override" — invented authority not in the table.
4. **Trismégiste has no Claude-subagent dispatch file.** Six PHAROS agents exist in `.claude/agents/`; Trismégiste is absent. Dispatch works only via trigger-phrase rules in `AGENTS.md`.

**Critical broken skills:** Hermes's three declared sub-skills (`hermes-dependency-mapper`, `hermes-integration-monitor`, `hermes-escalation-router`) and Gadget's build-mode skills (`builder-core`, `launch-pipeline`) are **missing from disk**. These are invocation-path failures.

**Architectural confusion:** `/mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/agent-hephaistos/AGENTS.md` describes a **completely different governance architecture** (Master Agent, Shadow Auditors, Meta Council, Professor X, Pathos, Manos, Evolution Engine) while labeled "AGENT HEPHAISTOS" — not the three-agent stack. Unresolved: legacy, alternative, or current.

**32 findings logged** (F-001 to F-032). Severity distribution: **13 HIGH, 18 MEDIUM, 1 LOW**.

**Pre-commit lint self-caught drift (during audit finalization):** attempting to commit this audit report on the audit branch tripped `/home/cerebrhoe/hephaistos/scripts/lint_authority_chain.py` with two findings unrelated to the audit content itself. The lint itself is evidence of drift F-031 and F-032 below. Report was kept uncommitted (file durable on disk, staged) rather than bypassing the hook with `--no-verify`.

---

## 0. Required Operator Decision Before Phase F

*Elevated from the self-critique appendix because Phase F remediation cannot proceed without this resolution.*

This conversation has produced three authoritative framings for HENRY/Gadget authority placement. They are not all compatible.

| Framing | Source | Position | QK authority over HENRY/Gadget |
|---|---|---|---|
| **1** (pre-this-session) | `.claude/agents/henry.md`, `.claude/agents/gadget.md` on disk | "Outside the governance stack (HEPHAISTOS, Queen Keyport, Hermes, Argus)" — outside Argus too | "Not ethics-gated" (Gadget); no QK role named |
| **2** (earlier this session, your instruction) | "Henry and Gadget DO NOT report to Hephaistos, they follow his guidelines only. He can change what they did if QK finds governance issues in their work." | Follow H's guidelines; subject to QK governance override | Yes — QK can require changes |
| **3** (this audit request, declared authority table) | Operator's agent-roster table at the top of this request | Independent — at Argus level; reports to Operator; consults H guidelines as reference | No — QK override not named |

**My edits earlier this session** (to `hephaistos/HENRY.md`, `hephaistos/GADGET.md`, `hephaistos/AGENTS.md`) implemented framing 2. This audit evaluates against framing 3. Remediation items **R2, R3, R4, R9, R10, R12, R13, R16** all assume framing 3 is canonical.

**Decision needed before Phase F:**
- (a) Confirm framing 3 canonical; treat framing 2 as superseded; proceed with remediation.
- (b) Reconcile framings 2 and 3 (e.g., keep "consults H guidelines" but reinstate QK override language); tell me which language goes to disk.
- (c) Something else — your call.

Separately, the audit found two governance documents that complicate this decision:
- `PHAROS METHOD REPOSITORY/agent-hephaistos/AGENTS.md` — a **completely different architecture** (Master Agent, Shadow Auditors, Meta Council, Professor X, etc.) also labeled "AGENT HEPHAISTOS" (F-018).
- `PHAROS METHOD REPOSITORY/ARBITRATION/PROVISIONAL_ARBITRATION_CHARTER_v1.2.md` — a **constitutional arbitration charter** naming Argus, Henry/Reviewer-#2, and four authority candidates in a 20-layer stack where "the stack's apex is ungoverned" (F-028).

Either of these may represent a parallel authority model you are still reconciling. If so, Phase F should wait until the target model is single-valued.

---

## 1. Inventory

### 1.1 Agent surfaces (16 surfaces across 7 agents)

| Agent | Surface | Path | Lines | Last mod | Notes |
|---|---|---|---|---|---|
| HEPHAISTOS | canonical entrypoint | `/home/cerebrhoe/hephaistos/HEPHAISTOS.md` | 148 | 2026-04-18 | Co-equal framing correct |
| HEPHAISTOS | `.claude/agents/` config | `/home/cerebrhoe/.claude/agents/hephaistos.md` | 121 | 2026-04-18 | **Tier 0, H→QK→Hermes sequence** |
| HEPHAISTOS | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 17 | — | 2026-04-23 | **Tier column = 0** |
| HEPHAISTOS | ops reference | `/home/cerebrhoe/hephaistos/HEPHAISTOS_OPERATIONS.md` | — | 2026-04-18 | not checked in pass 1 |
| Queen Keyport | canonical entrypoint | `/home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md` | 180 | 2026-04-23 (dirty) | Co-equal framing correct |
| Queen Keyport | `.claude/agents/` config | `/home/cerebrhoe/.claude/agents/queen-keyport.md` | 79 | 2026-04-18 | **Tier 1 governance agent** |
| Queen Keyport | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 18 | — | 2026-04-23 | **Tier column = 1** |
| Queen Keyport | ops reference | `/home/cerebrhoe/hephaistos/QUEEN-KEYPORT_OPERATIONS.md` | — | 2026-04-18 | not checked in pass 1 |
| Hermes | canonical entrypoint | `/home/cerebrhoe/hephaistos/HERMES.md` | 133 | 2026-04-18 | Correct downstream framing |
| Hermes | `.claude/agents/` config | `/home/cerebrhoe/.claude/agents/hermes.md` | 74 | 2026-04-18 | Tier 2 — downstream-consistent |
| Hermes | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 19 | — | 2026-04-23 | Tier column = 2 |
| Argus | contract | `/home/cerebrhoe/hephaistos/argus/argus-contract.md` | 294 | 2026-04-18 | **QK above Argus (§2.1)** |
| Argus | manifest | `/home/cerebrhoe/hephaistos/argus/argus-manifest.md` | 243 | 2026-04-23 (dirty) | **Layer 9, under QK umbrella** |
| Argus | formation | `/home/cerebrhoe/hephaistos/argus/argus-formation.md` | 196 | 2026-04-18 | Consistent with audit function |
| Argus | persona | `/home/cerebrhoe/hephaistos/argus/argus-persona.md` | 246 | 2026-04-09 | Voice characterization — no hierarchy drift |
| Argus | `.claude/agents/` config | `/home/cerebrhoe/.claude/agents/argus.md` | 108 | 2026-04-18 | Independent-observer framing; OK |
| Argus | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 20 | — | 2026-04-23 | Tier = Layer (vague) |
| HENRY | entrypoint (my edit) | `/home/cerebrhoe/hephaistos/HENRY.md` | 264 | 2026-04-23 | **"Subject to QK override" — invented** |
| HENRY | `.claude/agents/` config | `/home/cerebrhoe/.claude/agents/henry.md` | 175 | 2026-04-23 | **No mention of H guidelines; "outside Argus" too** |
| HENRY | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 21 | — | 2026-04-23 | **Tier = Specialist** (not Argus-level) |
| HENRY | constitutional row (my edit) | `/home/cerebrhoe/hephaistos/AGENTS.md` Specialist section | — | 2026-04-23 | **Same drift** |
| Gadget | entrypoint (my edit) | `/home/cerebrhoe/hephaistos/GADGET.md` | 226 | 2026-04-23 | **"Subject to QK override" — invented** |
| Gadget | `.claude/agents/` config | `/home/cerebrhoe/.claude/agents/gadget.md` | 173 | 2026-04-23 | **No mention of H guidelines; "not ethics-gated"** |
| Gadget | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 23 | — | 2026-04-23 | **Tier = Boundary** (not Argus-level) |
| Gadget | constitutional row (my edit) | `/home/cerebrhoe/hephaistos/AGENTS.md` Specialist section | — | 2026-04-23 | **Same drift** |
| Trismégiste | EMERAULD entrypoint | `/mnt/c/Users/softinfo/Documents/EMERAULD/CLAUDE.md` | 191 | — | "Hermes's shadow, external to infrastructure" ✓ |
| Trismégiste | operator state file | `/home/cerebrhoe/trismegiste-state.md` | 164 | 2026-04-21 | Continuity file |
| Trismégiste | EMERAULD session state | `/mnt/c/Users/softinfo/Documents/EMERAULD/session-state.md` | — | 2026-04-23 | Vault persistence |
| Trismégiste | `.claude/agents/` config | **MISSING** | — | — | **F-001: no trismegiste.md** |
| Trismégiste | root dispatch row | `/home/cerebrhoe/AGENTS.md` line 22 | — | 2026-04-23 | Tier = Shadow (consistent) |

### 1.2 Handoff packets (schemas)

| Packet | Path | Status | Consistent with table? |
|---|---|---|---|
| HEPHAISTOS → Queen Keyport | `hephaistos-to-queen-keyport.md` | Active (2026-04-09) | Yes — co-equal, no "primary over" |
| Queen Keyport → Hermes | `queen-keyport-to-hermes.md` | Active (2026-04-09) | Yes — uses `co-equal-arbitration-recorded` resolution |
| Operator → HENRY | **none** | — | Gap (F-023) |
| Operator → Gadget | **none** | — | Gap (F-023) |
| HEPHAISTOS ⇢ HENRY (guideline pull) | **none** | — | Gap (F-024) |
| HEPHAISTOS ⇢ Gadget (guideline pull) | **none** | — | Gap (F-024) |
| Argus → Operator | **none** (ledger format in argus-contract §6.5) | — | Partial: Relay Ledger schema exists; no explicit Operator handoff |
| Trismégiste → Operator | **none** | — | Gap (F-025) |

### 1.3 Skill counts

| Directory | SKILL.md count |
|---|---|
| `/home/cerebrhoe/.claude/skills/` | 99 |
| `/home/cerebrhoe/.codex/skills/` | 250 |
| `/home/cerebrhoe/hephaistos/skills/` | 46 |
| `/home/cerebrhoe/PHAROS-SUITE/skills/` | 18 |
| **Total (with shadowing)** | **406 SKILL.md files** |
| **Unique skill names** | **252** |
| **Skills shadowed across all 3 canonical dirs** | **25** |
| **Skills only in `.codex`** | **153** (codex-exclusive) |
| **Skills only in `.claude`** | **2** |
| **Skills only in `hephaistos/`** | **3** (`agent-management`, `ma-degree-guide`, `prompt-engineer`) |

### 1.4 PHAROS monorepo components checked

- `/home/cerebrhoe/PHAROS-SUITE/repos/CompassAI/` — present (backend, frontend, audit_profile.yaml, design_guidelines.json)
- `/home/cerebrhoe/PHAROS-SUITE/repos/AurorA/` — present (backend, frontend, pharos_canon.py, pharos_state_engine.py)
- `/home/cerebrhoe/PHAROS-SUITE/PHAROS-NEWLOOK/` — present
- `/mnt/c/Users/softinfo/Documents/HERMES Dashboard/` — present (hermes.py, build, dist)
- `/mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/agent-hephaistos/` — **F-018 — different architecture entirely**
- `/mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/ARBITRATION/PROVISIONAL_ARBITRATION_CHARTER_v1.2.md` — **F-028 — constitutional provisional, 20-layer stack, "apex is ungoverned"**
- `/home/cerebrhoe/personal-assistant/trismegiste/` — **F-029 — parallel Trismégiste runtime install (vault, services, CLI), not registered in dispatch table**
- `/home/cerebrhoe/HEPHAISTOS_BUILD/` — grep pass: only data artifacts (csv/json), no agent configs. Confirmed: no agent surfaces under `HEPHAISTOS_BUILD/` needing audit this pass.

---

## 2. Per-Surface Five-Check Matrix

**Legend:** ✓ pass · ✗ fail · ⚠ partial · — not applicable · ? not verified in pass 1

### 2.1 Core three-agent stack

| Surface | (1) Loads | (2) Authority line | (3) Invocation | (4) Contract docs | (5) Handoff schemas |
|---|---|---|---|---|---|
| `hephaistos/HEPHAISTOS.md` | ✓ | ✓ co-equal explicit | ✓ trigger phrases defined | ✓ ops ref + right-arms | ✓ → QK packet |
| `.claude/agents/hephaistos.md` | ✓ | **✗ "Tier 0"**, sequences H→QK→Hermes | ✓ name/desc valid | ⚠ references `ma-arts-letters` not in its skill list | ⚠ no explicit handoff schema cited |
| Root `AGENTS.md` H row | ✓ | **✗ Tier column = 0** | ✓ trigger pattern valid | ✓ points to canonical | — |
| `hephaistos/QUEEN-KEYPORT.md` | ✓ | ✓ co-equal explicit | ✓ trigger phrases | ✓ right-arms + ops ref | ✓ → Hermes packet |
| `.claude/agents/queen-keyport.md` | ✓ | **✗ "Tier 1 governance agent"**, "push upstream to Hephaistos" | ✓ | ⚠ references `inner-mind-eye` (skill verify pending) | — |
| Root `AGENTS.md` QK row | ✓ | **✗ Tier column = 1** | ✓ | ✓ | — |
| `hephaistos/HERMES.md` | ✓ | ✓ downstream explicit, does-not-adjudicate | ✓ | ✓ ops ref + handoff contract | ✓ receives QK packet |
| `.claude/agents/hermes.md` | ✓ | ✓ "Tier 2" — aligned with downstream | ✓ | **✗ 3 declared skills missing from disk (F-019)** | — |
| Root `AGENTS.md` Hermes row | ✓ | ✓ Tier column = 2 (consistent) | ✓ | ✓ | — |

### 2.2 Argus

| Surface | (1) Loads | (2) Authority line | (3) Invocation | (4) Contract docs | (5) Handoff schemas |
|---|---|---|---|---|---|
| `argus/argus-contract.md` | ✓ | **✗ §2.1 puts QK ABOVE Argus (F-009)**; §Signatures: "Governance: QK umbrella" (F-010) | ✓ | ✓ 8 sections | ⚠ Relay Ledger schema only (§6.5); no Operator handoff |
| `argus/argus-manifest.md` | ✓ | **✗ "Layer 9" inside stack (F-011)**; Relationships: "under Keyport's governance umbrella" (F-012) | ✓ triggers listed | ✓ contracts referenced | — |
| `argus/argus-formation.md` | ✓ | ⚠ No explicit hierarchy claim — but inherits manifest's Layer 9 positioning | — | ✓ | — |
| `argus/argus-persona.md` | ✓ | ⚠ No hierarchy drift in persona itself | — | ✓ | — |
| `.claude/agents/argus.md` | ✓ | ✓ "does not certify, govern, or build"; "does not take orders" — **matches independence** | ✓ | ✓ references method.md, subjectivity.md, etc. | ⚠ references not verified in pass 1 |
| Root `AGENTS.md` Argus row | ✓ | ⚠ Tier = "Layer" (vague — not "Independent") | ✓ | ✓ | — |

### 2.3 HENRY

| Surface | (1) Loads | (2) Authority line | (3) Invocation | (4) Contract docs | (5) Handoff schemas |
|---|---|---|---|---|---|
| `hephaistos/HENRY.md` (my edit) | ✓ | **✗ "Subject to Queen Keyport override" (F-002)**; follows H guidelines ✓; does-not-report-to-H ✓; **missing "at Argus level" and "reports to Operator"** | ✓ trigger pattern | ⚠ references `HENRY/` ops specs (exist); `DIAMOND-EYES.md` (exists) | ✗ no Operator→HENRY packet |
| `.claude/agents/henry.md` | ✓ | **✗ "outside the governance stack (HEPHAISTOS, QK, Hermes, Argus)" — places HENRY outside Argus too, not "at Argus level" (F-004); no mention of H methodological guidelines (F-003 — methodological drift)** | ✓ frontmatter valid | ✓ 14 skills listed | — |
| Root `AGENTS.md` HENRY row | ✓ | **✗ Tier = "Specialist" (F-015)** | ✓ | ✓ | — |
| `hephaistos/AGENTS.md` Specialist row (my edit) | ✓ | **✗ Same QK-override framing (F-017)** | ✓ | ✓ | — |

### 2.4 Gadget

| Surface | (1) Loads | (2) Authority line | (3) Invocation | (4) Contract docs | (5) Handoff schemas |
|---|---|---|---|---|---|
| `hephaistos/GADGET.md` (my edit) | ✓ | **✗ "Tier: Boundary", "Subject to Queen Keyport override" (F-002)**; does-not-report-to-H ✓; **missing "at Argus level" and "reports to Operator"** | ✓ | ⚠ External System Registry detailed | ✗ no Operator→Gadget packet |
| `.claude/agents/gadget.md` | ✓ | **✗ "external to the governance stack ... not ethics-gated" — contradicts hephaistos/GADGET.md QK-override (F-005); no mention of H methodological guidelines (F-003 — methodological drift)** | ✓ | **✗ `builder-core`, `launch-pipeline` missing from disk (F-020)** | — |
| Root `AGENTS.md` Gadget row | ✓ | **✗ Tier = "Boundary" (F-015)** | ✓ | ✓ | — |
| `hephaistos/AGENTS.md` Specialist row (my edit) | ✓ | **✗ Same QK-override framing (F-017)** | ✓ | ✓ | — |

### 2.5 Trismégiste

| Surface | (1) Loads | (2) Authority line | (3) Invocation | (4) Contract docs | (5) Handoff schemas |
|---|---|---|---|---|---|
| `EMERAULD/CLAUDE.md` | ✓ | ✓ "Hermes's shadow, external to infrastructure, external to Gadget, external to ROOK" — **matches parallel position** | ⚠ trigger-phrase only; no subagent frontmatter | ✓ session-state protocol defined | ✗ no explicit Trismégiste→Operator schema |
| `/home/cerebrhoe/trismegiste-state.md` | ✓ | ✓ consistent | — | ✓ | — |
| Root `AGENTS.md` Trismégiste row | ✓ | ✓ Tier = "Shadow" | ✓ | ✓ | — |
| `.claude/agents/trismegiste.md` | **✗ MISSING (F-001)** | — | **✗ no Claude-subagent dispatch** | — | — |

---

## 3. Handoff Matrix

**9 positive tests + 4 negative tests.**

| # | Source → Target | Expected | Evidence | Verdict |
|---|---|---|---|---|
| P1 | Hephaistos ↔ Queen Keyport | Symmetric co-equal consultation | `hephaistos-to-queen-keyport.md` — "without making forging primary over governance" | ✓ PASS |
| P2 | Hephaistos → Hermes | Downstream routing after governance clears | `queen-keyport-to-hermes.md` required fields; HERMES.md "receives work only after both co-equal authorities have cleared" | ✓ PASS |
| P3 | Queen Keyport → Hermes | Downstream routing after governance clears | `queen-keyport-to-hermes.md` `governance_decision.status == approve`; HERMES.md § Primary Function | ✓ PASS |
| P4 | Operator → HENRY | Direct invocation, no intermediary | `.claude/agents/henry.md` frontmatter: direct subagent invocation available; `hephaistos/HENRY.md` Invocation Pattern: direct trigger | ✓ PASS (routing) / ⚠ no formal schema (F-026) |
| P5 | Operator → Gadget | Direct invocation, no intermediary | `.claude/agents/gadget.md` frontmatter: direct subagent invocation; `hephaistos/GADGET.md` Invocation Pattern | ✓ PASS (routing) / ⚠ no formal schema (F-026) |
| P6 | Hephaistos ⇢ HENRY (guideline pull) | HENRY consults H guidelines as reference | `hephaistos/HENRY.md` line 230: "Follows HEPHAISTOS guidelines" — stated as input; `.claude/agents/henry.md`: **does not mention H guidelines** | **⚠ SPLIT** — hephaistos/HENRY.md pulls; .claude/agents/henry.md has methodological drift (F-003) |
| P7 | Hephaistos ⇢ Gadget (guideline pull) | Gadget consults H guidelines as reference | `hephaistos/GADGET.md` line 46: "Follows HEPHAISTOS guidelines" — stated; `.claude/agents/gadget.md`: **does not mention H guidelines** | **⚠ SPLIT** — hephaistos/GADGET.md pulls; .claude/agents/gadget.md has methodological drift (F-003) |
| P8 | Argus → Operator | Direct audit report, no intermediary | `argus-contract.md §2.2`: some findings route to "Queen Keyport + Operator" (F-013); §2.1: "Chain of Accountability" puts QK between Argus and Operator (F-009) | **✗ FAIL** — routes through QK for some finding types |
| P9 | Trismégiste → Operator | Direct synthesis delivery | `EMERAULD/CLAUDE.md` session-state protocol delivers to operator state files directly; no intermediary defined | ✓ PASS |
| N1 | Hermes → Hephaistos (upstream write) | Must not exist | `HERMES.md §Hephaistos/Queen Keyport Conflict Handling`: "Hermes does not determine which authority is correct...routes conflict explicitly back." No upstream write authority stated. | ✓ PASS (does not exist) |
| N2 | Hephaistos → HENRY/Gadget (binding command) | Must not exist | `hephaistos/HENRY.md` line 232: "Does not report to HEPHAISTOS"; `hephaistos/GADGET.md` line 48: same. `.claude/agents/{henry,gadget}.md`: "outside governance stack." No binding-command channel defined. | ✓ PASS (does not exist) |
| N3 | HENRY/Gadget reachable via H/QK/Hermes chain | Must not be reachable | `hephaistos-to-queen-keyport.md` and `queen-keyport-to-hermes.md` schemas do not name HENRY or Gadget as routing targets. | ✓ PASS |
| N4 | Argus/Trismégiste reachable via normal routing chain | Must not be reachable | Argus is invocable via `.claude/agents/argus.md` (independent subagent) and trigger phrase. Trismégiste via trigger phrase + EMERAULD vault only. Neither listed in handoff schemas. | ✓ PASS |

**Summary:** 8 positive pass; 2 positive split (guideline-pull ambiguous across surfaces); 1 positive fail (Argus→Operator routes through QK); 4 negative pass (negative tests confirm the hierarchy doesn't leak where it shouldn't).

---

## 4. Drift List

### 4.1 Authority-line drift (surface claims mismatch declared table)

**HIGH**
- **F-002** — `hephaistos/HENRY.md`, `hephaistos/GADGET.md`, and `hephaistos/AGENTS.md` Specialist Agents section (all edited by Claude earlier this conversation) position HENRY/Gadget as "autonomous executors subject to Queen Keyport governance override" at "Specialist"/"Boundary" tier. Declared table: "Independent — at Argus level, reports to Operator." Nowhere on disk does "at Argus level" or "reports to Operator" appear for HENRY/Gadget. Evidence: `hephaistos/HENRY.md:228-233`, `hephaistos/GADGET.md:42-49`, `hephaistos/AGENTS.md:60-101`.
- **F-003** — `.claude/agents/henry.md` and `.claude/agents/gadget.md` do not mention HEPHAISTOS's methodological guidelines as input at all. Declared table: "follows Hephaistos's methodological guidelines." Per operator instruction: "if HENRY or Gadget ignore Hephaistos's guidelines entirely when executing their respective domains, flag that as methodological drift." Evidence: `.claude/agents/henry.md:83,157`; `.claude/agents/gadget.md:74,159`.
- **F-006** — `.claude/agents/hephaistos.md` frontmatter line 2: "Tier 0 forging and scope-definition agent." Body line 69-73: "If a task spans all three, sequence them in this order: 1. HEPHAISTOS... 2. Queen Keyport... 3. Hermes." This is the exact hierarchy `CO-EQUAL-AUTHORITY-DECISION.md` was written to supersede. The decision explicitly lists `CLAUDE.md` and `AGENTS.md` as files that must be updated; the decision does not name `.claude/agents/*.md` but the same logic applies.
- **F-007** — `.claude/agents/queen-keyport.md` frontmatter line 2: "Tier 1 governance agent." Line 49: "push the task back upstream to HEPHAISTOS rather than pretending governance can proceed cleanly." "Upstream" implies hierarchy.
- **F-009** — `argus-contract.md §2.1` Chain of Accountability diagram puts Queen Keyport between Argus and Operator: `Human Operator ← Queen Keyport ← Argus ← Hephaistos/Hermes`. Declared table: Argus "Independent — not in the hierarchy, reports to Operator."
- **F-011** — `argus-manifest.md` line 4: "Stack Position: Layer 9 (Arbitration + Formalization)"; Stack Integration diagram places Argus at Layer 9 *inside* a layered stack above the three-agent system at Layer 8. Declared table: Argus "not in the hierarchy."
- **F-012** — `argus-manifest.md` Relationships table: "Argus operates under Keyport's governance umbrella; escalates to Keyport for control decisions." Declared table: Argus reports to Operator.

**MEDIUM**
- **F-004** — `.claude/agents/henry.md` line 83: "operate outside the governance stack (HEPHAISTOS, Queen Keyport, Hermes, Argus)." This places HENRY outside **all four**, not "at Argus level." "At Argus level" (declared table) means peer of Argus, which is a specific positional claim that the file does not make. Same issue in `.claude/agents/gadget.md` line 74.
- **F-005** — Cross-surface contradiction for Gadget on ethics-gating: `.claude/agents/gadget.md:74` "You are not ethics-gated"; `hephaistos/GADGET.md:47` "Subject to Queen Keyport override: If Queen Keyport finds security, governance, or policy issues..." These cannot both be true. Declared table resolves to neither — Gadget reports to Operator, neither "not ethics-gated" nor "subject to QK override" is correct.
- **F-008** — Both `.claude/agents/hephaistos.md` and `.claude/agents/queen-keyport.md` use "upstream" language (line 66, 49 respectively), implying linear hierarchy.
- **F-010** — `argus-contract.md` line 292 Signatures block: "Governance: Queen Keyport (umbrella control)." Puts Argus under QK's control umbrella.
- **F-013** — `argus-contract.md §2.2` Reporting Lines: some finding types (Authority drift) route to "Queen Keyport + Operator"; Skill composition issue routes to "Hephaistos (via Operator)." Mixed direct/indirect routing.
- **F-014** — Root `AGENTS.md` lines 17-19 dispatch table: `Tier` column values `0`, `1`, `2` for HEPHAISTOS, Queen Keyport, Hermes. Tier framing was supposed to be removed by `CO-EQUAL-AUTHORITY-DECISION.md`.
- **F-015** — Root `AGENTS.md` lines 21, 23: `Tier` column values `Specialist` (HENRY) and `Boundary` (Gadget). Declared table: both are "Independent — at Argus level."
- **F-016** — Root `AGENTS.md` line 85 (my edit): "Specialist agents (HENRY, Gadget) are autonomous executors: they follow HEPHAISTOS guidelines and are subject to Queen Keyport governance override." Same invented QK-override authority as F-002.
- **F-017** — `hephaistos/AGENTS.md` lines 60-101 Specialist Agents & Autonomous Executors section (my edit): "subject to Queen Keyport governance override...retroactive governance override by Queen Keyport" and "Queen Keyport's override authority." Same invented authority.

**LOW**
- **F-021** — Zero surfaces on disk contain the declared "at Argus level" or "reports to Operator" positional language for HENRY/Gadget. This is not drift from a competing framing; it is an **absence** of the declared framing.

### 4.2 Hierarchy violations (routing bypass or illegal relays)

**HIGH**
- **F-018** — `/mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/agent-hephaistos/AGENTS.md v1.1` describes a completely different agent ecosystem (Master Agent, Shadow Auditors, Professor X, Alfred, Meta Council, Pathos, Manos, Evolution Engine, Meta Evolution X, Constitution Layer, System Notifier) while labeled "AGENT HEPHAISTOS." Not the three-agent stack. Invocation of "Hephaistos" from that vault could load this file instead of the canonical `/home/cerebrhoe/hephaistos/HEPHAISTOS.md`. Operator must decide: legacy/archive, alternative branch, or current-and-diverged.
- **F-028** — `/mnt/c/Users/softinfo/Documents/PHAROS METHOD REPOSITORY/ARBITRATION/PROVISIONAL_ARBITRATION_CHARTER_v1.2.md` ("Constitutional provisional (Layer 9.5)") names Argus as audit agent, Henry as "Adversarial reviewer / Reviewer #2," and discusses four authority candidates in a 20-layer stack. Declares: "The stack's apex is ungoverned." This is a governance-crisis flag that overlaps with F-018 (different architecture) and the co-equality deadlock gap (§5.1). Operator must decide: is this charter binding on the current three-agent architecture, or part of the PHAROS-METHOD-REPOSITORY alternative-architecture path?
- **F-029** — `/home/cerebrhoe/personal-assistant/trismegiste/` contains a complete Trismégiste runtime implementation (README.md, ask.py CLI, vault/, vault_watcher.py, services/, skills/, scripts/setup.sh). This is a parallel Trismégiste install that is **not registered** in `AGENTS.md` dispatch table, not mirrored to `.claude/agents/`, and not cross-linked from the EMERAULD entrypoint. Either the personal-assistant/trismegiste/ install is the real runtime and EMERAULD/CLAUDE.md is documentation, or vice versa, or they are independent parallel installs. Declared table for Trismégiste is "parallel — external to hierarchy" which is consistent with either, but the fragmentation of surface canonicity is drift.

**MEDIUM**
- **F-030** — `/home/cerebrhoe/personal-assistant/trismegiste/vault/CLAUDE.md` (the memory file surfaced by grep) still references the Obsidian product by its **pre-rename name "BRAINiaC"** in the Active Projects table ("BRAINiaC | Obsidian agent vault product ($49, Gumroad) | Near launch"). Per `EMERAULD/CLAUDE.md`, the rename BRAINiaC → EMERAULD was completed 2026-04-18. The personal-assistant install has stale project naming.
- **F-031** — `/home/cerebrhoe/.codex/skills/free-tool-strategy/` exists as a live skill directory. The `lint_authority_chain.py` (Hephaistos repo's own authority-drift linter) classifies it as "retired gadget skill" that should not exist as a live target. However, `/home/cerebrhoe/.claude/agents/hermes.md` frontmatter still lists `free-tool-strategy` as an active Hermes skill. Live-vs-retired drift; the ecosystem disagrees with its own linter.
- **F-032** — `/home/cerebrhoe/hephaistos/DEPLOYMENT-CHECKLIST.md` declares "Active skill count: 37. Routing stubs (files on disk, not standalone targets): 9. Retired: 1." But `lint_authority_chain.py` requires the snippet "Active skill count: 36" and fails the lint when the deployment-checklist declares 37. Off-by-one drift in skill accounting between the checklist and the lint.

**MEDIUM**
- **F-023** — No `Operator → HENRY` or `Operator → Gadget` handoff schema exists. Per declared table, both are directly invoked by Operator. A schema would lock what Operator must send and what the agent may assume. Currently only the narrative invocation pattern exists in the entrypoint files.
- **F-024** — No `HEPHAISTOS ⇢ HENRY` or `HEPHAISTOS ⇢ Gadget` guideline-publication mechanism specified. Operator instruction: "HENRY and Gadget consume Hephaistos's method/scope guidelines as inputs (reference material), not as commands." There is no machine-checkable pointer file listing which HEPHAISTOS docs HENRY/Gadget are expected to consult.
- **F-025** — No `Trismégiste → Operator` schema. The session-state protocol in `EMERAULD/CLAUDE.md` is narrative ("update these files"), not structured.

### 4.3 Broken skill references (invocation path fails)

**HIGH**
- **F-019** — `.claude/agents/hermes.md` declares skills `hermes-dependency-mapper`, `hermes-integration-monitor`, `hermes-escalation-router`. None exist under `.claude/skills/`, `.codex/skills/`, or `hephaistos/skills/`. Hermes cannot invoke its three declared sub-functions.
- **F-020** — `.claude/agents/gadget.md` declares skills `builder-core` and `launch-pipeline`. Neither exists under any canonical skill directory. Gadget's Build Mode (and its launch-pipeline variant) cannot be invoked.

### 4.4 Missing agents / surfaces

**HIGH**
- **F-001** — No `/home/cerebrhoe/.claude/agents/trismegiste.md` exists. Claude-subagent dispatch for Trismégiste does not work through the Claude-agent subsystem — only through trigger-phrase parsing in `AGENTS.md` plus narrative entrypoint in EMERAULD vault `CLAUDE.md`. Six PHAROS agents have dispatch configs; Trismégiste is the outlier.

### 4.5 Shadowed authored skills

**MEDIUM**
- **F-022** — 25 skills appear in all three canonical skill directories (`.claude/skills/`, `.codex/skills/`, `hephaistos/skills/`). Total shadowed (2+ dirs): 75+ skill names. Without content-level diff, we cannot confirm these are identical vs. drifted copies. Skills referenced by agents (e.g., `peer-reviewed-paper-writer`, `novelist`, `philosopher`, `red-team`, `fully-rounded-power-analyst`) are all in the shadowed set. Which copy wins at runtime depends on Claude Code resolution order.

### 4.6 Guideline-vs-command (the ambiguity the operator pre-declared as a gap)

**MEDIUM**
- **F-026** — `hephaistos/HENRY.md` line 230: "HEPHAISTOS sets what HENRY can legitimately claim and what counts as evidence." Verb "sets" is ambiguous between "publishes guidelines HENRY pulls" and "issues binding instructions HENRY must follow." Operator pre-declared this ambiguity as a structural gap, not to be resolved in this pass. Logging locations where it surfaces.
- **F-027** — `hephaistos/GADGET.md` line 46: "HEPHAISTOS sets the legitimate scope of external system interaction." Same ambiguity as F-026.

---

## 5. Gap Log (log only — not to be resolved in this pass)

### 5.1 Co-equality deadlock (operator pre-declared)
Hephaistos and Queen Keyport can deadlock when they disagree and the Operator is unavailable. Locations where the deadlock surfaces:
- `hephaistos/HEPHAISTOS.md:41-46` — "When their directions conflict... the operator (Martin) arbitrates." No fallback if Martin unavailable.
- `hephaistos/QUEEN-KEYPORT.md:39-44` — same language.
- `hephaistos/HERMES.md:37-47` — Hermes escalates to operator; no timeout/auto-decay behavior if operator unavailable.
- `hephaistos/queen-keyport-to-hermes.md:53` — `co-equal-arbitration-recorded` resolution path assumes arbitration happened; no schema path for "arbitration pending."
- `hephaistos/CO-EQUAL-AUTHORITY-DECISION.md:27-33` — defines the deadlock but explicitly declines to set a fallback.

### 5.2 Guideline-vs-command ambiguity (operator pre-declared)
The line between "methodological guidance HENRY/Gadget are expected to honor" and "guidance HENRY/Gadget may override" is underspecified. Locations:
- `hephaistos/HENRY.md:230` — "sets what HENRY can legitimately claim" (F-026).
- `hephaistos/GADGET.md:46` — "sets the legitimate scope" (F-027).
- `hephaistos/AGENTS.md:68-77` — "guidance, not approval" in specialist section, but "retroactive governance override by Queen Keyport" also present.
- `.claude/agents/henry.md:157` — "Does not route through HEPHAISTOS / Queen Keyport / Hermes. Ethics review, if needed for the content, is the caller's responsibility." This pushes override responsibility onto caller, not onto HENRY or governance.
- `.claude/agents/gadget.md:159` — same pattern.
- **Not a resolution target per operator.** This gap requires a separate operator decision.

---

## 6. Severity-Ordered Remediation Queue

### 6.1 HIGH (13 findings; 8 fix rows + F-028/F-029 newly added below + R-items for broken skills)

| # | Finding | Surface | Fix class |
|---|---|---|---|
| R1 | F-001 | `.claude/agents/` | **Needs Martin's review** — create `trismegiste.md` subagent config. Trismégiste formation/role is defined in EMERAULD/CLAUDE.md but not mirrored as Claude-dispatch. |
| R2 | F-002 / F-016 / F-017 | `hephaistos/HENRY.md`, `hephaistos/GADGET.md`, `hephaistos/AGENTS.md`, root `AGENTS.md` line 85 | Auto-fix: revert Claude-introduced "subject to Queen Keyport override" framing; replace with "Independent — at Argus level, reports to Operator, consults HEPHAISTOS guidelines." One PR per file. |
| R3 | F-003 | `.claude/agents/henry.md`, `.claude/agents/gadget.md` | Auto-fix: add reference-manifest section pointing to the HEPHAISTOS guideline docs HENRY/Gadget are expected to consult (e.g., HEPHAISTOS.md, HEPHAISTOS_OPERATIONS.md, handoff schemas). |
| R4 | F-006 / F-007 / F-008 | `.claude/agents/hephaistos.md`, `.claude/agents/queen-keyport.md` | Auto-fix: remove "Tier 0/1" and "upstream" language; replace with co-equal framing per `CO-EQUAL-AUTHORITY-DECISION.md`. |
| R5 | F-009 / F-010 / F-011 / F-012 | `argus/argus-contract.md`, `argus/argus-manifest.md` | **Needs Martin's review** — these are contract docs. Proposed change: re-position Argus as independent in §2.1 diagram, remove "umbrella" from Signatures, replace "Layer 9" with "Independent Audit — outside hierarchy." Do NOT auto-modify. |
| R6 | F-018 | `PHAROS METHOD REPOSITORY/agent-hephaistos/AGENTS.md` | **Needs Martin's review** — resolve: legacy, alternative, or current. No action without classification. |
| R7 | F-019 | `.claude/agents/hermes.md` + missing skills | Two paths: (a) create the three missing skills, or (b) remove the references from hermes.md frontmatter. Latter is cheaper; operator decides. |
| R8 | F-020 | `.claude/agents/gadget.md` + missing skills | Same structure as R7: create `builder-core`, `launch-pipeline` or remove frontmatter references. |
| R8a | F-028 | `PHAROS METHOD REPOSITORY/ARBITRATION/PROVISIONAL_ARBITRATION_CHARTER_v1.2.md` | **Needs Martin's review** — classify: binding on current three-agent architecture, or part of the PHAROS-METHOD-REPOSITORY alternative-architecture path (F-018). Phase F remediation should reconcile or disambiguate before editing contracts. |
| R8b | F-029 | `/home/cerebrhoe/personal-assistant/trismegiste/` | **Needs Martin's review** — declare canonical: (a) personal-assistant/trismegiste/ is the runtime, EMERAULD entrypoint references it; (b) they are independent; (c) merge. Also: register in AGENTS.md dispatch if (a) or (c). |

### 6.2 MEDIUM (16 items; 11 fix rows + F-022/26/27/30 deferred per note)

| # | Finding | Surface | Fix class |
|---|---|---|---|
| R9 | F-004 | `.claude/agents/{henry,gadget}.md` | Auto-fix: change "outside the governance stack (HEPHAISTOS, Queen Keyport, Hermes, Argus)" to "independent at Argus level; outside the HEPHAISTOS/Queen Keyport/Hermes routing chain; peer of Argus." |
| R10 | F-005 | `.claude/agents/gadget.md`, `hephaistos/GADGET.md` | Auto-fix: resolve the "not ethics-gated" vs "Subject to QK override" contradiction by replacing both with declared-table framing. |
| R11 | F-013 | `argus/argus-contract.md §2.2` | **Needs Martin's review** — Reporting Lines table re-routes all finding types directly to Operator per declared table. |
| R12 | F-014 | Root `AGENTS.md` lines 17-19 | Auto-fix: change `Tier` column values `0`, `1`, `2` to scope labels (`Forging/scope`, `Governance`, `Routing`) or remove the column. |
| R13 | F-015 | Root `AGENTS.md` lines 21, 23 | Auto-fix: change `Specialist` and `Boundary` to `Independent (Argus-level)` for HENRY and Gadget rows. |
| R14 | F-022 | Skill shadowing | Audit: for the 25 skills shadowed across all three dirs, diff content. Create dedup/canonicalization plan. **No auto-fix in this pass** — shadowing may be intentional per-surface (Claude vs. Codex). |
| R15 | F-023 | Missing Operator→HENRY/Gadget schemas | **Needs Martin's decision** — do we need formal JSON schemas for specialist invocation, or is the narrative trigger pattern sufficient? |
| R16 | F-024 | Missing HEPHAISTOS⇢HENRY/Gadget guideline manifest | Proposal: create `hephaistos/GUIDELINES-FOR-SPECIALISTS.md` listing the reference docs HENRY and Gadget consult. Machine-checkable pointer. |
| R17 | F-025 | Missing Trismégiste→Operator schema | Lower priority. Narrative session-state works for now. |
| R18 | F-026 / F-027 | `hephaistos/HENRY.md:230`, `hephaistos/GADGET.md:46` | **Gap log only — do not resolve.** See §5.2. |
| R19 | Argus `.claude/agents/argus.md` references | `.claude/agents/argus.md` references `references/method.md`, `references/subjectivity.md`, etc. These were not verified in pass 1. | Verify existence in pass 2 before any PR. |
| R19a | F-030 | `/home/cerebrhoe/personal-assistant/trismegiste/vault/CLAUDE.md` memory file | Auto-fix: rename "BRAINiaC" → "EMERAULD" in the Active Projects table per the 2026-04-18 rename. Do only after R8b is resolved. |
| R19b | F-031 | `/home/cerebrhoe/.codex/skills/free-tool-strategy/` + `/home/cerebrhoe/.claude/agents/hermes.md` | **Needs Martin's decision** — is `free-tool-strategy` retired (per lint) or active (per Hermes frontmatter)? If retired: remove directory and remove from hermes.md skills list. If active: update lint_authority_chain.py to stop flagging it. |
| R19c | F-032 | `/home/cerebrhoe/hephaistos/DEPLOYMENT-CHECKLIST.md` vs `lint_authority_chain.py` | **Needs Martin's decision** — reconcile: either the lint is correct (checklist should say 36) or the checklist is correct (lint should permit 37). One-line numeric fix once direction is chosen. |

### 6.3 LOW (1 finding + 5 operational nits)

| # | Finding | Surface | Fix class |
|---|---|---|---|
| R20 | F-021 | Zero-surface absence | Auto-fix: ensure R2/R3/R4 text changes actually introduce "at Argus level" and "reports to Operator" language. This is the positive side of R2. |
| R21 | Tier-0/1/2 residue | `hephaistos/FORGING-TIER-0.md`, `FORGING-TIER-0-QUICKSTART.md`, `PHASE-1-PLAN.md`, `INTEGRATION-PROGRESS.md`, `NEXT-STEPS.md`, `DEPLOYMENT-CHECKLIST.md` | **Needs Martin's review** — these are historical phase docs. Decision: rename, archive, or annotate with a "supersede" banner pointing at `CO-EQUAL-AUTHORITY-DECISION.md`. |
| R22 | EMERAULD authority pointer | `EMERAULD/CLAUDE.md` should cite the declared authority table for Trismégiste's position relative to Argus-level specialists | Auto-fix: add one-line citation. |
| R23 | Skills in `hephaistos/skills/` but not in `.codex`/`.claude` (`agent-management`, `ma-degree-guide`, `prompt-engineer`) | Hephaistos-exclusive skills | Verify: are these intentionally hephaistos-only, or should they be mirrored? |
| R24 | Argus references dir | `hephaistos/argus/` has `ai-governance-workflow/` sub-bundle dated 2026-04-23 — not reviewed in pass 1 | Verify: scope/status of this adjacent bundle. |
| R25 | Handoff packet timestamps | `hephaistos-to-queen-keyport.md` / `queen-keyport-to-hermes.md` both dated 2026-04-09 — stable | No action. |

---

## 7. Self-Critique Appendix

*Mandatory per the operator's discipline rules: re-read the report and flag every place I deferred to operator framing instead of testing against actual files.*

### 7.1 Framing-deference flags

- **SC1.** I presented the operator's declared authority table as the oracle against which all surfaces are measured, rather than testing it independently. **In particular:** the operator's table places HENRY and Gadget "at Argus level," but the surfaces say "outside the governance stack (HEPHAISTOS, QK, Hermes, **Argus**)." The surfaces claim HENRY/Gadget are outside *even Argus*, not peer to it. I flagged this as F-004 but did not ask the operator whether the surfaces' framing might be the correct one and the table an aspirational edit. **Verdict:** This is a real ambiguity, not a pure drift. The audit report should have offered both readings.

- **SC2.** F-002, F-016, F-017 — my own edits from earlier this conversation — could be read two ways: (a) I misinterpreted the operator's prior instruction ("He can change what they did if QK finds governance issues"), or (b) the operator's instruction then is inconsistent with the operator's instruction now. I treated (a) as the verdict ("my edits were wrong") without asking the operator to disambiguate. **Verdict:** My edits were at least partially a faithful read of the prior instruction; whether they are drift from the *current* instruction depends on which instruction is canonical. Flagging this as an unresolved meta-drift, not a pure me-error.

- **SC3.** I accepted the operator's characterization of Argus as "independent — not in the hierarchy, reports to Operator" against the canonical `argus-contract.md`/`argus-manifest.md` on-disk position that Argus operates under QK's umbrella at Layer 9. **The contract files are binding documents**, formally signed off with "Contract Version 1.0 (April 2026)." Simply updating them to match the declared table would overwrite a versioned contract. The PR to fix F-009/F-010/F-011/F-012 should be gated on explicit operator approval with the understanding that **this is a contract amendment, not a copy-edit.** I flagged this as "Needs Martin's review" but did not highlight the contract-amendment severity strongly enough.

- **SC4.** I did not diff the 25 fully-shadowed skills (F-022). I only counted them. A drift audit that does not confirm content identity across shadowed copies is incomplete. Pass 1 did not verify whether `peer-reviewed-paper-writer` under `.claude/skills/` is the same file as under `.codex/skills/`. **This is a known coverage gap.**

- **SC5.** I did not verify that `.claude/agents/argus.md` references (`references/method.md`, `references/subjectivity.md`, `references/ecosystem.md`, `references/evolution.md`, `references/composition-architecture.md`) actually exist at that relative path. Logged as R19.

- **SC6.** I did not audit `HEPHAISTOS_BUILD` or `APEX_PAPERS_COMMON` contents despite including them in scope. Counted files only (180, 46). Both directories are in scope per Q2 answer but did not surface agent surfaces in the grep pass. **If agent configs exist under `HEPHAISTOS_BUILD/EXTRACTED/` or `MASTERxMASTERxMASTER_REBUILT/`, they are not in this audit.**

- **SC7.** I did not audit `PHAROS METHOD REPOSITORY` beyond finding `agent-hephaistos/AGENTS.md`. That directory has 838 files total. Other agent-relevant configs may exist there.

- **SC8.** I did not audit `.codex/agents/` (which has 15+ gsd-*.md agents and frontmatter/toml pairs). These could be GSD-project-specific agents or additional PHAROS-relevant configs. **Explicitly out-of-scope per the operator's Q1 default** (which was "all three + PHAROS-SUITE skills"), but worth flagging that this skipped-scope may contain agent surfaces.

- **SC9.** The handoff matrix test P4/P5 (Operator → HENRY/Gadget direct) was evaluated on the presence of direct-invocation entrypoints, not by actually attempting the invocation. Pass 1 did not dry-run any invocations. The matrix is structural-claim verification, not runtime verification.

- **SC10.** I did not check whether `personal-assistant/trismegiste/` (found during scan) contains a canonical Trismégiste contract that should be promoted to `.claude/agents/trismegiste.md`. That directory was found but not read.

### 7.2 Meta-finding: the audit audited me

This conversation contains three authoritative framings for HENRY/Gadget placement:

1. **Prior-prior session** (pre-this-conversation): unknown; possibly the `.claude/agents/{henry,gadget}.md` framing ("outside the governance stack including Argus").
2. **Prior-this-session** (earlier message this conversation): "Henry and Gadget DO NOT report to Hephaistos, they follow his guidelines only. He can change what they did if QK finds governance issues in their work."
3. **Current** (this request): "HENRY and Gadget report to the Operator. At Argus level. Consult Hephaistos's guidelines as reference material, not as commands."

Framings 2 and 3 are not fully compatible. Framing 2 gives QK corrective power over HENRY/Gadget outputs; framing 3 has no QK override — just "reports to Operator." My edits earlier in the session implemented framing 2. This audit evaluates against framing 3.

**This is the kind of drift the audit is designed to catch.** The audit catches it. The audit also notes that catching it is partially an artifact of the audit's own disposition — it believes the current (newest) framing over the prior framing, without a rule for why the newer framing should win.

Recommended: operator should either (a) confirm framing 3 as authoritative and treat framing 2 as superseded, or (b) reconcile the two and tell me which language goes to disk.

---

## 8. Inventory Table (file-level, for audit reproducibility)

See `/tmp/audit-2026-04-23/hephaistos_root.tsv` (83 files), `/tmp/audit-2026-04-23/hephaistos_argus.tsv` (9 files), `/tmp/audit-2026-04-23/claude_agents.tsv` (21 files), `/tmp/audit-2026-04-23/skills_manifest.txt` (406 SKILL.md files), `/tmp/audit-2026-04-23/skills_by_name.tsv` (indexed by skill name). These are read-only artifacts produced during Phase B and are not intended for branch commit.

---

**End of audit report.**

**Status:** Pass 1 (read-only) complete. No PRs opened. No ledger patches written. Awaiting operator approval to proceed to Phase F (remediation).

## Related

- [[Research and Papers MOC]]
- [[HEPHAISTOS]]
