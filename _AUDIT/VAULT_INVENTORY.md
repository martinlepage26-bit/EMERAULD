---
type: audit-doc
title: VAULT INVENTORY
tags:
- audit
- vault
- inventory
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _AUDIT
canonical_path: _AUDIT/VAULT_INVENTORY.md
---

# VAULT INVENTORY

## Scope

- **Vault root:** `/home/martin/EMERAULD`
- **Scan date:** 2026-07-10
- **Git branch:** `main`
- **HEAD at scan:** `50fd067`
- **Observed dirty worktree entries at scan:** `350`

## Verified facts

- Total files in the vault root: `42,641`
- Total Markdown files in the vault root: `2,991`
- Editable Markdown in the current audit harness scope: `1,580`
- Embedded git repos inside the vault: `PEER-REVIEW/`, `projects/patent-workbench/`
- Current entry surfaces at root or near-root: `Welcome.md`, `index.md`, `wiki/Home.md`
- Current graph-store snapshot: `1,462` nodes, `13,217` edges, `3,265` unresolved links, `19` components, `24` zero-backlink notes
- Current audit harness result: `1` editable Markdown file without frontmatter, `0` YAML parse failures

## Top-Level Cluster Inventory

| Path | Markdown files | Total files | Working classification |
|---|---:|---:|---|
| `Areas/` | 400 | 400 | Primary knowledge |
| `Resources/` | 71 | 71 | Primary knowledge |
| `wiki/` | 432 | 433 | Mixed: legacy hubs, machinery, residual knowledge |
| `memory/` | 109 | 109 | Primary knowledge + active continuity |
| `projects/` | 601 | 34,384 | Operational support; major navigation noise source |
| `artifacts/` | 72 | 112 | Operational support |
| `graph/` | 73 | 74 | Operational support |
| `graphify-out/` | 5 | 1,584 | Generated operational residue; major noise source |
| `.graph_store/` | 1 | 6 | Runtime store |
| `.vector_store/` | 0 | 3 | Runtime store |
| `raw/` | 50 | 82 | Raw intake |
| `raw sources/` | 777 | 957 | Legacy raw intake; major navigation noise source |
| `Inbox/` | 1 | 1 | Raw intake |
| `archive/` | 83 | 116 | Historical lane |
| `.trash/` | 26 | 27 | Historical / discard lane |
| `_vault/` | 9 | 12 | Operational support |
| `Bases/` | 0 | 4 | Operational support |
| `Logs/` | 13 | 20 | Operational support |
| `assets/` | 21 | 45 | Supporting assets |
| `Publications/` | 2 | 4 | Specialized durable knowledge |
| `governance/` | 66 | 66 | Durable governance + operational doctrine |
| `hephaistos/` | 76 | 111 | Durable governance + operational doctrine |
| `PEER-REVIEW/` | 45 | 73 | Embedded repo; excluded from structural reorg |

## Density notes

- `projects/` contains only `601` Markdown files but `34,384` total files. It is the single largest navigation-distorting surface in the vault.
- `graphify-out/` contains only `5` Markdown files but `1,584` total files, dominated by generated graph chunks, manifests, and cache-like byproducts.
- `raw sources/` is still larger than `Areas/`, `Resources/`, and `memory/` combined by Markdown count.

## Embedded Repos and Exclusions

These were verified and are excluded from structural reorganization in this pass:

- `PEER-REVIEW/.git`
- `projects/patent-workbench/.git`

## Entry-Surface Condition

- `wiki/Home.md` is the only broad graph-facing home with established `[[Home]]` resolution.
- `Welcome.md` already points to `[[Home]]` but still behaves like a parallel entry surface.
- `index.md` still presents itself as a master catalog and secondary starting point.

## Reliability Signals

- `audit_vault.py` reports `1,289` editable notes with `updated: 2026-06-26`, which confirms a compressed recency signal rather than trustworthy freshness metadata.
- `wiki/Vault Health — 2026-07-05.md` reports `409` actionable dead-link pairs across `131` top-level `wiki/` notes in its narrower scope.
- The current full-corpus graph snapshot still shows `3,265` unresolved links and `19` connected components, so navigation cohesion remains materially degraded outside the strongest MOC surfaces.

## Observed noise clusters

- `graphify-out/` root runtime debris, including `.graphify_chunk_files_01.txt` through `.graphify_chunk_files_56.txt`
- generated directory MOCs in `wiki/` such as `GRAPHIFY-OUT MOC`, `RAW MOC`, and `RESOURCES MOC`
- large raw capture packs in `raw sources/`
- large code/runtime surface under `projects/`, especially `projects/micro1/` and the embedded `projects/patent-workbench/`

## Notes requiring Martin's judgment

- Whether `projects/` should remain vault-visible long term or be reduced to a narrower set of mirrors
- Whether old generated directory MOCs in `wiki/` should be rewritten, archived, or left as low-priority legacy surfaces
- Whether `.trash/` should ever be purged automatically; this audit assumes no
