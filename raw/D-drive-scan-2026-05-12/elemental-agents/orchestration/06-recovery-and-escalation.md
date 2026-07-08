---
type: raw-source
title: Recovery and Escalation
aliases:
- raw/D-drive-scan-2026-05-12/elemental-agents/orchestration/06-recovery-and-escalation
tags:
- raw
- agents
- intake
- raw-source
- d-drive-scan-2026-05-12
- correction
- recovery
- validation
- freeze
- blast
- color-lime
status: preserved
created: '2026-05-12'
updated: '2026-06-26'
vault_area: raw
canonical_path: raw/D-drive-scan-2026-05-12/elemental-agents/orchestration/06-recovery-and-escalation.md
backlink_count: 2
backlinks:
- '[[wiki/Control Protocols MOC]]'
- '[[raw/D-drive-scan-2026-05-12/elemental-agents/orchestration/03-planning-to-execution-bridge]]'
---

# Recovery and Escalation

See also [[Control Protocols MOC]].
See also [[03-planning-to-execution-bridge]].
## Goal

Recover safely when execution or validation fails.

## Triggers

- Missing requirements
- Failing validation command
- Conflicting conventions
- Security or governance risk

## Recovery steps

1. Freeze current state and capture failure evidence.
2. Classify failure severity and blast radius.
3. Apply smallest reversible correction.
4. Re-run affected validation gates.
5. Escalate when unresolved after one correction cycle.

## Exit criteria

- Failure resolved or escalated with full evidence packet.
