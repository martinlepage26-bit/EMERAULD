---
type: raw
source_kind: pdf_text
source_path: /mnt/d/LIBRARY/Review/Unreadable/2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf - 2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf.pdf
source_rel: Review/Unreadable/2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf - 2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf.pdf
pages_total: 3
text_first_pages: 3
text_last_pages: 0
pdfinfo:
  Custom Metadata: "no"
  Encrypted: "no"
  File size: "106042 bytes"
  Form: "none"
  JavaScript: "no"
  Metadata Stream: "no"
  Optimized: "no"
  PDF version: "1.4"
  Page rot: "0"
  Page size: "596 x 842 pts (A4)"
  Pages: "3"
  Producer: "Skia/PDF m146 Google Docs Renderer"
  Suspects: "no"
  Tagged: "yes"
  Title: "Explainability Audit Report Using SHAP and LIME"
  UserProperties: "no"
dr_sort_original_filename: "2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf - 2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf.pdf.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf - 2026 - audit_or_assessment_2.pdf - 2026 - audit_or_assessment_2.pdf.pdf.pdf.md"
dr_sort_filename_normalized: "2026-05-06"
---

# Explainability Audit Report Using SHAP and LIME

## Extracted Text

Explainability Audit Report Using SHAP and LIME
Healthcare AI Model – Understanding Why the Model Flags Patients as “High Risk”
Student: M. Lepage​
Date:2026-02-02

1. This audit looks at a healthcare AI model that makes predictions about patient risk, such as
whether someone is likely to miss an appointment or need additional follow-up care. On
paper, that sounds simple. In reality, predictions like these can affect how patients are treated.
They can influence who gets extra reminders, who gets outreach calls, or who gets flagged
for care coordination.
Because the outcome can affect real people, it is not enough for the model to be “accurate.”
We need to understand why it makes certain predictions. If we cannot explain a decision
clearly, then it becomes hard to trust it, defend it, or safely use it in a clinical workflow.
2. To make the model’s decisions understandable, this audit used two explainability methods:
●​ SHAP, which helps explain patterns across the model overall (what features matter
most in general).
●​ LIME, which helps explain one prediction at a time (why the model flagged this
specific patient).
Using both tools matters, because clinicians often care about individual cases, while
leadership and governance teams care about whether the model behaves reasonably at scale.
3. LIME was used to zoom in on one example where the model predicted a patient was high
risk.
What LIME showed is that the model was not making a random decision. It focused on
factors that make sense clinically, such as:
●​ whether a follow-up appointment was scheduled​
a history of serious medical conditions
●​ recent symptoms that could worsen quickly
●​ missed medication doses
●​ older age (a smaller but noticeable factor)
LIME made it possible to translate the model’s “score” into a story: these are the main
reasons the system is worried about this patient.
That kind of explanation is exactly what clinical staff need if they are expected to act on a
model output.

4. SHAP was used to step back and look at what the model relies on across many patients, not
just one.
Overall, SHAP showed that the model consistently put the most weight on:
●​ follow-up scheduling and care continuity signals
●​ prior health history and risk indicators
●​ clinical factors tied to stability after discharge
Meanwhile, demographic and administrative features did not appear to dominate the model’s
decisions. That does not prove “no bias,” but it is a good sign that the model is mainly driven
by healthcare-relevant factors rather than inappropriate proxies.
5. Even when explanations look reasonable, there are still real risks in healthcare.
One major issue is that some predictors can reflect structural barriers, not patient choice.
For example:
●​ missed appointments may reflect transportation issues, unstable housing, shift work,
language barriers, or lack of childcare
●​ lack of follow-up could reflect system access problems, not lack of motivation
So the risk is not only whether the model is explainable. The risk is whether humans interpret
the model in a harmful way, like treating the output as blame or “noncompliance.”
Explainability helps here, because it forces us to see what the model is actually responding to,
and whether we need to handle those signals carefully.
6. Based on what SHAP and LIME revealed, here are the most important recommendations:
1.​ Use the model to support patients, not penalize them​
A high-risk flag should trigger outreach, reminders, navigation support, or care
coordination. It should not reduce access to care or lead to punitive actions.
2.​ Keep a human decision-maker in the loop​
Clinicians should treat model outputs as decision support, not final judgment. The
explanation should help a clinician say: “Does this match what I know about this
patient?
3.​ Save explanations for accountability​
If the model affects care decisions, the organization should keep explainability logs
(or summaries) so decisions can be reviewed later if needed.
4.​ Re-check model behavior regularly​
Models can drift. Patient populations and clinic workflows change. Explainability
checks should be repeated over time, not done once and forgotten.
Final Summary

This explainability audit used LIME to explain individual predictions and SHAP to
understand overall model behavior. Together, they make the model’s reasoning much easier to
interpret, communicate, and safely use in a healthcare setting. The main value is simple:
when clinical decisions are influenced by AI, we need to be able to say, clearly and
responsibly, why the model is making the recommendation it’s making, and ensure that
the recommendation leads to patient support rather than unintended harm.

## Related

- [[Research and Papers MOC]]
- [[Emotional Alliance vs. Evidentiary Discipline in AI]]
