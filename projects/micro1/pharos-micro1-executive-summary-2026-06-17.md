# Pharos AI × micro1
## Executive Summary — Governance & Professional Domain Evaluation Data Partnership

**Date**: 2026-06-17  
**Prepared for**: micro1 (Camilo / qualification follow-up)  
**From**: Martin Lepage, Founder, Pharos AI  
**Status**: External-facing summary for discussion. Ready for NDA + controlled sample upon category alignment.

---

### The Opportunity

micro1 builds human data pipelines for frontier AI labs, with emphasis on evaluation, red-teaming, and structured reasoning traces that capture how models operate under real constraints.

Pharos AI operates deterministic, expert-governed data production pipelines that generate precisely this category of data:

- Structured records of how decisions are authorized, escalated, overridden, corrected, and bounded.
- Explicit human rationale and claim-boundary enforcement at every step.
- Two complementary production lines that can be licensed separately or together.

We are not offering a static archive or commodity annotation. We are offering repeatable production capacity under contract — the same operational discipline that has allowed specialized providers to secure meaningful recurring relationships with frontier labs.

### Two Product Lines

**1. Governance Evaluation Data (Blackboard / COMPASS / HELIX pipelines)**

Core pattern: Task → checkpoint → escalation / veto / override → documented expert rationale → bounded claim / proof packet / resolution.

- Append-only operational workflow events (tasks, sessions, signals) from real governance and evidence workflows.
- Adversarial evaluation traces with probe types, model responses, failure classifications, and human corrections.
- Partial cryptographic provenance already present on a substantial portion of events.
- Audited candidate pool in internal governance slices: substantial volume (strongest clean bucket: internal signals governance events, >11k in the primary audited family pre-redaction/normalization).

Value: Frontier labs need records of *why* and *under what institutional rule* a human overruled or bounded an AI output — not just input/output pairs. This is evaluation and alignment data at the governance layer.

**2. Professional Domain Evaluation Data (LegiPro pipelines)**

Core pattern: Messy professional query or source material → normalized intent → source-family routing + bias rules → extraction/validation with claim-boundary enforcement → accepted / quarantined outcome.

- Conveyor extraction/validation traces (7,350+ accepted candidates) with full lifecycle events, manifests, patches, gates, and quarantine/acceptance decisions.
- 8,888+ extraction artifacts and 9,344+ tests encoding domain-specific overclaim prevention and source-path validation (e.g., `test_no_forbidden_overclaim_language`).
- Autocomplete intent transformation data (62k+ raw rows): the high-value layer is the mapping from raw professional search strings into safe intent, routing, expected results, and bad-source rejection rules.

Value: Trains and evaluates professional AI systems (accounting, tax, legal) on safe retrieval, citation discipline, and bounded claim generation — where errors carry real compliance and liability cost.

### What Makes Pharos Different

- **Deterministic & versioned production**: Identical generation → test → correction → annotation → claim-boundary protocol every time. Quality is engineered, not sampled.
- **Expert reasoning layer**: Corrections and rationales produced at PhD-level socio-anthropological + technical governance depth. This is the premium tier buyers pay for in RLHF and evaluation programs.
- **Claim-boundary enforcement built in**: Every record documents not only the correction but the specific institutional or professional rule that required it.
- **Provenance & auditability**: Timestamps, reviewer roles, workflow versions, and existing signed receipts on production data.
- **Structured & export-ready**: JSON records with explicit field maps, designed for direct use in training/evaluation pipelines.
- **Domain specificity that is rare**: Deep expertise at the intersection of institutional governance and professional services (French/Canadian accounting & tax corpora). Most suppliers cover generic or coding domains.

We license the *traces, labels, routing decisions, and expert judgments* produced by these workflows. We do not license raw source corpora, client work product, or the underlying governance methodology itself.

### Proposed Path (Non-Exclusive, Renewable)

1. **Qualification** (current) — Align on priority categories, schema needs, field-of-use, downstream users, and pilot success criteria.
2. **NDA + Controlled Sample** (within ~10 days of signed NDA) — 25–50 redacted, formatted records from the cleanest audited buckets + full data dictionary and field documentation. Allows direct quality and structure evaluation.
3. **Phase 1 Pilot — Proof of Operation (30 days)**: 200–300 records in the agreed schema/format (governance, professional-domain, or mix). Fixed fee $25K–$40K. Includes QA summary and versioned notes. Paid pilot validates pipeline before larger commitment.
4. **Phase 2 — Volume (90 days)**: 1,000–2,000+ records/month, tiered by complexity (standard traces / expert-annotated rationale / custom scenario + protocol design). Fee range $100K–$200K for the phase.
5. **Phase 3 — Ongoing Partnership**: Dedicated monthly stream + custom evaluation work. Non-exclusive, renewable. Target ~$50K–$150K/month depending on volume and tiers.

Illustrative 12-month value on this structure: $500K–$800K. This is a realistic, executable number for a specialized deterministic operation. We are not positioning for the $2M ceiling (that requires scale and terms we would scope deliberately over time).

### Readiness & Supporting Materials

Pharos has completed:
- Internal licensability audit on candidate Blackboard/signals buckets (preliminary: ~15k potentially recoverable events in audited internal slices; signals_internal_governance the cleanest starting family).
- Full data dictionary defining canonical fields, redaction rules, and provenance requirements across pipelines.
- Representative sample records demonstrating both product lines (schema + examples available for review under NDA).
- Domain map covering institutional/regulatory governance, healthcare/clinical, financial compliance, legal/accounting, and cross-cutting regulatory policy.
- Pilot proposal language, call posture, and response templates calibrated to a disciplined qualification process.
- Detailed 49-entry Blackboard Training Data Asset Catalogue (4391 pack, June 2026): curated real multi-agent tasks across 10 domains (infra/coordination, rook/identity-security, context/memory, gov, philosophy-as-runtime, red-team/spin, whitepapers-bible, optimise/routing, drone/robotics, content-narrative) with acceptance criteria, results, explicit traps, and "why this matters for training data" notes for each. Cross-referenced to ~78 GB recoverable full session/rollout logs. The 4391-InfraFabric_Blackboard_Micro1_Explainer_2026-06.docx/.md (now in docs/) is the authoritative detailed description of the governance workflow data line.

All materials are designed to be consistent, auditable, and protective of core IP while demonstrating real production capability. The 4391 catalogue provides the concrete high-signal examples and taxonomy that substantiate the asset.

### Recommended Discussion Points for Tomorrow

- Which 1–2 categories (governance decision/override traces, adversarial evaluation, professional-domain extraction/validation, or other) are highest priority for micro1 clients right now?
- Preferred output schemas, provenance elements, and delivery formats?
- Field-of-use expectations (evaluation/red-team only vs. supervised fine-tuning vs. broader foundation model training)?
- Downstream users and any sublicensing or onward-transfer requirements?
- Retention/deletion posture given the irreversibility of model training?
- What would success look like for a 30-day Phase 1 pilot (volume, quality gates, integration criteria)?

We are prepared to move immediately to NDA and a tailored controlled sample once category fit is confirmed.

---

**Contact**  
Martin Lepage  
Founder, Pharos AI  
ml@pharos-ai.ca

*Pharos AI (InfraFabric and LegiPro are product/trading surfaces of the same entity). This summary reflects the current state of our governed data production operations and is provided for qualification purposes. Full details, samples, and commercial terms are subject to NDA and scoping.*