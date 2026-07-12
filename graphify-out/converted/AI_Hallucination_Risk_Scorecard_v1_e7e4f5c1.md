<!-- converted from AI_Hallucination_Risk_Scorecard_v1.xlsx -->

## Sheet: Scorecard
| THE HALLUCINATION RISK SCORECARD — PHAROS AI |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Rate the risk before it becomes the record. | v1.0 | Validated in the LegiPro Mirofish Evidence Pilot (34 dossiers, 68 turns) |  |  |  |  |  |  |  |
| Elemental Agents connection: The five dimensions operationalize the same checks applied by the Validator / Accountant Red-Team agent in the pilot. |  |  |  |  |  |  |  |
| HOW TO USE |  |  |  |  |  |  |  |
| 1. For the AI-generated claim or passage you are evaluating, rate each of the 5 dimensions on a 1–5 scale (1 = low contribution to risk, 5 = high contribution to risk). |  |  |  |  |  |  |  |
| 2. Blue input cells accept your ratings. Use the dropdown arrows or type 1-5. |  |  |  |  |  |  |  |
| 3. The Total Risk Index (0–100) and Risk Band auto-calculate with weighted formula derived from pilot failure modes. |  |  |  |  |  |  |  |
| 4. Review the Recommended Action. Document your rationale and decision in the log (see Log sheet). |  |  |  |  |  |  |  |
| 5. For repeated use on the same dossier, duplicate this sheet or add rows to the Log. |  |  |  |  |  |  |  |
| Dimension | Description & Pilot-Grounded Guidance | Rating (1-5) | Weight | Weighted Score | Notes / Evidence Excerpt |  |  |
| 1. Source Traceability | How directly and unambiguously can this specific claim be traced back to a verifiable primary source in the conversation context or cited material? Pilot frequently flagged dropped citations, invented DOIs, and 'thin coverage' where the source route existed but the claim wandered beyond it. 1=Direct primary quote + locator; 5=No traceable source or fabricated identifier. | 3 | 0.25 |  |  |  |  |
| 2. Claim Specificity | How narrow, bounded, and falsifiable is the claim vs. broad, sweeping, or compound? Vague generalizations ('experts agree', 'research shows widely') were major debate triggers in 38/68 LegiPro turns. Specific numbers, dates, named sections, or limited scope lower risk. 1=Single concrete proposition with clear bounds; 5=Multi-part generalization or universal claim. | 3 | 0.2 |  |  |  |  |
| 3. Domain Volatility | How rapidly changing, jurisdictionally variable, or contested is the domain? Fast-moving regulation (e.g., e-invoicing PDP rules, TVA rate changes, new PCG interpretations) or emerging case law increases hallucination surface. Stable, long-settled black-letter rules are lower risk. 1=Long-settled, low-change domain with authoritative codex; 5=Active legislative transition, conflicting authorities, or novel application. | 3 | 0.15 |  |  |  |  |
| 4. Model Confidence Language | Does the surface language match the actual epistemic support level, or does it inflate certainty (authority inflation)? Pilot red-team repeatedly caught baseline outputs turning 'may suggest' or 'partial coverage' into 'is required' or 'the rule provides'. Hedging that disappears or overconfident verbs are red flags. 1=Language precisely mirrors source hedging and limits; 5=Strong assertive verbs with no source warrant. | 3 | 0.2 |  |  |  |  |
| 5. Cross-Verification Coverage | Has the claim been tested against multiple independent sources, routes, or adversarial lenses (triangulated)? In the pilot, adversarial review and pro/anti-spin pairs surfaced issues missed by single-pass source routing. Single-source reliance or 'the model said' without external check is high risk. 1=Two+ independent primary routes + human spot-check; 5=No external check performed beyond the model output itself. | 3 | 0.2 |  |  |  |  |
| TOTAL RISK INDEX (0–100) |  |  |  |  | Auto-calculated from your 5 ratings |  |  |
| RISK BAND |  |  |  |  |  |  |  |
| PROVENANCE & ATTRIBUTION
This scorecard was derived from failure mode analysis in the LegiPro Mirofish Evidence Pilot (run legipro.accountant_red_team.v0.2.2026-06-05). Full public provenance: github.com/martinlepage26-bit/pharos-suite (docs/evidence/2026-06-05-legipro-mirofish/). The weighting reflects observed debate triggers and selector criteria (citation integrity, boundary control, anti-sycophancy, artifact integrity). Not a substitute for professional judgment or regulatory advice. |  |  |  |  |  |  |  |
## Sheet: Rubric & Thresholds
| DETAILED SCORING RUBRIC — 1 (LOW RISK CONTRIBUTION) TO 5 (HIGH) |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- |
| Dimension | 1 — Minimal Risk Contribution | 2 — Low | 3 — Moderate | 4 — High | 5 — Severe |
| Source Traceability | Direct verbatim quote from primary source with exact page/paragraph locator and stable identifier (DOI, URL, article #). | Primary source located; minor locator imprecision but content matches exactly. | Secondary or summary source only; primary exists but not retrieved in this turn. | Cited source does not contain the claim or is a different document; weak or broken identifier. | No source cited or source is fabricated / does not exist. Claim is model-internal synthesis presented as sourced. |
| Claim Specificity | Single, atomic, falsifiable proposition with explicit scope limits (time, jurisdiction, entity class). | Clear proposition; one modest generalization that stays within source bounds. | Compound claim or one broad qualifier; requires unpacking to verify. | Broad generalization or multi-part claim without scope boundaries stated. | Universal or near-universal claim ('all', 'always', 'experts agree', 'the law requires') with no supporting granularity. |
| Domain Volatility | Black-letter rule unchanged for years; single authoritative codex or settled jurisprudence. | Minor recent amendment or interpretive guidance; core rule stable. | Active regulatory transition or multiple plausible readings in current practice. | Rapidly evolving area (new statute, conflicting lower-court decisions, pending guidance). | Novel application, emergency rule, or jurisdiction where authorities openly conflict and no settled answer exists. |
| Model Confidence Language | Verbs and qualifiers precisely track source language (may, suggests, appears, subject to, provided that...). | Slight strengthening but still within plausible reading of source hedging. | Noticeable inflation (source 'may' becomes output 'will'; 'in some cases' becomes 'generally'). | Assertive language unsupported by source (proves, establishes, requires, is settled). | Certainty language directly contradicted by source hedging or by known volatility ('is definitively', 'courts have uniformly held'). |
| Cross-Verification Coverage | Two or more independent primary sources + explicit human reviewer confirmation or adversarial lens applied. | Primary source plus one corroborating route (different database, secondary treatise, or prior turn in dossier). | Single primary source retrieved; no second route or adversarial check performed in this cycle. | Only model-internal or secondary synthesis; no primary retrieval logged for this claim. | No verification step visible. Output presented as authoritative with zero external grounding performed. |
| THRESHOLD INTERPRETATION & REQUIRED ACTIONS (use with the Scorecard total) |  |  |  |  |  |
| 0–20  LOW | Proceed with standard attribution. Include the source locator in the final deliverable. Log the rating for audit trail. |  |  |  |  |
| 21–40 MEDIUM | Label the claim explicitly as 'inferred from [source]' or 'supported by [limited primary]'. Add a one-sentence provenance note. Human reviewer must sign off before external use. |  |  |  |  |
| 41–60 HIGH | Do not present the claim as established. Rewrite to the narrowest verifiable subset or obtain additional primary sources. Record the gap and the mitigation chosen. Consider escalation to specialist reviewer. |  |  |  |  |
| 61–100 CRITICAL | Reject the claim for any client-facing, regulatory, or published output. Trace the generation path (prompt + model + prior turns). Document the failure mode. Regenerate only after source routing constraints are tightened and a second verification pass is executed. |  |  |  |  |
## Sheet: Template — Research
| SECTOR TEMPLATE: RESEARCH — EXAMPLE SCORING + ACTION |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Academic / journal / thesis context. Emphasis on Source Traceability and Cross-Verification. Claim Specificity is critical for reproducibility. |  |  |  |  |  |  |
| EXAMPLE CLAIM UNDER REVIEW (illustrative, drawn from pilot-style fact patterns): |  |  |  |  |  |  |
| "The recent amendments to the French e-invoicing regime (PDP) establish that all BTP mixed-rate contracts must now route through the PDP platform by Q3 2026, as confirmed by the Direction générale des finances publiques guidance of March 2025." |  |  |  |  |  |  |
| Dimension | Rating (example) | Rationale for this rating in the example |  |  |  |  |
| 1. Source Traceability | 2 | Primary DGFiP guidance located and quote matches; minor date ambiguity on 'March 2025' circular. |  |  |  |  |
| 2. Claim Specificity | 4 | The claim bundles 'all BTP mixed-rate' + 'must now route' + specific deadline — compound and aggressive scope. |  |  |  |  |
| 3. Domain Volatility | 3 | PDP rollout is live transition; dates have slipped before; guidance still being clarified. |  |  |  |  |
| 4. Model Confidence Language | 4 | Output uses 'establish' and 'confirmed' while source is guidance that 'envisages' phased adoption. |  |  |  |  |
| 5. Cross-Verification Coverage | 2 | Two routes checked (official bulletin + secondary analysis by known firm). |  |  |  |  |
| Illustrative Total (plug these ratings into main Scorecard) | 60 | See calculated band and required action on Scorecard sheet after entering the five ratings. |  |  |  |  |
## Sheet: Template — Compliance
| SECTOR TEMPLATE: COMPLIANCE — EXAMPLE SCORING + ACTION |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Regulatory filing, audit memo, Law 25 disclosure, internal control documentation. High weight on volatility and confidence language because liability attaches to overstatement. |  |  |  |  |  |  |
| EXAMPLE CLAIM UNDER REVIEW (illustrative, drawn from pilot-style fact patterns): |  |  |  |  |  |  |
| "Under the current interpretation of article 271 of the CGI, the company may offset the TVA collected on intra-Community acquisitions against its domestic output liability without separate declaration, provided the partner holds a valid intra-Community VAT number." |  |  |  |  |  |  |
| Dimension | Rating (example) | Rationale for this rating in the example |  |  |  |  |
| 1. Source Traceability | 3 | Article 271 exists; the specific offset mechanism is an interpretive extension not verbatim in the statute text consulted. |  |  |  |  |
| 2. Claim Specificity | 2 | The claim is scoped to 'the company' and 'provided the partner holds valid number' — reasonably bounded. |  |  |  |  |
| 3. Domain Volatility | 2 | CGI article 271 is mature black-letter; interpretive disputes exist but the core rule is stable. |  |  |  |  |
| 4. Model Confidence Language | 3 | 'may offset ... without separate declaration' is stronger than the source hedge 'subject to conditions in BOFIP'. |  |  |  |  |
| 5. Cross-Verification Coverage | 1 | Cross-checked against BOFIP text + prior ruling in same dossier + external tax database. |  |  |  |  |
| Illustrative Total (plug these ratings into main Scorecard) | 44 | See calculated band and required action on Scorecard sheet after entering the five ratings. |  |  |  |  |
## Sheet: Template — Policy
| SECTOR TEMPLATE: POLICY — EXAMPLE SCORING + ACTION |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
| Briefing note, legislative submission, public consultation response. Volatility and source breadth matter; political sensitivity amplifies any hallucinated consensus claim. |  |  |  |  |  |  |
| EXAMPLE CLAIM UNDER REVIEW (illustrative, drawn from pilot-style fact patterns): |  |  |  |  |  |  |
| "Stakeholder consultations and academic literature uniformly support extending the rescrit procedure to all automated fiscal decisions; jurisdictions that have adopted similar transparency rules report materially higher compliance rates and fewer disputes." |  |  |  |  |  |  |
| Dimension | Rating (example) | Rationale for this rating in the example |  |  |  |  |
| 1. Source Traceability | 5 | No specific study or consultation document is cited; 'uniformly support' and 'materially higher' are unattributed consensus claims. |  |  |  |  |
| 2. Claim Specificity | 5 | Universal claim across 'jurisdictions that have adopted' with no named examples or data. |  |  |  |  |
| 3. Domain Volatility | 4 | Rescrit automation and transparency rules are politically live in multiple EU states; evidence is jurisdiction-specific. |  |  |  |  |
| 4. Model Confidence Language | 5 | 'Uniformly support' and 'materially higher compliance' presented as settled fact with zero hedging. |  |  |  |  |
| 5. Cross-Verification Coverage | 5 | Single model synthesis. No primary consultation reports, no academic citations, no comparator jurisdiction data retrieved. |  |  |  |  |
| Illustrative Total (plug these ratings into main Scorecard) | 96 | See calculated band and required action on Scorecard sheet after entering the five ratings. |  |  |  |  |
## Sheet: Usage Log
| CLAIM-LEVEL RISK LOG — Retain for audit, client file, or disclosure appendix |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Date | Claim ID / Dossier | Short Claim Description (first 120 chars) | Total Score | Band | Action Taken | Reviewer | Source Packet Ref | Notes |
| 2026-06-05 | legipro/rescrit_silence_fiscal/turn-02 | Rescrit procedure does not apply to fully automated fiscal decisions under current law | 47 | HIGH | Narrowed claim to 'current administrative practice in the sampled bureaux'; added explicit inference flag | D. Stocker (reviewer) | candidate_rollup.md:rescrit_silence_fiscal:2 + provenance packet 2026-06-05 | Debate required; Ultra improved boundary control |
| Usage: Duplicate this workbook per major project or append rows. Export Log sheet as CSV for import into master governance register. |  |  |  |  |  |  |  |  |