---
type: wiki
title: Obsidian Second Brain Integration — EMERAULD Setup (2026-06-21)
aliases:
- obsidian-second-brain
- obsidian skills integration
- wiki/Obsidian Second Brain Integration — EMERAULD Setup (2026-06-21)
tags:
- infrastructure
- vault
- claude-code
- obsidian
- wiki
- obsidian-second-brain-integration-emerauld-setup-2026-06-21-md
- commands
- installed
- brain
- emerauld
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Obsidian Second Brain Integration — EMERAULD Setup (2026-06-21).md
backlink_count: 5
backlinks:
- '[[.graph_store/graph_report]]'
- '[[wiki/EMERAULD]]'
- '[[Areas/PHAROS/MCP and Runtime Integration MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[memory/daily/2026-06-23]]'
---

> For future Claude: This note documents the three-repo Obsidian stack integrated into EMERAULD on 2026-06-21. It enables self-rewriting notes, 45 new slash commands, and format-literate writes via kepano's skills. Load this note when diagnosing vault tooling, adding new commands, or explaining the skill stack to a fresh session.

## Summary

Three GitHub repos were integrated into [[EMERAULD]] to extend it into a living, self-rewriting knowledge base connected to [[Claude Code]] and the [[PHAROS]] stack.

## Context

EMERAULD already had 879 wiki notes, a Python vector store (`vsearch.py`), and [[Trismégiste]] for continuity. These repos add write-back capability, format literacy, and a 45-command research and synthesis toolkit without replacing the existing infrastructure.

## Details

### Repos installed

**1. [kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)** — by Steph Ango (Obsidian CEO)
- 5 format skills: `obsidian-markdown`, `obsidian-bases`, `json-canvas`, `obsidian-cli`, `defuddle`
- Installed to: `~/.claude/skills/` via symlinks
- Purpose: ensures every Claude write to EMERAULD uses correct Obsidian syntax (wikilinks, callouts, frontmatter, Canvas)

**2. [eugeniughelbur/obsidian-second-brain](https://github.com/eugeniughelbur/obsidian-second-brain)**
- 45 slash commands in `~/.claude/commands/`
- Skill at `~/.claude/skills/obsidian-second-brain`
- Config: `~/.config/obsidian-second-brain/.env` (OBSIDIAN_VAULT_PATH set)
- Key commands: `/obsidian-save`, `/obsidian-ingest`, `/obsidian-reconcile`, `/obsidian-synthesize`, `/research`, `/research-deep`, `/x-pulse`
- Note: self-rewriting mode inverts Karpathy's append-only LLM Wiki — sources update existing pages

**3. [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind)** — not installed
- Requires Node 22+ (current: v20.20.2); EMERAULD already has `vsearch.py` as equivalent to QMD; rook harness already handles session start
- Revisit if Node 22 is installed via nvm

### Integration decisions

| Decision | Rationale |
|---|---|
| `wiki/` as write-back target (not vault root) | EMERAULD's primary note directory |
| `raw sources/` as ingest lane (not `raw/`) | EMERAULD convention: `raw/` = verified hard-moved |
| Keep `vsearch.py`, skip QMD | Already local, Python-based, no Node 22 needed |
| Keep Trismégiste as primary agent | Second Brain commands are additive tools |
| `_CLAUDE.md` bridges to existing `CLAUDE.md` rules | Second Brain reads `_CLAUDE.md` at vault root |

### Runtime dependencies installed

- `uv` 0.11.23 → `~/.local/bin/uv`
- Python 3.12 venv at `~/.claude/skills/obsidian-second-brain/.venv` (51 packages synced)
- Vector store rebuilt: 902 entries (was 896), integration note confirmed indexed and searchable

### API keys — all set (as of 2026-06-21)

- `XAI_API_KEY` — Grok; powers `/x-pulse`, `/x-read`, `/youtube`
- `PERPLEXITY_API_KEY` — powers `/research`, `/research-deep`
- `GEMINI_API_KEY` — powers `/notebooklm`
- `YOUTUBE_API_KEY` — optional; transcript extraction works without it
- Location: `~/.config/obsidian-second-brain/.env` (chmod 600)

### Hooks wired (as of 2026-06-21)

**PostCompact — ACTIVE**
- Script: `hooks/obsidian-bg-agent.sh`
- Fires after context compaction; reads session summary, propagates vault-worthy items (decisions, tasks, people, projects, dev work) to [[EMERAULD]] unattended
- Enabled via: `OBSIDIAN_BG_AGENT_ENABLED=1` + `OBSIDIAN_VAULT_PATH` in `~/.claude/settings.json` env block
- Logs to: `/tmp/obsidian-bg-agent.log`

**PostToolUse validator — SKIPPED (format incompatibility)**
- `validate-ai-first.sh` checks for `date:`, `ai-first: true`, and `## For future Claude` heading
- EMERAULD uses `created:`/`updated:` (not `date:`), no `ai-first:` field, blockquote preamble (`> For future Claude:` not `##`)
- Wiring would fire false positives on every vault write — noise with no signal
- Revisit if EMERAULD format is ever aligned to second-brain defaults, or if a fork of the validator is written for EMERAULD's schema

### Scheduled agents — wired via cron (as of 2026-06-21)

Scripts at `/home/martin/EMERAULD/scripts/scheduled/`. Logs to `/tmp/obsidian-*.log`.

| Agent | Schedule | What it does |
|---|---|---|
| `morning.sh` | daily 8:00 AM | Creates daily note, surfaces overdue tasks + stale active projects |
| `nightly.sh` | daily 10:00 PM | Reconciles contradictions, synthesizes patterns, heals orphans, rebuilds vector store |
| `weekly.sh` | Fri 6:00 PM | Generates weekly review note in `wiki/` |
| `health-check.sh` | Sun 9:00 PM | Vault health audit (orphans, missing frontmatter, broken links, stale projects) |

### obsidian-mind — selective install (as of 2026-06-21)

Node 22.23.0 installed via nvm (unblocks QMD and TypeScript hooks if needed later).

7 unique performance/career commands installed to `~/.claude/commands/` (skipping hooks, CLAUDE.md, and commands already covered by obsidian-second-brain):

- `/om-incident-capture` — structured incident documentation
- `/om-peer-scan` — GitHub PR archaeology for performance evidence / brag doc
- `/om-review-brief` — performance review aggregation
- `/om-review-peer` — peer review writing
- `/om-self-review` — self-review writing
- `/om-prep-1on1` — 1-on-1 preparation
- `/om-slack-scan` — Slack incident reconstruction

obsidian-mind hooks (SessionStart TypeScript, QMD): not installed — rook harness and vsearch.py already cover these functions.

## Related

- [[EMERAULD]] — vault home
- [[Trismégiste]] — primary vault continuity agent
- [[MCP and Runtime Integration MOC]] — related tooling
- [[PHAROS]] — broader stack this serves
