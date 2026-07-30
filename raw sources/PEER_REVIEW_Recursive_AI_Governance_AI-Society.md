---
type: source
aliases: []
tags: [raw-source, orphan-repair, ai-governance, methods, writing-corpus]
status: raw
created: 2026-07-10
updated: 2026-07-10
source: "PEER_REVIEW_Recursive_AI_Governance_AI-Society"
---
# Peer Review

**Manuscript:** *Recursive AI Governance as Executable Method: The Very Long Narrative*
**Target venue:** *AI & Society* (Springer)
**Review type:** Structural + developmental review, reviewer-as-author-proxy
**Reviewer stance:** External submission-readiness audit against AI & Society standards and the author's specific revision requests (overlap collapse; empirical object and contribution legible by page 2).

---

## 1. Summary Statement

This is a conceptually ambitious, methodologically self-aware qualitative archival study that proposes a three-order model of recursive AI governance (internalization → protocolization → distributed build enforcement), grounded in a bounded PHAROS archive. The underlying argument is genuinely publishable and genre-appropriate for *AI & Society*: it treats governance as sociotechnical, takes recursive/agentic methods seriously, and locates control inside the production loop rather than outside it.

In its current form, however, the manuscript is **not yet submittable** to *AI & Society*. Three problems dominate, roughly in order of severity:

1. **Structural duplication.** §Background and Context (¶17–23) and §Theoretical Framework (¶24–30) are near-verbatim duplicates. Six long paragraphs repeat the same literature, the same archive description, the same protocol-stack summary, and the same positioning claim, with only cosmetic substitutions ("AI" ↔ "artificial intelligence"). Once this collapse is resolved, the §Literature Review also becomes partially redundant.
2. **Buried empirical object and contribution.** The empirical object (the PHAROS archive) and the contribution (a method history + a three-order operational model) are not visible until ¶10, after the reader has traversed ~1,500 words of citation-heavy context. For *AI & Society*, both must be legible on page 2.
3. **Submission-readiness gaps.** No reference list, no keywords, no author metadata, no positionality statement, no data-availability statement, no corpus counts, multiple "AUTHOR TO CLARIFY" and "date?" placeholders, and ~30 uses of "internal archive source" as a citation. These are hard blockers for any Springer journal.

**Recommendation:** Major revision. The intellectual substance is there; the manuscript is a structural and production job away from being defensible. The priority order is (a) collapse Literature Review / Background / Theoretical Framework into a single Related Work section, (b) rewrite the Introduction so that the research problem, empirical object, and contribution sit on page 2, (c) fix the submission-artefact gaps.

---

## 2. Against the Author's Specific Revision Requests

### 2.1 Collapse overlap across Literature Review, Background/Context, and Theoretical Framework

This is the correct diagnosis. The three sections together span ¶11–30 (≈3,400 words) and revisit the same seven literatures — foundation-model risk (Bommasani, Bender, Weidinger); sociotechnical debt and ML infrastructure (Sculley, Sambasivan); external AI governance frameworks (OECD, NIST, EU AI Act); documentation instruments (datasheets, model cards, internal audit); agentic methods (Constitutional AI, Toolformer, ReAct, ToT, Reflexion, Self-Refine); recursive-governance critique (Selbst, Passi & Jackson, Novelli); and the archive's internal vocabulary. Each literature is introduced three times.

The most egregious case: ¶18 and ¶25 open with the same sentence ("Recursive [AI / artificial intelligence]-assisted production places governance pressure on workflows, not only on models") and then rehearse the same paragraph structure for the next 1,200 words. This is not developmental overlap; it is duplicated text. A journal reviewer will read this as either (a) a drafting error the authors did not catch or (b) an attempt to pad length. Neither is recoverable without structural cuts.

**Recommended target architecture for AI & Society:**

| Current | Recommended |
|---|---|
| Introduction + Literature Review + Background and Context + Theoretical Framework (≈4,500 words) | Introduction (≈900 words) + **Related Work and Conceptual Frame** (≈1,800 words) |
| 3 reviews of sociotechnical AI literature | 1 consolidated treatment |
| 3 reviews of agentic/recursive methods | 1 consolidated treatment |
| 3 statements of positioning | 1 positioning move in Introduction, reinforced at close of Related Work |
| 2 introductions of archive-native vocabulary | 1 introduction, deferred until §Methods where the archive is the object of analysis |

Concrete moves:

1. **Delete §Theoretical Framework entirely.** It is a redraft of §Background and Context, not a separate conceptual layer. The "theoretical framework" content that is genuinely additive — governance as *the object that recurses*, the skill / build-truth conceptual pair — can be folded into the closing paragraph of the new Related Work section and the opening of §Methods.
2. **Merge Literature Review + Background and Context** into a single section titled **Related Work and Conceptual Frame**. Organize it around three subsections: (a) external AI governance and documentation; (b) recursive and agentic methods; (c) the unresolved junction — governance *as* the recursive object. End each subsection with a one-sentence gap claim rather than a full positioning paragraph.
3. **Move the archive-native vocabulary** (charge, stutter, glitch, boobytrap, traversal, Sakura, Sealed Card, Violet Gem, ALAMBIC, Master Key, Hephaistos, Recurso, RECURSUS, Theseus, Auryn, Hopf) out of the conceptual sections and into §Methods → "Analytic vocabulary of the archive." This is where it belongs analytically: it is not theory the paper imports, it is data the paper reads. Introducing it as theoretical apparatus lets reviewers mistake archive-native terminology for the author's proposed general framework, which is a category error the current draft does not forestall.

**Target word count for the consolidated front matter:** Introduction ≤ 900 words; Related Work and Conceptual Frame ≤ 1,800 words. This preserves every piece of substantive content that is not duplicated, and cuts ≈1,800 words.

### 2.2 Make empirical object and article contribution fully legible by page 2

As drafted, the Introduction performs four moves in order: (i) general problem statement about recursive AI (¶6); (ii) three paragraphs synthesizing external governance, documentation, agentic methods (¶7–9); (iii) gap identification (¶9); (iv) finally, in ¶10, the empirical object (PHAROS archive) and the contribution. A reader who stops reading after page 2 — which is what reviewers and editors often do — encounters only the problem framing and the literature context. They do not yet know what the paper actually studies or what it claims.

**Fix:** Move the empirical object and the contribution forward. Target structure for the new Introduction (≤ 900 words, 4 paragraphs):

1. **¶1 (Hook + problem).** One paragraph: the asymmetry between output scale and trust scale under recursive production. End with the specific governance question the paper takes up: *how governance itself operates recursively within sustained AI-assisted production.*
2. **¶2 (Empirical object, named on page 1).** One paragraph introducing the PHAROS archive as the bounded empirical site, describing what it contains (normalized markdown copy, raw DOCX version family, version genealogy note, companion wiki summary, linked archive documents; Sep 2024–Jan 2026), and declaring the design (qualitative archival case study, interpretive).
3. **¶3 (Gap + contribution, on page 2).** One paragraph stating what existing work does not resolve (governance operating *from within* the loop, with lineage preserved) and the paper's twofold contribution: (a) a method history of recursive governance reconstructed from a bounded archive, and (b) a three-order operational model (signals of instability → executable controls → conditions of continuity) in which governance is internalized, protocolized, and distributed under a shared forge layer.
4. **¶4 (Roadmap).** One paragraph previewing sections.

All literature synthesis moves out of the Introduction and into §Related Work. The Introduction's job is: *what is this paper, what does it study, what does it claim*. That is what *AI & Society* reviewers need on page 2.

### 2.3 AI & Society submission guidelines compliance

Non-negotiable missing pieces (hard blockers):

- **Reference list.** The manuscript cites ~30 sources in-text but contains no References section. For Springer/*AI & Society*, this alone triggers desk rejection. Use author-date style consistent with in-text citations. Ensure each in-text citation has a full reference with DOI where available.
- **Keywords.** Four to six required. Suggested: *AI governance; recursive systems; sociotechnical systems; archival case study; agentic methods; auditability*.
- **Title page requirements.** Author name(s), affiliation(s), ORCID, corresponding-author contact, acknowledgments, funding statement, competing-interest declaration, author-contributions statement (if applicable).
- **Abstract length.** Current abstract is 320 words. *AI & Society* targets ~200–250 words unstructured. Trim; keep the three-order transitions claim and the bounded-archive qualifier.
- **Data availability statement.** Required by Springer. This manuscript is particularly sensitive on this point because the empirical object *is* an archive. State what portion of the archive is available, under what terms, and cite any repository DOI. If the archive is not shareable, justify why and indicate what is available on reasonable request.
- **Ethics declaration.** For archival work where the archive is the author's own production, state this explicitly and address whether the materials include third-party or participant-identifying content. Declare IRB status (likely not applicable, but say so).
- **Reproducibility note for qualitative work.** *AI & Society* accepts interpretive research but expects the reflexive-standards equivalent: positionality disclosure, analytic decision trail, and a statement about member checking, intercoder work, or auditor review (or their documented absence). The current §Study Design already notes that these were not done; that admission needs a position statement and a mitigation in §Limitations.

Softer recommendations:

- **Subtitle "Companion paper to Invention Disclosure v12" must be removed.** This references an internal artifact that readers of *AI & Society* cannot access and that signals the paper is embedded in a proprietary product pipeline. Reframe or delete.
- **Section labeling.** AI & Society tolerates conceptual/interpretive structures beyond IMRaD. The current seven-section structure is acceptable *if* the duplication is removed. After consolidation, the structure should read: Introduction → Related Work and Conceptual Frame → Methods (Study Design) → Findings → Discussion → Conclusion. This matches what the journal expects of qualitative work.
- **"Internal archive source" citations (≈30 instances).** Unacceptable as-is. Options: (a) cite a specific, named, dated artifact from the archive with a stable identifier (file path, commit hash, version tag) and list these in an appendix or supplementary materials table; (b) replace with direct quotation framed as primary data ("The archive states, in [Artifact X, dated Y]: '…'"); (c) deposit the relevant artifacts as supplementary materials with DOIs. Without one of these, the evidentiary basis of the paper is unverifiable.

---

## 3. Major Comments

### M1. Placeholders and unresolved drafting marks

The manuscript contains visible drafting marks that must not reach peer review:

- ¶4 (Abstract): "hsd been generated" — typo.
- ¶32: "(date?)"
- ¶34: "N documents = ?; N version transitions = ?"
- ¶39: "(N = ? documents; N = ? version instances)"
- ¶47, ¶54, ¶58, ¶61: "(AUTHOR TO CLARIFY: …)" and "(Reporting guideline gaps: …)"
- ¶60: "(Editor note: moved to Discussion.)"

Every placeholder must be resolved *before* submission. Each "N = ?" requires an actual count. If counts cannot be produced, redesign the corpus description to state what *is* known (e.g., "one focal narrative and its version family, the version genealogy note, the companion wiki summary, and five linked archive documents"). A journal cannot evaluate bounded-corpus claims without actual enumeration.

### M2. Positionality is acknowledged in principle but not discharged

¶37 notes that positionality should be disclosed: "At minimum, the final manuscript should disclose the researcher's relationship to the archive, role in producing or curating documents, authority over version control, and involvement in naming the archive-native constructs analyzed here." This is the correct standard. But the current draft does not do it.

For *AI & Society* this is not optional. If the author is also the producer of the archive — which the internal vocabulary (Hephaistos, PHAROS, the skill ecosystem naming) strongly suggests — the paper is practitioner or autoethnographic research, and that framing must be declared. Without it, the reader cannot assess whether archive-native categories are being recovered or authored. The strongest version of this paper is one that *owns* the practitioner-researcher stance, cites it appropriately (Ellis et al., 2011; Anderson, 2006; or Schön's reflective practitioner, depending on fit), and uses it to motivate why the archive can legitimately serve as both data and conceptual source.

### M3. "Internal archive source" as a citation class

Related to M2, but distinct. ~30 in-text citations take the form "(internal archive source)." In §Findings this is especially frequent. A reviewer cannot verify any of the empirical claims without external access to these sources. Minimum acceptable fix: a supplementary appendix that lists each archive artifact by stable identifier (filename or commit hash), with date and one-line description, and every in-text "(internal archive source)" citation replaced by a specific artifact reference (e.g., "(PHAROS archive, *recursus-v3.md*, 2025-07-12)"). Stronger fix: deposit the cited artifacts in a repository (Zenodo, OSF) under controlled access if needed, and cite the DOI.

### M4. Three research questions announced late, not previewed in Introduction

The Introduction gestures at the contribution, but the three research questions (RQ1: from external constraint to recursive method maintenance; RQ2: translation into executable protocol; RQ3: distributed skills + forge layer) appear only in §Results. For a reader who does not know the archive, the RQs function as the spine of the paper. They must be stated in the Introduction (end of the new ¶3) and reiterated at the start of §Methods. Currently, by the time the RQs are introduced, the reader has already read ~5,000 words.

### M5. Archive-native vocabulary — status ambiguity

The manuscript oscillates on whether terms like *charge*, *stutter*, *glitch*, *boobytrap*, *traversal*, *Sakura*, *Sealed Card*, *Violet Gem*, *ALAMBIC*, *Master Key*, *Hephaistos*, *Recurso*, *RECURSUS*, *Theseus*, *Auryn*, *Hopf*, *Mobius* are (a) archive-native data to be described, (b) analytic categories proposed by the author, or (c) shared constructs in a broader field. The paper says (a) in multiple places ("archive-native diagnostics," "archive-specific analytic categories rather than standardized terms in the broader literature") but then uses them as if they were (b) in §Results and §Discussion.

Fix: decide the status per term. Any term used in interpretive argumentation (e.g., "build truth," "delegated execution vs. delegated authority") should be explicitly proposed as the *paper's* analytic contribution, operationally defined, and separated from archive-native data terms. Any term that remains pure archive data (Sakura, Violet Gem, ALAMBIC) should be used descriptively only and italicized or tagged on first use. *AI & Society* readers will tolerate exotic vocabulary if it is disciplined; they will reject it if it reads as in-group jargon.

### M6. Claim-evidence asymmetry in §Findings

§Results presents each RQ's evidence in prose, but because (a) corpus counts are missing (M1) and (b) citations are internal (M3), the findings read as assertions about the archive rather than traceable claims from it. At minimum: for each major empirical claim, provide either a direct quotation from a named artifact or a reference to a specific document with date/version. The current pattern — "The archive marked that shift through the paired terms Recurso and RECURSUS" — needs to become "The shift appears in [Artifact X, dated Y], where the author writes: '…' (Recurso); and in [Artifact Z, dated W], where the framing 'RECURSUS' is introduced as '…'."

### M7. Tables and figure are referenced but not supplied

The manuscript refers to "TABLE 1: Analytic corpus by document type," "TABLE 2: Documented transitions from external containment to recursive method maintenance," "TABLE 3: Distributed governance units and reported build-enforcement functions," and "FIGURE 1: Reported sequence from corpus pressure to containment, recursive revision, protocolization, and distributed build enforcement." None are present. These must be produced before submission. TABLE 1 in particular is load-bearing for the bounded-corpus claim and should not be handwaved.

### M8. The "three-order" synthesis is buried

¶58 offers the most analytically distinctive claim in the paper: a three-order organization (instability signals → executable controls → continuity conditions). This is the model the paper actually contributes. Currently it appears once, mid-Results, and is not foregrounded in Abstract, Introduction, or Discussion section headers. It should be (a) named in the Abstract, (b) previewed in the Introduction contribution statement, (c) visualized as Figure 1 (replace the currently promised sequence figure), and (d) re-asserted as the organizing logic of Discussion. This is the easiest single structural improvement available.

---

## 4. Minor Comments

1. **¶4 (Abstract):** "hsd been generated" → "had been generated." Also: "two-fold" rather than "twofold" if you want British style, but AI & Society accepts either — be consistent.
2. **¶5–10:** Paragraphs are very long (one paragraph = 400+ words). Break into shorter paragraphs aligned with single rhetorical moves.
3. **¶6:** The citation dump — ten citations in one parenthetical — is a common reviewer irritant. Trim to three or four most load-bearing per claim; move the rest to §Related Work.
4. **¶8:** "Yao et al., 2023a" and "Yao et al., 2023b" are distinguished in-text but the References section that would disambiguate does not exist. Ensure the forthcoming reference list does so correctly.
5. **¶10:** "the source corpus does not specify a discrete study timeframe (internal archive source)" contradicts the Abstract, which gives a timeframe ("September 2024 to January 2026"). Reconcile.
6. **¶14–16 and ¶22–23:** The repeated "to our knowledge" claims are acceptable but become cumulative. One is enough.
7. **¶19, ¶26:** The archive-native vocabulary is introduced twice, in near-identical paragraphs. Keep one (in §Methods).
8. **¶32–37 (§Study Design):** Framing is strong; move the positionality paragraph earlier in the section, not last.
9. **¶38–61 (§Results):** Consider renaming to §Findings, consistent with qualitative conventions and *AI & Society* norms.
10. **¶45, ¶57, ¶58:** "(FIGURE 1: …)" and "(TABLE 2: …)" are stage directions rather than figure calls. Produce the figures and refer to them as "Figure 1" in running text.
11. **¶47:** "exact document counts and ordering" — resolve before submission.
12. **¶58:** "Theseus, Auryn, Hopf" appear once without definition. If retained, define; otherwise cut.
13. **¶77:** The three actionable recommendations for practitioners are good but generic. Consider one concrete illustrative example per recommendation.
14. **¶83 (closing):** "Trust scales only when recursive return, protocol passage, distributed skill inheritance, and implementation correspondence are governed as parts of the same architecture." This is the paper's best single sentence. Elevate to Abstract.
15. **Overall word count.** Current ≈ 8,800 words. *AI & Society* original articles typically target 6,000–8,000. After the consolidation proposed in §2.1, the paper should land near 6,500 — well within range.
16. **Consistency:** "artificial intelligence" vs. "AI" — pick one. Current practice mixes them, partly as a side effect of the duplication across §BC and §TF.
17. **Hyphenation:** "AI-assisted," "AI-governance" — enforce consistently.

---

## 5. Questions for the Author

1. Is the author also the producer of the PHAROS archive? If yes, how should the paper position this (autoethnography, practitioner research, reflexive case study)?
2. What is the actual N for the corpus (documents, versions, linked artifacts)?
3. What are the closure dates for corpus delimitation, and why those?
4. Can archive artifacts be deposited under a DOI, or do constraints prevent this? If the latter, what limited-access arrangement is possible?
5. Is the "Invention Disclosure v12" lineage something the paper should own (and cite formally) or sever?
6. Was any part of the corpus generated with AI assistance, and if so, how is that disclosed per *AI & Society* AI-disclosure norms?

---

## 6. Revision Priority (in order)

1. Delete §Theoretical Framework; merge §Literature Review and §Background and Context into a single §Related Work and Conceptual Frame.
2. Rewrite Introduction to four paragraphs, ≤ 900 words, with empirical object in ¶2 and contribution in ¶3.
3. Add References section; resolve every in-text citation.
4. Resolve all "N = ?", "(date?)", and "AUTHOR TO CLARIFY" placeholders.
5. Produce Table 1, Table 2, Table 3, and Figure 1.
6. Write positionality statement and data-availability statement.
7. Replace all "(internal archive source)" citations with specific artifact identifiers or primary quotations.
8. Trim abstract to ≤ 250 words; add keywords.
9. Remove subtitle "Companion paper to Invention Disclosure v12" or reframe.
10. Move archive-native vocabulary into §Methods subsection.
11. Foreground the three-order synthesis as the paper's core model.

---

## 7. Bottom Line

The argument is defensible and the empirical site is distinctive. The paper is structurally redundant, under-produced as a submission artifact, and currently buries both its empirical object and its contribution under a tripled literature review. None of these problems is fatal. A disciplined two-pass revision — one structural, one production — should put this manuscript in range for *AI & Society*. As submitted, it would be desk-rejected on the missing references and the duplicated sections alone.

## Related

- [[Recovered analysis Ballad Witches Road]]
- [[Governance and PHAROS MOC]]
- [[Research and Papers MOC]]
- [[Peer Review — Recursive AI Governance as Executable Method (AI & Society)]]


---
## Backlinks
Provenance artifact de-orphaned via graph repair (frontmatter + backlinks added 2026-07-10). Original content preserved above, unaltered.

- Indexed in: [[Home]]
