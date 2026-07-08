---
type: wiki
title: Martin Voice Spec — Stage Map
aliases:
- Voice Spec Stage Map
tags:
- voice-spec
- stage-map
- identity
- hermes
- operator-continuity
- wiki
- stage
- spec
- genealogy
- voice
- charm
status: active
created: '2026-05-02'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Martin Voice Spec — Stage Map.md
backlink_count: 12
backlinks:
- '[[Areas/PHAROS/Second Self System — Identity Kernel and Agent Routing Architecture]]'
- '[[Areas/PHAROS/voice11 — ElevenLabs TTS Pipeline]]'
- '[[Areas/Writing/Martin Voice Spec — Version Genealogy]]'
- '[[Areas/Writing/PAPER BUILDER — Source Bundle and HENRY Origin]]'
- '[[wiki/Home]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/wiki-2026-07-08/Second Self System Identity Kernel and Agent Routing Architecture]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
- '[[wiki/genealogy/Martin Voice Spec — Version Genealogy]]'
---

# Martin Voice Spec — Stage Map

## Summary
Compact stage map of the Martin voice spec for Hermes-style reuse. Where [[Martin Voice Spec — Version Genealogy]] tracks the document lineage, this stage map tracks the **functional stages** the voice spec passes through when producing output — usable as a runtime checklist by any specialist (HENRY, operator-side personas, custom GPTs) producing text in Martin's register. Reference for [[HEPHAISTOS Agent Architecture]] (Hermes-routing format), [[Version Genealogy System]], and [[Martin Lepage Professional Identity]].

## Context
The Stage Map is the operational counterpart to the Version Genealogy: the Genealogy says *which spec is current*, the Stage Map says *what the spec does at runtime*. Designed for Hermes-style routing — each stage is a checkpoint that produces a recordable artifact.

## Stage Map (compact)

| Stage | Function | Input | Output | Anti-pattern caught |
|---|---|---|---|---|
| **1. Register fix** | Set the bilingual EN/FR baseline; clinical-rigour register | Raw task | Register-locked draft | Casual register; corporate-pitch tone |
| **2. Claim boundary** | Bound every claim to its evidence class | Draft | Claim-classified draft | Overclaiming; unhedged universal claims |
| **3. Anti-charm pass** | Strip charm, decorative confidence, rhetorical flourish | Claim-classified | Charm-stripped text | Persuasive-but-evidence-thin language |
| **4. Disclosure layer** | Add function-specific AI-mediation disclosure where relevant | Charm-stripped | Disclosed text | Generic "AI-assisted" disclaimer that collapses expressive and epistemic mediation |
| **5. Refusal check** | Verify nothing crosses Queen Keyport refusal conditions | Disclosed | Verified text | Silent breach of refusal conditions under output pressure |
| **6. Consented Frame gate** | Wisdom-and-care validation before promotion | Verified | Promotion-ready text | Formal correctness without wisdom |

## Use as Hermes routing checklist

Each stage produces a checkpoint artifact that Hermes can route to the next stage. The Stage Map allows a specialist to:
1. Declare which stage their output has reached
2. Hand off explicitly to the next stage
3. Surface stage-specific failures without collapsing the whole pipeline

This makes the voice spec compatible with the [[HEPHAISTOS Agent Architecture|three-agent stack]] — voice production becomes a routable activity, not a monolithic black box inside one persona.

## Distinction from the Version Genealogy

- **Genealogy:** which voice-spec document is current (v3 → v4.0 → ...)
- **Stage Map:** what the current voice spec does at runtime, decomposed into discrete checkpoints
- **Use one to find the other:** Genealogy tells you which spec to load; Stage Map tells you how to apply it

## Related

- [[Martin Voice Spec — Version Genealogy]] — Document-lineage companion
- [[HEPHAISTOS Agent Architecture]] — Routing context for stage-map use
- [[Version Genealogy System]] — Hub for genealogy systems
- [[Martin Lepage Professional Identity]] — Identity the spec produces
- [[Diamond-Eyes — Aesthetic Refinement Skill]] — Stage 6 implementation
- [[HENRY — Research Paper Writing System]] — Specialist consuming the stage map
- [[Second Self System — Identity Kernel and Agent Routing Architecture]] — Operator-level architecture into which the stage map slots
- [[PHAROS Final Voice Operator — GPT Creator]] — Earlier GPT operator embodying the stage discipline
