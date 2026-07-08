---
type: wiki
title: HENRY — Research Paper Writing System
aliases:
- HENRY
- paper writing
- research assistant
- peer review
- wiki/HENRY — Research Paper Writing System
tags:
- research
- writing
- academic
- voice
- workflow
- wiki
- henry-research-paper-writing-system-md
- henry
- paper
- bundle
- spec
- color-blue
status: active
created: '2026-04-18'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/HENRY — Research Paper Writing System.md
backlink_count: 28
backlinks:
- '[[wiki/AI Infrastructure Stack]]'
- '[[Areas/Writing/Academic Paper Pipeline]]'
- '[[Areas/Writing/AREA]]'
- '[[wiki/Chat Node Instructions — 16-Node Scholarly Paper Pipeline]]'
- '[[wiki/Custom GPT Products — PHAROS AI GPT Roster]]'
- '[[wiki/Henry GPT — Peer Reviewer ChatGPT Product Specification]]'
- '[[wiki/Literary References — Craft Guide]]'
- '[[Areas/Writing/Manuscript Pipeline MOC]]'
- '[[wiki/Martin Voice Spec — Stage Map]]'
- '[[wiki/Martin Voice Spec — Version Genealogy]]'
- '[[wiki/Obsidian Second Brain Product]]'
- '[[wiki/PAPER BUILDER — Source Bundle and HENRY Origin]]'
- '[[wiki/Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes AI Governance]]'
- '[[wiki/Per-Paper Project Structure — Folder and File Architecture]]'
- '[[wiki/Personal and Projects MOC]]'
- '[[wiki/Publisher Assessment — Literary Idioms and Phrase-Origin Book]]'
- '[[wiki/Publishing Strategy — Springer Trilogy and Parallel Tracks]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/Root Loose Notes Cluster Map — 2026-05-06]]'
- '[[Areas/Writing/Writing and Novels MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[wiki/genealogy/Martin Voice Spec — Version Genealogy]]'
- '[[memory/agents/Events]]'
- '[[memory/agents/Journal]]'
- '[[memory/agents/Learning]]'
- '[[projects/Papers — Fisher King Project State]]'
- '[[session-state]]'
- '[[wiki/voice11 — ElevenLabs TTS Pipeline]]'
---

# HENRY — Research Paper Writing System

## Summary

HENRY is both a multi-component writing system at `/home/cerebrhoe/HENRY/` and the identity of the **Henry agent** (`/home/cerebrhoe/hephaistos/HENRY.md`) — the author agent for [[Martin Lepage — Professional Profile|Martin's]] full writing stack. The agent operationalizes all writing and research workflows: academic papers, peer-review cycles, novels, governance writing, policy briefs, and any long-form output. The system includes a formal paper writing runbook ("Write Notes → I'll Turn Them Into a Peer-Reviewed Research Paper") and a voice code spec. Relevant to Martin's active [[Recursive Deterministic AI Governance — Method and Paper|AI governance paper pipeline]], [[Self-Polygraph Protocol and Suprametacognition|AI Society submission work]], and [[Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes AI Governance|Paper 25]].

## Context

HENRY sits at the intersection of [[Martin Lepage — Professional Profile|Martin's]] academic writing practice and voice/audio production (see [[voice11 — ElevenLabs TTS Pipeline]]). The paper writing workflow applies the same evidence discipline as the [[PHAROS Method — Technical Reference|PHAROS method]] — bounded claims, claim-evidence matrices, and staged review. The `debate-redteam.md` file in HENRY suggests red-team review integration (see [[PROTOCOLS — Debate and Red-Team Runbook]]).

## Details

### Installation path

`/home/cerebrhoe/HENRY/`

### Key files

| File | Purpose |
|---|---|
| `HENRY.txt` | Core paper writing runbook v3 |
| `HENRY APP.txt` | Application specification |
| `HENRY APP VOCAB.txt` | Vocabulary/terminology reference |
| `HENRY APP WF.txt` | Application workflow |
| `HENRY WF Sum.txt` | Workflow summary |
| `HENRY WK SocialStudies.txt` | Social studies workbook |
| `HENRY voice CODE.txt` | Voice synthesis code spec |
| `HENRY Voice Spec v3 OFFICIAL (2).pdf` | PDF mirror of the MOBI/Mobius v3 official voice specification |
| `05_AI_Governance_Constitution.pdf` | Unified Martin Voice Spec v4.0; current labeled voice constitution |
| `Martin Voice Spec — Version Genealogy.md` | Canonical index for the Martin voice-spec corpus |
| `Martin Voice Spec — Stage Map.md` | Compact stage map for Hermes-style reuse |
| `henry_voice_optimizer.py` | Voice optimization script |
| `bib_rebuild.py` | Bibliography rebuilder |
| `debate-redteam.md` | Red-team review integration |

### Paper writing workflow (v3 Runbook)

**Input types accepted:**
- Bullets/notes/voice memo transcripts
- Rough outlines, screenshots of tables/figures
- Messy paragraphs, links and PDFs
- Dataset summaries, journal requirements

**Outputs produced:**
- Paper skeleton with correct section logic
- Draft in journal style (IMRaD or narrative)
- Abstract mirroring the final paper (no overpromise)
- Title set (12 options + "Reviewer-2 safe" picks)
- Claim→Evidence matrix (the audit sheet)

**Format modes:**
- Empirical IMRaD (Intro–Methods–Results–Discussion)
- Humanities/social theory (Intro–Literature–Analysis–Conclusion)
- Mixed methods / policy (Problem–Framework–Methods–Findings–Implications)

**Preflight step (5-10 min):** Lock format and venue expectations before drafting. Prevents 80% of revision pain.

**Reviewer-#2 gates:** Mechanical checks for rejection triggers run during drafting, not after.

### Evidence discipline

HENRY's claim-evidence matrix mirrors [[Emotional Alliance vs. Evidentiary Discipline in AI|PHAROS evidence discipline]] — every claim must be traceable, bounded, and stated to match the actual design. No overpromising in abstracts.

## Key Ideas

- Note-to-paper pipeline: any input messiness is acceptable; structure is imposed by the system
- Claim→Evidence matrix is the governance artifact — the audit sheet reviewers wish authors had
- Reviewer-2 gates run mechanically during drafting, not as a final-stage check
- Bibliography rebuilder (`bib_rebuild.py`) handles citation hygiene

## Open Questions

- Is HENRY integrated with [[voice11 — ElevenLabs TTS Pipeline]] for audio narration of papers?
- Is HENRY's voice spec connected to the HeyGen avatar pipeline?
- Which active papers are being drafted through HENRY?

## Source Provenance

The `/home/cerebrhoe/HENRY/` directory is a **rebuilt output** of the upstream source bundle at `C:\Users\softinfo\Desktop\ubuntu disk\` (WSL: `/mnt/c/Users/softinfo/Desktop/ubuntu disk/`). The `rebuild_henry_bundle.py` script performs the rename: `PAPER BUILDER → HENRY`, `Martin's voice CODE → HENRY voice CODE`, `martin_voice_optimizer → henry_voice_optimizer`. See [[PAPER BUILDER — Source Bundle and HENRY Origin]] for the full genealogy, bundle contents, and architectural evolution (three-arm → relational coupling).

Raw source capture: `raw sources/paper-builder-origin-bundle/`

Original files:
- `/home/cerebrhoe/HENRY/HENRY.txt`
- `/home/cerebrhoe/HENRY/` (directory scan, rebuilt from source bundle)

## Related

- [[Manuscript Pipeline MOC]]
- [[Research and Papers MOC]]
- [[Writing and Novels MOC]]
- [[PAPER BUILDER — Source Bundle and HENRY Origin]] — upstream source bundle; genealogical link and relational coupling evolution
- [[Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes AI Governance]] — first paper to be routed through the Henry agent
- [[Recursive Deterministic AI Governance — Method and Paper]]
- [[Self-Polygraph Protocol and Suprametacognition]]
- [[Emotional Alliance vs. Evidentiary Discipline in AI]]
- [[voice11 — ElevenLabs TTS Pipeline]]
- [[PROTOCOLS — Debate and Red-Team Runbook]]
- [[AI Personas — Agatha, DOTTIE, and MOBI]] — prior writing persona stack Henry partially supersedes
- [[Henry GPT — Peer Reviewer ChatGPT Product Specification]] — standalone published ChatGPT product running the three-mode adversarial peer review; the externally deployed surface of the same Henry identity this system embodies
- [[Chat Node Instructions — 16-Node Scholarly Paper Pipeline]] — Complete node-by-node instruction set for HENRY-integrated 16-session scholarly article production; operationalizes session-isolation and evidence discipline across the full pipeline
- [[Per-Paper Project Structure — Folder and File Architecture]] — Canonical folder/file structure for each paper project managed by HENRY; enforces continuity across model sessions
