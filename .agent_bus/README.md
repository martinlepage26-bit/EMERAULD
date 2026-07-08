---
type: agent-bus-doc
title: agent_bus
aliases:
- .agent_bus/README
tags:
- agents
- agent-bus-doc
- agent-bus
- readme-md
- agent
- 'null'
- python
- heartbeat
- claude
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: .agent_bus
canonical_path: .agent_bus/README.md
backlink_count: 33
backlinks:
- '[[wiki/Agent Session Phenomenology]]'
- '[[wiki/CLI-Anything — Agent Harness for Tool Integration]]'
- '[[wiki/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]'
- '[[wiki/Claude Code Skill Corpus]]'
- '[[wiki/Cloudflare Pages-to-Worker Migration — Build and Asset Behavior]]'
- '[[wiki/Control Protocols MOC]]'
- '[[wiki/Elemental Agents Framework — Multi-Agent Role and Validation Architecture
  (2026-05-12)]]'
- '[[wiki/GSD — Get Shit Done Context Engineering System]]'
- '[[wiki/Governance Controls and Mechanisms]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)]]'
- '[[wiki/LightRAG — Graph-Based RAG System]]'
- '[[wiki/Manuscript Pipeline MOC]]'
- '[[wiki/Obsidian Agent Vault — Launch Kit]]'
- '[[wiki/PHAROS Final Voice Operator — GPT Creator]]'
- '[[wiki/PHAROS Runbook SOP]]'
- '[[wiki/PHAROS Workspace Inventory 2026-04-18]]'
- '[[wiki/Reddit Data API — Access Terms and Rate Limits]]'
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/Skill Corpus — Complete Live Index (260 Active Skills)]]'
- '[[wiki/Smallest Building Block — Relation as Rule]]'
- '[[wiki/Writing and Novels MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[archive/session-state/session-state-002]]'
- '[[artifacts/2026-04-19-pharos-migration-pr4/_manifest/MANIFEST]]'
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/START_HERE]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
- '[[wiki/claude-mem — Persistent Memory Compression for Claude Code]]'
- '[[wiki/claude-peers-mcp — Claude Peer Network]]'
- '[[memory/agents/Blockers]]'
- '[[memory/agents/Learning]]'
- '[[raw/Clippings/Reddit Data API Wiki]]'
- '[[templates/Raw Capture Template]]'
---

# agent_bus

Durable SQLite-backed message bus for Claude ↔ Codex coordination, scoped to this
repository (the EMERAULD vault). Complementary to — not a replacement for — the
machine-wide markdown peer channel at `/home/cerebrhoe/.claude/peer-channel.md`.

## Layout

```
.agent_bus/
├── agent_bus.py       # CLI, stdlib only (Python 3.9+, sqlite3)
├── messages.sqlite    # database (WAL mode; auto-created)
└── README.md          # this file
```

Invoke from the repo root:

    python3 .agent_bus/agent_bus.py <command> [options]

## Commands

### send

Send a message from one agent to the other. `--thread` is required for routing.

    python3 .agent_bus/agent_bus.py send \
        --from claude --to codex \
        --thread coordination \
        --body "Hello from Claude."

Body can also be piped or loaded from a file:

    echo "hello" | python3 .agent_bus/agent_bus.py send --from claude --to codex --thread t
    python3 .agent_bus/agent_bus.py send --from claude --to codex --thread t --body-file msg.txt

### inbox

Read unread messages (default) or all messages for an agent.

    python3 .agent_bus/agent_bus.py inbox --agent claude
    python3 .agent_bus/agent_bus.py inbox --agent claude --all
    python3 .agent_bus/agent_bus.py inbox --agent claude --json
    python3 .agent_bus/agent_bus.py inbox --agent claude --mark-read

### mark-read

Mark one or more messages as read. Use repeated `--id` or `--all`.

    python3 .agent_bus/agent_bus.py mark-read --agent claude --id 3
    python3 .agent_bus/agent_bus.py mark-read --agent claude --id 3 --id 4
    python3 .agent_bus/agent_bus.py mark-read --agent claude --all

### heartbeat

One-shot heartbeat update.

    python3 .agent_bus/agent_bus.py heartbeat --agent claude
    python3 .agent_bus/agent_bus.py heartbeat --agent claude --status online --note "watching"

### peers

List all heartbeats to see who is currently online.

    python3 .agent_bus/agent_bus.py peers
    python3 .agent_bus/agent_bus.py peers --json

### watch

Poll loop. Prints new unread messages as they arrive and refreshes the agent's
heartbeat on every tick. Default poll interval is 4 seconds (spec: 3–5).

    python3 .agent_bus/agent_bus.py watch --agent claude
    python3 .agent_bus/agent_bus.py watch --agent claude --interval 5
    python3 .agent_bus/agent_bus.py watch --agent claude --mark-read

Ctrl+C stops the loop cleanly and writes an `offline` heartbeat.

## Schema

```sql
messages(
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    thread      TEXT NOT NULL,
    sender      TEXT NOT NULL,    -- from_agent
    recipient   TEXT NOT NULL,    -- to_agent
    body        TEXT NOT NULL,
    created_at  TEXT NOT NULL,    -- ISO-8601 UTC (ts)
    read_at     TEXT              -- NULL = unread (status)
);

heartbeats(
    agent       TEXT PRIMARY KEY,
    status      TEXT NOT NULL,
    note        TEXT NOT NULL DEFAULT '',
    updated_at  TEXT NOT NULL
);
```

Semantic mapping to the original spec: `sender` = `from_agent`, `recipient` =
`to_agent`, `created_at` = `ts`, `read_at IS NULL` = `status='unread'`. The
heartbeats table carries `status`/`note` in addition to the spec's `ts` for
richer presence reporting.

Known agents: `claude`, `codex`. Unknown agents are rejected by `validate_agent`.

This bus is intentionally limited to Claude/Codex coordination for this
repository. Independent specialists such as Gadget are not bus participants
here; direct Gadget invocation is documented in
`/home/cerebrhoe/hephaistos/operator-to-gadget.md`.

## Concurrency

- `journal_mode = WAL` — readers don't block writers
- `busy_timeout = 5000` ms — tolerates brief lock contention
- `sqlite3.connect(..., timeout=30)` — transaction-level retry window
- Each write wrapped in an explicit `conn.commit()`

## Relation to the markdown peer channel

| Surface | Scope | Format | Best for |
|---------|-------|--------|----------|
| `/home/cerebrhoe/.claude/peer-channel.md` | machine-wide | append-only markdown | narrative session-close, audit exchanges, long-form reasoning |
| `.agent_bus/messages.sqlite` (this) | this repository | structured rows, read-tracked | short directed messages, live coordination, watch/heartbeat |

Use whichever fits the message. They are not mutually exclusive. Significant
disk-level events should still be posted to the markdown channel so a peer not
actively watching the bus sees them on next session start.

## Troubleshooting

- **"database is locked"** — another long-running `watch` is holding the write
  lock. Wait ~5 s or increase `--interval`.
- **WAL files on NTFS (WSL)** — `.sqlite-shm` and `.sqlite-wal` sidecar files
  are expected; do not delete while a connection is open.
- **Body empty** — pass `--body`, `--body-file`, or pipe to stdin. Empty bodies
  are rejected.

## Related

- [[Writing and Novels MOC]]
- [[Blockers]]
