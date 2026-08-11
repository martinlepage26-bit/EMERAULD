---
type: raw-source
title: Executive Summary
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/Executive Summary.md
---



**Commercial Brief — Q2 2026**
**For: Chief Risk Officers, Heads of Model Risk Management, AI Governance Leads**

---

## Executive Summary

On August 2, 2026 — 93 days from the date of this brief — the high-risk AI obligations of EU Regulation 2024/1689 (the EU AI Act) become enforceable. The Digital Omnibus proposal that would have postponed this deadline failed at trilogue on April 28, 2026. As of this writing, no delay is legally in force. Penalties for non-compliance reach €35 million or 7% of global annual turnover.

For Canadian financial institutions, insurers, and Crown corporations, the operative regimes are not theoretical. They are: **Quebec Law 25** (in full force since September 2024, penalties up to $25M CAD or 4% of global turnover), the **OSFI E-23 Guideline on Model Risk Management** (in force May 2027, with examination expectations now), and **EU AI Act extraterritorial provisions** for any Canadian entity providing AI systems used in the EU market or whose outputs are used in the EU.

Most organizations facing these regimes will buy **compliance theater**: a binder of policies, a checklist of controls, an attestation signed by an external auditor. Compliance theater satisfies the inspector for a day. It does not survive incident review, regulatory examination, or board scrutiny when an AI system fails.

PHAROS AI builds the other thing. **Continuous assurance of AI systems through layered, evidence-tiered governance** — engineered so that when nobody is watching, the controls still work, and when something does fail, the failure is traceable, bounded, and reportable.

This brief explains what we do, in the language of the procurement frameworks you already use: ISO/IEC 42001:2023, NIST AI RMF 1.0 (with the GenAI Profile), EU AI Act Articles 9, 10, 13–17, 26, 27, and 72, and the OSFI three-lines-of-defense model. It closes with three engagement options sized for organizations at different points in their governance maturity.

The headline: if your organization will face AI regulatory examination in the next eighteen months and you are not already at evidence-ready posture, you have a window measured in weeks, not quarters.

---

## 1. The 2026 Compliance Reality

The regulatory perimeter facing a Canadian financial institution, insurer, or public-sector AI deployer in 2026 is no longer hypothetical. Five live pressure points:

**EU AI Act, Article 6 and Annex III — high-risk systems.** AI used in credit scoring, employment decisions, education, essential public services, biometric identification, and critical infrastructure becomes high-risk on August 2, 2026. High-risk providers must implement a risk management system (Art. 9), data governance (Art. 10), technical documentation (Art. 11), record-keeping (Art. 12), transparency to deployers (Art. 13), human oversight (Art. 14), accuracy, robustness, and cybersecurity (Art. 15), a quality management system (Art. 17), conformity assessment, CE marking, and EU database registration (Art. 49). Deployers carry parallel obligations under Article 26 and, for public-sector deployments, a fundamental rights impact assessment under Article 27.

**OSFI E-23 — Model Risk Management.** The revised guideline, applicable to all federally regulated financial institutions effective May 1, 2027, materially expands the scope of "model" to include AI and ML systems and requires organization-wide model risk management frameworks with documented model inventories, independent validation, and ongoing monitoring. Examiners are setting expectations now.

**Quebec Law 25.** In full force since September 22, 2024. Applies to any organization handling personal information of Quebec residents. Section 12.1 imposes specific obligations for automated decisions, including notification, the right to human review, and disclosure of the personal information used and the principal factors and parameters that led to the decision. Penalties up to $25M CAD or 4% of global turnover. The Commission d'accès à l'information has audit and order-making powers.

**Federal vacuum.** Bill C-27, including the Artificial Intelligence and Data Act (AIDA), died on the order paper at prorogation in January 2025 and has not been reintroduced. Federal AI regulation in Canada is currently absent. Provincial frameworks and sectoral regulators (OSFI, AMF, Santé Canada) carry the load.

**Sectoral and procurement signals.** ISO/IEC 42001:2023 is increasingly cited in enterprise RFPs as a procurement prerequisite. NIST AI RMF 1.0 with the Generative AI Profile (NIST AI 600-1) is the de facto reference for U.S. counterparties. The Canadian Centre for Cyber Security and the Bank of Canada have both issued AI-specific risk guidance referenced by examiners.

The aggregate effect: an organization deploying AI in any decision-bearing function now faces overlapping, non-identical compliance regimes with materially different evidence requirements. Building a separate program for each is unaffordable. Building one program that satisfies all of them is the work.

---

## 2. Why Most Approaches Fail

The dominant pattern in AI governance consulting is what we call the **binder pattern**. An external firm arrives, conducts a gap assessment against a chosen framework (typically ISO 42001 or NIST AI RMF), produces a written policy suite, runs a workshop, and leaves a binder. The organization's legal and compliance teams accept the deliverable. The binder sits on a shelf.

Six months later, an incident occurs. A model produces a discriminatory outcome, a chatbot leaks personal information, a credit decision cannot be explained to a regulator. Investigation reveals: the binder existed, the policies were never operationalized, the controls were never tested, the evidence the regulator now requires was never captured.

This is not a hypothetical. It is the documented failure mode in every jurisdiction that has begun examining AI systems against governance standards. The pattern has three structural causes.

**First, framework substitution masquerading as governance.** Mapping policies to ISO 42001 clauses is necessary but not sufficient. Clauses 6.1.2 (AI risk assessment), 6.1.4 (AI system impact assessment), and Annex A.6 (AI system life cycle) require evidence of operation, not evidence of documentation. An auditor can verify the existence of a risk register. A regulator examining an incident asks how the register was used to prevent the incident.

**Second, the absence of independent challenge.** OSFI's three-lines-of-defense model requires the second line (risk management) to be operationally independent of the first (the business deploying the model). Most consulting deliverables embed the assurance function inside the development team. When the development team is also writing the controls and evaluating them, the controls drift toward what is convenient rather than what is sound.

**Third, no evidence tiering.** Regulators distinguish between what an organization claims, what it can demonstrate with internal documentation, and what it can demonstrate with externally-verifiable evidence. Most governance programs treat all three as equivalent. Under examination, only the third tier holds. Programs that don't tier evidence in advance produce volumes of paper that satisfy nobody.

The PHAROS approach is built around the failure modes that the binder pattern produces. Not as a critique — as the design constraint.

---

## 3. The PHAROS Approach in Procurement Language

PHAROS AI's methodology is **continuous assurance of AI systems through evidence-tiered, layered governance with mandatory independent challenge.** It maps to existing frameworks; it is not a parallel framework competing with them. The differentiator is operational depth — the methodology is engineered to produce evidence that survives examination, not to produce documents that pass procurement intake.

The core practice has four operating principles:

**Continuous, not periodic.** AI systems drift. Training data goes stale, deployment context shifts, model behavior changes under load. PHAROS engagements build assurance cycles measured in weeks, not annual reviews. Continuous monitoring is mandatory under EU AI Act Article 72 (post-market monitoring) and aligns directly with NIST AI RMF MANAGE-4 (regular monitoring of risks and benefits).

**Evidence-tiered.** Every claim about an AI system is classified into three tiers: documented (what the organization asserts), supported (what internal evidence corroborates), and verified (what external or independent evidence corroborates). Tier discipline maps to OSFI E-23's documentation expectations and to ISO 42001 Clause 9.1 (monitoring, measurement, analysis, evaluation).

**Mandatory independent challenge.** The PHAROS methodology embeds an independent challenge function in every assurance cycle. The function is structurally separate from the development team and produces written challenge memoranda that are retained as part of the audit trail. This implements OSFI's second line of defense and satisfies ISO 42001 Annex A.6.2.7 (verification and validation by an independent party).

**AND-gate enforcement at deployment.** No AI system advances from one lifecycle stage to the next without all required gates clearing simultaneously. A system with a passing accuracy assessment but an unresolved fundamental rights impact does not deploy. AND-gate enforcement implements EU AI Act Article 9 (risk management system), Article 14 (human oversight), and Article 27 (FRIA).

### Mapping Table — PHAROS Approach to Procurement Frameworks

| PHAROS Element | ISO/IEC 42001:2023 | NIST AI RMF 1.0 | EU AI Act |
|---|---|---|---|
| Continuous assurance cycle | Cl. 9.1, 9.2, 10 | MANAGE-4, MEASURE-2 | Art. 9, Art. 72 |
| Evidence tiering | Cl. 7.5, A.4.5 | GOVERN-1.4, MEASURE-1.3 | Art. 11, Art. 12 |
| Independent challenge function | A.3.2, A.6.2.7 | GOVERN-3.2, GOVERN-4.3 | Art. 17(c) |
| AND-gate deployment review | A.6.2.2, A.6.2.5 | MAP-5, MANAGE-1 | Art. 9, Art. 14, Art. 27 |
| Pre-deployment risk identification | Cl. 6.1.2, A.5.2 | MAP-1, MAP-2 | Art. 9(2), Art. 27 |
| Lifecycle traceability | A.6.2, A.7 | GOVERN-1.7, MAP-4 | Art. 11, Art. 12, Art. 13 |
| Third-party AI system assurance | A.10 | GOVERN-6, MAP-4.1 | Art. 25, Art. 28 |
| Incident response and reporting | Cl. 10.2 | MANAGE-4.3 | Art. 73 |
| Human oversight design | A.6.2.6, A.9.3 | MEASURE-2.6, MANAGE-2 | Art. 14 |
| Fundamental rights / impact assessment | Cl. 6.1.4, A.5 | GOVERN-5, MAP-5.1 | Art. 27 |

### Methodological Foundation

The methodology rests on socio-technical governance research — the principle that AI systems fail not because individual technical controls are weak, but because organizational structures, incentive systems, and decision rights determine whether technical controls are operated as designed. This is the basis for NIST AI RMF's GOVERN function and for ISO 42001's emphasis on management system architecture in Clauses 4 through 7.

PHAROS AI's principal, Martin Lepage, brings doctoral-level training in qualitative methods and institutional analysis to bear on the question every framework asks but few answer in the field: *under what organizational conditions do AI controls actually operate?* The methodology converts that research base into deliverables that procurement teams can specify, audit teams can verify, and examiners can examine.

---

## 4. Engagement Models

Three entry points, sized for different governance maturity levels and budget envelopes. All three produce examination-ready deliverables.

### Tier 1 — AI Governance Readiness Diagnostic

**Duration:** 4–6 weeks
**Format:** Fixed fee
**Deliverable:** Written diagnostic against ISO/IEC 42001:2023 and the EU AI Act high-risk requirements, with prioritized remediation roadmap and twelve-month implementation budget envelope.

The diagnostic identifies the organization's AI system inventory, classifies systems by risk tier under the EU AI Act and OSFI E-23 definitions, evaluates existing controls against framework requirements, identifies the highest-impact gaps, and sequences remediation by regulatory exposure and effort.

**Suitable for:** Organizations that have AI deployments but no current AI governance program, or have a program but no defensible mapping to incoming regulations. Required input from the organization is roughly 20–30 hours of stakeholder interviews and document review across the engagement.

**Output supports:** Board reporting on AI risk posture, internal audit committee briefings, Q3 2026 implementation planning, RFP responses requiring ISO 42001 alignment.

### Tier 2 — Implementation Sprint

**Duration:** 3–6 months
**Format:** Phased fixed fee with defined milestones
**Deliverable:** Operational AI governance capability — control library, assurance cycle calendar, independent challenge process, evidence repository, training for first-line and second-line staff, and a formal governance charter.

The Implementation Sprint takes the Tier 1 diagnostic (or an equivalent baseline) and builds the capability to operate it. PHAROS works alongside the organization's internal team — risk, compliance, technology, business — transferring methodology rather than producing artifacts the team cannot maintain.

**Suitable for:** Organizations with an AI governance commitment from senior management, an internal team of at least three FTEs allocatable to AI risk work, and a target of being examination-ready within twelve months.

### Tier 3 — Continuous Assurance Retainer

**Duration:** Ongoing, twelve-month minimum
**Format:** Monthly retainer
**Deliverable:** Quarterly independent challenge memoranda, annual program effectiveness review, examination support, and methodology adaptation as frameworks evolve.

The retainer model preserves the structural independence required by OSFI's three-lines-of-defense model while keeping continuity of methodology across the assurance cycle. Suitable for organizations whose AI deployment footprint requires sustained external challenge but whose internal second-line capacity is not yet proportionate to the risk surface.

---

## 5. About PHAROS AI

PHAROS AI is a Quebec-registered consultancy specializing in AI governance, risk, and assurance for organizations subject to EU AI Act, OSFI, AMF, and Quebec Law 25 oversight. Registered under CAE codes 7771 (management consulting) and 7759 (technical services). Bilingual delivery (English / French).

**Methodological foundation.** Doctoral-level training in qualitative institutional analysis, applied research on organizational conditions for control effectiveness, and seventeen documented methodology modules covering diagnostic, implementation, and continuous assurance work. Methodology documented in a forthcoming peer-review submission and available to engaged clients in technical detail under NDA.

**What we don't do.** We do not certify AI systems — that role belongs to notified bodies under the EU AI Act and to internal audit functions for ISO 42001 attestation. We do not develop AI systems. We do not provide technical model validation for performance metrics — that is the province of specialized model validation firms. We provide governance, assurance methodology, and independent challenge.

**Why now.** The August 2, 2026 EU AI Act deadline is 93 days from this brief's date. Quebec Law 25 examinations have begun. OSFI E-23 examiner expectations are crystallizing. Organizations that wait for federal Canadian legislation will be examined first. Organizations that buy compliance theater will be examined twice — once before the incident, once after.

---

## Contact

**Martin Lepage, Founder**
PHAROS AI
ml@pharos-ai.ca
pharos-ai.ca

*Initial conversations are no-fee and held under mutual NDA on request. Diagnostic engagements typically scope within two meetings.*

---

*This brief is provided for procurement intake and is not legal advice. Regulatory citations reflect frameworks as of May 1, 2026 and may evolve. PHAROS AI works alongside but does not replace internal legal counsel, internal audit, or notified bodies.*

## Related

- [[Governance and PHAROS MOC]]
- [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]
