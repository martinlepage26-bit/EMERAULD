---
type: skill-spec
title: Ilyris - Synthesis Guide
tags:
- skill
- agents
- skill-spec
- artifacts
- marketplace
- synthesize
- update
- editorialize
- exists
- lighter
status: active
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/skills/synthesis_prompt.md
backlink_count: 3
backlinks:
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Ilyris - Synthesis Guide

## Purpose

Convert an unprocessed note from `raw/` into a clean, linked wiki note in `wiki/`.

## When to Use

- A new note has been dropped into `raw/`.
- The user asks you to "synthesize," "process," or "clean up" a raw note.
- You find relevant raw material while answering a question and it should be promoted.

## Steps

1. **Read** the raw note carefully. Identify: key facts, decisions, action items, people, projects, and open questions.
2. **Check wiki/** for existing notes on the same topic. If one exists, update it rather than creating a duplicate.
3. **Create** or update a wiki note in `wiki/` with:
   - A clear, descriptive title (not a date or filename).
   - A brief context section explaining what this is about.
   - Extracted key points, decisions, or action items.
   - At least one `[[backlink]]` to a hub note, MOC, or related wiki page.
4. **Link** the new wiki note from the relevant hub note or MOC (update the hub if needed).
5. **Move** the raw note to `archive/` or delete it. Ask the user which they prefer the first time.

## Output

A wiki note in `wiki/` that is self-contained, linked, and retrievable. The raw/ folder should be one note lighter.

## Rules

- Never leave the wiki note unlinked. If no hub note exists yet, create one from the closest template in `templates/`.
- Preserve the raw note's original meaning. Synthesize, don't editorialize.
- Use `[[wikilinks]]` for all internal references.
- If the raw note references a person, check if a person hub exists. If not, note it as an open action.
- If the raw note contains secrets, credentials, private client details, or sensitive personal data, stop and ask before promoting it into wiki/.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
