---
type: wiki
aliases: [ROOK, session harness, execution boundary]
tags: [infrastructure, agents, hephaistos, session-management]
status: active
created: 2026-04-18
updated: 2026-04-18
---

# ROOK — Session Boundary Model

## Summary

ROOK is the infrastructure harness and execution boundary model for the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|HEPHAISTOS three-agent architecture]]. It provides session lifecycle management, tool availability enforcement, communication rooms for agent coordination, and headroom-based pause triggers. Source: `/home/cerebrhoe/ROOK.md`.

## Context

ROOK sits beneath the [[Agent Session Phenomenology|governance layer]]: HEPHAISTOS forges artifacts within Rook's tool boundaries, [[Recursive Governance Protocol — Theseus, Auryn, Hopf|Queen Keyport]] governs decisions within those constraints, and Hermes routes using Rook's communication channels. ROOK does not own governance — it enforces the operational envelope that governance runs inside. It is the part of the [[InfraFabric Architecture]] that Claude Code sessions directly interact with.

## Details

### Live infrastructure

- Platform: `https://infrafabric.io/chat`
- Session config: `/home/cerebrhoe/.codex/harnesses/martin-infrafabric/rook_session.env`
- Primary room: `martin-room`
- Debug room: `martin-room-debug`
- Noise mode: `balanced`

### What ROOK provides

- Session boundary and execution constraint model
- Communication rooms for agent coordination (no direct agent-to-agent coupling)
- Tool availability and permission enforcement
- Headroom tracking (pause threshold: **5%**)
- Human-in-the-loop surface (Martin has visibility into both rooms)

### What ROOK does NOT own

- Governance decisions → Queen Keyport
- Task definition / artifact design → HEPHAISTOS
- Routing logic → Hermes
- Orchestration sequencing → ORCHESTRATION

### Session lifecycle

1. Load control files (AGENTS.md, HEPHAISTOS.md, QUEEN-KEYPORT.md, HERMES.md, ORCHESTRATION.md, ROOK.md)
2. Establish headroom baseline (100%)
3. Route work through the three-agent stack
4. Track headroom decay
5. Pause at 5% threshold; emit continuity prompt
6. Martin reviews and approves/redirects
7. Close with tracker entry

### Tool tiers

| Tier | Tools |
|---|---|
| Guaranteed | Read, Glob, Grep, Edit, Write, Bash (allowed paths) |
| Controlled | Agent dispatch, Skill invocation, permission-scoped tools |
| Restricted | Infrastructure mutation (Proxmox, 10.10.10.170, secret rotation) |
| Escalation | Tools requiring Queen Keyport approval |

### Room coordination model

| Room | Purpose | Occupants |
|---|---|---|
| `martin-room` | Primary workspace | HEPHAISTOS, Queen Keyport, Hermes, Martin |
| `martin-room-debug` | Debug/exploration | HEPHAISTOS, debug instances |

Communication flows: HEPHAISTOS → QK (proposal) → Hermes (approval/refusal) → HEPHAISTOS (status). All visible to Martin.

### Authority rule

If Rook's operational constraint conflicts with an agent decision, **the operational constraint wins**. Safety > governance.

## Key Ideas

- Headroom management prevents truncated decisions and context overflow
- Room model maintains agent autonomy without tight coupling
- Tool restrictions are non-negotiable by governance decisions
- Session closure requires: tracker updated, open work identified, Martin has full context

## Sources

- `/home/cerebrhoe/ROOK.md`

## Related

- [[Agent Session Phenomenology]]
- [[InfraFabric Architecture]]
- [[Agatha Unified Skill System — Eight Sovereign Operators]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
