---
dr_sort_original_filename: "2013 - audit_or_assessment.docx - 2013 - audit_or_assessment.docx.docx - 2013 - audit_or_assessment.docx - 2013 - audit_or_assessment.docx.docx.docx.md"
dr_sort_original_path: "raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable/converted_ocr/Review/Unreadable/2013 - audit_or_assessment.docx - 2013 - audit_or_assessment.docx.docx - 2013 - audit_or_assessment.docx - 2013 - audit_or_assessment.docx.docx.docx.md"
dr_sort_filename_normalized: "2026-05-06"
---
**The Witches’ Road — Switchback Governance Protocol**

*Road Card (2 pages) · v1.0 · Oath: to know, to will, to dare, to be silent*

Purpose: A repeatable route for making legitimacy reconstructable under constraint—without surrendering the seal. Use this when an AI system (or an AI-enabled workflow) must be assessed, approved, paused, repaired, or reported.

**1) Roadhead — Name the work**

* System/capability (plain language) + deployment site (workflow interface).
* Affected parties + consequence domain (choose one primary).
* Decision needed (approve / modify / pause / rollback) + timebox.
* Primary uncertainty (what you do not yet know).

**Gate:** Scope is clamped; stakes are named; the decision is explicit.

**2) Convene — Bind roles and authority**

* Owner (can approve/pause/rollback) · Risk/Compliance (obligations translator) · Ops/Eng (implements) · Witness (reconstructs).
* Name the Scribe function (human, tool-assisted, or shared)—because the audit trail is a governance artifact.
* Agree on escalation thresholds and who holds the stop-switch.

**Gate:** Authority is real, named, and executable (not “consensus vibes”).

**3) First Descent — Map the system as it lives**

* Inventory: what exists (models, prompts, data sources, vendors, dependencies).
* Workflow map: where it touches people + decisions (handoffs, UI, approvals).
* Data lineage: inputs → transformations → outputs → storage/retention.
* Change surface: what can change without a release (prompts, policies, features, data).

**Gate:** A skeptical reader can locate the interfaces where harm/benefit concentrates.

**4) Trial One — Classify and choose proportional controls**

* Classify impact and context (decision criticality, affected populations, data sensitivity, autonomy).
* Select the applicable control set(s) + document why.
* Assign owners and cadence for each control (who checks, how often, what counts).

**Gate:** Controls are chosen and owned; proportionality is stated, not implied.

**5) Trial Two — Evidence and reconstructability**

* Label every claim as evidence, inference, or stance.
* Attach receipts where required (tests, logs, contracts, policies, dataset notes, incident history).
* Create/refresh the decision record: what was considered, what was rejected, and why.

**Gate:** The decision path is reconstructable without trusting the author.

**6) Trial Three — Dare under uncertainty (design response, not bravado)**

* Run a pre-mortem at seam points: drift, data shift, misuse, automation bias, silent failure, handoff confusion, escalation paralysis.
* Define monitoring signals + thresholds (what triggers review, pause, rollback).
* Write the incident playbook (who triages, timelines, comms, remediation, lessons learned).

**Gate:** There is a designed response when the system is wrong—not only detection.

**7) The Seal — Silence as a control**

* Document what is sealed (confidentiality, safety, interior practice, sensitive methods) and why.
* Set access rules (who can see), retention rules (how long), and redaction rules (what appears in public outputs).
* When the institution demands an incompatible proof-regime: offer alternate legitimacy (third-party audit, constrained disclosure, different artifact).

**Gate:** Boundaries are explicit and defensible; silence is procedural, not evasive.

**8) Return — Produce the legitimacy bundle**

* Executive summary (mechanism + scope + decision).
* Control matrix (status, owners, evidence links).
* Risk register deltas + roadmap (next controls, dates).
* Decision record (approve/modify/pause/rollback) + next review date.

**Gate:** Package can be audited, contested, and revised without collapse.

**9) Switchbacks — The honesty mechanism**

|  |  |  |
| --- | --- | --- |
| Trigger | Move | Back to |
| Missing receipts / claim outpaces evidence | Downgrade claim, acquire evidence, or remove sentence. No tone-smuggling. | Trial Two |
| Authority unclear / cannot enforce controls | Reassign owners; make stop-switch real; update RACI. | Convene |
| Signals show unacceptable risk / near misses | Pause/rollback; redesign thresholds and playbook; reclassify if needed. | Trial Three (+ Trial One) |
| Institution demands extraction / ontology betrayal | Reassert seal; offer alternate legitimacy artifact; refuse incompatible proof regime. | The Seal |

**10) Tooling note — Where AI fits (and doesn’t)**

* AI can assist as Scribe (drafting, refactoring, checklisting) and as Legitimacy Simulator (skeptical reader).
* AI does not supply authority, receipts, or consent. The oath remains human-held.
* If using AI: log prompts/inputs that materially shaped decisions where appropriate, and store outputs as evidence artifacts when they inform governance.

## Related

- [[Governance and PHAROS MOC]]
- [[PHAROS Runbook SOP]]
