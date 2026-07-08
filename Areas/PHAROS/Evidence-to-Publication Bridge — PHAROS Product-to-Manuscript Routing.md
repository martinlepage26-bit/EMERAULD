---
type: wiki
title: Evidence-to-Publication Bridge — PHAROS Product-to-Manuscript Routing
aliases:
- Evidence-to-Publication Bridge
- PHAROS evidence bridge
- product-to-manuscript routing
tags:
- pharos
- scholarly
- evidence
- publication
- governance
- architecture
- areas
- evidence-to-publication-bridge-pharos-product-to-manuscript-routing-md
- manuscript
- cluster
- bridge
- color-orange
status: active
created: '2026-06-26'
updated: '2026-06-26'
vault_area: Areas
canonical_path: Areas/PHAROS/Evidence-to-Publication Bridge — PHAROS Product-to-Manuscript Routing.md
backlink_count: 6
backlinks:
- '[[.graph_store/graph_report]]'
- '[[Areas/PHAROS/2026-06-29 - idea-discovery]]'
- '[[Areas/Writing/AREA]]'
- '[[Areas/PHAROS/PHAROS Scholarly Publication Track]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Evidence-to-Publication Bridge — PHAROS Product-to-Manuscript Routing

## Summary

The Evidence-to-Publication Bridge is a structural reframe adopted on 2026-06-26 to replace the prior "monolithic PHAROS MOC cluster" model. It treats PHAROS product surfaces ([[COMPASSai — Governance Engine]], [[AurorA — COMPASSai Input Module]], [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]], [[Hermes Dashboard — Professional Governance Tool]]) as **evidence nodes** that feed into manuscript surfaces — not as parallel ends in themselves.

## Context

Prior to 2026-06-26, PHAROS-adjacent notes were loosely grouped under a monolithic MOC cluster, making it hard to navigate from product work (routes, deployments, classifier outputs) to the manuscripts those products are supposed to support. The bridge reframe draws a clear directional line:

```
[Product / Protocol Surface]
        ↓  (implementation evidence)
[Evidence-to-Publication Bridge]
        ↓  (supports specific manuscript claims)
[PHAROS Scholarly Publication Track]
        ↓  (journals and submissions)
[Research and Papers MOC]
```

## Details

### The Four Evidence Nodes

- **[[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]]** — stress-test and transcript evidence for revisability, continuity pressure, and audit-after-the-run claims in the AI Society / RDAIG manuscript lane.
- **[[COMPASSai — Governance Engine]]** — implementation evidence only where specific route, gate, or deployment records support a manuscript claim (gate-model language in RDAIG; consequence-binding in PHAROS AI Ethics; revisability in AI Society manuscript).
- **[[AurorA — COMPASSai Input Module]]** — intake and admissibility evidence for bounded corpus formation and pre-engine handoff claims.
- **[[Hermes Dashboard — Professional Governance Tool]]** — operator-view evidence for routing, monitoring, and governance-work coordination; belongs to the implementation cluster, not the manuscript-writing cluster.

### Routing Rule

Cite a product surface in a manuscript **only** where named evidence (routes, gate transitions, classifier outputs, deployment records, transcripts) supports the specific claim. If no concrete artifact is named, the citation is a claim-by-association and should be removed.

### What Is NOT Part of the Bridge

- **Fisher King project-state notes** — operations and recovery trackers; reachable from project hubs but not conceptual centers of the publication cluster.
- **RECURSO** — audit substrate and recursive test bed that sits *upstream* of the bridge as a deeper evidence layer (see [[RECURSO — Final Audit and Ethical Review]] and [[RECURSO — Recursive Governance Test Archive]]).

## Related

- [[PHAROS Scholarly Publication Track]] — the publication landing hub; defines the bridge's downstream target
- [[Research and Papers MOC]] — top-level scholarly index containing the bridge cluster
- [[Research Hub]] — broader research context
- [[PHAROS Commercial Strategy]] — the commercial branch alongside the publication branch
- [[Recursive Governance Theory]] — theoretical substrate that the bridge evidence is meant to support
