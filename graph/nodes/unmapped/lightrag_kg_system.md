---
type: System
title: LightRAG Knowledge Graph
tags:
- system
- graph
- nodes
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/nodes/unmapped/lightrag_kg_system.md
backlink_count: 2
backlinks:
- '[[graph/nodes/unmapped/ingest_py]]'
- '[[graph/nodes/unmapped/query_py]]'
id: lightrag_kg_system
canonical_name: LightRAG Knowledge Graph
confidence: high
sources:
- scripts/ingest.py
created_from: graphify_pass
---

# LightRAG Knowledge Graph

## Summary

LightRAG-backed knowledge graph over wiki/ notes, built via ingest.py and queried via query.py.

## Known Relationships

### Incoming

- [[ingest.py]] → writes → This Node
- [[query.py]] → reads → This Node

### Outgoing

- This Node → depends_on → [[ingest.py]]

## Related Files

- scripts/ingest.py

## Evidence

- "Ingest EMERAULD wiki/ notes into LightRAG knowledge graph." — scripts/ingest.py

## Open Questions

- None identified in this pass.
