# Pharos AI Domain Map
## Governance & Professional Evaluation Data Production Capabilities

**Version**: 2026-06-09  
**Purpose**: External one-pager for micro1 qualification call  
**Company**: Pharos AI

Pharos AI operates deterministic, expert-governed data production pipelines that generate high-value structured traces for AI training and evaluation. We produce two complementary categories:

1. **Governance Evaluation Data** — How institutional AI systems make decisions under constraint.
2. **Professional Domain Evaluation Data** — How expert systems retrieve, cite, extract, and bound claims in high-stakes professional fields.

Below is the domain matrix showing where we operate today and what makes our traces uniquely valuable.

| Domain | Primary Data Types Produced | Domain-Specific Characteristics & Value | Why This Is Rare / Hard to Replicate |
|--------|-----------------------------|-----------------------------------------|-------------------------------------|
| **Institutional & Regulatory AI Governance** (Blackboard / COMPASS / HELIX) | Task / checkpoint / escalation / veto / override / resolution logs<br>Adversarial evaluation traces (probe types: ANCHOR, MIRROR, TRAP, etc.)<br>Human rationale + outcome records<br>Signed provenance events | • Explicit modeling of "lawful basis", risk appetite, veto authority, and claim-boundary enforcement<br>• Recursive review cycles (human-in-the-loop correction of AI outputs)<br>• Failure modes: authority inflation, evidence drift, overclaim, sycophancy<br>• Output includes: input scenario, system response, classified failure, expert correction + rationale, final bounded claim | PhD-level socio-anthropological + technical depth on how organizations produce legitimacy and close decision loops. Most data suppliers produce "the model answered X"; we produce "why the expert overrode it and what institutional rule required the override." |
| **Healthcare / Clinical AI Governance** | Same governance trace structure applied to clinical decision support, diagnostic aids, treatment recommendation systems | • Patient safety constraints<br>• Regulatory (FDA, Health Canada, etc.) compliance gates<br>• Ethical override scenarios (e.g., bias in triage, over-treatment recommendations)<br>• Evidence-packet requirements for liability | Rare combination of deep clinical governance understanding + technical implementation of audit trails and human override protocols. |
| **Financial Compliance & Risk AI** | Governance decision logs for credit, fraud, AML, KYC, claims, and trading surveillance systems | • Regulatory (OSFI, SEC, etc.) and internal risk appetite translation into automated decisions<br>• Override rationale for "false positive" suppression vs. real risk<br>• Audit-ready proof packets | High-stakes domain where "why we overrode the model" has direct regulatory and capital impact. Few suppliers produce expert-annotated governance traces here. |
| **Legal & Professional Services AI** (LegiPro) | Conveyor extraction/validation traces<br>Autocomplete intent normalization packs<br>Extraction JSON + tests<br>Source-authority scoring records | • Claim-boundary enforcement in tax/accounting/legal corpora (e.g., "test_no_forbidden_overclaim_language")<br>• Messy user query → professional intent → source-family routing + bias rules → expected result + bad-source rejection<br>• Source rights posture, authority scoring, and ingestability decisions | Deep domain expertise in French/Canadian accounting & tax + structured workflow data that teaches safe retrieval and citation. The transformation layer (intent + routing + rejection rules) is far more valuable than raw corpus text. |
| **Regulatory & Public Policy AI** | Cross-cutting governance + professional traces focused on compliance rule application | • How models interpret and apply complex, frequently changing regulations<br>• Evidence of "what the regulator actually requires" vs. model hallucination<br>• Multi-stakeholder override (legal, compliance, policy, operations) | Combines regulatory interpretation depth with the same deterministic governance loop used in internal workflows. |

### Common Production Strengths Across All Domains
- **Deterministic & versioned methodology** — same generation → test → correction → annotation protocol. Quality is structurally consistent.
- **Built-in claim-boundary enforcement** — not added after the fact.
- **Expert (PhD-level) reasoning traces** — the premium layer buyers pay most for (RLHF / evaluation teams at frontier labs).
- **Provenance & auditability** — timestamps, reviewer identity, workflow version, partial cryptographic signatures already present in production stores.
- **Export-ready structured format** (JSON with explicit field map).

### Current Proof-of-Concept Scale (audited candidate pool, preliminary)
- Governance evaluation traces: ~15,379 potentially recoverable events (Blackboard signals bucket is the cleanest: 11,897 / 11,924).
- Professional domain traces: 7,350+ conveyor accepted candidates + 8,888 extraction artifacts + 9,344 tests + intent transformation logic (62k+ raw autocomplete rows).

These numbers are proof the pipelines run. Under a paid pilot we commit to specific delivery volumes in the domains you prioritize.

**Contact**  
Martin Lepage, Founder  
Pharos AI  
ml@pharos-ai.ca

(Prepared to deliver controlled sample under NDA immediately after qualification confirms category fit.)
