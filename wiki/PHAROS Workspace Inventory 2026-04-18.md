---
type: wiki
aliases: []
tags: [project-management, inventory, cleanup, shipping, workspace]
status: active
created: 2026-04-18
updated: 2026-04-28
---

# PHAROS Workspace Inventory 2026-04-18

## Summary

Full inventory of `C:\Users\softinfo` (and glance at D:\) produced by [[Claude Code Skill Corpus|Claude]], paired with a sequenced plan of action. Companion files: `pharos-inventory-2026-04-18.xlsx` and `PLAN-OF-ACTION-2026-04-18.md.docx`. Links to [[Master Project Tracker — 2026]] and [[Martin Lepage — Professional Profile|Martin's]] broader project landscape.

## Context

Produced in a session focused on answering: "what do I actually have, and what should I ship next?" The inventory maps the full disk state, the plan sequences four sessions. Paired with [[Rest and Consolidation Guide — Martin]] — the sprawl documented here is the specific failure pattern that guide addresses.

## Details

### Active projects (touched last 7 days)

| Project | Status | Next action |
|---|---|---|
| MARTIN-SITE | ACTIVE | **Ship next** — see ship criteria below |
| PHAROS-SUITE | ACTIVE | Security + deployability audit |
| pharos-api | ACTIVE | Inventory endpoints, secrets audit, confirm deploy target |
| PHAROS METHOD REPOSITORY | ACTIVE | Decide: canonical or working copy? |
| PHAROS_PAPERS_DB | ACTIVE | Consolidate with PAPERS_MASTER_CONSOLIDATED |
| PAPERS_MASTER_CONSOLIDATED | ACTIVE | Single source of truth for papers |
| Governess | ACTIVE | Decide scope: separate product or PHAROS sub-component? |
| EMERAULD | ACTIVE | Define shipping target or park |
| INTERNAL | ACTIVE | Keep — governance work |
| NEW AGATHA STRESS-TEST | ACTIVE | Read FAIL files — decide keep or park; 2026-04-28 root intake preserved two FAIL traces in [[AGATHA Failure Pack — Theseus Continuity Stress Test]] |

### Security flags (priority 1)

- `.env` — sitting at C:\Users\softinfo root
- `.cloudflare-govern-ai.env` — at root
- `set-cloudflare-e…bat` — audit for hardcoded secrets
- `.codex` — check for auth tokens

All at profile root = any backup captures secrets. Fix: move into owning project folder or Cloudflare env vars.

### Cleanup targets

- `~` folder (shell typo — delete)
- `__pycache__`, `node_modules`, `.venv` in home root
- `tmp/`, `output/`, `memory/`
- Abandoned home-root project: `package.json`, `requirements.txt`, `server.py`, `scan_and_upload.py`, `design_guidelines.json`, `README.md`
- Estimated recovery: 2–5 GB from caches alone

### Duplicate candidates

- AutoResearchClaw + autoresearch-master — same thing; merge or kill one
- PHAROS_PAPERS_DB + PAPERS_MASTER_CONSOLIDATED — likely redundant intent

### Drive roles (proposed)

| Drive | Proposed role |
|---|---|
| C: SSD | OS, active projects, active documents |
| D: BACKEND | Reference, model weights, archived projects, snapshots |
| E: MLONF3 | Unknown — scan before assigning role |
| G: Google Drive | Scan for orphan decks and proposals; pull what's relevant |
| H: SDHC | Check contents; decide keep or wipe |

### Ship next: MARTIN-SITE

Ship criteria (in order):
1. Triage MARTIN-SITE CHANGE TRACKER.md → must-ship / nice-to-ship / defer
2. Confirm build+deploy pipeline succeeds end to end
3. Secrets audit: all env vars in platform secret store only
4. Minimal security surface: HTTPS, no debug endpoints, form rate-limit
5. Write launch paragraph before deploy — not after

Everything else (pharos-api, PHAROS-SUITE, Governess, EMERAULD, Agatha) waits until the site is out.

### Four follow-up sessions

- **Session 2** (90 min): Ship MARTIN-SITE — triage tracker, close small items live, name blockers on medium items
- **Session 3** (60 min): Security + deploy audit — read .env files, identify and rotate secrets, document DEPLOY.md per project
- **Session 4** (45 min): Home-directory cleanup — specific move/delete list above
- **Session 5** (45 min): External-drive tiering — formalize C/D/E/G/H roles into a one-page map

### Do before next session (10 min)

1. Move `.env` out of home root into owning project (read it if you don't know which one)
2. Delete the `~` folder (typo artifact, safe)

## Later Vault Links

- [[Documents Root Loose Files Intake — 2026-04-28]] — follow-up intake of loose root Documents files flagged by this workspace-sprawl picture.
- [[Local Hardware and Discovery Snapshot — Laptop A]] — exact root-folder hardware/WSL discovery files preserved after the inventory.
- [[L99 PHAROS Migration Artifacts 2026-04-19]] — later hardening/migration bundle that operationalized part of the security and deployability agenda.
3. Read first/last 50 lines of AGATHA FAIL files — decide: keep or park

## Key Ideas

- Active work is concentrated: one line (PHAROS broadly) + two adjacent experiments
- The "too many projects" feeling is real but scoped — dormant count is high, active count is manageable
- Home root treated as workspace is the structural cause of the "what did I start" feeling

## Open Questions

- Governess: separate product or PHAROS sub-component? Needs a decision before Session 2
- E:\ MLONF3 contents unknown
- EMERAULD shipping target undefined

## Sources

- `raw sources/pharos-inventory-plan-2026-04-18.md`
- `pharos-inventory-2026-04-18.xlsx` (original at Downloads)
- `PLAN-OF-ACTION-2026-04-18.md.docx` (original at Downloads)

## Related

- [[Governance and PHAROS MOC]]
- [[Master Project Tracker — 2026]]
- [[Rest and Consolidation Guide — Martin]]
- [[Martin Lepage — Professional Profile]]
- [[PHAROS-SUITE]] (if note exists)
- [[Founder Charter — Lepage and Stocker]]

- [[README]]
## Archive Closeout Note

- 2026-04-20 21:35 EDT — Closeout: the AutoResearchClaw duplicate-candidate was resolved by removing the Windows-home copy (`/mnt/c/Users/softinfo/AutoResearchClaw`) into archive (`/home/cerebrhoe/_archive/Governess_empty_shell_backup/AutoResearchClaw`), and the Linux-side `document-organizer-app` working tree was archived from `/home/cerebrhoe/document-organizer-app` to `/home/cerebrhoe/_archive/document-organizer-app_2026-04-21` (see `/home/cerebrhoe/_archive/MANIFEST_2026-04-21.md`).
