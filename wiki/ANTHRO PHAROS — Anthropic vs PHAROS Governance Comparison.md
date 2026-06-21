# ANTHRO PHAROS — Anthropic vs PHAROS Governance Comparison

## Summary

Structured comparative analysis contrasting Anthropic's governance framework (policy-and-training for a single model) with [[PHAROS Recalibration — Unified Governance Architecture|PHAROS]] (procedural-and-verification for any AI-assisted workflow). Establishes that the two systems operate at different levels of abstraction and address different failure modes. Part of [[Governance and PHAROS MOC]].

## Context

This document is an analytic memo that positions PHAROS relative to the dominant industry governance approach embodied by Anthropic's Responsible Scaling Policy (RSP), Constitutional AI, and API usage policy. Two versions exist in raw sources (`ANTHRO_PHAROS.docx` and `ANTHRO_PHAROS (1).docx`). The comparison is relevant to the [[PHAROS AI Ethics Submission — Springer Draft]], the [[Architectural AI Governance — Willis and PBSAI|Architectural AI Governance]] convergence analysis, and the [[PHAROS Licensing Prospectus]] competitive positioning. See [[AI Platform Dependence — Anthropic OpenClaw and Commoditization Pressure]] for the later platform-access and pricing-trust extension.

## Details

**Core distinction (repeated across all dimensions):**
- Anthropic governs **the model itself** before deployment (weights, API, training, capability assessments)
- PHAROS governs **the human–AI interaction loop** during and after deployment (workflow operators, third-party auditors)

**Key comparison dimensions:**

| Dimension | Anthropic | PHAROS |
|---|---|---|
| What is governed | A single LLM (Claude) | Any AI-assisted workflow (model-agnostic) |
| Governance artifact type | Policy + training + API terms | Executable procedure + audit protocol + control register |
| Locus of control | Centralized (Anthropic) | Distributed (implementable, auditable by third parties) |
| Risk model | Catastrophic risk (CBRN, cybersecurity, autonomy) from model capabilities | Epistemic risk (inferential collapse, performative coherence, ungoverned recursion) from workflow design |
| Trigger logic | ASL-2, ASL-3 triggered by capability benchmarks | Specific phase failure rules; escalation at Phase 5 |
| Conditionality | Conditional on future capabilities | Unconditionally applied to each pass — gates always active |

**Alignment mechanism comparison:**
- Anthropic: Constitutional AI (training-time value embedding), RLHF, RSP commitments
- PHAROS: Explicit phase-by-phase value checks embedded in the protocol; values are governance artifacts, not training parameters

**Key difference on binding:** Anthropic's RSP is conditional on future model capabilities. PHAROS is unconditionally applied to each pass — its gates are always active, regardless of the model's capability level.

## Key Ideas

- Level-of-abstraction gap: Anthropic operates at model level; PHAROS operates at workflow level — they are not competing governance systems but operating at different strata
- Epistemic risk vs. catastrophic risk: PHAROS's failure mode theory (performative coherence, inferential collapse, ungoverned recursion) is distinct from and complementary to Anthropic's capability-based risk model
- Distributed vs. centralized control: PHAROS's distributed, third-party-auditable structure is the direct alternative to centralized corporate governance
- Unconditional gates: the PHAROS always-active gate structure is a specific architectural claim against advisory governance

## Insights

- This document provides the competitive positioning argument for [[PHAROS Licensing Prospectus|PHAROS's commercial offering]]: PHAROS does not compete with Anthropic's safety work — it governs the deployment layer that Anthropic cannot reach
- The "advisory governance cannot constrain systems at runtime" claim — also in [[Architectural AI Governance — Willis and PBSAI]] — is the core justification for PHAROS's deterministic gate approach

## Open Questions

- Is this memo intended for publication, or is it an internal positioning document?
- Does it engage the most recent Anthropic Constitutional AI papers (Claude's Character, 2024)?

## Sources

- `ANTHRO_PHAROS.docx`
- `ANTHRO_PHAROS (1).docx`
- Related: [[PHAROS AI Ethics Submission — Springer Draft]]
- Related: [[Architectural AI Governance — Willis and PBSAI]]
- Related: [[PHAROS Licensing Prospectus]]
- Related: [[PHAROS Recalibration — Unified Governance Architecture]]
- Related: [[Governance and PHAROS MOC]]
- Related: [[AI Platform Dependence — Anthropic OpenClaw and Commoditization Pressure]]
