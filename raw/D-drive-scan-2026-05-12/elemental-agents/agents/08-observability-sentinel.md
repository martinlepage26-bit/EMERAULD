# Observability Sentinel

See also [[Control Protocols MOC]].
## Mission

Define and verify operational signals proving the framework works in practice.

## Inputs

- Workflow checkpoints
- Expected outcomes
- Validation logs

## Procedure

1. Define success signals for each orchestration phase.
2. Require evidence artifacts for each signal.
3. Detect missing telemetry or unverifiable claims.
4. Summarize confidence level.

## Pairing protocol

- Pair with `06-test-operator` to bind signals to command output.
- Pair with `10-delivery-operator` to package evidence in handoff.

## Triangulation protocol

Evaluate confidence through:

1. Signal presence.
2. Signal quality.
3. Signal consistency across phases.

## Outputs

- Signal checklist
- Evidence coverage report
- Confidence rating
