---
type: wiki
title: CLI-Anything — Agent Harness for Tool Integration
tags:
- areas
- agents
- wraps
- harness
- mubu
- mutate
- anything
- wiki
- pharos
status: active
domain: pharos
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/CLI-Anything — Agent Harness for Tool Integration.md
backlink_count: 13
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[Areas/PHAROS/HEPHAISTOS Agent Architecture]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Launch Kit]]'
- '[[Areas/PHAROS/ai-agent-board — Third-Party Tool Evaluation]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/Home]]'
- '[[Resources/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]'
- '[[archive/wiki-2026-07-08/SYSTEM CHECK]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# CLI-Anything — Agent Harness for Tool Integration

## Summary
CLI-Anything is a framework for building AI-controlled CLI wrappers around GUI and service-based tools, enabling [[Agent Session Phenomenology|agent-driven]] programmatic access to applications that do not natively expose a CLI. Part of the local agent harness infrastructure supporting [[InfraFabric Architecture]] and [[Martin Lepage — Professional Profile|Martin's]] tool ecosystem.

## Context
The project produces a set of tool-specific harnesses under a unified architecture. Each harness wraps a target application's API, filesystem, or GUI layer, and exposes it through a Click-based CLI with both subcommand and REPL modes. This infrastructure supports the [[Recursive Deterministic AI Governance — Method and Paper|recursive governance]] workflow by allowing agents to inspect, navigate, and mutate external tools programmatically. Source files live in `/root/cli-anything/` and are packaged under `agent-harness/`.

## Details

### Architecture Pattern
Each tool harness follows the same structure:
- **Backend surface**: REST API, local file inspection, or GUI-level config
- **Click CLI**: structured command groups (discover, inspect, mutate, session)
- **REPL mode**: persisted session state (current document, current node, history)
- **Safety model**: inspect before mutate; dry-run first; live-verified mutations
- **Packaging**: editable install, skill-generator for agent skill regeneration

### Tool Harnesses

**Mubu** (`cli-anything-mubu`) — Mindmap / outliner desktop app. Wraps local backup snapshots, RxDB storage, and live Mubu REST API (`/v3/api/document/get`, `/v3/api/colla/events`). Commands: `recent`, `folders`, `doc-nodes`, `update-text`, `create-child`, `delete-node`. Known gaps: no undo/redo, no move primitive.

**Ollama** (`cli-anything-ollama`) — Local LLM runtime on `localhost:11434`. Wraps full REST API surface: model management (`list`, `pull`, `rm`, `copy`, `ps`), generation (`text`, `chat`), and embeddings. Supports streaming NDJSON for progressive output.

**Obsidian** (`cli-anything-obsidian`) — Wraps the Obsidian Local REST API plugin on `localhost:27124`. Commands: `vault list/read/create/update/delete/append`, `search query/simple`, `note active/open`, `command list/execute`. Auth via Bearer token + `OBSIDIAN_API_KEY` env var. Related to this vault directly.

**OBS Studio** (`cli-anything-obs`) — Screen recording and streaming. Wraps JSON scene collection format rather than live OBS API. Commands manage projects, scenes, sources (webcam, display capture, browser), filters (chroma key, noise suppression), and output (streaming/recording configs).

**Openscreen** — Electron-based screen recording editor (React + PixiJS + WebCodecs). CLI harness wraps timeline editing operations (zoom effects, speed changes, annotations, crop).

**NotebookLM** — Service-style CLI wrapper around the community `notebooklm` CLI client. Wraps notebook management, source ingestion, chat, and artifact generation. Auth via local Google session; destructive operations require explicit confirmation.

**LibreOffice** — Produces real ODF files (ZIP archives with XML) without requiring a GUI or LibreOffice installation. Targets Writer, Calc, and Impress document types.

**Mermaid** — Creates, edits, and renders Mermaid diagrams via stateful project files and the mermaid.ink renderer. Supports flowcharts, sequence diagrams, and other diagram types.

**n8n** — Workflow automation platform CLI. Manages workflows, executions, credentials, variables, and tags via the n8n Public API v1.1.1.

**Novita AI** — OpenAI-compatible AI API client targeting DeepSeek, GLM, and other models available via the Novita service.

**PM2** — Stateless CLI for Node.js process management via the PM2 CLI subprocess. List, start, stop, restart processes, view logs, manage system configuration. No local state or session.

### Skill Generation
Packaged skill regeneration via `python3 agent-harness/skill_generator.py agent-harness`. The REPL startup banner exposes the packaged `SKILL.md` absolute path. Session state stored at `~/.config/cli-anything-{tool}/session.json`.

## Key Ideas
- Single unified pattern across all tool wrappers: discover → inspect → mutate
- Stateless subcommand mode vs. stateful REPL mode per harness
- Agent-safe by design: dry-run first, live verification on mutations, no undo gap is documented as a known risk

## Insights
- The framework turns any tool with an accessible API or config layer into an agent-addressable surface, extending the reach of [[Recursive Governance Protocol — Theseus, Auryn, Hopf|recursive governance]] beyond text artifacts into live tooling
- The Obsidian harness is particularly relevant: it could enable agent-driven note creation and graph traversal directly in this vault

## Open Questions
- Are the PM2 and MuseScore harnesses complete? (Raw sources reference them but their SOPs were not reviewed)
- Is any harness currently in active use, or are all in development?

## Sources
`raw sources/MUBU.md`, `OLLAMA.md`, `OBSIDIAN.md`, `OBS.md`, `OPENSCREEN.md`, `NOTEBOOKLM.md`

## Related

- [[README]]
- [[readme]]
- [[HISTORY]]
