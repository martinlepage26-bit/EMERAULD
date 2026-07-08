---
type: agent-instructions
title: Memory Context
aliases:
- Memory Context
- _vault/AGENTS
tags:
- agents
- agent-instructions
- vault
- agents-md
- perplexity
- computer
- hermes
- softinfo
- tracker
- color-orange
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: _vault
canonical_path: _vault/AGENTS.md
backlink_count: 8
backlinks:
- '[[CLAUDE]]'
- '[[wiki/EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Research and Papers MOC]]'
- '[[wiki/Workspace Cleanup Ledger — 2026-05-31]]'
- '[[wiki/archive/Orphan Index — Post Dr Sort Rename Residuals — 2026-05-06]]'
- '[[governance/governance-index]]'
- '[[governance/hephaistos/HEPHAISTOS]]'
---

<!-- Durable Codex/Claude/Perplexity Computer workspace instructions for /mnt/c/Users/softinfo/Documents/EMERAULD. Promoted 2026-05-06; Perplexity seat noted 2026-05-08. -->

<claude-mem-context>
# Memory Context

# $CMEM EMERAULD 2026-04-25 7:44am EDT

No previous sessions found.
</claude-mem-context>

## Temporary Perplexity Computer Seat

- As of 2026-05-08, Martin has welcomed Perplexity Computer as the temporary active counterpart in the workspace seat previously occupied by Claude.
- This is additive, not a purge: Claude-era files remain provenance, compatibility, and historical coordination surfaces until Martin explicitly promotes replacements.
- Perplexity Computer should start from `PERPLEXITY-COMPUTER.md`, then read `Welcome.md`, `AGENTS.md`, `session-state.md`, `memory.md`, and `memory/agents/`.
- Codex should address the temporary counterpart as Perplexity Computer for current coordination unless Martin explicitly says to use Claude.

## Knowledge Scan Default (Locked 2026-05-12)

- When Martin asks to scan for new knowledge, agents run the full chain:
  1. scan broadly for new material,
  2. verify first (integrity, readability, provenance, duplicate check),
  3. hard-move verified source artifacts into `/raw/`,
  4. write or update wiki notes from verified sources,
  5. link into relevant MOCs and adjacent notes,
  6. report output split as `verified` vs `inferred`.
- `/raw/` is now the default intake lane for newly scanned source files.
- `raw sources/` and `raw\ sources/` remain legacy provenance lanes; do not delete historical content, but do not use them as default destination for new scan runs unless Martin explicitly asks.
- Fail-closed hardening:
  - no wiki synthesis from unverified artifacts,
  - duplicates are excluded from hard-move by default and reported,
  - every scan run must emit a verification report with `verified` and `rejected` lists.
- Canonical enforcement tool: `/mnt/c/users/softinfo/documents/emerauld/scripts/verify_and_hardmove_to_raw.py`.

## Hermes Dashboard Design System Rules

### Scope and source of truth
- Hermes Dashboard is the Python + PyWebView desktop shell at `C:\Users\softinfo\Documents\HERMES Dashboard\hermes.py` (WSL: `/mnt/c/Users/softinfo/Documents/HERMES Dashboard/hermes.py`).
- Markdown trackers are the canonical business content. JSON files are state/cache only.
- Do not confuse the dashboard surface with the Hermes agent role in `hephaistos/agents/hermes.md`.

### Canonical lanes
- The five primary lanes are: Client Accounts, Master Tracker, PHAROS Surface, Method & Harness, and Martin Public Surface.
- Legacy builds may still label the master lane as `Umbrella Control`; treat that as the same lane as `Master Tracker`, not a separate surface.
- Keep those five lanes visible as the main workbench. If `Vault Additions` is retained, treat it as auxiliary and do not let it displace a primary lane.
- Preserve tracker file names on disk; user-facing labels may be cleaner than legacy filenames, but the filesystem paths stay stable.
- Primary lane sources:
  - `C:\Users\softinfo\Documents\CLIENT ACCOUNTS TRACKER.md`
  - `C:\Users\softinfo\Documents\MASTER TRACKER (recreated from MASTER PACK 4).md`
  - `C:\Users\softinfo\Documents\PHAROS-AI CHANGE TRACKER.md`
  - `C:\Users\softinfo\Documents\METHOD TRACKER.md`
  - `C:\Users\softinfo\Documents\MARTIN-SITE CHANGE TRACKER.md`
- Vault mirrors to keep aligned when relevant:
  - `CLIENT ACCOUNTS.md`
  - `wiki/Master Project Tracker — 2026.md`
  - `PHAROS SURFACE.md`
  - `hephaistos/SKILL-MAP.md`
  - `MARTIN SURFACE.md`
  - `VAULT ADDITIONS TRACKER.md`

### Corpus panel
- The PHAROS Corpus panel must expose editable Phases, APEX entries, Papers, and Families.
- Keep `pharos_hermes_sync.json` and any `pharos_corpus_edited_*.json` fallback aligned with the UI schema.
- Every corpus mutation must be logged with timestamp, entity, entity id, field, old value, and new value.
- Do not silently rewrite family or paper relationships; make the change visible in the panel and in the mutation log.

### Visual system
- Use a dark graphite/navy shell with ocher/gold as the primary accent. Keep the UI warm, not neon, and do not default to purple-brand gradients.
- Prefer layered document surfaces: sidebar, content pane, workbench cards, and compact metadata bars.
- Keep tracker rows dense but legible. Use uppercase labels for metadata, normal case for content, and monospace only for ids, paths, counts, and timestamps.
- Keep the boot mark and HERMES identity stable unless the design brief explicitly says to rebrand.
- On narrow screens, collapse gracefully, but keep the five primary lanes discoverable without turning the dashboard into a hamburger-only app.

### Editing and persistence
- Inline edits must stay click-to-edit, blur-save, Enter-to-commit, Escape-to-cancel.
- Checkbox completion changes may be optimistic in the UI, but the markdown source must be updated in the background and then reloaded from disk.
- Write canonical markdown content first; JSON persistence follows the file, not the other way around.
- If a file changes externally, reload before overwriting so the dashboard does not stomp operator edits.
- Keep open-file and open-folder actions available from each lane.

### Figma-to-code workflow
- For every Figma-driven change, fetch the design context and screenshot first. If the node is large, inspect metadata before pulling the exact node subset you need.
- Translate the design into the app's current stack: PyWebView plus embedded HTML/CSS/JS in `hermes.py`. Do not replace that stack with a different framework unless the task explicitly calls for a rewrite.
- Reuse the existing lane-card, corpus-section, sidebar-nav, mutation-log, and progress-ring patterns before inventing new components.
- Validate the result against the design reference and against live markdown/JSON save behavior before marking the work complete.

### Bundling and assets
- Any new UI asset must be added to `HERMES.spec` and verified in the frozen EXE.
- Prefer the existing Winged Boot asset or built-in emoji over adding a new icon package.
- Keep the source script and the packaged build behavior aligned when changing layout, assets, or window sizing.

### Project-specific conventions
- Keep the Hermes Dashboard, the EMERAULD vault mirrors, and the PHAROS/Martin trackers in sync when a change affects the same underlying business state.
- `memory.md` is the vault-side business mirror; it is related context, not the desktop app's source of truth.
- Hermes routes and monitors approved work. It does not override HEPHAISTOS scope decisions or Queen Keyport governance constraints.

## Agent Registry

| Agent | File | Domain | Stack level |
|-------|------|---------|-------------|
| Perplexity Computer | `PERPLEXITY-COMPUTER.md` | Temporary active computer-use counterpart replacing Claude's workspace seat for now | Temporary collaborator seat |
| Gadget | `/home/cerebrhoe/hephaistos/GADGET.md` | Frontier tooling, build, launch | Independent (Argus-level specialist) |
| Henry | `/home/cerebrhoe/hephaistos/HENRY.md` | All writing, research workflows, novels, governance docs | Independent (Argus-level specialist) |

## Related

- [[2026-05-09_emerauld-agents-perplexity-hermes-instructions]]
- [[Research and Papers MOC]]
- [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]
