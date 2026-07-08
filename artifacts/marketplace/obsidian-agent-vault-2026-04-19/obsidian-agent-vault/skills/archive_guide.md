---
type: skill-spec
title: Mnara - Archive Guide
aliases:
- artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/skills/archive_guide
tags:
- skill
- agents
- archive
- skill-spec
- artifacts
- marketplace
- sensitive
- deleting
- processed
- deletion
- color-orange
status: active
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/skills/archive_guide.md
backlink_count: 3
backlinks:
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
- '[[artifacts/marketplace/promo/hashnode-iter34-skill-guides]]'
---

# Mnara - Archive Guide

## Purpose

Keep raw sources, archive decisions, and provenance clean after a note has been processed.

## When to Use

- A raw note has been synthesized into `wiki/`.
- The user asks what can be archived, kept, or deleted.
- A source contains sensitive details that should not be promoted into a durable note.

## Steps

1. **Identify** the raw source that produced the wiki note.
2. **Confirm** whether the wiki note preserves the source's meaning without exposing secrets, credentials, client data, or sensitive personal details.
3. **Recommend** one source action:
   - keep in `raw/` if the source is still active
   - move to `archive/` if the source has been processed
   - ask before deleting if no deletion policy exists
4. **Record** provenance in the wiki note when useful, using a short `Source` or `Related` section.
5. **Report** any sensitive material that should stay out of public, demo, or marketplace outputs.

## Output

A short archive decision:

- source file
- recommended action
- reason
- any sensitivity warning

## Rules

- Ask before deleting raw source material unless the user has already set a deletion policy.
- Do not expose secrets or private identifiers in a wiki note.
- Preserve raw evidence when the user may need auditability later.
- Keep archive actions reversible where possible.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
