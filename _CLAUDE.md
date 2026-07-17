# EMERAULD Vault — Second Brain Operating Rules

> This file is read by obsidian-second-brain before any vault operation.
> Full vault documentation lives in `CLAUDE.md`. Where this file is silent, defer to `CLAUDE.md`.

---

## Section 0 — AI-First Vault Rule

Every note Claude writes must be self-contained for future Claude:
- **"For future Claude" preamble** — 2-3 sentence summary at the top so relevance is assessable in 10 seconds
- **Rich frontmatter** — `type`, `aliases`, `tags`, `status`, `created`, `updated` (see format below)
- **Recency markers** — "X raised $24M (as of 2026-04, source-url)" so future Claude knows what to verify
- **Verbatim source quotes** — every external claim has a source URL inline
- **Wikilinks mandatory** — every person, project, concept, decision uses `[[wikilinks]]`; minimum 2 inline links per note (not just in Related section)
- **Confidence levels** — `stated | high | medium | speculation` where applicable

---

## Section 1 — Vault Path and Structure

**Vault root:** `/home/martin/EMERAULD`

**Primary note directory:** `wiki/` — all durable, linked knowledge notes go here (not vault root)

**Directory map:**
```
wiki/          ← main notes (all new notes default here)
maps/          ← MOCs and topic indexes (7+ page topics)
projects/      ← per-project state files
resources/     ← reference docs, checklists, access notes
raw/           ← verified source files after hard-move (immutable)
raw sources/   ← legacy provenance storage, preserve as-is, NEVER overwrite or delete; not the default destination for new scans
templates/     ← note templates
assets/        ← deliverables, slides, PDFs
artifacts/     ← generated outputs and reports
governance/    ← governance docs and protocols
memory/        ← daily logs (memory/daily/) and client files (memory/clients/)
archive/       ← archived registers
```

**When obsidian-second-brain says "save to vault root":** save to `wiki/` instead.
**When obsidian-second-brain says "save to raw/":** save to `raw/` (verified hard-move destination). Use `raw sources/` only for explicit legacy provenance overrides.
**Do not create new top-level directories** without updating `CLAUDE.md`.

---

## Section 2 — Note Format (overrides obsidian-second-brain defaults)

```yaml
---
type: wiki          # wiki | map | raw | project | resource | artifact
aliases: []
tags: []
status: active      # active | archived | draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Then body structure:

```markdown
> For future Claude: [2-3 sentence preamble — what this note is, why it matters, when to load it]

## Summary
Short summary with at least one contextual [[wikilink]].

## Context
How this connects to [[projects]], [[people]], and concepts.

## Details
Main content. All projects, concepts, tools, decisions, people must be linked inline.

## Related
- [[Note Name]]
```

**No `ai-first: true` field** — EMERAULD does not use that frontmatter key.
**Language:** bilingual EN/FR — research and governance content may be in either language.

---

## Section 3 — Linking Rules (non-negotiable)

A note is not complete until:
1. At least 2 meaningful inline wikilinks in the body (not just Related)
2. A relevant MOC or map in `maps/` links to the new note
3. VAULT ADDITIONS TRACKER entry written in the same response

Before creating any note, search `wiki/` for related material. Prefer updating existing notes over creating new ones.

---

## Section 4 — Raw Source Protection

- `raw sources/` — NEVER overwrite, delete, or modify. Preserve verbatim. Legacy provenance only, not the default new-scan destination.
- `raw/` — verified hard-moved files. Immutable after move.
- When `/obsidian-ingest` processes a URL or file: save the verified source to `raw/`; use `raw sources/` only for explicit legacy provenance overrides, then rewrite or create the wiki note in `wiki/`.

---

## Section 5 — Self-Rewriting Rules

When updating existing notes:
- **Bi-temporal facts**: never delete old values; add to `timeline:` frontmatter array
- **Contradictions**: flag with `> [!warning] Contradiction detected` callout, then reconcile
- **Append vs rewrite**: rewrite the Summary and Details sections; append to Related and timeline
- **No orphans**: every updated note must still satisfy the linking rule above

---

## Section 6 — Existing Agents

- **Trismégiste** — primary vault agent; handles continuity via `session-state.md` and `/home/martin/trismegiste-state.md`
- **Argus** — paired audit agent for file-surface coherence checks
- obsidian-second-brain commands operate **alongside** Trismégiste, not as a replacement

---

## Section 7 — Vector Search

EMERAULD has a local Python vector store. Do not attempt to install QMD or external semantic search.

```bash
# Query:
cd /home/martin/EMERAULD/scripts
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "your question"
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "question" --top 10
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "question" --full

# Rebuild after 5+ new notes:
/home/martin/.venvs/emerauld/bin/python3 embed.py --changed
```

---

## Section 8 — VAULT ADDITIONS TRACKER

Every time a note is created or significantly updated, write one line to `_vault/VAULT ADDITIONS TRACKER.md`:
```
YYYY-MM-DD | [[Note Title]] | one-sentence summary of what was added and why it matters
```

## Related

- [[EMERAULD]]
- [[Home]]
