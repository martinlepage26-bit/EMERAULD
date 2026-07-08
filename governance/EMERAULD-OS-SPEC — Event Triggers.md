---
type: governance-doc
title: EMERAULD-OS-SPEC — Event Triggers
tags:
- governance-doc
- emerauld-os
- spec
- event-triggers
- governance
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/EMERAULD-OS-SPEC — Event Triggers.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[EMERAULD_OS_ARCHITECTURE]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[governance/EMERAULD-OS-BUILD-ORDER]]'
---

# OS Spec — Event-Driven Triggers (gaps 2 + 9)

> [!success] Executed 2026-07-08 (operator directive)
> The recommended option is live: systemd **user** path unit `emerauld-inbox.path` (PathModified on Inbox/) → oneshot `emerauld-inbox.service` → `scripts/scheduled/inbox-route.sh` (flock-guarded, haiku-tier headless routing pass, durable logs, FAILURES.md surfacing, 2-strike manual-review loop protection). Linger enabled for martin, so the watcher survives logout/reboot. **Exit criterion met twice:** the standing MCP smoke-test note and a fresh capture were both routed autonomously — normalized to vault schema, ≥2 verified wikilinks, tracker lines, no human step. Implementation finding worth keeping: `PathModified` is edge-triggered and loses events that arrive while the service is running — the first capture was stranded exactly this way — so the script drains up to 5 eligible files per invocation instead of relying on re-triggering. Ledger: RELAY-20260708-003.

> For future Claude: the OS currently acts only on cron ticks (4 daily/weekly one-shots). This spec chooses how the vault gains "note arrives → agent reacts" behavior. Build in Stage 3 of [[governance/EMERAULD-OS-BUILD-ORDER|the build order]].

## Options assessed (2026-07-08)

| Option | Verdict |
|---|---|
| **systemd path unit watching `Inbox/` → oneshot service running a headless routing pass** | **RECOMMENDED.** Native to this host (systemd already runs the legipro/contremaitre timers), no daemon to babysit, debounce via `StartLimitIntervalSec`, logs journald + `Logs/scheduled/`. |
| Launch Kit `vault_watcher.py` (from the Gumroad product zip) | Assessed, rejected for production: a polling file-watcher designed as a teaching artifact for buyers; would add a persistent Python process without service supervision. Its debounce/ignore patterns are worth porting into the systemd service's routing script. |
| Persistent agent daemon (long-running Claude session) | Rejected for now: cost, drift, and supervision burden; revisit only if sub-minute reaction time ever matters. |
| Cron tightening (e.g. every 15 min Inbox sweep) | Fallback if systemd path units prove awkward; simplest possible, higher latency. |

## Behavior contract for the routing pass

- Trigger: new/changed file in `Inbox/` (`status: inbox` or no frontmatter).
- Action: headless `claude -p` pass that routes per `_CLAUDE.md` §1 (PARA map + Inbox/README decision tree), stamps schema frontmatter, writes ≥2 wikilinks + MOC link + tracker line, moves the file.
- Guardrails: never touches raw lanes; never deletes; failures append to `Logs/scheduled/FAILURES.md`; one file per invocation (queue drains across firings — no unbounded batch).

## Exit criterion

Drop a markdown capture in `Inbox/` → within minutes it sits in the right PARA folder, fully schematized and linked, with a tracker line — no human step.

## Related

- [[governance/EMERAULD-OS-BUILD-ORDER|EMERAULD OS Build Order]]
- [[Areas/PHAROS/Obsidian Agent Vault — Launch Kit]]
