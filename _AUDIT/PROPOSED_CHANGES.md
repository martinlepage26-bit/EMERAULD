---
type: audit-doc
title: PROPOSED CHANGES
tags:
- audit
- vault
- plan
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _AUDIT
canonical_path: _AUDIT/PROPOSED_CHANGES.md
---

# PROPOSED CHANGES

## Execution posture for this pass

Conservative, vault-local, reversible, and navigation-first.

## Changes approved for execution in this pass

1. Create the `_AUDIT/` record set before editing major navigation files.
2. Make `wiki/Home.md` the explicit canonical home for human navigation.
3. Thin `Welcome.md` into an orientation surface that points to `Home`.
4. Recast `index.md` as an operational catalog and filesystem guide.
5. Create `_INDEXES/CRITICAL_KNOWLEDGE_INDEX.md` as a retrieval surface for high-value notes.
6. Repair one demonstrated retrieval gap: `Areas/Writing/Writing and Novels MOC.md`.
7. Establish a visible historical/quarantine boundary without broad deletion.

## Changes intentionally deferred

- no mass rename campaign
- no vault-wide broken-link repair
- no large moves inside `projects/`, `raw sources/`, `graphify-out/`, or embedded repos
- no broad deletion pass
- no attempt to normalize every legacy `wiki/` note

## No-touch or low-touch zones

- `PEER-REVIEW/` internal structure
- `projects/patent-workbench/` internal structure
- runtime stores: `.graph_store/`, `.vector_store/`
- large raw intake packs under `raw sources/`
- user-modified files outside the limited navigation and audit scope

## Proposed lane model

| Lane | Surfaces | Intended role |
|---|---|---|
| Primary knowledge | `Areas/`, `Resources/`, selected `wiki/`, key `memory/` | durable knowledge and active conceptual retrieval |
| Operational support | `projects/`, `artifacts/`, `graph/`, `graphify-out/`, `_vault/`, `Bases/`, `Logs/`, `governance/`, `hephaistos/` | searchable but not human-first |
| Raw intake | `raw/`, `raw sources/`, `Inbox/` | provenance and intake |
| Historical | `archive/`, `.trash/`, `_QUARANTINE/` | historical retention and uncertain material |

## Decision rule

When a surface is both useful and noisy, this pass prefers:

1. keep it in place
2. remove it from the main navigation path
3. archive or quarantine only if confidence is high and recovery remains trivial
