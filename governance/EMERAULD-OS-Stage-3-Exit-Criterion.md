---
type: artifact
title: EMERAULD OS Stage 3 — Event-Driven Inbox Routing (exit criterion)
aliases:
  - Stage 3 exit-criterion capture
tags:
  - emerauld-os
  - stage3
  - event-driven-routing
  - governance
  - systemd
status: active
created: 2026-07-08
updated: 2026-07-08
vault_area: governance
canonical_path: governance/EMERAULD-OS-Stage-3-Exit-Criterion
---

> For future Claude: Stage 3 marks the operationalization of autonomous inbox routing via systemd path monitoring. A new file in Inbox/ triggers the emerauld-inbox.path unit, which fires an agent that normalizes frontmatter, adds wikilinks, moves the file to PARA destination, and appends a tracker line — entirely without human intervention. This note itself is the proof of concept, routed autonomously at 2026-07-08 16:32 UTC.

## Summary

Stage 3 operationalizes [[governance/EMERAULD-OS-BUILD-ORDER|the OS build sequence]] by implementing event-driven inbox routing via systemd. When a new file lands in Inbox/, the [[governance/EMERAULD-OS-SPEC — Event Triggers|emerauld-inbox.path unit]] detects it, fires a routing agent, and moves the file to its PARA destination with full frontmatter normalization and wikilink enrichment.

## Details

**Exit criterion:** A single new file in Inbox/ → systemd path fires → agent normalizes frontmatter, adds ≥2 inline wikilinks to existing notes, moves file to PARA folder, appends VAULT ADDITIONS TRACKER line — all autonomously, no human step.

**Implementation:**
- Systemd user path unit: `emerauld-inbox.path` watches `/home/martin/EMERAULD/Inbox/` for `.md` file arrivals
- Trigger: systemd fires the corresponding `.service` unit on file event
- Loop protection: ledger-based attempt tracking in `governance/tasks/` prevents duplicate routing
- Failure visibility: any routing failure appends to `Logs/scheduled/FAILURES.md` for operator review

**Proof of concept:** This note was dropped into Inbox/ at 2026-07-08 16:32 UTC and autonomously routed by the event-driven pass (frontmatter normalized per the vault schema, wikilinks verified and added, file moved from Inbox to governance/, VAULT ADDITIONS TRACKER line appended).

## Related
- [[governance/EMERAULD-OS-BUILD-ORDER]]
- [[governance/EMERAULD-OS-SPEC — Event Triggers]]
- [[governance/EMERAULD-OS-MCP-Surface-Smoke-Test]]
- [[Logs/scheduled/FAILURES.md]]
