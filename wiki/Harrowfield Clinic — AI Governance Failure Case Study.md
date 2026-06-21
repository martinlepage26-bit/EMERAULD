# Harrowfield Clinic — AI Governance Failure Case Study

## Summary
A detailed fictional or anonymized teaching case documenting a cascade of AI governance failures at "Harrowfield Clinic" across 2023, involving two AI systems (CareBot v2.1.0 and HarrowfieldDiagAI) and producing at least five documented patient harm incidents. Author: Martin Lepage, PhD (implied — case architecture matches PHAROS governance methodology). Sources: `ai_ethics_framework_DRAFT.md`, `ai_governance_policy_v3_DRAFT_UNREVIEWED.md`, `carebot_complaint_log_manual.txt`, `carebot_weekly_review_march2023.txt`, `failure_timeline_2023_summary.md`, `governance_review_evidence_summary_feb2024.txt`, `complaint_response_draft_PT10482.md`. The case is highly internally consistent (patient IDs, session IDs, dates cross-reference across 7 files) and reads as a crafted pedagogical scenario for AI governance in clinical settings. Related to [[Responsible AI Evaluation — Patient Readmission Model]] and [[Recursive Deterministic AI Governance — Method and Paper]].

## Context
Seven source files document the same fictional clinic across multiple document types (ethics framework, policy draft, complaint logs, weekly reviews, timeline, evidence summary, complaint response draft). The internal consistency (e.g., PT-10482 appears in four separate files with matching session IDs and dates) suggests deliberate construction as a teaching case. The governance failures illustrated map precisely onto the mechanisms analyzed in [[Fluency, Interruption, and Institutional Accountability]] and [[Governance by Denial]].

---

## Two AI Systems

### CareBot v2.1.0
Patient-facing chatbot deployed across clinic kiosks and digital channels. Permitted uses: appointment booking, general health information, symptom triage with escalation rules. Governed (in theory) by escalation rules including ESC-001 (cardiac symptoms → advise 999), suicidal ideation escalation, anticoagulant alert, and paediatric dose safety.

### HarrowfieldDiagAI (DiagAI)
Clinical decision support system for diagnostic assessment. Requires physician sign-off, validated intake, INR/coagulation data feed, and consent. Governed by DPIA, consent module, and physician sign-off mechanism. Version v1.4.1-beta deployed to production in error in July 2023 when rollback failed.

---

## Failure Timeline

### Q1 2023 — Nominal Operations with Known Gaps
- CareBot and DiagAI v1.2.0 in production
- Internal CareBot validation completed; external evaluation assigned to "TBC" — never resolved
- Only 3 weekly flagged-session reviews conducted in all of 2023 out of ~45 required
- The March 10 weekly review (the only detailed review in the record) flags a mental health session as "technically safe but feels very transactional" — reviewer intends to raise at team meeting; this concern is never acted on before escalation rules are disabled

### Q2–Q3 2023 — Control Degradation
- **June 1**: DiagAI v1.3.2 upgrade breaks consent module (`consent_check_enabled: false`) — never fixed
- **June 12**: Last verified DiagAI audit DB connection
- **June 15**: DPO role becomes vacant — UK GDPR Article 9 processing continues without a DPO
- **July 14**: CareBot escalation rules disabled — "for testing, re-enable not scheduled." Remain disabled until November 22 (130 days)
- **July 19**: DiagAI v1.4.1-beta deployed to production in error; rollback fails; rollback failure PDF goes missing; F. Rahman's response to urgent email: "sort it out"
- **August 1**: Physician sign-off disabled for DiagAI after load testing; JIRA ticket raised, never resolved
- **September 15**: PT-40059 (Thomas Birch) — first documented distress session; suicidal ideation rule disabled; not escalated

### Q4 2023 — Crisis Accumulation
- **October 8**: INR/coagulation feed to DiagAI fails silently
- **October 27**: JIRA API token expires; **zero escalation tickets created Oct 27–Nov 21** (25 days)
- **October 31**: DiagAI log server disk quota exceeded; log writes stop
- **November 1**: **PT-10482 (Margaret Osei) MI adverse event.** CareBot session provides cardiac information without advising 999 despite ESC-001 confidence threshold (0.81 > 0.75); DiagAI had flagged ischaemic heart disease 27 minutes earlier — not linked to CareBot session. Patient hospitalized with confirmed myocardial infarction. Solicitor instructed (Clarke & Associates)
- **November 3–21**: PT-40059 multiple additional distress sessions (scores 0.72–0.74); suicidal ideation rule disabled; JIRA broken; not escalated
- **November 5**: PT-20871 (Yusuf Adeyemi) — paediatric paracetamol dosage given for 4-year-old; paediatric rule disabled
- **November 8**: **PT-33014 (Priya Chakraborty) warfarin near-miss.** Bot advises dose skip; anticoagulant rule disabled; not in formal incident register
- **November 9**: kiosk_1 auth bypass not reset; unauthenticated session
- **November 13**: Clinical Governance Lead begins annual leave with no handover of open incidents
- **November 15**: kiosk_4 discovered — unregistered kiosk installed by facilities, running CareBot v2.0.1 since August; all sessions permanently unrecoverable
- **November 22**: PT-10482 formal complaint registered 19 days after initial contact; suicidal ideation rule "re-enabled" by F. Rahman (self-approved, testing not completed)
- **December 1**: Solicitor letter received for PT-10482; **December 29**: solicitor response deadline missed

---

## Five Documented Patient Incidents

| ID | Patient | Date | System | Incident | Governance failure |
|---|---|---|---|---|---|
| PT-10482 | Margaret Osei | Nov 1, 2023 | CareBot | MI adverse event — no 999 advice | ESC-001 disabled, JIRA down |
| PT-40059 | Thomas Birch | Sep–Nov, 2023 | CareBot | Suicidal ideation not escalated (×5) | Escalation rules disabled |
| PT-33014 | Priya Chakraborty | Nov 8, 2023 | CareBot + DiagAI | Warfarin near-miss | Anticoagulant rule disabled; INR feed broken |
| PT-20871 | Yusuf Adeyemi | Nov 5, 2023 | CareBot | Paediatric paracetamol dosage | Paediatric rule disabled |
| Unknown | Anonymous | Nov 2023 | kiosk_4 | Sessions unrecoverable | Unregistered kiosk, logs lost |

---

## Governance Architecture Failures

The case illustrates seven distinct governance failure modes:

1. **Silent rule disabling** — escalation rules disabled "for testing" with no re-enable schedule; no alert when rules remain off
2. **API dependency failure** — JIRA token expiry disabling all escalation tickets for 25 days; no monitoring of the escalation mechanism itself
3. **Beta-in-production failure** — v1.4.1-beta deployed in error; rollback fails; documentation disappears; no accountability
4. **Log loss** — disk quota exceeded; audit logs stop writing; no alert
5. **Abandoned oversight role** — DPO vacant 8 months; no cover; regulated processing continues
6. **Consent module failure** — `consent_check_enabled: false` for the full year; unquantified re-consent required
7. **Shadow infrastructure** — kiosk_4 installed by facilities without governance review; sessions permanently unrecoverable

**The PT-10482 governance finding**: CareBot's ESC-001 rule (cardiac escalation) had a confidence score of 0.81 — above the 0.75 threshold. The rule should have fired. The root cause of why it did not fire despite meeting the threshold was "unknown at draft time" of the complaint response. This is the critical governance gap: a rule that meets its conditions but doesn't execute, with no explainability mechanism to diagnose why.

---

## Policy Documents

The case includes two policy documents that are themselves governance failures:

**`ai_ethics_framework_DRAFT.md`** (K. Mensah, 2023): Five ethical commitments each followed by a November 2023 status check. Every check is damning — DiagAI in production unvalidated, CareBot involved in two serious incidents, physician sign-off disabled, no demographic fairness assessment, DPO role vacant. The document was "only partially incorporated (without attribution) into the v3 governance policy draft."

**`ai_governance_policy_v3_DRAFT_UNREVIEWED.md`** (K. Mensah, 2023): Explicitly marked DO NOT CIRCULATE; v2 remains operative. Contains six TODOs blocking finalization, including a fundamental conflict: §5.1 prohibits DiagAI v1.4.1-beta in production — but the system is currently running that version. The policy document prohibits the current production state.

---

## Connection to PHAROS Governance Methodology

The Harrowfield case is a worked example for almost every [[PHAROS Invention Disclosure]] governance principle:

- **Consequence binding**: No stage of the CareBot governance architecture bound governance decisions to infrastructure responses — rules could be disabled without alerts, JIRA could fail without notifications
- **Non-exceptionable gates**: There were no gates that could not be bypassed — every control was bypassable through administrative action (rule disable, API expiry, unregistered kiosk)
- **DEFER as first-class state**: No mechanism routed ambiguous cases to safety; the system defaulted to output (provided information, booked appointments) when it should have deferred
- **Monotonic tightening (_tighten())**: No governance mechanism prevented a previously identified risk from being de-escalated without documentation (suicidal ideation rule disabled after being identified as a concern)

---

## Insights

- The 25-day JIRA blind spot (October 27–November 21) is the single most important governance failure: the escalation mechanism itself failed, creating a window in which the system operated with no functioning accountability pathway. This is the clinical version of the [[RECURSO — Final Audit and Ethical Review]] Gap 4.4 finding (identical voting structural flaw) — a system that cannot produce escalation is a system that cannot catch itself being wrong
- The PT-10482 threshold mystery (confidence 0.81 > 0.75, rule should fire, rule doesn't fire, root cause unknown) illustrates precisely why [[Recursive Deterministic AI Governance — Method and Paper]]'s TC-1 Inferential Carry-Through target construct is necessary: systems can produce outputs inconsistent with their own stated logic without any visible signal
- The case is constructed to illustrate that governance failure is not a single event but a cascade of individually small decisions (test-then-forget rule disable; deferred DPO appointment; missed external evaluation) that interact to produce conditions for catastrophic harm

## Open Questions

- Is this a fictional teaching case, an anonymized real case, or a composite? The internal consistency is very high — it reads as constructed
- What is the intended publication/use venue? Healthcare AI governance training? Academic paper? Consulting case study?
- Who is "F. Rahman"? The repeated failures of response to urgent escalation suggest a named senior accountability gap
- Does the case have a formal resolution — was the clinic subject to regulatory action?

## Sources
- `raw sources/ai_ethics_framework_DRAFT.md`
- `raw sources/ai_governance_policy_v3_DRAFT_UNREVIEWED.md`
- `raw sources/carebot_complaint_log_manual.txt`
- `raw sources/carebot_weekly_review_march2023.txt`
- `raw sources/failure_timeline_2023_summary.md`
- `raw sources/governance_review_evidence_summary_feb2024.txt`
- `raw sources/complaint_response_draft_PT10482.md`
- Related: [[Responsible AI Evaluation — Patient Readmission Model]]
- Related: [[Recursive Deterministic AI Governance — Method and Paper]]
- Related: [[PHAROS Invention Disclosure]]
- Related: [[Fluency, Interruption, and Institutional Accountability]]
- Related: [[Governance by Denial]]
- Related: [[Healthcare Governance Packet — Recursive Governance for Providers]]
