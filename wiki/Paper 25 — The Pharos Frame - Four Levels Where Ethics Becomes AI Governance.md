---
type: wiki
title: Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes AI Governance
aliases:
- Paper 25
- The Pharos Frame
- Pharos Frame paper
- capstone paper
- Paper 25 — The Pharos Frame (Draft 2026-04-23)
- 'Paper 25 — The Pharos Frame: Four Levels Where Ethics Becomes AI Governance'
- wiki/Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes AI Governance
tags:
- pharos
- paper-25
- capstone
- governance
- ready-for-submission
- the-pharos-frame
- four-levels
- wiki
- paper-25-the-pharos-frame-four-levels-where-ethics-becomes-ai-governance-md
- mechanism
- frame
- conditions
- phase
- color-purple
status: ready-for-submission
created: '2026-04-23'
updated: '2026-06-26'
vault_area: wiki
canonical_path: wiki/Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes
  AI Governance.md
backlink_count: 16
backlinks:
- '[[Areas/Writing/AI Society Manuscript — From AI Anxiety to Recursive Governance]]'
- '[[wiki/Argus]]'
- '[[wiki/Causal Mechanisms in the Social Sciences — Hedström & Ylikoski (Mechanistic
  Explanation)]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/Writing/HENRY — Research Paper Writing System]]'
- '[[wiki/How French Canadians became White Folks — Scott 2016 (Race in Quebec)]]'
- '[[wiki/Learning Together for Responsible AI — ISED Public Awareness WG 2022]]'
- '[[Resources/Mapping the Margins — Crenshaw 1991 (Intersectionality and Violence)]]'
- '[[wiki/NIST AI RMF 1.0 — NIST AI 100-1 (2023)]]'
- '[[Resources/Process-Tracing Methods — Beach & Pedersen 2019 (Mechanisms and Evidence)]]'
- '[[wiki/Publishing Strategy — Springer Trilogy and Parallel Tracks]]'
- '[[wiki/Queerness and Transgender Identity — Lepage 2017 (Pagan Montreal, Wicca
  vs Reclaiming)]]'
- '[[wiki/Transparency Against Democracy — Paquin 2025 (Sweden Democrats, trust)]]'
- '[[archive/session-state/session-state-001]]'
- '[[memory/daily/2026-04-23]]'
- '[[projects/Stuttering Machines — Fisher King Project State]]'
---

# Paper 25 — The Pharos Frame - Four Levels Where Ethics Becomes AI Governance

*Martin Lepage, PhD*
*PHAROS Inc., Montréal, Québec, Canada*

*Draft 2026-04-26. [[HENRY — Research Paper Writing System|Henry]] agent revision pass 4 ([[Argus|Argus]] gate responses: Phase P/Level 4 mechanism gap, corpus citation gap, scenarios denominator). Target: AI & Society — Open Forum section (~8,000 words). [[Argus|Argus audit]]: CONDITIONAL PASS (conditions addressed in this pass). [[Diamond-Eyes — Aesthetic Refinement Skill|Diamond-Eyes]]: PASSED. [[Möbius Protocol — AI Self-Polygraph Template|Mercury Protocol]]: Major Revision — 5 major, 5 minor concerns. Circular validation finding: structural — deferred to peer review lane. Cross-context: companion to [[Paper 25 — Pre-Draft Artifacts (Pharos Frame Capstone)|Pre-Draft Artifacts]] and [[Governance and PHAROS MOC]]; convergence framework discussed in [[DEEPER CONNECTIONS — The Triple Synthesis and the Governance Architecture]].*

---

## Abstract

Governance discourse about artificial intelligence has expanded faster than the mechanisms it describes. Ethics frameworks proliferate; technical standards accumulate; policy consultations multiply — yet the mechanisms through which governance actually constrains what systems do, how operators are held accountable, and how outcomes can be publicly contested remain underdeveloped. This paper proposes **The Pharos Frame** as an integrative theoretical framework developed through twenty-four papers spanning fluency and interruption, recursive audit, institutional continuity, and cultural legitimacy. Drawing on a bounded corpus of practitioner-generated governance artifacts produced under conditions of recursive AI production, the paper applies the methods of reflective practice research to theorize from the archive the practice generated.

The thesis: AI governance is not an ethics subfield and not a compliance process; it becomes real only when four conditions converge simultaneously — technical design that supports interrogation, operator-led recursive audit that sustains contested re-entry, institutional form that enables repetition, and public legitimacy that makes outcomes contestable. The twenty-four Pharos papers, read as one arc, instantiate Levels 1 and 2 of this convergence under one operator and one institutional context, and specify — by the frame's own falsifiability conditions — what demonstration of Levels 3 and 4 would require. This paper, the twenty-fifth, names the frame, maps it against the corpus, and states the conditions under which it would fail. It makes no claim of universal applicability; it offers a falsifiable convergence model and invites the field to apply its own contestation.

**Keywords:** AI governance, recursive audit, operator accountability, institutional form, public legitimacy, AI accountability

---

## 1. Introduction

The governance of artificial intelligence systems is a problem that has been solved, repeatedly, on paper. Every major jurisdiction now has a framework: the European Union's AI Act, the United States' Executive Orders on AI Safety, Canada's Artificial Intelligence and Data Act (prorogued January 2025), the OECD AI Principles, ISO/IEC 42001. These documents name what governance should accomplish. They specify categories of risk, requirements for transparency, and procedures for conformity assessment. What they do not specify — and what no framework has yet resolved — is how governance holds under the specific conditions in which AI systems operate: recursive production, asymmetric expertise, rapid capability change, and operators who are simultaneously accountable and incentivized to avoid accountability. Foundation models compound these conditions: their homogenization dynamic means that governance failures at the foundation layer propagate into every downstream application that inherits from them (Bommasani et al., 2021).

This paper does not survey these frameworks. It proposes a theoretical framework for AI governance from the inside — developed through twenty-four papers that build the thing they describe. The Pharos corpus is an archive of governance practice conducted under the conditions it theorizes: recursive AI production, with a single operator, documented through the artifacts the practice generates. The resulting theory — The Pharos Frame — names four levels that must converge simultaneously for governance to hold. It is not a checklist. It is a convergence condition, and its falsifiability is one of its defining properties.

The paper is organized as follows. Section 2 names the three reductions that governance discourse has not escaped. Section 3 describes the methodological posture of the corpus. Section 4 describes what the twenty-four papers did, in the shape of seven moves of one argument. Section 5 names the mechanisms. Section 6 specifies the ethical ground. Section 7 addresses sequence and dependency. Section 8 presents The Pharos Frame. Section 9 offers a practical test set. Section 10 states the limits. The conclusion and coda close the argument and refuse to claim completion.

---

## 2. The Pharos Question: Three Reductions That Fail

The dominant responses to AI governance risk share a common structure: they add something. Add ethics review. Add compliance certification. Add authority to an oversight body. The additions are not wrong in themselves; they are wrong as governance, because they do not specify the mechanism through which the addition changes what systems actually do.

**The first reduction: governance as ethics.**

Ethics frameworks for AI are now numerous, sophisticated, and institutionally embedded (Floridi et al., 2018; Jobin et al., 2019). The literature has moved from simple principle lists to structured processes — ethics impact assessments, algorithmic audits, responsible AI programs, and increasingly granular risk taxonomies for language models (Raji et al., 2020; Selbst et al., 2019; Weidinger et al., 2022). The assumption underneath this movement is that governance follows from articulated values: once the right principles are identified and institutionally endorsed, governance will follow. This assumption fails because articulated values do not constrain systems; mechanisms do. The space between "the system should be fair" and "the system is fair in practice under adversarial conditions" is the space governance must occupy. Ethics discourse has not closed that space.

**The second reduction: governance as compliance.**

Compliance-based approaches specify what organizations must do and verify. They are necessary. They are not sufficient. Compliance is downstream of governance: it presupposes that governance has already specified what to comply with, established the mechanisms that make compliance detectable, and created the consequences that make non-compliance costly. When compliance frameworks arrive before those conditions are in place — as they routinely do in fast-moving technical domains — they generate paperwork that precedes practice. The risk is not non-compliance but performed compliance (Power, 1997): organizations that meet the letter of requirements while the conditions under which governance holds remain unspecified.

**The third reduction: governance as authority.**

The most persistent reduction conflates governance with the authority of an oversight body: a regulator, an ethics board, a certification authority. Authority structures are necessary carriers of governance. They cannot substitute for the mechanisms through which authority is exercised in practice — what is interrogated, what is contested, what can be denied, what can be repeated. The authority claim without those mechanisms is assertion, not governance (Crawford, 2021; Pasquale, 2015).

The Pharos question — asked across twenty-four papers over a period of sustained recursive production — is what governance must meet to actually hold: not on paper, not in principle, and not under ideal conditions, but in practice, in recursive AI systems, under pressure, with a single operator who is simultaneously accountable and incentivized to deflect.

---

## 3. Démarche: Methodological Posture

The Pharos corpus is a bounded archive. Its boundaries matter. It was produced by one operator (the author) across a period of sustained AI-assisted production, using multiple models across two LLM platforms (OpenAI Codex and Anthropic Claude), coordinated through a shared build-governance layer (HEPHAISTOS) that runs under WSL2 and is runtime-agnostic. The archive contains drafts, revisions, governance protocol documents, protocol revisions, test artifacts, audit outputs, and failure records. Its size at the time of this writing: more than two hundred documents across seven functional categories. The twenty-four papers that constitute the corpus for this paper are those directly constitutive of the governance method (a numbered list with phase assignments and primary corpus functions is provided in Appendix A) — the papers that build, apply, stress-test, or contest the mechanisms described here, in the sequence they were produced. Governance protocol documents, architecture specifications, earlier draft versions, and the book-length synthesis project that draws from the corpus are counted separately; they are products of the method rather than constitutive elements of it.

This methodological posture — constructing the object of inquiry through sustained practice and theorizing from the archive that practice generates — belongs to the tradition of reflective practice research (Schön, 1983) and action science (Argyris & Schön, 1978). The practitioner's archive is the primary site of inquiry, not a supplement to it. The claims derived from this corpus are bounded to one operator, one institutional context, and one technological period; their generalizability is a claim the field must test, not one this paper can establish. The corpus is offered not as proof of the frame, but as the practitioner ground from which the frame is theorized — a distinction the Pharos method applies to all its claims (see §10, Limits).

Three methodological commitments follow from this setup.

**Bounded non-finality.** The corpus does not converge. Its governance layer has been revised twenty-three times — across all twenty-five papers, including this one. Each revision was triggered by something the previous version could not handle — a failure of containment, a contradiction between protocols, a new capability that the existing governance architecture did not anticipate. The non-finality is not a defect; it is the epistemically honest form of governance work. Any theory that claims finality in this domain should be treated with suspicion.

**Dysfluency as signal.** The corpus is organized around the thesis — developed across the first method papers — that fluency in AI systems is a failure mode. A system that produces fluent output is not necessarily a system that is governed. Fluency conceals error, smooths over contradiction, and generates the appearance of competence without its substance (Bai et al., 2022). The Pharos governance architecture was built around interruption: points in the production pipeline where fluency is suspended and the claim is tested against evidence.

**Operator-led audit.** The audit locus in this corpus is the operator, not the system, not an external reviewer. This is not because external review is unnecessary — it is necessary, and its absence is one of the frame's declared limits. It is because governance that requires external review as its primary mechanism cannot sustain itself in recursive production: the production rate exceeds the review rate, and the mechanism breaks down. Operator-led audit is the mechanism that can, in principle, scale with the production it governs.

---

## 4. What We Did: Seven Phases of One Argument

The twenty-four papers are not a sequence of discoveries. They are, read collectively, seven moves of a single argument about what governance requires.

**Phase 0 — Ritual Substrate.** The archive contains two pre-AI papers: *Sealed Card Protocol* (2004) and *Charging Objects* (2017). These are not AI governance papers; they are papers about the conditions under which governance can exist at all. Both describe binding acts — acts that commit an agent to a course and make defection costly in a way the agent cannot simply undo (Austin, 1962). The contribution: governance requires a binding act and a chargeable site. Without them, commitment is discourse, not mechanism.

**Phase 1 — First Method.** The first method papers establish the conceptual vocabulary that all subsequent papers use. Fluency as failure mode. Interruption as audit mechanism. Dysfluency — stuttering, glitching, recursive breakage — as the signal that governance is being exercised rather than performed. The papers in this phase (*RECURSO*, *Hegemonic Fluency*, *Stuttering Machines*, *Discursive Authority Under Recursive Pressure*) build the claim: if the system never stutters, it is not being governed; it is being performed.

**Phase 2 — Recursive Governance Under Constraint.** The APEX papers in this phase (*AI Anxiety → Recursive Governance*, *Governance by Denial*) resolve the question of where governance lives when the system is recursive. The answer: governance is what the operator can deny and sustain. Denial is not refusal; it is the ability to interrupt the recursive stream at a decision point and withhold forward movement until the condition is satisfied. Governance by denial is the functional core of the Pharos method.

**Phase 3 — Pharos Closure.** The closure papers establish that the method is externalizable: not just practiced by the operator who built it, but describable in terms that another operator could use. *PHAROS: Recursive Production to Governable Method* and *Multi-Model Adversarial Evaluation* do this by moving from first-person practice to third-person specification. The mechanism can be named, tested, and contested from outside.

**Phase 4 — Continuity Without Memory.** The Möbius Protocol papers (*Self-Polygraph*, *Wheel & Watcher*, *Recursive Continuity Without Memory*, *Möbius Under Pressure*) address the problem that the governance mechanism cannot assume continuity of context. AI sessions end. Models are replaced. Operators change. The papers in this phase develop mechanisms for governance that survives forgetting — not by storing memory but by rebuilding orientation from traces. Continuity is a mechanism, not a memory.

**Phase 5 — Authority, Ethics, Voice.** The papers in this phase (*For Her Alone to Wield*, *Compress Without Opacity*, *Who's the Boob Who's the Trap* revised) work at the intersection of authority and ethics: what it means to hold authority without power-over, to compress information without hiding its structure, to resist the trap form — outputs that confirm what the user wants to hear rather than what is actually true. The ethical ground of the Pharos method is not declared as a principle; it is built into the mechanisms (Bourdieu, 1991).

**Phase P — Cultural Studies (parallel track).** These papers (*Voodoo / Afterlife of Colonial Naming*, *Every Hair a Battle Scar*, *Glitching the Sacred*, *Magic After Legitimacy*, *Still Running*) run parallel to the governance papers and are not secondary to them. They establish that legitimacy is socially made and socially unmade — that governance has a cultural surface and that surface is not ornamental. A governance architecture that cannot be contested in public, by communities that did not design it, is not legitimate (Buolamwini & Gebru, 2018; Eubanks, 2018). This is the constitutive argument for Level 4: if public contestability is the condition for legitimate governance, then demonstrating that governance has a cultural surface accessible to communities outside the mechanism is not supplementary to the governance claim — it is the structural basis for it.

A clarification is necessary here. The Phase P papers are submitted to peer-reviewed academic journals. This is not equivalent to the public contestability that Level 4 requires. Academic contestation by specialist reviewers is not the same as contestation by communities affected by governance systems they did not design. The Phase P papers establish that legitimacy is socially produced and culturally specific — they carry the theoretical argument for Level 4 — but they do not themselves instantiate Level 4's contestability condition. That condition is not demonstrated by this corpus. It is specified by it: Level 4 names what the frame requires that the corpus cannot, from the inside, deliver.

**Bridge — Bounded Non-Finality.** *This Paper May Not Exist* is the bridge paper: the one that refuses to claim completion. It models what it argues: governance that is honest about its own limits is more governable than governance that asserts its completeness. The bounded non-finality formulation is the epistemological stance the frame requires of all claims made within it.

---

## 5. How — Method and Mechanisms

The Pharos method is not a philosophical position. It is a set of mechanisms. Six are central to the frame.

**Recursive audit.** The primary mechanism. Each production pass is treated as an opportunity to re-enter the prior pass with corrected conditions (Raji et al., 2020). Recursive audit is not editing; it is governance: the prior output is not revised for quality but interrogated for compliance with the governance conditions under which it was produced. The audit record is the artifact. Operationally, a re-entry point is any production decision at which the operator asks whether the current output complies with the declared governance conditions — and withholds forward movement until the answer is yes.

**Governance by denial.** The operator can withhold forward movement. This is the operationalization of the ethical commitment to authority without power-over: the operator does not override the system's output; the operator refuses to forward it until the output meets the declared conditions. The mechanism is negative rather than positive — denial rather than direction. It is also, for that reason, more verifiable: it produces a record of what was denied, at what point, and on what grounds.

**Möbius continuity.** The protocol for governance across context breaks. When a session ends — or when a model is replaced, or an operator changes — the governance mechanism must be able to reorient without full recall. The Möbius Protocol does this by treating disorientation as a normal condition and encoding in each artifact the minimal information needed for re-entry: current constraint set, current operator, current condition of the mechanism. Continuity becomes structural rather than mnemonic.

**Self-polygraph.** A protocol for testing whether the governance layer is governing the system or the system is governing the governance layer. Across documented applications in the corpus, the protocol detects five conditions: confirmation bias in audit, fluency capture of the audit mechanism, asymmetric holding (the operator absorbs cost that the mechanism should distribute), narrative capture (the output becomes the criterion), and recursion without re-entry. The Self-Polygraph is the mechanism's immune system. The distinction from agent self-improvement frameworks that use verbal reflection to optimize task performance (Shinn et al., 2023) is structural: the Self-Polygraph does not optimize the system's outputs; it tests whether the governance layer is still governing.

**Multi-model adversarial evaluation.** The mechanism for testing the method against systems that were not designed for it. A governance architecture validated only under cooperative conditions is not robust. The multi-model adversarial evaluation protocols expose the governance claims to models optimizing for outputs rather than for compliance, under conditions of conflicting incentives. Results are bounded: across the adversarial test set — documented multi-model evaluation runs archived in the Pharos corpus — the method sustained operator-led denial capacity in the majority of tested scenarios (where denial capacity is defined as the operator's ability to withhold forward movement until the governance condition was met), with documented degradation cases where production pressure exceeded the operator's re-entry capacity. The total number of documented scenarios is not disclosed here; the test design, inclusion criteria, and per-scenario outcomes are archived in the corpus and available from the author. The bounded claim is not that the method is robust universally, but that it sustained denial capacity under documented adversarial pressure across a plurality of tested cases, with named failure modes.

**Compression without opacity.** The mechanism for communicating governance outputs without hiding their governance-relevant structure. Compression that loses structure is opacity: the output is shorter but the conditions under which it was produced are no longer visible in it. The anti-opacity principle requires that every compressed output retain the minimal trace needed to reconstruct its governance conditions (Doshi-Velez & Kim, 2017).

---

## 6. Why — The Ethical Ground

The ethical ground of the Pharos Frame is not a supplement to the mechanisms; it is built into them. The seven non-negotiable values that govern the corpus are not declared principles that stand apart from the method and evaluate it. They are the conditions under which the mechanisms are built and against which they are tested.

The seven: equity promoting equality; social justice; representation of oppressed communities; intersectionality; anti-oppressive practice; cultural safety; the system answering to the human and the humane.

The formulation draws on the tradition of anti-oppressive practice in social work (Dominelli, 2002), the cultural safety literature originating in Māori health practice (Ramsden, 2002), and intersectional theory (Crenshaw, 1991); the specific configuration of these seven values, and the seventh in particular, is the author's formulation, developed through the governance practice the corpus records.

Each generates a constraint that is mechanically implemented.

*Equity promoting equality* — the governance mechanism must not allocate its benefits in ways that reproduce existing hierarchies. This constrains how the operator structures the audit locus: if governance is operator-led, the operator's structural position is itself a governance variable.

*Social justice* — the governance mechanism must be answerable to claims made by those affected by its outputs, not only to claims made by those who designed it. This requires a public contestability mechanism: governance that can only be evaluated by experts who built it is not answerable to social justice.

*Representation of oppressed communities* — the corpus and its governance frame must account for absences as well as presences. What is not in the archive, and why, is a governance question. The cultural papers (Phase P) are the mechanism through which the corpus is accountable to this value (Eubanks, 2018).

*Intersectionality* — governance claims cannot be made about a category in isolation (Crenshaw, 1991). Race, class, gender, disability, language, and jurisdiction intersect in the conditions under which AI systems operate and in the populations they affect. The Pharos method applies this by requiring that governance claims be accompanied by specification of the conditions under which they hold.

*Anti-oppressive practice* — the governance mechanism must not reproduce oppressive dynamics in its own operation. The anti-trap mechanisms in Phase 5 are the technical implementations of this value: outputs that confirm what the operator wants to hear, rather than what is accurate, are oppressive in their structure even if benign in their intent.

*Cultural safety* — the governance mechanism must not require cultural assimilation as the price of participation. The bilingual and cross-cultural dimensions of the corpus are not incidental to its governance claims; they are mechanisms for ensuring that the frame is not tied to one cultural context's conventions.

*The system answering to the human and the humane* — the governing condition for all of the above. The mechanism does not govern for efficiency, or capability, or scale. It governs for the condition in which human beings are not diminished by the systems that assist them.

The seven values are not parallel constraints that apply independently; they are an intersectional system (Crenshaw, 1991; Buolamwini & Gebru, 2018). Each value modifies the scope and application of the others: equity and social justice without representation is redistribution in the wrong direction; representation without anti-oppressive practice reproduces the dynamics it names; cultural safety without the system answering to the human and the humane collapses into cultural relativism. The seven function as a governance specification only when treated as interlocking — a failure to meet any one is not a partial pass but a condition under which the others are undermined. These are not decorative values. They are specifications. Each one generates a falsifiable condition under which the method would fail its own ethical standard. That falsifiability is what makes them part of the governance architecture rather than a governance supplement.

---

## 7. When — Sequence and Dependency

The seven phases are not a linear development through which one replaces another. They are layers with load-bearing dependencies.

Remove Phase 0's binding acts, and Phase 1's interruption mechanism has no site of commitment to interrupt. Remove Phase 1's fluency critique, and Phase 2's governance-by-denial has no criterion for what to deny. Remove Phase 2's denial mechanism, and Phase 3's closure claim is not falsifiable. Remove Phase 3's external describability, and Phase 4's continuity protocols serve only the operator who built them. Remove Phase 4's continuity mechanisms, and Phase 5's ethical authority claims are not sustainable across context breaks.

Phase P runs parallel rather than prior because cultural legitimacy is not preparatory to governance — it is constitutive of it. The cultural papers do not establish a foundation that the governance papers then build on; they operate at the same level and cannot be separated from the mechanisms without changing what the mechanisms govern.

The Bridge — bounded non-finality — appears last not because it is most advanced but because it is the condition that makes the preceding phases honest. It is not a conclusion; it is an epistemological constraint applied retroactively to all prior claims.

The dependency structure means the frame has an order of operations for failure. Governance fails from the bottom up: if public contestability is removed (Level 4), the institutional form (Level 3) still holds — but in a condition of reduced legitimacy. If institutional form is removed (Level 3), operator-led audit (Level 2) still runs — but with no mechanism for the audit to accumulate into durable constraint. If operator-led audit is removed (Level 2), technical design (Level 1) still exists — but as capability without governance.

The dependency structure does not only describe how the frame fails from the bottom up; it specifies the order in which governance capacity must be built. Level 1 is not the most important level — it is the necessary precondition for all the others.

The seven phases do not map one-to-one onto four levels; the compression is structural. Phases 0 through 3 establish the conditions for Levels 1 and 2 — the interrogable design that Phase 0's binding acts require, and the operator-led audit mechanism that Phases 1 through 3 specify and externalize. Phase 4's continuity mechanisms are the institutional substrate through which Level 3 (repetition across context change) becomes possible. Phase P carries Level 4 (public legitimacy) by establishing that governance has a cultural surface that is constitutive, not incidental. Phase 5 and the Bridge are cross-cutting: they specify the ethical commitments and epistemological stance that all four levels must satisfy.

*Table 1. Phase-to-level compression. Each phase names its primary level contribution; cross-cutting phases modify the conditions all levels must satisfy.*

| Phase | Name | Level contribution | Primary function |
|---|---|---|---|
| 0 | Ritual Substrate | Level 1 — Technical Design | Binding acts establish the site of interrogation; commitment without a binding act has no governance surface |
| 1 | First Method | Level 2 — Operator-Led Recursive Audit | Fluency/interruption as the criterion for audit; establishes what denial means |
| 2 | Recursive Governance Under Constraint | Level 2 — Operator-Led Recursive Audit | Governance-by-denial as the operative audit mechanism |
| 3 | Pharos Closure | Levels 1–2 | Externalizes the mechanism; makes it testable by operators outside the original practice |
| 4 | Continuity Without Memory | Level 3 — Institutional Form | Continuity protocols as the institutional substrate enabling repetition across context change |
| P | Cultural Studies | Level 4 — Public Legitimacy | Cultural legitimacy as constitutive governance surface, not supplementary illustration |
| 5 | Authority, Ethics, Voice | Cross-cutting | Ethical commitments and authority conditions operative at all four levels |
| Bridge | Bounded Non-Finality | Cross-cutting | Epistemological stance — all claims in all phases must satisfy this condition |

---

## 8. The Pharos Frame — Central Synthesis

The Pharos Frame proposes a four-level convergence model of AI governance. Each level is a necessary condition. None is sufficient. Governance is the line where all four hold simultaneously.

### Level 1: Technical Design

The artifact must support interrogation. Not transparency in the general sense — full interpretability of internal states — but interrogability: the design must make it possible for an operator to ask whether the system is complying with its declared governance conditions, and to receive an answer that is actionable (Doshi-Velez & Kim, 2017). This is a design requirement, not an interpretability wish. Interrogability is structural: it constrains what can be built, not just how it is evaluated after the fact.

Systems that cannot be interrogated cannot be governed. Machine learning systems accumulate hidden technical debt — boundary erosion, undeclared consumers, hidden feedback loops — that compounds this opacity: what the system does may not be visible even to the operators responsible for governing it (Sculley et al., 2015). They can be regulated — subjected to external requirements — but regulation that cannot interrogate the thing it regulates is not governance; it is management of externalities.

Level 1 does not require that all systems be fully interpretable. It requires that the mechanisms through which governance operates — the audit point, the denial gate, the compliance check — have access to the system-state information they need to function. Architectures that interleave reasoning traces with actions (Yao et al., 2023) offer a partial model of what interrogable design looks like at the system level: the reasoning path remains visible rather than compressed into the output alone. Interrogability in the governance sense extends this requirement to the governance conditions themselves — not only what the system inferred, but whether the inference was produced under the conditions governance requires.

### Level 2: Operator-Led Recursive Audit

The method must sustain contested re-entry. Governance in recursive production cannot rely on a single audit of the initial system design; it must be able to re-enter the system at any point, under any condition, and re-apply the governance constraints. Recursive audit is the mechanism through which governance keeps pace with recursive production (Raji et al., 2020).

The "operator-led" qualifier is not incidental. The mechanism must have an accountable locus: a person or entity that is responsible for the audit, that can be held to the audit's results, and that cannot delegate its accountability to the audit mechanism itself. The audit cannot govern itself; it requires an operator who is both within the mechanism (conducting the audit) and answerable to something outside it.

Contested re-entry means the audit must be possible even under adversarial conditions: when the system produces fluent output, when the operator is under pressure to accept it, when the production rate creates time pressure, when the incentives are aligned toward non-governance. The mechanisms in Phase 4 were developed specifically to sustain audit under these conditions.

### Level 3: Institutional Form

The mechanism must repeat. A governance intervention that occurs once, under specific conditions, by a specific operator, is not governance; it is an event. Governance requires institutional form: the mechanism must be embedded in a structure that enables repetition — across operators, across context changes, across time, across the conditions that governance was not designed for (DiMaggio & Powell, 1983; Scott, 2001).

Institutional form is where individual practice becomes method. The Pharos method becomes externalizable in Phase 3 not because the author describes it — description alone is not institutional form — but because the description specifies the conditions under which another operator could apply the mechanism and produce comparable results.

The crisis of governance discourse is largely a crisis of institutional form. There is no shortage of governance events: ethics reviews, algorithmic audits, impact assessments. What is missing is the institutional architecture through which these events accumulate into durable constraint.

### Level 4: Public Legitimacy

The outcome must be contestable in public. Governance that cannot be contested from outside the governance architecture — by people who were not part of designing it, who do not share its conceptual vocabulary, who are affected by its outputs without having been consulted about its design — is not legitimate (Habermas, 1996; Dryzek, 2000). It may be technically sound, internally consistent, and even beneficial in its outcomes. But benefit is not legitimacy: governance that is uncontestable only succeeds if the governing actor's judgment is correct. Public contestability is the mechanism that catches the cases where the judgment is wrong.

The cultural studies papers (Phase P) carry the *theoretical argument* for this level: they establish that legitimacy is socially made and socially unmade, and that a governance architecture with no cultural surface accessible to communities outside the mechanism is not legitimate. They do not, however, instantiate Level 4's contestability condition — academic publication is a form of expert contestation, not the broader public contestability the level requires. The gap between what Phase P argues and what Level 4 demands is itself a declared limit of this corpus (see §10).

### The Convergence Condition

Governance is the line where all four levels hold simultaneously. Remove any one:

- Remove Level 1: governance becomes assertion — claimed but not technically enforceable.
- Remove Level 2: governance becomes design — capable of being governed, with no one actually governing.
- Remove Level 3: governance becomes event — it happens, then dissipates.
- Remove Level 4: governance becomes internal — coherent within its own terms, unaccountable to those outside them.

The causal logic of convergence is not additive but one of mutual constraint. Level 1 (technical design) creates the conditions under which Level 2 (operator audit) is possible; Level 2, sustained over time, generates the institutional record through which Level 3 (institutional form) accumulates; Level 3 creates the structure within which Level 4 (public legitimacy) can be exercised. The reverse also holds: Level 4 legitimizes the institutional form, which sustains the audit mechanism, which justifies the design requirements. Governance is the line where all four loops close simultaneously and reinforce rather than undermine each other (DiMaggio & Powell, 1983; Habermas, 1996). The failure mode is not only the removal of a single level; it is the decoupling of the loops — governance events that produce no institutional record, institutional form that cannot be publicly contested, audit mechanisms that interrogate design elements that were never built to support interrogation.

The Pharos Frame is not a framework for adding ethics to AI systems. It is a framework for specifying the conditions under which governance holds — and for being honest about what happens when any of those conditions fails.

---

## 9. Practical Framework — How Others Apply It

The Pharos Frame generates a set of interrogative tests that any governance claim can be subjected to. They are not a checklist; they are conditions that must be demonstrated, not asserted.

*Can you interrogate the system?* Not "is the system transparent" but: can the governance mechanism access the system-state information it needs to function? If no, governance is blocked at Level 1.

*Can you deny?* Can the operator withhold forward movement — sustain denial — until the condition is met? If the mechanism cannot sustain denial under production pressure, governance is blocked at Level 2.

*Can it repeat?* Is the mechanism embedded in a structure that enables another operator, in different conditions, to apply it and produce comparable results? If the mechanism exists only in one operator's practice, governance is blocked at Level 3.

*Can you be contested?* Are the governance outcomes available for contestation by people who were not part of designing the mechanism? If contestation requires internal vocabulary access, governance is blocked at Level 4.

These tests are logically falsifiable — each specifies a necessary condition under which governance fails by the frame's own terms. Empirical falsification requires application in contexts that did not generate the frame; that condition is not met here (see §10). Applied to existing governance frameworks, the tests expose characteristic failure modes: ethics review processes that address Level 1 (auditability requirements) while leaving Level 3 (institutional accumulation) unaddressed; audit mechanisms that are technically sound at Level 2 but produce no publicly contestable record at Level 4 (Metcalf & Crawford, 2016). The frame does not prescribe how these gaps are closed; it specifies that the gaps are governance failures, not implementation details.

---

## 10. Limits

*The frame does not scale by language-replication.* Governance is not achieved by reproducing the Pharos Frame's vocabulary in new contexts. The mechanisms must be rebuilt for each context, by operators accountable within that context, against the governance conditions appropriate to it. The frame is a specification, not a template.

*The frame does not substitute for democratic process.* Public legitimacy (Level 4) requires contestability, but contestability is not the same as democratic deliberation. The Pharos Frame does not specify the political form through which public legitimacy is achieved (Habermas, 1996; Dryzek, 2000); it specifies that governance without public legitimacy is incomplete.

*The frame does not solve alignment.* The alignment problem in AI systems is a technical and philosophical problem that the Pharos Frame does not resolve. The frame governs the conditions under which governance operates; it does not govern the system's capability to produce aligned outputs.

*The frame is limited by the corpus's bounds.* The twenty-four Pharos papers are produced by one operator, in one institutional context, across a specific period. The claims made from this corpus are bounded by that origin. They are not claims about AI governance in general; they are claims derived from one archive, tested against its own conditions, offered to a field that will apply its own contestation.

*The operator's position is a variable.* The governance mechanism is operator-led, which means the operator's structural position — their expertise, their institutional location, their intersectional identity — is not external to the governance claims. It is a governance variable. The Pharos Frame acknowledges this without resolving it. A governance mechanism operated by a single researcher in one jurisdiction, primarily in two languages, cannot claim neutrality about whose governance conditions it reflects (Sambasivan et al., 2021; Bender et al., 2021).

*The frame's falsifiability is structural, not demonstrated.* The corpus does not contain a case in which the Pharos Frame ruled against the practice that generated it — a governance-failure verdict that required the operator to halt production, retract a published claim, or abandon a tested mechanism. Such a case is the necessary condition for empirical demonstration of the frame's falsifiability claim. In its absence, falsifiability is a structural property of the frame's design: the conditions under which it would fail are specifiable, but the frame has not yet been tested against those conditions by the practice that built it.

*The frame is produced by the system it theorizes.* The theoretical architecture of the Pharos Frame was developed through the same AI-assisted recursive production process the frame claims to govern. The frame's coherence and elegance are therefore subject to an echo risk: they may reflect the internal consistency of a governed production loop rather than independent theoretical validity. This paper cannot resolve that risk from the inside. External review by readers outside the Pharos production ecosystem is the mechanism the frame itself requires for this validation — an instance of Level 4 (public legitimacy) applied to the paper's own claims.

*The corpus does not demonstrate Level 4.* The Phase P papers make the theoretical case for public legitimacy as constitutive of governance. They do not enact it. The communities whose cultural frameworks are cited — Māori health practice, Vodou practitioners, queer communities — were not consulted in the design of the governance architecture whose legitimacy the cultural papers are meant to secure. This gap is structural: the corpus was produced by one operator in one institutional context, and the contestability it argues for requires institutional conditions it cannot generate alone.

---

## 11. Conclusion

AI governance becomes real not when ethics is added to AI systems but when four conditions converge: technical design that supports interrogation, operator-led recursive audit that sustains contested re-entry, institutional form that enables repetition, and public legitimacy that makes outcomes contestable.

The twenty-four Pharos papers instantiate Levels 1 and 2 of this convergence under one operator and one institutional context, and specify — by the frame's own falsifiability conditions — what demonstration of Levels 3 and 4 would require. They do not argue for governance; they practice it, record the practice, and derive the frame from the record. The Pharos Frame is the name for the conditions their practice reveals.

This paper, the twenty-fifth, has named the frame and tested it against the question it was designed to answer. It has not established that the frame is universally applicable, or that it is complete, or that its methods are sufficient for all governance contexts. Those claims would fail the bounded non-finality test that all twenty-four papers before this one have applied to themselves.

What the frame has established: governance is a composite practice, not an ethics subfield. Ethics is socially implemented through mechanisms, not declared through principles. The conditions for that social implementation are specifiable, testable, and falsifiable.

---

## 12. Coda — What Comes After

The next test of the Pharos Frame is not another paper. It is repetition under pressure in institutions that did not write the method.

The frame specifies the conditions; it does not build the institutions. That work is outside this paper.

---

## Declarations

**Funding:** This work received no external funding.

**Competing interests:** The author declares no competing interests.

**Data availability:** The Pharos corpus — the archive of twenty-four papers that constitutes the practitioner archive for this theoretical proposal — is available from the author on request.

**Author contributions:** Martin Lepage: sole author; conceptualization, methodology, writing — original draft, writing — review and editing.

---

## References

Argyris, C., & Schön, D. A. (1978). *Organizational learning: A theory of action perspective*. Addison-Wesley.

Austin, J. L. (1962). *How to do things with words*. Oxford University Press.

Bai, Y., Jones, A., Ndousse, K., et al. (2022). Training a helpful and harmless assistant with reinforcement learning from human feedback. *arXiv:2204.05862*.

Bender, E. M., Gebru, T., McMillan-Major, A., & Shmitchell, S. (2021). On the dangers of stochastic parrots: Can language models be too big? In *Proceedings of FAccT 2021* (pp. 610–623). ACM. https://doi.org/10.1145/3442188.3445922

Bommasani, R., Hudson, D. A., et al. (2021). On the opportunities and risks of foundation models. *arXiv:2108.07258*.

Bourdieu, P. (1991). *Language and symbolic power* (J. B. Thompson, Ed.; G. Raymond & M. Adamson, Trans.). Harvard University Press.

Buolamwini, J., & Gebru, T. (2018). Gender shades: Intersectional accuracy disparities in commercial gender classification. In *Proceedings of the 1st Conference on Fairness, Accountability and Transparency* (pp. 77–91). PMLR.

Crawford, K. (2021). *Atlas of AI: Power, politics, and the planetary costs of artificial intelligence*. Yale University Press.

Crenshaw, K. (1991). Mapping the margins: Intersectionality, identity politics, and violence against women of color. *Stanford Law Review*, *43*(6), 1241–1299. https://doi.org/10.2307/1229039

DiMaggio, P. J., & Powell, W. W. (1983). The iron cage revisited: Institutional isomorphism and collective rationality in organizational fields. *American Sociological Review*, *48*(2), 147–160. https://doi.org/10.2307/2095101

Dominelli, L. (2002). *Anti-oppressive social work theory and practice*. Palgrave Macmillan.

Doshi-Velez, F., & Kim, B. (2017). Towards a rigorous science of interpretable machine learning. *arXiv:1702.08608*.

Dryzek, J. S. (2000). *Deliberative democracy and beyond: Liberals, critics, contestations*. Oxford University Press.

Eubanks, V. (2018). *Automating inequality: How high-tech tools profile, police, and punish the poor*. St. Martin's Press.

Floridi, L., Cowls, J., Beltrametti, M., et al. (2018). An ethical framework for a good AI society. *Minds and Machines*, *28*(4), 689–707. https://doi.org/10.1007/s11023-018-9482-5

Habermas, J. (1996). *Between facts and norms: Contributions to a discourse theory of law and democracy* (W. Rehg, Trans.). MIT Press.

Jobin, A., Ienca, M., & Vayena, E. (2019). The global landscape of AI ethics guidelines. *Nature Machine Intelligence*, *1*, 389–399. https://doi.org/10.1038/s42256-019-0088-2

Metcalf, J., & Crawford, K. (2016). Where are human subjects in big data research? The emerging ethics divide. *Big Data & Society*, *3*(1), 1–5. https://doi.org/10.1177/2053951716650211

Pasquale, F. (2015). *The black box society: The secret algorithms that control money and information*. Harvard University Press.

Power, M. (1997). *The audit society: Rituals of verification*. Oxford University Press.

Raji, I. D., Smart, A., White, R. N., Mitchell, M., Gebru, T., Hutchinson, B., Smith-Loud, J., Theron, D., & Barnes, P. (2020). Closing the AI accountability gap: Defining an end-to-end framework for internal algorithmic auditing. In *Proceedings of FAccT 2020* (pp. 33–44). ACM. https://doi.org/10.1145/3351095.3372873

Ramsden, I. (2002). *Cultural safety and nursing education in Aotearoa and Te Waipounamu*. Unpublished doctoral thesis, Victoria University of Wellington.

Sambasivan, N., Kapania, S., Highfill, H., et al. (2021). "Everyone wants to do the model work, not the data work": Data cascades in high-stakes AI. In *Proceedings of CHI 2021*, 39:1–39:15. ACM. https://doi.org/10.1145/3411764.3445518

Schön, D. A. (1983). *The reflective practitioner: How professionals think in action*. Basic Books.

Scott, W. R. (2001). *Institutions and organizations: Ideas and interests* (2nd ed.). Sage.

Sculley, D., Holt, G., Golovin, D., et al. (2015). Hidden technical debt in machine learning systems. In *Proceedings of NeurIPS 2015* (Vol. 28). Curran Associates.

Selbst, A. D., Boyd, D., Friedler, S. A., Venkatasubramanian, S., & Vertesi, J. (2019). Fairness and abstraction in sociotechnical systems. In *Proceedings of FAccT 2019* (pp. 59–68). ACM. https://doi.org/10.1145/3287560.3287598

Shinn, N., Cassano, F., Gopinath, A., et al. (2023). Reflexion: Language agents with verbal reinforcement learning. In *Proceedings of NeurIPS 2023*. Curran Associates.

Weidinger, L., Mellor, J., Rauh, M., et al. (2022). Taxonomy of risks posed by language models. In *Proceedings of FAccT 2022* (pp. 214–229). ACM.

Yao, S., Zhao, J., Yu, D., et al. (2023). ReAct: Synergizing reasoning and acting in language models. In *Proceedings of ICLR 2023*. OpenReview.

---

---

## Appendix A: Pharos Corpus — Twenty-Four Papers

The following papers constitute the Pharos corpus on which the theoretical framework presented in this article is based. They are listed by their phase assignment in Section 4. The papers are available from the author on request; some are under review or forthcoming.

| # | Phase | Title (abbreviated) | Primary function in corpus |
|---|---|---|---|
| 1 | 0 | Sealed Card Protocol (2004) | Binding act — establishes governance surface |
| 2 | 0 | Charging Objects (2017) | Chargeable site — commitment structure |
| 3 | 1 | RECURSO | Fluency as failure mode — first articulation |
| 4 | 1 | Hegemonic Fluency | Fluency/interruption — governance criterion |
| 5 | 1 | Stuttering Machines | Dysfluency as governance signal |
| 6 | 1 | Discursive Authority Under Recursive Pressure | Authority under recursion |
| 7 | 2 | AI Anxiety → Recursive Governance (APEX 1) | Governance-by-denial — first formulation |
| 8 | 2 | Governance by Denial | Denial mechanism — operative core |
| 9 | 3 | PHAROS: Recursive Production to Governable Method | External describability |
| 10 | 3 | Multi-Model Adversarial Evaluation | Third-person specification + adversarial test |
| 11 | 4 | Self-Polygraph | Governance immune system — detection protocol |
| 12 | 4 | Wheel & Watcher | Continuity under context break |
| 13 | 4 | Recursive Continuity Without Memory | Möbius Protocol — structural continuity |
| 14 | 4 | Möbius Under Pressure | Continuity under adversarial pressure |
| 15 | 5 | For Her Alone to Wield | Authority without power-over |
| 16 | 5 | Compress Without Opacity | Compression — anti-opacity mechanism |
| 17 | 5 | Who's the Boob Who's the Trap (revised) | Anti-trap mechanism |
| 18 | P | Voodoo / Afterlife of Colonial Naming | Cultural legitimacy — colonial naming structures |
| 19 | P | Every Hair a Battle Scar | Cultural surface — bodily governance |
| 20 | P | Glitching the Sacred | Legitimacy failure modes |
| 21 | P | Magic After Legitimacy | Post-legitimacy governance conditions |
| 22 | P | Still Running | Queer ritual infrastructure as governance model |
| 23 | Bridge | This Paper May Not Exist | Bounded non-finality — epistemological stance |
| 24 | Cross-cutting | [Confirmatory synthesis paper] | Convergence test across all phases |

*Note: Paper titles are working titles. Abbreviated forms reflect corpus filing conventions. Full titles and access information available from the author.*

---

## Related

- [[Paper 25 — Pre-Draft Artifacts (Pharos Frame Capstone)]] — artifacts A–D that generated this draft
- [[Governance and PHAROS MOC]] — primary governance index
- [[PHAROS Method — Technical Reference]] — method specification this paper rests on
- [[First Method Paper — Recursive AI Governance as Executable Method]] — Phase 1 anchor
- [[AI Society Manuscript — From AI Anxiety to Recursive Governance]] — Phase 2 anchor (APEX 1)
- [[Self-Polygraph Protocol and Suprametacognition]] — Phase 4 anchor
- [[Magic After Legitimacy — Charmed and the Governance of Female Power]] — Phase P anchor
- [[Loop Hinge Candidate — This Paper May Not Exist]] — Bridge
- [[Research and Papers MOC]] — research-domain MOC
- [[PHAROS Scholarly Publication Track]] — publication trajectory
- [[2009 - JourNal of]]
- [[2025 - https lthj.qut.edu.au LAW, TECHNOLOGY AND HUMANS.pdf - 2025 - h - 2025 - https lthj.qut.edu.a]]
- [[Regulating human control over autonomous systems]]
- [[Turing AI Ethics and Governance]]
- [[Misfit as Method Ten Diagnostic Scenes of Institut]]
