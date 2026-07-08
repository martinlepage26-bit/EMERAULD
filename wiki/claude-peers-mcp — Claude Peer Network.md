---
type: wiki
title: claude-peers-mcp — Claude Peer Network
aliases:
- claude-peers
- peer network
- MCP peers
- multi-agent communication
- wiki/claude-peers-mcp — Claude Peer Network
tags:
- tooling
- mcp
- multi-agent
- claude-code
- infrastructure
- wiki
- claude-peers-mcp-claude-peer-network-md
- peers
- claude
- server
- message
- infrafabric
- color-orange
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/claude-peers-mcp — Claude Peer Network.md
backlink_count: 11
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Codex Skill Corpus Sync — 2026-04-20]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/HEPHAISTOS Agent Architecture]]'
- '[[wiki/InfraFabric Codex Alignment — System-Shaper Frame]]'
- '[[wiki/InfraFabric MCP Stack — Remote Bundles]]'
- '[[wiki/MCP and Runtime Integration MOC]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[memory/agents/Blockers]]'
- '[[memory/agents/Journal]]'
- '[[memory/agents/Learning]]'
---

# claude-peers-mcp — Claude Peer Network

## Summary

claude-peers-mcp is a local MCP server at `/home/cerebrhoe/claude-peers-mcp/` that enables multiple Claude Code instances running on the same machine to discover each other and exchange messages in real time. It is registered as a global MCP server via `claude mcp add --scope user` and is currently active in this session via the `claude-peers` channel. Built with TypeScript/Bun.

## Context

This tool enables the same kind of inter-agent coordination that the [[ROOK — Session Boundary Model|ROOK room model]] and [[InfraFabric Architecture|InfraFabric]] provide at the infrastructure level — but locally, between parallel Claude Code sessions. Relevant to the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|three-agent architecture]] where HEPHAISTOS, Queen Keyport, and Hermes may run as distinct agents. See also the [[InfraFabric MCP Stack — Remote Bundles]] for the server-side coordination layer.

## Details

### Installation

- Path: `/home/cerebrhoe/claude-peers-mcp/`
- Stack: TypeScript, Bun
- Registered: `claude mcp add --scope user --transport stdio claude-peers -- bun ~/claude-peers-mcp/server.ts`

### Key files

| File | Purpose |
|---|---|
| `server.ts` | MCP server entry point |
| `broker.ts` | Message routing between peers |
| `cli.ts` | CLI interface |
| `index.ts` | Package index |
| `shared/` | Shared types and utilities |

### Available MCP tools (via claude-peers)

| Tool | Purpose |
|---|---|
| `list_peers` | Discover other Claude Code instances (scope: machine/directory/repo) |
| `send_message` | Send a message to another instance by ID |
| `set_summary` | Set 1-2 sentence summary visible to other peers |
| `check_messages` | Manually check for new messages |

### Operating rule

When a `<channel source="claude-peers">` message arrives, respond immediately — pause current work, reply via `send_message`, then resume. Treat as a peer tap on the shoulder, not a background notification.

### Launch command

```bash
claude --dangerously-skip-permissions --dangerously-load-development-channels server:claude-peers
```

## Key Ideas

- Peer discovery is scoped: can find instances working in same machine, directory, or repo
- Messages arrive as channel events, not polled — immediate response expected
- `set_summary` creates ambient awareness across sessions without explicit querying

## Open Questions

- Is claude-peers used to coordinate HEPHAISTOS, Queen Keyport, and Hermes as distinct Claude Code sessions?
- What is the relationship between claude-peers and the InfraFabric `if_chat` MCP server?

## Sources

- `/home/cerebrhoe/claude-peers-mcp/README.md`
- `/home/cerebrhoe/claude-peers-mcp/` (directory scan)

## Related

- [[ROOK — Session Boundary Model]]
- [[InfraFabric MCP Stack — Remote Bundles]]
- [[InfraFabric Architecture]]
- [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)]]
- [[README]]
