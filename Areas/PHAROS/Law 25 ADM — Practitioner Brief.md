---
type: note
title: Law 25 ADM — Practitioner Brief
tags:
- law-25
- automated-decision-making
- quebec-privacy-law
- regulatory-compliance
- financial-services
- pharos-marketing-asset
status: active
domain: pharos
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Law 25 ADM — Practitioner Brief.md
---

# Law 25 ADM — Practitioner Brief

> For future Claude: this is a finished PHAROS marketing/thought-leadership asset, not a working note. Treat it as a citable artifact — read it before assuming Martin needs the Law 25 ADM argument re-derived from scratch.

## Summary

A short, finished practitioner brief titled *"What Quebec's Law 25 Actually Requires from Organizations Running Automated Decisions,"* authored by Martin Lepage / PHAROS AI, aimed at compliance, legal, and risk functions in financial services. Its core claim: Quebec's Law 25 (the *Act respecting the protection of personal information in the private sector*) already imposes a harder automated-decision transparency obligation than the EU AI Act will before December 2027, and most financial-services firms running automated credit/claims decisions are non-compliant right now, not on some future deadline.

## Context

Source: `/home/martin/.UPLOADS/Law25-ADM-practitioner-brief.md` (5,981 bytes, 46 lines, last modified 2026-06-08). The brief states its own currency: "reflects the state of the law as of June 2026," with an explicit non-legal-advice disclaimer and a pointer to `[martin.govern-ai.ca]` for the "full obligation-to-control mapping." This is downstream marketing/positioning content built on the same regulatory-window thesis tracked elsewhere in the vault — see [[EU AI Act and Law 25 — Regulatory Pressure Window]] for the underlying analytical case and [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]] for the timing-arbitrage synthesis this brief is likely drawing on.

## Details

The brief's argument runs in five parts:

1. **The obligation, stated plainly** — when a decision is based *exclusively* on automated processing and significantly affects the individual, four things become mandatory: notice at time of decision, on-request disclosure of the data/reasons/principal factors used plus the correction right, a route to have a human with real authority review the decision, and (for high-risk processing) a privacy impact assessment before deployment. Penalty ceiling: C$25 million or 4% of worldwide turnover, whichever is higher.

2. **The four operative articles**, each named and dated:
   - **Section 12.1** — automated decision transparency (in force since September 2023).
   - **Section 22.1** — the right to human review, framed as the provision "most credit-scoring and claims-adjudication pipelines are architecturally unprepared for."
   - **Section 3.3** — mandatory PIA before deploying high-risk automated decision-making/profiling.
   - **Section 14** — explicit, informed, purpose-specific consent (a general ToS checkbox does not satisfy it).

3. **The failure pattern in financial services** — three predictable gaps: (a) a "human in the loop" that is decorative because it routinely defers to the model, which does not exempt the firm from s. 12.1 in fact even if it looks exempt on paper; (b) an explanation capability that describes the system in general (a model card) rather than the *per-decision* principal factors s. 12.1 actually requires — many firms discover their vendor cannot surface this at all; (c) an s. 22.1 review route that doesn't functionally exist because there is no person empowered to re-examine, only a complaints line.

4. **The diagnostic question** the brief poses to any Quebec-facing firm making automated credit/claims/underwriting/eligibility decisions: can it produce, today, a PIA, a per-decision factor disclosure, and a working human-review route for one named automated decision? The brief's position: most cannot.

5. **The framing move** in the closing line: "Closing it is governance work, not legal work — the law states the obligation; the difficulty is building the disclosure, review, and assessment machinery that actually satisfies it inside a real ML pipeline." This is the pivot from regulatory description to PHAROS's service offer (governance-control-mapping work, ISO/IEC 42001-aligned, per the closing attribution line).

Provenance note: this file lives in `.UPLOADS/`, a staging area for finished external-facing drafts, not in a working-drafts or scratch directory — consistent with it being a completed, ready-to-publish asset rather than a note-in-progress.

## Related

- [[EU AI Act and Law 25 — Regulatory Pressure Window]]
- [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]
- [[Governance and PHAROS MOC]]
