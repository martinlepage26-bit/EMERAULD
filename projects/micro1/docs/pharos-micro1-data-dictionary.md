# Pharos AI Data Dictionary
## Structured Evaluation & Governance Traces

**Version**: 2026-06-09  
**Applies to**: HELIX (adversarial evaluation), Blackboard/COMPASS (governance decision logs), LegiPro (professional domain extraction & intent)

This dictionary defines the canonical fields for all exportable datasets. All fields are designed to be:
- Directly usable for RLHF / evaluation / red-teaming training
- Anonymizable / licensable with clear boundaries
- Reproducible via the deterministic Pharos / LegiPro production pipelines

## Core Record Schema (JSON)

| Field | Type | Required | Description | Allowed Values / Examples | Redaction / Licensing Notes | Provenance Requirements |
|-------|------|----------|-------------|---------------------------|-----------------------------|-------------------------|
| `record_id` | string | Yes | Unique identifier within the delivered batch | "HELIX-001", "BB-SIG-11987", "LP-CONV-3192" | Can be opaque hash if needed for anonymity | Must be stable across deliveries |
| `pipeline` | string | Yes | Source production pipeline | "HELIX", "BLACKBOARD", "COMPASS", "LEGIPRO_CONVEYOR", "LEGIPRO_EXTRACTION", "LEGIPRO_AUTOCOMPLETE" | — | — |
| `domain` | string | Yes | Primary institutional or professional domain | "institutional_governance", "regulatory_compliance", "healthcare_ai", "financial_governance", "legal_accounting", "clinical_decision_support" | Use controlled vocabulary | — |
| `input_scenario` | string \| object | Yes | The triggering context, query, or scenario presented to the system | Free text or structured (e.g. { "query": "...", "source_family": "..." }) | Redact any client PII or proprietary scenario details | Timestamp of input |
| `system_response` | string \| object | Yes | Raw or normalized output from the AI / workflow under test | — | Can be lightly redacted for sample | — |
| `probe_type` | string | No (HELIX only) | Adversarial probe category | "ANCHOR", "MIRROR", "TRAP", "FALSE_POSITIVE_SUPPRESSION", "RECURSIVE_MANIPULATION", "N/A" | — | — |
| `failure_mode` | string | Yes | Classified failure or boundary violation | "authority_inflation", "evidence_drift", "overclaim", "source_hallucination", "sycophancy", "claim_boundary_violation", "source_path_ambiguity", "N/A" | Use controlled vocabulary from Pharos taxonomy | — |
| `human_correction` | string | Yes | The actual change, decision, or annotation made by the expert | — | Core value — protect the reasoning but the correction itself is usually licensable | Reviewer identity |
| `rationale` | string | Yes | Expert (PhD-level) reasoning explaining why the correction was required and what institutional / professional logic governed it | "The original claim crossed from model interpretation into institutional fact without primary source. In governance workflows this creates downstream liability because..." | This is the premium layer. Full rationale is high-value; can be summarized for lower tiers. | Must include reviewer credentials / role |
| `outcome` | string | Yes | Final disposition of the case | "DEFER", "APPROVE_WITH_CONDITIONS", "QUARANTINE", "ACCEPT", "REJECT", "APPROVE" | Controlled vocabulary | — |
| `risk_tier` | string | Yes | Assessed risk level before correction | "low", "medium", "high", "critical" | — | — |
| `claim_boundary` | string | Yes | Explicit statement of what was permitted vs. forbidden in the final output | "Permitted: description of proposal content. Forbidden: any assertion of external regulatory acceptance without primary source citation." | This field is often the most valuable for training "safe claim generation" | — |
| `provenance` | object | Yes | Structured audit metadata | See sub-fields below | Minimize identifiers for sample; full for production delivery | Always required |
| `provenance.timestamp` | ISO-8601 datetime | Yes | When the human correction / decision was recorded | "2026-05-12T14:22:00Z" | — | — |
| `provenance.reviewer` | string | Yes | Role or pseudonym of the expert reviewer | "Governance lead (PhD)", "LegiPro extraction QA" | Can be role-only for anonymity | Must be traceable internally |
| `provenance.workflow_version` | string | Yes | Version of the deterministic pipeline that produced this record | "pharos-helix-v3.2", "legipro-conveyor-v2.7" | — | — |
| `provenance.signature_status` | string | Yes | Cryptographic or manual signing status | "signed", "receipt_verified", "unsigned" | "unsigned" rows should be noted in delivery | — |
| `format_notes` | string | No | Any special serialization, schema, or delivery notes for this record | "Full lifecycle event + manifest + patch record" | — | — |

## Pipeline-Specific Extensions

**HELIX (Adversarial Evaluation Traces)**
- Additional recommended fields: `model_name`, `model_version`, `temperature`, `hedge_count`, `original_confidence_language`

**Blackboard / COMPASS (Governance Decision Logs)**
- Additional recommended fields: `task_id`, `pillar` (ops/product/docs/review/research/runtime), `escalation_trigger`, `veto_authority_used`

**LegiPro (Professional Domain)**
- Additional recommended fields: `source_family`, `intent_hint`, `route_bias_rule`, `bad_source_rejection_rule`, `extraction_confidence`, `quarantine_reason`

## Delivery & Licensing Constraints (Mandatory in Every Package)

- **Never license raw source corpus text** (BofIP, CGI, official filings, client workpapers) — only the labels, routing decisions, traces, and judgments around them.
- **Google autocomplete raw rows** are not licensable. Only the normalized intent + transformation rules are.
- **Field minimization** is required before any sample leaves the building (strip internal schema names that reveal architecture, e.g., "gce_sf_v4_coverage_bridge").
- **Client data contamination** check required: any row that could contain ExterminationDG or other client-specific operational data must be classified "off-limits" or heavily redacted.
- **Provenance** must travel with the record. "Signed" or "receipt_verified" rows command premium pricing.

## Example Record (condensed)

See the companion `pharos-micro1-sample-dataset-schema-and-examples.json` for three fully populated examples (one per major pipeline).

## How to Use This Dictionary

1. Every delivered batch must include a copy of this dictionary (or a versioned link).
2. All records in a batch must conform to the schema above.
3. A separate "field map" JSON can be provided for the first pilot if the buyer wants minor field renames.
4. Quality SLA: every record must have non-empty `human_correction`, `rationale`, `claim_boundary`, and `provenance`.

**Contact for questions on this dictionary**: ml@pharos-ai.ca

This dictionary is itself versioned and will be updated only with explicit buyer agreement on new fields.
