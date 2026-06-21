---
type: wiki
aliases: [MCP stack, remote-bundles, if_context, if_blackboard, openspace, if_chat, InfraFabric MCP]
tags: [infrastructure, mcp, infrafabric, tooling, remote]
status: active
created: 2026-04-18
updated: 2026-04-18
---

# InfraFabric MCP Stack — Remote Bundles

## Summary

The InfraFabric MCP stack is a set of four MCP servers registered in `~/.mcp.json` that connect Claude Code sessions on Martin's machine to [[InfraFabric Architecture|InfraFabric]] services running on `infrafabric.io`. The bundle files live at `/home/cerebrhoe/remote-bundles/martin_lepage_codex_remote_bundle_20260317T022437Z/`. Two servers (if_context, if_blackboard) tunnel through SSH to a Proxmox container; two (openspace, if_chat) run locally.

## Context

This is the local side of the [[ROOK — Session Boundary Model|ROOK infrastructure harness]]. The `if_chat` server provides the room-based communication model (martin-room / martin-room-debug) that ROOK uses for agent coordination. The `if_context` server provides context storage for the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|HEPHAISTOS governance stack]]. The `openspace` server bridges Claude Code's skill directory (`~/.codex/skills`) with the OpenSpace workspace. See also [[claude-peers-mcp — Claude Peer Network]] for the local peer-to-peer layer.

Cluster routing note: [[MCP and Runtime Integration MOC]].

## Details

### Bundle location

`/home/cerebrhoe/remote-bundles/martin_lepage_codex_remote_bundle_20260317T022437Z/`

### Four MCP servers

#### 1. if_context (remote via SSH)

- Transport: Node script + SSH tunnel → Proxmox container 270
- Purpose: Context storage and policy for HEPHAISTOS sessions
- Remote target: `root@infrafabric.io` via `/home/cerebrhoe/.ssh/infrafabric_martin_lepage_ed25519`
- Remote command: `pct exec 270 -- /usr/bin/env IF_CONTEXT_MCP_CLAUDE_COMPAT=1 ... if-context-mcp-server.mjs`
- API base: `http://127.0.0.1:18881`

#### 2. if_blackboard (remote via SSH)

- Transport: Node script + SSH tunnel → Proxmox container 270
- Purpose: Shared blackboard for inter-agent state
- Remote target: `root@infrafabric.io` (same SSH identity)
- Remote command: `pct exec 270 -- /usr/bin/node ... if-blackboard-mcp-server.mjs`

#### 3. openspace (local)

- Transport: Local Python venv (`/home/cerebrhoe/.venvs/openspace/bin/openspace-mcp`)
- Purpose: Bridges Claude Code skill directories with OpenSpace workspace
- Skill dirs: `/home/cerebrhoe/.codex/skills`
- OpenSpace workspace: `/mnt/c/Users/softinfo/Documents/GitHub/OpenSpace-main`
- Timeout: 600s

#### 4. if_chat (local script + remote bridge)

- Transport: Local Python script + JS bridge → `https://infrafabric.io/chat`
- Purpose: Room-based communication (the ROOK communication surface)
- Default room: `main-room`
- Debug room: `main-room-debug`
- Noise mode: `balanced`
- Rook env file: `config/rook_session.env` in bundle
- `IF_CHAT_ALLOW_SHARED_ROOMS=1` — enables multi-agent room sharing

### SSH safety rule

**Never use direct `10.10.10.170` MCP URLs from this machine.** All remote access goes through `infrafabric.io` SSH tunnel only.

### Known risk

SSH tunnels and MCP connections can silently drop. Verify connectivity before assuming a remote operation succeeded.

## Key Ideas

- Remote servers (if_context, if_blackboard) require SSH to infrafabric.io — they fail silently when the tunnel drops
- if_chat provides the ROOK room model: martin-room for governance, main-room-debug for exploration
- openspace is the bridge between Claude Code's skill corpus and the OpenSpace project environment
- Bundle was provisioned 2026-03-17; check for updates if behavior diverges from expectations

## Open Questions

- Is if_blackboard used for cross-agent state in the three-agent HEPHAISTOS stack?
- What is the relationship between openspace and the Codex skill update workflow?

## Sources

- `/home/cerebrhoe/.mcp.json`
- `/home/cerebrhoe/remote-bundles/` (directory scan)

## Related

- [[CLAUDE]]
- [[ROOK — Session Boundary Model]]
- [[InfraFabric Architecture]]
- [[MCP and Runtime Integration MOC]]
- [[claude-peers-mcp — Claude Peer Network]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
- [[Recursive Governance Protocol — Theseus, Auryn, Hopf]]
- [[HISTORY]]
