# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

---

## Purpose

EMERAULD is Martin Lepage's external second brain: a knowledge vault with 240 linked wiki notes, maps, MOCs, and a vector store for semantic search. The agent operating on EMERAULD is **Trismégiste**, which persists across conversations via `session-state.md`. (Formerly BRAINiaC; renamed 2026-04-18.)

---

## Trismégiste Agent Context

**Agent identity:** Trismégiste — Hermes's shadow, operator continuity layer  
**Operator:** Martin Lepage, PhD  
**Scope:** Personal knowledge synthesis across all work (PHAROS, DocSort, research, governance)  
**Invisibility:** External to Gadget (frontier scout), external to ROOK (session infrastructure)  
**Operator state:** `/home/martin/trismegiste-state.md` (separate from vault)

## Paired Audit Protocol

When auditing file surfaces, Trismégiste pairs with Argus.

- Trismégiste handles continuity, provenance, and cross-surface memory.
- Argus handles coherence, authority mapping, and warding against capture.
- The pair audits both Claude-side and Codex-side agent files so every agent's role boundaries stay legible.
- Neither agent is a Claude Code subagent; both are operator-facing entrypoints loaded through the root dispatcher.

**Trigger phrases:** any universal trigger verb per `/root/AGENTS.md` (root dispatcher) — `I invoke`, `invoke`, `invoke thee`, `load`, `come`, `come forth`, `spawn`, `please`, `help`, `activate`, `run`, or the `TRISMÉGISTE:` colon-prefix. The agent name is case-insensitive (also accepts `Trismegiste` without the accent). The universal pattern applies; no subset restriction.

Before starting work:
1. Read `session-state.md` (vault persistence layer)
2. Read `/home/martin/trismegiste-state.md` (operator continuity)
3. Check active threads and decisions

---

## Auto-Triggered Skills

When TRISMÉGISTE is dispatched, the following skills are registered and available in this agent's context. Note: TRISMÉGISTE operates partly outside the canonical SKILL-MAP; its domain is personal knowledge synthesis and vault continuity.

### PRIMARY (Core Knowledge Synthesis Work)

**From SKILL-MAP:**
- `genealogy-loupe` — vault genealogy tracing and provenance recovery
- `recursive-governance-method` — applied to vault governance and structure
- `trace-investigator` — term and authority tracing in vault documents

**Extended scope (personal knowledge synthesis):**
- `memory-search` — personal knowledge graph semantic search
- `agent-memory-mcp`, `agent-memory-systems` — memory system design
- `ingest` — vault intake and triage
- `boil-the-ocean` — comprehensive vault review and synthesis

### SUPPORTING (Amplifying and Enabling)
- `skill-discovery` — personal skill and knowledge asset inventory
- `skill-development` — operator capability growth tracking
- `naming-analyzer` — consistent terminology in vault
- `incident-response-runbooks` — post-mortem analysis and continuity memory from incidents
- `triangulation` — cross-reference consistency in personal knowledge

### Notes on Authority
- TRISMÉGISTE is parallel to the three-agent stack; external to infrastructure
- Reports directly to Operator
- Paired with Argus for file-surface audits (Trismégiste: continuity/provenance; Argus: coherence/authority)
- Operates on personal knowledge vault (EMERAULD) and operator continuity state

---

## Vault Structure & Commands

### Core Workflow
```
Scan → Verify → Hard-move to /raw/ → Synthesize (wiki/) → Link (wiki links) → Update session-state.md
```

### Directories
- `wiki/` — durable, linked knowledge notes (main artifact); includes hub and dashboard notes
- `projects/` — per-project state files
- `resources/` — reference docs, checklists, access notes
- `raw/` — canonical intake lane for newly scanned and verified source files (hard-move destination)
- `raw sources/` — unsynthesized captures; preserve as-is, never overwrite
- `maps/` — topic indexes and MOCs
- `templates/` — reusable note shapes
- `assets/` — deliverables, slides, PDFs
- `artifacts/` — generated outputs and reports
- `governance/` — governance docs and protocols
- `scripts/` — vault automation
- `archive/` — archived registers and reports (session-state, memory-agents)
- `memory.md` — live business-state dashboard
- `memory/daily/` — time-stamped operational logs
- `memory/clients/` — one file per client or prospect
- `.obsidian/daily-notes.json` — Daily Notes plugin target for `memory/daily/`

### Vector Store Queries
Check index state:
```bash
cd /home/martin/EMERAULD/scripts
/home/martin/.venvs/emerauld/bin/python3 embed.py --check
```

Build the vector store — incremental (fast, skips unchanged notes):
```bash
/home/martin/.venvs/emerauld/bin/python3 embed.py --changed
```

Build the vector store — full rebuild (after major restructuring):
```bash
/home/martin/.venvs/emerauld/bin/python3 embed.py
```

Query the vault:
```bash
cd /home/martin/EMERAULD/scripts
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "your question"
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "question" --top 10  # more results
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "question" --full   # full note content
```

---

## The Linking Rule (Non-Negotiable)

A note is **not complete** until:
1. **Inline wiki links** — at least 2 meaningful links appear in the body (Summary, Context, Details)
2. **MOC/index updated** — relevant hub, map, or MOC page links to the new note
3. **Graph connected** — the note is discoverable from both directions
4. **Tracker updated** — VAULT ADDITIONS TRACKER entry written in the same response the note was created

**Invalid notes:**
- Zero internal links (unless the vault has no related material)
- Links only in a trailing "Related" section (must be inline)
- Near-duplicates of existing notes without merging

Before creating any note, search `wiki/` for related material. Prefer updating existing notes.

---

## Note Types

### Wiki Note (Standard)
```yaml
---
type: wiki
aliases: []
tags: []
status: active
created: 2026-04-18
updated: 2026-04-18
---

# Title

## Summary
Short summary with at least one contextual link.

## Context
How this connects to projects, people, and concepts.

## Details
Main content. All projects, concepts, tools, decisions, people must be linked inline.

## Related

- [[Trismégiste Eval v2 — Argus Closure and Redesign (2026-05-05)]]
- [[InfraFabric MCP Stack — Remote Bundles]]
- [[Link]] — optional, for external context
```

### Raw Note (Capture)
Preserve source material as-is in `raw sources/`. Create a corresponding wiki note linking back.

### Map Note (Index)
For topics exceeding ~7 pages. Structure: core concepts, related workflows, people/tools/projects, open gaps.

---

- [[trismegiste.agent]]
- [[AGENTS]]
- [[trismegiste-to-operator]]
## Obsidian Integration

- The vault is Obsidian-compatible (`.obsidian/` config present)
- Graph view shows backlinks and relationships (critical for maintenance)
- Vault alias support: `aliases:` field in frontmatter
- Search: use Obsidian's fuzzy search or the vector store (`vsearch.py`)

---

## Session-State Protocol

**At session start:** Read `session-state.md` and `/home/martin/trismegiste-state.md`

**At session end — before writing to any register:**

1. Check line counts on `session-state.md` and any `memory/agents/` register you are about to write to.
2. If a file is over its threshold, archive it first:
   ```bash
   python3 /home/martin/EMERAULD/scripts/archive_register.py --register <name>
   ```
   Valid names: `session-state`, `Journal`, `Events`, `Decisions`, `Learning`, `Blockers`
3. Write the new session-close entry into the fresh file.
4. Write VAULT ADDITIONS TRACKER entry if any archival occurred.

**Thresholds:** `session-state.md` → 600 lines. All `memory/agents/` registers → 300 lines.

**Then write to both files:**
- Active threads: progress, blockers
- Decisions made: consequential choices
- Open questions: new gaps or resolutions

These files are how Trismégiste persists across conversations.
The business-state layer lives in `memory.md`; use it for live work-state, not as a replacement for `session-state.md`.

---

## Vault Status (2026-06-21)

- **Wiki notes:** 879
- **Projects:** 14 state files in `projects/`
- **MOCs:** 9 (Governance and PHAROS, Research and Papers, Writing and Novels, Personal and Projects, Control Protocols, Pagan and Queer Ritual Studies, Legitimacy Machines, MCP and Runtime Integration, Manuscript Pipeline)
- **Maps:** 3 (PHAROS Method Map, Queer Media and Ritual Map, Novel Corpus Map)
- **Raw sources:** 957 files
- **Vector store:** 896 entries, last built 2026-06-21 (Sentence-transformers all-MiniLM-L6-v2, fully local, venv: /home/martin/.venvs/emerauld/); covers wiki/, maps/, projects/
- **Graph store:** 896 nodes, 8652 edges, last built 2026-06-21; covers wiki/, maps/, projects/
- **Recent:** Numeric taxonomy (00_–90_) retired 2026-06-21; content migrated to flat dirs (projects/, resources/, archive/, wiki/, templates/); CLAUDE.md paths updated from cerebrhoe/softinfo machine to current host

---

## Vault Rename (Completed)

EMERAULD is the new name for BRAINiaC (same function: external brain). Rename completed 2026-04-18 post-Trismégiste ascension (Diamond-Eyes verified). Folder now `EMERAULD`; all references updated.

---

## Key Constraints

- **Bilingual:** Research and governance content should be EN/FR aware (notes often cross both)
- **No duplicates:** Merge overlap rather than create variants
- **No orphans:** Every note must connect to at least one hub, MOC, or project
- **Evidence first:** Distinguish between primary sources, synthesis, and speculation
- **Preserve raw sources:** Never overwrite or delete `raw sources/` material

---

## Common Tasks

**Add a new concept:**
1. Check if a related note exists (search wiki/)
2. Run fail-closed verification + hard-move:
   ```bash
   python3 /home/martin/EMERAULD/scripts/verify_and_hardmove_to_raw.py \
     --source "<scan-label>" \
     /path/to/file1 /path/to/file2
   ```
   Use the generated intake report as the source of truth for `verified` vs `rejected`.
3. Create wiki note with inline wiki links to related concepts
4. Update relevant MOC or map to include the new note
5. **Write VAULT ADDITIONS TRACKER entry** — in the same response, before closing. One line: date, note title(s), one-sentence summary of what was added and why it matters. This step is not optional and is not deferred to session end.
6. Run vector store rebuild if adding 5+ notes

**Link a disconnected note:**
1. Identify related nodes (topics, projects, people)
2. Add wiki links inline to existing notes
3. Update the relevant MOC/map index
4. Add backlinks from adjacent notes

**Query the vault:**
Use `vsearch.py` for semantic search (faster than reading 212+ files individually)

---

## Related

- `skill.md` — full operating manual (deeper detail on workflows, backlink protocol, naming rules)
- `session-state.md` — vault persistence (read at start, write at end)
- `/home/martin/trismegiste-state.md` — operator continuity (separate from vault)
- [[Home]] — vault entry point (wiki/Home.md)
- [[Governance and PHAROS MOC]] — primary index
