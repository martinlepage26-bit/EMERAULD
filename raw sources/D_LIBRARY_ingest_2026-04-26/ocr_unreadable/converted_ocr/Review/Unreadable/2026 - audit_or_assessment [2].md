---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf - 2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf - 2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf.pdf
pages_total: 2
text_first_pages: 2
text_last_pages: 0
pdfinfo:
  Author: "(anonymous)"
  CreationDate: "Mon Feb  2 13:32:51 2026 EST"
  Creator: "(unspecified)"
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "4863 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  ModDate: "Mon Feb  2 13:32:51 2026 EST"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "612 x 792 pts (letter)"
  Pages: "2"
  Producer: "ReportLab PDF Library - www.reportlab.com"
  Subject: "(unspecified)"
  Suspects: "no"
  Tagged: "no"
  Title: "(anonymous)"
  UserProperties: "no"
aliases: [orphan-raw-2026-05-06-102, post-dr-sort-rename-residual-2026-05-06-085]
dr_sort_original_filename: "2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf - 2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf - 2026 - audit_or_assessment [2].pdf - 2026 - audit_or_assessment [2].pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# (anonymous)

## Extracted Text

Auditing Fairness in a Healthcare Appointment No-Show
Model
Fairness Audit Report (AI Fairness 360-style workflow)
Client: MedCare Health Network
Consultant: (Your Name)
Date: 2026-02-02

1) AI Tool and Process Overview
This audit follows the course workflow: load the provided dataset, select a protected attribute, compute
Disparate Impact and Statistical Parity Difference, apply a mitigation method (reweighing), then re-compute
the metrics and write a short, non-technical report with recommendations.

Dataset & model (for audit)
Dataset: synthetic_healthcare_appointments.csv (100 records). Target label: appointment_missed (1 =
missed, 0 = not missed). For this audit, a baseline predictive model was trained and evaluated on a held-out
test split to generate predictions for fairness measurement. Favorable outcome is defined as the model
predicting a patient will *not* miss the appointment (prediction = 0).

2) Audit Findings and Key Metrics
Protected attribute selected: Age group (65+ vs <65). Privileged group: <65. Unprivileged group: 65+.
Metric (favorable = predict not missed)

Baseline (before mitigation)

After reweighing (mitigated)

Selection rate (privileged)

0.800

0.600

Selection rate (unprivileged)

0.300

0.500

Disparate Impact (unpriv/priv)

0.375

0.833

Statistical Parity Difference (unpriv - priv)

-0.500

-0.100

Interpretation (plain language): In the baseline model, patients aged 65+ received the favorable prediction
(“will not miss”) at a much lower rate than patients under 65 (0.300 vs 0.800). This produces a Disparate
Impact of 0.375, which is far below the commonly used 0.80 threshold and indicates a strong disparity. After
applying reweighing during training, the gap narrowed (0.500 vs 0.600), improving Disparate Impact to 0.833
and bringing Statistical Parity Difference closer to zero (-0.100).

3) Recommendations and Reflections
Recommendation 1 (deployment readiness): Do not deploy the baseline model as-is. The observed
age-related disparity is large enough to create ethical and operational risk (patients who could benefit from
reminders/support may be deprioritized). Use the mitigated model (or continue mitigation iterations) and
re-test on a larger, more representative dataset before any production release.

Recommendation 2 (what to do next): Pair reweighing with (a) threshold tuning per group, (b) feature
review to remove “proxy” variables that may encode age-related disadvantage, and (c) ongoing monitoring in
production (monthly fairness checks, drift checks, and a documented escalation path if disparities reappear).
Reflection: In healthcare contexts, “fairness” is not only a compliance issue. It directly affects access to care
and patient outcomes. Fairness auditing should be treated as a repeatable operational control, not a one-time
test.

## Related

- [[Governance and PHAROS MOC]]
- [[Responsible AI Evaluation — Patient Readmission Model]]
