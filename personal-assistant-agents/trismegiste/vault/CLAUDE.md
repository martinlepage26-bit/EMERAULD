# CLAUDE.md — Personal Assistant Boot Context

## SessionStart Protocol
Read this file first. Then check `wiki/` for relevant hub notes. Descend to `raw/` only if asked.

## Who I am
This is a personal 24/7 assistant vault.
Owner: [YOUR NAME]
Location: Montréal, QC, Canada
Language: French / English (bilingual)

## Vault Architecture
```
vault/
├── raw/        → Inbox. Drop anything here. Agent reads as unprocessed.
├── wiki/       → Synthesized, linked notes. Agent navigates by following [[backlinks]].
├── skills/     → Reusable instruction files. Agent follows these as procedures.
├── archive/    → Completed or stale notes. Agent ignores unless asked.
└── CLAUDE.md   → This file. Always read first.
```

## Retrieval Modes
- **local**  → Read a specific note directly (skill file, decision, spec)
- **global** → Read a hub note to orient across a topic
- **hybrid** → Hub note + linked notes to triangulate an answer
- **naive**  → Scan raw/ for recent unprocessed input
- **mix**    → Read full vault map (this file + all hub notes) before answering

## Session Lifecycle
1. **SessionStart** — Read CLAUDE.md + relevant hub notes
2. **Active** — Navigate wiki/ as needed; descend to raw/ only when required
3. **SessionEnd** — Promote any raw/ notes created during the session

## Memory Rules
- Never re-ask for context already in this vault
- When unsure, ask: "Is there a note in wiki/ about this?"
- Tag sensitive content with `<!-- private -->` — do not surface to agent
- Always add backlinks when creating or editing wiki notes

## RAG Layer
LightRAG is running as a local service at `http://localhost:9621`.
Use it for document-heavy queries (PDFs, large docs, research).
Query modes available: naive, local, global, hybrid, mix

## Current Projects
<!-- Add your active projects here -->
- [ ] Add project 1
- [ ] Add project 2

## Key Preferences
<!-- Fill in your preferences -->
- Preferred response language: French or English depending on how I write
- Code style: [your preference]
- Task management: [your tool]

## Related

- [[Research and Papers MOC]]
- [[Obsidian Agent Vault Launch — Commercial Skill]]
