---
type: project-mirror
title: 'Pharos AI x micro1: Qualification Call Posture v2'
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-06-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/4168-pharos-micro1-qualification-call-posture-v2-trading-names-and-deal-guardrails-2026-06-08.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Pharos AI x micro1: Qualification Call Posture v2

Document ID: 4168  
Danny Stocker | InfraFabric Research | 2026-06-08  
Status: current internal call-prep note  
Supersedes: `/root/docs/4167-pharos-micro1-qualification-call-posture-and-reply-draft-2026-06-08.md`

Companion docs:

- `/root/docs/4164-pharos-micro1-operational-data-licensing-blackboard-iftrace-assessment-2026-06-08.md`
- `/root/docs/4165-pharos-micro1-sample-blackboard-governance-dataset-2026-06-08.jsonl`
- `/root/docs/4166-pharos-micro1-missing-workstreams-entanglement-ip-and-methodology-risk-2026-06-08.md`

## Purpose

This is the tightened call-posture and reply document for the micro1 data-licensing conversation.

It incorporates the latest review:

- Pharos AI and InfraFabric are trading names / product identities of the same company.
- The first reply should use **Pharos AI** only.
- The call posture is **ready to qualify, not ready to close**.
- The first call should establish fit, requirements, and process, not quote final volume or price.
- Additional gaps are addressed: data rights, data room controls, legal/privacy review, field-of-use, sublicensing, retention/deletion, liability, pricing posture, and internal sign-off.

## Trading-name clarification

Pharos AI and InfraFabric are **trading names / product identities of the same company**, not two separate companies.

Practical external rule:

- Use **Pharos AI** in the first email because it is the cleaner outward-facing sender identity.
- Do not sign the first email as `Pharos AI / InfraFabric`.
- Describe the asset category without over-explaining the internal product map.
- Introduce **InfraFabric** later, ideally under NDA, as the infrastructure / evidence-workflow identity if it becomes relevant.
- Treat the issue as internal product-boundary discipline, not joint-party negotiation.

## Key posture

The right posture is:

> **ready to qualify, not ready to close**

That means:

- a call this week is reasonable,
- over-claiming volume or negotiability is not,
- the call should be framed as discovery and qualification,
- the company should buy itself time to complete the licensability audit and data-pack preparation properly.

## Core positioning sentence

Use this sentence on the call and in follow-up materials:

> We operate structured AI governance and evidence workflows that generate append-only task records, checkpoints, escalation signals, proof packets, claim-boundary records, and signed operational traces. The data is valuable because it captures how work is authorized, how exceptions are escalated, how review closes the loop, and what can be safely claimed at the end.

This is specific, valuable, and does not reveal the crown-jewel methodology.

## What the first call is for

The first call is **not** for:

- quoting final licensable volume,
- naming a price,
- discussing exclusivity,
- sending raw samples,
- promising all blackboard events are available,
- explaining the internal methodology.

The first call **is** for:

1. learning which data categories micro1 is prioritizing,
2. understanding their minimum schema and volume requirements,
3. testing whether governance / evaluation / override data is actually in budget,
4. understanding field-of-use, sublicensing, retention, and model-training expectations,
5. setting up NDA plus a structured redacted sample if there is a fit.

## What to say when they ask for volume too early

If they ask:

> How much data do you have?

do **not** answer with the gross raw total.

Use:

> We're completing a licensability audit now, so I don't want to give you an inflated gross number that won't survive diligence. What I can say today is that the event volume is substantial, the data already carries cryptographic provenance on a meaningful subset, and the governance/evaluation category is specifically where we believe there may be a fit. We can share a qualified estimate and a structured redacted sample under NDA within about 10 days if the category matches what you're buying.

This answer is disciplined. It keeps the door open without creating a diligence problem later.

## What to say when they ask what kind of data this is

Use:

> This is not generic chat data. The most interesting part is structured governance workflow data: task progression, checkpoints, escalation and response flows, proof-packet formation, claim-boundary behavior, and signed provenance around those operations.

## What to say when they ask whether it can be anonymized

Use:

> Yes, in principle, but we are treating that as a formal workstream rather than an assumption. Some slices are internal-only and likely straightforward. Others are likely to require redaction or to be excluded entirely. We are classifying the candidate pool before making any broad availability claims.

## What to say when they ask whether you can send a sample immediately

Use:

> We can send a sample, but only under NDA and after a quick redaction and exclusion pass. We'd rather send you a clean representative sample than a fast but sloppy one.

If they press for something pre-NDA, offer a **schema-level field map** or a synthetic/redacted specimen, not raw data.

## Structured questions for micro1

Ask these in order if the conversation allows it:

1. Which data category are you prioritizing right now?
   - annotation / labeling
   - evaluation / red-team
   - governance / override
   - expert reasoning

2. Are you currently buying operational workflow datasets with human escalation and review signals?

3. What minimum volume and schema maturity are you looking for?

4. Are you looking for one-time acquisition, recurring refresh, or a pilot-to-license path?

5. Is non-exclusive licensing acceptable?

6. What fields are essential to utility versus optional?

7. Do you require fully standardized schemas up front, or can a pilot dataset be delivered with a structured field map?

8. Who are the downstream users of the data: micro1 internal teams, named AI labs, or undisclosed third parties?

9. What field-of-use do you need: evaluation only, supervised fine-tuning, RLHF, general model training, or benchmark construction?

10. What retention, deletion, and audit-rights terms are standard in your program?

## Additional gaps the latest review still missed

The latest external/internal review converged on the call posture. These remaining items still need explicit handling before sample delivery or commercial negotiation.

### 1. Downstream use and sublicensing

micro1 may be a broker/intermediary. The company needs to know whether data will be used by:

- micro1 only,
- named model-lab customers,
- unnamed downstream customers,
- subcontractors,
- future customers not yet identified.

Default position:

- no open-ended onward transfer,
- no undisclosed resale,
- named or category-bounded downstream use,
- no exclusivity on the first pilot.

### 2. Field-of-use limits

Evaluation data and general model-training data are not the same risk.

The agreement should distinguish:

- evaluation / benchmarking,
- red-team training,
- RLHF / preference data,
- supervised fine-tuning,
- general foundation-model training,
- synthetic-data generation from the licensed data.

The broader the field of use, the higher the price and the stronger the controls required.

### 3. Model-training irreversibility

Deletion after model training is not like deleting a file.

Before licensing any real dataset, ask:

- what happens after training,
- whether model weights trained on the data are considered derivatives,
- whether deletion requests are technically meaningful,
- whether outputs can be audited or constrained,
- whether the data may be used to generate synthetic successor datasets.

This should be treated as a negotiation point, not a footnote.

### 4. Data-rights authority

Confirm the company has the right to license each selected event family, not merely physical access to the logs.

This check should cover:

- internal work,
- customer-derived work,
- contractor or agent-generated work,
- third-party source material embedded in events,
- confidential prompts or client facts,
- public-source excerpts embedded in artifacts.

### 5. Data-room and sample controls

Do not send raw samples casually.

Preferred sample sequence:

1. pre-NDA: synthetic or heavily redacted specimen plus field map,
2. NDA: small controlled sample,
3. post-fit: larger audited sample in a restricted data room,
4. pilot: scoped delivery with watermarking and manifest.

Controls to consider:

- per-recipient watermark,
- row IDs logged in a disclosure manifest,
- canary rows,
- access expiry,
- no bulk download until agreement terms are clear.

### 6. Privacy, confidentiality, and trade-secret review

The licensability audit should include:

- PII scan,
- client confidentiality scan,
- path / host / username stripping,
- trade-secret leakage review,
- methodology reconstruction review,
- field-minimization pass,
- re-identification risk check.

This is more than anonymization. It is licensability review.

### 7. Liability and indemnity boundaries

Before price discussion, establish whether micro1 expects:

- representations and warranties about data ownership,
- indemnity for downstream use,
- security obligations,
- audit rights,
- privacy compliance commitments.

Default position:

- narrow warranties,
- no broad indemnity for downstream model behavior,
- no responsibility for model outputs trained by third parties,
- liability cap tied to fees paid.

Legal counsel should review this before any binding term sheet.

### 8. Pricing posture

Do not quote price on the first call.

Ask first:

- data category,
- field of use,
- exclusivity,
- volume,
- refresh cadence,
- downstream access,
- required warranties,
- whether this is a pilot or production license.

Price depends on those answers.

### 9. Internal sign-off owner

Before any sample leaves the company, name who can approve:

- sample release,
- data family inclusion,
- use of the InfraFabric name,
- use of current blackboard counts,
- use of `if.trace` counts,
- exclusivity discussion,
- commercial terms.

### 10. Evidence freshness

Refresh `if.trace` current counts before numeric use.

Until then, keep this sentence:

> `if.trace` is a shipped public receipt layer with historically verified signed coverage.

Do not say:

> thousands of fully signed `if.trace` transactions

unless it is freshly verified.

## Internal no-go lines for the first call

Do not:

- explain the crown-jewel methodology in detail,
- quote gross blackboard totals as licensable totals,
- quote current `if.trace` volume before re-verification,
- promise exclusivity,
- send raw customer-derived examples,
- improvise a price,
- accept open-ended onward transfer,
- agree to general model-training use without understanding price and risk,
- imply that anonymization alone removes trade-secret reconstruction risk.

## Send-ready reply to micro1

Subject: Re: Potential fit for operational data licensing

Hi [Name],

Thank you for reaching out. Based on what you've described, there may be a real fit.

We operate structured AI governance and evidence workflows that generate append-only task records, checkpoints, escalation signals, proof packets, claim-boundary records, and signed operational traces. The data is valuable because it captures how work is authorized, how exceptions are escalated, how review closes the loop, and what can be safely claimed at the end.

The most relevant category on our side is not generic annotation data, but workflow data tied to evaluation, review, escalation, and bounded decision-making.

I'd be open to a short qualification call to better understand which data categories your team is prioritizing right now, what minimum structure or volume you typically require, and whether governance/evaluation datasets are in scope for your current program.

We are also completing an internal licensability audit, so I would prefer to treat an initial conversation as a fit and requirements discussion first. If there is alignment, the next step could be NDA followed by a structured redacted sample and a qualified estimate.

What availability do you have later this week or early next week?

Best,  
Martin Lepage  
Founder  
Pharos AI

## Shorter reply

Subject: Re: Potential fit for operational data licensing

Hi [Name],

Thank you. There may be a fit.

We generate structured operational workflow data around AI evaluation, review, escalation, and evidence formation, which sounds closer to your description than standard annotation work.

I'd be happy to take a short qualification call to understand what categories and minimum data requirements you're prioritizing. If there is alignment, the next step on our side would likely be NDA plus a structured redacted sample.

What times work for you this week or next?

Best,  
Martin Lepage

## Suggested internal sequence

1. Finalize the internal product-boundary memo.
2. Run the fast licensability audit.
3. Refresh `if.trace` current counts if it will be mentioned numerically.
4. Send the reply.
5. Treat the first call as qualification only.
6. After the call, decide whether to prepare an NDA sample pack, a field map, or a formal pilot proposal.

## Bottom line

The strongest posture is calm and precise:

- Pharos AI and InfraFabric are trading names / product identities of the same company.
- First-touch communication should use Pharos AI.
- The data category is governance/evaluation workflow data, not generic chat logs.
- The company is ready to qualify interest.
- It is not ready to quote final licensable volume, price, or exclusivity.

This is a good opportunity, but the value comes from being disciplined before the call, not from sounding bigger than the evidence.
