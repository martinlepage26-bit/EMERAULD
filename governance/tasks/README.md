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
| `{field}_stamp` / `{field}_stamped_at` / `{field}_section_sha` | `scripts/gate_stamp.py` only | HMAC-SHA256 stage stamp binding the field value + its section text, chained to the prior stage (task #3). Never hand-written; `stamped_at` always quoted |
| `stamp_key_id` | `scripts/gate_stamp.py` | First 8 hex chars of the stamping key's hash (rotation legibility) |
| `stamp_status` | executor, once | `grandfathered` = note predates the stamp mechanism (tasks #1-#2); visibly labeled, never silently passed |

## Rules

1. Execution requires `governance_state: cleared` — checked by `scripts/governance_gate.py` (soft mode warns; `--hard` refuses; invoked nightly via `--audit-all` since task #2). Tighten to hard after the first clean month (QK-Gate pattern, piloted on pharos-suite).
1b. Stage transitions are stamped with `scripts/gate_stamp.py` (task #3): HMAC over the stage's section text, chained in order — stamp after writing your section, and know the boundary: stamps are tamper-EVIDENCE against non-key-hunting drift (the RELAY-20260703-014 class), not proof of dispatch isolation. Full honesty section: [[governance/tasks/gate-authenticity-20260708|task #3 scope packet]].
2. The executing session writes the RELAY-LEDGER entry at true dispatch time, never backfilled ([[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger|why this matters]]).
3. Hephaistos/Queen Keyport disagreement → operator Branch arbitration, recorded in the task note ([[Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)|worked example]]).
4. Argus audits this folder + the ledger on its existing cadence; a task at `done` without `relay_id`, or executed work with no task note, is drift.

## Related

- [[governance/EMERAULD-OS-SPEC — Governance Wiring|OS Spec — Governance Wiring]]
- [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS Build Order]]
