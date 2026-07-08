---
type: project-mirror
title: Pharos AI × micro1 — Full Call Posture Script
tags:
- project-mirror
- projects
- micro1
status: active
created: '2026-07-08'
updated: '2026-07-08'
vault_area: projects
canonical_path: projects/micro1/docs/pharos-micro1-call-posture-script.md
backlink_count: 1
backlinks:
- '[[wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06]]'
---

# Pharos AI × micro1 — Full Call Posture Script
## Qualification Call (20–30 minutes)

**Version**: 2026-06-09 (absorbs Danny memos + assessment)  
**Tone**: Calm expert operator, not salesperson. Listen more than you pitch. You are qualifying them as much as they are qualifying you.

### Pre-Call (5 minutes before)
- Have open: this script, the one-pager, the sample JSON schema + examples, the response email you sent.
- Do **not** have the full assessment or internal memos on screen.
- Goal of this call: Confirm they have budget and real interest in governance/professional evaluation data. Get them to name their top 1–2 categories. Leave with clear next step (NDA + sample within 10 days).

### Opening (first 45–60 seconds — you speak first after pleasantries)
"Pharos AI runs a governance evaluation operation. We design and produce adversarial test cases and structured decision traces for AI systems operating in institutional, regulatory, and professional compliance environments.

Our methodology is deterministic — every case follows the same generation, testing, correction, annotation, and claim-boundary protocol. We can produce to spec in any governance or professional domain you point us at.

What I want to understand on this call is which governance or professional domain your current clients have the most coverage gaps in, because that's where we add the most value."

Then stop. Let them talk.

### When They Ask "How much data do you have?" or "What exactly are you licensing?"
**Safe deflection (use almost verbatim until you have the fresh audit number in hand):**

"We're completing a full licensability audit of our operational stores this week. We can share a qualified volume estimate and a structured, redacted sample under NDA within 10 days.

What I can tell you now is that we operate two distinct production pipelines that generate the kind of data you described:

1. Governance workflow evaluation traces — how work gets authorized, escalated, overridden, and closed under explicit institutional and regulatory constraints, with full human rationale and proof packets.

2. Professional domain evaluation traces — in accounting, tax, and legal contexts: messy query to professional intent, source-family routing, claim-boundary enforcement, extraction/validation outcomes, and bad-source rejection rules.

Both are produced through the same deterministic, governed process."

**Do not say:**
- Exact current numbers ("15k", "34k", "7k") until the audit is signed off.
- "We have thousands of fully signed transactions."
- Anything about the recursive Pharos method, Möbius protocol, agent architecture, or internal IP.

### The Questions You Ask Them (ask in roughly this order — listen for the answers)
Use Danny's structured questions (absorbed and slightly tightened):

1. "What specific workflows or AI use cases are your clients currently trying to improve with evaluation or red-teaming data?" (This surfaces their real gaps.)

2. "Which of these categories are highest priority for you right now: governance decision / override traces, adversarial evaluation records, professional-domain extraction and validation traces, or something else?"

3. "What output schemas or field structures do you typically require? Are you looking for fully standardized schemas up front, or can a pilot dataset be delivered with a clear field map that we align on together?"

4. "Who are the downstream users of this data inside your clients' organizations — RLHF / post-training teams, evaluation / red-team groups, or product teams building governed features?"

5. "How do your clients think about field-of-use? Is this data intended strictly for internal evaluation and model improvement, or could it flow into foundation model training more broadly?"

6. "On retention and deletion: once a model has been trained on the data, what are your clients' typical expectations around the supplier's ability to delete or restrict further use? (We're particularly interested in the irreversibility of training.)"

7. "Do you have preferred provenance or signature requirements (cryptographic receipts, reviewer identity, workflow version, etc.)?"

8. "What does a successful pilot look like for you in the first 30–90 days — volume, quality gates, format, integration with your existing pipelines?"

9. "Are there any domains or data types that are explicitly off-limits or lower priority for you right now?"

10. (If the conversation is going well) "Assuming we align on category and format, what would the next step typically look like on your side — NDA, sample review, then pilot scoping?"

### What You Never Say on This Call
- Any description of the core Pharos recursive governance methodology or "how the engine works."
- Patent, IP architecture, or "Möbius" language.
- Specific client names or data volumes from Blackboard/LegiPro without the audit.
- Pricing or "we're thinking $X".
- That you are a one-person shop (frame as "specialized operation with deterministic production pipelines").

### Strong Closing (last 2–3 minutes)
"Thank you — this has been very useful. It sounds like [repeat back the 1–2 categories they named] are the highest priority.

As I mentioned, we're finishing the licensability audit this week. If this is a fit, the fastest path is for us to sign a short NDA and deliver a controlled, redacted sample (with field documentation) within 10 days so you can evaluate the quality and structure directly.

Would that work for you? If yes, I'll send the NDA language and a proposed sample scope right after this call."

Get explicit agreement on next step.

### Post-Call Protocol (do this immediately after hanging up)
1. Send thank-you + confirmation of next step within 30 minutes (use the response email style if you haven't sent it yet).
2. Note in your log: exact categories they named, any schema hints, timeline signals, budget signals, red flags.
3. If they want the sample fast, prepare the controlled package from the cleanest buckets (signals_internal_governance + LegiPro conveyor/extraction examples).
4. Do not send raw data or full volumes before NDA + their explicit category confirmation.

### One-Page Cheat Sheet (print this)
**Opening sentence** (say it):  
"Pharos AI runs a governance evaluation operation. We design and produce adversarial test cases for AI systems operating in institutional, regulatory, and professional compliance environments. Our methodology is deterministic — every case follows the same generation, testing, correction, and annotation protocol. We can produce to spec in any governance domain you point us at."

**When asked about volume**: Use the two-pipeline deflection above.

**Top 3 questions to get them talking**:
1. Which categories are highest priority?
2. What schemas / formats do you need?
3. What does success look like in the first 30–90 days?

**Never say**: methodology details, exact un-audited numbers, IP architecture, one-person framing.

**Desired outcome of this call**: They name 1–2 categories + agree to NDA + sample within 10 days.

**Document owner**: Martin Lepage  
**Last updated**: 2026-06-09 (aligned with Danny v2 + LegiPro integration)
