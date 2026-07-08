---
type: wiki
title: Responsible AI Evaluation — Patient Readmission Model
aliases:
- Responsible AI Evaluation — Patient Readmission Model
- wiki/Responsible AI Evaluation — Patient Readmission Model
tags:
- wiki
- ai
- responsible-ai-evaluation-patient-readmission-model-md
- readmission
- spanish
- recall
- fairness
- clinical
- color-purple
status: active
created: '2026-06-21'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Responsible AI Evaluation — Patient Readmission Model.md
backlink_count: 13
backlinks:
- '[[wiki/AI Governance Failure Cases]]'
- '[[Areas/Personal/CDPDJ Complaint — Lepage v Calian and Novartis]]'
- '[[wiki/Care, Ethics, and Governance]]'
- '[[wiki/Consent and Boundary Frameworks]]'
- '[[Resources/Evidence Discipline and Epistemics]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/Governance by Denial]]'
- '[[wiki/Harrowfield Clinic — AI Governance Failure Case Study]]'
- '[[wiki/Home]]'
- '[[wiki/LOTUS Model and Agency]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/September 2024 Research Retrospective]]'
- '[[maps/PHAROS Method Map]]'
---

# Responsible AI Evaluation — Patient Readmission Model

## Summary
Clinical responsible AI evaluation report for a hospital patient readmission prediction model. Author: Martin Lepage, PhD (2025). Four-part evaluation framework: model performance audit, fairness analysis, model card documentation, and deployment recommendation. Key finding: **58% accuracy overall** with a **16% recall gap for Spanish-speaking patients** relative to English-speaking patients. Final verdict: **"Failed validation — do not deploy."** Supplementary principle: **"Quality must precede fairness"** — a model that performs poorly overall cannot be made fair through fairness interventions alone. Related to [[Healthcare Governance Packet — Recursive Governance for Providers]] and [[Recursive Deterministic AI Governance — Method and Paper]].

## Context
Sources: `2025 - analysis - Responsible AI Evaluation Patient Readmission Model.docx` and `2026 - Overview of model prediction.docx`. The evaluation report is the primary document; the 2026 XAI vignette (featuring a case study of a 72-year-old female patient with 83% readmission risk) is a separate document illustrating the clinical communication challenge — how to translate model predictions into actionable clinical guidance.

---

## Model Profile

**Task**: Binary classification — predict 30-day hospital readmission (yes/no)
**Population**: Hospital patients across language groups
**Architecture**: Not specified in evaluation
**Training data**: Historical readmission records

**Baseline performance**:
- Overall accuracy: 58%
- Recall gap: 16 percentage points between English-speaking and Spanish-speaking patient populations
- This recall gap means Spanish-speaking patients who will be readmitted are significantly less likely to be flagged by the model — they are more likely to be discharged without follow-up care that could prevent readmission

---

## Four-Part Evaluation Framework

### Part 1 — Model Performance Audit
Standard performance metrics evaluation:
- Accuracy (58% overall — below clinical utility threshold for deployment)
- Precision, recall, F1-score by class (readmission vs. no-readmission)
- ROC-AUC analysis
- Calibration assessment: is the model's expressed confidence aligned with actual probability?

**Finding**: The model does not meet the threshold for clinical deployment on accuracy grounds alone, before fairness analysis.

### Part 2 — Fairness Analysis
Disaggregated performance analysis by patient subgroup:
- Language (English vs. Spanish: 16% recall gap)
- Age group analysis
- Insurance status analysis

**Key finding**: The 16% recall gap for Spanish-speaking patients is the primary fairness failure. It is not a marginal gap — 16 percentage points in clinical recall means Spanish-speaking patients who need follow-up are systematically missed.

**The "Quality Must Precede Fairness" principle**: The evaluation makes an important methodological claim. A model with 58% overall accuracy cannot be remediated to fairness through fairness interventions (reweighting, calibration by subgroup, adversarial debiasing) without first addressing the fundamental performance problem. Fairness interventions on a low-accuracy model may equalize failure rates across groups without improving outcomes for anyone.

### Part 3 — Model Card Documentation
The evaluation produces a formal **model card** — a structured documentation artifact that specifies:
- Intended use and out-of-scope use cases
- Performance metrics by population subgroup
- Known limitations and failure modes
- Governance conditions for deployment consideration

The model card is not a deployment authorization — it is a documentation requirement that enables subsequent governance decisions. Even for a model that fails validation, the model card documents what was tested and found wanting, creating an auditable record.

**Model card content (from evaluation)**:
- Intended use: clinical decision support for discharge planning
- Out-of-scope: autonomous discharge decisions without clinician review
- Performance: 58% overall accuracy; 16% recall gap for Spanish-speaking patients
- Limitation: training data may underrepresent Spanish-speaking patient outcomes; socioeconomic factors not included
- Governance status: **DO NOT DEPLOY — Failed validation**

### Part 4 — Deployment Recommendation
**Verdict: Failed validation — do not deploy.**

The evaluation specifies conditions that would need to be met for resubmission:
1. Improve overall accuracy above clinical utility threshold (not specified but implied > 70%)
2. Close the recall gap to within acceptable bounds (suggested: ≤ 5 percentage points across language groups)
3. Explain the sources of the recall gap: is it training data composition, feature selection, or model architecture?
4. Assess whether accuracy improvement for Spanish-speaking patients requires separate model training or additional features

---

## XAI Vignette — 72F Patient, 83% Readmission Risk

The companion document (`2026 - Overview of model prediction.docx`) presents a clinical explainability vignette:

**Patient profile**: 72-year-old female patient, post-surgery discharge planning

**Model output**: 83% predicted probability of 30-day readmission

**SHAP (SHapley Additive exPlanations) factors contributing to high risk**:
- Age (contributes positively)
- Comorbidity count (contributes positively)
- Prior readmission history (contributes positively)
- Social support score (contributes negatively — low social support increases risk)

**LIME (Local Interpretable Model-Agnostic Explanations) output**: Consistent with SHAP — identifies same top factors, presented in counterfactual format ("If this patient had a higher social support score, readmission probability would decrease by X%")

**Plain-language communication challenge**: The vignette demonstrates that neither SHAP nor LIME outputs are directly usable by clinicians without translation. The evaluation work includes designing the communication layer — how to express model uncertainty, risk factors, and limitations in clinical language.

**The governance gap**: The XAI explanations identify contributing factors but cannot tell the clinician whether to trust the 83% figure — that requires the calibration analysis from the main evaluation. A poorly calibrated model expressing 83% confidence may be systematically overconfident, making the clinical communication misleading even if the explanation is technically correct.

---

## Connection to Healthcare Governance Packet

The evaluation operationalizes several principles from [[Healthcare Governance Packet — Recursive Governance for Providers]]:
- Disaggregated validation discharge: validation cannot be approved if equity analysis is incomplete
- Pass 8 drift detection (missing disaggregated data): the Spanish-speaking recall gap would have triggered a drift alert in the Healthcare Governance Packet's framework
- Model card as governance artifact: the Healthcare Governance Packet requires model card documentation before clinical deployment

---

## Insights

- "Quality must precede fairness" is a governance principle that pushes back against a common fairness intervention pattern: attempting to equalize outcomes across subgroups in a model that has not yet established baseline performance. The argument is not that fairness matters less — it is that fairness is not achievable through remediation of a fundamentally inadequate model
- The 16% recall gap for Spanish-speaking patients is a clinical equity finding with direct consequences: patients who need follow-up care to prevent readmission will not receive it at systematically higher rates. This is not an abstract fairness statistic — it is a healthcare outcome disparity
- The XAI vignette demonstrates that explainability is a communication design problem, not just a technical problem: generating SHAP values solves the technical explainability requirement but does not solve the clinical communication requirement. The governance gap between "technically explainable" and "clinically actionable" is a design space that the evaluation only partially addresses

## Open Questions

- Is this a real clinical evaluation (actual model, actual hospital) or a pedagogical case study? The specificity of the 58% accuracy and 16% recall gap suggests real data, but the document source context (in Martin Lepage's research archive) could be either
- What is the intended publication venue? Clinical informatics journal? AI governance journal? Educational use?
- Does the evaluation address whether the recall gap is present in other language groups, or only English/Spanish?
- What is the governance pathway for resubmission? Who has authority to approve a revised model for deployment?

## Sources
- `raw sources/2025 - analysis - Responsible AI Evaluation Patient Readmission Model.docx`
- `raw sources/2026 - Overview of model prediction.docx`
- Related: [[Healthcare Governance Packet — Recursive Governance for Providers]]
- Related: [[Recursive Deterministic AI Governance — Method and Paper]]
- Related: [[PHAROS Invention Disclosure]]
- Related: [[September 2024 Research Retrospective]]
- Related: [[CDPDJ Complaint — Lepage v Calian and Novartis]]
- Related: [[Governance by Denial]]

## Related

- [[2026 - audit_or_assessment [2]]]
- [[2026 - report_1]]
