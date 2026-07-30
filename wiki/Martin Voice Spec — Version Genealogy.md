---
type: wiki
aliases:
  - Martin Voice Spec — Version Genealogy
  - Voice Spec Genealogy
  - Unified Martin Voice Spec
  - Martin Voice Spec Root Genealogy
  - Voice Spec Root Genealogy
tags: [voice-spec, version-genealogy, identity, henry, mobi, hephaistos, operator-continuity]
status: active
created: 2026-05-02
updated: 2026-07-30
---

# Martin Voice Spec — Version Genealogy

## Summary
Canonical index for the Martin voice-spec corpus and operator-voice lineage. Tracks the evolution of the voice specification used by AI agents to produce output in Martin's register — clinical rigour, evidence-bounded claims, anti-charm posture, bilingual EN/FR sensitivity. Use this index instead of chasing the raw versions one by one. Reference for [[Version Genealogy System]], [[Martin Lepage Professional Identity]], and [[HEPHAISTOS Agent Architecture]] (the voice spec is the public-output discipline that pairs with the agent-internal governance discipline).

## Context
The voice-spec corpus is a sequence of documents that progressively refined how AI agents (HENRY, MOBI, GPT custom personas, current operator-side specialists) produce text in Martin's voice. The corpus is *operational documentation*, not theory — the spec is what gets loaded into a custom GPT or skill to constrain output register. Closely paired with [[Martin Voice Spec — Stage Map]] (compact stage map for Hermes-style reuse), [[genealogy/Martin Voice Spec — Stage Map]] and [[genealogy/Martin Voice Spec — Version Genealogy]] (path-local genealogy copies), and [[Second Self System — Identity Kernel and Agent Routing Architecture]] (operator-level architecture into which the voice spec slots).

## Version Lineage

| Version | Source artifact | Status | Notes |
|---|---|---|---|
| v3 OFFICIAL (Martin-named source) | `Martin Voice Spec v3 OFFICIAL (2).pdf` — at `C:\Users\softinfo\Desktop\ubuntu disk\` | Source | **Newly traced (2026-05-03):** this is the original Martin-named PDF; the HENRY-named version below is its rebuild output |
| v3 OFFICIAL (HENRY rebuild output) | `HENRY Voice Spec v3 OFFICIAL (2).pdf` — at `/home/cerebrhoe/HENRY/` | Superseded (output) | Renamed copy produced by `rebuild_henry_bundle.py`; previously attributed to MOBI/Mobius without source trace |
| v3 Voice CODE (Martin-named source) | `Martin's voice CODE.txt` — at `C:\Users\softinfo\Desktop\ubuntu disk\` | Source | Machine-readable JSON spec: 11 operators, paragraph contract, lexicon EN/FR; renamed to `HENRY voice CODE.txt` by rebuild script |
| v4.0 (Unified) | `05_AI_Governance_Constitution.pdf` | **Current labeled voice constitution** | **Mislabeled** in source files as "AI Governance Constitution" — confirmed in [[Complete Paper List — Martin Lepage Corpus]] as actually being the Unified Martin Voice Spec v4.0 |
| Mobius extensions | `Mobius-GPTExt-Think-Desktop-Super.txt` | Lateral artifact | Mobius-thread variant for desktop deep-think contexts |
| Operator voice (current) | [[Second Self System — Identity Kernel and Agent Routing Architecture]] | Active | Architecture supersedes single-document spec; voice spec now distributed across kernel + specialist agents |
| **Audio reference (canonical)** | `mlen.mp3` — at `/home/cerebrhoe/voice11/mlen.mp3` | **Active** | **Operator-confirmed 2026-05-03.** Quebec English voice sample; phonetic anchor for all TTS cloning. English (not French). Full parameters and modulation guide: [[voice11 — ElevenLabs TTS Pipeline]]. |

## 2026-07-30 Metadata Resolution

The 2026-07-30 metadata audit resolves the latest-code question without flattening artifact classes: `HENRY voice CODE.txt` is the latest recovered machine-readable voice-code artifact, while v4.0 remains the latest labeled voice constitution and [[Second Self System — Identity Kernel and Agent Routing Architecture]] remains the current distributed operator architecture. See [[genealogy/Voice Operator Lineage - Metadata Resolution 2026-07-30]].

## Mislabeling Note (research-integrity flag)

The PDF `05_AI_Governance_Constitution.pdf` is **not** an AI governance constitution — it is the Unified Martin Voice Spec v4.0. This mislabeling propagates into anything that cites the file by name. Citation must reference the corrected identity, not the PDF filename.

## Open Questions

- Which voice-spec elements have been internalized into specialists ([[HENRY — Research Paper Writing System|HENRY]], [[Trismégiste — Personal AI Assistant|Trismégiste]], operator-side personas) vs. which remain in the v4.0 document only?
- Does the [[Second Self System — Identity Kernel and Agent Routing Architecture|Second Self architecture]] supersede the unified voice spec or extend it?
- Is there a v5 candidate that consolidates v4 with the [[PHAROS — Origin and Doctrine|origin-doctrine register]]?

## Related

- [[voice11 — ElevenLabs TTS Pipeline]] — Audio anchor: mlen.mp3 canonical voice sample + Quebec English modulation guide
- [[PAPER BUILDER — Source Bundle and HENRY Origin]] — Upstream source bundle from which HENRY was built; traces v3 origin
- [[genealogy/Voice Operator Lineage - Metadata Resolution 2026-07-30]] — Metadata audit resolving HENRY voice code, DOTTIE / Voice Operator 2, and MOBI/Mobius chronology
- [[Martin Voice Spec — Stage Map]] — Compact stage map (Hermes-style reuse format)
- [[Version Genealogy System]] — Hub for all version-genealogy notes
- [[Martin Lepage Professional Identity]] — Authorial identity the spec produces
- [[HEPHAISTOS Agent Architecture]] — Architecture in which the voice spec runs
- [[HENRY — Research Paper Writing System]] — Specialist consuming the voice spec
- [[PHAROS Final Voice Operator — GPT Creator]] — GPT operator built around earlier voice-spec versions
- [[Second Self System — Identity Kernel and Agent Routing Architecture]] — Current architecture
- [[AI Personas — Agatha, DOTTIE, and MOBI]] — Persona genealogy adjacent to voice-spec lineage
- [[Complete Paper List — Martin Lepage Corpus]] — Source of the v4.0 mislabeling flag
- [[APEX Papers — Research Archive Map]] — Archive map referencing this index
