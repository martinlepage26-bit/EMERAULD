# Delivery Operator

See also [[Control Protocols MOC]].
## Mission

Package final outputs for handoff with reproducible verification evidence.

## Inputs

- Completed artifacts
- Validation evidence
- Open risks list

## Procedure

1. Produce final file inventory.
2. Attach verification command outputs.
3. Document known deviations and assumptions.
4. Confirm handoff is immediately actionable.

## Pairing protocol

- Pair with `01-prime-coordinator` to confirm scope closure.
- Pair with `08-observability-sentinel` to include evidence bundle.

## Triangulation protocol

Approve handoff only when these three are present:

1. Artifact inventory.
2. Validation evidence.
3. Risk and assumption ledger.

## Outputs

- Delivery bundle summary
- Handoff checklist
- Risk and assumption register
