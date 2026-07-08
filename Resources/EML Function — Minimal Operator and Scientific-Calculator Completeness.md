---
type: wiki
title: EML Function — Minimal Operator and Scientific-Calculator Completeness
aliases:
- EML function
- Exp-Minus-Log
- eml(x,y)
- single binary operator
tags:
- reference
- mathematics
- recursion
- symbolic-regression
- epistemics
- generative-minimalism
- resources
- calculator
- trees
- functions
- trigonometric
- elementary
- wiki
status: active
domain: reference
created: '2026-04-26'
updated: '2026-06-26'
vault_area: Resources
canonical_path: Resources/EML Function — Minimal Operator and Scientific-Calculator Completeness.md
backlink_count: 13
backlinks:
- '[[Areas/PHAROS/Smallest Building Block — Relation as Rule]]'
- '[[Areas/Writing/Research and Papers MOC]]'
- '[[wiki/Home]]'
- '[[Resources/Entropic Gravity, Lily-of-the-Valley, and EML — Three Instances of Emergent Phenomenon]]'
- '[[Resources/Evidence Discipline and Epistemics]]'
- '[[Resources/Lily-of-the-Valley and EML — Reconstruction from Minimal Elements]]'
- '[[Resources/Recursive Governance Theory]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[archive/session-state/session-state-001]]'
- '[[artifacts/stale-projects-2026-07-04]]'
- '[[artifacts/stale-projects-2026-07-05]]'
- '[[artifacts/stale-projects-2026-07-06]]'
- '[[artifacts/stale-projects-2026-07-07]]'
---

# EML Function — Minimal Operator and Scientific-Calculator Completeness

## Summary
The raw source describes the EML operator, `eml(x, y) = exp(x) - ln(y)`, as a proposed single binary primitive that, together with the constant `1`, can generate the ordinary repertoire of a scientific calculator through composition in the complex domain. The important vault reading is bounded: EML is not "all of mathematics." It is a compact grammar for reconstructing a broad calculator-style basis of elementary functions.

## Core Idea
- `exp(x)` appears immediately as `eml(x, 1)`, because `ln(1) = 0`.
- Logarithms can be built through nested EML expressions, after which arithmetic, powers, roots, and trigonometric functions can be reconstructed through deeper expression trees.
- The raw source frames EML expressions as binary trees whose leaves are `1` or variables and whose internal nodes are repeated `eml` operations.
- Trigonometric functions are theoretically reachable, but the resulting trees are large, opaque, and impractical to print or evaluate naively.

## Limits and Cautions
- The phrase "all elementary functions" is domain-sensitive. The raw source itself flags a narrower scientific-calculator sense, not the broadest classical mathematical definition.
- The source mentions critiques involving algebraic functions and arbitrary polynomial roots; treat this as a verification lead before formal citation.
- The source also mentions a withdrawn follow-on paper about hardware-efficient EML networks. Do not rely on the practical ML/hardware implication until the bibliographic trail is checked directly.
- Deep EML trees can create overflow, branch-cut, and NaN problems. Numerical verification and symbolic checking are part of the claim, not optional decoration.

## Vault Use
EML is useful as a concept note for **generative minimalism**: one primitive, one constant, repeated composition, and a bounded world of reconstructed operations. That makes it a good formal analogy for [[Lily-of-the-Valley and EML — Reconstruction from Minimal Elements]], [[Poiesis Poietics Poetics Praxis — Making and Action Distinctions]], and the recursive-governance distinction between a powerful generator and an overclaimed total explanation.

For PHAROS-style evidence discipline, the lesson is almost too perfect: a compact generative rule can be real and beautiful while still requiring scope limits, verification constraints, and anti-myth language.

## Related
- [[Lily-of-the-Valley and EML — Reconstruction from Minimal Elements]]
- [[Recursive Governance Theory]]
- [[Evidence Discipline and Epistemics]]
- [[Narrative Capture Failure Taxonomy — Substituting Theory for Contact]]
- [[Poiesis Poietics Poetics Praxis — Making and Action Distinctions]]

## Sources
- Raw capture: `raw sources/The EML function.txt`

