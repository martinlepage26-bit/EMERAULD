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
