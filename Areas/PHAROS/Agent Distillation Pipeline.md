---
type: wiki
title: Agent Distillation Pipeline
aliases:
- distillation
- agent distillation
- student models
tags:
- infrastructure
- ai
- distillation
- agents
- ml
- areas
- runner
- configs
- host
- wiki
- pharos
status: active
domain: pharos
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Agent Distillation Pipeline.md
backlink_count: 7
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Host Environment — pharos-corpus-runner-01]]'
- '[[Areas/PHAROS/ai-agent-board — Third-Party Tool Evaluation]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# Agent Distillation Pipeline

## Summary

A config-driven ML pipeline for distilling 32 AI agents into smaller, faster student models while preserving each agent's domain expertise, style, constraints, and safety behavior. Located at `~/distillation/`. Discovered 20 core Claude Code agents (`~/.claude/agents/`) and 12 personal assistant agents (`~/EMERAULD/personal-assistant-agents/`). Connected to [[Host Environment — pharos-corpus-runner-01]] as a server-side ML project and to the agent stack documented in [[Host Environment — pharos-corpus-runner-01]].

## Context

Production-oriented pipeline with teacher-student architecture. Each agent gets a distillation strategy based on its domain and behavior profile. The goal is deployable specialist models that don't require full frontier-model inference for every operator task.

## Structure

| Path | Purpose |
|---|---|
| `~/distillation/configs/` | Per-agent distillation configs |
| `~/distillation/datasets/` | Training datasets per agent |
| `~/distillation/teacher/` | Teacher model outputs |
| `~/distillation/eval/` | Evaluation results |
| `~/distillation/scripts/` | Pipeline automation |
| `~/distillation/inventory/` | Agent discovery (agents.json, agents_report.md) |
| `~/distillation/reports/` | Distillation run reports |

## Agent Inventory

- **32 agents total** — 20 core Claude Code + 12 personal assistant agents
- Inventory at `~/distillation/inventory/agents.json`

## Related

- [[Host Environment — pharos-corpus-runner-01]]
- [[Personal and Projects MOC]]
