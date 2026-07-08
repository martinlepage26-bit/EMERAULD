---
type: artifact
title: Very Long Narrative — Section-by-Section GPT Rewrite Prompts (2026-04-21)
aliases:
- assets/Very Long Narrative — Peer Review and GPT Rewrite Prompts 2026-04-21
tags:
- artifact
- assets
- very-long-narrative-peer-review-and-gpt-rewrite-prompts-2026-04-21-md
- prompt
- todo
- section
- rewritten
- author
- color-purple
status: active
created: '2026-04-21'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/Very Long Narrative — Peer Review and GPT Rewrite Prompts 2026-04-21.md
backlink_count: 1
backlinks:
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
about: 'Section-by-section GPT rewrite-prompt pack for the Apr 21 2026 Google Doc
  rewrite of "Recursive AI Governance as Executable Method: The Very Long Narrative."
  One prompt per section.'
source-doc-id: 1T4Y75b4VcYKYhBfPKMW6Fh33DvRRDStwxxCzUfUXzeU
source-doc-url: https://docs.google.com/document/d/1T4Y75b4VcYKYhBfPKMW6Fh33DvRRDStwxxCzUfUXzeU/edit
related: '[[Recursive AI Governance as Executable Method — The Very Long Narrative]],
  [[Recursive AI Governance Very Long Narrative — Version Genealogy]], [[First Method
  Paper — Recursive AI Governance as Executable Method]]'
---

# Very Long Narrative — Section-by-Section GPT Rewrite Prompts (2026-04-21)

## How to use

1. Run **Prompt 0 (Setup)** once at the start of the GPT session. It locks voice, evidence discipline, and bounded-claim rules for every following turn.
2. Run **Prompts 1 → 16** in order, one per section. Each prompt:
   - Names the section being rewritten
   - States the diagnosed weakness specific to that section
   - Gives the rewrite target with concrete constraints
   - Tells GPT to output only the rewritten section, ready to drop in
3. After Prompt 16, run **Prompt 17 (Integration)** to merge and audit cross-references.

Paste the relevant section of the current draft along with each prompt. The current draft is the Google Doc at `1T4Y75b4VcYKYhBfPKMW6Fh33DvRRDStwxxCzUfUXzeU`.

---

## Prompt 0 — Session setup (run once)

> You are a senior peer reviewer and academic editor in AI governance, science and technology studies (STS), and qualitative methods. The author is Martin Lepage, PhD, an AI governance researcher building a method called PHAROS. He has a manuscript titled *"Recursive AI Governance as Executable Method: The Very Long Narrative."* You will revise it section by section across the next 17 turns.
>
> **Hard constraints, applied to every section:**
> 1. **Genre.** Empirical archival method paper for an AI-governance / STS journal. Not manifesto, not memoir, not internal documentation.
> 2. **Evidence.** Every substantive claim must cite literature, name a corpus item, or be labeled *interpretation*. No floating assertions.
> 3. **Bounded claims.** Use *suggests / indicates / was observed in this corpus*. Drop *only / always / finally / the architecture demands*.
> 4. **Glossary discipline.** Every archive-native proper noun (Sakura, Sealed Card, Violet Gem, ALAMBIC, AIGOV, Voice Operator, Recurso, RECURSUS, Hephaistos, Hexa, Wheels of Will, etc.) must be either defined operationally on first use, replaced with a generic term, or cut.
> 5. **No charm.** Cadence does not buy authority. Strip rhetorical flourishes that do not carry verifiable claims.
> 6. **Voice.** Third-person academic. Past tense for empirical observations, present tense for conceptual claims.
> 7. **Length.** Restore the substance lost from the v3 .docx (11,957 words). Target final manuscript: 8,000–11,000 words.
> 8. **Honest gaps.** Where a fact is unknown, write `[TODO: author to supply]`. Do not fabricate.
>
> Acknowledge the constraints. I will then send one section at a time.

---

## Prompt 1 — TITLE

> **Section:** Title.
>
> **Current state:** *"# Recursive AI Governance as Executable Method: The Very Long Narrative"* — leading `# ` is a markdown leakage from the paste. Title is also ambiguous about the genre (is this a narrative? a method paper? a manifesto?).
>
> **Rewrite target:**
> 1. Drop the leading `# `.
> 2. Add a subtitle that names the empirical contribution and signals it is bounded.
> 3. Two candidates to choose from, or propose a third:
>    - *Recursive AI Governance as Executable Method: An Archival Reconstruction of One Bounded Corpus*
>    - *From Recursive Production to Governable Method: Archival Evidence from the PHAROS Corpus*
>
> **Output:** the recommended title, plus two alternatives, plus one sentence per option explaining the trade-off.

---

## Prompt 2 — ABSTRACT

> **Section:** Abstract.
>
> **Current state:** ~210 words. Frames the paper as both descriptive method history and analytic contribution. Central claim — *"the archive stabilized only after governance was internalized, protocolized, and distributed through a managed skill ecosystem enforced by a shared forge layer"* — is unfalsifiable as written. Three contributions are listed (descriptive, analytic, field-level) but compressed.
>
> **Rewrite target:** 200–250 words covering, in order:
> 1. **Object** (one sentence): what is being studied — the PHAROS archive, what it contains.
> 2. **Problem** (one sentence): why governance under recursive AI production is hard.
> 3. **Method** (two sentences): bounded archival reading; corpus size; selection rule; analytic procedure.
> 4. **Findings** (two to three sentences): bounded, falsifiable, tied to corpus evidence. Rewrite the central claim so a reviewer could in principle disagree with it.
> 5. **Contribution** (one sentence): what this paper offers a non-PHAROS reader.
> 6. **Limitations** (one sentence): single-author corpus, archive-native terminology, no counterfactual.
>
> Avoid the words *only*, *finally*, *demands*, *insists*. Use *this study suggests*, *the corpus indicates*, *was observed across N revisions*.
>
> **Output:** the rewritten Abstract, ready to drop in.

---

## Prompt 3 — INTRODUCTION

> **Section:** Introduction.
>
> **Current state:** Three paragraphs. Frames recursive AI production crossing a "trust-scaling threshold" and positions the paper as method history. Asserts the archive became "book-scale" without quantifying. Last paragraph asserts the central thesis without preview of evidence.
>
> **Rewrite target:**
> 1. **Paragraph 1 — phenomenon.** Open with the empirical phenomenon: recursive AI-assisted production at sustained pace. Cite at least one source (e.g., Bommasani 2021 on foundation-model reuse, or Sambasivan 2021 on data cascades) showing this is a recognized class of problem.
> 2. **Paragraph 2 — gap.** State the residual gap left by external governance frameworks (NIST AI RMF, EU AI Act), sociotechnical risk work (Weidinger 2022/2023), and agentic-recursive methods (Constitutional AI, ReAct, Reflexion, Self-Refine). One short sentence per strand. Then: what those strands do not yet handle.
> 3. **Paragraph 3 — this paper.** State precisely what this paper does: an archival reconstruction of one bounded corpus (the PHAROS archive) that documents how a particular control architecture co-evolved with output volume. Name the unit of analysis. Quantify the corpus (use `[TODO]` if unknown).
> 4. **Paragraph 4 — preview.** One sentence each previewing: method, key finding (bounded), contribution, what the paper does *not* claim.
>
> Drop "trust-scaling question" and "the architecture demanded a book-scale form" — both are manifesto register.
>
> **Output:** the rewritten Introduction.

---

## Prompt 4 — CORPUS AND METHOD

> **Section:** Corpus and Method.
>
> **Current state:** One paragraph asserting "close archival reading of a bounded corpus" without operationalization. Names internal labels (AIGOV, Voice Operator, Sakura, Sealed Card, Hephaistos) without definition. Acknowledges archive-native terminology in passing.
>
> **Rewrite target:** A full Methods section with the following six subsections:
>
> 1. **Corpus boundary.** Document count, document types (drafts, revisions, protocol artifacts, wiki notes, code, build manifests), date range, language(s). Use `[TODO]` for unknowns.
> 2. **Selection rule.** Inclusion / exclusion criteria. What counts as a *PHAROS method document* vs. adjacent creative material vs. infrastructure file.
> 3. **Coding scheme.** The categories already implicit in the draft (fluency, governance, body-cost, return, implementation, stress-testing). For each, an operational indicator an outside reader could apply.
> 4. **Analytic procedure.** How transitions across versions were identified (diff between V_n and V_{n+1}, timestamp ordering, manifest fingerprints). How patterns were aggregated. How confidence was assigned.
> 5. **Reflexivity.** The author is the producer of the corpus. State this explicitly. Describe what mitigates conflict of interest (version control, archive timestamps, third-party tooling traces, runtime-agnostic build layer across two LLM platforms).
> 6. **Limitations of method.** Single-coder, single-author corpus, no external validation, archive-native terminology, no counterfactual archive without recursive governance.
>
> **Output:** the rewritten Corpus and Method section as six numbered subsections.

---

## Prompt 5 — LITERATURE REVIEW (parent + three subsections)

> **Section:** Literature Review (introduction + three subsections: *External Governance, Documentation, And Audit*; *Foundation Models And Sociotechnical Risk*; *Agentic And Recursive Methods*).
>
> **Current state:** Real, current citations engaged correctly (NIST AI RMF, EU AI Act, OECD, Gebru, Mitchell, Raji, Sculley, Sambasivan, Bommasani, Bender, Weidinger, Bai, Schick, Yao, Shinn, Madaan). But each strand is summarized rather than steelmanned, and the gap claim — *"rarely treats governance itself as something that must recurse"* — is asserted, not argued.
>
> **Rewrite target:**
>
> 1. **Parent intro paragraph.** Name the three strands and state, in one sentence each, what gap each leaves under conditions of sustained recursive production. Tee up the contribution.
>
> 2. **§ External Governance, Documentation, And Audit.**
>    - Steelman: state the strongest version of what this strand achieves (lifecycle risk management, accountability artifacts, internal audit pipelines).
>    - Sharpen the gap: under what specific decisions does external oversight not reach? Use Sculley 2015 and Sambasivan 2021 to argue that governance failures accumulate at interfaces and handoffs that external review rarely inspects.
>
> 3. **§ Foundation Models And Sociotechnical Risk.**
>    - Steelman: Bommasani on capability + defect propagation, Bender on grounded understanding, Weidinger on sociotechnical safety evaluation.
>    - Sharpen the gap: this literature shifts the unit of analysis but the dominant response is *evaluation*, which is post-hoc. Argue precisely why post-hoc evaluation does not reach decisions made during recursive production.
>
> 4. **§ Agentic And Recursive Methods.**
>    - Steelman: Constitutional AI (principles + AI feedback), Toolformer (tool use), ReAct (reasoning + acting), Tree of Thoughts (deliberate search), Reflexion (verbal reinforcement), Self-Refine (self-feedback).
>    - Sharpen the gap: these methods internalize feedback for *task performance, interpretability, or harmlessness*. They do not internalize feedback for *governance*. Distinguish self-refinement from governance-refinement.
>
> 5. **Add adjacent literatures the current draft misses.** Cite only what you can verify:
>    - Suchman on situated action
>    - Star & Bowker on infrastructure and classification
>    - Latour on inscription
>    - Pasquale on the black-box society
>    - Crawford on the political atlas of AI
>    - ISO/IEC 42001 (AI management system standard)
>    - IEEE 7000-series (ethics in system design)
>
> 6. **Closing paragraph.** Position the present study modestly: it does not close the gap; it documents one bounded archive in which a particular control architecture attempts to operate inside the gap.
>
> **Output:** the rewritten parent intro + three subsections + closing paragraph, with all citations preserved and the new ones inserted only where they actually fit.

---

## Prompt 6 — THE ARCHIVE AS CLASSES

> **Section:** The Archive As Classes.
>
> **Current state:** Two paragraphs. Names six classes (fluency, governance, body-cost, return, implementation, stress-testing) and asserts that body-cost runs through the archive as exchange currency. The body-cost framing is evocative but undefended; risks reading as memoir.
>
> **Rewrite target:**
> 1. Convert this section into the **opening of the Results section** (rename if needed: *§ Results: Document Classes in the Corpus*).
> 2. For each of the six classes, state:
>    - **Definition** (one sentence, operational).
>    - **Indicator** (what document-level feature triggers classification).
>    - **Corpus count** (how many documents fall in this class — use `[TODO]` if unknown).
>    - **Example** (one named document, dated).
> 3. Treat *body-cost* with discipline: present it as a class observed in the corpus (titles like *Hair as Battle Scar*, *Stutter Through Institution*, *Transmutation of the Body*), not as a metaphysical claim about method. The evidence is the documents.
> 4. Cut the line *"This is not a disembodied theory of method. It is a method with a toll."* — manifesto register.
>
> **Output:** the rewritten section as a structured table-or-list, plus a short interpretive paragraph at the end.

---

## Prompt 7 — IGNITION AND LABORATORIES

> **Section:** Ignition And Laboratories.
>
> **Current state:** Three paragraphs. Names *The Witch's Road* and *Agatha All Along* as "epistemic ignition," then *Hexa* and *Wheels of Will* as "laboratories." Lists ~15 archive-internal titles (CORPUS, Broken Frequency, Sixth Signal, etc.) without defining them. Introduces first-order diagnostic vocabulary (Charge, Glitch, Stutter, Boobytrap, Traversal) without operationalization.
>
> **Rewrite target:**
> 1. Reframe as **§ Results: Origins of the Diagnostic Vocabulary**.
> 2. State the empirical observation: in the corpus, a set of diagnostic terms (Charge, Glitch, Stutter, Boobytrap, Traversal) appear first in early documents and then propagate to later governance artifacts.
> 3. For each term, give:
>    - **Operational definition** (what failure mode or signal it names).
>    - **First appearance** (document, date).
>    - **Subsequent uses** (count, or `[TODO]`).
> 4. Drop the cultural-reference language ("Witch's Road," "Agatha All Along," "epistemic ignition") from the body of the Results section. If they matter biographically, move them to a one-paragraph **§ Background** before Methods, framed as the intellectual context in which the diagnostic vocabulary first appeared.
> 5. Do not list 15+ document titles in running prose. Move the document inventory to a **Table 1** or to the appendix. Cite individual documents only when they support a specific claim.
>
> **Output:** the rewritten section, plus the proposed Table 1 (Document Inventory) as a markdown table.

---

## Prompt 8 — CONTAINMENT AND RECURSIVE REVISION

> **Section:** Containment And Recursive Revision.
>
> **Current state:** Three paragraphs. Introduces AIGOV 1, Voice Operator 1, then Recurso, RECURSUS, AIGOV 2, Voice Operator 2 — and asserts these together produced "the first coherent control envelope" and later "recursive method maintenance." Lists derivative texts (Stuttering Machines, Embedding Before Rupture, Misfit as Method, etc.).
>
> **Rewrite target:**
> 1. Reframe as **§ Results: Emergence of an Internal Control Layer**.
> 2. Open with the empirical observation: the corpus contains two governance documents (AIGOV 1, AIGOV 2) and two voice-discipline documents (Voice Operator 1, Voice Operator 2). Date their first appearance and revisions.
> 3. Define each document operationally on first mention:
>    - **AIGOV 1 / AIGOV 2** — what they specify (governance constraints, evidence thresholds, approval gates).
>    - **Voice Operator 1 / Voice Operator 2** — what they specify (voice discipline rules, claim-integrity constraints).
>    - **Recurso** — name for the observed pattern of outputs revising the conditions of future outputs.
>    - **RECURSUS** — the bounded corpus and trace structure used to make Recurso observable.
> 4. Present the empirical pattern: revisions to AIGOV and Voice Operator over time correlate with the appearance of new derivative texts. Show this as a small table (revision date → derivative text appearing within N days).
> 5. State the bounded interpretive claim: the corpus *suggests* that internalizing governance into the recursive stream changed the distribution of derivative outputs. Do not claim this proves causation. Acknowledge the alternative interpretation (selection bias: the author may simply have produced more derivative texts during periods of active method work).
>
> **Output:** the rewritten section, plus a small revision-correlation table.

---

## Prompt 9 — PROTOCOL STACK

> **Section:** Protocol Stack.
>
> **Current state:** Two paragraphs. Names a five-layer stack (Sakura → Sealed Card → Violet Gem → ALAMBIC → Master Key) and assigns each a function (pre-threshold, threshold, carriage, transformation, explainer). Asserts that the stack solves a "handoff problem" but provides no failure case it caught.
>
> **Rewrite target:**
> 1. Reframe as **§ Results: Protocolization Layer**.
> 2. Introduce the stack as an empirical artifact in the corpus: five protocol documents, dated, with their stated functions.
> 3. For each layer, give:
>    - **Generic-equivalent name** in parentheses (e.g., *Sakura (pre-threshold sensing protocol), Sealed Card (threshold gating protocol), Violet Gem (context-and-constraint carriage protocol), ALAMBIC (lawful-amendment protocol), Master Key (method-readable explainer protocol)*).
>    - **Operational definition** (one sentence).
>    - **Inputs / outputs** (what the protocol takes and produces).
>    - **Audit trail** (how compliance is checked).
> 4. **Worked example.** Walk through one concrete passage of an artifact through the stack — `[TODO: author to supply specific case]` — showing what each layer did and what evidence was logged.
> 5. Cut the line *"This is the moment when the method stops being a set of written commitments and becomes an executable control architecture"* — claim made in the absence of a worked example.
>
> **Output:** the rewritten section, plus the worked-example slot marked `[TODO]` for the author.

---

## Prompt 10 — DISTRIBUTION AND SKILL GOVERNANCE

> **Section:** Distribution And Skill Governance.
>
> **Current state:** Three paragraphs. Introduces *skill-architect* as the constitutional layer of a skill ecosystem. Lists workflow controls (Henry, Reviewer #2, Governess Agatha) and application surfaces (Lotus, Flowerapp, Scriptorium, Dr. Sort, ECHO, Voice11, CompassAI, AuroraI, Govern-AI/PHAROS). Lists DOTTIE, fourteen standalone skills, pairing skill, Mobius Protocol, Mobius GPT. Closes with an ethical claim ("voluntary recursion") and three application papers as "control cases."
>
> **Rewrite target:**
> 1. Reframe as **§ Results: Distributed Governance Through Skills**.
> 2. Open with the empirical observation: the corpus contains N governed-skill artifacts, distributed across M execution surfaces. Define a *skill* operationally: a bounded execution unit constrained by skill-architect's routing, inheritance, and conflict-resolution rules.
> 3. Move the long inventory (Henry, Reviewer #2, Governess Agatha, DOTTIE, Mobius, Lotus, Flowerapp, Scriptorium, Dr. Sort, ECHO, Voice11, CompassAI, AuroraI, Govern-AI / PHAROS, etc.) to **Table 2 — Skill and Application Inventory** in the appendix. In the body, cite only skills that support a specific claim.
> 4. **Worked example.** One concrete trace: a single skill being routed under skill-architect, showing inputs, constraints, audit trail, and outcome. `[TODO: author to supply]`.
> 5. Recast *"voluntary recursion"* and *"the deliberate choice to make augmentation answer to human formation rather than human replacement"* as a clearly labeled **interpretation** at the end of the section, not as method evidence.
> 6. Drop the assertion that *Pourquoi rever encore, Why Be King, For Her Alone to Wield* are "control cases" unless you can show the protocol that made them control cases.
>
> **Output:** the rewritten section, plus Table 2 in the appendix, plus the worked-example slot marked `[TODO]`.

---

## Prompt 11 — HEPHAISTOS AND BUILD TRUTH

> **Section:** Hephaistos And Build Truth.
>
> **Current state:** Three paragraphs. Introduces Hephaistos as a "shared forge/build governance layer," WSL-mediated, runtime-agnostic across Codex and Claude. Lists what it enforces (one build root, source provenance, manifest coherence, validator coherence, collision-safe evidence handling, canonical status semantics, no false readiness claims). Asserts that build coherence failure equals method legitimacy failure.
>
> **Rewrite target:**
> 1. Reframe as **§ Results: Build-Layer Governance Enforcement**.
> 2. Define Hephaistos operationally: a build-time enforcement layer, executed under WSL, applied uniformly across two LLM execution contexts (OpenAI Codex and Anthropic Claude). Cite what makes it cross-runtime.
> 3. Enumerate enforced invariants as a structured list, each with:
>    - **Invariant name** (e.g., *single build root*, *manifest coherence*, *collision-safe evidence handling*).
>    - **What it prevents** (the failure mode it catches).
>    - **How it is checked** (validator, manifest fingerprint, runtime probe).
> 4. **Worked failure case.** One concrete instance in which Hephaistos caught a governance failure that policy alone would have missed. `[TODO: author to supply]`. Without this example, the section's central claim — that build coherence equals method legitimacy — is unsupported.
> 5. Add a one-sentence acknowledgment: cross-runtime enforcement reduces platform-specific bias but does not eliminate platform-specific failure modes that affect both runtimes equivalently.
> 6. Cut *"That is method proof, not method rhetoric."* — rhetorical figure asserting what it should demonstrate.
>
> **Output:** the rewritten section, plus the worked-failure-case slot marked `[TODO]`.

---

## Prompt 12 — THREE-ORDER LOGIC

> **Section:** Three-Order Logic.
>
> **Current state:** Two paragraphs. Asserts a three-order architecture (first order = signal/instability; second order = condensation into executable control; third order = continuity and bounded non-convergence) and a six-step behavioral spine (compose → conform → comply → adjust → adapt → align). Both are introduced without theoretical grounding or prior cite.
>
> **Rewrite target:**
> 1. Reframe as **§ Discussion: A Three-Order Reading of the Corpus**. This is interpretation, not result. Move it accordingly.
> 2. Ground the three-order framing. Cite at least one source that uses similar layered reasoning (e.g., systems-theoretic levels of analysis, Star & Bowker on infrastructure, Suchman on situated action). State that the three-order reading is one possible interpretive frame, not the only one.
> 3. For each order, give:
>    - **Definition** (one sentence).
>    - **Corpus evidence** (which documents from the Results section instantiate this order).
>    - **Limitation** (what this order does not address).
> 4. **Worked example for each order.** Take one artifact from the corpus (e.g., AIGOV 2, ALAMBIC, Hephaistos) and show how it reads at each of the three orders. `[TODO: author to supply specific artifact for each order]`.
> 5. Recast the six-step behavioral spine (compose → conform → comply → adjust → adapt → align) as a **proposed analytic vocabulary**, not as an asserted property of the method. Acknowledge that the steps are not strictly sequential; they describe modes of engagement that recur.
> 6. Drop *"This is not overcomplication."* — defensive register.
>
> **Output:** the rewritten Discussion subsection, plus the worked-example slots marked `[TODO]`.

---

## Prompt 13 — RETURN MAP AND LOOP PAPERS

> **Section:** Return Map And Loop Papers.
>
> **Current state:** Three paragraphs. Introduces a return-map vocabulary (stutter → dissonance → hiatus → glitch) and an energy-to-power-dynamics movement. Brings in compressed cultural markers (Voodoo, Compress without Opaq, Spider-Man) as "handles for the mechanics of recursive cultural production." Distinguishes apex paper (*Discursive Authority Under Recursive Pressure*), root-architecture paper (this one), hinge paper (*This Paper May Not Exist*), and loop papers (*The Afterlife of Colonial Naming*, *Spider-Man*).
>
> **Rewrite target:**
> 1. **Split this section in two.**
>    - Part A: **§ Discussion: A Return-Map Vocabulary for Recursive Disturbance.** Treat stutter / dissonance / hiatus / glitch as proposed analytic vocabulary, not as observed structure of the world. Define each operationally. Acknowledge the vocabulary overlaps with existing terms in HCI, STS, and software engineering (suggest comparisons).
>    - Part B: **§ Paper Family and Position of This Manuscript.** Name the apex / root-architecture / hinge / loop distinction as the author's positioning of the present manuscript within a larger paper family. Cite each paper. State that this typology is the author's, not a field-standard one.
> 2. Cut the cultural-marker paragraph entirely (Voodoo, Compress without Opaq, Spider-Man) — or move it to an appendix as *§ Appendix: Cultural Vocabulary in the Archive*. As body text, it reads as private symbolism.
> 3. Cut *"Even the smallest piece of cultural meaning production is therefore infrastructural."* — overgeneralization.
>
> **Output:** Part A and Part B, with the cultural-marker material either cut or moved to appendix.

---

## Prompt 14 — DISCUSSION

> **Section:** Discussion.
>
> **Current state:** Five paragraphs. Mixes ethical claims ("recursive AI should not become more skilled than the user who governs it"), methodological points (interruption is gain, not loss; stutter is real condition; subjectivity belongs), affirmative framing ("intelligence properly governed can change the world"), and procedural points (recursive prompt governance, repository-as-architecture correspondence audit).
>
> **Rewrite target:** Restructure into four labeled subsections, each with bounded claims:
>
> 1. **§ 7.1 Implications for AI-Governance Design.** What this study suggests about where governance work should be done in recursive AI systems. Tie back to Results.
> 2. **§ 7.2 Implications for Method.** What this study contributes methodologically: archival reconstruction as a method for studying one's own AI-augmented practice. Cite reflexive ethnography and autoethnography literatures (Ellis, Adams & Bochner; Anderson on analytic autoethnography) as comparison.
> 3. **§ 7.3 Limitations.** Required. Include at minimum:
>    - Single-author, single-coder corpus.
>    - Archive-native terminology not externally validated.
>    - No counterfactual archive without recursive governance.
>    - Selection bias: corpus reflects what was kept.
>    - Generalizability: claims hold for this archive, not for AI production at large.
>    - Unfalsifiable elements of the three-order interpretation.
> 4. **§ 7.4 Open questions.** Two or three falsifiable next-step questions another researcher could pursue.
>
> Cut the affirmative paragraph ("This is not a wound narrative...") — it is voice-of-the-author, appropriate for a preface or positionality statement, not for Discussion.
>
> **Output:** the rewritten Discussion as four labeled subsections.

---

## Prompt 15 — CONCLUSION

> **Section:** Conclusion.
>
> **Current state:** Three paragraphs. Names "three broader incursions" (literature into recursive words, religion into recursive ontologies, philosophy into recursive reflexivity). Restates the central claim. Asserts the paper *had to* become book-scale.
>
> **Rewrite target:** A short, restrained conclusion (200–300 words) doing exactly four things, in order:
>
> 1. **Restate the bounded finding** in one sentence, matching the Abstract.
> 2. **State the contribution** in one sentence: what a non-PHAROS reader can take from this study.
> 3. **State what the study does not establish** in one sentence (no counterfactual, no generalization).
> 4. **Name one concrete next step** for the field — something another researcher could do.
>
> Cut the "three broader incursions" framing entirely. It is essayistic and unsupported. If it matters to the author, save it for a separate essay.
>
> Cut *"the architecture demanded a book-scale form to remain legible"* — manifesto.
>
> Close on the bounded-non-finality formulation, restated soberly.
>
> **Output:** the rewritten Conclusion.

---

## Prompt 16 — REFERENCES

> **Section:** References.
>
> **Current state:** 18 references, APA-style, real and current. Hyphens are escaped (`\\-`) — markdown-paste artifact. The reference list is one of the strongest parts of the manuscript.
>
> **Rewrite target:**
> 1. Strip all `\\-` and `\\#` escape artifacts.
> 2. Verify each reference resolves. Drop any that does not.
> 3. Add the references introduced by Prompt 5 (Suchman, Star & Bowker, Latour, Pasquale, Crawford, ISO/IEC 42001, IEEE 7000-series), and any added by Prompt 14 (Ellis/Adams/Bochner on autoethnography, Anderson on analytic autoethnography). Cite only what you can verify.
> 4. Audit each reference: it should be engaged at least once in the body. Drop unengaged citations.
> 5. Add DOIs or stable URLs where available.
> 6. Sort alphabetically by first author surname.
>
> **Output:** the cleaned reference list.

---

## Prompt 17 — INTEGRATION AND CROSS-REFERENCE AUDIT (final)

> Final integration pass. Take all rewritten sections produced by Prompts 1–16 and assemble them into a single manuscript. Then perform the following audit and report any failures before producing the final document.
>
> **Structural audit.** Verify the manuscript follows this order:
> 1. Title (Prompt 1)
> 2. Abstract (Prompt 2)
> 3. Introduction (Prompt 3)
> 4. Background (cultural-context paragraph moved out of Prompt 7)
> 5. Related Work (Prompt 5)
> 6. Corpus and Method (Prompt 4)
> 7. Glossary (built from terms across Prompts 8–12)
> 8. Results (Prompts 6, 7, 8, 9, 10, 11)
> 9. Discussion (Prompts 12, 13 Part A, 14)
> 10. Paper Family and Position (Prompt 13 Part B)
> 11. Conclusion (Prompt 15)
> 12. Positionality, Conflicts, and Ethics (write fresh, see below)
> 13. Data Availability (write fresh, see below)
> 14. References (Prompt 16)
> 15. Appendix A — Document Inventory (Table 1, from Prompt 7)
> 16. Appendix B — Skill and Application Inventory (Table 2, from Prompt 10)
> 17. Appendix C — Cultural Vocabulary in the Archive (from Prompt 13)
>
> **Cross-reference audit.** Every claim in Discussion must trace to a Results subsection. Every Results subsection must trace to a Method procedure. Every Method procedure must trace to the Corpus boundary.
>
> **Citation audit.** Every reference must be engaged at least once in body text. Drop unengaged ones.
>
> **Voice audit.** No first-person pronouns outside the Positionality section. No manifesto register. No floating *only / always / finally / demands*.
>
> **TODO audit.** Surface every `[TODO: author to supply]` as a final checklist for the author.
>
> **Two new short sections to write fresh:**
>
> - **Positionality, Conflicts, and Ethics** (~150 words): author identity (Martin Lepage, PhD, AI governance researcher, Quebec, bilingual EN/FR); relationship to corpus (author = producer); funding `[TODO]`; conflicts `[TODO]`; ethics (corpus is the author's own work — note this clearly); positionality statement.
> - **Data Availability** (~80 words): where a reader can request access to the archive, under what conditions, what metadata is shared even if full access is restricted.
>
> **Output:** the final integrated manuscript, followed by the TODO checklist.

---

## Section-to-prompt map (quick reference)

| Section in current draft | Prompt |
|---|---|
| Title | 1 |
| Abstract | 2 |
| Introduction | 3 |
| Corpus And Method | 4 |
| Literature Review (parent + 3 sub) | 5 |
| The Archive As Classes | 6 |
| Ignition And Laboratories | 7 |
| Containment And Recursive Revision | 8 |
| Protocol Stack | 9 |
| Distribution And Skill Governance | 10 |
| Hephaistos And Build Truth | 11 |
| Three-Order Logic | 12 |
| Return Map And Loop Papers | 13 |
| Discussion | 14 |
| Conclusion | 15 |
| References | 16 |
| (integration pass) | 17 |

---

## Optional follow-up prompts

- **Prompt A (translation):** *"Produce a French version suitable for a Francophone AI governance audience, preserving the bounded-claim discipline."*
- **Prompt B (companion methods note):** *"Write a 1,500-word standalone Methods Note extracting the analytic procedure as a transferable method other archive owners could apply."*
- **Prompt C (anticipated reviewer responses):** *"Generate three reviewer personas — sympathetic STS scholar, skeptical AI safety researcher, methods-strict qualitative methodologist — and draft author responses to each."*
