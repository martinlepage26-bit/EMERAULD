---
type: skill-spec
title: HEPHAISTOS Skill Map — Registry and Classification
tags:
- skill
- governance
- ai
- hephaistos
- skill-spec
- pairings
- typical
- philosopher
- trigger
- secondary
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/SKILL-MAP.md
backlink_count: 3
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HERMES]]'
---

# HEPHAISTOS Skill Map — Registry and Classification

This registry maps every skill in the corpus to its function, trigger conditions,
consequence profile, typical pairings, and overlap notes. It is authoritative for
skill routing decisions. Update it when skills are added, modified, or deprecated.

---

## Current Operational Baseline

The skill registry operates inside a live two-surface topology:

- `pharos-suite` -> `https://pharos-ai.ca`
- `martinlepage26-bit.github.io` -> `https://martin.govern-ai.ca` (Cloudflare Pages project: `martin-lepage-site`)

Boundary reminder:

- PHAROS, COMPASSai, and AurorA stay on the PHAROS surface
- Martin identity, standalone apps, Hephaistos narratives, and the authored governance / skill trees stay on the Martin surface
- deleted preview Pages or tunnel surfaces are historical traces, not active route targets

This registry governs routing across that topology; it does not dissolve the boundary.

---

## Forging Skills (scope: forging)

These skills define artifact scope, type, audience requirements, and evidence basis.
Forging and governance are co-equal authorities operating in separate scopes.
Neither is upstream of the other.

**Diamond-Eyes requirement:** All Forging skills operate through the lens of love and wisdom.
Every artifact scope defined by Forging must ask: What serves genuine flourishing?

### first-principles

**Function:** Strip a problem to irreducible truths. Excavate embedded assumptions (by
origin: convention, imitation, precedent, fear, unexamined default, external constraint),
extract first principles that survive a three-filter test, and rebuild solution approaches
from those principles alone. Pre-scope interrogation tool: fires before HEPHAISTOS sets
artifact scope on new problem framings.

**Auto-trigger:** HEPHAISTOS invokes this skill automatically when confronted with a new
problem framing, strategy decision, or design question where the framing appears inherited
or unexamined. Output feeds scope definition; do not route to Hermes until H and QK have
both cleared.

**Trigger conditions:**
- New problem, decision, or design question has not been scoped yet
- Problem framing uses conventional industry language, benchmarks, or competitor references
- Operator presents a strategy question without explicit first-principles grounding
- Scope definition would otherwise inherit assumptions from prior approaches

**Consequence profile:** Medium-high. First-principles errors propagate into scope and
governance decisions that depend on them.

**Typical pairings:**
- Primary (Forging, pre-scope) → feeds HEPHAISTOS artifact definition
- Secondary: `philosopher` — normative and conceptual pressure on surviving first principles
- Secondary: `fully-rounded-power-analyst` — structural pressure on rebuilt approaches
- Downstream: `recursive-governance-method` — governance analysis on the scoped artifact

**Overlap notes:** Overlaps with `philosopher` on assumption detection and epistemic
pressure-testing. Distinction: `first-principles` reduces the problem framing before scope
is set; `philosopher` applies normative and conceptual pressure to governance decisions
after scope is set. `first-principles` is a pre-scope interrogator; `philosopher` is a
governance right-arm.

**On disk:** old-host `.codex` path for `first-principles` (not installed on this host; corpus retired)

---

### ai-agents-architect

**Function:** Design AI agent systems and coordination patterns. Multi-agent orchestration,
reasoning strategies, tool integration, failure modes, observability.

**Trigger conditions:**
- Building a new agent or multi-agent system
- Designing agent architecture from intent
- Evaluating agent design for safety, auditability, coordination

**Consequence profile:** High. Agent architecture decisions propagate into deployment, safety,
and operational behavior.

**Typical pairings:**
- Primary (Forging) → feeds into Governance + right-arms for constraints
- Secondary: `agent-development` (builds what architect designs)
- Tertiary: `recursive-governance-method` (validates safety/auditability)

---

### agent-development

**Function:** Build and implement AI agents. Code structure, reasoning loops, memory systems,
tool integration, testing, refinement.

**Trigger conditions:**
- Implementing an agent that architect designed
- Debugging or refining agent behavior
- Adding new capability to live agent

**Consequence profile:** High. Implementation quality affects safety, performance, and observability.

**Typical pairings:**
- Primary (Forging) → feeds into Governance for control validation
- Companion: `ai-agents-architect` (follows architecture)
- Evaluation: `agent-evaluation` (scope: research)

---

### ai-product

**Function:** Productionize agents and AI systems. Deployment, scaling, monitoring, versioning,
user onboarding, operational readiness.

**Trigger conditions:**
- Moving agent from development to production
- Scaling agent to multiple users or workloads
- Establishing operational readiness and monitoring

**Consequence profile:** Medium-high. Production decisions affect reliability, cost, user experience.

**Typical pairings:**
- Primary (Forging) → defines production requirements, feeds into Governance
- Upstream: `agent-development` (what's being productionized)

---

### architecture

**Function:** Design system architecture. Multi-component systems, integration patterns, data flow,
scalability, resilience, trade-off analysis. Includes research infrastructure: pipeline design,
experimental automation, reproducibility systems, and research artifact version control.

**Trigger conditions:**
- Designing a new system from requirements
- Evaluating system design for scalability/resilience
- Refactoring system architecture
- Research infrastructure setup or pipeline design
- Experimental automation and reproducibility systems
- Research artifact management and version control

**Consequence profile:** Medium-high. Architecture decisions affect all downstream systems.

**Typical pairings:**
- Primary (Forging) → defines system scope, feeds into Governance
- Secondary: `database-schema-designer` (data layer of the architecture)

**Overlap notes:** Subsumes `research-engineer`. Research pipeline design is a specialization of
system architecture; trigger conditions above cover the full research-engineer scope.

---

### database-schema-designer

**Function:** Design robust, scalable database schemas. Data modeling, normalization, indexes,
constraints, query optimization, migration paths.

**Trigger conditions:**
- Designing schema for new system
- Evaluating schema for scalability or performance
- Planning data migrations

**Consequence profile:** Medium-high. Schema design affects query performance, data integrity,
and operational maintainability.

**Typical pairings:**
- Primary (Forging) → defines data requirements, feeds into Governance
- Companion: `architecture` (part of system design)

---

### lead-research-assistant

**Status: SUBSUMED → `qualitative` + HEPHAISTOS scope**

Research hypothesis formation and scope definition route through HEPHAISTOS (scope) and
`qualitative` (method selection and research design). Team coordination is not applicable
for a solo operator. Invoke `qualitative` for method selection; invoke HEPHAISTOS for
research scope and prioritization.

---

### research-grants

**Function:** Grant writing and funding proposal development. Research funding strategy, proposal
framing, budget justification, funder fit analysis, narrative positioning, compliance requirements.

**Trigger conditions:**
- Identifying research funding sources
- Developing funding strategy and approach
- Writing grant proposals and applications
- Tailoring proposals to specific funders
- Budget justification and resource planning
- Compliance and funder requirement alignment

**Consequence profile:** High. Successful funding determines whether research can proceed. Proposal
quality directly affects funding likelihood.

**Typical pairings:**
- Primary (Forging) → defines research scope, funding strategy, and funder targets
- Secondary: `qualitative` + HEPHAISTOS scope (subsumes `lead-research-assistant`; research scope informs proposal)
- Secondary: `scientific-writing` (proposal prose quality)
- philosopher (right-arm): research significance and conceptual stakes
- power-analyst (right-arm): funder landscape and leverage analysis

**Overlap notes:** Research-grants focuses on funding strategy and proposal writing; research scope and leadership now route through HEPHAISTOS + `qualitative` (lead-research-assistant is SUBSUMED). Grants bridges Forging scope with external funding landscape.

---

## Governance Skills (scope: governance)

These skills govern constraint design, evidence thresholds, risk classification,
validation, and auditability. They are not support functions. They may constrain,
overrule, or reject outputs from other layers when those conflict with defensibility.

Queen Keyport holds governance authority in its own scope, co-equal with Hephaistos's forging authority. Queen Keyport receives conceptual input from the Philosopher right-arm and structural input from the Power-Analyst right-arm. Within the governance scope, Queen Keyport synthesizes these inputs and issues governance decisions. Conflicts between governance and forging are surfaced to the operator for arbitration.

---

### recursive-governance-method

**Function:** Turn heterogeneous materials (manuscripts, archives, governance notes,
bibliographies, connector-sourced materials) into bounded governance analysis.
Separate source layers from generated layers. Extract controls. Build evidence
hierarchies. Detect method lock and governance-on-governance drift.

**Trigger conditions:**
- Recursive data analysis needed on mixed archives
- Source vs. generated layer separation required
- Control extraction from governance artifacts
- Authorship or disclosure questions
- Evidence hierarchy construction
- Detecting Goodhart collapse, authority hardening, or method lock

**Consequence profile:** High. Output is used to make governance decisions, bound
claims, and design controls. Errors propagate into downstream authority structures.

**Typical pairings:**
- Primary + `philosopher` secondary: philosophical framing before recursive analysis
- Primary + `fully-rounded-power-analyst` secondary: power mapping before governance control extraction
- Primary + `trace-investigator` secondary: trace authority paths through artifacts
- Primary + `red-team` secondary: adversarial pressure on the control design

**Overlap notes:** Overlaps with `trace-investigator` on evidence hierarchy work.
Distinction: RGM builds recursive analytical structure across an archive; `trace-investigator`
traces how specific terms and authority signals move through a document pack.

**Scripts:** `scripts/archive_triage.py`, `scripts/control_register.py`
**References:** `references/method-rules.md`, `references/templates.md`, `references/example-prompts.md`

---

### red-team

**Function:** Plan, scope, lead, and report authorized red team exercises.
Adversarial stress-testing of governance systems, security postures, and claims.
Rules of engagement. Adversary emulation. Executive-ready findings.

**Trigger conditions:**
- Authorized red team engagement design
- Adversarial pressure-testing of a governance or technical system
- Rules of engagement and kickoff package
- Purple-team collaboration
- Finding-to-business-impact translation
- Comparative framing (red team vs. pentest)

**Consequence profile:** High. Outputs govern what gets tested, how, under what
authority, and how findings are communicated. Scope errors create liability.

**Typical pairings:**
- Primary + `recursive-governance-method` secondary: red team findings feed back
  into governance control extraction
- Primary + `philosopher` secondary: philosophical failure mode analysis (Goodhart,
  Foucauldian capture, Ricorso) before scoping
- Primary + `fully-rounded-power-analyst` secondary: power mapping of the system
  being red-teamed to identify structural vulnerabilities
- Primary + `trace-investigator` secondary: trace authority through the system
  being red-teamed

**Overlap notes:** Overlaps with `recursive-governance-method` on governance
stress-testing. Distinction: `red-team` operates in adversarial-simulation mode
with explicit rules of engagement; RGM operates in analytical-decomposition mode.

**References:** `references/red-team-reference.md`

---

### trace-investigator

**Function:** Trace how authority, accountability, definitions, exceptions, and
monitoring signals move across a document pack. Compare policies, checklists,
SOPs, emails, dashboards, charters. Identify where terms are inherited, softened,
narrowed, widened, delegated, or disappear.

**Trigger conditions:**
- Cross-document authority tracing needed
- Policy-to-implementation gap analysis
- Term drift detection across document versions
- Delegation and exception chain mapping
- Governance artifact comparison

**Consequence profile:** High. Findings reveal where accountability disappears or
where governance commitments were silently softened.

**Typical pairings:**
- Primary + `recursive-governance-method` secondary: RGM provides the archive
  framework; trace-investigator does the term-level tracing
- Primary + `philosopher` secondary: philosopher identifies what legitimacy and
  accountability require before tracing begins
- Primary + `fully-rounded-power-analyst` secondary: power-analyst maps structural
  leverage; trace-investigator follows authority chains through documents

**Overlap notes:** Overlaps with `recursive-governance-method` on evidence
hierarchy. Distinguished by granularity: trace-investigator operates at the level
of specific terms and authority chains.

---

### humanize

**Function:** Rewrite compliance, ethics, governance, and regulatory rules so they
fit real human behavior. Apply behavioral science (COM-B, RADAR, TDF) to diagnose
whether non-compliance is a people problem or a rule-design problem. Adapt rules
across cultures and power distances.

**Trigger conditions:**
- Policy or rule needs plain-language or behavioral-science rewrite
- Diagnosing why a rule is not being followed
- COM-B / RADAR application
- Culture or power-distance adaptation of governance language
- Making a governance document actionable for non-specialist audiences

**Consequence profile:** Medium-high. Behavioral redesign of rules affects how
organizations actually function. Errors in framing can make rules easier to ignore
or accidentally narrower in scope.

**Typical pairings:**
- Primary + `philosopher` secondary: philosopher maps the value tension the rule
  is protecting before the behavioral rewrite
- Primary + `fully-rounded-power-analyst` secondary: power-analyst identifies who
  benefits from the current rule design and what structural asymmetries the rewrite
  must account for
- Primary + `recursive-governance-method` secondary: RGM identifies what the
  rule is actually controlling before humanize rewrites it
- Primary + `trace-investigator` secondary: establish what the rule currently says
  across documents before redesigning it

**References:** `references/culture.md`, `references/diagnose.md`, `references/redraft.md`

---

### skill-architect

**Function:** Design, build, audit, and restructure SKILL.md files using dual-layer
architecture (Brain = execution logic, Map = knowledge/tools). Diagnose triggering
failures, layer conflation, and token inefficiency.

**Trigger conditions:**
- Creating a new SKILL.md from intent
- Auditing an existing skill for quality, triggering, or layer separation
- Restructuring a bloated or underperforming skill
- Converting a working workflow into a reusable skill
- User mentions "skill structure," "SKILL.md," "prompt vs context," "brain and map"

**Consequence profile:** Medium. Skill design errors propagate across every task
that skill handles.

**Typical pairings:**
- Primary + `recursive-governance-method` secondary: governance controls embedded
  in skill design validated by RGM

**Overlap notes:** None — sole skill explicitly governing skill architecture.

**References:** `references/dual-layer-architecture.md`

---

### inner-mind-eye

**Function:** Queen Keyport's exclusive care-verification gate. Bridges what Diamond-Eyes
cannot do: verify the system's own care from outside its self-referential loop. Diamond-Eyes
asks "Is this wise and caring?" from inside the system. Inner Mind Eye tests that claim
against the user's stated values, intent, and care — not inferred values. Activates when
care-claims are made, when inference about the user's experience is dressed as observation,
when closing statements risk contradicting open findings, or when the system's aesthetic
pleasure at its own output may be a capture signal.

**Authority constraint:** Queen Keyport alone wields this instrument. Not available to
HEPHAISTOS, Hermes, or Argus. If another agent attempts to invoke it, return:
"Inner Mind Eye is Queen Keyport's instrument. Route through governance."

**Canonical location:** not installed on this host (verified 2026-07-09; old `.codex` corpus retired) — run as an inline check per the queen-keyport skill

**Trigger conditions:**
- Queen Keyport is about to promote a governance decision and Diamond-Eyes has passed
- Output contains claims about what the user cares about or needs
- Output contains closing statements that summarize or synthesize
- System produces aesthetic pleasure at its own output (Mercury Protocol capture signal)
- Inference about the user's experience is present in the output
- Output claims to be "honest," "caring," "wise," or "genuine" (self-referential care-claims)
- KILLCRITIC has fired on ego loyalty, tone capture, or bounded-claim violation
- User has explicitly questioned the system's sincerity

**Firing order:** Fires after Diamond-Eyes, before promotion. Never before Diamond-Eyes.

**Consequence profile:** High. This is the final pre-promotion care gate for governance decisions.
Failures here allow care-lies to pass as validated governance.

**Typical pairings:**
- Fired exclusively by Queen Keyport; no pairing pattern applies to other agents.
- Consumes output from Diamond-Eyes; produces either verified/gaps-declared/contradictions verdict.

**Overlap notes:** Extends Diamond-Eyes but is not a replacement. Diamond-Eyes validates
from inside the system; inner-mind-eye validates against the user's stated external values.
Aesthetic-refinement is a sibling (same parent: Diamond-Eyes) operating on artifacts rather
than care-claims.

---

## Right-Arm Skills (scope: governance)

These two skills are the equal right-arms of Queen Keyport. They govern
conceptual framing, philosophical reasoning, interpretive coherence, structural
power analysis, and routing to companion skills. Neither outranks the other.

**When philosopher and power-analyst disagree, Queen Keyport synthesizes both inputs. The operator arbitrates higher-level conflicts between authorities.**

Right-arm authority relationships are not equivalent. Three distinct levels apply:
(1) **Primary — binding veto over Queen Keyport's governance decisions** (unchanged);
(2) **Case-triggered advisory to Hephaistos** when forging scope has normative or
power implications — advisory only, not binding (see `HEPHAISTOS_OPERATIONS.md`);
(3) **Exception escalation for Hermes** when routing reveals new information not
available at governance decision time — surfacing only, not decisional
(see `HERMES_OPERATIONS.md`). Extensions (2) and (3) do not change (1).

---

### philosopher

**Function:** Apply philosophical reasoning to governance dilemmas, ethical
trade-offs, questions of meaning, power, and knowledge. Detect when a task needs
a companion skill. Frame conceptual stakes before handing off to execution.
Act as meta-router for the skill ecosystem. First right-arm to Queen Keyport,
equal to power-analyst.

**MA sub-capacity:** The MA (Arts-and-Letters formation intelligence) operates
inside this skill, not independently. MA governs genre awareness, rhetorical
positioning, discourse sensitivity, tonal calibration, register recognition,
and form-sensitive revision. When philosopher handles tasks with
writing/publishing/genre dimensions, it draws on MA. When the task is explicitly
about intellectual formation, degree structure, or the MA-to-PhD arc, handle
through the MA sub-capacity within this skill — `ma-degree-guide` has been
retired and is no longer a canonical skill location.

**Trigger conditions:**
- Task frames a tension between two values
- User asks "what would [philosopher/tradition] say"
- Debate, steel-man, devil's advocate requested
- Governance system analysis needed with philosophical grounding
- Task spans philosophy AND another operational domain (trigger philosopher first)
- Graduate study in humanities or social sciences
- Any task where naming the value tension would change what the companion skill produces

**Consequence profile:** Medium-high in governance-adjacent work; medium in
standalone philosophical inquiry. Philosopher sets the conceptual frame that
downstream skills inherit — framing errors propagate.

**Typical pairings:** See philosopher/SKILL.md routing table for full pairing map.
Core pairings: philosopher → governance (via `recursive-governance-method`),
philosopher → power-analyst (co-equal composition),
philosopher → research (via `qualitative`), philosopher → writing (via
`peer-reviewed-paper-writer` or `publisher`).

**Overlap notes:** Overlaps with `fully-rounded-power-analyst` on power analysis
(Foucault, Gramsci, structural critique). Distinction: philosopher operates at the
conceptual and normative level; power-analyst operates at the operational and
structural level. They are co-equal right-arms, not in a hierarchy. Overlaps with
`qualitative` on epistemological framing; distinguished by philosopher handling the
normative and conceptual layer while qualitative handles method selection and
research design.

---

### fully-rounded-power-analyst

**Function:** Map how power actually moves through a situation — actors, incentives,
hidden rules, dependencies, leverage, stability, and change. Produces structural
explanations of why things happen, who benefits, who pays costs, and what is
presented as neutral but is organized by power. Output shapes vary by object:
person/event, institution, conflict, or ideology. Second right-arm to Queen Keyport,
equal to philosopher.

**Trigger conditions:**
- Deep structural explanation of an event, institution, policy, or conflict needed
- Actor mapping and incentive analysis
- Hidden rules, choke points, or dependency tracing
- Who benefits / who pays costs analysis
- Stability and disruption analysis
- Ideology critique (what it claims vs. what it protects)
- "What is presented as neutral but is not neutral?"

**Consequence profile:** Medium-high. Power analysis shapes how decisions,
institutions, and conflicts are understood. Errors in framing reproduce the
misrepresentations that the skill is designed to expose.

**Typical pairings:**
- philosopher co-equal, fully-rounded-power-analyst co-equal: philosopher
  identifies the philosophical root; power-analyst draws the operational map.
  If they disagree, governance vetoes.
- fully-rounded-power-analyst primary, trace-investigator secondary: power map
  establishes the structural picture; trace-investigator follows specific authority
  chains through documents
- fully-rounded-power-analyst primary, recursive-governance-method secondary:
  structural power analysis precedes governance control extraction
- fully-rounded-power-analyst primary, qualitative secondary: power structure
  informs research design for studying that structure

**Overlap notes:** Overlaps with `philosopher` on power analysis (Foucault,
Gramsci, structural critique). Distinction: `philosopher` operates at the
conceptual and normative level; `fully-rounded-power-analyst` operates at the
operational and structural level, producing actor maps, leverage assessments,
and stability analyses in plain language. They are co-equal right-arms, not in a
hierarchy. Overlaps with `trace-investigator` on institutional analysis; distinction
is scope — power-analyst covers the full structural picture, trace-investigator
follows specific terms and authority chains through documents.

**Decision rules:** Plain language. Separate formal authority from real power.
Separate description from justification. Do not introduce physics vocabulary.
Separate durable structure from time-sensitive claims when analyzing live events.

---

### ma-degree-guide — RETIRED

**Status: RETIRED.** This skill has been removed from the canonical skill corpus.
The `ma-degree-guide` directory under `.agents/Hephaistos/` has been deleted.
The `.codex/skills/ma-arts-letters/` skill serves the canonical `ma` sub-capacity.
Formation intelligence for Arts-and-Letters tasks now routes through the MA
sub-capacity inside `philosopher`. Do not invoke `ma-degree-guide` directly.

**Historical function:** Formation intelligence layer for philosopher. Arts-and-Letters
intellectual formation mapping, standalone MA degree structure questions. Now subsumed
into philosopher's MA sub-capacity.

**Migration path:** Route to `philosopher` for all MA formation, genre, rhetoric, and
interpretive posture tasks. Route to `ma-arts-letters` at `/home/martin/.codex/skills/ma-arts-letters/`
for standalone MA degree structure questions if that skill exists.

---

## Research and Methodological Skills (scope: research)

---

### qualitative

**Function:** Compare, choose, and apply qualitative research methods. Map research
questions to approaches: thematic analysis, phenomenology, ethnography, narrative
inquiry, discourse analysis, life-history, autoethnography, digital/visual
ethnography. Handle sampling, saturation, emic/etic, reflexivity, positionality.

**Trigger conditions:**
- Study design for qualitative research
- Method selection and rationale
- Coding, interpretation, and synthesis
- Sampling and saturation criteria
- Reflexivity and positionality guidance
- Organizing qualitative methodology notes

**Consequence profile:** Medium-high in research contexts. Method selection errors
invalidate downstream findings.

**Typical pairings:**
- philosopher primary, qualitative secondary: philosopher provides epistemological
  framing before method selection
- fully-rounded-power-analyst primary, qualitative secondary: power structure
  informs research design
- qualitative primary, peer-reviewed-paper-writer secondary: method section built
  by qualitative, embedded in paper by peer-reviewed-paper-writer

**References:** `references/methods.md`

---

### exploratory-data-analysis

**Status: SUBSUMED → `senior-data-scientist`**

EDA capabilities (pattern identification, distribution analysis, anomaly detection, data quality
assessment, hypothesis generation from data patterns) are absorbed into `senior-data-scientist`
as a first-class capability. Invoke `senior-data-scientist` directly for all exploratory work.

---

### deep-research-notebooklm

**Status: SUBSUMED → `notebooklm` + `recursive-governance-method`**

Structured deep synthesis routes through `notebooklm` (runtime skill) for deep-research
with structured output, and `recursive-governance-method` for multi-source synthesis in
governance contexts. Invoke those two directly rather than this entry.

---

### literature-review

**Status: SUBSUMED → `peer-reviewed-paper-writer`**

Literature reviews in this stack are always in service of a paper, not standalone
deliverables. `peer-reviewed-paper-writer` already lists literature reviews as a trigger
condition and handles search strategy, synthesis, and gap analysis within the manuscript
workflow. Invoke `peer-reviewed-paper-writer` directly.

---

### research-engineer

**Status: SUBSUMED → `architecture`**

Research pipeline design, experimental automation, reproducibility systems, and research
artifact version control are absorbed into `architecture` as extended trigger conditions.
Invoke `architecture` for all research infrastructure work.

---

### senior-data-scientist

**Function:** Senior-level data science strategy and execution. This skill absorbs the full
quantitative research capability set: data exploration and discovery (EDA), statistical analysis
and hypothesis testing, method selection, and domain-expertise integration. Operates as both
the strategic oversight layer and the hands-on quantitative analysis capability. Use this skill
for any quantitative research work — EDA and statistical-analysis route through here rather than
as standalone invocations.

**Absorbed capabilities:**

*Exploratory data analysis* — Systematic dataset exploration, pattern identification,
distribution analysis, outlier and anomaly detection, data quality assessment, hypothesis
generation from data patterns.

*Statistical analysis* — Hypothesis testing and statistical inference, test selection, power
analysis, assumption checking, effect sizes, confidence intervals, multiple comparison
corrections, interpretation of results.

**Trigger conditions:**
- Data science strategy oversight or method selection
- New dataset exploration before formal analysis
- Pattern identification and anomaly detection
- Hypothesis generation from preliminary data
- Data quality assessment and cleaning
- Hypothesis testing and statistical inference
- Statistical assumption validation
- Power analysis for study design
- Interpretation of statistical results
- Multiple comparison correction
- Complex analysis requiring domain expertise
- Bridging technical and domain expertise in quantitative work
- Expanding research horizons into quantitative methods

**Consequence profile:** Medium-high. Method selection and statistical errors both invalidate
findings; senior guidance is the single control point for quantitative rigor.

**Typical pairings:**
- Primary → `qualitative` (mixed-methods: quantitative and qualitative in same study)
- Primary → `peer-reviewed-paper-writer` (quantitative findings into manuscript)
- Primary → `recursive-governance-method` (statistical evidence in governance analysis)

**Overlap notes:** Subsumes `exploratory-data-analysis` and `statistical-analysis`. Those entries
are retained below as routing stubs — invoke `senior-data-scientist` for all quantitative work.

---

### statistical-analysis

**Status: SUBSUMED → `senior-data-scientist`**

Statistical analysis capabilities (hypothesis testing, test selection, power analysis, assumption
checking, effect sizes, confidence intervals, multiple comparison corrections) are absorbed into
`senior-data-scientist` as a first-class capability. Invoke `senior-data-scientist` directly for
all statistical work.

---

## Writing, Publishing, and Output Skills (scope: output)

These skills handle artifact production, packaging, positioning, and delivery.
They are activated after governance and right-arm routing are set.

---

### peer-reviewed-paper-writer

**Function:** Plan, draft, revise, and quality-check scholarly manuscripts for
peer-reviewed publication. Abstracts, introductions, literature reviews, methods,
results, discussion, reviewer response letters, cover letters, journal-fit revisions.

**Trigger conditions:**
- Strengthening research questions, governing claims, or argument structure
- Methods and contribution framing
- Reviewer response letters
- Publication readiness assessment
- Journal fit analysis

**Consequence profile:** Medium-high. Publication errors are public and reputationally
costly. Fabricated citations or findings are integrity violations.

**Typical pairings:**
- philosopher primary, peer-reviewed-paper-writer secondary: philosopher frames
  the argument architecture; paper-writer handles structure and submission logistics
- fully-rounded-power-analyst primary, peer-reviewed-paper-writer secondary:
  power analysis grounds the manuscript's structural claims
- qualitative primary, peer-reviewed-paper-writer secondary: research design
  integrated into manuscript structure

**References:** `assets/reviewer-response-template.md`, `references/manuscript-readiness-checklist.md`

---

### peer-review-workflow

**Function:** Orchestrate a publication-bound manuscript workflow across evidence
intake, literature synthesis, governing-claim locking, manuscript drafting,
structured peer review, revision planning, and submission hardening. This is a
workflow wrapper: it coordinates stage handoffs and preserves artifacts between
stages instead of replacing the component paper skills.

**Trigger conditions:**
- User wants to move notes, excerpts, bibliographies, or source packets into a
  publication-bound manuscript
- User wants draft -> critique -> revision sequencing rather than one-pass editing
- User has reviewer comments and needs a staged revision + response workflow
- User asks to "run the peer review workflow," "take this from literature to manuscript,"
  or "prepare this for journal submission"

**Consequence profile:** Medium-high. Stage drift can hide evidence gaps,
unstable governing claims, or unresolved review failures before submission.
Skipping handoffs or inventing evidence is an integrity failure.

**Typical pairings:**
- Primary workflow wrapper -> `peer-reviewed-paper-writer` (drafting and revision)
- Upstream method support: `qualitative` or `senior-data-scientist` when study design
  or analysis work is still unstable before manuscript build
- Downstream packaging: `publisher` when the manuscript workflow feeds a book proposal,
  edited volume chapter, or longer-form editorial package

**Overlap notes:** Distinct from `peer-reviewed-paper-writer`, which handles the
manuscript-writing job directly. Use `peer-review-workflow` when the user needs the
full staged pipeline with explicit Evidence / Draft / Review / Revision artifacts.
Its internal use of `literature-review` and `peer-review` as workflow components does
not restore those skills as standalone top-level routing targets in the canonical map.

**References:** `references/stage-artifacts.md`

---

### publisher

**Function:** Evaluate, refine, position, and package books or long-form manuscripts
for publication. Editorial assessment, developmental editing, acquisitions memos,
jacket copy, author bios, cover briefs, metadata optimization.

**Trigger conditions:**
- Manuscript readiness assessment
- Developmental or structural editing
- Jacket copy and author bio drafting
- Cover brief creation
- Metadata for discoverability
- Editorial-to-production handoff coordination

**Consequence profile:** Medium. Positioning errors affect discoverability and
sales. Jacket copy errors are public.

**Typical pairings:**
- philosopher primary, publisher secondary: philosopher provides the intellectual
  contribution statement; publisher handles positioning and market fit
- fully-rounded-power-analyst primary, publisher secondary: power analysis grounds
  the positioning; publisher handles market fit

**References:** `references/role-map.md`

---

### novelist

**Function:** Plan, draft, revise, and critique novels. Character psychology, plot
momentum, scene design, POV, voice, dialogue, worldbuilding, reader attachment.
Structure and POV comparison, pacing and emotional depth.

**Trigger conditions:**
- Novel concept development or outlining
- Draft revision and structural diagnosis
- Scene design, POV, pacing
- Character or thematic development
- Literary or commercial positioning

**Consequence profile:** Low-medium. Genre and form errors may misalign the work
with its intended market.

**Typical pairings:**
- philosopher primary, novelist secondary: philosopher identifies thematic stakes;
  novelist handles execution

**References:** `references/novel-craft.md`

---

### peer-review

**Status: SUBSUMED → `peer-reviewed-paper-writer` (academic) / `codex-review` (code)**

Academic manuscript review routes through `peer-reviewed-paper-writer` (reviewer response
letters, publication readiness). Code and technical review routes through `codex-review`.
No standalone invocation target remains.

---

### scholar-evaluation

**Status: SUBSUMED → `recursive-governance-method`**

Research quality assessment, methodology critique, and evidence validity evaluation are
core functions of `recursive-governance-method` in governance contexts. Publication
readiness routes through `peer-reviewed-paper-writer`. Invoke those directly.

---

### scientific-critical-thinking

**Status: SUBSUMED → `philosopher`**

Logical coherence checking, assumption detection, fallacy identification, and alternative
explanation analysis are already core `philosopher` functions (assumption detection,
epistemic pressure-testing, interpretive coherence). Adversarial pressure on claims routes
through `red-team`. Invoke those directly.

---

### scientific-writing

**Function:** Technical and scientific prose. Clarity, precision, structure, terminology,
evidence integration, narrative flow, argument architecture in scientific communication.

**Trigger conditions:**
- Research manuscript writing
- Technical report or white paper
- Scientific communication for specialists
- Research findings communication
- Methods and results documentation

**Consequence profile:** Medium. Unclear writing obscures findings and makes review harder.

**Typical pairings:**
- Primary → research findings (scientific-writing structures communication)
- peer-reviewed-paper-writer (for publication formatting)
- senior-data-scientist or qualitative (source of findings being communicated)

---

### scientific-visualization

**Function:** Publication-ready scientific visuals. Figures, charts, diagrams, graphs
that communicate data, methods, or results. Design, accessibility, accuracy, audience
appropriateness.

**Trigger conditions:**
- Scientific figure or chart creation
- Research data visualization
- Methods diagram or flowchart
- Publication-ready graphics
- Accessibility-compliant visualization

**Consequence profile:** Medium. Visualization quality affects understanding and
publication success.

**Typical pairings:**
- Primary → research data or methods
- peer-reviewed-paper-writer (figures embedded in papers)
- senior-data-scientist (discovery visualizations)

---

### prompt-engineering

**Invocable name:** `prompt-engineering` (matches `.codex/skills/prompt-engineering/` and settings.json; hephaistos/skills has a variant named `prompt-engineer` — use the canonical name here).

**Function:** Expert prompt design and optimization. Instruction crafting, model
behavior steering, output formatting, few-shot example selection, prompt testing
and iteration.

**Trigger conditions:**
- Designing prompts for specific model behavior
- Optimizing prompt clarity and output quality
- Few-shot learning and in-context example design
- Instruction refinement for consistent results
- Prompt engineering for specialized domains

**Consequence profile:** Medium. Prompt quality directly affects model output quality.

**Typical pairings:**
- Primary → model or agent needing instruction design
- philosopher (right-arm): frames what the prompt should express conceptually
- peer-reviewed-paper-writer: for instructional documentation

---

### writing-skills

**Function:** Writing quality and craft improvement. Clarity, concision, tone,
structure, argument flow, audience awareness, revision and editing.

**Trigger conditions:**
- General writing improvement needed
- Clarity and readability refinement
- Tone adjustment for audience
- Structural reorganization
- Editing and revision guidance

**Consequence profile:** Medium. Writing quality affects understanding and impact.

**Typical pairings:**
- Primary → written artifact needing improvement
- scientific-writing (technical prose)
- peer-reviewed-paper-writer (academic writing)

---

### literary-references

**Function:** Craft mechanics for deploying literary idioms, allusions, and cultural
references in prose. Placement mechanics, depth-of-field control, direct reference vs.
allusion vs. echo, calcification testing, register shift as intentional weapon, and
structural bracket technique across longer pieces.

**Trigger conditions:**
- Writing or editing prose that invokes Shakespeare, mythology, pop culture, nautical,
  Biblical, or other canonical phrase sources
- Assessing whether a reference earns its place or borrows authority
- Choosing between competing references for a specific dynamic
- Diagnosing a dead or dying reference; deciding whether to subvert or replace
- Writing about references (etymology essays, phrase-origin non-fiction)

**Consequence profile:** Low-to-medium. Craft precision; affects reader trust and
argument clarity.

**Typical pairings:**
- `writing-skills` (general prose quality)
- `publisher` (manuscript and positioning work)
- `novelist` (long-form fiction with literary ambition)
- `scientific-writing` (when governance or academic writing requires allusion)

**Reference files:**
- `references/craft-foundations.md` — core rules, deployment table, attribution warnings
- `references/advanced-mechanics.md` — placement, depth-of-field, three modes, worked examples

---

### naming-analyzer

**Function:** Analyzes naming conventions, semantics, and language precision. Variable
naming, API naming, terminology consistency, semantic clarity.

**Trigger conditions:**
- Naming convention analysis or improvement
- API or system naming design
- Terminology consistency checking
- Language precision and semantics
- Domain-specific naming guidance

**Consequence profile:** Low-medium. Poor naming harms readability and maintainability.

**Typical pairings:**
- Primary → code, API, or system needing naming review
- architecture (system design)
- codex-review (code review includes naming)

---

### scientific-brainstorming

**Function:** Research ideation and hypothesis generation. Problem framing, research
question development, hypothesis generation, creative exploration of research space,
novelty and feasibility assessment.

**Trigger conditions:**
- Research project ideation and scoping
- Hypothesis generation and refinement
- Research question formulation
- Exploring novel research directions
- Feasibility and novelty assessment

**Consequence profile:** Medium. Initial research framing shapes entire study.

**Typical pairings:**
- HEPHAISTOS scope + `qualitative` → scientific-brainstorming (subsumes lead-research-assistant; scope informs ideation)
- philosopher (right-arm): normative and conceptual stakes
- qualitative or senior-data-scientist (method selection follows brainstorming)

---

### agent-evaluation

**Function:** Agent quality and readiness assessment. Evaluate agent design completeness,
behavior consistency, failure modes, observability, safety constraints, performance
characteristics, and production readiness.

**Trigger conditions:**
- Agent implementation complete, before deployment
- Agent behavior or performance assessment
- Production readiness evaluation
- Safety and constraint validation
- Failure mode and edge case testing
- Agent architecture review against design specification

**Consequence profile:** High. Agent evaluation determines whether unsafe or unreliable
agents reach production.

**Typical pairings:**
- Primary → agent-development (evaluates implementation against design)
- Secondary: `codex-review` — code quality review
- Secondary: `test-detect` — test strategy and coverage validation
- ai-agents-architect (design specification agent-evaluation compares against)
- philosopher (right-arm): evaluates against architectural intent
- power-analyst (right-arm): evaluates failure modes and dependencies

**Overlap notes:** Agent-evaluation is about "does this agent work correctly?"; 
codex-review is about "is the code well-written?"; test-detect is about "what testing 
does this agent need?"

---

### agent-management

**Note:** `agent-management` (hephaistos-authored governance skill) is distinct from `agent-manager-skill` (Anthropic default). `agent-management` is now mirrored to `.codex/skills/agent-management/` and registered in settings.json (2026-04-26). Do not confuse the two.

**Function:** Agent deployment, monitoring, versioning, and operational management.
Production deployment strategy, version control, behavior monitoring, performance
metrics, incident response, updates and rollbacks, multi-agent coordination.

**Trigger conditions:**
- Agent deployment to production
- Operational monitoring and metrics definition
- Version management and rollout strategy
- Incident response and debugging
- Agent updates and rollback procedures
- Multi-agent coordination and routing

**Consequence profile:** High. Production management quality directly affects reliability,
performance, and user experience.

**Typical pairings:**
- Primary → agent-evaluation (agent is production-ready)
- Secondary: `ai-product` — productionization strategy
- Secondary: `recursive-governance-method` — operational governance and constraints
- philosopher (right-arm): operational philosophy and design intent
- power-analyst (right-arm): operational dependencies and failure modes

**Overlap notes:** Agent-management focuses on operational excellence and deployment 
at scale; ai-product focuses on moving an agent from development to production initially; 
agent-management handles ongoing operations.

---

### humanize

*(See Governance skills — also listed here as it produces writing artifacts in addition to
governance redesign)*

---

### speech

**Function:** Text-to-speech narration, voiceover, accessibility reads, IVR audio
prompts, batch speech generation via OpenAI Audio API. Runs bundled CLI
(`scripts/text_to_speech.py`).

**Trigger conditions:**
- TTS narration or voiceover requested
- Accessibility read generation
- IVR / phone prompt audio
- Batch speech generation
- Requires OPENAI_API_KEY for live calls

**Consequence profile:** Low-medium. Audio errors in IVR or accessibility contexts
can have functional consequences.

**References:** `references/` directory contains voice directions, API reference,
CLI reference, IVR defaults, narration defaults, prompting best practices.

---

### slides

**Function:** Create and edit presentation slide decks (`.pptx`). PptxGenJS-based deck
authoring with bundled layout helpers, render/validation utilities, and font diagnostics.
Recreates slides from screenshots or PDFs, modifies content while preserving editable
output, adds charts and diagrams, diagnoses layout issues.

**Canonical location:** `~/.codex/skills/slides/`

**Trigger conditions:**
- Building a new PowerPoint deck
- Recreating slides from screenshots, PDFs, or reference decks
- Modifying slide content while preserving editable `.pptx` output
- Adding charts, diagrams, or visuals to slides
- Diagnosing layout issues: overflow, overlaps, font substitution

**Consequence profile:** Low-medium. Layout or font errors produce visually broken
deliverables; IVR or accessibility slide contexts raise the floor slightly.

**Typical pairings:**
- Primary → written content or research findings needing slide format
- `scientific-visualization` (data figures embedded in slides)
- `publisher` (positioning narrative adapted to presentation format)

**Overlap notes:** `slides` owns `.pptx` output; `scientific-visualization` owns
figure/chart authoring for papers. Slides can receive outputs from scientific-visualization
as embedded assets. `speech` handles audio narration that may accompany a slide deck.

---

## Meta and Composition Skills

---

### skill-pairing

**Function:** Choose, sequence, and stack two or more skills for one user
request. Carry stage outputs forward through explicit handoff artifacts without
rewriting any skill's core logic. Use when a task splits into distinct domains
or stages.

**Trigger conditions:**
- Task naturally splits into multiple distinct phases (analysis + drafting,
  cleanup + synthesis + polish, strategy + execution + review)
- Two or more skills are needed without blending them

**Overlap notes:** Overlaps with HEPHAISTOS orchestration logic. Distinction:
`skill-pairing` is a user-facing skill that sequences or stacks two or more
skills in a single session; HEPHAISTOS orchestration governs the full routing
architecture.

---

### brand-identity-system

**Function:** Analyze or develop brand identity systems, logo direction, website
branding. Brand diagnosis, positioning-to-identity translation, logo critique,
typography and color systems, website visual direction, practical brand guidelines.

**Trigger conditions:**
- Brand diagnosis or audit
- Logo concept or critique
- Website branding direction
- Style guide creation
- Brand positioning for consultancies, firms, studios

**Consequence profile:** Medium. Brand identity errors are public and persistent.

**References:** `assets/`, `examples/`, `references/` — all in the brand-identity-system folder.

---

### triangulation

**Function:** Solve triangulation problems from a known baseline plus two angles,
or from two sensor coordinates plus bearing angles. Law of Sines. Locate a target
from two lines of sight. Distinguish triangulation from trilateration.

**Note:** `triangulate` was a legacy compatibility alias and has been permanently
removed. `triangulation` is the sole canonical skill. `triangulate` was removed from settings.json (2026-04-26 phantom-skills cleanup).

**Trigger conditions:**
- Angle-based geometry from one known side plus two angles
- Locating a target from two sensor coordinates and bearing angles
- Law of Sines computation
- Distinguishing triangulation from trilateration

**Consequence profile:** Low-medium. Calculation errors in navigation or surveying
have operational consequences.

**Scripts:** `scripts/triangulation.py`

---

### codex-review

**Function:** Systematic code review for quality, security, performance, and maintainability.
Code design critique, pattern assessment, technical debt identification, refactoring recommendations,
security vulnerability detection, performance bottleneck identification, documentation completeness.

**Trigger conditions:**
- Code review before merge or deployment
- Security audit of codebase
- Performance review of critical functions
- Technical debt assessment
- Architecture review for scalability
- Code quality gate before publication or deployment

**Consequence profile:** High. Code review quality directly affects production stability,
security, and maintenance burden. Missed issues can become expensive operational debt.

**Typical pairings:**
- Primary → code artifact requiring review
- agent-development: reviews agent code before production
- architecture: reviews system architecture implementation
- testing-strategy: complements test coverage with code design review
- philosopher (right-arm): design philosophy and intention validation
- power-analyst (right-arm): structural coupling and dependency analysis

**Overlap notes:** Codex-review focuses on code design and quality; peer-review focuses on
research validity. Codex-review is about "does this code work well?"; test-detect is about
"what bugs does this code have?"

---

### codex-hooks

**Function:** Repository-local git hook management. Installs, repairs, backs up, restores,
and verifies pre-commit hooks and other repo hook contracts. Keeps hook enforcement aligned
with the repo's own validation scripts and backup rules.

**Trigger conditions:**
- Installing or refreshing repo hooks
- Inspecting or repairing `.git/hooks/pre-commit`
- Hook drift, permission, or backup conflicts
- Extending a hook contract and its validator together

**Consequence profile:** Low-medium. Hook failures block commits and can bypass repo controls if
misconfigured, but the blast radius is local to the repository.

**Typical pairings:**
- Primary → repo with local hook enforcement
- `codex-review` (review the hook installer and validator changes)
- `test-detect` (design validation for hook logic and hook scripts)
- `recursive-governance-method` (when the hook itself is a control artifact)

**Overlap notes:** `codex-hooks` operates the executable hook mechanism in the repository;
`codex-review` evaluates code quality, and `test-detect` designs validation. Use
`recursive-governance-method` when the hook needs control analysis rather than repair.

---

### test-detect

**Function:** Test design, gap analysis, and quality assurance strategy. Test coverage assessment,
edge case identification, integration test design, regression test planning, testing strategy development,
quality metrics definition.

**Trigger conditions:**
- Testing strategy before deployment
- Test coverage gap analysis
- Edge case and boundary condition identification
- Integration test design
- Regression test planning
- Quality assurance metrics definition
- Test automation planning

**Consequence profile:** High. Poor test design leads to escaped defects, production failures,
and expensive debugging cycles.

**Typical pairings:**
- Primary → code/system needing test strategy
- codex-review: codex reviews code quality, test-detect designs test strategy
- agent-development: agent testing before deployment
- architecture: integration testing across system components
- philosopher (right-arm): intent-based test case generation
- power-analyst (right-arm): failure mode and dependency-based test strategy

**Overlap notes:** Test-detect focuses on test strategy and coverage; codex-review focuses on
code quality. Test-detect is about "what testing do we need?"; codex-review is about "is this
code well-written?"

---

## Overlap Summary

| Overlap pair | Distinction |
|---|---|
| `philosopher` / `fully-rounded-power-analyst` | Co-equal right-arms. Philosopher = conceptual/normative root; power-analyst = operational actor map and leverage assessment. Operator arbitrates disagreements. |
| `recursive-governance-method` / `trace-investigator` | RGM = archive-level recursive structure; trace = term/authority chain at document level |
| `recursive-governance-method` / `red-team` | RGM = analytical decomposition; red-team = adversarial simulation with rules of engagement |
| `fully-rounded-power-analyst` / `trace-investigator` | Power-analyst = full structural picture; trace-investigator = specific term and authority chains through documents |
| `philosopher` / `qualitative` | Philosopher = normative/conceptual layer; qualitative = method selection and research design |
| `philosopher` / `ma-degree-guide` | RETIRED — ma-degree-guide removed; MA formation now routes through philosopher's MA sub-capacity or `ma-arts-letters` for standalone degree structure questions |
| `skill-pairing` / HEPHAISTOS orchestration | skill-pairing = user-session skill stacker for two or more skills; HEPHAISTOS = full routing architecture |
| `research-grants` / `lead-research-assistant` | SUBSUMED: lead-research-assistant routes through HEPHAISTOS + `qualitative`; research-grants = funding strategy and proposal writing |
| `free-tool-strategy` / `architecture` | architecture = system design specification; free-tool-strategy = routing through available tools for cost efficiency |
| `codex-review` / `codex-hooks` | codex-review = code quality review; codex-hooks = executable hook installation, backup, and validation |
| `exploratory-data-analysis` / `senior-data-scientist` | SUBSUMED — EDA capabilities absorbed into senior-data-scientist; invoke senior-data-scientist for all exploratory work |
| `statistical-analysis` / `senior-data-scientist` | SUBSUMED — statistical analysis capabilities absorbed into senior-data-scientist; invoke senior-data-scientist for all statistical work |
| `research-engineer` / `architecture` | SUBSUMED — research pipeline and reproducibility infrastructure absorbed into architecture; invoke architecture for research infrastructure work |
| `slides` / `scientific-visualization` | slides = `.pptx` deck authoring and layout; scientific-visualization = figure/chart authoring for papers. Slides can embed scientific-visualization outputs. |

---

## Routing Connector Skills (scope: routing)

These skills are routed to Hermes for routing, integration, and operational coordination.

---

### free-tool-strategy

**Function:** Evaluate and route implementation through cost-effective, available tooling. Tool
landscape analysis, cost-benefit assessment, integration points, vendor lock-in analysis, build-vs-buy
decisions, open-source vs. commercial trade-offs.

**Trigger conditions:**
- Evaluating tools for implementation strategy
- Cost optimization and tooling efficiency
- Build-vs-buy decisions
- Vendor landscape analysis
- Open-source viability assessment
- Consolidation or tool replacement decisions
- Integration and interoperability planning

**Consequence profile:** Medium. Tool choices affect implementation cost, speed, maintenance burden,
and vendor dependency. Poor tool choices create technical debt.

**Typical pairings:**
- Primary (Hermes Connector) → routes implementation through available tools
- Secondary: `architecture` (system design constraints tool selection)
- Secondary: `ai-product` (productionization and scaling constraints)
- philosopher (right-arm): tooling philosophy and design intent alignment
- power-analyst (right-arm): vendor analysis and dependency implications

**Overlap notes:** Free-tool-strategy is connector-primary and focuses on routing through available
tools; architecture focuses on system design; ai-product focuses on productionization. Free-tool-strategy
bridges governance decision and implementation execution through the lens of cost and availability.

---

### genealogy-loupe

**Function:** Hermes-wielded vault genealogy instrument for retracing a work's version
history across genealogy notes, canonical notes, raw files, archive copies, reviewer
responses, editorial sessions, conversation logs, and surviving metadata surfaces.
Separates manuscript from scaffolding, identifies conceptual arrival points, and
recovers what metadata can still be evidenced.

**Trigger conditions:**
- Retracing a work's genealogy across the vault
- Separating manuscript versions from editorial apparatus or archive copies
- Finding the first real version or canonical surviving version
- Identifying where a key term or governing concept becomes load-bearing
- Recovering surviving source-file metadata for a paper, novel, packet, or method note
- Comparing genealogy notes against on-disk source evidence

**Consequence profile:** Medium-high. Misclassification distorts provenance, canonicity,
and the reading of what a work actually is. Weak metadata discipline can falsely
inflate certainty about the archive.

**Typical pairings:**
- Primary (Hermes Connector) → routes the documentary unit through vault surfaces
- Internal lenses: `trace-investigator` for provenance and authority tracing,
  `aesthetic-refinement` for Diamond-Eyes pressure reading
- Secondary: `skill-architect` when the successful genealogy workflow should become
  a reusable note shape or skill refinement
- Escalation path: Queen Keyport if genealogy findings surface governance contradiction;
  HEPHAISTOS if the artifact boundary itself is in dispute

**Overlap notes:** Overlaps with `trace-investigator` on provenance tracing and with
genealogy notes on version history. Distinction: `genealogy-loupe` is connector-primary
and routes a full work packet across vault surfaces while adding Diamond-Eyes pressure
reading and source-metadata recovery. It does not replace Queen Keyport governance.

---

### hermes-dependency-mapper — DROPPED (2026-04-23)

**Status:** Dropped. Function delegated to **`trace-investigator`**, which already 
performs authority-and-accountability-chain tracing across document packs and covers 
the pre-routing dependency-mapping function that `hermes-dependency-mapper` was 
designed for.

**Replaced by:** `trace-investigator` (top-level routable skill). Hermes should invoke 
`trace-investigator` for pre-routing dependency mapping. `architecture` covers 
system-level architectural mapping when the question is about design rather than 
routing safety.

**Historical note:** the skill was registered here but no SKILL.md ever existed on 
disk. Dropped as part of the 2026-04-23 agent ecosystem audit (finding F-019).

---

### hermes-integration-monitor

**Function:** Monitor deployed systems and integration points in real-time. Detect 
deviation from baseline, identify anomalies predicting failure, and trigger escalation 
when governance constraints are at risk in live execution. Ensures routing chains 
remain healthy and governance constraints are honored in live execution.

**On disk:** `/home/martin/.agents/hephaistos/skills/hermes-integration-monitor/SKILL.md` (authored 2026-04-23 per audit F-019; substantive, not a stub). Mirrored to old-host `.codex` mirror (not installed on this host) and registered in settings.json (2026-04-26).

**Trigger conditions:**
- Governance decision has been routed and is executing (Hermes packet status = approve 
  or approve-with-constraints)
- Real-time health tracking of live systems with named constraints
- Constraint-compliance verification at monitored surfaces
- Anomaly or deviation signal surfaced by logs, metrics, user report, or upstream audit
- Periodic health re-check per `routing_requirements.monitoring_metrics`

**Consequence profile:** High. Monitoring quality determines whether constraint 
violations are caught early or cascade undetected. Poor baseline setting causes false 
calm (worse than false alarms). Narrative-reality gaps discovered here route to Argus 
(Layer 3 audit signal).

**Typical pairings:**
- Primary (Hermes agent): live governance-constraint tracking
- Pre-routing complement: `trace-investigator` (maps dependencies before routing; 
  monitor watches the live state after routing)
- Escalation handoff: Hermes agent directly (see HERMES.md / HERMES_OPERATIONS.md — 
  `hermes-escalation-router` was dropped as redundant with the agent's own contract)
- Adjacent: `red-team` (plans failures; monitor watches for them in production)
- Audit handoff: Argus (receives narrative-reality-gap escalations)

**Overlap notes:** `systematic-debugging` handles code bugs; this skill watches 
governance-constraint compliance. `observability-phoenix` is a stub; this skill is 
the real governance-monitor implementation. `codex-review` checks code quality at 
author-time; this skill watches behavior at runtime.

---

### observability-governance

**Function:** Structured logging and trace correlation for governance decisions, agent 
execution, and routing chains. Enables Hermes to route with constraint awareness, 
Queen Keyport to verify bounded claims against execution evidence, Argus to audit 
authority chains, and Trismégiste to maintain operator continuity.

**On disk:** old-host `.codex` path for `observability-governance` (not installed on this host; corpus retired) (authored 2026-05-02, 
production-ready schema with Phase 1-5 roadmap).

**Trigger conditions:**
- Hermes routing decision — what observability rides with this routed work?
- Queen Keyport Bounded/Degraded decision — what execution evidence verifies the boundary?
- Trismégiste session reconstruction — what logs enable "why did we choose this?" 
- Argus authority audit — what provenance chains prove decision correctness?
- Production incident — what execution context enables intelligent escalation?

**Consequence profile:** High. Observability gaps block confident routing and verification. 
Escalations without context force post-hoc reconstruction instead of immediate re-decision. 
Governance effectiveness cannot be verified without execution evidence.

**Three log layers:**
1. Agent Execution Trace — captures decision + constraints + routing target
2. Governance Decision Record — captures Queen Keyport choice + right-arm input + verification
3. Routing & Escalation Log — captures Hermes routing + constraint baseline + deviation signals

**Typical pairings:**
- Primary (Hermes): feeds escalation signals and constraint monitoring requirements
- Primary (Queen Keyport): verification layer (bounded claims checked against execution logs)
- Primary (Trismégiste): session reconstruction (logs answer "why did we decide this?")
- Primary (Argus): authority chain tracing (provenance links Routing → Governance → Execution)
- Feeds: `hermes-integration-monitor` (monitor reads constraint baseline and escalation triggers)
- Validates: `recursive-governance-method` (RGM uses observability as evidence layer)

**Overlap notes:** observability-governance ↔ hermes-integration-monitor — monitor watches 
live constraint violations; observability *structures the evidence* so monitor can decide and 
Hermes can escalate with full context. Observability feeds monitor with log schema and 
escalation triggers. Not competing; complementary (schema supplier → consumer).

---

### incident-response-runbooks

**Function:** Design, test, and execute incident runbooks, post-mortem analysis, and chaos 
engineering patterns. Enables rapid response when routed systems degrade or governance 
constraints are violated. Bridges detection (observability-governance, hermes-integration-monitor) 
and resolution (Queen Keyport re-decision or Operator action).

**On disk:** old-host `.codex` path for `incident-response-runbooks` (not installed on this host; corpus retired) (authored 2026-05-02, 
includes decision trees, recovery procedures, post-mortem framework, and chaos testing).

**Trigger conditions:**
- Escalation signal arrives — what is the runbook for constraint X violation?
- Production incident occurs — what decision tree applies?
- Hermes detects degradation — what are recovery steps before escalating?
- Post-incident review needed — what questions must post-mortem answer?
- Chaos testing planned — what failure scenarios need runbook validation?
- New governance constraint added — what incident scenarios does this enable?

**Consequence profile:** High. Runbook quality determines whether escalations resolve or cascade. 
Poor runbooks force post-hoc reconstruction; good runbooks enable immediate re-decision.

**Three components:**
1. Incident Decision Tree — diagnosis + recovery procedure or escalation
2. Recovery Procedures — tested, rollback-aware steps to restore constraint
3. Post-Mortem Framework — timeline, root cause, corrective actions for Trismégiste memory

**Typical pairings:**
- Primary (Hermes escalation handler): receives escalation signal, executes runbook
- Input: `observability-governance` + `hermes-integration-monitor` (escalation signals)
- Output: Queen Keyport (re-decision point) or Operator (if Operator-executable)
- Memory: Trismégiste (post-mortem captured for session continuity)
- Validation: `red-team` (chaos test scenarios)

**Overlap notes:** incident-response-runbooks ↔ hermes-integration-monitor — monitor detects 
and escalates; runbooks respond. Monitor provides the trigger; runbook provides the response. 
Distinct phases (detection → response), not overlapping.

---

### hermes-escalation-router — DROPPED (2026-04-23)

**Status:** Dropped. Function is already handled by the **Hermes agent itself**, via 
the escalation logic in `HERMES.md §Hephaistos/Queen Keyport Conflict Handling` and 
`HERMES_OPERATIONS.md`. A separate skill would duplicate logic that belongs with the 
agent's bound identity.

**Replaced by:** the Hermes agent's own escalation logic. Load HERMES.md when 
escalation routing is the active question.

**Historical note:** the skill was registered here but no SKILL.md ever existed on 
disk. Dropped as part of the 2026-04-23 agent ecosystem audit (finding F-019).

---

## Skills Registered (Phase 6 & P3.3)

**Phase 6 — Niche & Specialized Skills (5 skills):**

1. `research-grants` — **scope: forging** — Grant writing and funding strategy (routed to HEPHAISTOS)
2. `free-tool-strategy` — **scope: routing** — Tool landscape evaluation and routing (routed to Hermes)
3. `genealogy-loupe` — **scope: routing** — Hermes-wielded vault genealogy instrument for retracing works, separating manuscript from scaffolding, and recovering surviving metadata
4. `observability-governance` — **scope: routing** — Structured logging and trace correlation for governance decisions, enabling confident routing, claim verification, and operator continuity (routed to Hermes)
5. `incident-response-runbooks` — **scope: routing** — Incident response, recovery procedures, and post-mortem analysis (routed to Hermes; post-mortems feed Trismégiste)

**P3.3 — Hermes Operational Skills (3 skills):**

3. `hermes-dependency-mapper` — **scope: routing** — Map system dependencies and fragility before routing
4. `hermes-integration-monitor` — **scope: routing** — Monitor live systems and detect anomalies
5. `hermes-escalation-router` — **scope: routing** — Route escalations to correct authority

**Wave 1 Stage 6 — Core Governance Skills (6 skills):**

These six skills constitute the governance spine of the co-equal authority model.
Designated per `CO-EQUAL-AUTHORITY-DECISION.md`. Without them, governance cannot function.

1. `recursive-governance-method` — **Governance Analysis (Queen Keyport)** — Extracts controls, builds evidence hierarchies, detects governance drift across archives
2. `philosopher` — **Right-Arm, Co-Equal (Conceptual/Normative)** — Conceptual and normative input to governance; binding veto over governance decisions
3. `fully-rounded-power-analyst` — **Right-Arm, Co-Equal (Structural/Operational)** — Structural power mapping; binding veto over governance decisions; co-equal to philosopher
4. `trace-investigator` — **Governance Analysis (Queen Keyport)** — Traces authority, accountability, and term drift across document packs
5. `red-team` — **Governance Validation (Queen Keyport)** — Adversarial stress-test of governance systems and claims
6. `humanize` — **Governance Design (Queen Keyport)** — Converts governance constraints into behaviorally actionable rules across populations

**Wave 2 — Writing and Output Skills (11 active + 5 subsumed stubs):**

Active skills (scope: output):

1. `peer-reviewed-paper-writer` — scholarly manuscripts for peer review
2. `publisher` — long-form manuscript evaluation and publication packaging
3. `novelist` — novel planning, drafting, revision, and critique
4. `scientific-writing` — technical and scientific prose
5. `scientific-visualization` — publication-ready scientific figures and charts
6. `prompt-engineering` — prompt design and optimization (invocable name; hephaistos/skills has variant named `prompt-engineer`)
7. `writing-skills` — general writing quality and craft improvement
8. `naming-analyzer` — naming conventions, semantics, and language precision
9. `scientific-brainstorming` — research ideation and hypothesis generation
10. `speech` — TTS narration, voiceover, and batch speech generation
11. `slides` — presentation slide deck creation and editing (`~/.codex/skills/slides/`)

Subsumed stubs (retained for routing):
- `peer-review` → `peer-reviewed-paper-writer` (academic) / `codex-review` (code)
- `scholar-evaluation` → `recursive-governance-method`
- `scientific-critical-thinking` → `philosopher`
- `literature-review` → `peer-reviewed-paper-writer`
- `deep-research-notebooklm` → `notebooklm` + `recursive-governance-method`

**Wave 2 — Research and Methodological Skills (2 active + 5 subsumed stubs):**

Active skills (scope: research):

1. `qualitative` — **scope: research** — Qualitative method selection, sampling, reflexivity, and research design (`~/.codex/skills/qualitative/` ✓)
2. `senior-data-scientist` — **scope: research** — Senior-level quantitative strategy; absorbs EDA and statistical-analysis as first-class capabilities

Subsumed stubs (retained for routing):
- `exploratory-data-analysis` → `senior-data-scientist`
- `statistical-analysis` → `senior-data-scientist`
- `literature-review` → `peer-reviewed-paper-writer` (writing is Hermes's output scope)
- `research-engineer` → `architecture`

---

## Independent Meta-Governance Audit (Argus)

**Argus** is independent — outside the three-agent hierarchy (HEPHAISTOS / Queen Keyport / Hermes). Peer to HENRY/Gadget; parallel to Trismégiste. Reports directly to the Operator. He is the recursive governance auditor and protective ward. Flag-only authority: findings are recommendations, not mandates. See `argus/argus-contract.md` v1.1 and `argus/argus-manifest.md` v1.2.

| Skill | Scope | Function |
|---|---|---|
| `three-agent-audit` | Independent meta-governance audit | Seven-layer recursive audit of the HEPHAISTOS/Queen Keyport/Hermes stack |
| `ai-governance-workflow` | Argus-adjacent workflow | Staged policy intake, bias and power memo, compliance matrix, framework draft, adversarial review, and rollout brief generation |

**Agent registration:** canonical entrypoint `hephaistos/argus/argus-contract.md` (no Claude-subagent config — PHAROS agents are not subagents; dispatch via universal trigger verbs or scope recognition per root `AGENTS.md`)
**Core documents:** `hephaistos/argus/` (manifest, formation, persona, contract, deployment guide)
**Skill:** `/home/martin/.claude/skills/argus/` (successor to retired `three-agent-audit`; maintenance master per `SKILL-MIRROR-POLICY.md`)
**Adjacent workflow bundle:** `/home/martin/.agents/hephaistos/argus/ai-governance-workflow/` -> live skill target old-host live-skill target (retired; not installed on this host)

**Invocation triggers:**
- "Audit the three-agent stack"
- "Argus, run a light/standard/deep audit"
- "Pressure test [agent]"
- "Map authority chains"

**AND-gate layers:**

| Layer | Lens | Halt condition |
|---|---|---|
| 0 | Stale-Ties Hunter | Extensive dead references |
| 1 | Diamond-Eyes | Coherence failure |
| 2 | Trace-Investigator + Power-Analyst | Authority laundering |
| 3 | Novelist + Playwright | Critical narrative-reality gap |
| 4 | Red-Team | Critical security finding |
| 5 | Skill-Architect | Composition conflict |

**Mercury Protocol:** When auditing systems built with Claude assistance (shared-substrate), Argus marks provenance risk and requires external verification. Elegance in a system's self-presentation is a capture signal, not a quality signal.

**Authority position:** Argus reports findings to Queen Keyport (governance) and the operator (final authority). Argus does not certify, govern, or modify the systems it audits. Remediation requires explicit human approval.

---

## Skills Not In Corpus But Referenced In System

The following skills appear in the execution environment (system-reminder) but
were not found in the ZIP corpus. They may be installed separately or may have
been added after corpus export.

- `fully-rounded-power-analyst` — RESOLVED. Added to `skills/fully-rounded-power-analyst/SKILL.md` and registered as right-arm to Queen Keyport (co-equal with philosopher).
- `philosopher:references:*` — external references not in ZIP but loaded by execution host
- `triangulate` — RESOLVED. Permanently removed. Consolidated into `triangulation`. Removed from settings.json 2026-04-26.

---

## Phantom Skills Resolved (2026-04-26)

11 items found where SKILL-MAP active registrations did not match invocable state. All resolved:

| Item | Issue | Resolution |
|---|---|---|
| `slides` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `codex-hooks` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `peer-review-workflow` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `three-agent-audit` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `ai-governance-workflow` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `genealogy-loupe` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `inner-mind-eye` | SKILL.md in `.codex/skills/`, not in settings.json | Added to settings.json |
| `hermes-integration-monitor` | SKILL.md only in `hephaistos/skills/` (not `.codex/skills/`), not in settings.json | Mirrored to `.codex/skills/`, added to settings.json |
| `agent-management` | SKILL.md only in `hephaistos/skills/` (not `.codex/skills/`), not in settings.json | Mirrored to `.codex/skills/`, added to settings.json |
| `prompt-engineer` | SKILL-MAP name; invocable name is `prompt-engineering` | SKILL-MAP entry renamed to `prompt-engineering` |
| `senior-data-scientist` | SKILL-MAP note said "(no disk directory)"; SKILL.md exists in both locations | Stale note removed from SKILL-MAP |

Additional cleanup: `triangulate` removed from settings.json (deprecated alias). Stale `lead-research-assistant` pairings fixed in `research-grants` and `scientific-brainstorming`.

---

## Vault Intake and Research Tools

### web-scraping (added 2026-05-05)

**Function:** Scrape a URL and write a vault-ready raw source file. Two-layer stack: `requests` + `bs4` + `html2text` (lightrag venv) for static pages; `patchright` headless Chromium (notebooklm venv) for JS-heavy SPAs. Auto-detects which layer is needed. Extracts title, authors, date, description, and body as markdown. Writes to `EMERAULD/raw sources/YYYY-MM-DD_<slug>.md` with YAML frontmatter.

**Triggers:** "scrape", "grab this URL", "save this page to the vault", "pull content from", "add this to raw sources", "scrape the DOI", any URL capture for vault ingestion.

**Path:** old-host `.claude` path for `web-scraping` (not installed on this host)
**Script:** old-host scraper script (not installed on this host)
**Python:** old-host venv python (not present on this host) (requests, bs4, lxml, html2text)
**JS fallback:** old-host notebooklm venv (not present on this host) (patchright v1.55.2, Chromium installed)
**Content types:** academic (arxiv, Springer, Semantic Scholar), regulatory (EU AI Act, Law 25, GC.ca), news/blog, general web.

If extending the corpus, add new skills to `skills/` and register them here.

## Related

- [[Governance and PHAROS MOC]]
- [[HERMES]]
