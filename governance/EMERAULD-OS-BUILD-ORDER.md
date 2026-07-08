---
type: governance-doc
title: EMERAULD-OS-BUILD-ORDER
aliases:
- EMERAULD OS Build Order
tags:
- governance-doc
- emerauld-os
- build-order
- agentic-os
- governance
status: active
domain: governance
priority: high
created: '2026-07-08'
updated: '2026-07-08'
vault_area: governance
canonical_path: governance/EMERAULD-OS-BUILD-ORDER.md
backlink_count: 7
backlinks:
- '[[Areas/PHAROS/Agent Bus — Design Record (Retired Runtime)]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[EMERAULD_OS_ARCHITECTURE]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[governance/EMERAULD-OS-SPEC — Event Triggers]]'
- '[[governance/EMERAULD-OS-SPEC — Governance Wiring]]'
- '[[governance/EMERAULD-OS-SPEC — MCP Surface]]'
---

# EMERAULD OS Build Order — 2026-07-08

> For future Claude: this is the master build order for turning EMERAULD into a closed-loop agentic OS — agents autonomously reading, writing, filing, and advancing work in the vault. It sequences the 9 closed-loop gaps identified by the 2026-07-08 infrastructure survey, records which are already closed, and specs the rest. Architecture substrate: [[EMERAULD_OS_ARCHITECTURE|EMERAULD Operating System]] (4 pillars). Build discipline: [[Areas/PHAROS/STANDARD-BUILD-ORDER — Binding Build Discipline|STANDARD-BUILD-ORDER]] — every build turn ends with a handoff doc, and an empty next-decision means abandoned, not paused.

## Where the OS stands after the 2026-07-08 overhaul

The four pillars are now real, not aspirational:

1. **Storage (PARA)** — executed. 485 notes routed into Areas/{PHAROS,Writing,Personal,Lavoie}/, Resources/, archive/ ([[_vault/PARA-MIGRATION-MANIFEST-2026-07-08|manifest]]). `_CLAUDE.md` §1 carries the routing map.
2. **Structured data (frontmatter)** — executed. Unified 13-key schema vault-wide, zero missing frontmatter, zero YAML failures, type vocabulary normalized so Bases filters actually select (Daily 32/32, projects exactly the 16 index notes), `updated:` semantics restored (preserved unless content changes; the 2026-06-26 saturation bug is dead at the root — dynamic date + updated-preservation in `scripts/enrich_frontmatter_backlinks.py`).
3. **Brain (graph as domain)** — corpus unified. `embed.py` + `build_wikilink_graph.py` now index all PARA dirs (previously blind to Areas/, Resources/, memory/, governance/, archive/, PEER-REVIEW/, Publications/). Three graph layers with declared roles (below).
4. **Vision (Bases)** — filters repaired; verification dependency documented (below).

The autonomous layer already running: martin's crontab → `scripts/scheduled/{morning,nightly,weekly,health-check}.sh`, each a stateless headless `claude -p` pass. As of 2026-07-08 these write durable dated logs to `Logs/scheduled/`, surface failures to `Logs/scheduled/FAILURES.md`, run deterministic register archival before the nightly model pass, and scan PARA scope instead of wiki/-only.

## The 9 gaps — status and sequence

| # | Gap | Status | Where |
|---|---|---|---|
| 1 | Detection→remediation link | **CLOSED 2026-07-08** (session-state auto-archive in nightly.sh; contradiction workflow spec below) | scripts/scheduled/nightly.sh |
| 2 | Event-driven trigger / persistent process | SPEC — build next | [[governance/EMERAULD-OS-SPEC — Event Triggers|Event Triggers spec]] |
| 3 | Governance stack wired to execution | SPEC | [[governance/EMERAULD-OS-SPEC — Governance Wiring|Governance Wiring spec]] |
| 4 | Graph unification + refresh cadence | **CLOSED 2026-07-08** (corpus extension) + cadence rule below | scripts/embed.py, scripts/build_wikilink_graph.py |
| 5 | scheduler_memory + .agent_bus retire-or-revive | **CLOSED 2026-07-08** — both RETIRED | archive/retired-2026-07-08/ + [[Areas/PHAROS/Agent Bus — Design Record (Retired Runtime)|design record]] |
| 6 | MCP/API surface for the vault | **CLOSED 2026-07-08** (server registered + live-verified, exit criterion met; local scope, global after 1 clean week) | [[governance/EMERAULD-OS-SPEC — MCP Surface|MCP Surface spec]] |
| 7 | Cron monitoring/alerting | **CLOSED 2026-07-08** (durable logs + FAILURES.md + health-check reads it) | scripts/scheduled/*.sh |
| 8 | Bases verification dependency | DOCUMENTED below | this doc |
| 9 | Shared watch-vault-react primitive | SPEC (folded into gap 2) | Event Triggers spec |

## Build sequence (what to do, in order)

**Stage 1 — prove the closed loop (done 2026-07-08).** Cron pauses lifted at overhaul close; first post-overhaul morning run must show a sane stale scan. Success metric: no FAILURES.md entries and no re-saturation for 7 days.

**Stage 2 — MCP surface. DONE 2026-07-08.** Vendored server wired per the MCP spec; raw-lane write guard added and verified; exit criterion met by a headless MCP-only second surface (RELAY-20260708-001). Remaining follow-through: promote registration local → global after ~1 week of clean use.

**Stage 3 — event triggers (1-2 sessions).** Implement the chosen option from the Event Triggers spec (recommended: systemd path-unit watcher over Inbox/ driving a headless routing pass). Exit: a file dropped in Inbox/ gets routed to the correct PARA folder with schema frontmatter within minutes, no human in the loop.

**Stage 4 — governance wiring (2-3 sessions).** Implement the Governance Wiring spec's minimal path: scope-classified task intake, Hephaistos+Queen-Keyport clearance artifacts as machine-readable frontmatter, Hermes routing recorded in RELAY-LEDGER. Exit: one real task flows end-to-end with ledger entries written by the pipeline, not by hand.

**Stage 5 — self-measurement.** Weekly review gains an OS-health section: FAILURES.md count, orphan count, unresolved-link delta, register line counts, contradiction flags open/closed. The OS reports on itself; Argus audits the reports.

## Standing rules established by this overhaul

- **Graph refresh cadence (gap 4):** nightly pass already runs `embed.py --changed`; weekly run adds `build_wikilink_graph.py --no-vector-paths`; graphify-out refresh stays manual/on-demand. Layer roles: `.graph_store/` = canonical link graph; `graphify-out/` = semantic reference graph; `graph/` = hand-curated operational ontology. When a doc cites "the graph," it must name the layer.
- **Contradiction workflow (gap 1b):** nightly flags with `> [!warning] Contradiction detected` callouts (unchanged). NEW: flags older than 48h surface in the morning agent's daily note under `## Operator decisions needed`, and any interactive session that receives an operator decision must convert the callout to `> [!success] Contradiction resolved (operator decision, DATE)` in every note carrying it — the 2026-07-08 Lavoie resolutions are the worked example.
- **Bases dependency (gap 8):** no Obsidian GUI exists on this host; `.base` files are verified only by frontmatter simulation (`scripts/audit_vault.py` bases section). Rendering verification requires an Obsidian client on a synced device — until one is confirmed, treat Bases as data-contract-verified, not render-verified.
- **updated: semantics:** `updated` moves only when note content changes. Bulk mechanical passes must never re-stamp it. The stale scanner depends on this.
- **Anti-pollution:** `auto_tagger.py`/`color_tagger.py` stay retired; `scripts/tag_blocklist.txt` is the noise-tag registry; enrichment runs with `--strip-noise-tags`.

## Related

- [[EMERAULD_OS_ARCHITECTURE|EMERAULD Operating System]] (4-pillar architecture)
- [[_vault/OVERHAUL-BASELINE-2026-07-08|Overhaul Baseline 2026-07-08]]
- [[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger|RELAY-LEDGER]]
- [[wiki/Architecture - EMERAULD Scripts - Overview|EMERAULD Scripts Architecture]]
