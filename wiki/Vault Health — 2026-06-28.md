---
type: wiki
title: Vault Health — 2026-06-28
tags:
- health
- vault
- wiki
- bulk
- wikilinks
- mocs
- zero
- maps
status: active
created: '2026-06-28'
updated: '2026-06-28'
vault_area: wiki
canonical_path: wiki/Vault Health — 2026-06-28.md
backlink_count: 8
backlinks:
- '[[wiki/EMERAULD]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-003]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[memory/daily/2026-06-28]]'
---

> For future Claude: vault health report for 2026-06-28. Load to understand structural debt and what needs attention.

## Summary

Report-only structural scan of [[EMERAULD]] `wiki/` (563 notes) plus `maps/` (3 topic maps) and the 9 MOCs. Nothing was modified. Headline numbers: **0 notes missing frontmatter**, **388 truly-dangling wikilinks across 123 notes**, **6 orphans**, **558 of 563 notes missing the `> For future Claude` preamble**, and a **bulk timestamp reset** (every note stamped `updated: 2026-06-26` or `2026-06-27`) that has erased the recency signal the stale-project and MOC-recency checks depend on. See [[MCP and Runtime Integration MOC]] for the runtime/tooling surface most affected by cross-directory links.

Scope note on method: the brief specified "9 MOCs in `maps/`", but all 9 MOCs actually live in `wiki/`; `maps/` holds only 3 topic maps (Novel Corpus, PHAROS Method, Queer Media and Ritual). Link resolution counts a target as valid if it matches a `wiki/` or `maps/` filename or a frontmatter alias. "Broken" links are split into **dangling** (target exists nowhere in the vault) and **cross-directory** (target resolves to a real file outside `wiki/`+`maps/`, e.g. `projects/`, `memory/`, `archive/`).

---

## Critical

### Missing frontmatter — CLEAN
All 563 `wiki/` notes carry every required field (`type`, `tags`, `status`, `created`, `updated`). No action needed.

### Broken (dangling) links — 388 across 123 notes
These wikilinks point to targets that exist **nowhere** in the vault (not `wiki/`, `maps/`, or any other directory). 242 distinct missing targets.

Worst-offender notes:

| Note | Dangling links |
|------|----------------|
| Research and Papers MOC | 65 |
| Governance and PHAROS MOC | 46 |
| Writing and Novels MOC | 35 |
| Mythocritique to PHAROS — The 2010 Master's Thesis as Methodological Keystone | 11 |
| Root Loose Notes Cluster Map — 2026-05-06 | 9 |
| Reddit Data API — Access Terms and Rate Limits | 8 |
| Martin Lepage Publications — Annotated Bibliography and Verification Leads | 7 |
| Elemental Agents — Productization Plan (2026-05-24) | 6 |
| Source Cluster — 2026-05-13 Client and Operator Continuity | 6 |

The three big MOCs account for 146 of the 388 (38%) — they index notes that were renamed, merged, or never created.

Most-repeated missing targets (signal of systemic causes):

- **Code/repo artifacts leaked from ingested READMEs**: `HISTORY` (14), `CHANGELOG` (6), `LICENSE`/`license` (6), `THREAT_MODEL`, `MockCallHistory`, `MockPool`, `writing-tests`. These are not knowledge notes — they are scaffolding from ingested code repos and should be unlinked or stripped.
- **Phantom knowledge notes** (referenced but never created / since renamed): `PHAROS AI governance service business` (4), `AI Agent Operations Manager — Credential Path and Portfolio` (4), `EMERAULD — Vault and Knowledge Graph` (3), `EXTERNAL DATA REGISTRY (Phase 1 Build)` (3), `Second Self System — Adversarial Review` (3), `ACTOR Framework Worksheet` (2).
- **Raw-source slugs** pointing at intake files that were trashed or never synthesized: `2026-05-09_emerauld-agents-perplexity-hermes-instructions` (3), `2026-04-30_inderscience-ijaighr-submission-pipeline` (3), `2026-04-18_anthropic-openclaw-...` (2).
- **Heading/section fragments mistyped as links**: `Introduction`, `FIRST DRAFT`, `History`, `summary`, `Literature Review …`, and bracket-truncated targets like `2015 - policy_or_guidance [3`.

---

## Warnings

### Orphans — 6 notes with zero outgoing wikilinks in body
- `2026 - Mauss - The Gift.md`
- `Daily Dashboard.md`
- `Epistemic AI Purple Teaming.md`
- `Knowledge Gaps.md`
- `MARTIN SURFACE.md`
- `Queering Neo-Pagan Magic — FINAL FINAL PAPER.md`

Each violates the non-negotiable linking rule (≥2 inline links). `Daily Dashboard` and `MARTIN SURFACE` are likely dashboard/index notes that should at minimum link their constituents; the two papers and the Mauss source should link into their MOCs.

> [!warning] Contradiction detected
> [[EMERAULD Graph Architecture — Link Density and Vector Layer (2026-05-25)]] reports **0 zero-backlink notes** after the 2026-06-26 enrichment pass, and the recent graph commit "enforce zero-orphan rule" claims the vault has **0 orphans**. This scan reports **6 orphans**. The two are not actually in conflict — they measure different things. The graph store's "orphan / zero-backlink" = a note with zero *incoming* wikilinks (nothing links **to** it). This scan's "orphan" = a note with zero *outgoing* wikilinks in its body (it links **to** nothing), which is what the `_CLAUDE.md` ≥2-inline-links rule actually governs. A note can be richly linked-to yet still link to nothing itself, so it passes the graph's zero-orphan rule while failing the linking rule. Reconciliation: keep both checks but disambiguate the term — call the graph metric "zero-inbound" and reserve "orphan" for the zero-outbound case the linking rule cares about.

### Stale active projects — 0 by literal test, but the test is BLIND right now
The literal check (tag/type `project` + `status: active` + `updated` older than 30 days) returns **0**. This is a false negative, not a clean bill of health: **every one of the 563 notes was bulk-stamped `updated: 2026-06-26` (556) or `2026-06-27` (7)** — only two distinct dates in the whole vault. This matches the recent `frontmatter normalization` / graph-topology commits in git status. 119 notes carry a project tag/type and all read `status: active`, so the moment a genuine edit-recency signal is needed, it does not exist. **Recommendation: stop overwriting `updated` in bulk passes, or move bulk-touch timestamps to a separate field (e.g. `graph_touched`) so `updated` keeps reflecting real content edits.**

### Missing `> For future Claude` preamble — 558 of 563 notes (systemic)
Only 5 notes carry the preamble required by `_CLAUDE.md` Section 2:
- `Railway — COMPASSai Production Deployment Platform`
- `Obsidian Second Brain Integration — EMERAULD Setup (2026-06-21)`
- `Weekly Review — 2026-06-26`
- `if.switchboard — InfraFabric Product Center`
- `COMPASSai — EU AI Act Classifier Expansion and Quebec Construction Module (2026-06-22)`

The preamble rule post-dates almost the entire vault, so this is structural debt rather than per-note negligence. Backfilling 558 preambles is a batch job, not a blocker; prioritize high-traffic notes (MOCs, dashboards, active project states) first.

---

## Info

### MOC coverage — check is currently unreliable
The brief asks whether each of the 9 MOCs links to notes "added in the last 30 days." Because the bulk timestamp reset makes **all 563 notes appear ≤30 days old**, this check cannot distinguish genuinely-new notes from bulk-touched ones — so no MOC can be flagged as "missing recent notes" with confidence. Raw outbound-link counts (links resolving to current `wiki/` notes) per MOC, for reference:

| MOC | Resolving note-links |
|-----|----------------------|
| Governance and PHAROS MOC | 290 |
| Research and Papers MOC | 246 |
| Personal and Projects MOC | 154 |
| Writing and Novels MOC | 114 |
| Pagan and Queer Ritual Studies MOC | 75 |
| Manuscript Pipeline MOC | 40 |
| Legitimacy Machines MOC | 36 |
| Control Protocols MOC | 33 |
| MCP and Runtime Integration MOC | 19 |

`MCP and Runtime Integration MOC` (19) and `Control Protocols MOC` (33) are the thinnest indexes — candidates for a coverage sweep once a real recency signal is restored.

### Cross-directory links — 4,261 links across 309 notes (scope note, not breakage)
Per the brief's narrow definition (anything not in `wiki/` or `maps/` is "broken"), 4,261 wikilinks would qualify — but they resolve to **real files** in operational surfaces the vault deliberately references: `_vault/` (351), `skills/` (320), `memory/` (316), `archive/` (257), `projects/` (79), `raw/` (74), `governance/` (56), and others. These are functional cross-surface references, not dead links. Flagged only so a future "fix broken links" pass does not mass-delete them. One subset to watch: ~73 links pointing into `.trash/` — those genuinely point at discarded content and should be treated as broken on a later cleanup pass.

---

## Vector Store

```
Vector store: 909 notes, built 22.9h ago
  /home/martin/EMERAULD/.vector_store/embeddings.npy
```

The store indexes 909 entries vs. 563 current `wiki/` notes + 3 maps + projects — consistent with coverage of `wiki/`, `maps/`, and `projects/`. Built 2026-06-27 22:03 (~23h before this scan). No rebuild required for a report-only pass; rebuild after any remediation that adds or removes 5+ notes.

---

## Related

- [[EMERAULD]]
- [[MCP and Runtime Integration MOC]]
- [[Vault Health — 2026-07-05]] — next report in the series
