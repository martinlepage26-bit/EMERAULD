---
type: tool-evaluation
title: ai-agent-board — Third-Party Tool Evaluation
tags:
- tool-evaluation
- oss-clone
- kanban
- multi-agent-orchestration
- claude-code
- codex
- hermes-naming-collision
- pharos
- vm-inventory
- areas
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/ai-agent-board — Third-Party Tool Evaluation.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/corpus-5point — FastAPI-Next.js Research Platform]]'
- '[[Areas/PHAROS/nexusos — Base44 App]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# ai-agent-board — Third-Party Tool Evaluation

> For future Claude: this is **not a PHAROS product**. It's a clone of an
> open-source third-party repository (`DanWahlin/ai-agent-board`) sitting at
> `/home/martin/apps/ai-agent-board/`, present on this VM for evaluation/use
> as a coding-agent orchestration tool, not something Martin built or owns.
> Treat any references to a production deployment (`kanban.codewithdan.com`)
> as the **upstream author's** deployment documented in their own README/AGENTS.md
> — not evidence Martin has deployed an instance.

## Summary

AI Agent Board is a drag-and-drop Kanban board that delegates coding tasks
to AI coding-agent CLIs — GitHub Copilot, Claude Code, OpenAI Codex,
OpenCode, "Hermes," or OpenClaw — streaming their live progress back to the
board and supporting local-merge or PR-based delivery. It is cloned onto
this host as a candidate tool for coordinating multi-agent coding work,
adjacent to (but independent of) Martin's own three-agent governance
architecture.

## Context

Sources read (read-only): `README.md` and `AGENTS.md` at the repo root. No
`.env`/`.env.example` values, Docker credentials, or CI secrets were
inspected beyond confirming their file paths exist.

- Repository origin: `github.com/DanWahlin/ai-agent-board` (per the CI
  badge URL in `README.md`).
- On-disk clone date: file mtimes across the repo (`README.md`, `AGENTS.md`,
  `package.json`, etc.) are 2026-06-25.
- Licensed under its own `LICENSE` file (present in repo root; not read for
  terms beyond confirming its existence — treat as third-party licensed
  code, respect its license before any redistribution).

## Details

**What it does:** create a task in Backlog → drag to In Progress → the
agent panel opens → configure repo path, branch, agent type, and whether to
use an isolated git worktree → the selected agent CLI plans, executes, and
streams live output via WebSocket → review the diff/output → merge locally
or open a PR (auto-detected based on whether the repo has a GitHub remote).
It also supports **Task Groups** — batches of 2–20 related child tasks
launched with a configurable concurrency slider, useful for fanning out
similar changes across a codebase.

**Architecture** (from `AGENTS.md`): npm-workspaces monorepo —
`packages/client` (React 19 + Vite + Tailwind 4 + Framer Motion + xterm.js
terminal viewer), `packages/server` (Express + WebSocket + a
provider-pattern agent abstraction via the external
`@codewithdan/agent-sdk-core` package, with SQLite via better-sqlite3 as the
zero-config default or PostgreSQL via `pg`), and `packages/e2e` (Playwright
tests). Agents are auto-detected at server startup by checking for
installed/authenticated CLIs.

**Six supported agent providers**: `copilot`, `claude` (via
`@anthropic-ai/claude-agent-sdk`), `codex` (`@openai/codex-sdk`),
`opencode`, `hermes`, and `openclaw` — each normalized into a common
`AgentEvent` stream regardless of provider.

**Naming collision worth flagging**: one of the six supported agent
providers is literally named "Hermes" (a "Hermes Agent" CLI, checked via
`hermes acp --check`). This is a different tool than Martin's own **Hermes**
— the Tier 2 routing/integration agent in the PHAROS three-agent
architecture (Hephaistos / Queen Keyport / Hermes). They are unrelated
software with the same name; do not conflate the two when reading logs or
docs that mention "Hermes" in the context of this tool.

**Production reference in the docs (upstream, not Martin's):** `AGENTS.md`
documents a systemd-managed production deployment at
`kanban.codewithdan.com` (server on port 3001, client dev server on port
4175, PostgreSQL via a `ai-agent-board-db` Docker container) — this is the
open-source project author's own hosted instance, described in their
repository documentation as reference material, not a deployment Martin has
stood up.

**Framing for this note:** treat `ai-agent-board` as a tool under
evaluation for Martin's own multi-agent coding workflows (it directly
overlaps with the tmux-ai-council / council-of-CLIs pattern already in use)
— not as a product to build, brand, or ship under PHAROS.

## Related

- [[Areas/PHAROS/PHAROS Product Stack]] — canonical PHAROS product-family bridge note; explicitly not extended here since this is a third-party evaluation, not a PHAROS product.
- [[Areas/PHAROS/CLI-Anything — Agent Harness for Tool Integration]] — closely related existing note on harnessing CLI-based agent tools; directly relevant framing for evaluating this board's CLI-agent-orchestration approach.
- [[Areas/PHAROS/Agent Distillation Pipeline]] — existing note on agent workflow/distillation patterns, useful comparison for how this tool structures agent task execution.
- [[Areas/PHAROS/nexusos — Base44 App]] — a different internal-tooling answer to a related need (managing a portfolio of projects/decisions) evaluated on the same host.
- [[Areas/PHAROS/corpus-5point — FastAPI-Next.js Research Platform]] — contrast point: CORPUS is a project Martin is building, whereas this is a project Martin is only running/evaluating.
