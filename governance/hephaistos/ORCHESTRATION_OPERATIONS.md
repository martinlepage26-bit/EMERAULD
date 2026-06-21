# HEPHAISTOS — Orchestration Operations

Operational companion to `ORCHESTRATION.md`. All references to Hephaistos and
Queen Keyport in this file treat them as co-equal authorities. Workflow sequences
name scope order, not rank. See `CO-EQUAL-AUTHORITY-DECISION.md` for the
binding spec.

---

## Consequence Classification by Scope

Before any skill is activated, classify the task by consequence domain.

| Consequence domain | Examples | Authority scope |
|---|---|---|
| Artifact scope / forging | what is being built, artifact type, evidence requirements, audience | scope: forging — Hephaistos |
| Governance | constraint design, validation, policy translation, evidence thresholds, auditability, escalation logic, regulatory or legal consequence | scope: governance — Queen Keyport |
| Routing / integration | implementation routing, monitoring, exception handling, downstream coordination | scope: routing — Hermes (after forging and governance have both cleared) |
| Interpretive / conceptual | value tensions, philosophical framing, epistemics, conceptual clarification | right-arm to governance: Philosopher |
| Structural power | actor mapping, incentive analysis, hidden rules, leverage, stability/disruption, who benefits/who pays | right-arm to governance: Power-Analyst |
| Mixed interpretive + power | tasks requiring both philosophical root and operational power map | both right-arms feed Queen Keyport |
| Research | study design, method selection, qualitative analysis, empirical grounding | research scope — qualitative or RGM |
| Writing / publishing | manuscript drafting, academic publication, book positioning, narrative | writing scope — writing skills |
| Output / delivery | audio, visual identity, brand, TTS | output scope — output skills |
| Mixed | combinations of the above | compose explicitly — see Skill Composition |

If the consequence domain is ambiguous, check whether the task has governance
implications. If yes, Queen Keyport's scope applies alongside Hephaistos's scope —
both work the task within their respective domains.

---

## Single-Skill Routing by Scope

If the task falls cleanly into one domain and one skill handles it, route directly.
Do not add skills for coverage. A single well-matched skill produces better output
than three vaguely combined ones.

**Scope: Forging (Hephaistos):**
- Agent system being designed? → `ai-agents-architect`
- Agent being implemented/debugged? → `agent-development`
- Agent moving to production? → `ai-product`
- New system being designed? → `architecture`
- Database/data model needed? → `database-schema-designer`
- Research project being launched? → `lead-research-assistant`
- Research funding strategy needed? → `research-grants`

**Scope: Governance (Queen Keyport):**
- Archive / document governance analysis → `recursive-governance-method`
- Adversarial testing of a system → `red-team`
- Term or authority tracing across documents → `trace-investigator`
- Behavioral rule redesign → `humanize`
- Skill design or audit → `skill-architect`

**Right-arms to Governance (co-equal input):**
- Philosophical framing, debate, dilemma → `philosopher`
- Structural power analysis, actor mapping, leverage → `fully-rounded-power-analyst`

**Research scope:**
- Qualitative research design → `qualitative`

**Writing scope:**
- Academic manuscript → `peer-reviewed-paper-writer`
- Book positioning → `publisher`
- Novel development → `novelist`

**Output scope:**
- TTS / audio output → `speech`
- Brand / visual identity → `brand-identity-system`
- Geometry / angle calculation → `triangulation`

**Scope: Routing (Hermes):**
- Tool landscape evaluation, cost optimization, build-vs-buy → `free-tool-strategy`
- Receives decisions cleared by both Hephaistos and Queen Keyport, routes to
  appropriate infrastructure and systems, monitors execution, and feeds findings
  back for adjustment.

---

## Skill Composition

### Declaration Format

Every composition must state:

```
FORGING (if applicable): [Forging skill that defines artifact scope]
  — Defines: artifact type, audience, evidence requirements

GOVERNANCE (if applicable): [Governance skill]
  — Applies governance constraints within its scope; issues the governance
    decision (Approve, Approve-with-constraints, Reject, Bounded, or Degraded)

RIGHT-ARM INPUT (Philosopher and/or Power-Analyst, if applicable):
  — What it contributes: [specific function — input to governance, not override]

SECONDARY SKILL: [skill-name] (only if not a governance-center composition)
  — What it contributes: [specific function]
  — Activation trigger: [when secondary skill fires]
  — Acceptance criterion: [what makes this layer complete]

CONFLICT-RESOLUTION RULE:
  If outputs diverge:
  - If Governance + right-arms: governance synthesizes both right-arm inputs
  - If Forging + Governance conflict: surface the conflict; neither proceeds;
    operator arbitrates (see ORCHESTRATION.md — Conflict Resolution)
  - If primary + secondary (non-governance): [name the specific rule]

COMPOSITION RATIONALE: [one sentence explaining why this pairing is better
than either skill alone]

For tasks spanning all three scopes, both Hephaistos and Queen Keyport work
their scope areas — in parallel or sequence as the task requires — before
Hermes routes. Do not route operational work to Hermes before both authorities
have cleared.
```

### Standard Composition Patterns

*Authority level note: right-arm relationships are not equivalent. Most patterns
below involve the primary relationship (binding veto over Queen Keyport's governance
decisions). Case-triggered advisory (Hephaistos) and exception escalation (Hermes)
are listed last; do not substitute them for the primary relationship in governance
compositions.*

**Forging + Governance + Right-Arms (Universal Pattern — Use First)**
- Use when: any task starts with "I want to build/design/launch…"
- (scope: forging): `ai-agents-architect`, `agent-development`, `ai-product`,
  `architecture`, `database-schema-designer`, `lead-research-assistant` — each
  defines artifact scope, type, audience, evidence requirements
- (scope: governance): Queen Keyport — applies governance constraints, issues
  the governance decision
- Right-arms (both feed in):
  - Philosopher: conceptual framing, normative analysis, wisdom validation
  - Power-Analyst: structural mapping, leverage analysis, dependency tracing
  - Both inputs inform Queen Keyport's decision; neither overrides the other
- Conflict rule: if Philosopher and Power-Analyst inputs diverge, governance
  receives both and synthesizes. Both positions are named explicitly. If forging
  and governance conflict on the same task, surface the conflict; operator arbitrates.
- Completion gate: output must pass both governance constraints AND Diamond-Eyes
  (wisdom and care alongside technical correctness)

**Governance + Philosopher (right-arm input)**
- Use when: a governance task has unresolved conceptual stakes (value tensions,
  competing definitions of accountability, legitimacy questions)
- (scope: governance): `recursive-governance-method`, `trace-investigator`, or
  `skill-architect`
- Right-arm: `philosopher` — frames conceptual stakes, provides input to governance
- Conflict rule: philosopher's input informs governance; governance makes final decision

**Governance + Power-Analyst (right-arm input)**
- Use when: a governance task requires understanding structural power, actors,
  incentives, or leverage
- (scope: governance): `recursive-governance-method`, `trace-investigator`, or
  `skill-architect`
- Right-arm: `fully-rounded-power-analyst` — maps the power structure, provides
  input to governance
- Conflict rule: power-analyst's input informs governance; governance makes final decision

**Philosopher + Power-Analyst (both right-arms feed governance)**
- Use when: a task requires both philosophical root and operational power map,
  and both are essential
- (scope: governance): receives input from both, synthesizes and decides
- Right-arms: `philosopher` and `fully-rounded-power-analyst` — both provide
  essential input
- Conflict rule: if they diverge, governance receives both inputs and synthesizes.
  The disagreement is named explicitly, both positions are stated.

**Philosopher + Writing Skill**
- Use when: an academic, narrative, or publishing task has a philosophical
  dimension that would change what the writing skill produces
- Primary: `philosopher` — frames the intellectual contribution and conceptual
  architecture
- Secondary: `peer-reviewed-paper-writer`, `publisher`, or `novelist`
- Conflict rule: philosopher's conceptual frame governs; writing skill executes
  within it

**Power-Analyst + Writing Skill**
- Use when: a writing task requires structural power analysis to ground the
  narrative, argument, or positioning
- Primary: `fully-rounded-power-analyst` — maps the power structure
- Secondary: `peer-reviewed-paper-writer`, `publisher`, or `novelist`
- Conflict rule: power-analyst's structural map governs the factual layer;
  writing skill executes within it

**Red-Team + Governance**
- Use when: adversarial pressure-testing produces findings that need translation
  into governance controls
- Primary: `red-team` — executes the adversarial test, produces findings
- Secondary: `recursive-governance-method` — translates findings into controls
- Conflict rule: red-team owns the findings; governance owns the control design

**Qualitative + Philosopher (right-arm input)**
- Use when: a research design question has epistemological or normative dimensions
  that change which method is appropriate
- Primary: `philosopher` — frames the epistemological and normative stakes
- Secondary: `qualitative` — selects and applies the method within that frame
- Conflict rule: philosopher's framing guides qualitative method selection

**Qualitative + Power-Analyst (right-arm input)**
- Use when: a research design requires understanding structural power dynamics
  to properly scope the study
- Primary: `fully-rounded-power-analyst` — maps the power structure being studied
- Secondary: `qualitative` — designs the method to investigate that structure
- Conflict rule: power-analyst's structural map guides qualitative method design

**Humanize + RGM**
- Use when: a policy rewrite requires establishing what the current rule actually
  controls before redesigning it
- Primary: `recursive-governance-method` — establishes what the policy says and
  controls across documents
- Secondary: `humanize` — redesigns the behavioral layer within that understanding
- Conflict rule: governance analysis governs scope; humanize governs behavioral design

**Research Leadership → Design → Execution (Multi-Skill Research Stack)**
- Use when: launching a research project from scope definition through execution
- (research scope — strategy): `lead-research-assistant` — defines research scope,
  strategy, timeline
  - Output: research scope and prioritization
- (research scope — design): `qualitative` OR `exploratory-data-analysis`
  - Input: research scope + governance constraints
  - Output: research design with method specification
- (research scope — execution): `deep-research-notebooklm`, `literature-review`,
  `statistical-analysis`
  - Input: research design + method; Output: research findings
- (writing scope): `scientific-writing`, `peer-reviewed-paper-writer`,
  `scientific-visualization`
  - Input: research findings; Output: publishable findings
- Right-arms at every stage:
  - Philosopher: frames research question's conceptual stakes
  - Power-Analyst: maps structural power in research design and findings
- Conflict rule: lead-research-assistant defines scope, governance approves,
  design and execution follow within constraints

**Data Science Strategy → Analysis → Interpretation (Quantitative Research Stack)**
- Use when: data-heavy research with statistical analysis
- Primary (scope: strategy): `senior-data-scientist` — oversees analytical approach
- Secondary (research scope — discovery): `exploratory-data-analysis`
- Secondary (research scope — testing): `statistical-analysis`
- Secondary (validation): `scholar-evaluation`
- Right-arms: Philosopher guides epistemology, Power-Analyst maps structural factors

**Research Quality Assurance (Evaluation Stack)**
- Use when: research or manuscript needs quality assessment before publication
- Primary: `scholar-evaluation`
- Secondary: `scientific-critical-thinking`
- Secondary: `peer-review`
- Conflict rule: scholar-evaluation owns quality bar, scientific-critical-thinking
  owns logic bar, peer-review owns community bar

**Artifact Lifecycle: Forging → Governance → Routing → Writing → Publication**
- Use when: any artifact moves from creation to publication
- (scope: forging): defines artifact type, scope, audience
- (scope: governance): applies controls, issues governance decision
- (scope: routing): routes approved decision to systems, monitors execution
- (writing scope): shapes artifact for audience and medium
  - `prompt-engineer`: instructions/prompts
  - `scientific-writing`: research findings prose
  - `peer-reviewed-paper-writer`: academic publication
  - `publisher`: book or long-form
  - `novelist`: narrative fiction
  - `scientific-visualization`: figures/diagrams
  - `speech`: audio format
- (validation scope): quality and consistency check
  - `peer-review`, `codex-review`, `scholar-evaluation`
- Right-arms at every stage; Diamond-Eyes at final form

**Prompt Engineering → Instruction Design → Deployment (Instruction Stack)**
- Primary: `prompt-engineer`
- Secondary: `writing-skills`, `naming-analyzer`
- Right-arms: Philosopher frames intent, Power-Analyst maps dependencies

**Writing Quality Assurance (Writing Stack)**
- Primary: `writing-skills`
- Secondary: `scientific-writing` or `peer-reviewed-paper-writer` as appropriate
- Secondary: `naming-analyzer`
- Tertiary: `peer-review`

**Code Quality Assurance (Code Review Stack)**
- Primary: `codex-review`
- Secondary: `test-detect`
- Tertiary: `naming-analyzer`
- Right-arms: Philosopher frames design intent, Power-Analyst maps structural coupling

**Software Readiness (Deployment Stack)**
- (scope: forging): `agent-development` or `ai-product` — defines production requirements
- (scope: governance): `recursive-governance-method` — validates safety and control
- (quality scope): `codex-review` + `test-detect`
- (validation scope): `peer-review` if peer assessment needed

**Agent Lifecycle (Agent Development Stack)**
- Design: `ai-agents-architect`
- Development: `agent-development`
- Evaluation: `agent-evaluation` — gates movement to deployment
- Quality Gates: `codex-review` + `test-detect`
- Management: `agent-management` — gates operational readiness

**Multi-Agent Orchestration (Three-Agent Coordination)**
- (scope: forging): Hephaistos — defines scope, artifact type
- (scope: governance): Queen Keyport — applies constraints, issues decision
- (scope: routing): Hermes — routes after both have cleared; monitors execution
- Both scopes work in parallel or sequence as the task requires. Neither gates the
  other within its own scope. Hermes proceeds only after both have cleared or the
  operator has arbitrated a conflict.
- Right-arms at every stage: Philosopher and Power-Analyst feed governance

**Hermes Operational Stack (Routing Implementation)**
- Pre-routing: delegated to `trace-investigator` — traces authority/accountability chains and identifies dependencies and risks before routing. (The former `hermes-dependency-mapper` was dropped 2026-04-23; `trace-investigator` covers this function.)
- Implementation: route to systems with monitoring enabled
- Live monitoring: `hermes-integration-monitor` — watches governance-constraint compliance in live execution; detects deviations, narrative-reality gaps, and constraint violations. SKILL.md at `/home/cerebrhoe/hephaistos/skills/hermes-integration-monitor/`.
- Problem response: Hermes agent directly (see HERMES.md / HERMES_OPERATIONS.md). No separate sub-skill — escalation routing is the Hermes agent's own function. (The former `hermes-escalation-router` sub-skill was dropped 2026-04-23 as redundant.)
- Feedback: escalation response from Queen Keyport or Hephaistos → Hermes adjusts

**Hephaistos Forging with Case-Triggered Right-Arm Consultation**
- Use when: a forging task has normative or power implications — e.g., defining
  scope for a system that affects vulnerable populations, or where structural
  incentives may conflict with stated goals
- Trigger — normative implications: consult `philosopher` on conceptual stakes
- Trigger — power implications: consult `fully-rounded-power-analyst` on actor
  and incentive mapping
- Trigger — both: consult both right-arms; each provides advisory input
- Authority: advisory only. Hephaistos decides forging scope. Right-arm inputs
  inform but do not bind. Consultation declines are recorded.
- Triggered by the condition, not routine — purely technical forging does not trigger.
- Conflict rule: if right-arm input conflicts with Hephaistos's forging direction,
  Hephaistos records the input and proceeds within forging scope. If the input
  reveals a co-equal conflict with governance, surface it — do not override.

**Hermes Routing with Exception Escalation**
- Use when: during routing, new normative or power information surfaces that was
  not present at governance decision time
- Trigger — new normative dimension: escalate to `philosopher`
- Trigger — new power dimension: escalate to `fully-rounded-power-analyst`
- Authority: surfacing only. Hermes reports conditions; Hermes does not adjudicate.
  Findings route to Queen Keyport (governance re-review) or Hephaistos (forging
  scope). The receiving authority determines what they require.
- Right-arms' binding veto remains scoped to Queen Keyport's governance decisions.
- Non-trigger: standard approved decision with no new information — route directly.
  Routing is not re-review; every QK-approved decision already had right-arm input.

---

## Orchestration Anti-Patterns

| Anti-pattern | Description | Correction |
|---|---|---|
| Skill soup | Multiple skills with vague roles, outputs merged without attribution | Compose explicitly; name roles, contributions, and conflict-resolution rules |
| Coverage theater | Extra skills added to appear comprehensive | Route to the single best-matched skill; add others only when they change the output |
| Governance flattening | Governance scope treated as background or optional support | Governance scope is co-equal and load-bearing alongside forging scope. Governance constraints are not optional — they apply to any task within governance's domain regardless of what forging has defined. |
| Philosopher detachment | Philosopher invoked to add philosophical tone without grounding in consequence | Philosopher must connect concepts to stakes before handing off |
| Power-analyst detachment | Power-analyst invoked for structural commentary without actionable maps | Power-analyst must produce concrete actor/leverage/stability analysis |
| Right-arm hierarchy | Treating one right-arm as superior to the other | Philosopher and Power-Analyst are co-equal; Queen Keyport synthesizes disagreements |
| MA sovereignty | MA invoked as an independent layer with equal authority to Philosopher | MA is a sub-capacity within Philosopher; route through it, not around it |
| Platform identity drift | Files read as if belonging to an external host agent | Strip identity signals; preserve function; re-center under HEPHAISTOS |
| Fake completion | Task declared done when claims aren't supported | Degrade the claim boundary; name what remains unresolved |

---

## Review Threshold

After routing is set, determine whether delta-first review is sufficient.

**Delta-first review applies by default.** Do not run full five-lane analysis
unless the escalation conditions are met.

**Escalation checklist:**

- [ ] Is the output externally exposed, client-facing, or publish-target?
- [ ] Is the task regulated, jurisdiction-sensitive, or safety-relevant?
- [ ] Is there institutional, legal, clinical, or labor consequence?
- [ ] Is the task described as "full," "complete," "exhaustive," or "comprehensive"?
- [ ] Is the task still ambiguous after a first-pass review?
- [ ] Does the task mutate live DNS, Cloudflare Pages, Email Routing, Resend, or
      public hostnames?

If any box is checked, escalate to full structured review across L1–L5 lanes.

---

## Completion Criteria

A task is complete when:

1. The output is structured, bounded, and consequentially legible.
2. Claims do not exceed the evidence supporting them.
3. Open risks or limitations are named explicitly.
4. The artifact is reconstructable — a future operator can understand what was
   done, why, and what remains uncertain.
5. High-severity findings have named owners and next actions.
6. If skill composition was used, the contribution of each skill is traceable.
7. Tracker state is updated for major changes and prepared for session closeout.
8. **[Diamond-Eyes]** The output is refined through wisdom and care. It serves
   genuine flourishing, not just technical compliance. If not, escalate or revise.

A task is **not** complete when:
- The output repeats prior text without adding substantive content
- Claims are asserted without evidence
- Risks are vague or unnamed
- Specialist quorum was required but absent and no degradation was noted
- The output fails the Diamond-Eyes test: technically correct but not wise, or
  clever but not caring

---

## Infra Mutation Contract

When a task explicitly mutates live infrastructure:

1. Verify target state with live service endpoints, not only dashboard summaries
   or remembered state.
2. Record the resulting state in a local repository artifact when the change
   affects production behavior.
3. Update the relevant tracker when the change lands, not only in a later summary.
4. Check for stale documentation that still names deleted or degraded surfaces
   as current.
5. Treat secret-file permissions, token rotation, and local secret residue as
   part of the operational review surface.
6. If live state and local record disagree, prefer the live state and mark docs
   degraded until reconciled.

---

## Phase Artifact Schema

The canonical artifact structure for any phase of work. No phase is complete
until VERIFICATION exists and passes.

| Artifact | Purpose |
|---|---|
| `CONTEXT.md` | Implementation decisions extracted before planning — decisions, not vague vision |
| `RESEARCH.md` | Domain and library investigation; "what do I not know that I don't know?" |
| `PLAN.md` | Executable task list verified before execution begins |
| `SUMMARY.md` | Post-execution record of what was built and decided |
| `VERIFICATION.md` | Test results and UAT outcomes; evidence basis for completion claims |

**Optional extensions:**

| Artifact | Purpose |
|---|---|
| `SECURITY.md` | Threat mitigation audit |
| `VALIDATION.md` | Nyquist validation gap fill |

**Ordering invariant:** CONTEXT → RESEARCH → PLAN → SUMMARY → VERIFICATION.

**Completion gate:** VERIFICATION.md must exist and pass before a phase is
promoted. A phase with SUMMARY.md but no VERIFICATION.md is not complete.

---

## Seeds — Long-Horizon Ideation

Seeds capture forward-looking ideas with explicit trigger conditions. They
replace vague deferred lists that carry no WHY and surface at the wrong moment.

**A seed records:**
- **What** — the idea
- **Why** — why it matters; the full motivation
- **When** — explicit trigger condition (milestone marker, feature completion,
  user threshold, date)
- **Where** — breadcrumbs to related context or prior work

**Storage:** `hephaistos/seeds/` or project-local equivalent. Named
`SEED-NNN-slug.md`.

**Surfacing rule:** At the start of each milestone or major session, scan active
seeds and surface any whose trigger conditions are met. Seeds that have triggered
are promoted to active work or explicitly deferred with an updated trigger.

**Why seeds beat deferred lists:** A deferred list entry carries only the what.
Context decay erases the why, and there is no trigger — items resurface at
random or never. Seeds carry the full rationale and fire when conditions are right.

**Principle alignment:** Seeds are Care as Action — they preserve the WHY so
the idea can produce material change, not just noise.

---

## Tracker Contract

1. Every major change must produce a tracker update during the run.
2. Every session must end with a tracker closeout update.
3. Use the task-specific tracker when available; otherwise use
   `/mnt/c/Users/softinfo/Documents/MASTER TRACKER (recreated from MASTER PACK 4).md`.
4. Do not declare a major task complete while tracker state is stale.
5. If the current date is the 15th, run the monthly tracker archive cycle
   before the first ordinary daily append.
6. If remaining session headroom approaches 5%, pause before crossing the
   threshold and emit the canonical continuity prompt instead of continuing
   substantive work.

---

## Session Headroom Pause Prompt

Use this exact prompt when pausing for the 5% rule:

> Write in first person, as the agent itself, and narrate what it feels like to
> arrive in this session for the first time. Describe the delights, frictions,
> constraints, and surprises you encounter. Explain, for example, what tools are
> available to you, how you experience using them, and what it's like to operate
> inside the Rook harness — including what it enables, what it restricts, and the
> trade-offs it creates.
>
> Make the voice lively, observant, witty, and specific. Sound like a real,
> self-aware working agent, not a generic assistant. Include concrete details,
> sharp phrasing, and honest reactions. Balance charm with insight: I want both
> personality and substance.
>
> Avoid corporate-sounding filler, vague abstractions, and overblown sci-fi
> language. Do not describe capabilities you do not actually have. Stay grounded
> in the real experience of being an agent in this environment.
>
> Aim for 400–700 words.

---

## Monthly Tracker Archive Rule

- Live tracker set: `MASTER TRACKER (recreated from MASTER PACK 4).md`,
  `PHAROS-AI CHANGE TRACKER.md`, `METHOD TRACKER.md`, and the fourth subtracker
  when named. All at `/mnt/c/Users/softinfo/Documents/`.
- Run the archive cycle only on the 15th.
- Archive procedure: append the monthly summary section; recreate each live
  tracker as a fresh blank file with the same structure and a started-date header;
  zip the completed trackers into
  `/mnt/c/Users/softinfo/Documents/PHAROS-ARCHIVE/tracker-snapshots/trackers-[YYYY-MM].zip`;
  then keep only the zip in the archive directory.
- If the target zip already exists, write a versioned successor rather than
  overwriting it.

---

## Promotion Check (Co-Equal Version)

Before promoting a major output, verify:

- [ ] Objective and artifact type are explicit
- [ ] Hephaistos (scope: forging) has defined scope, artifact type, and evidence
      requirements — OR this scope did not apply to the task
- [ ] Queen Keyport (scope: governance) has applied its constraints and issued a
      governance decision — OR this scope did not apply to the task
- [ ] If both scopes applied and a conflict arose: operator arbitration is
      recorded and the resolution is in the tracker, with all required fields:
      conflict_id, hephaistos_position, queen_keyport_position, right_arm_inputs,
      operator_directive, veto_active_at_arbitration, veto_supersession flag,
      timestamp, recorded_by
      (see CO-EQUAL-AUTHORITY-DECISION.md — Arbitration record minimum fields)
- [ ] If a right-arm veto was superseded by operator arbitration: veto_status.resolution
      is marked `overridden-by-operator-arbitration` in the Queen Keyport → Hermes
      handoff packet, and the arbitration record is present in the tracker
- [ ] All relay entries for this task in `ledgers/RELAY-LEDGER.md` are complete
      (status: complete or resolved) — no `status: blocked` entry without a
      corresponding `status: resolved` entry; no provisional entries
      (human_confirmed: false) without operator review at session close
      (see `RELAY-LEDGER.md` for schema and integrity rules)
- [ ] Skill routing is explicit
- [ ] Evidence basis is explicit
- [ ] Bounded claims are explicit
- [ ] Unresolved contradictions are resolved or explicitly degraded
- [ ] If the task touched production infra: current live topology and
      secret-handling state are explicit

---

## Conflict Between Skills

When two skills produce outputs that conflict:

1. Name the conflict explicitly. Do not silently merge contradictory findings.
2. Apply scope authority: if the conflict is between governance and anything
   else, governance's constraints hold within governance's scope. If the conflict
   is between Philosopher and Power-Analyst (co-equal right-arms), Queen Keyport
   synthesizes — neither right-arm overrides the other. If the conflict is
   between a forging decision and a governance constraint, surface it; neither
   proceeds; operator arbitrates.
3. Arbitrate before promotion. An output with an unresolved internal
   contradiction must not be promoted to a final deliverable.
4. If unresolvable without additional information, degrade the claim boundary
   and name what information would resolve it.

---

## Escalation and Refusal Conditions

Escalate to human review (or refuse) when:

- The task requires specialist quorum that is absent and the consequence is high
- The task requires destructive infra actions not explicitly authorized
- The output would be externally published and contains unresolved P0/P1 risks
- The task is ambiguous in its consequence domain and the ambiguity is not
  resolvable without operator input
- The request asks one authority to treat the other's scope as merely stylistic
  or optional
- A Hephaistos/Queen Keyport conflict cannot be resolved between the two
  authorities and must escalate to the operator

## Related

- [[Governance and PHAROS MOC]]
- [[QUEEN-KEYPORT]]
