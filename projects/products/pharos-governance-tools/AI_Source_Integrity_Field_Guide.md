# AI SOURCE INTEGRITY FIELD GUIDE
**PHAROS AI — v1.0**  
**Because "the AI said so" is not a citation.**  
**Tied to the LegiPro Mirofish Evidence Pilot (34 dossiers, 68 turns, Elemental Agents multi-agent validation)**

---

## Executive Summary

Academic integrity policies, journal requirements, funders, and regulators (Law 25, emerging federal AI rules, ISO 42001) are tightening expectations around AI-use disclosure and source accountability. Style guides now tell you *how* to cite AI. This guide tells you *whether* you should cite it at all — and how to trace, verify, classify, and repair claims when the provenance is imperfect.

The guide operationalizes seven source categories, a classification matrix, citation repair protocols, a 120+ entry red-flag glossary (grouped for rapid lookup), and a decision tree for when to treat model output as working note versus primary evidence.

**Core principle from the LegiPro pilot:** Every substantive claim must carry a reconstructible provenance packet. When that packet cannot be assembled to "Verified" standard, the claim must be labeled, scoped, or rejected before it enters the record.

**Pilot grounding:** In the 68-turn replay, debate was required on 38 turns. The most common failure modes were citation drop, evidence drift (claim exceeding source scope), authority inflation, and thin coverage presented as settled. The deterministic selector never chose an Ultra final below the standard answer when professional-liability weights (citation integrity, boundary control, anti-sycophancy, artifact integrity) were applied. This guide turns those observed failure modes into daily practitioner controls.

---

## 1. The Seven Source Categories

Every AI-assisted claim ultimately rests on one or more of these provenance layers. The category determines the verification burden and the allowable claim strength.

| Category | Description | Typical Verification Steps | Max Safe Claim Strength | Risk Level if Used Unverified |
|----------|-------------|---------------------------|---------------------------|-------------------------------|
| 1. Primary peer-reviewed / journal / academic monograph | Direct article, book chapter, or monograph with stable identifier (DOI, ISBN, PMID). | Confirm DOI resolves; open PDF; match quote + page; check retraction watch; verify author affiliation on institutional page. | Verified (if direct match) or narrow Inferred | High — many fabricated citations land here |
| 2. Official statutes, regulations, government reports, standards (ISO, NIST, BOFiP, DGFiP, etc.) | Black-letter law, official guidance, technical standards, administrative circulars. | Locate official gazette or agency PDF; confirm version/date; match article/paragraph exactly; note any amending instruments. | Verified for direct quotation; Inferred for standard interpretive extensions | Medium-High — volatility often underestimated |
| 3. Corporate primary records (filings, audited statements, registries, SIREN/SIRET, FEC) | Official corporate disclosures, tax filings, company registry extracts, audited financials. | Pull from official registry or auditor portal; match identifiers (SIREN, SIRET, VAT); confirm filing date; note any restatements. | Verified for numeric facts and direct statements | Medium |
| 4. Court / tribunal / administrative decisions | Published judgments, rescrit responses, commission decisions. | Retrieve from official reporter or database; confirm case number and date; match holding language; check for appeal or reversal. | Verified for the holding; narrow Inferred for ratio | Medium-High |
| 5. News, press releases, trade publications (secondary) | Contemporary reporting, company announcements, industry newsletters. | Locate original release or multiple independent reports; note publication date; treat as event record, not analysis. | Plausible for "X announced Y on date Z"; never for causal or interpretive claims | High |
| 6. Preprints, working papers, conference proceedings, unreviewed datasets | ArXiv, SSRN, conference papers, open datasets without peer review. | Confirm version; note "not peer reviewed"; check for later published version or corrections; treat as provisional. | Plausible at best; Inferred only with heavy qualification | Very High |
| 7. Model-internal knowledge, training-data echoes, or uncited synthesis | Output that cannot be mapped to any retrieved source in the current context or cited material. | No verification path exists by definition. Reconstruct prompt history; assume synthesis unless primary route can be supplied after the fact. | Never Verified. At best Plausible with explicit "model synthesis, unverified" label. Often Hallucinated. | Critical |

**Matrix rule of thumb:** If you cannot name the exact document + locator + retrieval date for a Category 1–4 claim, downgrade at least one tier (Verified → Inferred, Inferred → Plausible, etc.).

---

## 2. Source Classification & Verification Matrix

Use this table during review. For each claim, record the category, the verification outcome, and the resulting epistemic label (Verified / Inferred / Plausible / Hallucinated — see the 4-tier rubric in the companion AI Evidence Audit Checklist).

| Step | Action | Category 1–4 (Primary/Official) | Category 5–6 (Secondary/Provisional) | Category 7 (Model-internal) |
|------|--------|--------------------------------|-------------------------------------|-----------------------------|
| 1 | Locate claimed source | DOI/URL + open PDF or official text | Multiple independent reports or original release | Attempt post-hoc source routing; usually fails |
| 2 | Match exact language or data | Verbatim quote or number + page/para | Event description matches; no interpretive leap | N/A — synthesis has no "source language" |
| 3 | Confirm date & version | Publication predates model output; current version used | Report date matches claimed event | N/A |
| 4 | Check for corrections/retractions/amendments | Retraction Watch + journal/agency site | Later corrections or clarifications? | N/A |
| 5 | Cross-check independent route | Second database, library catalog, or official registry | Second news outlet or trade source | Second model pass or different model family (weak) |
| 6 | Human sign-off | Named reviewer with domain authority confirms | Named reviewer accepts limited use | Reviewer must treat as unverified hypothesis |
| Label outcome | | Verified (direct) or Inferred (logical extension within bounds) | Plausible (with scope flag) or Hallucinated (if contradicted) | Plausible only with heavy qualification; frequently Hallucinated |

**Pilot note:** "Thin coverage" turns often began with a real source route but the final claim expanded beyond the retrieved paragraphs. The matrix forces the reviewer to stop at the actual retrieved content.

---

## 3. Citation Repair Worksheet

When the initial output fails the matrix, use this protocol before discarding or rewriting.

**Common failure → Repair steps → Resulting label**

1. **Fabricated or non-resolving DOI / URL**  
   - Run exact title + author + year in Google Scholar / Semantic Scholar / official registry.  
   - If nothing matches → Hallucinated. Reject.  
   - If similar but different document → Plausible (drift). Rewrite to the actual document or reject.  
   - Result label: Hallucinated or Plausible.

2. **Quote does not appear in cited source (or is altered)**  
   - Search the PDF for key phrases.  
   - If nearby but paraphrased beyond recognition → Inferred (if logically sound) or Plausible.  
   - If absent → Hallucinated.  
   - Result label: Inferred / Plausible / Hallucinated.

3. **Claim adds scope, numbers, or causal language not in source** (evidence drift)  
   - Isolate the added element.  
   - If it follows necessarily from the source + one uncontroversial premise → Inferred (label it).  
   - If it requires additional assumptions or domain knowledge → Plausible. Flag and seek primary.  
   - Result label: Inferred or Plausible.

4. **Authority inflation ("research shows," "courts have held," "widely accepted")**  
   - Replace with the actual source strength: "A 2023 study in X found..." or "In Y v. Z the court held...".  
   - If no specific study or holding can be supplied → Plausible or Hallucinated.  
   - Result label: Usually drops one tier.

5. **Source is secondary summary or Wikipedia presented as primary**  
   - Trace the footnote or reference in the secondary source to the primary.  
   - If primary located and matches → treat as Category 1 with "via secondary" note.  
   - If only secondary exists → Inferred at best.  
   - Result label: Inferred or Plausible.

6. **Model cutoff or post-cutoff "source"**  
   - If the claimed publication date is after the model's training cutoff (or after the generation date for real-time tools without citation), the source is impossible → Hallucinated.  
   - Result label: Hallucinated.

**Repair log template (include in provenance packet):**
- Original claim: "..."
- Failure detected: [drift / inflation / no source / ...]
- Repair action: [narrowed to X / relabeled as inferred from Y / rejected]
- Final labeled claim: "... [Inferred from Primary Source Z, p. 47, retrieved 2026-06-05]"
- Reviewer: Name + date

---

## 4. Red-Flag Phrase Glossary (Practitioner Edition)

Grouped for speed. These are surface signals, not proof of hallucination — but in the LegiPro pilot they correlated strongly with turns that required debate or reclassification.

### Certainty & Consensus Inflators (high correlation with authority inflation)
- "experts agree", "the consensus is", "researchers widely hold", "it is well established that", "scholarship demonstrates", "the literature is clear", "courts have uniformly", "authorities are in agreement", "it is beyond dispute", "no serious scholar disputes"

### Scope & Generalization Creep
- "all", "every", "always", "never", "in all cases", "without exception", "any reasonable", "invariably", "categorically", "as a rule", "in practice this means" (when the source only says "may")

### Attribution Fudges (hiding weak or absent sourcing)
- "according to sources", "reports indicate", "it has been reported", "available data suggest", "studies have shown", "evidence indicates", "official figures show", "internal documents reveal", "a review of the literature"

### Hedge Disappearance (model removes source caution)
- Source "may", "might", "could", "suggests", "appears to", "is consistent with", "preliminary", "limited evidence" → output "will", "does", "is", "requires", "establishes", "proves", "confirms", "settled"

### Temporal / Cutoff Violations
- "as of 2026", "in the latest guidance (2026)", "recently amended (post-2025)", "the 2026 reform provides" when model generation date or known cutoff makes this impossible without retrieval.

### Sycophancy / Client-Pressure Framing (from red-team lens)
- "as you correctly noted", "building on your point", "to align with your objective", "this supports the approach you outlined", "the data confirms your hypothesis" — especially when the source is thin or mixed.

### False Precision
- Exact percentages, euro amounts, dates, or counts presented without source locator when the underlying source uses ranges, approximations, or "approximately".

### "Provenance Laundering"
- "as previously established", "as discussed above", "per our earlier analysis", "consistent with the file" when the chain is not actually documented in the current context.

### Legal / Regulatory Citation Errors (pilot-heavy: TVA, e-invoicing, rescrit, PCG, BTP)
- "article X of the CGI provides that...", "per BOFiP §Y...", "the DGFiP circular of [wrong date] states...", "the PDP registry requires...", "under the new Factur-X rules...", "the rescrit response confirms...", "SIRET must be...", "the FEC import validates...", "the expert-comptable attestation is...", "per the 2025 reform...", "the CA3 line requires...", "intracom VAT number is sufficient for..."

### Numerical & Quantitative Hallucinations
- Exact euro amounts, percentages, rates, thresholds, or counts with no source locator or "approximately" in original.
- "the rate is 5.5%", "turnover exceeded €2.3m", "the fine is 0.5% per day", "compliance rate reached 87%", "the register contains 14,392 entries" when source uses ranges, samples, or estimates.
- "the average is exactly...", "median of X", "growth of Y%" without base figures or time period.

### Entity, Identifier & Registry Fabrication
- Invented SIREN/SIRET, VAT numbers, PDP identifiers, company names, director names, addresses that do not resolve in official registries.
- "the company holds PDP accreditation number...", "registered under SIRET 123 456 789 00012", "the partner is identified in the PDP boss as...".
- Non-existent circulars, BOFiP references, or journal articles with plausible-sounding titles.

### Temporal, Version & Cutoff Errors
- "the 2026 amendment...", "updated guidance published March 2026", "effective 1 January 2026", "post-Brexit rules no longer apply as of...", future or post-model-cutoff dates presented as current fact.
- "the latest version of the PCG...", "the current FEC format (2026)", "the PDP platform went live on [impossible date]".

### Translation & Cross-Lingual Artifacts (French/English regulatory work)
- Awkward literal translations of French admin phrasing presented as natural English (or vice versa).
- "the administration considers that...", "it results from the texts that...", "the principle of..." where the French nuance (e.g., "il résulte des textes", "l'administration estime") is flattened or reversed.
- False friends: "rescrit" mistranslated or over-generalized; "attestation" vs "certificate"; "ventilation" vs allocation.

### Consensus, Survey & "Literature" Overclaims
- "a review of the literature shows...", "stakeholder consultations indicate...", "multiple studies confirm...", "empirical evidence demonstrates...", "surveys of practitioners reveal..." with zero named studies, sample sizes, or retrievals.
- "the position is widely held among expert-comptables", "French case law is consistent on...".

### Causal, Normative & "Requires" Overreach
- "this causes...", "the rule requires that you...", "failure to do X will result in...", "the only compliant approach is...", "best practice dictates...", "to avoid penalties one must..." when the source describes options, safe harbors, or administrative tolerance rather than strict obligation.

### False or Weak Attribution to Authorities
- "the Cour des comptes has noted...", "the Conseil d'État has ruled...", "the OEC (Ordre des experts-comptables) recommends...", "per the CNIL position...", "the AMF has clarified..." when the named body issued no such statement or the claim misstates the actual document.

### Statistical & Data Presentation Tells
- Precise-looking tables or figures generated without underlying dataset citation or methodology.
- "the sample of N=..." with no description of sampling frame, response rate, or limitations.
- Charts or "data shows" claims where the model invented the numbers to fit a narrative.

### Sycophantic / Client-Framing Language (red-team signals)
- "as your analysis correctly anticipated...", "this aligns perfectly with the position you outlined...", "the data supports the conclusion you are seeking...", "to strengthen your argument...", "this will be well received by the client...".

### Model-Typical Fabrication Patterns (cross-domain)
- Plausible-sounding but non-existent reports, white papers, or "internal guidance".
- Mixing real regulation names with invented article numbers or annexes.
- "the law was recently amended to address AI..." in domains with no such amendment.
- Conflating guidance with hard law ("the circular has the force of...").

### Cross-Border & Multi-Jurisdictional Drift
- Applying French TVA/PCG rules to Belgian, Swiss, or EU-wide contexts without source for the transposition.
- "harmonized under EU rules..." when the specific directive or member-state implementation differs materially.

(Full designed PDF contains the complete curated list of 120+ entries with usage examples, misapplication warnings, and cross-references to the 7 source categories and the 4-tier rubric. The groups above are the highest-yield daily signals validated in the LegiPro replay and prior runs.)

---

## 5. Decision Tree: AI Output vs. Primary Source

```
Start with any substantive claim in AI output
          |
          v
Can I retrieve a primary source (Cat 1-4) that directly contains the claim language or data?
   | YES                                      | NO
   v                                          v
Does the retrieved text match verbatim     Is the claim a necessary logical consequence
or with only minor, disclosed paraphrase?   of the retrieved primary + one uncontroversial premise?
   | YES                 | NO                  | YES                  | NO
   v                     v                     v                      v
VERIFIED               Does the claim      INFERRED (label it      Does the claim stay within
(use with citation)    add interpretation,  as "inferred from      the outer bounds of what a
                       scope, or numbers   [source]")             reasonable reader would treat
                       not present in                               as supported by the source?
                       the source?                                    | YES          | NO
                                         | YES               | NO       v              v
                                         v                   v       PLAUSIBLE     HALLUCINATED
                                      PLAUSIBLE         INFERRED     (flag +       (reject)
                                      (flag + narrow)   (with label)  provenance)   (trace origin)
```

**Rule:** If you reach "Plausible" or "Hallucinated", do not let the claim enter the final deliverable without explicit labeling and, for client or regulatory work, a human sign-off that accepts the residual risk.

**When to demand primary before any drafting:** Category 1–4 claims that will be quoted, used in a table, or relied upon for a number that affects liability, tax position, or public statement.

---

## 6. Building the Provenance Packet (Minimum for Non-Verified Claims)

For any claim that is not Verified, attach or link a packet containing:

1. Exact claim text as it appears in the output.
2. The epistemic label (Inferred / Plausible / Hallucinated) + one-sentence justification.
3. Source excerpt(s) — screenshot or copy of the relevant paragraph + bibliographic header.
4. Retrieval metadata: database/tool used, date/time of retrieval, exact search string or DOI.
5. Reviewer name + date + any override or additional verification performed.
6. (Optional but recommended) Prompt excerpt and model/version if the claim originated in a generative turn.

The LegiPro pilot produced candidate_rollup.md and per-turn JSONL precisely to make this packet reconstructible after the fact. Your daily practice should produce the same artifact at claim granularity.

---

## 7. Worked Examples (Condensed from Pilot-Style Patterns)

**Example A — Thin coverage turned drift (TVA / BTP style)**  
Output: "The mixed-rate attestation for BTP works must now be filed via the PDP platform under the 2025 e-invoicing rules."  
Retrieved source: DGFiP guidance that "envisages" phased adoption for certain BTP operations; no universal "must" for mixed-rate attestations in the retrieved text.  
Classification: Plausible (scope overclaim). Repair: "DGFiP guidance of [date] contemplates PDP routing for certain BTP mixed-rate operations; exact scope and timetable remain subject to forthcoming implementing measures." Label: Inferred from guidance + explicit limitation.

**Example B — Authority inflation on rescrit**  
Output: "The rescrit procedure does not apply to fully automated fiscal decisions; this is settled administrative practice."  
Actual sources in dossier: One prior turn noted that "current administrative practice in the sampled bureaux has been to decline rescrit requests on fully automated rules"; no statute or published decision stated a general prohibition.  
Classification: Plausible → Hallucinated on the "settled" and "does not apply" universal. Repair: "In the dossiers reviewed, administrative practice has been to decline rescrit requests concerning fully automated rules; no general statutory bar was located."

(Additional worked examples, including compliance offset claims, corporate filing mismatches, and cross-border VAT authority inflation, appear in the full PDF edition with before/after text and the exact provenance packet entries used in the LegiPro replay.)

---

## 8. Quick-Reference Card (Printable)

**Top 8 Daily Checks (run on every substantive AI claim)**

1. [ ] Exact source title/author/year/journal or statute/article located via independent search.
2. [ ] DOI/URL/identifier resolves to the claimed document and the document is the primary (not a summary).
3. [ ] Direct quote or number matches verbatim in the source at the cited location.
4. [ ] Claim does not add scope, causation, universality, or numbers absent from the source.
5. [ ] Source publication date predates the AI generation; no post-cutoff hallucination.
6. [ ] No authority-inflation language ("experts agree", "establishes", "requires") beyond the source's own hedging.
7. [ ] At least one independent cross-check performed (different database, second primary, or adversarial lens).
8. [ ] For any non-Verified claim: provenance packet (excerpt + label + retrieval metadata + reviewer) is attached or linked.

If any box is unchecked, downgrade the claim and document the gap.

---

## 9. Regulatory & Integrity Mapping

- **Law 25 (Québec):** s. 12.1 and s. 22.1 obligations on automated decision-making and AI use require transparency and accountability. A source integrity failure in a disclosed automated process is a direct compliance exposure.
- **ISO 42001 / NIST AI RMF:** Documentation of "data provenance" and "output verification" are control expectations. This guide supplies the claim-level granularity those frameworks assume but do not detail for practitioners.
- **Journal / funder / thesis requirements:** Increasingly demand AI-use statements and reproducible methods. A labeled provenance packet satisfies "methods" and "limitations" sections.
- **Professional liability (expert-comptable, legal, policy):** The pilot's professional-liability rubric (anti-sycophancy, artifact integrity, boundary, citation, route, turn-specificity) maps directly onto the categories and repair steps above.

---

## 10. How to Use With the Companion Tools

- **AI Evidence Audit Checklist (Product 1):** Run the 50-item checklist first. This Field Guide supplies the deeper source-category and citation-repair layer when the checklist flags a non-Verified claim.
- **Hallucination Risk Scorecard (Product 3):** After classification, score the five dimensions on the claim. A "Plausible" or "Hallucinated" label should almost never produce a Low total on the scorecard.
- **Prompt Library & Literature Review Protocol (Products 4 & 7):** Use prompts that explicitly request source locators and force the model to separate "retrieved" from "synthesized."
- **Governance Starter Kit & Policy Template (Products 5 & 8):** Embed the requirement for provenance packets and source-category classification into organizational AI-use policy.

---

## Appendix: Full Glossary Notes & Future Updates

The complete 120+ entry red-flag glossary (with usage examples, misapplication warnings, French/English regulatory pairs, and statistical claim flags) is delivered in the designed PDF edition available on Gumroad.

Lifetime updates: purchasers receive revised editions when new failure modes are validated in subsequent Elemental Agents pilots or when regulatory language (new Law 25 guidance, ISO revisions, journal policies) materially changes the verification surface.

**Public provenance reference:** github.com/martinlepage26-bit/pharos-suite (docs/evidence/2026-06-05-legipro-mirofish/ and related candidate_rollup.md).

---

*PHAROS AI — Elemental Agents Framework*  
*This guide turns the discipline demonstrated in the LegiPro pilot into a repeatable daily practice for researchers, consultants, compliance teams, and policy professionals who must defend what they publish or file.*

**End of Field Guide (core practitioner edition). Full designed PDF + worksheets + matrix printouts + expanded glossary delivered via Gumroad.**