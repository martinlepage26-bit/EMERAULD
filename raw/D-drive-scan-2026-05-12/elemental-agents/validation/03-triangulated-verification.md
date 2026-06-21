# Triangulated Verification

See also [[Control Protocols MOC]].
See also [[05-validation-gates]].
## Objective

Validate delivery from three independent angles.

## Angles

1. **Build angle**: structure and file-count integrity.
2. **Quality angle**: operational content usefulness.
3. **Governance angle**: assumptions, risks, and deviations are explicit.

## Procedure

1. Run structure commands from `01-structure-check.md`.
2. Run content sampling from `02-operational-content-check.md`.
3. Produce a short governance ledger:
   - assumptions made
   - deviations from request
   - residual risks

## Pass criteria

All three angles pass. If one angle fails, delivery is incomplete.
