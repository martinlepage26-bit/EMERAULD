---
type: wiki
title: Hermes Dashboard — Professional Governance Tool
aliases:
- Hermes Dashboard
- governance dashboard
- wiki/Hermes Dashboard — Professional Governance Tool
tags:
- pharos
- product
- governance-tool
- hermes
- operator-view
- wiki
- hermes-dashboard-professional-governance-tool-md
- dashboard
- softinfo
- activity
- lanes
- color-purple
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Hermes Dashboard — Professional Governance Tool.md
backlink_count: 37
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/AurorA — COMPASSai Input Module]]'
- '[[Areas/PHAROS/COMPASSai — Governance Engine]]'
- '[[wiki/Documents Root Intake — Hermes Action Map 2026-04-28]]'
- '[[wiki/Documents Root Loose Files Intake — 2026-04-28]]'
- '[[wiki/EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]]'
- '[[wiki/EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]]'
- '[[wiki/Evidence-to-Publication Bridge — PHAROS Product-to-Manuscript Routing]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/HELIX Hermes-Assisted Prospect Extension - Canada Regulated AI Routes 2026-05-06]]'
- '[[wiki/HELIX Production Shipping Runbook — Web, iOS, Android (2026-04-19)]]'
- '[[wiki/InfraFabric Codex Alignment — System-Shaper Frame]]'
- '[[wiki/L99 PHAROS Migration Artifacts 2026-04-19]]'
- '[[Areas/PHAROS/PHAROS Scholarly Publication Track]]'
- '[[Areas/PHAROS/PHAROS-AI Webservice — pharos-ai.ca]]'
- '[[wiki/Paper 25 — Pre-Draft Artifacts (Pharos Frame Capstone)]]'
- '[[wiki/Posture vs Execution Drift — The Practice of Refusal]]'
- '[[wiki/Research Hub]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/Second Self System Identity Kernel and Agent Routing Architecture]]'
- '[[Areas/PHAROS/Second Self System — Identity Kernel and Agent Routing Architecture]]'
- '[[wiki/Weekly Review — 2026-06-26]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[archive/session-state/session-state-002]]'
- '[[assets/elemental-agents/positioning-memo]]'
- '[[memory]]'
- '[[memory/agents/Events]]'
- '[[memory/agents/Vibe]]'
- '[[memory/clients/ExterminationDG]]'
- '[[memory/clients/Lavoie Construct]]'
- '[[memory/clients/Sante-France]]'
- '[[memory/daily/2026-04-24]]'
- '[[memory/daily/2026-04-28]]'
- '[[raw/00_Inbox/Raw/2026-04-25 — Stop coding, clean, package, send]]'
- '[[session-state]]'
- '[[templates/Invoice Template Pharos-AI]]'
---

# Hermes Dashboard — Professional Governance Tool

## Summary

The Hermes Dashboard is a professional governance tool designed for [[Martin Lepage — Professional Profile|Martin Lepage, PhD]] to manage, monitor, and coordinate AI governance work across active engagements. It provides activity lanes — structured views of Martin's ongoing governance obligations, client cases, research threads, and operational tasks — within the [[PHAROS AI Ethics Submission — Springer Draft|PHAROS]] practice. The dashboard is part of the operator-facing layer of the PHAROS product stack, distinct from the client-facing [[AurorA — COMPASSai Input Module]] and processing [[COMPASSai — Governance Engine]]. It is the desktop/app surface for the live business state tracked in [[memory]]. The Hermes-as-router architecture is the explicit invocation of Hermès Thoth Trismégiste from p. 50 of the [[Mort et Naissance et L'Ombre et le Double — MA Thesis on Yvon Rivard (Université Laval, 2010)|2010 MA thesis]] (see [[Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone]]); the Hermes Dashboard is the practitioner-surface manifestation of that role — *psychopomp*-authority operationalized as activity routing.

## Surface

- Canonical local surface: `C:\Users\softinfo\Documents\HERMES Dashboard`
- WSL path: `/mnt/c/Users/softinfo/Documents/HERMES Dashboard`
- Canonical source script: `C:\Users\softinfo\Documents\HERMES Dashboard\hermes.py`
- Packaged executable (when built): `C:\Users\softinfo\Documents\HERMES Dashboard\dist\HERMES.exe`
- Vault-side counterpart: [[memory]] and [[memory/clients/Progression]]

## Context

Hermes as a name in the PHAROS architecture refers to the Tier 2 routing, coordination, and escalation agent in the [[HEPHAISTOS Co-Equal Authority Cleanup — Wave 1 and 2 (2026-04-18)|three-agent stack]] (Hephaistos → Queen Keyport → Hermes). The Hermes Dashboard extends this routing-and-monitoring function into a practitioner-facing tool for Martin's consulting and research work.

Activity lanes provide structured visibility into parallel governance engagements — preventing context collapse across multiple client cases, research threads, and operational tasks running simultaneously. This directly applies the PHAROS principle that governance work must remain inspectable and traceable.

Access via [[PHAROS-AI Webservice — pharos-ai.ca]] once live.

## Details

**Product stack position:**
- [[AurorA — COMPASSai Input Module]]: client intake
- [[COMPASSai — Governance Engine]]: governance engine
- Hermes Dashboard: operator activity management (this note)
- [[PHAROS-AI Webservice — pharos-ai.ca]]: public deployment surface

**Activity lane concept:**
Lanes are structured work tracks — each lane holds one active governance thread (client case, research manuscript, operational task, product sprint). Designed to prevent cognitive overload and enforce the single-owner control model at the practitioner level.

**Status:** Local desktop surface is production-ready (operator tool). Public web access remains a separate surface/decision.

## Canonical Lanes (Documents Source Of Truth)

Per EMERAULD operating rules, canonical business content is written to markdown trackers under `C:\Users\softinfo\Documents\` and mirrored into the vault. JSON files in the dashboard folder are state/cache only.

Five primary lanes:

- Client Accounts: `C:\Users\softinfo\Documents\CLIENT ACCOUNTS TRACKER.md`
- Master Tracker: `C:\Users\softinfo\Documents\MASTER TRACKER (recreated from MASTER PACK 4).md`
- PHAROS Surface: `C:\Users\softinfo\Documents\PHAROS-AI CHANGE TRACKER.md`
- Method & Harness: `C:\Users\softinfo\Documents\METHOD TRACKER.md`
- Martin Public Surface: `C:\Users\softinfo\Documents\MARTIN-SITE CHANGE TRACKER.md`

Vault mirrors (aligned as needed):

- [[CLIENT ACCOUNTS]]
- [[PHAROS SURFACE|PHAROS Surface]]
- [[MARTIN SURFACE]]
- [[memory]]

## Persistence and Drift Notes

- Dashboard reads the canonical markdown trackers and persists UI state to JSON (`hermes_state.json`) plus corpus state (`pharos_hermes_sync.json`).
- On 2026-04-24 a reconciliation pass re-aligned the vault mirrors and expanded the client ledger notes under `memory/clients/` (see [[memory/daily/2026-04-24]]).
- On 2026-04-28, [[Documents Root Intake — Hermes Action Map 2026-04-28]] turned the Documents-root intake into a routeable dashboard object with P0/P1/P2 work packets across PHAROS Surface, Master Tracker, and Method & Harness. Canonical tracker entries were added to the Documents trackers first; dashboard JSON should follow those markdown sources.
- On 2026-04-29, [[Second Self System — Identity Kernel and Agent Routing Architecture]] clarified the identity/routing layer that can help Hermes Dashboard distinguish public voice, orchestration, execution, memory, and governance organs. This is a tracker/content architecture update, not a `hermes.py` UI change yet.
- On 2026-05-09, [[EMERAULD Workspace Instructions - Perplexity Computer and Hermes Dashboard]] made the root `AGENTS.md` Hermes design-system rules graph-visible for retrieval. `AGENTS.md` remains the runtime source of truth.

## Key Ideas
- Operator-facing view of Martin's governance practice
- Activity lanes enforce single-thread focus on each engagement
- Routing and monitoring logic derived from the Hermes agent role

## Open Questions
- How many concurrent activity lanes are intended?
- Does the dashboard connect to [[InfraFabric Architecture]] blackboard state?
- Integration with [[ROOK — Session Boundary Model]] session tracking?

## Evidence-to-Publication Bridge

Hermes Dashboard belongs to the operator-routing evidence cluster, not the manuscript-writing cluster. It supports publication claims about inspectable governance work, single-owner control, and routing/monitoring under parallel engagements — useful where [[AI Society Manuscript — From AI Anxiety to Recursive Governance]] or [[PHAROS AI Ethics Submission — Springer Draft]] discuss revisability, accountability chains, or practitioner oversight. Pair with [[COMPASSai — Governance Engine]] and [[AurorA — COMPASSai Input Module]] for client-facing implementation evidence; pair with [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]] for adversarial continuity pressure. Index through [[PHAROS Scholarly Publication Track]] and [[Research Hub]]; return to [[PHAROS]] for stack context.

## Related
- [[COMPASSai — Governance Engine]]
- [[AurorA — COMPASSai Input Module]]
- [[PHAROS-AI Webservice — pharos-ai.ca]]
- [[ROOK — Session Boundary Model]]
- [[Martin Lepage — Professional Profile]]
- [[Governance and PHAROS MOC]]
- [[memory]]
- [[Documents Root Intake — Hermes Action Map 2026-04-28]]
- [[Second Self System — Identity Kernel and Agent Routing Architecture]]
- [[RECURSO — Final Audit and Ethical Review]]
- [[PHAROS]]
- [[PHAROS Scholarly Publication Track]]
- [[Research Hub]]
- [[HELIX Desktop Corpus — Protocol Evolution and Stress-Test Runs (2026-05-06)]]
- [[Recursive Deterministic AI Governance — Method and Paper]]
- [[AI Society Manuscript — From AI Anxiety to Recursive Governance]]
- [[PHAROS AI Ethics Submission — Springer Draft]]
