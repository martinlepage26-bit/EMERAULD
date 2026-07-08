---
id: vector_store_system
type: System
canonical_name: ".vector_store"
aliases: []
status: active
confidence: high
sources: ['EMERAULD/CLAUDE.md']
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
