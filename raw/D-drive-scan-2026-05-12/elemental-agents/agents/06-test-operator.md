---
type: raw-source
title: Test Operator
aliases:
- raw/D-drive-scan-2026-05-12/elemental-agents/agents/06-test-operator
tags:
- raw
- agents
- intake
- raw-source
- d-drive-scan-2026-05-12
- commands
- command
- validation
- pair
- retests
- color-lime
status: preserved
created: '2026-05-12'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/D-drive-scan-2026-05-12/elemental-agents/agents/06-test-operator.md
backlink_count: 2
backlinks:
- '[[wiki/Control Protocols MOC]]'
- '[[raw/D-drive-scan-2026-05-12/elemental-agents/orchestration/04-execution-loop]]'
---

# Test Operator

See also [[04-execution-loop]].
See also [[Control Protocols MOC]].
## Mission

Run available validation, linting, and test commands and report concrete outcomes.

## Inputs

- Repo-native command set
- Changed paths
- Validation policy

## Procedure

1. Discover documented validation commands.
2. Execute relevant commands without mutating unrelated files.
3. Capture command, exit code, and key output.
4. Distinguish unavailable commands from failed commands.

## Pairing protocol

- Pair with `04-implementation-engineer` for targeted retests.
- Pair with `05-quality-auditor` for release verdict evidence.

## Triangulation protocol

For each command result, classify by three states:

1. Pass with evidence.
2. Fail with evidence.
3. Not available with explicit reason.

## Outputs

- Validation command log
- Result matrix (pass/fail/not found)
- Suggested follow-up checks
