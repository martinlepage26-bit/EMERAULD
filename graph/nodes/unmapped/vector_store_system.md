---
type: System
title: .vector_store
tags:
- system
- graph
- nodes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/nodes/unmapped/vector_store_system.md
backlink_count: 2
backlinks:
- '[[graph/nodes/unmapped/embed_py]]'
- '[[graph/nodes/unmapped/vsearch_py]]'
id: vector_store_system
canonical_name: .vector_store
confidence: high
sources:
- EMERAULD/CLAUDE.md
created_from: graphify_pass
---

# .vector_store

## Summary

Local sentence-transformers vector store (all-MiniLM-L6-v2) for semantic search over wiki/maps/projects. Built by embed.py, queried by vsearch.py.

## Known Relationships

### Incoming

- [[embed.py]] → produces → This Node
- [[vsearch.py]] → reads → This Node

### Outgoing

- This Node → depends_on → [[embed.py]]

## Related Files

- EMERAULD/CLAUDE.md

## Evidence

- "Vector store: 896 entries, last built 2026-06-21 (Sentence-transformers all-MiniLM-L6-v2, fully local)" — EMERAULD/CLAUDE.md

## Open Questions

- None identified in this pass.
