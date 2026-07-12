---
type: index
title: EMERAULD Vault Index
aliases:
- vault-index
tags:
- vault-doc
- ai-first-true
- projects
- fisher
- king
- bases
- progress
status: active
created: '2026-06-29'
updated: '2026-07-10'
vault_area: index.md
canonical_path: index.md
backlink_count: 1
backlinks:
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

> For future Claude: This file is the operational and filesystem catalog for EMERAULD. Do not treat it as the conceptual home. Start with [[Home]] for knowledge navigation, then return here when you need folder lanes, operational surfaces, or retrieval boundaries.

# EMERAULD Vault Index

Human-first conceptual entry lives at [[Home]]. Use this note when you need the vault's operating lanes, not when you need the best thinking surface.

## Navigation Roles

| Surface | Role |
|---|---|
| [[Home]] | canonical conceptual home |
| [[Welcome]] | thin orientation wrapper |
| [[_INDEXES/CRITICAL_KNOWLEDGE_INDEX|Critical Knowledge Index]] | shortest high-value retrieval path |
| [[memory]] | active business-state dashboard |
| [[wiki/Master Project Tracker — 2026|Master Project Tracker — 2026]] | cross-project control note |

## Lane Map

| Lane | Main paths | Role |
|---|---|---|
| Primary knowledge | `Areas/`, `Resources/`, selected `wiki/`, key `memory/` | durable knowledge and active conceptual retrieval |
| Operational support | `projects/`, `artifacts/`, `graph/`, `graphify-out/`, `_vault/`, `Bases/`, `Logs/`, `governance/`, `hephaistos/` | searchable support surfaces, not main home |
| Raw intake | `raw/`, `raw sources/`, `Inbox/` | provenance and intake |
| Historical | `archive/`, `.trash/`, `_QUARANTINE/` | historical retention and uncertain material |

## Primary Knowledge Surfaces

- [[Areas/PHAROS/Governance and PHAROS MOC|Governance and PHAROS MOC]]
- [[Areas/Writing/Research and Papers MOC|Research and Papers MOC]]
- [[Areas/Writing/Writing and Novels MOC|Writing and Novels MOC]]
- [[Areas/Personal/Personal and Projects MOC|Personal and Projects MOC]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[Resources/ROUTING|Resources — What Goes Here]]

## Operational Surfaces

- `projects/` holds project-state notes, embedded codebases, and large non-note payloads. It remains searchable but should not lead human navigation.
- `graphify-out/` is runtime output, not a browsing hub.
- `_vault/` holds manifests and vault meta.
- `governance/` and `hephaistos/` hold durable doctrine plus operational control material.

## Raw and Historical Boundaries

- `raw/` is the default intake lane for newly verified source material.
- `raw sources/` remains a legacy provenance lane and should not be treated as peer knowledge.
- `archive/` is searchable historical memory.
- `_QUARANTINE/` exists for uncertain low-value material that should be recoverable before any deletion decision.

## High-Signal Operational Notes

- [[memory]]
- [[wiki/Master Project Tracker — 2026|Master Project Tracker — 2026]]
- [[Areas/Lavoie/AREA|Area — Lavoie]]
- [[_AUDIT/VAULT_INVENTORY|Vault Inventory]]
- [[_AUDIT/PROPOSED_CHANGES|Proposed Changes]]

## Retrieval Commands

```bash
# Semantic search
/home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/vsearch.py "query"

# Editable-vault audit snapshot
python3 /home/martin/EMERAULD/scripts/audit_vault.py

# Vector refresh after real note changes
/home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/embed.py --changed
```
