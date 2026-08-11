---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf - 2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf.pdf
source_rel: Review/Unreadable/2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf - 2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf.pdf
pages_total: 2
text_first_pages: 2
text_last_pages: 0
pdfinfo:
  Author: "(anonymous)"
  CreationDate: "Wed Dec 24 03:59:25 2025 EST"
  Creator: "(unspecified)"
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "4353 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  ModDate: "Wed Dec 24 03:59:25 2025 EST"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "595.276 x 841.89 pts (A4)"
  Pages: "2"
  Producer: "ReportLab PDF Library - www.reportlab.com"
  Subject: "(unspecified)"
  Suspects: "no"
  Tagged: "no"
  Title: "(anonymous)"
  UserProperties: "no"
dr_sort_original_filename: "2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf - 2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf - 2025 - audit_or_assessment.pdf - 2025 - audit_or_assessment.pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# (anonymous)

## Extracted Text

End-to-End AI Security Audit Report
Student Name: Ahmed Alkaabi
System: MedDiagnose AI (Medical Diagnosis Support System)
Role: External AI Security Consultant

Introduction
This report presents a high-level security audit of the MedDiagnose AI system, a cloud-based
medical diagnostic support tool that analyzes patient symptom text and generates ranked
diagnostic suggestions for clinicians. The audit identifies three significant security risks aligned with
the AI development lifecycle and proposes actionable mitigation strategies to reduce operational,
privacy, and intellectual property risks.

Threat 1 (LO1): Inference Attack Leading to Sensitive Data
Leakage
The Threat: An attacker could submit carefully crafted symptom descriptions to the deployed API in
an attempt to extract memorized or verbatim training data from the model. Because the training
data originated from electronic health records (EHRs), such an inference attack could expose
sensitive or re-identifiable patient information.
Lifecycle Stage Affected: Data Phase and Deployment Phase.
Recommended Mitigation: Implement differential privacy during model training to limit
memorization of sensitive records. Additionally, deploy output filtering and response scanning on
the API to detect and block outputs that contain PII-like patterns before responses are returned to
users.

Threat 2 (LO2): AI Supply Chain Compromise During Model
Training
The Threat: The training environment relies on open-source libraries such as PyTorch, Hugging
Face Transformers, and pandas downloaded from public repositories. Without dependency security
scanning, a compromised or malicious package could introduce backdoors or data exfiltration logic
into the training pipeline.
Lifecycle Stage Affected: Model Training Phase.
Recommended Mitigation: Enforce software supply chain security controls, including dependency
vulnerability scanning, package integrity verification, and the use of approved internal package
repositories. Training environments should also be isolated with restricted network access.

Threat 3 (LO3): Lack of Rate Limiting Enabling Model Extraction
The Threat: The deployed API uses a static API key and lacks rate limiting. An attacker or
competitor could automate millions of requests to systematically collect model outputs and recreate
a functionally equivalent model, resulting in intellectual property theft.
Lifecycle Stage Affected: Deployment Phase.
Recommended Mitigation: Implement strict API rate limiting, per-client usage quotas, and
anomaly detection to identify abusive query patterns. These controls significantly increase the cost
and difficulty of large-scale model extraction attempts.

Conclusion
This audit demonstrates that MedDiagnose AI faces meaningful risks across data, training, and
deployment stages. By addressing inference risks, securing the AI supply chain, and strengthening
API protections, InnovateHealth AI can significantly improve the security posture and
trustworthiness of the system prior to clinical deployment.

## Related

- [[Governance and PHAROS MOC]]
- [[PHAROS Runbook SOP]]
