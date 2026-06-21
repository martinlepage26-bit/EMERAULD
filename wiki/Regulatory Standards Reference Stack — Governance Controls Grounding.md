---
type: wiki
aliases:
  - GDPR Article 5 — Principles
  - GDPR Article 5 — Accuracy Principle Explained
  - HIPAA 45 CFR § 164 — Security and Privacy
  - FINRA Rule 4530 — Books and Records
  - ISO 15489 Records Management
  - ISO 15489 Records Management Standard
  - ISO 27001:2022 Information Security Management
  - ISO 9001 Document Control and Obsolescence Prevention
  - NIST SP 800-53 — CA-7 Continuous Monitoring
  - NIST SP 800-53...
  - NIST SP 800-53 CM-3 Change Control and Authorization
  - COBIT DSS Domain Audit Framework
  - ITIL Change Management Process
tags: [reference, regulatory, standards, governance-controls, compliance, nist, GDPR, HIPAA, ISO, FINRA, COBIT, ITIL]
status: active
created: 2026-05-02
updated: 2026-05-02
---

# Regulatory Standards Reference Stack — Governance Controls Grounding

## Summary
Single organizing hub for the regulatory standards and frameworks cited as **regulatory grounding** for the EMERAULD/PHAROS governance controls (CONTROL 1, 2, 3). Each standard is named where it appears in the governance documentation, with what it grounds and where to find authoritative current text. Reference for [[Governance Controls and Mechanisms]], [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]], [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]], [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]], and [[Governance Controls — Baseline Assessment (2026-04-26)]].

## Context
The CONTROL governance docs cite these standards as the **regulatory grounding** for their design. Inside the vault, individual `[[NIST SP 800-53...]]` brackets do not resolve to standalone notes (and creating 12 separate stubs would clutter the graph without adding value). This single note acts as the resolver: each standard appears as an alias here, and authoritative current text lives at the publishers' canonical sources, not in the vault.

The standards are reference material, not vault content. The vault's job is to **point to them, scope their application, and flag when they bind a control**.

## Standards Inventory

### Privacy and Data Protection

**GDPR — General Data Protection Regulation (EU 2016/679)**
- *GDPR Article 5 — Principles*: foundational principles for personal-data processing (lawfulness, fairness, transparency; purpose limitation; data minimization; accuracy; storage limitation; integrity/confidentiality; accountability)
- *GDPR Article 5 — Accuracy Principle Explained*: principle of accuracy plus right of rectification; grounds CONTROL 2 (External Data Lifecycle)
- Canonical text: eur-lex.europa.eu, never expires (foundational)
- Vault use: foundational reference, cited in [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]]

**HIPAA 45 CFR § 164 — Security and Privacy**
- US health-data security and privacy rule
- Canonical text: ecfr.gov (Code of Federal Regulations)
- Revision cycle: changes annually
- Vault use: cited in healthcare-AI governance work; see [[Healthcare Governance Packet — Recursive Governance for Providers]]

### Information Security and Records Management

**ISO 27001:2022 — Information Security Management**
- ISMS framework standard
- Revision cycle: ~3 years
- Vault use: foundational reference for information-security governance

**ISO 15489 — Records Management** (also "ISO 15489 Records Management Standard")
- Records management framework
- Revision cycle: ~5–7 years (stable)
- Vault use: grounds CONTROL 3 (Architecture Deprecation Protocol) — recordkeeping discipline for deprecated artifacts

**ISO 9001 — Document Control and Obsolescence Prevention**
- Quality management standard with document control clauses
- Vault use: grounds [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]] obsolescence prevention

### Continuous Monitoring and Change Control

**NIST SP 800-53 — Security and Privacy Controls** (US federal information systems)
- *CA-7 Continuous Monitoring*: grounds [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]]
- *CM-3 Change Control and Authorization*: grounds [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]]
- Canonical text: csrc.nist.gov
- Revision cycle: ~3 years (current revision: Rev. 5)
- Vault use: cited as the change-control and continuous-monitoring backbone for the EMERAULD CONTROL set

**ITIL Change Management Process**
- Service-management framework change control
- Vault use: grounds [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]] alongside NIST CM-3

### Audit and Governance Frameworks

**COBIT DSS Domain Audit Framework**
- COBIT (Control Objectives for Information and Related Technologies); DSS = Deliver, Service, Support domain
- Vault use: cited in [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]] as audit-framework grounding

**FINRA Rule 4530 — Books and Records**
- US financial-industry recordkeeping rule
- Revision cycle: ad-hoc
- Vault use: cited in [[Governance Controls — Baseline Assessment (2026-04-26)]] as a regulatory-update tracker target

## How to use this note

When a CONTROL doc cites a standard like `[[NIST SP 800-53 — CA-7 Continuous Monitoring]]`, the link resolves here. To find the authoritative current text, follow the canonical-source URL named above for the relevant standard. Do not paraphrase regulatory text in vault notes; cite the standard, name the section, and point to the publisher.

## Related

- [[Governance and PHAROS MOC]]
- [[Governance Controls and Mechanisms]] — Hub for the EMERAULD CONTROL set
- [[CONTROL 1 — Tool Layer Audit Protocol (Regulatory Grounding)]]
- [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]]
- [[CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding)]]
- [[Governance Controls — Baseline Assessment (2026-04-26)]]
- [[Governance Controls Integration Dashboard]]
- [[Governance Controls — Monitoring Plan & Automation Roadmap]]
- [[OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]
- [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]
- [[Harrowfield Clinic — AI Governance Failure Case Study]]
