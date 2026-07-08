---
type: wiki
title: Skill Domain — Agent Architecture
aliases:
- Agent Architecture domain
- Agent development domain
- Multi-agent skills hub
tags:
- skills
- domain
- hub
- agent-architecture
- multi-agent
- autonomous
- hitl
- orchestration
- wiki
- agent
- skill
- designs
status: active
created: '2026-05-07'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Skill Domain — Agent Architecture.md
backlink_count: 11
backlinks:
- '[[Areas/PHAROS/Control Protocols MOC]]'
- '[[Areas/PHAROS/GSD Tier 1 — Core Workflow Skills Hub]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/Skill Domain — Design and UX]]'
- '[[wiki/Skill Domain — Security and Compliance]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# Skill Domain — Agent Architecture

See also [[Control Protocols MOC]].
## Summary

The Agent Architecture domain contains the skills for designing, building, coordinating, and monitoring AI agent systems: autonomous agents, HITL oversight, parallel dispatch, self-healing agents, memory systems, and the Claudex coordination protocol. This domain sits at the intersection of [[Skill Domain — Governance and Method]] (agent governance, HITL policy) and [[Skill Domain — Skill Architecture]] (agent-as-skill composition). The Hephaistos/Queen Keyport/Hermes three-agent stack described in the [[Agatha Unified Skill System — Eight Sovereign Operators]] is the architectural reference for all agent design work here. All agent architecture skills belong to the broader [[Skill Ecosystem — Professional Capability Registry]].

Peer domains: [[Skill Domain — Security and Compliance]] (threat models, adversarial testing, refusal conditions) and [[Skill Domain — Design and UX]] (the interaction layer where agent tooling becomes usable by real operators).
Security, privacy, and adversarial testing inputs route through [[Skill Domain — Security and Compliance]].

## Agent Attribution

| Agent | Role |
|---|---|
| Hephaistos | Agent scope and design, skill composition, artifact shaping for agent systems |
| Hermes | Routing, integration, monitoring, and escalation for deployed agent systems |
| Codex | Agent build, deployment, memory wiring, tool integration |

## Full Skill Roster

All agent architecture and development skills in this domain.

- [[agent-creator]] — creates and initializes new agent configurations and entrypoints
- [[agent-manager-skill]] — manages running agents: status, handoff, pause, resume, and shutdown
- [[agent-memory-mcp]] — MCP-based agent memory integration: read, write, search, and persist context (cross-listed with Vault)
- [[agent-memory-systems]] — designs and audits agent memory architectures for persistence and recall (cross-listed with Vault)
- [[agent-tool-builder]] — builds and packages tools for agent consumption via MCP or function calling
- [[autonomous-agents]] — designs and evaluates fully autonomous agent pipelines with appropriate oversight
- [[claudex]] — Claude/Codex coordination protocol; inter-agent task passing and session handoff
- [[codex]] — Codex agent operations: invocation, context passing, skill dispatch, and output handling
- [[delegate-task]] — structured task delegation from Claude to Codex with scoped context (cross-listed with Skill Architecture)
- [[dispatching-parallel-agents]] — orchestrates parallel agent dispatch for independent reasoning lanes
- [[helix-operator]] — HELIX desktop protocol: operator-level agent lifecycle and session management
- [[hitl-awareness]] — designs and reviews human-in-the-loop oversight, verification, and escalation (cross-listed with Governance)
- [[self-healing]] — designs agents and systems that detect, diagnose, and recover from failures autonomously

## Applied Context

- [[AI Agent Operations Manager — Credential Path and Portfolio]] — Career-track synthesis for the operations management layer of agent systems: ranked credential path (OpenAI Agents, Anthropic Academy, IBM RAG/Agentic), five portfolio artifacts, and a 60-day governance-review-agent build plan that exercises every skill in this domain.

## Canonical References

- [[Martin Lepage — Authored Skills]]
- [[Skill Ecosystem — Professional Capability Registry]]
- [[Skill Corpus — Complete Live Index (260 Active Skills)]]
- [[Agatha Unified Skill System — Eight Sovereign Operators]]
- [[Agent Ecosystem Audit — 2026-04-23]]
