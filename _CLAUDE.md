---
type: agent-instructions
title: EMERAULD Vault — Second Brain Operating Rules
aliases:
- EMERAULD Vault — Second Brain Operating Rules
tags:
- agents
- ai
- agent-instructions
- lavoie
- save
- yyyy
- emerauld
status: active
created: '2026-06-26'
updated: '2026-06-26'
vault_area: _CLAUDE.md
canonical_path: _CLAUDE.md
backlink_count: 1
backlinks:
- '[[index]]'
---

# EMERAULD Vault — Second Brain Operating Rules

> This file is read by obsidian-second-brain before any vault operation.
> Full vault documentation lives in `CLAUDE.md`. Where this file is silent, defer to `CLAUDE.md`.

---

## Section 0 — AI-First Vault Rule

Every note Claude writes must be self-contained for future Claude:
- **"For future Claude" preamble** — 2-3 sentence summary at the top so relevance is assessable in 10 seconds
- **Rich frontmatter** — `type`, `aliases`, `tags`, `status`, `created`, `updated` (see format below)
- **Recency markers** — "X raised $24M (as of 2026-04, source-url)" so future Claude knows what to verify
- **Verbatim source quotes** — every external claim has a source URL inline
- **Wikilinks mandatory** — every person, project, concept, decision uses `[[wikilinks]]`; minimum 2 inline links per note (not just in Related section)
- **Confidence levels** — `stated | high | medium | speculation` where applicable

---

## Section 1 — Vault Path and Structure

**Vault root:** `/home/martin/EMERAULD`

**Primary note routing (PARA, since 2026-07-08 migration):** new durable notes go to the matching `Areas/` subfolder or `Resources/`; only vault-machinery and genuinely unroutable notes go to `wiki/`.

**Directory map:**
```
Areas/PHAROS/  ← PHAROS business, products, governance architecture, agents/skills (largest area)
Areas/Writing/ ← manuscripts, papers, queer/pagan studies, novels, version genealogies
Areas/Personal/← personal life, legal, health, home
Areas/Lavoie/  ← Groupe Lavoie client engagement
Resources/     ← annotated sources, reference stacks, external tool specs, frameworks
Inbox/         ← captures awaiting routing (status: inbox)
wiki/          ← vault-machinery notes, skill-corpus mirrors (wiki/skills/), hubs, residual legacy (~100 top-level)
maps/          ← MOCs and topic indexes (7+ page topics)
projects/      ← per-project state files (top level) + mirrored working dirs (subfolders)
resources/     ← (lowercase, legacy) small reference docs; new reference material goes to Resources/
raw/           ← verified source files after hard-move (immutable)
raw sources/   ← unsynthesized captures, preserve as-is, NEVER overwrite or delete
templates/     ← note templates
assets/        ← deliverables, slides, PDFs
artifacts/     ← generated outputs and reports
governance/    ← governance docs and protocols
memory/        ← daily logs (memory/daily/) and client files (memory/clients/)
archive/       ← archived registers + archive/wiki-2026-07-08/ (migrated dated ops notes) + archive/retired-2026-07-08/ (retired subsystems)
docs/handoff/  ← build-turn handoff documents per STANDARD-BUILD-ORDER
```
485 wiki notes were routed into this layout on 2026-07-08 — manifest at `_vault/PARA-MIGRATION-MANIFEST-2026-07-08.md`.

**When obsidian-second-brain says "save to vault root":** route per the PARA map above (never vault root).
**When obsidian-second-brain says "save to raw/":** save to `raw sources/` (EMERAULD's intake lane).
**Do not create new top-level directories** without updating `CLAUDE.md`.

---

## Section 2 — Note Format (overrides obsidian-second-brain defaults)

```yaml
---
type: wiki          # wiki | map | raw | project | resource | artifact
aliases: []
tags: []
status: active      # active | archived | draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```

Then body structure:

```markdown
> For future Claude: [2-3 sentence preamble — what this note is, why it matters, when to load it]

## Summary
Short summary with at least one contextual [[wikilink]].

## Context
How this connects to [[projects]], [[people]], and concepts.

## Details
Main content. All projects, concepts, tools, decisions, people must be linked inline.

## Related
- [[Note Name]]
```

**No `ai-first: true` field** — EMERAULD does not use that frontmatter key.
**Language:** bilingual EN/FR — research and governance content may be in either language.

---

## Section 3 — Linking Rules (non-negotiable)

A note is not complete until:
1. At least 2 meaningful inline wikilinks in the body (not just Related)
2. A relevant MOC or map in `maps/` links to the new note
3. VAULT ADDITIONS TRACKER entry written in the same response

Before creating any note, search `wiki/` for related material. Prefer updating existing notes over creating new ones.

---

## Section 4 — Raw Source Protection

- `raw sources/` — NEVER overwrite, delete, or modify. Preserve verbatim.
- `raw/` — verified hard-moved files. Immutable after move.
- When `/obsidian-ingest` processes a URL or file: save original to `raw sources/`, then rewrite or create the wiki note in `wiki/`.

---

## Section 5 — Self-Rewriting Rules

When updating existing notes:
- **Bi-temporal facts**: never delete old values; add to `timeline:` frontmatter array
- **Contradictions**: flag with `> [!warning] Contradiction detected` callout, then reconcile
- **Append vs rewrite**: rewrite the Summary and Details sections; append to Related and timeline
- **No orphans**: every updated note must still satisfy the linking rule above

---

## Section 6 — Existing Agents

- **Trismégiste** — primary vault agent; handles continuity via `session-state.md` and [[Areas/PHAROS/Trismégiste — Operator State]] (no standalone trismegiste-state file exists on this host — corrected 2026-07-08)
- **Argus** — paired audit agent for file-surface coherence checks
- obsidian-second-brain commands operate **alongside** Trismégiste, not as a replacement

---

## Section 7 — Vector Search

EMERAULD has a local Python vector store. Do not attempt to install QMD or external semantic search.

```bash
# Query:
cd /home/martin/EMERAULD/scripts
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "your question"
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "question" --top 10
/home/martin/.venvs/emerauld/bin/python3 vsearch.py "question" --full

# Rebuild after 5+ new notes:
/home/martin/.venvs/emerauld/bin/python3 embed.py --changed
```

---

## Section 8 — VAULT ADDITIONS TRACKER

Every time a note is created or significantly updated, write one line to `_vault/VAULT ADDITIONS TRACKER.md`:
```
YYYY-MM-DD | [[Note Title]] | one-sentence summary of what was added and why it matters
```

---

## Section 9 — Vault Identity

- **Owner:** Martin Lepage, PhD — AI governance consultant + solo developer
- **Contact:** ml@pharos-ai.ca (professional) · martinlepage.ai@gmail.com (personal, never surfaced)
- **Purpose:** Personal knowledge base + PHAROS governance product proof-of-concept + academic writing substrate
- **Vault root:** `/home/martin/EMERAULD`
- **Last updated:** 2026-06-29

---

## Section 10 — Verify Live State Before Acting

Before declaring a bug, drafting a fix, or writing architecture: read the actual code, schema, deployed branch, env, or live data. Speculation from stale context produces drafts that contradict reality.

- Read the schema or types before declaring a bug — real field names live in the code, not in memory
- `git fetch origin` and check the deployed branch, not local main
- Grep the live file before any anchor-based patch
- Fetch live dates and rates — never infer from training data
- Verify env vars in the running process before blaming code

---

## Section 11 — Auto-Save Rules

**Save automatically (no prompt needed):**
- Decisions made in conversation → relevant project note + `memory/daily/YYYY-MM-DD.md`
- Notes created or significantly updated → `_vault/VAULT ADDITIONS TRACKER.md` (same response)
- Architecture or ADR content → wiki architecture note, link from daily log
- Dev work or script changes → `Logs/YYYY-MM-DD.md` entry + architecture notes if applicable

**Ask before saving:**
- Anything touching `memory/clients/` (client-sensitive)
- Anything touching `assets/invoices/` or financial documents
- Archiving or deleting existing notes
- Creating a new top-level directory

---

## Section 12 — Active Context

*Update this section at the start of each major work sprint.*

**Current top priorities (as of 2026-07-08):**
1. Lavoie contract v5 signature — ~July 13 window; P0 items in `~/Lavoie/review-gate-signature-2026-07-06.md`; vault state at [[Areas/Lavoie/Contrat PHAROS x Groupe Lavoie — v5 Signature Track (2026-07-08)]]
2. HELIX outreach — EU AI Act window closes 2026-08-02 (~25 days); send one message to Humania or Koios; draft in [[Areas/PHAROS/HELIX — Value Proposition and Buyer Profile]]
3. EMERAULD OS build Stage 2 — MCP surface wiring per [[governance/EMERAULD-OS-SPEC — MCP Surface]]; sequence in [[governance/EMERAULD-OS-BUILD-ORDER]]
4. Gumroad listing publish — copy ready at `artifacts/marketplace/promo/gumroad-listing.md`; upload zip is `assets/obsidian-agent-vault-2026-06-29.zip`; manual browser action remaining
5. GAIA soft launch — v1.6 built, 39/39 tests pass; name 10 people, send TestFlight/APK

**2026-07-08 vault overhaul:** full PARA migration + frontmatter overhaul + VM sync + OS build order executed — see [[docs/handoff/vault-overhaul-2026-07-08]] and session-state.md. Both Lavoie contradictions resolved by operator decision (entity split; two-workstream framing).

**Key people:**
| Person | Role |
|--------|------|
| Patricia | Martin's sister; relay at Groupe Lavoie (collects A1–A5 gates from Israël + Guillaume) |
| Israël Lavoie | Groupe Lavoie — grand patron |
| Guillaume Lavoie | Groupe Lavoie — co-owner, signs gate A5 |
| Jade | Base44 developer; handoff at `Lavoie/jade-base44-handoff.md` |

**Lavoie disambiguation:** `memory/clients/Lavoie Construct.md` = April 2026 excavation SOP client (different entity). `Areas/Lavoie/AREA.md` = Groupe Lavoie (SOS Plomberie, Excavations Lavoie, GVI). Do not conflate.
