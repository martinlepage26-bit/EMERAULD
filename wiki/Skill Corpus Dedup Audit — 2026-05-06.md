---
type: audit
title: Skill Corpus Dedup Audit — 2026-05-06
aliases:
- Skill Corpus Dedup Audit — 2026-05-06
- wiki/Skill Corpus Dedup Audit — 2026-05-06
tags:
- skills
- dedup
- codex
- claude
- audit
- wiki
- skill-corpus-dedup-audit-2026-05-06-md
- subsumed
- workspace
- directories
- retired
- color-orange
status: active
created: '2026-05-06'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Skill Corpus Dedup Audit — 2026-05-06.md
backlink_count: 4
backlinks:
- '[[wiki/PHAROS Skill Corpus Change Genealogy — 2026-05-06]]'
- '[[wiki/Skill Corpus Genealogy Delta — 2026-05-06]]'
- '[[Areas/PHAROS/Skill Corpus — Complete Live Index (260 Active Skills)]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
source_roots:
  codex: /home/cerebrhoe/.codex/skills
  claude: /home/cerebrhoe/.claude/skills
---

# Skill Corpus Dedup Audit — 2026-05-06

## Executive Result

There are **no exact duplicate active skill folders inside the Codex skill root**.

The real duplication is cross-runtime mirroring:

- Codex active top-level skill folders: 260
- Claude top-level skill folders scanned: 109
- Same-name skills shared by Codex and Claude: 100
- Same-name `SKILL.md` files that are byte-identical: 87
- Same-name `SKILL.md` files that differ: 13
- Full-folder hash matches reported by `skills-dedup`: 83
- Non-directory junk in either skills root: 0

Interpretation: the corpus has **intentional mirroring**, not dangerous internal duplication. Cleanup should focus on obsolete routing entries and archive/workspace hygiene, not deleting active mirrored skills.

## Tool Output Summary

Command used:

```bash
python3 /home/cerebrhoe/.codex/skills/skills-dedup/scripts/skills_dedup.py scan --format md
```

Scanner findings:

- Codex entries: 261 directories, 0 non-directories
- Codex missing `SKILL.md`: `_backups`
- Claude entries: 109 directories, 0 non-directories
- Claude missing `SKILL.md`: `boil-the-ocean-workspace`, `ceiling-gap-compression-workspace`
- Cross-root only in Codex by name: 161
- Cross-root only in Claude by name: 9
- Cross-root identical by full content hash: 83

## Same-Name Cross-Root Duplicates

These 87 skills have byte-identical `SKILL.md` files in both `/home/cerebrhoe/.codex/skills/` and `/home/cerebrhoe/.claude/skills/`.

- `agent-evaluation`
- `agent-tool-builder`
- `ai-product`
- `api-documentation-generator`
- `app-builder`
- `architecture`
- `backend-dev-guidelines`
- `boil-the-ocean`
- `brief-to-tasks`
- `claude-api`
- `claudex`
- `clean-migrate`
- `cli-anything`
- `cli-anything-libreoffice`
- `cli-anything-mermaid`
- `cli-anything-obsidian`
- `cli-anything-ollama`
- `codex`
- `codex-review`
- `consent-framework`
- `cost-reducer`
- `data-privacy-compliance`
- `database`
- `database-schema-designer`
- `deep-research-notebooklm`
- `delegate-task`
- `design-brief`
- `design-flow`
- `design-review`
- `design-tokens`
- `dispatching-parallel-agents`
- `emerging-techniques-long-context`
- `emerging-techniques-speculative-decoding`
- `ethical-hacking-methodology`
- `exploratory-data-analysis`
- `fastapi-endpoint`
- `fastmcp-server`
- `fetch`
- `frontend-design`
- `github-actions-creator`
- `github-workflow-automation`
- `grill-me`
- `impeccable`
- `information-architecture`
- `ingest`
- `literature-review`
- `loki-mode`
- `markitdown`
- `mcp-builder`
- `mcp-integration`
- `memory-search`
- `naming-analyzer`
- `observability-phoenix`
- `openai-account-usage`
- `peer-review`
- `pharos-papers-db`
- `privilege-escalation-methods`
- `prompt-engineering`
- `receiving-code-review`
- `red-team-tactics`
- `reference-list-builder`
- `risk-management-specialist`
- `scholar-evaluation`
- `scientific-brainstorming`
- `scientific-critical-thinking`
- `scientific-visualization`
- `scientific-writing`
- `senior-data-scientist`
- `skill-development`
- `skill-discovery`
- `skill-judge`
- `skills-dedup`
- `sora`
- `systematic-debugging`
- `tabula-rasa`
- `tdd-feature-loop`
- `test-detect`
- `trailofbits-security`
- `tts`
- `ux-researcher-designer`
- `verification-before-completion`
- `web-artifacts-builder`
- `web-scraping`
- `web-tech-fundamentals`
- `webapp-testing`
- `workflow-automation`
- `writing-skills`

## Same-Name Skills That Differ Across Codex and Claude

These need review before any synchronization. Treat them as authored variants until proven otherwise.

- `agent-development`
- `agent-manager-skill`
- `agent-memory-mcp`
- `agent-memory-systems`
- `ai-agents-architect`
- `audit`
- `deploy`
- `lead-research-assistant`
- `recursive-ecosystem`
- `research-engineer`
- `research-grants`
- `self-healing`
- `statistical-analysis`

## Obsolete, Subsumed, Dropped, or Historical Entries

These are not content duplicates; they are routing-status findings from [[../governance/hephaistos/SKILL-MAP.md]].

### Active Folders With Superseded Routing

These folders still exist in Codex and Claude, but canonical routing says their work should normally route elsewhere.

| Skill | Current routing status | Route to |
|---|---|---|
| `lead-research-assistant` | SUBSUMED | HEPHAISTOS scope + `qualitative` |
| `exploratory-data-analysis` | SUBSUMED | `senior-data-scientist` |
| `deep-research-notebooklm` | SUBSUMED | `notebooklm` + `recursive-governance-method` |
| `literature-review` | SUBSUMED | `peer-reviewed-paper-writer` |
| `research-engineer` | SUBSUMED | `architecture` |
| `statistical-analysis` | SUBSUMED | `senior-data-scientist` |
| `peer-review` | SUBSUMED | `peer-reviewed-paper-writer` for academic review, `codex-review` for code review |
| `scholar-evaluation` | SUBSUMED | `recursive-governance-method` |
| `scientific-critical-thinking` | SUBSUMED | `philosopher` |

Recommendation: mark these as **routing aliases / compatibility stubs**, not deletion targets, until the active runtime is checked for direct invocation dependencies.

### Retired or Dropped Entries Already Removed From Active Roots

These are not active top-level skill folders in either Codex or Claude.

| Entry | Status |
|---|---|
| `free-tool-strategy` | retired; present only under `_retired` in Codex |
| `hermes-dependency-mapper` | dropped 2026-04-23; no active folder found |
| `hermes-escalation-router` | dropped 2026-04-23; no active folder found |
| `triangulate` | deprecated alias; removed in favor of `triangulation` |

### Historical / Formation Case

- `ma-degree-guide` is retired in the canonical map.
- Active Codex has `ma-arts-letters`, which appears to be the current standalone degree/formation skill.
- Do not recreate `ma-degree-guide` as an active skill. Keep it as a historical bridge note only.

## Archive and Workspace Hygiene

Codex top-level special directories:

- `.backups`
- `.system`
- `_backups`
- `_retired`

Claude special/workspace directories:

- `_retired`
- `boil-the-ocean-workspace` (missing `SKILL.md`)
- `ceiling-gap-compression-workspace` (missing `SKILL.md`)

These are not active skill duplicates. The only cleanup candidate is whether workspace directories should remain under the skills root or be moved to a workspace/archive location.

## Cleanup Recommendation

1. Do not delete cross-root mirrored skills; the Codex/Claude duplication appears intentional.
2. Do not auto-retire same-name differing skills; review the 13 variants manually.
3. Convert the 9 active-but-subsumed skills into explicit compatibility/alias stubs only after checking runtime invocation dependencies.
4. Keep `_backups` and `_retired` as provenance buckets, but exclude them from active inventory counts.
5. Move Claude workspace folders out of the skills root only if no tooling expects them there.

## Related

- [[PHAROS Skill Corpus Change Genealogy — 2026-05-06]]
- [[Skill Corpus Genealogy Delta — 2026-05-06]]
- [[Skill Corpus — Complete Live Index (260 Active Skills)]]
- [[Skill Map — Canonical Routed Skills (2026-05-06)]]
- [[Skill Ecosystem — Professional Capability Registry]]
- [[skills/skills-dedup]]
