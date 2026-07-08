---
type: wiki
title: if.switchboard — InfraFabric Product Center
aliases:
- if.switchboard
- InfraFabric Switchboard
tags:
- infrafabric
- switchboard
- product-center
- governance
- mcp
- areas
- if-switchboard-infrafabric-product-center-md
- blackboard
- coordination
- reachability
- color-purple
status: active
created: '2026-06-27'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/if.switchboard — InfraFabric Product Center.md
backlink_count: 2
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# if.switchboard — InfraFabric Product Center

> For future Claude: if.switchboard is InfraFabric's current product center — the governed interconnect/switchboard surface. Load this when a question involves InfraFabric's primary product posture, module hierarchy, or how supporting modules (if.bus, if.blackboard, if.trace, if.context) relate to the product center.

## Summary

`if.switchboard` is the current product center of [[InfraFabric Architecture]]. It owns the governed interconnect posture: audited reachability, wake delivery, contact registration, request/response routing, and delivery records. The canonical reference is the if.switchboard full explainer v1.6 (2026-03-09), second in the [[InfraFabric Architecture|InfraFabric canon review order]] after the public roadmap.

## Context

Within the InfraFabric module map, if.switchboard sits above the supporting modules. [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard]] records durable coordination evidence; if.bus handles transport/control boundary claims; if.trace provides audit/provenance receipts; if.context supplies bounded recall. None of these replace the switchboard's routing and reachability role. The [[AI Infrastructure Stack]] indexes if.switchboard as the product-center entry in the InfraFabric cluster.

## Details

**Owned claims (from InfraFabric canon):**
- Audited reachability between agents and services
- Wake delivery and contact registration
- Request/response routing with delivery records

**Boundary:** if.switchboard does not own task/session/signal state (that is [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard]]), does not own transport/control primitives (that is if.bus), and does not own audit/provenance receipts (that is if.trace).

**Canon version:** if.switchboard full explainer v1.6 (2026-03-09). Historical: v1.4 (superseded), unified v1.2 with if.blackboard (snapshot only).

**Local access:** remote MCP access through `root@infrafabric.io` SSH tunnel per `governance/global/AGENTS.md`; do not use direct `10.10.10.170` URLs.

## Related

- [[InfraFabric Architecture]] — module map and canon hierarchy
- [[if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)]] — coordination evidence surface (not routing)
- [[AI Infrastructure Stack]] — indexes if.switchboard in the MCP and Agent Coordination section
- [[InfraFabric MCP Stack — Remote Bundles]] — local MCP bundle accessing InfraFabric services
- [[ROOK — Session Boundary Model]] — session lifecycle harness that operates alongside the switchboard
