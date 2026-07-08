---
type: project-planning
title: EMERAULD Vault Runtime
aliases:
- .planning/PROJECT
tags:
- planning
- project-planning
- project-md
- runtime
- scripts
- repo
- brownfield
- lightrag
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: .planning
canonical_path: .planning/PROJECT.md
backlink_count: 3
backlinks:
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[wiki/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
---

# EMERAULD Vault Runtime

## What This Is

EMERAULD is an Obsidian-based working vault that combines durable wiki notes, live business memory, and Python retrieval scripts so Martin can use the vault as an operational knowledge system. The code surface in this repo is the runtime layer around ingestion, vector search, and LightRAG-backed querying rather than the Hermes desktop app itself.

## Core Value

The vault must remain a reliable, source-faithful memory surface that agents and operator scripts can query without silently corrupting state.

## Requirements

### Validated

- ✓ Wiki notes can be ingested into a local LightRAG store via `scripts/ingest.py` — existing
- ✓ Local embeddings and vector search can be built and queried with `scripts/embed.py` and `scripts/vsearch.py` — existing
- ✓ The vault already maintains agent-facing continuity files such as `AGENTS.md`, `memory.md`, and `session-state.md` — existing

### Active

- [ ] Retrieval scripts always finalize LightRAG storage handles even when an operation raises
- [ ] LightRAG ingestion uses stable unique IDs for wiki notes rather than filename-only stems
- [ ] Claude OAuth refresh failures surface actionable errors instead of falling through to stale credentials
- [ ] A minimal local GSD scaffold exists for brownfield runtime hardening work in this repo

### Out of Scope

- Hermes Dashboard UI redesign or desktop packaging changes — those belong to the separate PyWebView app source of truth
- Broad vault-content restructuring, genealogy cleanup, or wiki rewrites — this pass is for runtime stability only
- Full product roadmap planning for every EMERAULD subdomain — this bootstrap is intentionally scoped to the script runtime

## Context

EMERAULD mixes knowledge-work artifacts with executable Python helpers. The main runtime scripts live under `scripts/` and currently cover LightRAG ingestion/querying, local embedding search, drive auditing, and related utilities. Repo instructions already distinguish the vault as business/context memory and keep Hermes Dashboard as a separate operational surface, so the first GSD phase here should focus on script reliability rather than content or UI redesign.

## Constraints

- **Scope**: Keep changes additive and local — the repo already contains operator-edited vault files and continuity notes
- **Compatibility**: Preserve the existing Python script entrypoints and CLI ergonomics — these scripts are already used as operator tools
- **Governance**: Do not treat `memory.md` or vault notes as the source of truth for Hermes runtime state — AGENTS instructions separate those concerns
- **Safety**: Avoid repo-wide rewrites or automatic commits while unrelated local changes are present

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Seed GSD locally around the Python retrieval runtime first | The repo had no `.planning/` tree, but the runtime scripts provide a real executable surface for a brownfield first phase | ✓ Good |
| Use a review/fix bootstrap instead of a broad roadmap buildout | The immediate need is actionable script hardening, not large-scale planning ceremony | ✓ Good |

## Evolution

This document evolves at phase transitions and milestone boundaries.

**After each phase transition**:
1. Move validated runtime guarantees into the Validated section
2. Add newly discovered operational constraints from the vault/runtime boundary
3. Record decisions that affect Hermes, Trismégiste, or retrieval wiring

**After each milestone**:
1. Recheck whether the script runtime still reflects current repo reality
2. Expand the roadmap only if a second executable surface needs phased planning
3. Keep vault-content work and runtime work explicitly separated

---
*Last updated: 2026-04-23 after local brownfield GSD bootstrap*

## Related

- [[Governance and PHAROS MOC]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
