---
type: wiki
title: Plugin Recommendations
aliases:
- Plugin Recommendations
tags:
- resources
- plugin-recommendations-md
- plugins
- obsidian
- templater
- install
- plugin
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: Resources
canonical_path: Resources/Plugin Recommendations.md
backlink_count: 14
backlinks:
- '[[Resources/Awesome Design Resources — Curated UI-UX Reference List]]'
- '[[Areas/PHAROS/CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]]'
- '[[Resources/ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]'
- '[[Areas/PHAROS/Governance Controls Integration Dashboard]]'
- '[[wiki/Home]]'
- '[[wiki/LightRAG — Graph-Based RAG System]]'
- '[[wiki/OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Launch Kit]]'
- '[[Areas/PHAROS/Obsidian Agent Vault — Setup Guide]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[wiki/RAG-Anything — Multimodal RAG Framework]]'
- '[[archive/session-state/session-state-001]]'
- '[[wiki/claude-mem — Persistent Memory Compression for Claude Code]]'
---

# Plugin Recommendations

Part of [[Home]].

## Summary
Community plugins that extend the vault's core capabilities. Install each one through the Obsidian UI: Settings → Community plugins → turn off Restricted mode if prompted → Browse → search by name → Install → Enable. This note is the canonical example flagged as Outlier 1 in [[OUTLIERS — Five Notes That Break the Architecture]] — the tool layer is *prerequisite* to governance and is governed (now) by [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]].

## Context
These plugins complement the core plugins already enabled in this vault and support the [[Master Project Tracker — 2026|ongoing work]] of building a connected, queryable knowledge system. Plugin determinism, dependency chains, and version drift are auditable concerns under [[Governance Controls Integration Dashboard|Layer 0.5]] and tie back into the [[ROOK — Session Boundary Model|ROOK]] session-boundary discipline.

## Details

The following plugins are recommended. None are installed automatically; each requires a manual install through the Obsidian interface.

### Query and structure

- **Dataview** (`dataview`) — Query your notes like a database. Write inline queries or full DataviewJS blocks to generate dynamic lists, tables, and task views from note metadata and frontmatter.

### Templating

- **Templater** (`templater-obsidian`) — Advanced templating beyond the built-in Templates plugin. Supports dynamic variables, JavaScript execution, file-creation hooks, and folder-specific templates. Works alongside `templates/Note Template.md` in this vault.

### Time and dates

- **Calendar** (`calendar`) — Visual calendar panel for daily notes. Provides a month view in the sidebar with dot indicators for days that have notes.
- **Natural Language Dates** (`nldates-obsidian`) — Type dates in plain English (e.g., "next Monday", "two weeks ago") and have them resolved to formatted date strings. Integrates with Templater and daily notes.

### Tags and metadata

- **Tag Wrangler** (`tag-wrangler`) — Manage and rename tags across the entire vault from the tag pane. Supports tag merging, aliasing, and bulk rename without breaking existing notes.

### Version control

- **Obsidian Git** (`obsidian-git`) — Version control for the vault using an existing local Git repository. Supports automatic commits on a timer, manual push/pull, and a source-control panel in the sidebar.

## How to install

1. Open Obsidian.
2. Go to Settings (gear icon) → Community plugins.
3. If Restricted mode is on, click "Turn off Restricted mode."
4. Click Browse.
5. Search for the plugin by name.
6. Click Install, then Enable.

## Sources
- Obsidian community plugins directory: https://obsidian.md/plugins
