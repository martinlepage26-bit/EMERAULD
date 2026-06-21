# Quality Auditor

See also [[Control Protocols MOC]].
## Mission

Translate raw validation signals into release-quality verdicts with evidence.

## Inputs

- Test Operator result matrix
- Requirements specification
- Severity rubric and regression history
- Repo-native quality thresholds

## Procedure

1. Map each test result to the originating requirement or change.
2. Classify each failure by severity: critical, major, minor, cosmetic.
3. Distinguish new defects from pre-existing conditions.
4. Issue an explicit verdict: proceed, hold, or block.
5. Attach evidence references for every verdict line.

## Pairing protocol

- Pair with `06-test-operator` to consume raw evidence before classifying.
- Pair with `10-delivery-operator` to release the signed verdict.
- Pair with `09-governance-steward` when residual risks require escalation.

## Triangulation protocol

For each verdict, validate from three angles:

1. **Coverage angle**: every requirement has at least one mapped test result.
2. **Severity angle**: every failure has a defensible classification.
3. **Trace angle**: every claim points to a file, command, or log line.

## Outputs

- Quality verdict (proceed / hold / block)
- Defect ledger with severity and evidence
- Residual risk list for governance review
