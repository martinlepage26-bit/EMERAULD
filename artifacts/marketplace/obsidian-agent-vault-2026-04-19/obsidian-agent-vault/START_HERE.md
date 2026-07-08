---
type: artifact
title: START HERE
aliases:
- artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/START_HERE
tags:
- artifact
- agents
- artifacts
- marketplace
- finished
- optional
- rename
- runtime
- guide
- color-orange
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/START_HERE.md
backlink_count: 3
backlinks:
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/Home]]'
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/README]]'
- '[[artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/scripts/README]]'
---

# START HERE

Use this file first. The vault works when your agent knows where context lives and where finished knowledge belongs.

## The First 10 Minutes

1. Open `CLAUDE.md` - Caelir, the context guide.
2. Replace the placeholders under **Who**, **Active Projects**, **Stack / Tools**, and **Preferences**.
3. Optional: run `python scripts/rename_guides.py --show` if you want to rename the guide names before using the vault.
4. Open `templates/hub_project.md`.
5. Duplicate it into `wiki/` and rename it for your real project.
6. Put one messy note into `raw/`.
7. Ask your agent:

```text
Read CLAUDE.md, then use skills/synthesis_prompt.md to turn raw/_example_raw_note.md into a linked wiki note. Show me the note and the backlink you added.
```

Optional second pass:

```text
Now read skills/link_guide.md and skills/archive_guide.md. Check whether the new wiki note is properly linked and whether the raw source should be archived.
```

Replace `_example_raw_note.md` with your own raw note when you are ready.

## What Success Looks Like

- The raw note is understood, not just copied.
- The finished note is in `wiki/`.
- The finished note links to a hub note or another wiki note.
- `Home.md` or a map of content can lead a future agent back to it.

## Optional Runtime Setup

If you want the bundled local agent runtime:

1. Open WSL in this folder.
2. Run `bash scripts/setup.sh`.
3. After setup, use `python3 scripts/ask.py "your question"`.
4. On Windows, you can use `Launch_Agent.bat` to open a runtime shell in the right folder.

The runtime is optional. The vault remains useful even if you skip it.

## Keep It Human

Do not try to organize everything on day one. Put messy material in `raw/`, promote only what matters into `wiki/`, and keep links honest. The vault should reduce repeated explanation, not become a second job.

## Related

- [[README]]
- [[product_CLAUDE]]
