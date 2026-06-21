# Obsidian Agent Vault

See also [[Manuscript Pipeline MOC]].
A structured knowledge layer for Claude Code and file-aware coding agents.

## Quick Start

1. Open this folder as a vault in Obsidian ("Open folder as vault").
2. Edit `CLAUDE.md` with your name, projects, stack, and preferences.
3. Drop a note in `raw/`, ask your agent to synthesize it into `wiki/`.
4. Confirm the wiki note links back to a hub note or MOC.

You're running.

## Structure

- `CLAUDE.md` — Agent reads this first. Standing context.
- `Home.md` — Human entry point. Links to everything.
- `raw/` — Incoming, unprocessed material.
- `wiki/` — Linked, durable knowledge. The retrieval layer.
- `skills/` — Reusable agent instructions.
- `archive/` — Done or retired.
- `templates/` — Hub-note templates.

## One Rule

A note without links is stored text, not usable memory. Always link back.

## License

Personal use. Team license available — contact consult@pharos-ai.ca.

Built with the PHAROS Method. pharos-ai.ca
