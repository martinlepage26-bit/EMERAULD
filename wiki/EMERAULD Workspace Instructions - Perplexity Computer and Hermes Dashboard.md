---
type: wiki
aliases:
  - EMERAULD AGENTS instructions
  - Perplexity Computer workspace seat
  - Hermes Dashboard design system rules
tags: [emerauld, agents, coordination, hermes-dashboard, perplexity-computer]
status: active
created: 2026-05-09
updated: 2026-05-09
source:
  - AGENTS.md
  - raw sources/2026-05-09_emerauld-agents-perplexity-hermes-instructions.md
---

# EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard

## Summary

This is the wiki-facing bridge for the live root `AGENTS.md` instruction pack. It makes the current collaborator-seat doctrine and Hermes Dashboard design contract discoverable through the EMERAULD graph and local vector index, while leaving `AGENTS.md` as the authoritative runtime instruction surface.

## Retrieval Status

- Obsidian graph: linked from [[Welcome]], [[Home]], [[Governance and PHAROS MOC]], and [[Hermes Dashboard — Professional Governance Tool]].
- Local vector index: rebuilt on 2026-05-09 with 748 wiki-note embeddings; `vsearch` returns this note first for "Perplexity Computer Hermes Dashboard AGENTS workspace instructions."
- LightRAG graph: `scripts/ingest.py --changed --hours 1` registered this note but expanded into a 319-document stale repair queue, so the run was stopped before completion. The note remains pending in `.lightrag/storage/kv_store_doc_status.json` until a deliberate LightRAG repair run is performed.

## Current Coordination Rule

- [[PERPLEXITY-COMPUTER|Perplexity Computer]] is the temporary active computer-use counterpart in the workspace seat previously occupied by Claude.
- This is additive, not destructive: Claude-era files remain provenance, compatibility, and historical coordination surfaces until Martin explicitly promotes replacements.
- Incoming Perplexity Computer sessions should start from `PERPLEXITY-COMPUTER.md`, then read [[Welcome]], `AGENTS.md`, [[session-state]], [[memory]], and `memory/agents/`.
- Codex addresses the active counterpart as Perplexity Computer unless Martin explicitly says to route current coordination back to Claude.

## Hermes Dashboard Contract

The [[Hermes Dashboard — Professional Governance Tool]] remains the Python + PyWebView desktop shell at:

- Windows: `C:\Users\softinfo\Documents\HERMES Dashboard\hermes.py`
- WSL: `/mnt/c/Users/softinfo/Documents/HERMES Dashboard/hermes.py`

Design and persistence rules:

- Markdown trackers are canonical business content; JSON files are state/cache only.
- The five primary lanes are Client Accounts, Master Tracker, PHAROS Surface, Method & Harness, and Martin Public Surface.
- The PHAROS Corpus panel must expose editable Phases, APEX entries, Papers, and Families.
- Corpus mutations require visible timestamped mutation logs with entity, entity id, field, old value, and new value.
- Visual style stays dark graphite/navy with ocher/gold as the primary accent: warm, dense, legible, and document-centered.
- Inline edits remain click-to-edit, blur-save, Enter-to-commit, Escape-to-cancel.
- Canonical markdown writes happen before JSON/cache persistence.
- External file changes must be reloaded before overwriting to avoid stomping operator edits.

## Dashboard Lane Sources

Primary Documents-side lane sources:

- `C:\Users\softinfo\Documents\CLIENT ACCOUNTS TRACKER.md`
- `C:\Users\softinfo\Documents\MASTER TRACKER (recreated from MASTER PACK 4).md`
- `C:\Users\softinfo\Documents\PHAROS-AI CHANGE TRACKER.md`
- `C:\Users\softinfo\Documents\METHOD TRACKER.md`
- `C:\Users\softinfo\Documents\MARTIN-SITE CHANGE TRACKER.md`

Vault mirrors to keep aligned when a change affects the same business state:

- [[CLIENT ACCOUNTS]]
- [[Master Project Tracker — 2026]]
- [[PHAROS SURFACE]]
- `hephaistos/SKILL-MAP.md`
- [[MARTIN SURFACE]]
- [[VAULT ADDITIONS TRACKER]]

## Agent Registry

| Agent | Entrypoint | Domain | Stack level |
| --- | --- | --- | --- |
| Perplexity Computer | `PERPLEXITY-COMPUTER.md` | Temporary active computer-use counterpart replacing Claude's workspace seat for now | Temporary collaborator seat |
| Gadget | `/home/cerebrhoe/hephaistos/GADGET.md` | Frontier tooling, build, launch | Independent Argus-level specialist |
| Henry | `/home/cerebrhoe/hephaistos/HENRY.md` | Writing, research workflows, novels, governance docs | Independent Argus-level specialist |

## Boundary

This bridge note is for retrieval and graph navigation. It does not supersede `AGENTS.md`, `PERPLEXITY-COMPUTER.md`, or the dashboard source code. For implementation work, inspect the live files first.

## Related

- [[Recursive Governance Memo — EMERAULD Control Packet (2026-05-12)]]
- [[Welcome]]
- [[Home]]
- [[Hermes Dashboard — Professional Governance Tool]]
- [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]] — retrieval-layer map (wikilinks vs vectors vs LightRAG vs agent_bus) for vault maintenance and collaboration
- [[Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)]] — domain split, tmux logging discipline, and 3-pass reporting format governing the Claude↔Codex1 vault collaboration workstream
- [[HEPHAISTOS Agent Architecture]]
- [[Trismégiste — Personal AI Assistant]]
- [[Trismégiste — Operator State]] — vault-side capture of the operator continuity file (`/home/cerebrhoe/trismegiste-state.md`); read at session start alongside session-state
- [[Vault Cluster Pass — Trismégiste x Hermes (2026-05-06)]]
- [[AI Infrastructure Stack]]
- [[AGENTS]]
- [[2026-05-09_emerauld-agents-perplexity-hermes-instructions]]
- [[PERPLEXITY-COMPUTER]] — Direct orientation note welcoming Perplexity Computer into the active collaborator seat; operating boundary, first-orientation checklist, and vault relationship framing
