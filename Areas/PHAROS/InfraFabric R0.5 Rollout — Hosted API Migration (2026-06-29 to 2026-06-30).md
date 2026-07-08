---
type: wiki
title: InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)
aliases:
- R0.5
- R0.5 rollout
- InfraFabric R0.5
tags:
- infrafabric
- blackboard
- if-context
- mcp
- migration
- infrastructure
- areas
- infrafabric-r0-5-rollout-hosted-api-migration-2026-06-29-to-2026-06-30-md
- stacklight
- sheet
- tunneled
- color-teal
status: active
created: '2026-07-01'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30).md
backlink_count: 7
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/InfraFabric MCP Stack — Remote Bundles]]'
- '[[Areas/PHAROS/MCP and Runtime Integration MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[wiki/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]'
- '[[memory/daily/2026-07-01]]'
- '[[session-state]]'
---

# InfraFabric R0.5 Rollout — Hosted API Migration (2026-06-29 to 2026-06-30)

> For future Claude: R0.5 is the InfraFabric release that moved `if.blackboard` and `if.context` off SSH-tunneled Proxmox script/JSONL access and onto hosted HTTPS APIs backed by PostgreSQL on `mtl-02`. Load this note whenever a vault note references SSH-tunneled InfraFabric access as current — as of 2026-06-29/06-30 that access pattern is superseded and fails closed by design.

## Summary

R0.5 is the InfraFabric infrastructure rollout that replaced direct SSH/script/JSONL mutation of [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard]] and `if.context` with hosted HTTPS APIs on host `mtl-02`, documented across [[InfraFabric MCP Stack — Remote Bundles]] and [[Stacklight-owner-explainer]].

## Context

Before R0.5, both `if_blackboard` and `if_context` were accessed as remote MCP wrappers over SSH to `root@infrafabric.io`, which tunneled into Proxmox container 270 to mutate local script/JSONL state directly. This was the access pattern documented in [[InfraFabric MCP Stack — Remote Bundles]] and the original [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard spec sheet]] when they were first written (2026-06-27). It is also the pattern [[AI Infrastructure Stack]] still needs correcting in its infrastructure status snapshot.

## Details

**Rollout timeline:**
- **2026-06-29** — `if_blackboard` migrated first. Durable reads/writes now go exclusively through a hosted HTTPS API at `https://api.infrafabric.io`, backed by PostgreSQL on `mtl-02` (database `if_blackboard`, table `if_blackboard.r05_events`). The MCP entrypoint changed from the SSH-tunneled `if-blackboard-mcp-server.mjs` to an API-backed stdio shim, `if_blackboard_api_mcp_server.py`.
- **2026-06-30** — `if_context` migrated the same way, repaired by session `/rook-410`. Hosted `if.context` R0.5 API on `mtl-02` at `https://api.infrafabric.io/v1/context/*`, PostgreSQL schema/table `if_context.r05_events` inside the same `mtl-02` `if_blackboard` database, systemd service `if-context-r05-api.service` on `127.0.0.1:8098` behind Caddy. MCP client is `/root/scripts/if_context_api_mcp_server.py`; `iftransport` defaults `if_context` to API mode (`IFTRANSPORT_MCP_IF_CONTEXT_MODE=api` set explicitly on `mtl-01` and `mtl-03`).

**Root cause of the pre-repair `if_context` outage:** `mtl-03`'s Codex config pointed `if_context` at the private `mtl-01` URL `10.10.10.170:18890`, unreachable from `mtl-03` — the exact address class the InfraFabric MCP Stack note's SSH safety rule warns against. This validated the safety rule with a real incident rather than caution alone.

**What changed vs. what didn't:** only the access/transport path changed. Direct script, JSONL, local database, and SSH-wrapper mutation paths now fail closed by design — they are not an alternate durable path, they are disabled. The data model, claim register, and non-claims in the [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard spec sheet]] still hold.

**This machine:** confirmed as `mtl-03` per the `5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md` host-role table.

**Open:** `mtl-03`'s own `if-cli` binary is drifted — points to an older `if_cli.py` with no `blackboard` command — so CLI parity is not yet claimed on this host even though the underlying API migration for both `if_blackboard` and `if_context` is complete. Not yet repaired as of the 2026-06-30 handover.

## Sources

- `/home/martin/apps/stacklight/documentation/agents/5009-if-blackboard-postgres-authority-runbook-2026-06-29.md`
- `/home/martin/apps/stacklight/documentation/agents/5011-stacklight-blackboard-mtl03-fresh-session-handover-2026-06-30.md`

## Related

- [[InfraFabric MCP Stack — Remote Bundles]]
- [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]]
- [[Stacklight-owner-explainer]]
- [[AI Infrastructure Stack]]
- [[InfraFabric Architecture]]
