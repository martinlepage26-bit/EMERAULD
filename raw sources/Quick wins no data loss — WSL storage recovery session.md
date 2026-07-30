---
type: source
aliases: []
tags: [raw-source, orphan-repair]
status: raw
created: 2026-07-10
updated: 2026-07-10
source: "Quick wins no data loss — WSL storage recovery session"
---

  1. Compact the WSL vhdx — this is the biggest lever (~30-40GB potentially recoverable). Run in PowerShell as admin:
  wsl --shutdown
  Optimize-VHD -Path "C:\Users\softinfo\AppData\Local\wsl\{426eedaf-ac29-4a33-9dfe-488cdae71271}\ext4.vhdx" -Mode Full

  2. Clear npm cache — 7GB, safe to delete:
  npm cache clean --force

  3. Clear pip/apt cache:
  sudo apt-get clean
  rm -rf ~/.cache/pip

  4. Prune .nvm — 5G; you likely only need 1-2 node versions:
  nvm ls  # see what's installed
  nvm uninstall <old-version>

  5. Review .venvs/lightrag — 8G for one venv. If it's not actively used, delete it.

  6. Prune .npm/_npx — 4G of cached one-off npx runs, safe to clear:
  rm -rf ~/.npm/_npx ~/.npm/_cacache

  Do the vhdx compaction first — that's the only thing that actually gives space back to Windows.

✻ Cogitated for 39m 55s · 9 shells still running

● Background command "cerebrhoe home top dirs by size" completed (exit code 0)

● Background command "cerebrhoe home sizes with awk conversion" completed (exit code 0)

● Additional 1G directories confirmed from the completed scan — adding to the picture:

  /home/cerebrhoe/ has another ~11G spread across small dirs:
  - worktrees, voice11, visuals, vibe-kanban-main, tools, tmp, test-results, tasks, staging, snap, root-docs, 模板 — all
   ~1G each

  These are likely stale project clones and scratch directories. Worth a sweep:

  # Quick review before deleting anything
  du -sh ~/worktrees ~/voice11 ~/visuals ~/vibe-kanban-main ~/staging ~/test-results ~/tmp ~/tasks ~/root-docs ~/snap
  2>/dev/null | sort -rh

  None of those names look like active primary repos — voice11, vibe-kanban-main, staging especially look like abandoned
   experiments. But confirm before deleting.

  Priority order for recovery:

  1. wsl --shutdown + Optimize-VHD (PowerShell admin) — biggest lever, compacts the vhdx itself
  2. ~/.venvs/lightrag (8G) — delete if not active
  3. npm cache clean --force + rm -rf ~/.npm/_npx ~/.npm/_cacache (7G+)
  4. ~/.cache cleanup (7G) — rm -rf ~/.cache/pip ~/.cache/ms-playwright ~/.cache/yarn selectively
  5. Prune stale 1G dirs above after review (~11G)
  6. nvm uninstall old Node versions (5G total)

  That's realistically 40-50GB recoverable without touching anything critical.


---
## Backlinks
Provenance artifact de-orphaned via graph repair (frontmatter + backlinks added 2026-07-10). Original content preserved above, unaltered.

- Indexed in: [[Home]]
