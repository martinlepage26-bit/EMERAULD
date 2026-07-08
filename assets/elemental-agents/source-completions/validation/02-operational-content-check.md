---
type: asset
title: Operational Content Check
aliases:
- assets/elemental-agents/source-completions/validation/02-operational-content-check
tags:
- asset
- agents
- assets
- elemental-agents
- combinations
- sample
- manifestation
- sampled
- delivery
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/elemental-agents/source-completions/validation/02-operational-content-check.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Operational Content Check

See also [[Control Protocols MOC]].
See also [[manifestation-rules]].
## Objective

Verify framework markdown contains operationally specific content rather than decorative or templated boilerplate.

## Sampling

- Random sample of 10 entries from `dual-combinations.md`.
- Random sample of 10 entries from `triple-combinations.md`.
- All four files in `validation/` and `orchestration/01-intake-and-routing.md`.

## Required content per combination entry

Every sampled entry must contain non-default text in all required fields:

- Composition (no token stutter, follows manifestation rules)
- Best use case (specific scenario, not "general product and engineering delivery")
- Risk or imbalance (specific failure mode, not a generic warning)
- Lead agent (single named role)
- Supporting agents (named, non-empty)
- Handoff or escalation (named target, not "escalate as needed")
- Autonomous automation behavior (executable trigger, not a template sentence)

Triples additionally require a unique manifestation field.

## Commands

```bash
bash combinations/validate-combinations.sh
grep -c "General product and engineering delivery" combinations/dual-combinations.md
grep -c "General product and engineering delivery" combinations/triple-combinations.md
```

## Pass criteria

- `validate-combinations.sh` exits zero.
- Boilerplate count in best-use-case fields is below the agreed threshold (default: 25 percent of sample).
- No sampled entry leaves a required field at template default.

## Failure handling

If the sample fails, escalate to Requirements Architect for content rewrite before delivery is signed off.
