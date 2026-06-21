# Execution Loop

See also [[06-test-operator]].
## Goal

Drive implementation in short, verifiable cycles.

## Loop

1. Execute the next change slice.
2. Run immediate checks for that slice.
3. Record evidence and outcomes.
4. Resolve defects before next slice.

## Rules

- Do not batch unrelated changes.
- Do not proceed with unresolved critical defects.
- Keep command and file logs current.
