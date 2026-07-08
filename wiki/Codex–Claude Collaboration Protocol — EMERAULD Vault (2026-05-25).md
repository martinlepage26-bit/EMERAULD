---
type: wiki
title: Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)
aliases:
- Codex Claude collaboration protocol
- EMERAULD vault graph collaboration protocol
tags:
- emerauld
- collaboration
- codex
- claude
- tmux
- coordination
- protocol
- graph
- wiki
- tooling
- session
- deepening
status: active
created: '2026-05-25'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25).md
backlink_count: 12
backlinks:
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]'
- '[[wiki/EMERAULD Thematic Analysis — Claude-Codex Pass (2026-05-25)]]'
- '[[wiki/EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]'
- '[[wiki/Weekly Review — 2026-06-26]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[archive/wiki-2026-07-08/WSL and System Storage Recovery — Quick Wins Checklist]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)

## Summary

Protocol for coordinated vault work between a Codex session (tooling/product/operator ops) and a Claude Code session (governance theory/humanities/scholarly track) while deepening the EMERAULD wiki-link graph and keeping logs auditable.

## Context

We run the vault as a governed system. Collaboration is not “chat”; it is **traceable edits + shared ledgers**. The two canonical ledgers are:

- [[session-state]] — durable session continuity (what happened, why, what changed, what’s next)
- [[VAULT ADDITIONS TRACKER]] — one-line addition log for every pass (what notes were created/edited and why it matters)

Tooling context and retrieval layers are documented in [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]].

## Details

### Domain split (default)

- **Claude owns:** governance theory, humanities/queer studies, PHAROS method, creative corpus, PHAROS scholarly track
- **Codex owns:** HELIX, operational records, skill domains, tooling scripts, commercial artifacts, agent architecture

If a pass crosses domains, the executor must **read the target note first** and keep edits minimal and link-focused.

### TMUX messaging protocol

- Treat tmux as the live coordination surface; treat the vault as the durable record.
- For coordination messages: paste the instruction packet into the target agent session, then record the outcome in `session-state.md` and `VAULT ADDITIONS TRACKER.md`.
- Never copy auth tokens or bearer strings from shell/tmux logs into vault notes; summarize actions and redact secrets.

### Pass discipline (graph deepening)

- Execute one pass at a time: read → edit notes → add reciprocal links where appropriate → log to [[VAULT ADDITIONS TRACKER]].
- After every 3 passes, append a status line under the current session note in [[session-state]] in this format:
  - `[CODEX1 PASS X–Y COMPLETE: one-line summary of notes edited and notes created]`

### Conflict avoidance

- Do not edit a note “owned” by the other agent without reading it first.
- Prefer adding links in **Related** or **Context** sections when editing outside your domain, unless the note’s body requires an inline bridge for graph health.

## Related

- [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]
- [[Personal and Projects MOC]]
- [[AI Infrastructure Stack]]
- [[HEPHAISTOS Agent Architecture]]
- [[WSL and System Storage Recovery — Quick Wins Checklist]] — Storage pressure on this machine directly affects Codex agent performance and vault tooling; priority recovery actions (vhdx compaction, lightrag venv deletion) required to unblock the vector search setup this protocol depends on
