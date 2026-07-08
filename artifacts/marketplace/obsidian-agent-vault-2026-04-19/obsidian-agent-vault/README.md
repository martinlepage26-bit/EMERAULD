---
type: artifact
title: Obsidian Agent Vault
tags:
- artifact
- agents
- artifacts
- marketplace
- scripts
- runtime
- optional
- guide
- local
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/README.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# Obsidian Agent Vault

A clean starter vault for people who want Claude Code, Cursor, Aider, and other file-aware agents to understand their work without rebuilding a full RAG stack.

This package now ships in two layers that live in one folder:

1. the vault itself, where durable memory lives
2. an optional local agent runtime for WSL, with a setup script, query CLI, and raw-note watcher

The point is still simple: stop re-explaining the same project every session. The difference is that buyers who want a local agent loop can start from the same folder instead of stitching one together later.

## Start Here

1. Open this folder in Obsidian with **Open folder as vault**.
2. Read `START_HERE.md`.
3. Edit `CLAUDE.md` with your name, projects, stack, and working preferences.
4. Create your first project hub from `templates/hub_project.md`.
5. Drop one real note into `raw/`, then ask your agent to run `skills/synthesis_prompt.md`.

If the result lands in `wiki/` with at least one backlink, the vault is working.

Optional:

- rename the guide names with `scripts/rename_guides.py`
- install the local runtime with `bash scripts/setup.sh`
- on Windows, launch the runtime console with `Launch_Agent.bat`

## What You Get

- `CLAUDE.md` - Caelir context guide for standing project memory.
- `Home.md` - human entry point.
- `START_HERE.md` - first 10-minute setup path.
- `raw/` - incoming, unprocessed material.
- `wiki/` - linked, durable knowledge.
- `skills/synthesis_prompt.md` - Ilyris synthesis guide for raw-to-wiki notes.
- `skills/link_guide.md` - Ariun link guide for backlink and map checks.
- `skills/archive_guide.md` - Mnara archive guide for source and provenance cleanup.
- `scripts/rename_guides.py` - optional guide-name customization script.
- `scripts/setup.sh` - optional WSL runtime installer.
- `scripts/ask.py` - terminal query CLI for the bundled runtime.
- `scripts/vault_watcher.py` - raw-note watcher that can auto-ingest to LightRAG.
- `services/README.md` - notes on the generated user services.
- `Launch_Agent.bat` - optional Windows launcher for the local runtime.
- `archive/` - completed, retired, or superseded material.
- `templates/` - hub-note templates for projects, people, concepts, decisions, and maps of content.

## Named Guides

The names are buyer-facing handles for four practical jobs:

- **Caelir** orients the agent from standing context.
- **Ilyris** turns raw material into linked wiki notes.
- **Ariun** checks backlinks, hubs, and maps of content.
- **Mnara** keeps raw sources, archive decisions, and provenance clean.

To personalize these names, run:

```bash
python scripts/rename_guides.py --context "North" --synthesis "Weaver" --link "Thread" --archive "Keeper"
```

## Optional Local Runtime

If you use WSL, the vault can also run as a local assistant shell:

- `bash scripts/setup.sh` creates `.venv`, `rag/`, and `mem/`
- `python3 scripts/ask.py "your question"` queries the local runtime
- `scripts/vault_watcher.py` can auto-ingest `raw/` notes into LightRAG

The runtime is optional. The vault still works as a file-native memory layer even if you never install it.

## What This Is Not

This is not automation magic, a managed database, or a replacement for judgment. It is a disciplined file structure that helps agents retrieve the right context and create notes that remain usable later.

## The Rule

A note without links is stored text, not memory. Link every durable note back to a project hub, person hub, concept hub, decision log, or map of content.

## License

Personal use for one buyer or one personal workspace. Team use requires a team license or written permission from the seller.

## Related

- [[Governance and PHAROS MOC]]
- [[START_HERE]]
