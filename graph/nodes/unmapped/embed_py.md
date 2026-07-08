---
type: Tool
title: embed.py
tags:
- tool
- graph
- nodes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/nodes/unmapped/embed_py.md
backlink_count: 1
backlinks:
- '[[graph/nodes/unmapped/vector_store_system]]'
id: embed_py
canonical_name: embed.py
confidence: high
sources:
- scripts/embed.py
created_from: graphify_pass
---

# embed.py

## Summary

Build the EMERAULD local vector store from wiki/, maps/, and projects/ notes. Embeddings saved to .vector_store/.

## Known Relationships

### Incoming

- [[.vector_store]] → depends_on → This Node

### Outgoing

- This Node → produces → [[.vector_store]]

## Related Files

- scripts/embed.py

## Evidence

- "Build the EMERAULD local vector store from wiki/, maps/, and projects/ notes. Embeddings saved to .vector_store/." — scripts/embed.py

## Open Questions

- None identified in this pass.
