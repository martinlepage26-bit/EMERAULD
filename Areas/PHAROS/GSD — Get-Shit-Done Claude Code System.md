---
type: wiki
title: GSD — Get-Shit-Done Claude Code System
aliases:
- GSD
- get-shit-done
- context rot
- meta-prompting
tags:
- tooling
- claude-code
- context-management
- codex
- areas
- gsd-get-shit-done-claude-code-system-md
- shit
- claude
- done
- codebase
- initialize
- color-orange
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/GSD — Get-Shit-Done Claude Code System.md
backlink_count: 8
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[Areas/PHAROS/GSD Tier 1 — Core Workflow Skills Hub]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[Areas/PHAROS/Obsidian Second Brain Product]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
---

# GSD — Get-Shit-Done Claude Code System

## Summary

GSD (Get-Shit-Done) is a lightweight meta-prompting, context engineering, and spec-driven development system installed at `/home/cerebrhoe/GSD/`. It addresses context rot — quality degradation as Claude fills its context window — and integrates with Claude Code, Codex, and other AI coding tools. Version 1.36.0 is installed locally.

## Context

Installed locally as a project companion to [[LightRAG — Graph-Based RAG System|EMERAULD's retrieval stack]] and [[InfraFabric Architecture|HEPHAISTOS's skill system]]. GSD is the planning-and-spec layer Martin uses alongside Claude Code sessions — relevant to the same context preservation problem [[claude-mem — Persistent Memory Compression for Claude Code]] addresses for code projects. Its `/gsd-map-codebase` and `/gsd-new-project` slash commands initialize project planning structure when resuming after a gap.

## Details

### Installation

- Path: `/home/cerebrhoe/GSD/get-shit-done-main-1.36.0/`
- Version: 1.36.0
- Install method: `npx get-shit-done-cc@latest`

### Core problem it solves

Context rot: as a Claude session fills its context window, output quality degrades. GSD prevents this through structured meta-prompting and spec-driven planning that keeps context lean and intentional.

### Key commands

| Command | Purpose |
|---|---|
| `/gsd-map-codebase` | Scan and index current codebase state |
| `/gsd-new-project` | Initialize fresh GSD planning structure from codebase map |

### Compatible tools

Works with: Claude Code, OpenCode, Gemini CLI, Kilo, Codex, Copilot, Cursor, Windsurf, Augment, Cline, and others.

### Local files

- `get-shit-done-main-1.36.0/` — main package
- `gsd-commands.txt` — local command reference
- `backups/` — local project backups

## Key Ideas

- Context rot is structural, not accidental — needs explicit mitigation
- Spec-driven development keeps Claude's working context aligned with stated intent
- The system is designed to be resumed after gaps (map first, then plan)

## Open Questions

- Is GSD integrated with HEPHAISTOS via the ORCHESTRATION layer, or used standalone?
- Is there an active GSD project plan running for PHAROS or martin-site?

## Sources

- `/home/cerebrhoe/GSD/get-shit-done-main-1.36.0/README.md`

## Related

- [[claude-mem — Persistent Memory Compression for Claude Code]]
- [[LightRAG — Graph-Based RAG System]]
- [[PHAROS Method — Technical Reference]]
- [[Obsidian Agent Vault — Launch Kit]]
