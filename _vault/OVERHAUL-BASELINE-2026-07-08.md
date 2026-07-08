---
type: register
title: OVERHAUL-BASELINE-2026-07-08
aliases:
- Overhaul Baseline 2026-07-08
tags:
- register
- overhaul
- baseline
- vault
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: _vault
canonical_path: _vault/OVERHAUL-BASELINE-2026-07-08.md
backlink_count: 4
backlinks:
- '[[Logs/2026-07-08]]'
- '[[_vault/PARA-MIGRATION-MANIFEST-2026-07-08]]'
- '[[_vault/RAW-FRONTMATTER-MANIFEST-2026-07-08]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
---

# Overhaul Baseline — 2026-07-08

For future Claude: this is the Phase 0 measurement floor for the 2026-07-08 vault overhaul (VM sync + frontmatter/graph overhaul + agentic OS preparation). All Phase 2–7 verification gates compare against these numbers. Plan: `/home/martin/.claude/plans/partitioned-wiggling-grove.md`. Rollback: git tag `pre-overhaul-2026-07-08` (commit e49adcf). Machine-readable copy: [[overhaul-baseline-2026-07-08.json|_vault/overhaul-baseline-2026-07-08.json]].

## Git

- Checkpoint commit `e49adcf` captured 1,486 previously uncommitted entries (PARA scaffold, Bases/, root agent docs, 91 deletions of personal-assistant-agents/). Pushed with tag.
- PEER-REVIEW/ and projects/patent-workbench/ are embedded git repos → recorded as gitlinks; their content history lives in their own .git.
- The 4 EMERAULD crontab entries are PAUSED for the overhaul window (backup at `~/.claude/cron-backup-pre-overhaul-2026-07-08.txt`, lines prefixed `#PAUSED-OVERHAUL#`). Re-enable in Phase 7.

## Graph (two corpus modes — compare like for like)

| Mode | Nodes | Edges | Unresolved | Components | Zero-backlink |
|---|---|---|---|---|---|
| Stored build 2026-06-27 (paths.json corpus) | 908 | 9,067 | 3,374 | 1 | 0 |
| Direct scan 2026-07-08 (`--no-vector-paths`, wiki+maps+projects rglob) | 1,505 | 9,304 | 3,453 | 561 | 561 |

The direct-scan mode sees the 561 projects/ working-dir mirror files that paths.json excluded — they account for the component/orphan explosion and are expected. Phase 2 batch gates use direct-scan mode: unresolved must never rise above 3,453; the wiki-note orphan set must not grow.

Bugfix pulled forward from Phase 1: `scripts/build_wikilink_graph.py` `strip_frontmatter()` crashed (`'str' object has no attribute 'append'`) when a scalar key was followed by list items; now coerces to list.

## Frontmatter audit (scope: editable .md, excluding raw lanes, .trash, node_modules, .git, dot-stores)

- Total in scope: **1,494**
- No frontmatter: **41** (full list in JSON)
- YAML parse failures: **2** — `wiki/argus-drift-audit-scope-multi-agent-orchestration.md`, `wiki/hephaistos-scope-security-audit-phases-2-6.md` (mapping values not allowed — unquoted colon)
- `color-*` tag occurrences: **1,353**
- Filename-echo tag occurrences: **731**
- `created > updated` impossible orderings: **30**
- Type histogram top: wiki 459, skill 264, note 63, artifact 61, governance-doc 49, peer-review-doc 45, raw-source 41, map 38, bridge-note 32, version-genealogy 24

Scope note: the pre-plan survey counted 2,081 "editable" files because it included `projects/patent-workbench/node_modules/**` and hidden config dirs; those are excluded here and from all enrichment passes.

## Related

- [[EMERAULD_OS_ARCHITECTURE|EMERAULD Operating System]]
- [[wiki/WIKI-ROUTING-REPORT|WIKI-ROUTING-REPORT]]
