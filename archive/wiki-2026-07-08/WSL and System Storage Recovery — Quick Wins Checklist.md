---
type: wiki
title: WSL and System Storage Recovery — Quick Wins Checklist
aliases:
- WSL Storage Recovery
- Disk Space Quick Wins
- vhdx compaction
tags:
- archive
- cache
- vhdx
- venvs
- compaction
- lightrag
- wiki
- wiki-2026-07-08
status: active
created: '2026-05-31'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/WSL and System Storage Recovery — Quick Wins Checklist.md
backlink_count: 8
backlinks:
- '[[wiki/Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)]]'
- '[[wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# WSL and System Storage Recovery — Quick Wins Checklist

## Summary

A disk-space recovery checklist for the WSL/Windows development environment, identifying 40–50GB of recoverable space. Priority order: WSL vhdx compaction (biggest lever, ~30–40GB), lightrag venv deletion (8GB), npm cache (7GB+), pip/apt cache (7GB), stale nvm versions (5GB), and orphan scratch directories (~11GB). Raw source was a session output from a storage analysis run.

## Context

Generated during an operator infrastructure session on `/home/cerebrhoe`. The storage pressure on this machine affects Codex agent performance and vault tooling (the lightrag venv at `~/.venvs/lightrag` was a blocker for vector search). Relevant to the open item in [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]] about setting up `/home/martin/.venvs/emerauld` for vector search.

## Details

**Recovery actions by priority:**

1. **WSL vhdx compaction** (PowerShell admin, ~30–40GB):
   ```powershell
   wsl --shutdown
   Optimize-VHD -Path "C:\Users\softinfo\AppData\Local\wsl\{426eedaf-...}\ext4.vhdx" -Mode Full
   ```
2. **~/.venvs/lightrag** (8GB) — delete if not active; replace with `/home/martin/.venvs/emerauld`
3. **npm cache** (7GB): `npm cache clean --force && rm -rf ~/.npm/_npx ~/.npm/_cacache`
4. **pip/apt cache** (7GB): `sudo apt-get clean && rm -rf ~/.cache/pip`
5. **nvm old versions** (5GB): `nvm ls` then `nvm uninstall <old-version>`
6. **Stale scratch dirs** (~11GB, review before deleting): `worktrees`, `voice11`, `visuals`, `vibe-kanban-main`, `staging`, `test-results`, `tmp`, `tasks`, `root-docs`, `snap`

**Note:** Do the vhdx compaction first — it is the only action that returns space to Windows.

## Related

- [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]
- [[Codex–Claude Collaboration Protocol — EMERAULD Vault (2026-05-25)]]
- [[AI Infrastructure Stack]]
