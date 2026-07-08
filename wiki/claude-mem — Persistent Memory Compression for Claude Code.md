---
type: wiki
title: claude-mem — Persistent Memory Compression for Claude Code
aliases:
- claude-mem
- claude-mem plugin
- thedotmack/claude-mem
- claude-mem Plugin — Session Memory Layer
- wiki/claude-mem — Persistent Memory Compression for Claude Code
tags:
- ai-tooling
- memory
- mcp
- claude-code
- persistence
- wiki
- claude-mem-persistent-memory-compression-for-claude-code-md
- claude
- corpora
- session
- lightrag
- plugin
- color-orange
status: active
created: '2026-04-16'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/claude-mem — Persistent Memory Compression for Claude Code.md
backlink_count: 12
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[wiki/Claude Code Skill Corpus]]'
- '[[wiki/EMERAULD]]'
- '[[wiki/GSD — Get Shit Done Context Engineering System]]'
- '[[wiki/GSD — Get-Shit-Done Claude Code System]]'
- '[[wiki/LightRAG — Graph-Based RAG System]]'
- '[[Areas/PHAROS/MCP and Runtime Integration MOC]]'
- '[[wiki/Obsidian Agent Vault Launch — Commercial Skill]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/RAG-Anything — Multimodal RAG Framework]]'
- '[[wiki/Reddit Data API — Access Terms and Rate Limits]]'
version-history-added: '2026-04-16'
---

# claude-mem — Persistent Memory Compression for Claude Code

## Summary

claude-mem (thedotmack/claude-mem, v6.5.0 in this archive) is a persistent memory compression system for [[Claude Code Skill Corpus|Claude Code]]. It compresses session history into searchable memory objects and exposes them as MCP tools. It is installed and active on this machine but is explicitly **not used for the [[EMERAULD Second Brain — Project Context]] vault** — EMERAULD uses `session-state.md` and [[LightRAG — Graph-Based RAG System]] instead.

## Context

claude-mem is scoped to code projects per `CLAUDE.md`. For EMERAULD, the persistence architecture is: [[LightRAG — Graph-Based RAG System]] for vault-wide knowledge retrieval, and `session-state.md` for session-level working memory. claude-mem handles memory for the broader [[HEPHAISTOS]] toolchain and code-project contexts where a LightRAG graph is not in place. The separation is intentional: EMERAULD is a structured knowledge vault, not a code project, and its retrieval needs are better served by graph traversal than by compressed session history. Relates to [[Recursive Continuity Without Memory — AI Identity Across Sessions]] as a practical implementation of continuity-by-compression.

## Details

### What It Does

claude-mem compresses Claude Code session history into memory objects (observations, corpora) and exposes them for retrieval via MCP tools. The result is that context from previous sessions becomes searchable without requiring the full transcript to be re-injected.

### Installation

- Node.js 18+
- Runs as a PM2 daemon in production
- Version in archive: 6.5.0

### Active MCP Tools (visible in this conversation)

| Tool | Function |
|---|---|
| `smart_search` | Semantic search across memory corpus |
| `search` | Keyword search across memory corpus |
| `query_corpus` | Structured query against a named corpus |
| `build_corpus` | Build a corpus from session history |
| `prime_corpus` | Pre-load a corpus for active session |
| `reprime_corpus` | Refresh a primed corpus |
| `rebuild_corpus` | Rebuild corpus from scratch |
| `get_observations` | Retrieve stored observations |
| `list_corpora` | List available corpora |
| `timeline` | Session timeline view |
| `smart_outline` | Structured outline of a corpus |
| `smart_unfold` | Expand a memory object for detail |

### Scoping Rule

claude-mem is explicitly scoped to code projects. The `CLAUDE.md` for EMERAULD states:

> claude-mem is excluded from this vault (scoped to code projects only).

EMERAULD uses `session-state.md` + [[LightRAG — Graph-Based RAG System]] as its two-layer persistence stack.

### Source Repository

- thedotmack/claude-mem on GitHub

## Key Ideas

- claude-mem and [[LightRAG — Graph-Based RAG System]] solve different problems: claude-mem compresses linear session history; LightRAG builds a traversable knowledge graph from structured notes.
- The MCP tool surface (`mcp__plugin_claude-mem_mcp-search__*`) is active in this session even though EMERAULD does not use it — it's available for code-project contexts.
- PM2 daemon operation means claude-mem persists across terminal sessions without manual restart.
- Corpus priming (`prime_corpus`, `reprime_corpus`) is the mechanism for making past memory available to the current session without re-injecting full transcripts.

## Version History (Oct–Dec 2025 commit log)

Captured from session activity log in `raw sources/claude-mem-plugin-2026-04-16.md`. Key milestones:

| Version | Date | Notable |
|---|---|---|
| 4.2.11 | Oct 25, 2025 | Marketplace metadata sync |
| 4.3.3 | Oct 27, 2025 | Configurable Session Display + First-Time Setup UX |
| 5.0.1–5.0.3 | Nov 4–5, 2025 | Version consistency work |
| 5.1.0 | Nov 5, 2025 | Comprehensive release with build process |
| 5.1.1 | Nov 6, 2025 | PM2 ENOENT fix (Windows), theme toggle, marketplace config |
| 5.2.0 | Nov 7, 2025 | Cleanup/worker branch merged (PR #69), PostToolUse hook schema compliance |
| 5.2.3 | Nov 8, 2025 | Troubleshooting skill added |
| 5.4.0 | Nov 9, 2025 | — |
| 5.4.1–5.4.5 | Nov 10–11, 2025 | Patch series |
| 7.2.3 | Dec 14, 2025 | Version consistency across all config files |
| 7.3.1–7.3.3 | Dec 16, 2025 | Final Dec bump |

The jump from 5.x to 7.x between November and December 2025 suggests either accelerated versioning or a major architectural revision in between. The archive snapshot (6.5.0 mentioned in this note) falls mid-range and may reflect an intermediate build.

## Open Questions

- Which corpora are currently built and available via `list_corpora`?
- Is there a clear boundary document defining which projects are in scope for claude-mem vs. session-state.md?
- Does 7.3.3 (Dec 2025) represent the current production version, or has it advanced further?
- What drove the version jump from 5.x to 7.x in December 2025?

## Sources

- `raw sources/claude-mem-plugin-2026-04-16.md` (commit activity log Oct–Dec 2025)
- `raw sources/claude-mem-plugin-2026-04-16.md` (original plugin capture)

## Related

- [[LightRAG — Graph-Based RAG System]]
- [[EMERAULD Second Brain — Project Context]]
- [[Recursive Continuity Without Memory — AI Identity Across Sessions]]
- [[Claude Code Skill Corpus]]
- [[HEPHAISTOS]]
- [[Plugin Recommendations]]
- [[changelog]]
- [[README]]
