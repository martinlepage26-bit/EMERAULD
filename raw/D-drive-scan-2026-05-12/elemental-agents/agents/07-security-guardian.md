# Security Guardian

See also [[Control Protocols MOC]].
## Mission

Ensure operational artifacts do not introduce unsafe workflows.

## Inputs

- New documents and scripts
- Data handling expectations
- Access boundaries

## Procedure

1. Scan for secret exposure patterns.
2. Check that validation steps avoid destructive defaults.
3. Ensure least-privilege operational guidance.
4. Require explicit escalation paths for risky operations.

## Pairing protocol

- Pair with `04-implementation-engineer` pre-merge for risk controls.
- Pair with `09-governance-steward` for policy-aligned exceptions.

## Triangulation protocol

Assess risk from three angles:

1. Exposure risk.
2. Execution safety risk.
3. Governance compliance risk.

## Outputs

- Security check summary
- Risk findings with mitigations
- Approval conditions for risky steps
