---
type: opportunity
title: micro1 — Data Licensing Opportunity (PHAROS)
tags:
- data-licensing
- micro1
- revenue-pipeline
- governance-evaluation-data
- blackboard
- legipro
- mock-dataset
- pharos-commercial
status: active
domain: pharos
priority: high
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/micro1 — Data Licensing Opportunity (PHAROS).md
---

> For future Claude: this note documents a cold-outreach data-licensing deal with micro1 (a Scale AI competitor) that was fully worked up in `~/infra/micro1/` in June 2026 but never entered the vault — despite being framed internally as a $500-800K/yr illustrative pipeline. Treat all figures and status here as **as-of the source document's date**, not current; before acting on this, check `~/infra/micro1/` directly for anything newer than 2026-06-17, since the qualification call with Camilo happened 2026-06-15 and no vault record captures what happened after.

## Summary

micro1 is a real, venture-backed human-data-pipeline company for frontier AI labs — Series A at a $500M valuation led by 01 Advisors (September 2025), per `pharos_micro1_assessment.md`. Daniel Warner from micro1 sent cold outreach (email dated 2026-06-08, `micro1-D. Warner.pdf`) proposing to buy structured operational and evaluation data, in the "$50K-$2M" range that the internal assessment explicitly flags as a funnel number designed to elicit a response rather than a real offer.

PHAROS's response, worked out across internal Blackboard memos (4164-4170, June 8-9 2026) and formalized in an executive summary dated 2026-06-17, positions PHAROS as a licensor of **governed data production capacity**, not a static archive — directly extending the commercial posture already laid out in [[Areas/PHAROS/PHAROS Commercial Strategy|PHAROS Commercial Strategy]]. The illustrative 12-month deal value, per the 2026-06-17 executive summary, is **$500K-$800K**, built from a three-phase structure (pilot -> volume -> recurring partnership).

## Context

- **Actors** (per `camilo-meeting-brief-2026-06-15.md` and the executive summary): Daniel Warner initiated cold outreach; Camilo is the live micro1 counterpart who ran the qualification call on 2026-06-15, believed to sit on the workflow-data sourcing/partnerships side rather than deep technical evaluation. Martin Lepage (ml@pharos-ai.ca) is the sole PHAROS-side actor.
- **What micro1 is**: per `pharos_micro1_assessment.md`, a direct Scale AI competitor, $41.6M raised total, real Palo Alto operation; the assessment separately notes their hiring/interview-data arm has a distinct, worse reputation from the data-licensing arm this opportunity concerns.
- **Two product lines identified** (per README.md, 2026-06-17 state, and the executive summary):
  1. **Governance evaluation data** — Blackboard/COMPASS/HELIX pipelines: task -> checkpoint -> escalation/veto/override -> documented rationale -> bounded claim/proof packet. This is the same operational engine described in [[Areas/PHAROS/COMPASSai — Governance Engine|COMPASSai — Governance Engine]] and specified structurally in [[Areas/PHAROS/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard spec]] (note: that spec sheet postdates this opportunity's working docs by 10 days, so cross-check for drift).
  2. **Professional domain evaluation data** — LegiPro pipelines (conveyor extraction/validation, autocomplete intent transformation), covering French/Canadian accounting and tax corpora.
- **The 4391 pack**: `4391-InfraFabric_Blackboard_Micro1_Explainer_2026-06.docx`/`.md`, dated June 2026, is described in the README as "the authoritative detailed description of the governance workflow data line" — a 49-entry curated Blackboard Training Data Asset Catalogue spanning 10 domains, drawn from a full ledger of 3,800+ task IDs accumulated over ~10 months, with ~78 GB of cross-referenced recoverable session logs. Entries document traps, checkpoints, acceptance criteria, and SHA-256-hashed closeouts as evidence that the data is real production trace, not synthetic.

## Details

**Numbers as stated, dated to source** (do not present as current without re-verifying against `~/infra/micro1/` and any 2026-06-15-forward call notes):

- Preliminary internal audit (per README.md, as of 2026-06-17): ~15k potentially recoverable events in audited internal Blackboard/signals slices; `signals_internal_governance` is the cleanest starting bucket, with partial cryptographic provenance already present.
- LegiPro side (per executive summary, 2026-06-17): 7,350+ accepted conveyor extraction/validation traces, 8,888+ extraction artifacts, 9,344+ tests, 62k+ raw autocomplete rows.
- **Deal structure** (per executive summary, 2026-06-17):
  1. Qualification (call held 2026-06-15 with Camilo).
  2. NDA + controlled sample within ~10 days of signed NDA: 25-50 redacted records + data dictionary.
  3. Phase 1 pilot (30 days): 200-300 records, fixed fee **$25K-$40K**.
  4. Phase 2 volume (90 days): 1,000-2,000+ records/month, **$100K-$200K** for the phase.
  5. Phase 3 ongoing partnership: **$50K-$150K/month**, non-exclusive, renewable.
  6. Illustrative 12-month total: **$500K-$800K**. The executive summary explicitly disclaims the $2M ceiling from Warner's original outreach range as requiring scale/terms not yet scoped.
- An earlier internal assessment pass (`pharos_micro1_assessment.md`, June 8-9 2026, predating the executive summary) had floated a more conservative $150K-$300K base case and treated $500K-$800K/$2M as later-phase targets — the 2026-06-17 executive summary is the more current and more aggressive framing. This inconsistency between internal working drafts is real and should be flagged if this deal resumes.

**Governance discipline applied to the deal itself** (per `camilo-meeting-brief-2026-06-15.md`): the brief is explicit that several external-facing docs quote exact counts even though internal posture says not to finalize numbers pre-audit; the call was scoped to NOT quote final volume, negotiate price, discuss exclusivity, or explain the Pharos method — only to learn micro1's priority category, field of use, and downstream rights posture, and to leave with NDA + sample as the next concrete step.

**Supporting role of the mock-governance-dataset** (per `~/workspaces/mock-governance-dataset/README.md` and `schema.md`, generated 2026-06-21, four days after the executive summary): this is a deterministic, re-runnable synthetic dataset (360 signal records, 12 structured use cases, evidence packages, a 40-record gold set) built as a black-box stand-in for the real governance pipeline's shape — used for internal testing of intake -> evidence -> risk assessment -> gate -> override -> audit flows without exposing real client or production Blackboard data. Its explicit purpose statement ties it to demonstrating the "structured, internally coherent" claim made to micro1 without the disclosure risk of real traces; it is a **credibility and QA prop**, not itself a licensable asset.

**Risks documented internally** (per `pharos_micro1_assessment.md` and the meeting brief): IP bleed through structural reconstruction of the Pharos governance method from enough traces; the $50K cold-outreach anchor; an exclusivity trap; client-data contamination (named specifically as a "do not include" boundary); and premature disclosure of method mechanics on sales calls. The assessment's stated rule: describe outputs, never the engine.

**Next actions as of the 2026-06-17 state** (per README.md, unconfirmed whether executed):
1. Review the 2026-06-15 Camilo call outcome and the categories he names as priority.
2. Send thank-you + next-step confirmation within 30 minutes of the call.
3. If fit confirmed: execute NDA, prepare a 25-50 record controlled redacted sample from the cleanest buckets.
4. Manual redaction/normalization pass on `clean_with_redaction` rows, post-NDA.
5. Deliver sample + data dictionary + proposal, advance to Phase 1 scoping workshop.
6. Maintain discipline: no unaudited volume quotes; protect methodology/IP; qualify field-of-use and downstream rights before pricing.

**Vault gap this note fixes**: as of 2026-07-08, no other PHAROS-area note referenced micro1, Daniel Warner, Camilo, or this pipeline, despite three weeks of dedicated working documents in `~/infra/micro1/` and a supporting synthetic dataset in `~/workspaces/mock-governance-dataset/`. This is the first vault record of the opportunity.

## Related

- [[Areas/PHAROS/PHAROS Commercial Strategy|PHAROS Commercial Strategy]] — parent commercial framing this opportunity extends.
- [[Areas/PHAROS/COMPASSai — Governance Engine|COMPASSai — Governance Engine]] — the engine generating the governance-evaluation-data product line.
- [[Areas/PHAROS/if.blackboard — Coordination Evidence Spec Sheet (2026-06-27)|if.blackboard spec]] — structural spec for the append-only ledger underlying the 4391 catalogue and the governance data line.
- Source files (outside vault, read-only): `~/infra/micro1/README.md`, `~/infra/micro1/pharos_micro1_assessment.md`, `~/infra/micro1/pharos-micro1-executive-summary-2026-06-17.md`, `~/infra/micro1/camilo-meeting-brief-2026-06-15.md`, `~/infra/micro1/4391-internal-micro1prep/`, `~/workspaces/mock-governance-dataset/README.md`, `~/workspaces/mock-governance-dataset/schema.md`.
