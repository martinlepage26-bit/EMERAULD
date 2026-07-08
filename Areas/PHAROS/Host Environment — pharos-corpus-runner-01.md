---
type: wiki
title: Host Environment — pharos-corpus-runner-01
aliases:
- pharos-corpus-runner-01
- home/martin
- GCE host
- server
tags:
- infrastructure
- environment
- host
- server
- areas
- host-environment-pharos-corpus-runner-01-md
- apps
- mobile
- pane
- voicebridge
- martinlepage
- color-teal
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Host Environment — pharos-corpus-runner-01.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Agent Distillation Pipeline]]'
- '[[archive/wiki-2026-07-08/CLAUDEX — AI Dialogue Archive]]'
- '[[wiki/VoiceBridge Foundation]]'
---

# Host Environment — pharos-corpus-runner-01

## Summary

`pharos-corpus-runner-01` is the primary GCE Linux server for Martin's operator stack. Home directory is `/home/martin`. It runs the EMERAULD vault, the PHAROS-SUITE web apps, all mobile app builds, and the full AI agent council (Claude, Codex, Grok). Connected to [[EMERAULD — Vault and Knowledge Graph]] as the host machine and to [[PHAROS AI Lineage — Source of Truth]] as the deployment server.

## Context

The server replaced the previous WSL/Windows (`softinfo`/`cerebrhoe`) environment. Migration completed 2026-06-15 (see `MIGRATION-MANIFEST-2026-06-15.md`). SSH access via `pharos-martin-direct` key from local machine. GitHub account `martinlepage26-bit` authenticated via ED25519 key added 2026-06-21.

## Directory Map

| Path | Purpose |
|---|---|
| `~/EMERAULD/` | Personal knowledge vault — git repo at github.com/martinlepage26-bit/EMERAULD |
| `~/apps/web-apps/pharos-suite/` | PHAROS-SUITE web app (canonical, git-tracked) |
| `~/apps/web-apps/PHAROS-SUITE/` | Legacy uppercase copy — verify if still needed |
| `~/apps/web-apps/martinlepage26-bit.github.io/` | Personal site / portfolio (Astro) |
| `~/apps/web-apps/corpus-5point/` | 5-point corpus web app |
| `~/apps/mobile-apps/GAIAapp/` | GAIA Earth-calendar mobile app (Expo, v1.6) |
| `~/apps/mobile-apps/clearday-mobile/` | Clearday mobile app (Expo) |
| `~/apps/mobile-apps/lotus-mobile/` | LOTUS mobile app (Expo) |
| `~/CLAUDEX/` | AI council dialogue archive (Claude × Codex sessions) |
| `~/Lavoie/` | Lavoie consulting project (SOS Plomberie / Excavations Lavoie) |
| `~/VoiceBridge/` | VoiceBridge Foundation — AAC bridge fund project |
| `~/distillation/` | Agent distillation pipeline (32 agents, config-driven) |
| `~/agent-collab/` | tmux AI council shared workspace |
| `~/.UPLOADS/` | Incoming files staging area |
| `~/.claude/` | Claude Code config, skills, agents, session state |
| `~/.venvs/emerauld/` | Python venv for EMERAULD scripts (sentence-transformers) |

## Key Files

- `~/MIGRATION-MANIFEST-2026-06-15.md` — full migration record from old environment
- `~/PHAROS-AI CHANGE TRACKER.md` — running log of PHAROS site changes
- `~/.claude/CLAUDE.md` — global Claude Code instructions for this host
- `~/.ssh/id_ed25519` — ED25519 key for GitHub (martinlepage26-bit)

## Agent Stack

Three AI agents run concurrently in tmux sessions:
- `claude` pane — Claude Code (this instance), lead coordinator
- `codex` pane — OpenAI Codex (gpt-5.4), implementer
- `grok` pane — Grok, adversarial critic
- Council workspace: `~/agent-collab/BOARD.md`

## Related

- [[EMERAULD — Vault and Knowledge Graph]]
- [[PHAROS AI Lineage — Source of Truth]]
- [[GAIA — Earth-Calendar App and Evidence-Aware Positioning]]
- [[VoiceBridge Foundation]]
- [[CLAUDEX — AI Dialogue Archive]]

## See also
- [[Agent Distillation Pipeline]]
