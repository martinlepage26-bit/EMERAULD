# Example: Incident Response

See also [[Control Protocols MOC]].
## Input

"Production validation failed after a deploy."

## Route

- Prime Coordinator
- Recovery and Escalation orchestration
- Observability Sentinel

## Execution summary

1. Capture failing command and impact.
2. Apply minimal rollback or hotfix.
3. Re-run critical gates.
4. Publish incident summary.

## Expected output

- Incident timeline
- Corrective action log
- Final service status
