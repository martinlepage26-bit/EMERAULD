# Combination Validation

See also [[Control Protocols MOC]].
## Structural checks

- [x] Exactly 45 dual combinations.
- [x] Exactly 120 triple combinations.
- [x] No duplicate permutations.

## Content checks

- [x] Every combination includes Natural manifestation.
- [x] Every combination includes Operational function.
- [x] Every combination includes Autonomous automation behavior.
- [x] Risks/imbalances are documented.
- [x] Lead and supporting assignments are present.
- [x] Triple-combination manifestation labels are unique.
- [x] Manifestation labels avoid repeated token stutter.

## Escalation checks

- [x] Spirit, Chi, and Akasha are treated as escalation modifiers, not routine peers.
- [x] Akasha appears as source-field modifier, not default name filler.

## Validation run

- Date: 2026-05-12
- Result: pass
- Evidence: `validate-combinations.sh` confirms counts, field coverage, uniqueness, escalation lead rules, and Akasha naming constraints.

## Command checks

```bash
cd /mnt/d/elemental-agents/combinations
./validate-combinations.sh
```
