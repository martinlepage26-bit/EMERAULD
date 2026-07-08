---
type: governance-update
title: HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)
aliases:
- HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)
- wiki/HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)
tags:
- governance-update
- wiki
- hephaistos-co-equal-authority-cleanup-wave-1-and-2-2026-04-18-md
- tier
- equal
- forging
- scope
- wave
- color-purple
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18).md
backlink_count: 24
backlinks:
- '[[wiki/AI Identity and Phenomenology]]'
- '[[wiki/Agatha Unified Skill System — Eight Sovereign Operators]]'
- '[[wiki/Agent Session Phenomenology]]'
- '[[wiki/Architecture Translation Guide — Eight Operators to Three-Agent Stack]]'
- '[[wiki/Archive Rebuild Normalized Tracker — MASTER PACK and HEPHAISTOS]]'
- '[[wiki/Claude Code Skill Corpus]]'
- '[[wiki/Desktop Text Intake — 2026-05-06]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[wiki/Hermes Dashboard — Professional Governance Tool]]'
- '[[wiki/InfraFabric MCP Stack — Remote Bundles]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[wiki/Operator-Check Skill — Burnout Cascade Interrupt]]'
- '[[wiki/PHAROS Strategic Analysis — Keep Stop Fix Finish (2026-04-18)]]'
- '[[wiki/PROTOCOLS — Debate and Red-Team Runbook]]'
- '[[wiki/Paper 25 — Pre-Draft Artifacts (Pharos Frame Capstone)]]'
- '[[wiki/ROOK — Session Boundary Model]]'
- '[[wiki/Right-Arm Extension Decision — Hephaistos and Hermes Advisory Consultation
  (2026-04-18)]]'
- '[[wiki/Supersession Registry]]'
- '[[wiki/Trismégiste — Personal AI Assistant]]'
- '[[wiki/claude-peers-mcp — Claude Peer Network]]'
- '[[hephaistos/agents/Trismegiste Personal AI Assistant]]'
- '[[memory/agents/Blockers]]'
- '[[memory/agents/Decisions]]'
---

# HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)

## Summary

A two-wave surgical cleanup of the [[Governance and PHAROS MOC|HEPHAISTOS]] governance spec files to enforce the co-equal authority model committed in [[Governance and PHAROS MOC|CO-EQUAL-AUTHORITY-DECISION.md]]. Prior to this session, residual tier-hierarchy language persisted across `CO-EQUAL-AUTHORITY-DECISION.md`, `SKILL-MAP.md`, and `WAVE2-CLEANUP.md` — language that directly contradicted the flat co-equal architecture the spec files claimed to establish. All Wave 1 and Wave 2 items are now resolved. A same-day follow-on registry normalization also closed the later `SKILL-MAP.md` cleanup thread: the active registry now aligns across `SKILL-MAP.md` and `DEPLOYMENT-CHECKLIST.md` at 35 active skills, 9 routing stubs, and 1 retired skill. The follow-up also added `hq-disagreement-test-case.md`, which exercises the [[Governance and PHAROS MOC|Hephaistos / Queen Keyport]] arbitration path before Hermes routing.

The co-equal Hephaistos/Queen Keyport pairing is structurally derived from the dual-arm authority pattern named in [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone|the keystone]]: forging (Ptah/Hephaistos slot) and judging (the Council that judges Thomas's *procès*, [[Mort et Naissance et L'Ombre et le Double — MA Thesis on Yvon Rivard (Université Laval, 2010)|MA pp. 17–19]]) operate as functionally distinct authorities within a single architecture. Neither can substitute for the other; this is why co-equal arbitration is structurally necessary, not procedural.

## Context

The [[Governance and PHAROS MOC|HEPHAISTOS]] three-agent stack — Hephaistos (forging), [[Governance and PHAROS MOC|Queen Keyport]] (governance), Hermes (routing) — was declared co-equal in April 2026 via `CO-EQUAL-AUTHORITY-DECISION.md`. That decision superseded the earlier Tier 0 / Tier 1 / Tier 2 hierarchy framing. However, the tier vocabulary had not been fully purged from `SKILL-MAP.md`, and two Hermes references in `CO-EQUAL-AUTHORITY-DECISION.md` itself still used "Tier 2" language — contradicting the spec's own framing. This session completed the decommissioning.

The right-arm ownership drift was a separate error: `SKILL-MAP.md` had assigned philosopher and fully-rounded-power-analyst as right-arms of "Agent HEPHAISTOS" when the correct owner is [[Governance and PHAROS MOC|Queen Keyport]]. That mattered architecturally: right-arms provide governance input, not forging input. Misattributing them to Hephaistos would imply the forging agent receives conceptual and structural governance vetting — inverting the co-equal model.

## Details

### CO-EQUAL-AUTHORITY-DECISION.md — 2 edits

The spec itself contained two residual "Tier 2" references for Hermes:

| Location | Old | New |
|---|---|---|
| "Relationship to Hermes" section | `Hermes (Tier 2, routing) remains downstream...` | `Hermes (scope: routing) remains downstream...` |
| "What this does not change" section | `Hermes remains Tier 2 (routing, monitoring, escalation).` | `Hermes remains the routing authority (routing, monitoring, escalation).` |

---

### SKILL-MAP.md — Wave 2 HIGH priority: 4 architectural contradiction fixes

These four items directly contradicted the co-equal model at the preamble and summary level — they implied forging feeds governance and governance outranks right-arms.

| Location | Problem | Fix |
|---|---|---|
| Tier 0 preamble | "Forging is primary upstream of governance. It feeds into the governance decision..." | "Forging and governance are co-equal authorities operating in separate scopes. Neither is upstream of the other." |
| Tier 1 preamble | "It receives scope from Forging (Tier 0)..." | Full rewrite: QK holds governance in its own scope, co-equal with Hephaistos's forging authority; synthesizes right-arm input within governance scope; conflicts with forging go to operator. |
| Tier 2 preamble | "When philosopher and power-analyst disagree, governance (Tier 1) has final word." | "When philosopher and power-analyst disagree, Queen Keyport synthesizes both inputs. The operator arbitrates higher-level conflicts between authorities." |
| Overlap Summary table | "Governance arbitrates disagreements." | "Operator arbitrates disagreements." |

---

### SKILL-MAP.md — right-arm ownership: 3 edits

Three instances in the Tier 2 section assigned philosopher and fully-rounded-power-analyst as right-arms of "Agent HEPHAISTOS." All replaced with "Queen Keyport":

- Section preamble: "equal right-arms of Agent HEPHAISTOS"
- philosopher Function entry: "First right-arm to Agent HEPHAISTOS"
- fully-rounded-power-analyst Function entry: "Second right-arm to Agent HEPHAISTOS"

---

### SKILL-MAP.md — tier label decommissioning: 13 edits

All "Authority Tier N" naming replaced with scope-based labels per the ORCHESTRATION_OPERATIONS.md convention:

**Section headers (7):**

| Old | New |
|---|---|
| `## Authority Tier 0 — Forging Skills` | `## Forging Skills (scope: forging)` |
| `## Authority Tier 1 — Governance-Critical Skills` | `## Governance Skills (scope: governance)` |
| `## Authority Tier 2 — Right-Arm Skills (Co-Equal)` | `## Right-Arm Skills (scope: governance)` |
| `## Authority Tier 3 — Research and Methodological Skills` | `## Research and Methodological Skills (scope: research)` |
| `## Authority Tier 4 — Writing, Publishing, and Output Skills` | `## Writing, Publishing, and Output Skills (scope: output)` |
| `## Authority Tier 5 — Meta and Composition Skills` | `## Meta and Composition Skills` *(no scope label — cross-cutting)* |
| `## Authority Tier 6 — Hermes Connector Skills` | `## Routing Connector Skills (scope: routing)` |

**Tracking labels (5):** All converted to `scope: X` pattern. `free-tool-strategy` received `scope: routing` (matching its function description "routed to Hermes") despite being placed under the Meta section — placement discrepancy logged for Wave 3.

**Body cross-reference (1):** `humanize` duplicate note under Writing skills: "See Tier 1" → "See Governance skills."

---

### WAVE2-CLEANUP.md — updated

All original 17 Wave 2 items marked complete. Four Wave 3 candidates logged:

1. `agent-development` pairings: `(Tier 3)` inline reference
2. `lead-research-assistant` pairings: `(Tier 3, method selection)` and `(Tier 3, background work)` (2 instances)
3. Skills Not In Corpus block: `registered as Tier 2 right-arm` → `right-arm to Queen Keyport`
4. `free-tool-strategy` body placement discrepancy: placed under Meta but functions as routing

---

### Follow-on registry normalization — same-day closure

The later cleanup thread on `SKILL-MAP.md` was resolved in a follow-on subsumption pass:

- `architecture` absorbed `research-engineer` scope and trigger conditions
- `senior-data-scientist` became the single quantitative entry point, absorbing `exploratory-data-analysis` and `statistical-analysis`
- `lead-research-assistant`, `deep-research-notebooklm`, `literature-review`, `peer-review`, `scholar-evaluation`, and `scientific-critical-thinking` were converted from active entries into routing stubs
- `DEPLOYMENT-CHECKLIST.md` was brought into alignment with `SKILL-MAP.md`

Resulting registry state:

- 35 active skills
- 9 routing stubs retained on disk but not as standalone invocation targets
- 1 retired skill (`ma-degree-guide`)

### Wave 1 handoff follow-up — same-day closure

The remaining Wave 1 spec requirement was also closed. The three active handoff files and their mirrored `templates/` copies now use scope/co-equal framing instead of Tier 0 / Tier 1 / Tier 2 language. Unresolved veto language now routes to scope redesign, co-equal conflict recording, or operator arbitration rather than a default HEPHAISTOS override.

The test case at `hephaistos/hq-disagreement-test-case.md` confirms the arbitration path: [[Governance and PHAROS MOC|Hephaistos]] may declare an artifact ready in its forging scope, [[Governance and PHAROS MOC|Queen Keyport]] may block publication in governance scope, Hermes refuses to route during the unresolved conflict, and work resumes only after the operator's resolution is recorded.

## Key Ideas

- The co-equal model is not just a hierarchy flattening — it is a structural claim that governance constraints must be present at the moment scope is defined, not applied afterward. The old tier vocabulary implied forging defined scope first and governance reviewed it second. That sequence is wrong by design.
- Right-arm ownership matters architecturally. Philosopher and Power-Analyst provide input to governance decisions, not to scope/forging decisions. Assigning them to Hephaistos would have allowed forging to claim conceptual and structural vetting that belongs to Queen Keyport.
- "Governance has final word" over right-arm disagreements was wrong in two ways: it used tier language, and it overstated governance's role. Queen Keyport *synthesizes* right-arm input — it does not override or dismiss it. The operator arbitrates at the higher conflict level (Hephaistos vs. Queen Keyport).
- Tier labels were a naming artifact from the pre-co-equal architecture. Replacing them with scope labels (`scope: forging`, `scope: governance`, `scope: routing`) makes the authority model legible in the file itself without requiring knowledge of the tier numbering system.

## Open Questions

- Historical note: the Wave 3 items logged above were later closed by the same-day registry normalization pass.
- `free-tool-strategy` placement remains an interpretive design question: should it live structurally under Routing Connector, or remain cross-cutting with routing behavior documented in place?
- Is there a case for a formal `scope: meta` label for the Meta and Composition section, or does the absence of a scope label correctly reflect that these skills are cross-cutting?

## Sources

- `/home/cerebrhoe/hephaistos/CO-EQUAL-AUTHORITY-DECISION.md`
- `/home/cerebrhoe/hephaistos/SKILL-MAP.md`
- `/home/cerebrhoe/hephaistos/WAVE2-CLEANUP.md`
- `/home/cerebrhoe/hephaistos/hq-disagreement-test-case.md`
- Related: [[Governance and PHAROS MOC]]
- Related: [[Agent Session Phenomenology]]
- Related: [[Claude Code Skill Corpus]]
