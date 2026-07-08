---
type: wiki
title: InfraFabric MCP Stack — Remote Bundles
aliases:
- MCP stack
- remote-bundles
- if_context
- if_blackboard
- openspace
- if_chat
- InfraFabric MCP
- wiki/InfraFabric MCP Stack — Remote Bundles
tags:
- infrastructure
- mcp
- infrafabric
- tooling
- remote
- wiki
- infrafabric-mcp-stack-remote-bundles-md
- blackboard
- openspace
- hosted
- stacklight
- color-orange
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/InfraFabric MCP Stack — Remote Bundles.md
backlink_count: 19
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[CLAUDE]]'
- '[[wiki/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/HEPHAISTOS Agent Architecture]]'
- '[[wiki/InfraFabric Codex Alignment — System-Shaper Frame]]'
- '[[wiki/InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)]]'
- '[[wiki/MCP and Runtime Integration MOC]]'
- '[[wiki/PHAROS Strategic Analysis — Keep Stop Fix Finish (2026-04-18)]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/Stacklight-owner-explainer]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[wiki/claude-peers-mcp — Claude Peer Network]]'
- '[[wiki/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]'
- '[[wiki/if.switchboard — InfraFabric Product Center]]'
- '[[memory/daily/2026-06-27]]'
- '[[memory/daily/2026-06-30]]'
- '[[memory/daily/2026-07-01]]'
- '[[session-state]]'
---

# InfraFabric MCP Stack — Remote Bundles

## Summary

The InfraFabric MCP stack is a set of four MCP servers registered in `~/.mcp.json` that connect Claude Code sessions on Martin's machine to [[InfraFabric Architecture|InfraFabric]] services running on `infrafabric.io`. The bundle files live at `/home/cerebrhoe/remote-bundles/martin_lepage_codex_remote_bundle_20260317T022437Z/`. Historically (through 2026-06-27), two servers (if_context, if_blackboard) tunneled through SSH to a Proxmox container while two (openspace, if_chat) ran locally; as of the [[InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)|R0.5 rollout]] (2026-06-29/06-30), if_context and if_blackboard both moved to hosted HTTPS APIs — see Details below.

## Context

This is the local side of the [[ROOK — Session Boundary Model|ROOK infrastructure harness]]. The `if_chat` server provides the room-based communication model (martin-room / martin-room-debug) that ROOK uses for agent coordination. The `if_context` server provides context storage for the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|HEPHAISTOS governance stack]]. The `openspace` server bridges Claude Code's skill directory (`~/.codex/skills`) with the OpenSpace workspace. See also [[claude-peers-mcp — Claude Peer Network]] for the local peer-to-peer layer.

Cluster routing note: [[MCP and Runtime Integration MOC]].

## Details

### Bundle location

`/home/cerebrhoe/remote-bundles/martin_lepage_codex_remote_bundle_20260317T022437Z/`

### Four MCP servers

#### 1. if_context (superseded 2026-06-30 — now hosted API, not SSH)

- **Historical transport (through 2026-06-27, when this note was last current on this point):** Node script + SSH tunnel → Proxmox container 270 via `root@infrafabric.io` (`/home/cerebrhoe/.ssh/infrafabric_martin_lepage_ed25519`), command `pct exec 270 -- /usr/bin/env IF_CONTEXT_MCP_CLAUDE_COMPAT=1 ... if-context-mcp-server.mjs`, local API base `http://127.0.0.1:18881`.
- **Current transport (repaired 2026-06-30 by session `/rook-410`):** Hosted `if.context` [[InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)|R0.5]] API on `mtl-02` at `https://api.infrafabric.io/v1/context/*`, PostgreSQL schema/table `if_context.r05_events` inside the same `mtl-02` `if_blackboard` database, systemd service `if-context-r05-api.service` on `127.0.0.1:8098` behind Caddy. MCP client `/root/scripts/if_context_api_mcp_server.py` is now a real API-backed client; `iftransport` defaults `if_context` to API mode (`IFTRANSPORT_MCP_IF_CONTEXT_MODE=api` set explicitly on mtl-01 and mtl-03). Verified: `context_health` returns `authority_class=hosted_context_r05_api` on both hosts.
- **Root cause of the pre-repair failure:** mtl-03's Codex config pointed `if_context` at the private mtl-01 URL `10.10.10.170:18890`, unreachable from mtl-03 — the exact address class this note's SSH safety rule (below) warns against using directly.
- Purpose: Context storage and policy for HEPHAISTOS sessions
- Source of the migration correction: `/home/martin/apps/stacklight/documentation/agents/5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md`, section "Hosted if_context API / MCP Repair"

#### 2. if_blackboard (superseded 2026-06-29 — now hosted API, not SSH)

- **Historical transport (through 2026-06-27, when this note was last current on this point):** Node script + SSH tunnel → Proxmox container 270, command `pct exec 270 -- /usr/bin/node ... if-blackboard-mcp-server.mjs`
- **Current transport (R0.5 rollout, 2026-06-29 onward):** API-backed stdio MCP shim (`if_blackboard_api_mcp_server.py`) calling the hosted HTTPS API at `https://api.infrafabric.io`, backed by PostgreSQL on host `mtl-02` (`if_blackboard.r05_events`). Direct SSH/script/JSONL mutation now fails closed by design — it is not a fallback path.
- Purpose: Shared blackboard for inter-agent task, signal, checkpoint, and verification state; see [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]
- Source of the migration correction: `/home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md`, also see [[Stacklight-owner-explainer]]

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

**Never use direct `10.10.10.170` MCP URLs from this machine.** All remote access goes through `infrafabric.io` SSH tunnel only. This was the historical rule through 2026-06-27/29. **Both `if_blackboard` (2026-06-29) and `if_context` (2026-06-30) have since migrated off SSH tunnel and off direct `10.10.10.x` URLs entirely** — see the superseded-transport notes above. A private-URL misconfiguration on `if_context` (mtl-03 pointed at `10.10.10.170:18890`) was the actual root cause of a real outage repaired 2026-06-30, which validates why this rule existed. This safety rule now applies only if a server in this bundle has not been separately documented as migrated to the R0.5 hosted-API pattern — as of 2026-07-01, that is not the case for any of the four servers listed here for `if_blackboard`/`if_context`; `openspace` and `if_chat` were local/bridge transports to begin with and were never SSH-tunneled.

### Known risk

SSH tunnels and MCP connections can silently drop. Verify connectivity before assuming a remote operation succeeded.

## Key Ideas

- Remote servers (if_context, if_blackboard) required SSH to infrafabric.io through 2026-06-27; both migrated to hosted HTTPS APIs on `mtl-02` in the R0.5 rollout (2026-06-29/06-30) and no longer depend on the SSH tunnel — see Details above
- if_chat provides the ROOK room model: martin-room for governance, main-room-debug for exploration
- openspace is the bridge between Claude Code's skill corpus and the OpenSpace project environment
- Bundle was provisioned 2026-03-17; check for updates if behavior diverges from expectations

## Open Questions

- Is if_blackboard used for cross-agent state in the three-agent HEPHAISTOS stack?
- What is the relationship between openspace and the Codex skill update workflow?
- ~~Did `if_context` (server #1) also migrate off SSH in the R0.5 rollout, or is it still SSH-tunneled?~~ **Resolved 2026-07-01:** yes, repaired 2026-06-30 — hosted API/Postgres, same as if_blackboard. See updated server #1 entry above.
- `mtl-03`'s own `if-cli` binary is drifted (points to an older `if_cli.py` with no `blackboard` command) — CLI parity is not yet claimed on this host even though the underlying if_blackboard/if_context API migration is complete. Not yet repaired as of the 2026-06-30 handover.

## Sources

- `/home/cerebrhoe/.mcp.json`
- `/home/cerebrhoe/remote-bundles/` (directory scan)
- `/home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md` (if_blackboard R0.5 migration evidence, 2026-07-01 correction)
- `/home/martin/apps/stacklight/documentation/agents/5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md` (if_context R0.5 migration evidence + mtl-03 if-cli drift, 2026-07-01 correction)

## Related

- [[CLAUDE]]
- [[ROOK — Session Boundary Model]]
- [[InfraFabric Architecture]]
- [[InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)]]
- [[MCP and Runtime Integration MOC]]
- [[claude-peers-mcp — Claude Peer Network]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
- [[Recursive Governance Protocol — Theseus, Auryn, Hopf]]
- [[Stacklight-owner-explainer]]
- [[HISTORY]]
