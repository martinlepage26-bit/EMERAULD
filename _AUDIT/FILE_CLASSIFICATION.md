---
type: audit-doc
title: FILE CLASSIFICATION
tags:
- audit
- vault
- classification
- emerauld
status: active
created: '2026-07-10'
updated: '2026-07-10'
vault_area: _AUDIT
canonical_path: _AUDIT/FILE_CLASSIFICATION.md
---

# FILE CLASSIFICATION

## Four-lane model

| Lane | Paths | Treatment in this pass |
|---|---|---|
| Primary knowledge | `Areas/`, `Resources/`, selected `wiki/`, key `memory/`, `Publications/` | promote in navigation |
| Operational support | `projects/`, `artifacts/`, `graph/`, `graphify-out/`, `_vault/`, `Bases/`, `Logs/`, `governance/`, `hephaistos/`, `.graph_store/`, `.vector_store/` | keep searchable, demote from home |
| Raw intake | `raw/`, `raw sources/`, `Inbox/` | keep intact, point to them explicitly as intake/provenance |
| Historical | `archive/`, `.trash/`, `_QUARANTINE/` | preserve, keep recoverable |

## Folder-by-folder classification

| Path | Lane | Notes |
|---|---|---|
| `Areas/PHAROS/` | Primary knowledge | canonical governance/product corpus |
| `Areas/Writing/` | Primary knowledge | canonical research and creative corpus |
| `Areas/Personal/` | Primary knowledge | active personal and project-facing anchors |
| `Areas/Lavoie/` | Primary knowledge | active client corpus |
| `Resources/` | Primary knowledge | reusable processed references |
| `wiki/` | Mixed | keep only selected hubs human-first |
| `memory/` | Mixed leaning primary | active continuity and business control |
| `projects/` | Operational support | keep discoverable, not top-level primary |
| `artifacts/` | Operational support | generated reports and packaging outputs |
| `graph/` | Operational support | graph data / reports |
| `graphify-out/` | Operational support | generated graph outputs and debris |
| `_vault/` | Operational support | manifests, internal vault meta |
| `Bases/` | Operational support | database views, not conceptual entry |
| `Logs/` | Operational support | operational traces |
| `governance/` | Operational support + durable doctrine | searchable and important, but not a main vault home |
| `hephaistos/` | Operational support + durable doctrine | same as above |
| `raw/` | Raw intake | canonical new intake lane |
| `raw sources/` | Raw intake | legacy intake and provenance lane |
| `Inbox/` | Raw intake | triage lane |
| `archive/` | Historical | live archive lane |
| `.trash/` | Historical | discard lane with provenance value |

## Canonical home rule

For human entry:

- `wiki/Home.md` is the conceptual home
- `index.md` is the filesystem and operational catalog
- `Welcome.md` is the orientation wrapper

Everything else should route outward from those roles instead of competing with them.
