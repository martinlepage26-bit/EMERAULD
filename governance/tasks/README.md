---
type: governance-doc
title: Governed Tasks — Intake and State Machine
tags:
- governance-doc
- governed-tasks
- state-machine
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/tasks/README.md
---

# Governed Tasks — Intake and State Machine

> For future Claude: this folder is the machine-readable execution path for the HEPHAISTOS / Queen Keyport / Hermes stack (OS build Stage 4, [[governance/EMERAULD-OS-SPEC — Governance Wiring|spec]]). A governed task is one note here; its `governance_state` frontmatter gates execution. Prompt-contract roleplay without these artifacts is NOT a governed task.

## State machine

`scoped → cleared → routed → done` (terminal alternatives: `refused`, `abandoned`)

| Field | Written by | Meaning |
|---|---|---|
| `governance_state` | pipeline | Current state; `cleared` requires BOTH verdicts below |
| `hephaistos_scope` | HEPHAISTOS session/agent | `defined` once the scope packet section exists in the note |
| `qk_verdict` | Queen Keyport session/agent | `cleared` or `refused` (+ conditions in the note body) |
| `relay_id` | executing (Hermes-routed) session | RELAY-LEDGER entry id, written AT DISPATCH TIME |

## Rules

1. Execution requires `governance_state: cleared` — checked by `scripts/governance_gate.py` (soft mode warns; `--hard` refuses). Tighten to hard after the first clean month (QK-Gate pattern, piloted on pharos-suite).
2. The executing session writes the RELAY-LEDGER entry at true dispatch time, never backfilled ([[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger|why this matters]]).
3. Hephaistos/Queen Keyport disagreement → operator Branch arbitration, recorded in the task note ([[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)|worked example]]).
4. Argus audits this folder + the ledger on its existing cadence; a task at `done` without `relay_id`, or executed work with no task note, is drift.

## Related

- [[governance/EMERAULD-OS-SPEC — Governance Wiring|OS Spec — Governance Wiring]]
- [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS Build Order]]
