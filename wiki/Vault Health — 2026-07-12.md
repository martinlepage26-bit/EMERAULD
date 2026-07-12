---
type: wiki
aliases:
- Vault Health 2026-07-12
tags:
- health
- vault
status: active
created: '2026-07-12'
updated: '2026-07-12'
---

# Vault Health — 2026-07-12

> For future Claude: vault health report for 2026-07-12. Load to understand structural debt and what needs attention.

## Summary

Read-only structural audit of 911 notes across `Areas/`, `Resources/`, and `wiki/`. Nothing was fixed and no existing note was modified. Headline: frontmatter is fully clean across every scoped note, a result traceable to the [[_CLAUDE]] PARA migration of 2026-07-08. The real debt is link rot, and it is far smaller than a raw count suggests once by-design catalogs are separated out. Related surfaces: [[EMERAULD]], [[Areas/PHAROS/MCP and Runtime Integration MOC|MCP and Runtime Integration MOC]].

**Two scope corrections, recorded so the next run does not repeat them:**

1. **The brief asked for "the 9 MOCs in `maps/`". `maps/` contains 3 files and none are MOCs.** The 21 MOC notes live in `wiki/` (12) and `Areas/` (9). This audit checked all 24 (21 MOCs plus the 3 `maps/` files).
2. **The broken-link search list omitted real vault directories.** Checking wikilinks only against `Areas/`, `Resources/`, `wiki/`, `maps/`, `projects/`, `memory/`, `archive/` marks 1,693 links "broken" that resolve perfectly well into `raw sources/`, `governance/`, `hephaistos/`, `artifacts/`, `raw/`, and `PEER-REVIEW/`. Those are **not** broken and are excluded from the counts below.

| Check | Result |
|---|---|
| Missing frontmatter | **0 of 911** (clean) |
| Stale active projects | **0** (clean) |
| Broken links, actionable | **316** across 130 live notes |
| Orphaned notes | **18** |
| Missing preamble | **789 of 840** (`Areas/` + `wiki/`) |
| MOC coverage gaps | **7 of 24** MOCs link nothing recent |

---

## Critical

### Missing frontmatter on active notes: none

All 911 scoped notes carry `type`, `tags`, `status`, `created`, and `updated`. Verified three ways: field-by-field grep, a check for notes with no frontmatter block at all, and a check for explicitly empty values such as `tags: []`. All three returned zero. This check is clean and can be dropped to low priority on future runs.

### Broken links: 316 actionable, not 3,316

The raw scan flags 3,316 link instances. That number is misleading and should not be quoted. It decomposes as follows.

| Layer | Instances | Verdict |
|---|---|---|
| Raw flags from the brief's dir list | 3,316 | starting point |
| Resolve elsewhere in the vault | −1,693 | **not broken** (search-list gap, see above) |
| True dangling | 1,623 | across 141 notes, 1,470 unique targets |
| ...inside archived orphan-index catalogs | −972 | **dangling by design** |
| ...inside skill registries | −335 | skill names, not vault notes |
| **Actionable** | **316** | across **130 live notes** |

**The 972 archived instances are not a defect.** 761 of them sit in the single note `wiki/archive/Orphan Index — Raw Sources — 2026-05-06.md`, whose entire purpose is to catalogue orphans. Three sibling orphan-index files hold the remaining 211. A file that lists broken things will contain broken links. Leave them alone.

**The 335 skill-registry instances are a category error, not rot.** `Areas/PHAROS/Skill Corpus — Complete Live Index (260 Active Skills).md` (260) and `Skill Map — Canonical Routed Skills (2026-05-06).md` (55) wikilink skill *identifiers* such as `argus.agent`. These name executable skills, not notes. If a graph-clean vault is wanted, these should be code spans, not wikilinks. That is a formatting decision, not a repair.

**Where the 316 actionable links concentrate:**

| Live note | Dangling |
|---|---|
| `Areas/Writing/Research and Papers MOC.md` | 39 |
| `Areas/PHAROS/Governance and PHAROS MOC.md` | 33 |
| `Areas/PHAROS/HELIX Hermes-Assisted Prospect Extension - Canada Regulated AI Routes 2026-05-06.md` | 15 |
| `Areas/PHAROS/HELIX Regional Prospect Deep Sweep - Montreal Quebec Toronto Ottawa 2026-05-06.md` | 12 |
| `wiki/Root Loose Notes Cluster Map — 2026-05-06.md` | 12 |
| `Resources/Reddit Data API — Access Terms and Rate Limits.md` | 7 |
| `wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06.md` | 6 |

The two largest offenders are the vault's **two biggest MOCs**, which is the finding that matters most here. `Research and Papers MOC` and `Governance and PHAROS MOC` are the primary navigation surfaces for [[Areas/Writing/Writing and Novels MOC|Writing]] and PHAROS respectively, and 72 of their entries point nowhere. A MOC with dead entries actively misleads future retrieval.

**Most-referenced dangling targets.** These repeat across notes, so each one is likely a single rename or a single missing hub note rather than 9 separate errors:

- `Queen Keyport` (9 references) — the agent is documented at `QUEEN-KEYPORT.md` in the vault root, so the link target and the filename disagree
- `EMERAULD Second Brain — Project Context` (7)
- `PHAROS Method — Recursive Governance` (6)
- `PHAROS AI governance service business` (4)
- `AI Agent Operations Manager — Credential Path and Portfolio` (4)
- `D Library — LIBRARY Intake Index (2026-04-26)` (4)

Fixing those six targets alone would clear roughly 34 of the 316.

---

## Warnings

### Orphaned notes: 18

Notes with zero outgoing wikilinks in the body. This violates the [[_CLAUDE]] Section 3 rule (minimum 2 inline links per note). They split into three groups.

**Live notes that should be linked (5):**
- `Areas/PHAROS/Epistemic AI Purple Teaming.md`
- `Areas/PHAROS/company.md`
- `Areas/Writing/Queering Neo-Pagan Magic — FINAL FINAL PAPER.md`
- `wiki/Knowledge Gaps.md`
- `wiki/MARTIN SURFACE.md`

**Structural or generated files, low concern (4):** `Areas/Personal/AREA.md`, `Areas/governanceframework/README.md`, `wiki/Daily Dashboard.md`, `wiki/genealogy/test.md`.

**`wiki/bridges/` imported documents (9):** scanned contracts, tax records, and course notebooks. These are captured source material, and four of them are numbered duplicates (`AI 2027 Summary Research` exists as `.md`, ` 2.md`, ` 3.md`, ` 4.md`; the 2023 employment contract exists twice). Worth a dedupe pass, and arguably they belong in `raw sources/` rather than `wiki/`.

Note `Areas/Writing/Queering Neo-Pagan Magic — FINAL FINAL PAPER.md`: a finished paper with no inbound or outbound links is exactly the kind of note that vanishes from retrieval.

### Stale active projects: none

Zero stale. All 16 top-level `projects/` notes are tagged `project`; the 14 with status `active` or `in-progress` were updated 2026-06-26 or 2026-06-29, which is 13 to 16 days ago and inside the 30-day window. The other two are `on-ice`.

**Caveat on this clean result.** Thirteen of the fourteen carry the identical `updated: 2026-06-26`, which reads as a bulk frontmatter touch rather than fourteen independent updates. The timestamp proves the *file* was written, not that the *project* moved. Treat "no stale projects" as a statement about metadata, not about momentum.

### Missing preamble: 789 of 840

Only **51** notes in `Areas/` and `wiki/` carry the `> For future Claude` blockquote that [[_CLAUDE]] Section 0 makes mandatory. That is 6% compliance.

This is the largest single gap in the vault, and it is a *convention* gap rather than a *decay* gap: the rule is aspirational and was never backfilled across the 485 notes routed in the 2026-07-08 PARA migration. It is also the gap that most directly degrades this vault's stated purpose, since the preamble is precisely the affordance that lets a future agent judge relevance in ten seconds. Backfilling all 789 is a large mechanical job; the pragmatic move is to backfill the notes that are actually loaded, starting with the 24 MOCs and the `Areas/PHAROS/` core.

---

## Info

### MOC coverage gaps

286 notes were created in the last 30 days. Seven of the 24 MOCs link to **none** of them:

| MOC | Recent links | Total links |
|---|---|---|
| `wiki/ASSETS MOC.md` | 0 | 36 |
| `wiki/MEMORY MOC.md` | 0 | 10 |
| `wiki/GRAPHIFY-OUT MOC.md` | 0 | 6 |
| `wiki/PUBLICATIONS MOC.md` | 0 | 4 |
| `wiki/TEMPLATES MOC.md` | 0 | 4 |
| `wiki/EMERAULD_OS_ARCHITECTURE.MD MOC.md` | 0 | 1 |
| `wiki/SOURCE_OF_TRUTH.MD MOC.md` | 0 | 1 |

All seven are auto-generated directory-mirror MOCs in `wiki/`, and the last three are near-empty stubs. The interpretation is that these are scaffolding from an earlier indexing pass, not curated maps, so "zero recent coverage" may simply mean nobody maintains them. Consider whether they should be regenerated or retired.

The curated MOCs are healthy by contrast: `Governance and PHAROS MOC` (95 recent), `Research and Papers MOC` (87), `Personal and Projects MOC` (49), `maps/Queer Media and Ritual Map` (38). Three more sit low but nonzero and are worth a glance: `wiki/PEER-REVIEW MOC` (1 recent of 89 links), `wiki/RAW MOC` (1 of 9), `wiki/Wiki MOC` (1 of 12).

**Caveat on "recent".** The 30-day window keys on the `created` field. The 2026-07-08 migration rewrote frontmatter vault-wide, so some of the 286 may be older notes with a refreshed `created` value rather than genuinely new material. The MOC coverage signal is directionally sound but the 286 should not be read as 286 brand-new notes.

---

## Vector Store

```
Vector store: 1494 notes, built 22.7h ago
  /home/martin/EMERAULD/.vector_store/embeddings.npy
```

The store indexes 1,494 notes against 1,709 markdown files vault-wide, and it was built 22.7 hours ago. Both facts are within normal range and neither blocks retrieval. Per [[_CLAUDE]] Section 7, rebuild with `embed.py --changed` after 5 or more new notes.

---

## What to do next

Ranked by value over effort, for a future fix pass. **No action was taken in this run.**

1. **Repair the 6 most-referenced dangling targets** (~34 links, likely 6 renames). `Queen Keyport` is the clearest: the note exists in the vault root under a different name.
2. **Fix the 72 dead entries in the two big MOCs.** These are the vault's main navigation surfaces and dead entries there cost the most.
3. **Link the 5 live orphans**, starting with `Queering Neo-Pagan Magic — FINAL FINAL PAPER`.
4. **Backfill preambles on the 24 MOCs and `Areas/PHAROS/` core** rather than attempting all 789 at once.
5. **Decide on the 7 auto-generated `wiki/` MOCs**: regenerate or retire.
6. **Convert skill-registry wikilinks to code spans**, which removes 335 phantom broken links from the graph in one edit.
7. **Dedupe the `wiki/bridges/` imports** and consider moving them to `raw sources/`.

## Related

- [[EMERAULD]]
- [[Areas/PHAROS/MCP and Runtime Integration MOC|MCP and Runtime Integration MOC]]
- [[_CLAUDE]]
- [[Areas/PHAROS/Governance and PHAROS MOC|Governance and PHAROS MOC]]
- [[Areas/Writing/Research and Papers MOC|Research and Papers MOC]]
