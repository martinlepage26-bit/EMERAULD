---
type: graph-index
title: Graph Map
tags:
- graph-index
- graph
status: active
created: '2026-07-02'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/graph-map.md
backlink_count: 5
backlinks:
- '[[EMERAULD_OS_ARCHITECTURE]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[graph/graph-schema]]'
- '[[graph/indexes/node-index]]'
- '[[memory/daily/2026-07-02]]'
---

# Graph Map — EMERAULD Curated Ontology Layer

This is the entry point to the curated `graph/` layer built 2026-07-02 per the
graphify Phase 1-10 protocol, scoped to EMERAULD's business/operations layer
(agents, governance, tools, products, clients) rather than the full 913-note
wiki corpus. See `graph/graph-schema.md` for the node/edge format and the
relationship of this layer to the vault's other graph systems.

## Navigation

- [[graph/indexes/node-index.md|Node Index]] — all 88 nodes grouped by type
- [[graph/indexes/edge-index.md|Edge Index]] — all 109 edges grouped by relation
- [[graph/indexes/workflow-index.md|Workflow Index]] — every workflow with owner/inputs/outputs
- [[graph/indexes/team-index.md|Team Index]] — the 7 AI agent actors with what they run/talk to/produce
- [[graph/indexes/project-index.md|Project Index]] — the 18 PHAROS/Martin products and projects
- [[graph/indexes/orphan-index.md|Orphan Index]] — nodes with no captured edges, flagged for the next pass
- [[graph/edges.yml|edges.yml]] — the raw edge registry with evidence

## Where entities live

- **24 nodes** are annotated in-place (existing wiki/agent/governance files got an additive `entity_*` frontmatter block — see `graph/graph-schema.md`).
- **64 nodes** have no pre-existing dedicated file (people, products, scripts, systems, most workflows and decisions) and got a new minimal file under `graph/nodes/unmapped/`.

## Relationship to EMERAULD's other graph systems

EMERAULD has three graph mechanisms. This layer is additive to all of them, not a replacement:

1. **`wiki/` + wikilinks** (Trismégiste-governed) — the vault's primary knowledge substrate, 913 notes.
2. **`graphify-out/graph.json`** — the automated, packaged-tool graph: 10,633 nodes / 13,893 edges / 1,254 communities, mostly a reference/citation/code-call graph (`references`, `calls`, `contains`, `cites`). Cited in `EMERAULD_OS_ARCHITECTURE.md` as the vault's automated Domain layer.
3. **`.graph_store/`** — deterministic wikilink graph from `build_wikilink_graph.py`.
4. **This `graph/` layer** — a small, hand-curated ontology (Person/Team/Product/Workflow/Tool/System/Client/Decision/Dataset) with operational-semantics edges (`owns`, `runs`, `consumes`, `produces`, `depends_on`, `talks_to`...) that none of the above three systems capture. Built from ~20 entity-bearing source documents (agent contracts, governance handoff schemas, decision records, the personal-assistant-agents catalog, root `CLAUDE.md` tables), not from re-scanning the full corpus.

## Scope note

This pass covers the business/operations layer: the three-agent stack (Hephaistos,
Queen Keyport, Hermes), Trismégiste + independent specialists (Argus, Gadget, Henry),
the personal-assistant-agents catalog, EMERAULD's own automation scripts, PHAROS
products, and the Groupe Lavoie client relationship. It does **not** attempt
node-per-file coverage of the 913 wiki notes or the 10,633 graphify-out nodes —
see the original Phase 8 plan discussion for why. Content-only wiki notes (novel
drafts, research papers, daily logs, genealogy research) are out of scope for
this pass.

## Related

- [[EMERAULD_OS_ARCHITECTURE]]
- [[SOURCE_OF_TRUTH]]
- [[Governance and PHAROS MOC]]
