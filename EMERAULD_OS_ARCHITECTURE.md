---
type: note
title: EMERAULD Operating System
aliases:
- EMERAULD_OS_ARCHITECTURE
tags:
- note
- emerauld-os-architecture-md
- graph
- bases
- native
- conveyor
- belt
- color-teal
status: active
created: '2026-06-26'
updated: '2026-06-26'
vault_area: EMERAULD_OS_ARCHITECTURE.md
canonical_path: EMERAULD_OS_ARCHITECTURE.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# EMERAULD Operating System

This replaces the static archive with a machine that agents can read and run.

## 1. Storage: The PARA Fracture

The vault currently mixes legacy folders with active structure. Move files into strict alignment:
- `Projects/` (deadlines, deliverables, active clients)
- `Areas/` (permanent responsibilities)
- `Resources/` (reusable knowledge, raw sources)
- `Archives/` (finished work)

You can move files freely. The OS reads from `graphify update .`, which repairs paths instantly without losing the semantic map.

## 2. Structured Data: Frontmatter

A note is text. A record is infrastructure. Every new file must carry this block:

```yaml
---
type: 
status: 
date: 
priority: 
domain: 
---
```

The `status` field is load-bearing. Skills read it to know exactly where a file sits on the conveyor belt.

## 3. The Brain: Graph as Domain

The OS demands a hard border between the *where* (Domain) and the *how* (Skill).

The 10,600-node semantic graph is the automated Domain layer. You do not need to write floor plans. The graph already knows where every concept lives.

When a skill needs to operate on the Percephal Protocol, it does not hardcode a folder path. It queries the graph, locates the file, runs the transformation, and exits.

The 10,600-node graph is a reference/citation graph — it knows what mentions what, not who owns, runs, or depends on what. For that operational ontology (agents, workflows, tools, products, clients and the owns/runs/consumes/depends_on relationships between them), see [[graph/graph-map.md|Graph Map]], a small hand-curated layer built 2026-07-02.

## 4. Vision: Native Bases

The file tree is blind. The native graph view is silent. 

Use Obsidian Bases to pull files by `domain` or `type`, rendering them as Kanban boards grouped by `status`. The vault becomes a database you own entirely.
