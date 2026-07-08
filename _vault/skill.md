---
type: skill-spec
title: 'SKILL: Ask Vault Build Mode (Obsidian Lightweight RAG)'
aliases:
- _vault/skill
tags:
- skill
- skill-spec
- vault
- skill-md
- pages
- obsidian
- retrieval
- lightweight
- aliases
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: _vault
canonical_path: _vault/skill.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Obsidian Agent Vault — Launch Kit]]'
- '[[wiki/Workspace Cleanup Ledger — 2026-05-31]]'
- '[[wiki/archive/Orphan Index — Root Loose Notes — 2026-05-06]]'
name: ask-vault
description: 'How to use an Obsidian vault as a lightweight retrieval system for LLM
  and coding-agent workflows. Use this skill whenever you are working inside an Obsidian
  vault — ingesting raw notes, converting captures into wiki pages, adding backlinks,
  building topic maps or index notes, preparing the vault so another agent can retrieve
  from it, or doing any kind of knowledge organization inside a vault. Trigger this
  skill even if the user doesn''t say "RAG" or "retrieval" — if they ask you to add
  notes to Obsidian, process raw material, build a knowledge base, or maintain a second
  brain, this skill applies. Do not skip this skill because the task seems simple;
  even a single note should follow the linking protocol.

  '
---

# SKILL: Ask Vault Build Mode (Obsidian Lightweight RAG)

## Purpose

Use this skill to make an Obsidian vault function like a lightweight retrieval system for coding agents and long-horizon knowledge work. The goal is not to build a full production RAG stack. The goal is to create a disciplined vault structure that gives a practical, high-quality retrieval layer for most personal and small-team use cases.

This skill treats the vault as a structured knowledge environment:
- `raw/` stores incoming, unsynthesized material
- `wiki/` stores cleaned, linked, queryable knowledge pages
- backlinks, cross-links, and index pages turn separate notes into a navigable graph

The agent must not dump information into the vault without linking it. Unlinked notes weaken the system.

---

## When to use

Use this skill when:
- ingesting new source material into an Obsidian vault
- converting raw notes into durable knowledge pages
- updating wiki pages from raw material
- creating backlinks and related-note links
- building topic maps, index notes, or lightweight knowledge graphs
- preparing a vault so another LLM or coding agent can retrieve from it effectively

Do not use this skill for:
- large-scale enterprise retrieval across millions of files
- sensitive data workflows that require dedicated security controls
- cases where the user explicitly wants flat storage without synthesis or linking

---

## Core principle

A vault becomes useful as retrieval infrastructure when the agent does three things consistently:

1. Captures source material in a stable place.
2. Converts source material into structured notes.
3. Links each note into the surrounding network.

The third step is mandatory. A note without links is stored text, not usable memory.

---

## Required vault structure

Use or create this structure unless the user already has a preferred layout:

```text
Vault/
  raw/
    inbox/
    captured/
    transcripts/
    web-clips/
    docs/
  wiki/
    concepts/
    people/
    projects/
    tools/
    workflows/
    summaries/
    indexes/
  maps/
  templates/
  assets/
  archive/
```

### Folder roles

- `raw/`: unsynthesized material; preserve source fidelity.
- `wiki/`: cleaned and reusable knowledge pages written for retrieval.
- `maps/`: higher-order notes that organize clusters of pages.
- `templates/`: reusable note templates.
- `assets/`: images, PDFs, attachments.
- `archive/`: deprecated or superseded material.

If the vault already contains an established folder system, adapt to it rather than forcing a rewrite.

---

## Operating rules

### 1) Never leave important notes orphaned
Every durable note must include:
- at least 2 internal links where possible
- 1 parent or index link
- 1 related-note section

If only one real connection exists, state that clearly and add a `Needs Links` marker.

### 2) Preserve raw material separately
Do not overwrite source notes with summaries. Raw notes are evidence. Wiki notes are interpretation and organization.

### 3) Prefer synthesis over duplication
When new raw material overlaps an existing wiki page:
- update the existing page
- add new evidence or examples
- avoid making near-duplicate pages

### 4) Write for future retrieval
Wiki pages must be scannable by both humans and models. Favor:
- explicit titles
- stable terminology
- short sections
- concrete aliases
- direct internal links

### 5) Make relationships explicit
Do not assume similarity is discoverable from text alone. Add links for:
- prerequisite concepts
- contrasting concepts
- upstream/downstream workflows
- people-to-project relationships
- tool-to-use-case relationships

### 6) Use maps sparingly but deliberately
Create map notes when a topic exceeds roughly 7-10 related pages or starts splitting into subdomains.

---

## Ingestion workflow

### Phase 1: Capture into `raw/`
When new information arrives:
1. Save it in the most appropriate `raw/` subfolder.
2. Preserve provenance when known.
3. Use a clear filename.
4. Add minimal frontmatter if useful.

Example filename patterns:
- `2026-04-14_youtube-obsidian-rag-notes.md`
- `2026-04-14_karpathy-obsidian-post.md`
- `meeting_transcript_project-x_2026-04-14.md`

Optional frontmatter for raw notes:

```yaml
---
type: raw
source: youtube
status: unsynthesized
tags: [raw, obsidian, rag]
created: 2026-04-14
---
```

### Phase 2: Synthesize into `wiki/`
For each meaningful raw note, create or update a wiki page that:
- names the concept clearly
- explains what it is
- states why it matters
- links to related pages
- points back to the source raw note

A wiki page is not a transcript. It is a durable retrieval object.

### Phase 3: Link into the graph
After writing or updating a wiki page:
- add links to relevant existing notes
- update at least one index or map note
- add backlinks from adjacent notes when appropriate
- mark unresolved relationships for later review

---

## Backlink protocol

Backlinks are not optional decoration. They are part of the retrieval system.

Whenever you create or modify a wiki note, inspect the vault for:
- broader parent topics
- sibling concepts
- specific examples
- tools or workflows mentioned
- projects that use the concept

Then add explicit links.

### Minimum linking standard for a new wiki note
A new wiki note should usually include:
- `Part of:` or `Index:` link
- `Related:` links to sibling notes
- `Source:` link to one or more raw notes
- `See also:` section

Example:

```md
## Related

- [[manual]]
- [[Obsidian as Lightweight RAG]]
- [[Knowledge Graphs]]
- [[Map of Content]]
- [[Agentic Coding Workflows]]

- [[Governance and PHAROS MOC]]
- [[Obsidian Agent Vault — Launch Kit]]
## Source
- [[2026-04-14_karpathy-obsidian-post]]
```

### Reverse-link expectation
When a new page materially relates to an existing important page, also update the existing page to point back when appropriate. Linking should not run in only one direction.

---

## Note types

### Raw note
Use for direct captures.

Template:

```md
---
type: raw
source: 
status: unsynthesized
tags: []
created: 
---

# Title

## Summary

## Full capture

## Extraction candidates
- 
- 
```

### Wiki note
Use for durable knowledge.

Template:

```md
---
type: wiki
aliases: []
tags: []
status: active
created: 
updated: 
---

# Title

## What this is

## Why it matters

## How it works

## Related
- 

## See also
- 

## Source
- 
```

### Map note
Use for higher-order navigation.

Template:

```md
---
type: map
tags: [index, map]
created: 
updated: 
---

# Topic Map

## Core concepts
- 

## Related workflows
- 

## People / tools / projects
- 

## Open gaps
- 
```

---

## Naming rules

Use names that support retrieval.

Prefer:
- explicit nouns
- stable topic names
- one concept per note when possible
- aliases for variant phrasings

Prefer `Obsidian as Lightweight RAG` over vague titles like `Thoughts on setup`.

When a term has common alternate names, include aliases:

```yaml
aliases:
  - Obsidian RAG
  - Vault as retrieval
  - lightweight knowledge graph
```

---

## Agent behavior requirements

When operating in the vault, the agent must:

1. Read nearby notes before creating a new permanent page.
2. Merge into existing pages when overlap is high.
3. Add links before considering a task complete.
4. Prefer updating indexes over scattering standalone pages.
5. Flag uncertain connections instead of inventing them.
6. Preserve source/raw notes as evidence.
7. Leave short, useful summaries rather than bloated prose.

The agent must not:
- create many near-duplicate wiki pages
- dump large raw transcripts into `wiki/`
- create notes with no parent/index relationship
- rely on tags alone instead of links
- replace specific filenames with vague ones

---

## Retrieval-oriented writing rules

To make notes easy for LLMs and humans to query:
- put the governing claim near the top
- define the concept in the first section
- separate mechanism from implication
- use specific nouns instead of vague pronouns
- keep paragraphs short
- include concrete examples where useful

Each wiki page should answer, quickly:
- what is this?
- what problem does it solve?
- what does it connect to?
- where did it come from?

---

## Maintenance loop

On each pass through the vault, do the following:

### Daily or per session
- process recent raw notes
- update 1-3 relevant wiki pages
- repair orphaned notes

### Weekly
- review `Needs Links`
- merge duplicates
- update major map notes
- archive stale or superseded pages

### Periodically
- normalize naming conventions
- add aliases to commonly queried notes
- split overloaded pages into cleaner subpages

---

## Quality bar

A vault page is retrieval-ready when:
- the title is specific
- the note has a clear function
- the note points to source material
- the note links into the surrounding graph
- another agent could find and use it without guessing context

A vault page is not retrieval-ready when:
- it is an isolated fragment
- it mixes raw capture and interpretation chaotically
- it has no related notes
- it duplicates an existing page without adding structure

---

## Example transformation

### Raw input
`raw/transcripts/2026-04-14_youtube-obsidian-rag-notes.md`

Contains notes about using Obsidian as a practical substitute for a full RAG stack.

### Wiki output
`wiki/workflows/Obsidian as Lightweight RAG.md`

Possible structure:

```md
# Obsidian as Lightweight RAG

## What this is
A practical pattern for using an Obsidian vault as a retrieval layer for LLM or coding-agent workflows.

## Why it matters
This approach gives many users most of the value of a traditional RAG system without the infrastructure overhead.

## How it works
Raw material enters a vault through `raw/`. The agent then converts selected material into linked wiki pages. Those links create a navigable graph that improves retrieval quality.

## Related
- [[Knowledge Graphs]]
- [[Agentic Coding Workflows]]
- [[Map of Content]]

## Source
- [[2026-04-14_youtube-obsidian-rag-notes]]
```

Then update:
- `maps/Knowledge Systems Map.md`
- any existing page on `Obsidian`
- any page on `RAG`

---

## Completion checklist

Before ending a vault-writing task, confirm:
- Was the raw material stored correctly?
- Was a wiki page created or updated?
- Were at least 2 meaningful internal links added?
- Was a parent/index/map note updated?
- Was source provenance preserved?
- Were duplicates avoided?

If the answer to any of these is no, the task is incomplete.

---

## One-line rule

Do not just store notes. Convert notes into linked retrieval objects.
