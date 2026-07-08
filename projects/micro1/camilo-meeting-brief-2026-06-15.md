---
type: project-mirror
title: Camilo Meeting Brief
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-06-15'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/camilo-meeting-brief-2026-06-15.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Camilo Meeting Brief
## micro1 qualification call

**Date**: 2026-06-15  
**Counterparty**: Camilo / micro1  
**Objective**: qualify whether micro1 has real demand for Pharos's governance and professional-domain data pipelines, and leave with a controlled next step.

## What this meeting is actually for

This is **not** the meeting to:

- quote final volume,
- negotiate price,
- discuss exclusivity,
- explain the Pharos methodology,
- promise raw dataset access.

This **is** the meeting to:

- learn which data category micro1 actually wants,
- learn the field of use and downstream customer structure,
- establish whether they are serious enough for NDA + controlled sample,
- frame Pharos as a governed data-production operation, not a one-off archive.

## Best reading of Camilo's role

Based on recent micro1 outreach language, Camilo appears to be on the workflow-data sourcing / partnerships side rather than deep technical evaluation. That means he is likely screening for:

- category fit,
- exportability,
- rights posture,
- sample readiness,
- operational credibility,
- low-friction path to a pilot.

Assume he is trying to sort suppliers quickly.

## What is strong in the current package

- Clear two-product-line story: governance evaluation data and professional-domain evaluation data.
- Strong posture against IP leakage and raw-data disclosure.
- Good pilot structure: NDA -> controlled sample -> paid 30-day pilot.
- Good language for deterministic production, claim-boundary enforcement, and expert rationale.
- Good question set for qualifying micro1's real needs.

## What is weak or unsafe in the current package

- Several external-facing docs include exact counts even though the internal posture says not to quote final numbers yet.
- The sample JSON is good as a specimen, but it is not proof of final licensable production volume by itself.
- The folder is built around Daniel Warner's outreach; your live counterpart is Camilo, so you should treat this as a fresh qualification screen.
- The internal memo explicitly says joint deal hygiene / rights authority still needs tightening; do not talk as if every data family is already cleared for licensing.

## The core story to tell

Use this shape:

"Pharos runs deterministic, governance-constrained data-production pipelines. We generate structured traces showing how decisions are authorized, escalated, corrected, and bounded in high-stakes domains. We also generate professional-domain evaluation traces in accounting, tax, and legal workflows. We are not selling raw corpora or raw client data. We are selling controlled outputs of expert workflows, and we want to understand which categories are most useful to your clients before we scope a sample or pilot."

## Safe opening

"Thanks for taking the time. The useful question for us is not just whether micro1 buys workflow data in general, but which categories are actually live priorities for your clients right now.

We operate two governed data-production lanes: one around governance and adversarial evaluation traces, and one around professional-domain retrieval, extraction, and claim-boundary enforcement in accounting/legal contexts.

What I'd like to understand first is where you currently have the biggest coverage gaps and what a successful pilot would need to look like on your side."

Then stop and let him talk.

## What you can credibly claim

- You have a real structured data story in two categories.
- You have a deterministic workflow and field-level schema story.
- You can provide a controlled redacted sample under NDA.
- You can scope a paid pilot around one or two agreed categories.
- You can discuss provenance, QA, claim-boundary enforcement, and schema alignment.

## What you should not claim

- Exact licensable volumes are final.
- The whole Blackboard store is ready for sale.
- micro1 can have broad/open-ended downstream rights.
- deletion after training is simple or meaningful.
- exclusivity is available.
- the current materials prove production-scale delivery without further scoping.

## What you need to learn from Camilo

Ask these in substance, even if you vary the wording:

1. Which category is actually highest priority right now: governance overrides, adversarial evaluation traces, or professional-domain extraction/routing traces?
2. Who uses the data downstream: micro1 internal teams, named labs, or unnamed future customers?
3. What field of use are they targeting: evaluation, red-teaming, RLHF, SFT, broader model training?
4. What schema and provenance requirements matter most in a first sample?
5. What would make a pilot successful in the first 30 days?
6. What sample size is enough for them to decide whether to proceed?
7. Are there domains or data types they will not touch?
8. How do they handle retention, deletion, and synthetic-derivative use once data enters training workflows?

## Likely pressure points and how to handle them

### If he asks "How much data do you have?"

"We have completed a first-pass internal audit on the cleanest candidate slices and it is clear that a meaningful recoverable pool exists. We are not treating gross internal counts as final licensable volume yet. The right next step is to align on category, then we can share a qualified estimate and controlled sample under NDA."

### If he asks for exact numbers immediately

"I do not want to give you false precision before the licensability and redaction pass is complete. We can give you a qualified estimate tied to the exact category you care about once we know the use case."

### If he asks for a sample before NDA

"Pre-NDA we can share schema, field map, and redacted specimen material. For anything that reflects real workflow structure in a useful way, we would want NDA first."

### If he asks whether this can train foundation models broadly

"That depends on field of use, downstream access, and rights posture. We should separate evaluation use from broader training use because the pricing and controls are different."

### If he asks about price

"I would rather not invent a number before we know the category, field of use, sample expectations, and whether this is a pilot or broader production relationship."

## The real leverage

Your leverage is not raw volume.

Your leverage is:

- rare high-stakes domain specificity,
- explicit claim-boundary enforcement,
- structured human correction + rationale,
- governance traces that show why a model was overruled,
- ability to scope a paid pilot instead of debating a speculative archive sale.

## The real risks

- Saying exact numbers that the internal materials themselves tell you not to say yet.
- Letting micro1 frame this as commodity workflow exhaust.
- Agreeing in principle to broad downstream training use.
- Revealing too much of the operating method through examples or vocabulary.
- Sliding into price talk before scope, field of use, or downstream rights are clear.

## Best meeting outcome

The best outcome is:

- Camilo names the top 1-2 categories they care about,
- confirms the likely field of use,
- agrees to NDA,
- agrees on a small controlled sample,
- gives you the criteria for a successful 30-day pilot.

Anything beyond that is a bonus.

## Bad meeting outcome

The bad outcome is:

- you quote unaudited numbers,
- you imply broad rights are available,
- you explain the method in detail,
- you talk price first,
- you leave with no concrete next step.

## Close the call this way

"This is helpful. Based on what you've said, it sounds like [repeat their top category or two] are the right starting point. The fastest path on our side would be NDA, then a controlled redacted sample with field documentation so you can evaluate structure and quality directly. If that looks right, we can scope a paid 30-day pilot around the exact category and schema you need."

## Immediate post-call actions

Within 30 minutes, send:

- a thank-you note,
- the categories they named,
- the next step you agreed,
- the timeline for NDA and sample.

Also log:

- downstream user structure,
- field of use,
- sample size request,
- any price signals,
- any exclusivity or retention red flags.
