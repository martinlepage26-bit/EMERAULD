---
type: genealogy-delta
title: Skill Corpus Genealogy Delta — 2026-05-06
aliases:
- Skill Corpus Genealogy Delta — 2026-05-06
- wiki/Skill Corpus Genealogy Delta — 2026-05-06
tags:
- skills
- genealogy
- delta
- corpus
- codex
- claude
- provenance
- drift
- genealogy-delta
- wiki
- skill-corpus-genealogy-delta-2026-05-06-md
- retired
- skill
- folders
- color-orange
status: active
created: '2026-05-06'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Skill Corpus Genealogy Delta — 2026-05-06.md
backlink_count: 7
backlinks:
- '[[wiki/Delta Closure Frame — Conditions, Actors, Constraints]]'
- '[[wiki/PHAROS Skill Corpus Change Genealogy — 2026-05-06]]'
- '[[wiki/Skill Corpus Dedup Audit — 2026-05-06]]'
- '[[wiki/Skill Corpus — Complete Live Index (260 Active Skills)]]'
- '[[wiki/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/Vault Delta Interconnectivity Atlas — 2026-05-06]]'
- '[[wiki/Version Genealogy System]]'
source_roots:
  codex: /home/cerebrhoe/.codex/skills
  claude: /home/cerebrhoe/.claude/skills
---

# Skill Corpus Genealogy Delta — 2026-05-06

## Summary

This note records the **genealogy delta** for the skill corpus: the difference between
older registry claims, current filesystem reality, cross-runtime mirroring, and
canonical routing doctrine.

It is not just a dedup report. It is a lineage/control note for how the skill
ecosystem changed shape.

## Delta Statement

The previous vault audit framed the corpus as **241 skills**. The live filesystem
now shows:

- 260 active top-level Codex skill folders
- 273 total `SKILL.md` files when backups, retired aliases, system skills, and templates are counted
- 265 vault bridge notes under `wiki/skills/`
- 0 active top-level Codex skills without a vault bridge note

The older 241-count note is therefore a **historical audit snapshot**, not the
current count.

Current live index:

- [[Skill Corpus — Complete Live Index (260 Active Skills)]]

Historical snapshot:

- [[Codex Skills Inventory — Complete Registry (241 Skills)]]

Closure frame:

- [[Delta Closure Frame — Conditions, Actors, Constraints]]

## Lineage Layers

### 1. Runtime corpus

The active Codex runtime corpus lives at:

- `/home/cerebrhoe/.codex/skills/`

This is the current operational skill surface.

### 2. Claude mirror surface

The Claude skill root lives at:

- `/home/cerebrhoe/.claude/skills/`

The mirror is partial and mixed:

- 100 same-name skills exist in both Codex and Claude
- 87 same-name `SKILL.md` files are byte-identical
- 83 full-folder matches were detected by `skills-dedup`
- 13 same-name skills differ and require review before sync

Audit:

- [[Skill Corpus Dedup Audit — 2026-05-06]]

### 3. Canonical routing doctrine

The live filesystem tells what exists. The canonical map tells what should be
routed.

Canonical routing map:

- `governance/hephaistos/SKILL-MAP.md`
- [[Skill Map — Canonical Routed Skills (2026-05-06)]]

The important delta is that some active folders remain present for compatibility
while canonical routing has moved elsewhere.

## Supersession / Compatibility Map

These active folders should be read as compatibility or transition surfaces, not
as primary routing authorities.

| Older / active folder | Current canonical routing |
|---|---|
| `lead-research-assistant` | HEPHAISTOS scope + `qualitative` |
| `exploratory-data-analysis` | `senior-data-scientist` |
| `deep-research-notebooklm` | `notebooklm` + `recursive-governance-method` |
| `literature-review` | `peer-reviewed-paper-writer` |
| `research-engineer` | `architecture` |
| `statistical-analysis` | `senior-data-scientist` |
| `peer-review` | `peer-reviewed-paper-writer` for academic review, `codex-review` for code review |
| `scholar-evaluation` | `recursive-governance-method` |
| `scientific-critical-thinking` | `philosopher` |

## Retired / Dropped / Removed Trace

These are lineage traces, not active top-level Codex skills.

| Entry | Genealogy status |
|---|---|
| `free-tool-strategy` | retired; present only under Codex `_retired` |
| `hermes-dependency-mapper` | dropped 2026-04-23 |
| `hermes-escalation-router` | dropped 2026-04-23 |
| `triangulate` | deprecated alias removed in favor of `triangulation` |
| `ma-degree-guide` | retired; standalone formation work now routes through `ma-arts-letters` or philosopher's MA sub-capacity |

## What This Delta Prevents

- Count drift: treating 241, 260, and 273 as interchangeable.
- Routing drift: invoking a compatibility folder as if it were still primary.
- Mirror confusion: treating Codex/Claude duplication as accidental deletion material.
- Archive collapse: treating retired or dropped entries as active simply because their names remain in notes.
- False cleanup: deleting provenance-bearing folders when the right move is aliasing, routing notes, or retirement with trace.

## Governance Interpretation

The skill corpus now has three truths that must stay separate:

- **Existence truth:** what folders and `SKILL.md` files exist.
- **Routing truth:** what the canonical map says should be invoked.
- **Lineage truth:** why old names, retired folders, and mirrors still appear.

This is the same pattern as manuscript genealogy: a later version does not erase
the earlier one. It changes its authority.

This delta was closed by applying [[Delta Closure Frame — Conditions, Actors, Constraints]] in practice: the current filesystem state, historical registry state, live routing authority, mirrored surfaces, and lineage constraints were named separately instead of being collapsed into one count.

## Related

- [[Delta Closure Frame — Conditions, Actors, Constraints]]
- [[PHAROS Skill Corpus Change Genealogy — 2026-05-06]]
- [[Vault Delta Interconnectivity Atlas — 2026-05-06]]
- [[Version Genealogy System]]
- [[Skill Ecosystem — Professional Capability Registry]]
- [[Skill Corpus Dedup Audit — 2026-05-06]]
- [[Skill Corpus — Complete Live Index (260 Active Skills)]]
- [[Skill Map — Canonical Routed Skills (2026-05-06)]]
- [[MASTERxMASTERxMASTER — Skill Corpus Map]]
- [[Codex Skill Corpus Sync — 2026-04-20]]
- [[Claude Code Skill Corpus]]
