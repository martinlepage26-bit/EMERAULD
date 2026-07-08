# Pharos AI × micro1 — Main Strategic Explainer

**Date**: 2026-06-09  
**Company**: Pharos AI (InfraFabric and LegiPro are trading names)  
**Purpose**: Internal and external reference for the data licensing opportunity with micro1. Use for qualification call preparation, sample scoping, and proposal development.

## What micro1 Is

micro1 is a real company that raised $41.6M (Series A at $500M valuation led by 01 Advisors in September 2025). It is a direct competitor to Scale AI. Its core business is building human data pipelines for frontier AI labs: recruiting domain experts, running evaluation environments, and supplying training and evaluation data.

The outreach is a standard qualification process for companies that may have licensable operational data. The advertised range ($50K–$2M) is a funnel; most deals land much lower unless the data is genuinely rare, structured, high-volume, and high-value.

## The Opportunity and Realistic Value

micro1 (like other data buyers) is looking for **structured decision traces where an expert reasoned under constraint** — not generic labeled data or simple annotation. High-value categories include:

- Adversarial mitigation logs
- Human-override records with rationale
- Recursive audit chains
- Governance, escalation, and claim-boundary workflows

**Pharos positioning**: We are not a data annotation shop. We operate governed data production pipelines that generate exactly these kinds of traces. The value comes from the combination of operational volume (from our production systems) and specialized governance methodology with PhD-level expert reasoning and explicit claim-boundary enforcement.

**Realistic ceiling**: $150K–$500K for a well-scoped package in the near term (pilot + first volume phase). $2M would require massive scale or a multi-year exclusive partnership, which is a 2027–2028 target.

Precedents that matter include non-exclusive recurring deals (e.g., Reddit-style) and red-teaming methodology sales (e.g., TELUS Digital model), where the ability to produce consistent, high-quality traces under contract is valued more than a one-time data dump.

## Our Data Assets

We have two complementary product lines that can be sold separately or together.

### 1. Governance Evaluation Data
Drawn from operational governance workflows and production systems (task, checkpoint, escalation, veto/override, resolution, and signals).

- **Sources**: Blackboard / COMPASS operational logs + HELIX adversarial evaluation traces.
- **Current audited candidate pool** (preliminary, if.trace excluded): ~15,379 potentially recoverable events. The strongest clean slice is signals (≈11,897 events).
- **Characteristics**: Structured, timestamped, versioned, with human rationale, outcome, risk tier, and claim-boundary documentation. Partial cryptographic provenance already present on many records.
- **Why valuable**: Captures how institutional constraints are applied in practice — exactly the “expert reasoned under constraint” pattern buyers need for evaluation and alignment work.

### 2. Professional Domain Evaluation Data (LegiPro)
Focused on accounting, tax, and legal domains.

- **Key assets**:
  - Conveyor extraction and validation traces (7,350+ accepted candidates) with full lifecycle events, validation gates, and quarantine/acceptance decisions.
  - Extraction JSON + tests (8,888 artifacts + 9,344 tests) showing domain-specific claim-boundary enforcement and overclaim prevention.
  - Autocomplete intent transformation packs (62k+ raw rows): the high-value layer is the transformation from messy professional queries into normalized intent, source-family routing, bias rules, expected results, and bad-source rejection.
- **Why valuable**: Teaches retrieval, intent understanding, source selection, and safe claim generation in high-stakes professional fields.

**Overall strength**: Deterministic, reproducible pipelines + expert (PhD-level) reasoning layer. This is rarer than volume alone in the current data supply market.

## Positioning (What to Sell)

Sell the **capacity to produce high-quality structured traces reliably at scale**, not a static archive.

Core message: “We operate governed data production pipelines that generate adversarial governance traces and professional-domain evaluation data. Our methodology is deterministic and versioned. We combine operational workflow data from our production systems with specialized expert reasoning and claim-boundary enforcement. We can produce to spec in the governance and professional domains you prioritize.”

**What not to sell or disclose**:
- The core recursive governance methodology or internal IP architecture.
- Raw client or source corpus text.
- Unaudited volume claims.
- Any suggestion of joint entities or side deals.

**Martin (governance methodology + expert reasoning) vs. operational data assets**: The data draws from large-scale operational governance traces generated through our production systems. The premium, differentiated value comes from the specialized governance evaluation methodology and PhD-level expert reasoning that structures, annotates, and enforces boundaries on those traces. This layered approach is what makes the output particularly suitable for AI labs training models that must respect institutional and regulatory constraints.

## Proposed Deal Structure

Start with a paid pilot (proof of operation), not a speculative data dump. Recommended structure:

- **Phase 1 — Proof of Operation (30 days)**: 200–300 fully annotated records in agreed schema/format. Fixed fee $25K–$40K. Includes documentation and QA summary. Purpose: validate quality, cadence, and fit.

- **Phase 2 — Volume Production (90 days)**: 1,000–2,000+ records/month, tiered by complexity (standard traces, expert-annotated reasoning traces, custom scenario design). Fee range $100K–$200K.

- **Phase 3 — Ongoing Partnership (recurring)**: Dedicated monthly stream + custom evaluation protocol work. Non-exclusive, renewable. Target $50K–$150K/month (balanced stream ≈$60K/month after Phase 2).

Illustrative 12-month value: $500K–$800K. This is defensible and executable for a specialized operation. Expandable with volume.

## Key Risks and Controls

1. **IP / methodology reconstruction** — License only outputs, labels, routing decisions, and traces. Never the core recursive logic or agent architecture. Use field minimization and schema abstraction on any sample.
2. **$50K anchor** — Never quote the high end of their range. Lead with pilot structure and qualification.
3. **Exclusivity trap** — Explicitly non-exclusive in all language.
4. **Client data contamination** — Full audit and redaction rules before any delivery (especially Blackboard pillars).
5. **Premature disclosure** — On the call, describe outputs and pipelines only. Save methodology depth for post-NDA work.

All controls are built into the prepared materials (one-pager, call posture, sample redaction rules, proposal).

## Prepared Materials (Ready for Use)

- **One-Pager** (`pharos-micro1-one-pager.md` / .docx) — Concise external summary of the two product lines and pilot structure.
- **Domain Map** (`pharos-micro1-domain-map.md` / .docx) — Matrix of domains, data types, value, and differentiation.
- **Call Posture Script** (`pharos-micro1-call-posture-script.md`) — Full qualification call language, questions to ask micro1, volume deflection, what never to say, and post-call protocol.
- **Data Dictionary** (`pharos-micro1-data-dictionary.md`) — Field-level schema, redaction rules, and provenance requirements for all pipelines.
- **Pilot Proposal** (`pharos-micro1-pilot-proposal.md` / .docx) — Draft proposal language with phases, deliverables, pricing, terms, and appendices.
- **Sample Dataset** (`pharos-micro1-sample-dataset-schema-and-examples.json`) — Proof-of-concept JSON with schema and realistic example records (use with the data dictionary).
- **Response Email** (`pharos-micro1-response-email.md`) — Calibrated qualification email.

These are designed to be consistent, professional, and low-pressure. Use the response email + one-pager + domain map for initial outreach. Deliver sample + dictionary under NDA. Customize the proposal after the call based on the categories they prioritize.

## Recommended Next Steps

1. Review and lightly customize the prepared materials (especially numbers after any fresh audit).
2. Send the response email (or use the call posture to book a qualification call directly).
3. On/after the call: confirm priority categories, send NDA + controlled sample (25–50 records from cleanest buckets, e.g., signals + LegiPro conveyor/extraction).
4. Follow up with the pilot proposal (customized) and scoping workshop if the sample validates.
5. Parallel: complete detailed licensability audit and redaction pass on remaining Blackboard pillars (Danny/operator side).

This package positions Pharos as a credible, specialized producer of high-value governance and professional evaluation data — ready to move from qualification to a paid pilot on a two-week timeline.

Contact: Martin Lepage, Founder, Pharos AI — ml@pharos-ai.ca

---

*This document is the authoritative internal and pre-NDA external reference. All other prepared materials are derived from or consistent with it.*