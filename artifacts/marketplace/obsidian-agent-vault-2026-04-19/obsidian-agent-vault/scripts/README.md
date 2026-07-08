---
type: artifact
title: scripts/
aliases:
- artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/scripts/README
tags:
- artifact
- agents
- artifacts
- marketplace
- bash
- rename
- scripts
- guide
- python
- color-orange
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/scripts/README.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# scripts/

This folder contains two kinds of tools:

1. vault customization
2. optional local runtime helpers

## Rename Guide Names

Use `rename_guides.py` if you want different names for the four guide roles.

Show the current names:

```bash
python scripts/rename_guides.py --show
```

Preview a rename:

```bash
python scripts/rename_guides.py --context "North" --synthesis "Weaver" --link "Thread" --archive "Keeper" --dry-run
```

Apply a rename:

```bash
python scripts/rename_guides.py --context "North" --synthesis "Weaver" --link "Thread" --archive "Keeper"
```

The script changes visible names only:

- **Caelir** - context guide
- **Ilyris** - synthesis guide
- **Ariun** - link guide
- **Mnara** - archive guide

File names stay stable so prompts and links keep working.

## Optional Local Runtime

If you use WSL, the vault can also act as a local assistant root.

Install the runtime:

```bash
bash scripts/setup.sh
```

Ask a question from the terminal:

```bash
python3 scripts/ask.py "What are my active projects?"
```

Watch `raw/` and auto-ingest to LightRAG:

```bash
python3 scripts/vault_watcher.py --vault . --lightrag-url http://localhost:9621
```

What each file does:

- `setup.sh` - installs the local runtime into this same folder
- `ask.py` - queries LightRAG or falls back to vault-only search
- `vault_watcher.py` - watches `raw/` and sends new notes to LightRAG

## Related

- [[Research and Papers MOC]]
- [[START_HERE]]
