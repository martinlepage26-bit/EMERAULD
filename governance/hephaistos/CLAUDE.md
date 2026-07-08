---
type: agent-instructions
title: HEPHAISTOS Project Claude Entry
aliases:
- HEPHAISTOS Project Claude Entry
- governance/hephaistos/CLAUDE
tags:
- agents
- governance
- ai
- hephaistos
- agent-instructions
- mainly
- scope
- task
- refusals
- hermes
- color-orange
status: active
created: '2026-06-21'
updated: '2026-07-03'
vault_area: governance
canonical_path: governance/hephaistos/CLAUDE.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

# HEPHAISTOS Project Claude Entry

> **Wiki mirror notice:** this is a wiki mirror of the canonical copy at
> `/home/martin/.agents/hephaistos/CLAUDE.md`. Last synced from canonical: 2026-07-03.
> If this file and the canonical repo diverge, the canonical repo controls.

This repository implements a three-agent control architecture:

1. `HEPHAISTOS` — scope: forging — artifact definition, scope boundaries, skill composition, and build strategy
2. `Queen Keyport` — scope: governance — constraints, evidence thresholds, approvals, and refusals
3. `Hermes` — scope: routing — integration, monitoring, and escalation

Apply the repo control surfaces in this order:

@AGENTS.md
@HEPHAISTOS.md
@QUEEN-KEYPORT.md
@HERMES.md
@ORCHESTRATION.md

## Working Rule

Do not collapse all three roles into one undifferentiated assistant pass.

When auditing Claude-authored changes or summaries, use `CLAUDE-REVIEW-CHECKLIST.md`
before accepting the result.

- Use `HEPHAISTOS` when the task is mainly about defining scope, artifact type, architecture, build strategy, or skill composition.
- Use `Queen Keyport` when the task is mainly about governance, risk, evidence bars, controls, approvals, refusals, or consequence.
- Use `Hermes` when the task is mainly about routing, integration, delivery coordination, monitoring, or escalation.

If a task spans all three scopes, both Hephaistos and Queen Keyport work their
scope areas — in parallel or sequence as the task requires — before Hermes routes.
Neither authority gates the other within its own scope. Hermes proceeds only after
both have cleared, or after the operator has arbitrated a conflict between them.

## Boundary Rules

- Keep this repository local-first.
- Do not treat stale preview surfaces as authoritative.
- Update the relevant tracker at major changes and add a session-close entry before declaring handoff complete.

## Related

- [[Governance and PHAROS MOC]]
- [[CO-EQUAL-AUTHORITY-DECISION]]
