---
type: governance-doc
title: L99 Demotion to Argus Review Criterion — Decision Spec
aliases:
- L99 Demotion to Argus Review Criterion — Decision Spec
tags:
- governance
- ai
- hephaistos
- argus
- governance-doc
- layer
- binding
- demotion
- placement
status: active
domain: governance
created: '2026-06-21'
updated: '2026-06-26'
vault_area: governance
canonical_path: governance/hephaistos/L99-DEMOTION-TO-ARGUS.md
backlink_count: 4
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Runtime And Agents — 2026-05-06]]'
- '[[governance/hephaistos/HEPHAISTOS]]'
- '[[hephaistos/agents/argus]]'
---

# L99 Demotion to Argus Review Criterion — Decision Spec

**Status:** Binding decision. Supersedes prior treatment of L99 as a top-level binding principle.
**Decided:** April 17, 2026.
**Scope:** Governance architecture, root and repo systems. Applies to all files that currently list L99 as a "Binding Principle."

---

## The decision

L99 (Gap Declaration) is demoted from **binding principle** to **Argus review criterion**.

L99's core discipline is preserved. It continues to operate as a detectable, enforceable check on outputs. What changes is its placement in the architecture: it moves from the constitutional layer (where it was being repeated in every file without doing load-bearing work) to the audit layer (where it can actually be checked against specific artifacts with specific evidence).

## What L99 is and continues to do

L99 names the commitment: **gaps are declared before they become claims.** An undeclared claim that papers over a gap is a lie, even if the lie is fluent and confident.

In practice, L99 protects against:
- Fluent closure over missing information
- Confident-sounding synthesis that hides unverified components
- Completion claims that omit what was not checked
- Narrative that smooths over structural uncertainty

None of that changes.

## What changes

### Before this decision

L99 was listed as item 1 in "Binding Principles" in:
- `/home/cerebrhoe/AGENTS.md`
- `/home/cerebrhoe/HEPHAISTOS.md`
- `/home/cerebrhoe/QUEEN-KEYPORT.md`
- `/home/cerebrhoe/HERMES.md`
- `/home/cerebrhoe/ORCHESTRATION.md`
- `/home/cerebrhoe/hephaistos/AGENTS.md`
- `/home/cerebrhoe/hephaistos/HEPHAISTOS.md`
- `/home/cerebrhoe/hephaistos/QUEEN-KEYPORT.md`
- `/home/cerebrhoe/hephaistos/HERMES.md`
- `/home/cerebrhoe/hephaistos/ORCHESTRATION.md`

This repetition was not enforcement. It was decoration. A principle that appears in every file without specific trigger conditions has no purchase on any specific output.

### After this decision

L99 is removed from the "Binding Principles" section of each file above and relocated to the Argus audit specification as a named review criterion. The principle no longer needs to be repeated in governance files because its enforcement is now concrete: Argus checks for it during audit passes.

## Where L99 lives in Argus

### Recommended placement: Layer 3 sub-gate

Argus has seven audit layers. Layer 3 (Novelist — narrative-reality gap analysis) is the structural closest match. Layer 3 already asks: *does the narrative overstate what was actually done?* L99 asks the sibling question: *were the gaps named, or closed over by fluency?*

L99 fits as a sub-gate within Layer 3 rather than as a new Layer 8, for three reasons:

1. Layer 3's existing job is detecting the same failure family (narrative exceeding reality).
2. Adding an eighth layer would fork the seven-layer audit structure, which is load-bearing in the current Argus contract.
3. A sub-gate inside Layer 3 can share evidence-gathering with the existing narrative-reality check, reducing audit redundancy.

If the operator prefers a standalone layer (Layer 8), this spec accommodates that alternative at the operator's discretion. Either placement is compatible with the demotion.

### L99 detection logic

When Argus evaluates an output, the L99 sub-gate asks:

1. **Does the output contain claims of completion, coverage, or verification?**
   - If yes, proceed to check 2.
   - If no, L99 does not trigger.

2. **For each claim, was the evidence basis named?**
   - "Passed review" — by whom? against what criteria? → evidence named or not.
   - "All files updated" — which files? confirmed how? → evidence named or not.
   - "No issues found" — what was checked? what was not? → evidence named or not.

3. **For each unnamed gap, is the gap declared explicitly?**
   - "Not verified" / "Gap: X was not checked" / "Bounded claim: applies only to Y" → L99 satisfied.
   - Silent omission, or fluent language that reads as covering X when X was not checked → L99 violation.

4. **Issue the L99 verdict:**
   - **PASS** — all claims carry evidence or explicit gap declarations.
   - **FINDING** — one or more claims close over a gap without declaring it.
   - **BLOCK** — the output as a whole rests on closed-over gaps that would mislead a reviewer.

### Verdict consequences

- **PASS:** Output proceeds through Layer 3, continues to Layer 4.
- **FINDING:** Output returned for gap declaration. Specific gaps named. Output may not promote until gaps are declared or evidence is added.
- **BLOCK:** Output rejected. Work returns to the producing layer (Hephaistos or Queen Keyport).

### AND-gate enforcement

Consistent with existing Argus AND-gate architecture: an L99 FINDING at Layer 3 halts the audit until resolved. The audit does not proceed through Layers 4-7 while an undeclared gap is flagged. This prevents L99 from becoming optional.

## Concrete pass/fail examples

### Example 1: PASS

Output: *"Governance spec updated in the hephaistos repo. Root files not updated in this pass — root system sync deferred to Wave 2. Argus audit of the repo changes passed seven layers."*

L99 verdict: **PASS.** The claim is bounded ("in the hephaistos repo"), the gap is declared ("root files not updated... deferred to Wave 2"), and the audit scope is named.

### Example 2: FINDING

Output: *"Governance spec updated. Argus audit passed."*

L99 verdict: **FINDING.** The same underlying work, but the claim is unbounded ("updated" with no scope) and the audit scope is not named. A reader would reasonably conclude the whole governance system had been updated and audited, when only the repo was.

### Example 3: BLOCK

Output: *"All hierarchical language has been removed from the governance architecture. The system now reflects co-equal authority throughout."*

L99 verdict: **BLOCK.** The claim is structurally false if any file still contains hierarchical language. "Throughout" is the word that triggers the block — it closes over gaps that would need to be explicitly scoped or declared.

## What this means for the governance files

During Wave 1 (or subsequent waves, at the operator's discretion), the following changes apply:

1. **Remove** L99 as item 1 from the "Binding Principles" section of the ten files listed above.
2. **Renumber** the remaining principles (currently 2-9, becomes 1-8).
3. **Add** a short pointer in the Argus-related files (`argus-contract.md`, `argus-formation.md`, or equivalent) that names L99 as the Layer 3 sub-gate per this spec.
4. **Do not remove** L99's practical enforcement. It continues to operate as an audit criterion.

If the operator selects the alternative (new Layer 8 instead of Layer 3 sub-gate), step 3 changes accordingly: the Argus seven-layer structure becomes an eight-layer structure, and Layer 8 is documented as the L99 layer.

## What this spec does not do

- Does not delete L99. L99 continues to operate, just in a different place.
- Does not remove the L99.html and L99_abstract.html historical records at `/mnt/c/Users/softinfo/Downloads/`. Those remain as provenance.
- Does not re-open or revise the underlying commitment captured in the original L99 moment. The personal-governance commitment stays; only its architectural placement changes.
- Does not touch the other binding principles (Diamond-Eyes, Anti-Charm, Machine Limitation, etc.). Those remain at the constitutional layer.

## Why this is a correct move

Three reasons.

**First, a principle repeated in every file is doing no work in any file.** Repetition is not enforcement. L99 was being performed as decoration, not enforced as a check. The failure mode L99 exists to prevent (fluent closure over gaps) cannot be stopped by printing the principle's name; it can only be stopped by a specific process that tests for it. Argus is that process.

**Second, Argus already has the structural equivalent of L99 in its Layer 3 (narrative-reality gap).** Demoting L99 to a sub-gate of Layer 3 eliminates redundancy and makes the existing Argus layer more precise. The change strengthens Argus rather than adding overhead.

**Third, the binding principles section of the governance files is reserved for commitments that bind *all* work, at all times, in all files.** L99 is better understood as a commitment that binds *outputs that make claims* — a narrower and more specific scope that fits better as an audit criterion than as a constitutional invariant.

## Gaps declared (L99 applied to itself)

This spec has not been verified against:

1. The full text of the current `argus-contract.md` or `argus-formation.md` files. The Layer 3 placement recommendation is based on the Argus seven-layer summary in `PHASE-7-FINAL-REPORT.md`; the implementation files may contain additional structure that affects where L99 fits best.
2. The full text of `SKILL-MAP.md`. If `novelist` or related skills encode Layer 3 responsibilities differently than described here, the placement may need adjustment.
3. Whether the Mercury Protocol (Layer 7, substrate self-audit) has overlap with L99 detection. It is possible L99 belongs in Layer 7 instead of Layer 3, or in both.
4. Whether any ongoing PHAROS-side work (audit reports, published artifacts, skill definitions) already cites "L99 (Binding Principle)" by name such that demoting it would create broken references.

These gaps are declared so they do not become hidden claims. Resolving them is part of Wave 1 execution, not this spec.

## Implementation order

This spec does not execute changes. It anchors them. Implementation happens in one of:

- **Option α (lean):** Include the L99 demotion in Wave 1 as a small additional task alongside the co-equal authority work. The file edits to remove L99 from "Binding Principles" can ride along with the other edits that are already being made to the same files.
- **Option β (bounded):** Execute the L99 demotion as its own sub-wave after Wave 1 is complete. Smaller scope, more reviewable in isolation.
- **Option γ (deferred):** Log this spec as a decision anchor and defer execution until a later operator session when both co-equal and L99 demotion can be handled together with rested judgment.

My recommendation: **Option α.** The file edits required for L99 demotion overlap substantially with the co-equal authority edits — the same files are being touched in the same "Binding Principles" sections. Doing them together minimizes duplicate review work and prevents a mid-state where co-equal is updated but L99 is still listed.

## Record of the operator's framing

The operator's stated framing on L99, recorded here:

> "L99 was a mistake. does it actually help?"

Followed by:

> "can you integrate L99 into Argus?"

This spec is the technical translation of those two observations. L99 was not a mistake in its underlying principle; it was a mistake in its architectural placement. Integration into Argus is the correct correction.

## Related

- [[Argus Audit Tracker — Snapshot 2026-04-28]]
- [[argus]]
- [[argus.agent]]
- [[Governance and PHAROS MOC]]
- [[HEPHAISTOS]]
