---
type: note
title: Agent Scaffolds — ~agents vs .claude-agents Distinction
tags:
- claude-code
- subagents
- agent-scaffolding
- infrastructure
- pharos-ops
- note
- areas
- pharos
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Agent Scaffolds — ~agents vs .claude-agents Distinction.md
backlink_count: 2
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Agent Scaffolds — ~agents vs .claude-agents Distinction

> For future Claude: these are two different layers of the same small set of agents, not two competing agent systems. `~/agents/` holds the design source-of-truth (prompt.md, guardrails.md, tests, logs); `~/.claude/agents/` holds the live, minimal Claude Code registrations that point back at those source files. Don't assume every entry in one directory has a counterpart in the other — most `.claude/agents/` entries do not.

## Summary

`/home/martin/agents/` and `/home/martin/.claude/agents/` are not duplicates or competing definitions — they are two different layers for the same handful of PHAROS ops agents. `~/agents/` is the scaffold/design layer (full spec, guardrails, test cases, run logs) for a small set of internal operations agents; `~/.claude/agents/` is the live registration layer Claude Code actually reads to make a subagent invocable, and for the agents that have a scaffold, the `.claude/agents/*.md` file is a thin pointer back into `~/agents/<name>/prompt.md` and `guardrails.md`.

## Context

Verified on disk 2026-07-08. `/home/martin/agents/` contains six scaffolded agents, each with the same internal shape (`README.md`, `prompt.md`, `guardrails.md`, `tools.json`, `tests/`, `logs/`): `analyst`, `data-query`, `doc-retriever` (each standalone), plus `ship-to-market/` which itself bundles three — `ship-announcer`, `deploy-checker`, `release-coordinator` — along with a `drafts/` staging area (`aurora-2026-06-27`, `helix-2026-06-27`, `pharos-site-2026-06-27`) and its own top-level `README.md` describing the ship-to-market build order. There is also `/home/martin/agents/reports/product-status-2026-06-27.md`, a synthesized cross-product status snapshot (6,991 bytes) produced by the `analyst` agent per its documented job description.

`/home/martin/.claude/agents/` holds 27 agent definition files total, of which exactly 6 have a matching scaffold in `~/agents/`: `analyst.md`, `data-query.md`, `doc-retriever.md`, `ship-announcer.md`, `deploy-checker.md`, `release-coordinator.md`. The remaining 21 (`hephaistos.md`, `queen-keyport.md`, `hermes.md`, `argus.md`, `bowie.md`, `gadget.md`, `henry.md`, `trismegiste.md`, `executor.md`, and the Code-reviewer/Code-Simplifier/IF-story/OCI-Expert/Project-Manager/Project-Owner/Release-Engineer/Release-Manager-Resume-Specialist/Security-Reviewer/Tech-Lead/UX-Reviewer/WordPress-Coder/release-coordinator set) are defined entirely inline in `.claude/agents/` with no corresponding `~/agents/<name>/` scaffold directory.

## Details

**What each layer actually contains, confirmed by reading files directly:**

`/home/martin/.claude/agents/analyst.md` (the live registration):
```
---
name: analyst
description: Use when Martin needs synthesis, calculation, or a structured report...
model: sonnet
---

You are the PHAROS analyst agent. Synthesize data into structured reports...

Full spec: `/home/martin/agents/analyst/prompt.md`
Guardrails: `/home/martin/agents/analyst/guardrails.md`

Read both files before doing anything else.
```

Same pattern confirmed in `data-query.md` (model: haiku) and `doc-retriever.md` (model: haiku) — each is a short frontmatter block (name, trigger description, model tier) plus an explicit instruction to go read the full spec and guardrails out of `~/agents/<name>/`.

`/home/martin/agents/analyst/README.md` is the design document: job description, business pain solved, trigger phrases, inputs, outputs (with exact write path `~/agents/reports/[topic]-[YYYY-MM-DD].md`), tools allowed vs. forbidden (Read/Write scoped to `~/agents/reports/` only, Bash limited to arithmetic — `bc`/`python3 -c`; no external API calls, no `wrangler`, no `gh` CLI, no data mutation), human-approval requirements, available report types, and a success metric. This is the layer that actually specifies behavior in detail — the `.claude/agents/analyst.md` file is deliberately thin and defers to it.

**So the distinction is:**

| Layer | Role | Contents | Governs |
|---|---|---|---|
| `~/agents/` | Design/scaffold source of truth | README (spec), prompt.md, guardrails.md, tools.json, tests/, logs/ | What the agent is supposed to do, its allowed tools, its guardrails, its test cases |
| `~/.claude/agents/` | Live Claude Code registration | Frontmatter (name, description/trigger phrases, model) + a short pointer back to the scaffold | Whether/how Claude Code can actually invoke the agent as a subagent, and which model tier it runs on |

For the 6 agents that exist in both places, the `.claude/agents/` file is not a second, independent definition — it is the runtime shim, and the scaffold in `~/agents/` is the thing that shim is required to read before acting. For the other 21 live agents (the three-agent-architecture agents — Hephaistos, Queen Keyport, Hermes — plus Argus, Bowie, Gadget, Henry, Trismégiste, Executor, and the various role-specific reviewers/leads), there is no `~/agents/` scaffold at all; they were built directly as `.claude/agents/*.md` definitions without going through the scaffold-prototype stage. This is consistent with `~/agents/` being an earlier or parallel prototyping ground for a specific class of narrow, single-job ops agents (status reporting, data query, doc retrieval, release/announcement pipeline) rather than a staging step every agent passes through.

One related HELIX data point worth noting: [[HELIX Test Run — Claude Code Agents as Subject (2026)]] treats Claude Code agents themselves as a HELIX test subject — a different investigative angle (stress-testing agent behavior) from this note's structural/inventory angle (where agent definitions physically live and how the two directories relate).

## Related

- [[HELIX Test Run — Claude Code Agents as Subject (2026)]]
- [[Governance and PHAROS MOC]]
- [[Contremaître — Groupe Lavoie Field-Operations Platform]]
