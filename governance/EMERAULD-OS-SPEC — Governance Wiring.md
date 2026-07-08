---
type: governance-doc
title: EMERAULD-OS-SPEC — Governance Wiring
tags:
- governance-doc
- emerauld-os
- spec
- governance-wiring
- governance
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/EMERAULD-OS-SPEC — Governance Wiring.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[EMERAULD_OS_ARCHITECTURE]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[governance/EMERAULD-OS-BUILD-ORDER]]'
---

# OS Spec — Wiring the Governance Stack to Execution (gap 3)

> [!success] Executed 2026-07-08 (operator directive)
> The minimal viable wiring is live and the exit criterion is met by a real task: [[governance/tasks/weekly-os-health-20260708|weekly-os-health-20260708]] flowed intake → HEPHAISTOS scope packet (written by the hephaistos agent) → Queen Keyport clearance (written by the queen-keyport agent: cleared with 8 binding conditions, including an empirically-refuted bash idiom in the scope itself — the co-equal review caught a real bug) → hard gate PASS (`scripts/governance_gate.py`, soft by default / `--hard` available) → routed execution with `RELAY-20260708-002` written at true dispatch time. State machine + rules: [[governance/tasks/README|governance/tasks/README]]. The task rests at `routed` until QK condition 8's live-run evidence lands (first Friday weekly run) — the pipeline's first act was to refuse premature closure, which is the point.

> For future Claude: HEPHAISTOS / Queen Keyport / Hermes / Argus are today prompt contracts — .md files an agent roleplays — with no code path that actually routes a task through clearance before execution. The council's own review ([[Areas/PHAROS/multi-agent-orchestration Skill — Governance Case File|governance case file]]) called this an unimplemented composite pattern. Build in Stage 4 of [[governance/EMERAULD-OS-BUILD-ORDER|the build order]].

## Minimal viable wiring (recommended over a LangGraph build)

Use artifacts, not frameworks. The stack becomes real when its decisions are machine-readable files that gate execution:

1. **Task intake** — a governed task = a note in `governance/tasks/` with frontmatter `governance_state: scoped | cleared | routed | done | refused`. Hephaistos-scope sessions produce the scope packet (pattern already exists: the 2026-07-03 scope packets in Areas/PHAROS/).
2. **Clearance** — Queen Keyport clearance appends `qk_verdict: cleared|refused` + conditions to the same note. Both verdicts required before `governance_state: cleared`. The clearday co-equal conflict record ([[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)|worked example]]) shows the arbitration path when they disagree: operator Branch decision, recorded.
3. **Routing** — Hermes execution requires `governance_state: cleared`; the executing session writes the RELAY-LEDGER entry at dispatch time (not backfilled — the ledger's own header documents why that matters).
4. **Enforcement point** — the QK-Gate pattern already piloted on pharos-suite (soft pre-push governance gate) is the model: a check script that refuses execution when the task note isn't `cleared`. Start soft (warn), tighten to hard after the first clean month.
5. **Audit** — Argus reads `governance/tasks/` + RELAY-LEDGER on its existing cadence; drift = tasks executed without clearance artifacts.

## Exit criterion

One real task flows intake → dual clearance → routed execution → ledger entry, all artifacts written by the pipeline at true dispatch time.

## Related

- [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS Build Order]]
- [[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger]]
- [[Areas/PHAROS/HEPHAISTOS Agent Architecture]]
