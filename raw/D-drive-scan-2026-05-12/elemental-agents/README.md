# Elemental Agents Framework

## Purpose

Elemental Agents is an operational markdown framework for running multi-agent work with explicit routing, clear ownership, and verifiable delivery quality.

## Folder layout

- `agents/`: role contracts for 10 specialized agents.
- `orchestration/`: execution control plane from intake to recovery.
- `examples/`: runnable request patterns with expected outputs.
- `validation/`: structure checks, quality gates, and triangulated review.

## Operating flow

1. Route new work through `orchestration/01-intake-and-routing.md`.
2. Assign agent ownership using `agents/*.md` contracts.
3. Execute with `orchestration/04-execution-loop.md`.
4. Validate output with all files in `validation/`.
5. Store a completed example in `examples/` when work is reusable.

## Non-negotiable standards

- Keep claims evidence-backed.
- Separate verified facts from assumptions.
- Use recovery playbooks when a gate fails.
- Require sign-off from technical, product, and governance perspectives.

## Git hooks

When this folder is inside a Git repo, install local hooks with:

```bash
cd /mnt/d/elemental-agents
./install-hooks.sh
```

This sets `core.hooksPath=hooks` and runs combination validation on every commit.

## Related

- [[Governance and PHAROS MOC]]
- [[Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]]
