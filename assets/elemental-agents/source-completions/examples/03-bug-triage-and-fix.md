---
type: asset
title: 'Example: Bug Triage and Fix'
tags:
- asset
- agents
- assets
- elemental-agents
- regression
- recipe
- intermittent
- localize
- checkout
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/elemental-agents/source-completions/examples/03-bug-triage-and-fix.md
backlink_count: 1
backlinks:
- '[[wiki/ASSETS MOC]]'
---

# Example: Bug Triage and Fix

See also [[Control Protocols MOC]].
## Input

"Users report intermittent 500 errors on the checkout endpoint."

## Route

- Context Cartographer
- Requirements Architect
- Implementation Engineer
- Test Operator

## Execution summary

1. Reproduce the failure and capture minimal trigger conditions.
2. Localize the defect to a specific path and commit range.
3. Apply the smallest correct fix with no unrelated edits.
4. Re-run the affected tests plus one regression sweep.

## Expected output

- Reproduction recipe
- Root-cause statement with file and line evidence
- Patch with change-to-requirement mapping
- Validation log including regression coverage
