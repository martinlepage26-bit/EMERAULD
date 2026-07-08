---
type: artifact
title: services/
aliases:
- artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/services/README
tags:
- artifact
- agents
- artifacts
- marketplace
- systemctl
- watcher
- user
- lightrag
- journalctl
- color-orange
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/obsidian-agent-vault/services/README.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# services/

See also [[Manuscript Pipeline MOC]].
This folder documents the optional local runtime services.

When you run:

```bash
bash scripts/setup.sh
```

the installer writes two user services into `~/.config/systemd/user/`:

- `lightrag.service`
- `vault-watcher.service`

Those generated service files use the absolute path of your local vault folder, which is why they are created at install time instead of being shipped as fixed files here.

Common commands:

```bash
systemctl --user status lightrag vault-watcher
systemctl --user restart lightrag vault-watcher
journalctl --user -u lightrag -f
journalctl --user -u vault-watcher -f
```

If you are using WSL and `systemctl --user` is unavailable, enable systemd first, then rerun setup.
