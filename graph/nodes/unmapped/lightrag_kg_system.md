---
id: lightrag_kg_system
type: System
canonical_name: "LightRAG Knowledge Graph"
aliases: []
status: active
confidence: high
sources: ['scripts/ingest.py']
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
