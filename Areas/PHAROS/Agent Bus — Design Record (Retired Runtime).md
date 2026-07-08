---
type: governance-doc
title: Agent Bus — Design Record (Retired Runtime)
tags:
- governance-doc
- agent-bus
- retired
- design-record
status: archived
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Agent Bus — Design Record (Retired Runtime).md
---

# Agent Bus — Design Record (Retired Runtime)

> For future Claude: the `.agent_bus/` runtime (agent_bus.py + messages.sqlite) was RETIRED on 2026-07-08 and moved to `archive/retired-2026-07-08/agent_bus/`. If a wiki note references agent_bus as live infrastructure, it is describing the design, not a running system. This note is the canonical landing point for those ~33 references.

## Summary

The agent bus was a designed inter-agent SQLite message bus for the EMERAULD agent ecosystem. It was never activated: `messages.sqlite` carried a creation-date mtime of 2026-05-24 and was never touched again, and no process on this host ever referenced it. The 2026-07-08 overhaul's infrastructure survey classified it "designed-never-activated" and the retire verdict was taken in [[governance/EMERAULD-OS-BUILD-ORDER|the OS build order]] (gap 5).

## Context

The capability the bus was designed for — inter-agent messaging — is served on this host by two live mechanisms: the tmux AI council (direct pane messaging via the tmux-ai-council skill) and the hosted InfraFabric coordination surface ([[Areas/PHAROS/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard]], hosted API since the R0.5 rollout). A future event-driven vault bus, if ever needed, should be designed against the [[governance/EMERAULD-OS-BUILD-ORDER|build order]]'s gap-2 spec rather than reviving this artifact.

## Details

- Retired artifacts: `archive/retired-2026-07-08/agent_bus/{agent_bus.py, README.md, messages.sqlite}`.
- Same-day sibling retirement: `scheduler_memory/` (superseded scheduler concept, dead since 2026-04-26) → `archive/retired-2026-07-08/scheduler_memory/`.
- The ~33 wiki notes referencing the bus are left textually intact (append-not-delete rule); this record supersedes their liveness claims.

## Related

- [[Areas/PHAROS/InfraFabric Architecture]]
- [[wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]
