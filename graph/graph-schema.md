---
type: graph-index
title: Graph Schema
tags:
- graph-index
- graph
status: active
created: '2026-07-02'
updated: '2026-07-08'
vault_area: graph
canonical_path: graph/graph-schema.md
backlink_count: 1
backlinks:
- '[[graph/indexes/node-index]]'
---

# Graph Schema — EMERAULD Curated Ontology Layer

## Node types

Person | Team | Project | Product | Workflow | Tool | System | Dataset | File |
Concept | Decision | Process | Policy | Client | Vendor | Repository | Environment | Unknown

In this pass: Person, Team, Product, Workflow, Tool, System, Client, Decision, Dataset
were used. "Team" is applied to the 7 AI agent actors (Trismégiste, Hephaistos, Queen
Keyport, Hermes, Argus, Gadget, Henry) as the closest fit to an organizational team —
EMERAULD has no human org-chart teams, only this agent stack. "Product" is used instead
of "Project" for the PHAROS/Martin build catalog since the source table (root
`CLAUDE.md`) frames them as products/codenames.

## Two node representations

**1. Annotated existing file** — used when the entity already has a dedicated
Markdown file with YAML frontmatter (a wiki note, an `.agent.md` contract, a
governance doc, `SKILL.md`). The file's original content and frontmatter are
untouched; four keys are appended immediately before the closing `---` of the
frontmatter block:

```yaml
entity_type: Team | Workflow | Tool | System | Product | Client | Person | Decision | Dataset
entity_id: node_unique_slug
entity_aliases: []
entity_confidence: high | medium | low
```

This uses a new `entity_*` prefix so it never collides with the vault's existing
`type:` field (which means note-format — `wiki`, `map`, `moc`, `agent-spec`,
`governance-doc`, etc. — not entity ontology).

**2. New minimal node file** — used when no dedicated file exists (most people,
products, scripts, systems, and several workflows/decisions). Written to
`graph/nodes/unmapped/<id>.md` in this format:

```markdown
---
id: node_unique_slug
type: Team | Workflow | Project | Tool | System | Dataset | Concept | Person | Client | Vendor | Unknown
canonical_name: ""
aliases: []
status: active | inactive | unknown
confidence: high | medium | low
sources: []
created_from: graphify_pass
---

# Canonical Name

## Summary

## Known Relationships
### Incoming
### Outgoing

## Related Files

## Evidence

## Open Questions
```

## Edge registry format (`graph/edges.yml`)

```yaml
edges:
  - id: edge_unique_slug
    source: node_slug
    relation: runs
    target: node_slug
    confidence: high | medium | low
    evidence:
      - file: path/to/source.md
        note: "Evidence for this relationship."
    inferred: false
    notes: ""
```

## Edge types used in this pass

owns, runs, uses, consumes, produces, depends_on, talks_to, reports_to, reads, writes,
transforms, triggers, blocks, documents, implements, deploys_to, references,
publishes_to. (`stores`, `replaces`, `duplicates`, `unknown` were not needed this pass.)

## Confidence and inference discipline

- `confidence: high` — direct quote from a source file states the relationship.
- `confidence: medium` — reasonably inferred from adjacent evidence (e.g. a table
  row implying ownership without the word "owns").
- `confidence: low` — weak or circumstantial; flagged in `graph/indexes/orphan-index.md`
  for correction or removal on the next pass. One such edge exists in this build
  (`hexa_project → publishes_to → recurso_framework`) and should be treated as
  unverified until re-checked.
- `inferred: true` marks any edge not directly quoted from source text.

## Related

- [[graph/graph-map.md|Graph Map]]
- [[EMERAULD_OS_ARCHITECTURE]]
