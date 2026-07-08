---
type: index
title: EMERAULD Vault Index
aliases:
- vault-index
- index
tags:
- index
- vault-doc
- ai-first-true
- index-md
- projects
- fisher
- king
- bases
- progress
- color-purple
status: active
created: '2026-06-29'
updated: '2026-06-26'
vault_area: index.md
canonical_path: index.md
backlink_count: 1
backlinks:
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

> For future Claude: Master catalog of all EMERAULD vault sections. Read this first when navigating the vault — it is cheaper and faster than listing directories. Regenerate with `/obsidian-init`. Vault has 575+ wiki notes; this index lists hubs, MOCs, and structural files, not every individual note. Use [[Areas/PHAROS/Governance and PHAROS MOC]], [[Areas/Writing/Research and Papers MOC]], and [[wiki/Personal and Projects MOC]] as topic entry points. Use `vsearch.py` for semantic search across all 575+ wiki notes.

# EMERAULD Vault Index

*Generated 2026-06-29 by /obsidian-init. Vault root: `/home/martin/EMERAULD`.*

---

## Top-Level Files

| File | Purpose |
|------|---------|
| [[Welcome]] | Vault entry point; main MOC links |
| [[CLAUDE]] | Trismégiste agent context; vault structure; vector search commands |
| [[_CLAUDE]] | obsidian-second-brain operating rules (overrides skill defaults) |
| [[memory]] | Live business-state dashboard (PHAROS, clients, priorities) |
| [[session-state]] | Trismégiste continuity layer; active threads; read at session start |
| [[log]] | Vault operations log pointer → Logs/ |
| Projects Dashboard.base | Kanban view of all projects by status (6 pipeline columns) |

---

## Projects — `/projects/`

Fisher King project state files. Each has: Status, Core Question, Blockers, Next Synthesis Move.

| Project | Status |
|---------|--------|
| [[projects/AurorA — Fisher King Project State\|AurorA]] | in-progress |
| [[projects/COMPASSai — Fisher King Project State\|COMPASSai]] | in-progress |
| [[projects/Echo — Fisher King Project State\|Echo]] | in-progress |
| [[projects/GAIA — Fisher King Project State\|GAIA]] | in-progress |
| [[projects/HELIX — Fisher King Project State\|HELIX]] | in-progress |
| [[projects/LOTUS — Fisher King Project State\|LOTUS]] | in-progress |
| [[projects/PHAROS — Fisher King Project State\|PHAROS]] | in-progress |
| [[projects/Papers — Fisher King Project State\|Papers]] | in-progress |
| [[projects/Scripto — Fisher King Project State\|Scripto]] | in-progress |
| [[projects/Second Brain — Fisher King Project State\|Second Brain]] | in-progress |
| [[projects/Second Self — Fisher King Project State\|Second Self]] | in-progress |
| [[projects/Glitching the Sacred — Fisher King Project State\|Glitching the Sacred]] | in-progress |
| [[projects/Stuttering Machines — Fisher King Project State\|Stuttering Machines]] | in-progress |
| [[projects/Dr. Sort — Fisher King Project State\|Dr. Sort]] | on-ice |
| [[projects/Magie sanguine — Fisher King Project State\|Magie sanguine]] | on-ice |
| [[projects/DOMAIN]] | Canonical status vocabulary and project note schema |

See also: [[Bases/Projects.base]] · [[wiki/Fisher King Hub — Project Recovery Map]] · [[wiki/Master Project Tracker — 2026]]

---

## Areas — `/Areas/`

Permanent responsibilities with no end date. Use for scope boundaries.

| Area | Scope |
|------|-------|
| [[Areas/PHAROS/AREA]] | Products, clients, public presence, PHAROS operations |
| [[Areas/Lavoie/AREA]] | Groupe Lavoie client — gates A1–A5, Patricia relay |
| [[Areas/Writing/AREA]] | Active writing: novel, thesis-book, RDAIG, HEXA, SPP paper |
| [[Areas/Personal/AREA]] | Health, finances, relationships, spiritual practice |

---

## Maps — `/maps/`

Topic indexes for subjects with 7+ linked notes.

- [[maps/Governance and PHAROS MOC\|Governance and PHAROS MOC]] — primary commercial and product index; AI governance, PHAROS products
- [[maps/Research and Papers MOC\|Research and Papers MOC]] — academic paper pipeline, literature, publication track
- [[maps/Novel Corpus Map\|Novel Corpus Map]] — The Broken Frequency of the Word; writing archaeology
- [[maps/Queer Media and Ritual Map\|Queer Media and Ritual Map]] — pagan, queer embodiment, ritual studies
- [[maps/PHAROS Method Map\|PHAROS Method Map]] — PHAROS methodology; RECURSO, RDAIG, DAST

See also wiki MOCs: [[Areas/Writing/Writing and Novels MOC]] · [[wiki/Personal and Projects MOC]] · [[Areas/PHAROS/Control Protocols MOC]] · [[wiki/Legitimacy Machines MOC]] · [[Areas/PHAROS/MCP and Runtime Integration MOC]] · [[Areas/Writing/Manuscript Pipeline MOC]] · [[Areas/Writing/Pagan and Queer Ritual Studies MOC]]

---

## Wiki — `/wiki/` (575 notes)

All durable linked knowledge notes. Too numerous to list individually — use entry points:

### Navigation hubs
- [[Areas/PHAROS/Governance and PHAROS MOC]] — AI governance, PHAROS products, commercial strategy
- [[Areas/Writing/Research and Papers MOC]] — papers, academic pipeline, publication track
- [[Areas/Writing/Writing and Novels MOC]] — fiction, thesis-book, creative work
- [[wiki/Personal and Projects MOC]] — personal life, project recovery (Fisher King)
- [[wiki/Fisher King Hub — Project Recovery Map]] — cross-project state map
- [[wiki/Projects Hub]] — active projects navigation
- [[wiki/Research Hub]] — research and papers entry point
- [[wiki/Master Project Tracker — 2026]] — live tracker for all 2026 projects

### Architecture notes (written 2026-06-29)
- [[wiki/Architecture - EMERAULD Scripts - Overview]] — Mermaid module map; 8 core + 12 support modules
- [[wiki/Architecture - EMERAULD Scripts - Knowledge Layers]] — 3 retrieval layers (vector/LightRAG/wikilink)
- [[wiki/Architecture - EMERAULD Scripts - Intake Pipeline]] — raw → wiki flow; WSL bug documented
- [[wiki/Architecture - EMERAULD Scripts - Key Decisions]] — 6 ADRs; open tech debt table

### Idea discovery
- [[wiki/2026-06-29 - idea-discovery]] — 5 ranked candidates; #1 Gumroad (executed), #2 HELIX outreach, #3 GAIA launch

### Search
```bash
cd /home/martin/EMERAULD/scripts
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "your question"
```

---

## Memory — `/memory/`

### Daily logs — `/memory/daily/`
One file per active session day. See [[Bases/Daily.base]] for calendar view.

Recent: 2026-06-22 through 2026-06-29 (active run)

### Agent registers — `/memory/agents/`

| Register | Purpose | Last entry |
|----------|---------|-----------|
| [[memory/agents/Decisions]] | Consequential decisions; council choices | 2026-06-29 (backfill + today) |
| [[memory/agents/Blockers]] | Active blockers across all projects | ~2026-05-13 (stale — needs backfill) |
| [[memory/agents/Events]] | External events; milestones | ~2026-05-13 (stale) |
| [[memory/agents/Learning]] | Technical and conceptual learning | ~2026-05-13 (stale) |
| [[memory/agents/Journal]] | Cross-agent continuity | ~2026-05-13 (stale) |

### Business dashboard
- [[memory]] — live PHAROS state; client status; priorities (dated 2026-05-01 — needs update)

### Client files — `/memory/clients/`
- `Lavoie Construct.md` — April 2026 excavation SOP client (NOT Groupe Lavoie)
- `Lavoie.md` — Groupe Lavoie client file (SOS Plomberie, Excavations Lavoie, GVI)
- ⚠️ Disambiguation needed: two Lavoie entities. See [[Areas/Lavoie/AREA]] for Groupe Lavoie.

---

## Artifacts — `/artifacts/`

Generated outputs and reports.

- [[artifacts/emerge-pattern-report-2026-06-29]] — 9 structural patterns; PHAROS launch gap; blocker analysis
- `artifacts/marketplace/` — Gumroad listing copy, social posts, marketplace assets

---

## Assets — `/assets/`

Deliverables, PDFs, product zips.

- `obsidian-agent-vault-2026-06-29.zip` — Clean Gumroad upload zip (28K, 37 files) ← **use this one**
- `Obsidian_Agent_Vault_Setup_Guide.pdf` — Setup guide PDF
- `CLAUDE_md_Before_After.pdf` — Before/After demonstration PDF
- `Obsidian_Agent_Vault_Demo.pptx` — Demo deck

---

## Bases — `/Bases/` (new 2026-06-29)

Obsidian Bases database views.

| Base | Queries | Folder |
|------|---------|--------|
| [[Bases/Projects.base\|Projects]] | in-progress / blocked / on-ice / complete / all | `projects/` |
| [[Bases/People.base\|People]] | all notes with `type: person` | `wiki/` |
| [[Bases/Daily.base\|Daily]] | recent + calendar | `memory/daily/` |
| [[Bases/Wiki.base\|Wiki]] | by type / recent / all | `wiki/` |
| Projects Dashboard.base (root) | kanban by status (6 columns) | `projects/` |

---

## Templates — `/templates/`

- `Wiki Note Template.md` / `Wiki Note.md` — standard wiki note shape
- `Memory Daily Template.md` — daily log template
- `Weekly Review Template.md` — weekly review format
- `Note Template.md` — general note
- `Raw Capture Template.md` — raw source capture
- `Recursive Governance Packet Header.md` — RECURSO/governance note header
- `Admissibility Delta Block.md` — evidence delta block for governance notes
- `Invoice Template Pharos-AI.md` / `.html` — client invoicing

---

## Vault Meta — `/_vault/`

- [[_vault/VAULT ADDITIONS TRACKER]] — append-only log of every note created or significantly updated
- `_vault/AGENTS.md` — agent roster and authority map
- `_vault/VAULT-PRODUCTION-MANIFEST.md` — canonical vault content manifest
- `_vault/skill.md` — vault-level skill definitions

---

## Logs — `/Logs/` (new 2026-06-29)

Per-day vault operations log. See [[log]] for structure and action vocabulary.

- [[Logs/2026-06-29]] — init; obsidian-os-ai; emerge; architect; idea-discovery; Gumroad execution; obsidian-init

---

## Inbox — `/Inbox/`

Routing triage for new captures. See [[Inbox/README]] for decision tree.

---

## Resources — `/Resources/`

New reference notes go here (not `wiki/`). `wiki/` is frozen legacy.

- [[Resources/ROUTING]] — declares wiki/ as frozen; routing rules for new notes

---

## Scripts — `/scripts/`

Local Python automation. See [[wiki/Architecture - EMERAULD Scripts - Overview]] for full module map.

Key commands:
```bash
# Vector search
/home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/vsearch.py "query"

# Rebuild vector store (after 5+ new notes)
/home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/embed.py --changed

# Archive register (if over threshold)
/home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/archive_register.py --register <name>
```

---

*Regenerate this index: run `/obsidian-init` in Claude Code.*

<!-- BEGIN STATS - generated by vault_stats.py -->
_Generated by `scripts/vault_stats.py` on 2026-07-05._

- **Total notes**: 2168
- **Projects**: 20 (13 in-progress, 5 active, 2 on-ice)
- **People**: 0 (-)
- **Ideas**: 0 (-)
- **Tasks**: 0 (-)
- **Research**: 0 (-)
- **Knowledge**: 0
- **Dev Logs**: 0
- **Operation logs**: 1 day(s)

_Latest activity per folder: .agent_bus (2026-06-26), .graph_store (2026-06-26), .planning (2026-06-26), 00_PROJECT_CONTROL (2026-06-26), 01-deploy-config (2026-06-26), 01-lightrag-script-runtime-hardening (2026-06-26), 01_RAW_MATERIALS (2026-06-26), 02-pipeline-triage (2026-06-26), 02_SOURCE_FIELD (2026-06-26), 03-pr4-hardening (2026-06-26), 03_OUTLINE_AND_ABSTRACT (2026-06-26), 04_RESEARCH_BUNDLE (2026-06-26), 05_SECTION_DRAFTS (2026-06-26), 06_VALIDATION (2026-06-26), 07_FINAL_OUTPUTS (2026-06-26), 2026-05-13 (2026-06-26), 2026-06-30 (2026-06-26), 2026-07-01 (2026-06-26), BOOKS (2026-06-26), EMERAULD (2026-06-26), HELIX-hermes-assisted-prospect-extension-2026-05-06 (2026-05-05), HELIX-potential-clients-2026-05-06 (2026-05-05), HELIX-regional-prospect-deep-sweep-2026-05-06 (2026-05-05), Inbox (2026-06-26), Lavoie (2026-06-26), Lazy Obsidian Method (2026-06-26), Logs (2026-06-29), PEER-REVIEW (2026-06-26), PHAROS (2026-06-26), PHAROS Invention Disclosure Bundle Sources 2026-04-25 (2026-06-26), Personal (2026-06-26), Resources (2026-06-26), Rivard2026 (2026-06-26), Writing (2026-06-26), _manifest (2026-06-26), _vault (2026-07-03), adr (2026-07-03), agents (2026-07-02), archive (2026-06-26), archive_files (2026-06-26), artifacts (2026-07-04), assets (2026-06-26), bridges (2026-06-26), clients (2026-06-26), consolidation-records (2026-06-26), content-inventory-cartographer (2026-06-26), converted (2026-06-26), daily (2026-07-04), demand-scout (2026-06-26), docs (2026-06-26), drive-audit-2026-04-18 (2026-06-26), elemental-agents (2026-06-26), examples (2026-06-26), figma-mcp-server (2026-06-26), genealogy (2026-06-26), global (2026-06-26), governance (2026-06-26), graph (2026-07-02), graph-retrieval-cartographer (2026-06-26), graphify-out (2026-06-26), hephaistos (2026-07-03), indexes (2026-07-02), intake-triager (2026-06-26), listing-creative-director (2026-06-26), local-session (2026-06-26), manuscript (2026-06-26), maps (2026-06-26), marketplace-dispatcher (2026-06-26), metadata-link-warden (2026-06-26), obsidian-agent-vault (2026-06-26), obsidian-agent-vault-2026-04-19 (2026-06-26), offer-pricing-architect (2026-06-26), personal-assistant-agents (2026-06-26), projects (2026-06-26), promo (2026-06-26), raw sources (2026-05-05), raw-archivist (2026-06-26), reddit-drafts (2026-06-26), resources (2026-06-26), rights-policy-warden (2026-06-26), scripts (2026-06-26), services (2026-06-26), session-state (2026-06-26), skills (2026-06-26), source_uploads (2026-06-26), synthesis-editor (2026-06-26), trismegiste (2026-06-26), ttrpg-repack (2026-06-26), validation (2026-06-26), vault (2026-06-26), wiki (2026-07-05)_
<!-- END STATS -->
