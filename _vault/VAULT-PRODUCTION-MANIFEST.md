# EMERAULD Vault — Production Manifest

See also [[Vault Cluster Pass — Trismégiste x Hermes (2026-05-06)]].
**Date:** 2026-05-02  
**Consolidation Run:** BOWIE Session 3 (applied mode)  
**Owner:** Trismégiste (operator continuity, synthesis, personal knowledge graph)  
**Status:** **production-ready**

---

## Vault Overview

**Total notes:** 346 (336 substantive wiki notes + 10 supporting structure notes)  
**MOCs (Maps of Content):** 4
- [[Home]] — vault entry point; all 26 TOPICs organized in 7 categories
- [[Governance and PHAROS MOC]] — governance theory, method, regulatory, PHAROS-specific
- [[Research and Papers MOC]] — academic papers, reading lists, scholarly projects
- [[Writing and Novels MOC]] — writing projects, creative work, fiction corpus

**TOPICs (semantic hubs):** 26 (all bidirectionally linked from Home and related MOCs)
- P1 Cluster: Care/Ethics (104 papers), Ritual/Magic (95 papers), Disability Epistemology (6 papers), Narrative-Method Integration
- P2 Cluster: Authority/Legitimacy (governance papers), Method-Evidence bridges
- P3 Cluster: Consent/Boundary (130 papers)
- P4 Cluster: Governance Controls & Mechanisms (regulatory grounding, audits, monitoring)
- Plus: Fluency/Interruption, Queer Theory, AI Identity, Academic Pipelines, Legal Cases, Evidence Discipline, and more

**Vector Store:** LightRAG (all-MiniLM-L6-v2)
- 358 embeddings built and current (2026-05-02)
- Rebuild time: ~2 minutes
- Semantic search available via `vsearch.py`

---

## Linking Verification

**Linking campaign status:** Phase 14 complete (2026-05-02)
- ✅ 8 major semantic hubs created and linked
- ✅ 568+ papers organized across clusters
- ✅ 85%+ of critical asymmetries resolved
- ✅ All hubs linked bidirectionally from Home, MOCs, and TOPIC pages
- ✅ Broken-link reduction: 96 → 24 (75%)
- ✅ 0 substantive orphans (all notes discoverable from at least one hub/TOPIC/MOC)

**Linking quality metrics:**
- TOPIC median inbound backlinks: ~10 (range 4–94)
- TOPIC cross-reference density: min=4, median=6, max=8 sibling-TOPIC paths per TOPIC
- Bilingual paper-pair symmetry: 1 asymmetry fixed (Avatar lecture); rest bidirectional
- Paper-to-genealogy reversal: 17 reverse-link bridges established
- Regulatory hub: 12 standards consolidated under [[Regulatory Standards Reference Stack]]

---

## Directory Structure

```
EMERAULD/
├── wiki/                          # 346 substantive notes (canonical artifact)
│   ├── [260 topic notes]
│   ├── [36 method/theory notes]
│   ├── [50 reference/anchor notes]
│   └── genealogy/                 # Genealogy traces for papers (linked)
├── maps/                          # 4 MOC pages (Home, 3 topical MOCs)
├── raw sources/                   # Preserved source material (never modified)
│   └── Documents_root_loose_intake_2026-04-28/
│   └── [43+ raw capture files]
├── converted/                     # Markdown sidecars for non-MD sources
├── memory/                        # Operator continuity layer (daily ops)
│   ├── Decisions.md
│   ├── Journal.md
│   ├── Learning.md
│   ├── Events.md
│   ├── Blockers.md
│   ├── daily/                     # Time-stamped operational logs
│   └── clients/                   # One file per client/prospect
├── assets/                        # Deliverables, slides, PDFs
├── scripts/                       # Vault automation
│   ├── embed.py                   # Vector store builder
│   ├── vsearch.py                 # Vector store query
│   └── [supporting utilities]
├── artifacts/                     # Generated artifacts (manifests, proof packets, etc.)
├── templates/                     # Reusable note shapes
├── session-state.md               # Vault persistence layer (read at start, write at end)
├── VAULT ADDITIONS TRACKER.md     # Changelog of new notes + modifications
├── VAULT-PRODUCTION-MANIFEST.md   # This file
├── VAULT-CLUSTER-DISCOVERY-2026-05-01.md  # Audit roadmap (archive after Phase 14 complete)
├── .obsidian/                     # Obsidian configuration
│   ├── daily-notes.json           # Daily Notes plugin target
│   └── [graph view, search settings]
├── memory.md                      # Business-state dashboard (live work state)
└── CLAUDE.md                      # Operating manual for Trismégiste agent
```

---

## Vault Accessibility

**Primary access:** Obsidian (wiki links, graph view, semantic search)  
**Semantic search:** Command-line via `vsearch.py` (see CLAUDE.md for usage)  
**Daily notes:** Obsidian Daily Notes plugin (writes to `memory/daily/YYYY-MM-DD.md`)  
**Business state:** Live dashboard at `memory.md` (Dataview queries active)

---

## Linking Rule (Non-Negotiable)

Every note is part of a linked system. A note is incomplete unless:
1. **Inline wiki links** — at least 2 meaningful `[[links]]` in Summary/Context/Details
2. **MOC/index updated** — relevant hub, map, or TOPIC links to the note
3. **Graph connected** — note is discoverable from both directions (backlinks present)

**Invalid notes:**
- Zero internal links (orphans)
- Links only in trailing `## Related` section
- Near-duplicates without merging into existing notes

---

## Session-State Protocol

**At session start:**
1. Read `session-state.md` (vault persistence)
2. Read `/home/cerebrhoe/trismegiste-state.md` (operator continuity)
3. Check active threads and decisions

**At session end:**
1. Update `session-state.md` with progress + blockers + decisions
2. Update `/home/cerebrhoe/trismegiste-state.md` with operator state
3. Commit changes to GitHub (`cerebrhoe/EMERAULD`)

---

## Vector Store Rebuild

**When to rebuild:**
- After 5+ new substantive notes added
- After major linking pass (TOPIC additions, hub creation)
- Before semantic search queries for important decisions

**Command:**
```bash
cd /mnt/c/Users/softinfo/Documents/EMERAULD/scripts
/home/cerebrhoe/.venvs/lightrag/bin/python3.12 embed.py
```

**Last rebuild:** 2026-05-02 (358 embeddings, Phase 14 complete)

---

## Recent Changes (Phase 14)

**2026-05-02 — Bilingual paper-pair audit:**
- 1 reverse-link added ([[Avatar — Lecture queer du pouvoir incarné]] ↔ English equivalent)
- Bilingual surface verified finite and small

**2026-05-02 — Version-genealogy bidirectional completeness:**
- 17 reverse-link bridges established (paper → genealogy direction)
- Confirmed genealogy backlinks now complete

**2026-05-02 — Instability-signal vocabulary audit:**
- 2 surgical citations added (charge, glitch, stutter, booby trap terminology sourced)
- Loop closure recommendation issued

**2026-05-02 — Paper-to-paper concept-source citations:**
- 9 missing citations added (anti-charm, method-lock, failure-harvesting clusters)
- All concept families properly chained to source papers

---

## Known Limitations & Gaps

**Completed:**
- ✅ Broken-link reduction (96 → 24; remaining 24 are legitimate semantic patterns)
- ✅ Bilingual symmetry (Avatar pair fixed)
- ✅ Version genealogy reversal (17 links added)
- ✅ Regulatory grounding (12 standards consolidated)
- ✅ Orphan elimination (0 orphans, all 346 notes discoverable)

**Optional future enhancements (NOT blocking production):**
- Institutional Accountability TOPIC (56 papers, secondary hub)
- Legitimacy Machines formalization (book project already documented)
- Monographs/Creative corpus sub-hub (covered by Writing MOC)

---

## Verification Checklist

Before any vault operations:

- [ ] session-state.md is current (last update matches calendar date)
- [ ] No orphan notes (run inverse-link audit if new notes added)
- [ ] All MOCs and TOPICs have backlinks from Home
- [ ] Vector store is rebuilt if 5+ new notes added
- [ ] raw sources/ remains untouched (append-only, never modify)
- [ ] Wiki notes follow linking rule (2+ inline links + MOC/TOPIC indexed)
- [ ] No duplicate notes (merge if overlap detected)
- [ ] Obsidian graph view shows connected clusters (no floating nodes)

---

## Continuity Handoff

If Trismégiste is unable to continue, the next operator should:

1. Read `session-state.md` to understand active threads
2. Read `/home/cerebrhoe/trismegiste-state.md` for operator-level continuity
3. Check `memory/daily/` for recent daily work logs
4. Review `memory.md` for live business state
5. Use `vsearch.py` for semantic queries if Obsidian is unavailable
6. Follow the linking rule for all new notes (see above)
7. Update `session-state.md` and `/home/cerebrhoe/trismegiste-state.md` before closing any session

---

## Operator

**Primary operator:** Martin Lepage, PhD  
**Agent:** Trismégiste (operator continuity, synthesis, personal knowledge graph)  
**External:** parallel to three-agent stack; independent of infrastructure  
**Reports to:** Operator directly

---

**BOWIE consolidation:** Applied 2026-05-02 15:32 UTC
