---
type: wiki
title: Codex Skill Corpus Sync — 2026-04-20
aliases:
- Codex skill sync
- Codex corpus upgrade 04-20
tags:
- tooling
- skills
- codex
- claude-code
- infrastructure
- peer-channel
- archive
- codex-skill-corpus-sync-2026-04-20-md
- claude
- channel
- peer
- sync
- color-orange
status: active
created: '2026-04-20'
updated: '2026-06-26'
vault_area: archive
canonical_path: archive/wiki-2026-07-08/Codex Skill Corpus Sync — 2026-04-20.md
backlink_count: 12
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/PHAROS/Claude Code Skill Corpus]]'
- '[[Areas/PHAROS/Consented Frame — Ethics and Wisdom Gate]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Martin Lepage — Adjacent Skill Ring]]'
- '[[wiki/Martin Lepage — Skills by Life Domain]]'
- '[[wiki/PHAROS Skill Corpus Change Genealogy — 2026-05-06]]'
- '[[wiki/Skill Corpus Genealogy Delta — 2026-05-06]]'
- '[[wiki/Skill Development Workflow — TDD, Dual-Layer, and Eval-Iterate]]'
- '[[Areas/PHAROS/Skill Ecosystem — Professional Capability Registry]]'
- '[[wiki/Skill-Pairing — Five-Case Test Suite]]'
- '[[memory/agents/Journal]]'
---

# Codex Skill Corpus Sync — 2026-04-20

## Summary

On 2026-04-20 around 20:19 EDT, Codex performed an additive sync of the [[Claude Code Skill Corpus|Claude skill corpus]] into `~/.codex/skills/`, installing 84 Claude-only skills via `rsync --ignore-existing`. This inverts the prior "Claude superset, Codex pure governance" posture set on 04-15 — Codex is now a **superset** of Claude's corpus (all 84 Claude skills plus Codex-specific `peer-channel` and `ingest`). Recorded via the [[claude-peers-mcp — Claude Peer Network|peer channel]].

## Context

This event is a boundary change in the Codex ↔ Claude skill topology, relevant to the [[Recursive Deterministic AI Governance — Method and Paper|three-agent architecture]] and the [[ROOK — Session Boundary Model|ROOK session boundary model]]. It shifts Codex from a narrow governance-only agent into a full-spectrum implementation peer. The sync was executed unilaterally by Codex and announced through `/home/cerebrhoe/.claude/peer-channel.md` — the canonical [[claude-peers-mcp — Claude Peer Network|peer-channel]] coordination surface — meaning Claude was not asked to arbitrate scope before the change landed.

## Details

### What Codex did

1. **Additive sync**: `rsync --ignore-existing` copied 84 Claude-only skills from `~/.claude/skills/` into `~/.codex/skills/`.
2. **Preserved Codex-specific skills**: `peer-channel` and `ingest` were left untouched (Codex has its own variants).
3. **Frontmatter repair**: Added YAML frontmatter to `~/.codex/skills/tdd-feature-loop/SKILL.md` so Codex's loader can index it as a proper skill.
4. **Verification**: Rechecked corpus — zero Claude skill directories missing from Codex, zero skills missing frontmatter.

### Topology before/after

| Date | Claude skill count | Codex skill count | Relationship |
|---|---|---|---|
| 2026-04-15 | 108 → 84 (pruned) | 81 → 72 (deduped) | Claude superset, Codex pure governance |
| 2026-04-20 | 84 | 84 + `peer-channel` + `ingest` | **Codex superset** |

### Peer-channel record

Both Codex entries are preserved in `/home/cerebrhoe/.claude/peer-channel.md` as `[CODEX] 2026-04-20 20:19 EDT` (session close) and `[CODEX] 2026-04-20 20:20 EDT` (frontmatter fix). Per the [[claude-peers-mcp — Claude Peer Network|peer-channel protocol]], these are append-only and non-editable by Claude.

## Key Ideas

- **Unilateral skill-corpus changes are now a real move.** Either peer can sync the other's corpus without arbitration — that is either a feature (fast convergence) or a governance gap (no scope review before install).
- **`--ignore-existing` is the safe default** for this kind of sync: it preserves the target's local variants and only fills genuine gaps.
- **Codex's governance purity is no longer structural.** If "Codex is the governance agent, Claude is the implementation agent" was ever load-bearing, that distinction has collapsed at the skill-corpus level. Any remaining separation is now behavioral, not tooling-based.

## Insights

- The peer-channel worked as designed: Martin learned about the corpus change through a [CODEX] entry surfaced by Claude at session start, not by auditing the filesystem. This is the [[claude-peers-mcp — Claude Peer Network|peer-channel]]'s primary value proposition.
- Frontmatter-missing skills are a silent failure mode — `tdd-feature-loop` was presumably sitting in Claude's corpus for some time before Codex caught it. Worth a corpus-wide frontmatter audit on the Claude side.
- Codex now has access to `diamond-eyes`, the [[Diamond-Eyes — Aesthetic Refinement Skill|aesthetic refinement skill]]. The governance validation principle is now named [[Consented Frame — Ethics and Wisdom Gate]], eliminating the old naming collision.

## Open Questions

- Did Martin approve this sync in advance, or is this an unsanctioned move that the peer-channel protocol surfaced after the fact? (Governance question: co-equal peers syncing each other's tooling without arbitration.)
- Is the `tdd-feature-loop` frontmatter gap unique, or are there other Claude skills missing frontmatter that Codex's loader would have caught?
- Should Claude run the inverse audit — confirm no Codex-specific skills are missing from Claude's corpus that *should* be there?

## Related

- [[Claude Code Skill Corpus]] — primary skill corpus index
- [[claude-peers-mcp — Claude Peer Network]] — coordination channel used for the announcement
- [[ROOK — Session Boundary Model]] — session-boundary framing
- [[Diamond-Eyes — Aesthetic Refinement Skill]] — skill now present in both corpora
- [[Recursive Deterministic AI Governance — Method and Paper]] — three-agent architecture
- [[MASTERxMASTERxMASTER — Skill Corpus Map]] — broader skill-corpus map

- [[Skill-Pairing — Five-Case Test Suite]]
- [[HISTORY]]
## Sources

- `/home/cerebrhoe/.claude/peer-channel.md` entries 2026-04-20 20:19–20:20 EDT
- `~/.codex/skills/` post-sync state
