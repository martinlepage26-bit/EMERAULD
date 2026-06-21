---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - HOL---Governance-Wiki-Worksheet.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - HOL---Governance-Wiki-Worksheet.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf.pdf.pdf
pages_total: 3
text_first_pages: 3
text_last_pages: 0
pdfinfo:
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "64081 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "612 x 792 pts (letter)"
  Pages: "3"
  Producer: "Skia/PDF m146 Google Docs Renderer"
  Suspects: "no"
  Tagged: "yes"
  Title: "_04ae953e9c294f3683945e1cd071b5c8_Lesson-3-HOL---Governance-Wiki-Worksheet"
  UserProperties: "no"
dr_sort_original_filename: "2026 - HOL---Governance-Wiki-Worksheet.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf.pdf - 2026 - HOL---Governance-Wi__ad4ecb2b26fe.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - HOL---Governance-Wiki-Worksheet.pdf - 2026 - HOL---Governance-Wiki-Worksheet.pdf.pdf - 2026 - HOL---Governance-Wi__ad4ecb2b26fe.md"
dr_sort_filename_normalized: "2026-05-06"
---

# _04ae953e9c294f3683945e1cd071b5c8_Lesson-3-HOL---Governance-Wiki-Worksheet

## Extracted Text

Governance Wiki
Purpose
This model is designed to support automated credit risk evaluation for consumer lending
products, including personal loans and credit lines. It produces a creditworthiness score
that informs loan approvals, limits, and pricing.
The model is intended for use in:
●​ Initial loan application review
●​ Limit adjustment recommendations
●​ Portfolio-level risk profiling
Assumptions
The credit scoring model assumes stable macroeconomic conditions, representative
training data, consistent input feature availability, non-adversarial use, and active
human oversight for borderline decisions. However, it has notable limitations: it lacks
fairness constraints, which may result in subgroup performance disparities; its outputs
are not inherently explainable to non-technical users; it has no automated drift detection
in place, increasing the risk of performance degradation over time; and it may
underperform on underrepresented populations such as newcomers or gig workers.
Additionally, the model predates the full implementation of emerging regulations (e.g.,
AIDA, EU AI Act), and may require future updates to meet compliance expectations.
Validation Methods
The model was validated using multiple approaches to ensure predictive accuracy,
regulatory defensibility, and operational robustness. Back-testing was conducted using
holdout datasets from the original training population, simulating real-world application
to measure predictive accuracy (AUC, F1 score, default rates). Performance was
evaluated across time slices to confirm temporal stability. For benchmarking, the model
was compared against an existing logistic regression scorecard and a traditional
rules-based engine. Results showed improved precision in identifying medium-risk
applicants while maintaining parity in high-risk rejection accuracy. A fairness analysis
was carried out post hoc using demographic parity ratio and equal opportunity
difference across age, gender, and language groups. While overall fairness metrics fell
within acceptable ranges, subgroup disparities were noted and flagged for ongoing
monitoring. Stress testing was performed by simulating edge-case scenarios (e.g.,
economic downturns, sudden income variability) to assess model resilience and

volatility in score distributions. These tests revealed areas of model brittleness under
data shifts, highlighting the need for live monitoring and periodic recalibratio
Data Lineage
The credit scoring model sources data from three primary systems: (1) internal
customer relationship databases, including application history and repayment behavior;
(2) third-party credit bureau reports providing credit scores, tradeline activity, and public
records; and (3) optional self-declared data, such as employment status or income
range, collected via digital application forms. Prior to model ingestion, all data
undergoes standardization through ETL pipelines that include formatting, deduplication,
and null-value imputation. Feature engineering applies normalization, binning, and
time-window aggregation for behavioral signals (e.g., utilization trends over 3 months).
Quality checks include schema validation, outlier detection, and cross-source
consistency audits. A data quality dashboard flags anomalies daily, with lineage
traceability maintained through automated logging in the model pipeline. All
transformations are version-controlled, and snapshots of training and scoring datasets
are retained for audit and revalidation purposes.
Escalation Rules
Escalation procedures are triggered when the model exhibits behavior that exceeds
defined risk thresholds or violates compliance guardrails. Escalations are owned by the
Model Risk Manager, with support from the Data Science Lead and Compliance Officer.
Trigger conditions include significant performance degradation (e.g., AUC drop >5%),
detection of drift in key input features, fairness violations across monitored subgroups,
or flagged incidents from the monitoring dashboard (e.g., unusual rejection rates, data
anomalies).
When a trigger occurs, the Model Risk Manager initiates a review by notifying
stakeholders via the governance channel (e.g., Teams + email alert). A formal incident
report is logged, and an internal review is scheduled within 48 hours. Urgent issues
(e.g., regulatory exposure, bias findings) escalate directly to the Head of Risk and
Legal. All communication is documented, and resolution steps are tracked through a
centralized incident response tracker, with outcomes feeding into the next model
monitoring cycle and revalidation schedule.

Review Cadence

The credit scoring model is subject to a semi-annual governance review, focused on
performance validation, fairness reassessment, regulatory alignment, and operational
risk exposure. Interim monitoring reports are reviewed monthly by the Model Risk
function, but formal end-to-end evaluations occur twice per year. These include a full
review of model outputs, input data integrity, drift trends, incident history, and
compliance updates. The next scheduled review is set for August 15, 2026, with
preparatory audit checklists distributed two weeks in advanc

Regulatory References
This model’s governance, monitoring, and validation practices are designed to align with
key regulatory and industry frameworks. These include:
●​ SR 11-7 (Federal Reserve Supervisory Guidance on Model Risk Management),
●​ Basel Committee Principles for Effective Model Risk Management,
●​ EU AI Act (with emphasis on Articles 9–11, 15, 17, and 29),
●​ Canada’s Artificial Intelligence and Data Act (AIDA) – anticipated provisions
●​ NIST AI Risk Management Framework (AI RMF 1.0), and
●​ OECD AI Principles for transparency, accountability, and robustness.
Where possible, model governance also draws from internal enterprise risk policies and
financial sector best practices for high-risk automated decision systems.

Version History
Date

Author

2026-02-02

Martin Lepage

2026-02-04

Martin Lepage

2026-02-07

TBD

Changes Made
Initial draft created: model
purpose, assumptions,
validation methods, data
lineage, monitoring, and
regulatory mapping.
Added escalation rules,
review cadence, and
version history section.
Reformatted regulatory
mapping into narrative
style.
To be completed

## Related

- [[Governance and PHAROS MOC]]
- [[Research and Papers MOC]]
- [[Regulatory Arbitrage — EU AI Act + Law 25 + 93-Day Window (Synthesis)]]
- [[CONTROL ID MON-CORE-01]]
- [[2026 - CORE-01]]
