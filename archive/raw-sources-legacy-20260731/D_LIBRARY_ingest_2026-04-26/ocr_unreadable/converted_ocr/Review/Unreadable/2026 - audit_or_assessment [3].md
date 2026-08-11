---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf - 2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf - 2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf.pdf
pages_total: 1
text_first_pages: 1
text_last_pages: 0
pdfinfo:
  Author: "(anonymous)"
  CreationDate: "Fri Jan 30 16:45:39 2026 EST"
  Creator: "(unspecified)"
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "3709 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  ModDate: "Fri Jan 30 16:45:39 2026 EST"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "612 x 792 pts (letter)"
  Pages: "1"
  Producer: "ReportLab PDF Library - www.reportlab.com"
  Subject: "(unspecified)"
  Suspects: "no"
  Tagged: "no"
  Title: "(anonymous)"
  UserProperties: "no"
aliases: [orphan-raw-2026-05-06-104, post-dr-sort-rename-residual-2026-05-06-087]
dr_sort_original_filename: "2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf - 2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf - 2026 - audit_or_assessment [3].pdf - 2026 - audit_or_assessment [3].pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# (anonymous)

## Extracted Text

AI Security Audit Report: MedDiagnose AI
Context: MedDiagnose AI is an LLM fine-tuned on 5 million anonymized EHRs and exposed via a cloud
REST API for hospital integration.

Threat 1 (LO1): Membership/Model-Inversion via Confidence Scores
(Inference Attack)
The Threat: An attacker with API access can issue many crafted symptom descriptions and observe the
returned confidence scores. By comparing score patterns for targeted symptom combinations, they may infer
whether specific rare cases were present in the training set (membership inference) and, in aggregate,
reconstruct sensitive attributes about cohorts (model inversion). This is especially risky in healthcare, where
rare conditions can be inherently identifying.
Lifecycle Stage Affected: Deployment (attack execution) and Data/Training (memorization and overfitting
risk).
Recommended Mitigation: Reduce leakage by (1) training with privacy-preserving techniques (e.g.,
differential privacy or regularization focused on memorization), (2) limiting or rounding confidence scores and
returning calibrated ranges rather than precise probabilities, and (3) adding an output privacy filter that blocks
responses that appear to disclose patient-level details.

Threat 2 (LO2): Training Supply-Chain Compromise (Lifecycle
Vulnerability)
The Threat: Training relied on popular open-source libraries pulled from public repositories without formal
security scanning. A poisoned dependency (typosquatting, compromised maintainer account, or malicious
update) could execute during ETL/training to exfiltrate the EHR dataset, steal API keys, or implant a hidden
backdoor that triggers unsafe outputs for specific symptom strings.
Lifecycle Stage Affected: Model Training (and associated build/ETL pipeline).
Recommended Mitigation: Implement a secure MLOps supply-chain program: pin and hash dependencies,
use an internal package mirror, generate an SBOM, and run automated dependency and container scans
(e.g., pip-audit/SCA) on every build. Require signed artifacts, least-privilege IAM for training jobs, and secrets
management to prevent credential exposure.

Threat 3 (LO3): Unbounded API Abuse Enables Model Extraction and
Denial-of-Service
The Threat: The API uses a static key and has no rate limiting or robust input validation. A stolen key (or a
misused partner key) can be used to send unlimited requests to (a) systematically extract the model’s
decision boundary (model stealing) and (b) overwhelm the service, degrading availability for clinical users.
Lifecycle Stage Affected: Deployment.
Recommended Mitigation: Enforce per-client quotas and burst rate limits, add anomaly detection and
logging, rotate keys regularly, and move to stronger client authentication (mTLS or OAuth with short-lived
tokens). Add request size limits, schema validation, and an API gateway policy to reduce abusive traffic and
operational risk.

## Related

- [[Governance and PHAROS MOC]]
- [[ChatGPT Apps SDK — Planning, Metadata, Deployment, and Operations]]
