---
type: archive
title: Retired subsystems — 2026-07-08
tags:
- archive
- retired-2026-07-08
status: archived
priority: low
created: '2026-07-08'
updated: '2026-07-08'
vault_area: archive
canonical_path: archive/retired-2026-07-08/README.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Retired subsystems — 2026-07-08

Retire-or-revive verdicts from the vault overhaul Phase 6 (see `governance/EMERAULD-OS-BUILD-ORDER.md`):

- **scheduler_memory/** — RETIRED. Superseded scheduler concept; its own state store (`.scheduler-state/`, moved here) shows a single `session_start` event ever logged, last scan 2026-04-26, zero references from any cron script or current skill. The live scheduling mechanism is martin's crontab → `scripts/scheduled/*.sh`.
- **agent_bus/** — RETIRED (runtime). Designed-never-activated inter-agent message bus: `messages.sqlite` untouched since creation 2026-05-24, no live process ever referenced it. The design remains documented in ~33 wiki notes; the design-record note at `Areas/PHAROS/Agent Bus — Design Record (Retired Runtime).md` is the canonical pointer target for those references. Live inter-agent coordination on this host runs through the tmux council and (hosted) if.blackboard.
