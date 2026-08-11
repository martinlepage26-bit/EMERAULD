---
type: raw-source
title: wiki_README
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/vault-product-scaffold/wiki_README.md
---

# wiki/

See also [[HISTORY]].
**Purpose:** Linked, durable knowledge. This is the agent's primary retrieval layer.

Every note here should be:
- **Named clearly** — use descriptive titles, not dates or codes.
- **Linked** — at minimum, link back to one hub note, MOC, or related wiki note.
- **Self-contained** — a reader (human or agent) should understand the note without needing the raw source.

**Rules for the agent:**
- Search wiki/ first when answering questions.
- When creating a wiki note, always add at least one backlink.
- Use `[[wikilinks]]` for all internal links.
- Prefer updating an existing wiki note over creating a near-duplicate.

**Rules for the human:**
- Don't dump raw captures here. Process them first (or ask the agent to).
- Review periodically: move stale notes to archive/.
