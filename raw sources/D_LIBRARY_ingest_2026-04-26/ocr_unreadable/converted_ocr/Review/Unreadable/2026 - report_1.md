---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - report_1.pdf - 2026 - report_1.pdf.pdf - 2026 - report_1.pdf - 2026 - report_1.pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - report_1.pdf - 2026 - report_1.pdf.pdf - 2026 - report_1.pdf - 2026 - report_1.pdf.pdf.pdf
pages_total: 2
text_first_pages: 2
text_last_pages: 0
pdfinfo:
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "62004 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "596 x 842 pts (A4)"
  Pages: "2"
  Producer: "Skia/PDF m146 Google Docs Renderer"
  Suspects: "no"
  Tagged: "yes"
  Title: "Explaining Model Predictions to Build Trust"
  UserProperties: "no"
dr_sort_original_filename: "2026 - report_1.pdf - 2026 - report_1.pdf.pdf - 2026 - report_1.pdf - 2026 - report_1.pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - report_1.pdf - 2026 - report_1.pdf.pdf - 2026 - report_1.pdf - 2026 - report_1.pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# Explaining Model Predictions to Build Trust

## Extracted Text

Explaining Model Predictions to Build Trust
Name: M. Lepage​
Date: J2026-02-02
1. Use Case and Model Purpose
This AI system is designed to predict the likelihood that a patient will be readmitted to the
hospital within 30 days of discharge. The goal of the model is not to replace clinical
judgment, but to support care teams by identifying patients who may need additional
follow-up, monitoring, or resources after leaving the hospital. By flagging higher-risk
patients early, clinicians can intervene proactively and potentially prevent avoidable
readmissions.
2. Model Output and Prediction
For the patient analyzed in this report, the model predicts a high risk of hospital readmission,
estimated at 83%. This prediction is based on a combination of medical history, discharge
information, and recent clinical indicators. The score represents a probability, not a certainty,
and should be interpreted as a signal for closer clinical attention rather than a definitive
outcome.
3. Explanation of Key Influencing Factors (Explainability)
Explainability tools were used to understand why the model produced a high-risk prediction.
Both SHAP and LIME highlight similar contributing factors, which strengthens confidence in
the explanation.
The most influential factor was the absence of a scheduled follow-up appointment after
discharge. Without follow-up care, potential complications may go unaddressed, increasing
the chance of readmission.​
Other important contributors included the patient’s history of stroke, which reflects
underlying chronic health risks, and shortness of breath at discharge, suggesting unresolved
symptoms.​
Age over 70 also increased risk, as older patients often require longer recovery and
additional support. Finally, missed medication doses contributed to the prediction, since
inconsistent medication adherence can worsen existing conditions.
Together, these factors explain why the model assessed this patient as high risk rather than
presenting a risk score without context.
4. Consistency Across Explainability Methods
Both SHAP and LIME identified the same core risk drivers, although with slightly different
ranking orders. In both methods, the lack of a follow-up appointment remained the strongest
contributor, followed by clinical history, age, respiratory symptoms, and medication

adherence. This consistency across tools increases trust in the model’s explanation and
reduces concern that the result is driven by unstable or misleading features.
5. Communication for Non-Technical Stakeholders
In simple terms, the model predicts a high chance of readmission because the patient does not
yet have a follow-up visit scheduled, has a serious medical history, experienced breathing
issues at discharge, is over 70 years old, and has missed some medications. These are all
factors clinicians already recognize as important. The AI helps bring them together into a
single risk signal, making it easier to prioritize care without requiring staff to interpret
technical metrics or algorithms.
6. Responsible Use, Limitations, and Ethical Reflection
This prediction should be used as decision support, not as an automated decision. The model
does not account for all social or contextual factors, such as caregiver availability or
transportation access, which may also affect outcomes. There is also a risk of over-reliance if
scores are treated as definitive. For this reason, human review is essential, especially for
high-risk cases.
Explainability plays a key role in responsible AI use in healthcare. By showing why the
model reached its conclusion, clinicians can validate the result, challenge it when necessary,
and identify actionable steps such as scheduling follow-up care or improving medication
adherence. This transparency helps build trust, supports accountability, and ensures the AI
system enhances patient-centered care rather than replacing it.

## Related

- [[Writing and Novels MOC]]
- [[Responsible AI Evaluation — Patient Readmission Model]]
