---
type: governance-doc
title: Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06)
tags:
- co-equal-authority
- hephaistos
- queen-keyport
- clearday
- governed-task
- operator-arbitration
- freemium-parity
- governance-doc
- areas
- pharos
status: active
domain: governance
created: '2026-07-08'
updated: '2026-07-08'
vault_area: Areas
canonical_path: Areas/PHAROS/Co-Equal Authority Conflict — clearday ASC-RevenueCat Governed Task (2026-07-06).md
backlink_count: 5
backlinks:
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[Areas/PHAROS/RELAY-LEDGER — Live Governance Handoff Ledger]]'
- '[[wiki/HEPHAISTOS MOC]]'
- '[[_vault/VAULT ADDITIONS TRACKER]]'
- '[[governance/EMERAULD-OS-SPEC — Governance Wiring]]'
---

> For future Claude: this is a record of a live, recorded Hephaistos/Queen-Keyport
> authority conflict from this week (2026-07-06), not a hypothetical worked example
> like the Phase 7 case studies. Sources:
> `/home/martin/.agents/hephaistos/governed-tasks/clearday-asc-revenuecat-20260706/co-equal-conflict.md`
> and the sibling `run-report.md` in the same directory. Clearday is a separate PHAROS
> mobile product (`apps/mobile-apps/clearday-mobile`), distinct from the client work
> documented elsewhere in this vault under Lavoie.

## Summary

On 2026-07-06, a real governed task — submitting Clearday's ASC (App Store Connect)
IAP setup and RevenueCat configuration, then shipping to TestFlight — produced a named,
recorded disagreement between Hephaistos and Queen Keyport over timing: whether to
ship to external TestFlight testers now while freemium-parity code gaps closed in
parallel (Hephaistos's position), or hold external TestFlight until parity was fully
wired (Queen Keyport's position). The conflict was surfaced explicitly, both positions
were documented with their right-arm inputs, and Martin arbitrated a middle path
(Branch B: internal sandbox TestFlight now, external testers blocked on named
conditions). Status per source: RESOLVED, operator arbitration recorded 2026-07-06.
Sources: `co-equal-conflict.md`, `run-report.md` (same directory).

## Context

This conflict ran through the `governed-tasks/` mechanism — a directory-per-task
structure distinct from the `ledgers/RELAY-LEDGER.md` entry format documented in
[[RELAY-LEDGER — Live Governance Handoff Ledger]]. The task directory
(`clearday-asc-revenuecat-20260706/`) holds four files: the Hephaistos-to-Queen-Keyport
scope/failure-modes JSON, the Queen-Keyport-to-Hermes governance-decision JSON, the
`co-equal-conflict.md` naming the disagreement, and `run-report.md` recording the gate
result and evidence. The `run-report.md` explicitly labels this a "governed task dry
run," and notes the gate itself (`~/.agents/hephaistos/scripts/handoff-gate.py`) is
currently a stub — it produces a verdict but does not yet enforce it. That distinction
matters: the conflict, its documentation, and the arbitration are real; the automated
gate that would eventually block routing on an unresolved conflict is not yet live
enforcement.

The trigger was a real product decision. Clearday's store metadata and in-app copy
already claimed a 7-day free history window. The client-side UI filter enforcing that
window (`isWithinFreeHistory`) and the RevenueCat user-identity wiring
(`initSubscription(userId)`) were not yet complete when Hephaistos proposed shipping
the production build to TestFlight.

## Details

### The conflict, named

| Authority | Position |
|---|---|
| Hephaistos | Ship EAS production build to TestFlight now; complete ASC + RevenueCat setup and wire `isWithinFreeHistory` + `userId` in parallel, as a fast-follow rather than a gate. |
| Queen Keyport | No **external** TestFlight until freemium parity is wired (7-day UI filter or a metadata revision) plus `initSubscription(userId)` plus RevenueCat keys in the build. Internal sandbox TestFlight only until then. |

Grounds, per `co-equal-conflict.md`: Hephaistos argued velocity and learning — the IAP
setup is an external bottleneck, the binary can ship while code gaps close, and 51
tests were passing. Queen Keyport argued that shipping with store metadata and in-app
copy claiming a benefit (7-day free history) the client does not yet enforce is a
marketing-enforcement gap — flagged as an Anti-Charm risk and a potential App Review
issue given clearday is a health-adjacent subscription product.

### Right-arm divergence

The Hephaistos scope packet surfaced both right-arms explicitly rather than letting
Queen Keyport synthesize alone after the fact:

- **Philosopher:** limits must be honest before monetization asks for money.
- **Power-analyst:** platform gatekeepers plus client-only enforcement together
  produce a structural illusion of control — the enforcement can be bypassed or fail
  silently and no one downstream would know.

Queen Keyport's synthesis was approve-with-constraints, not reject — consistent with
the co-equal model's design (see [[Areas/PHAROS/Architecture Translation Guide — Eight Operators to Three-Agent Stack]]):
a right-arm divergence gets named and folded into constraints, not suppressed into a
single verdict that erases the disagreement.

### Resolution

Martin's recorded arbitration, verbatim from `co-equal-conflict.md`:

> "OPERATOR DECISION: Branch B — internal sandbox TestFlight now (Martin sandbox Apple
> ID only). External TestFlight testers blocked until: isWithinFreeHistory wired in
> dashboard+log UI, initSubscription(authenticatedUserId) wired, and sandbox purchase
> proof on file."

By the time of `run-report.md` (same date), two of those three conditions were
confirmed wired in the live repo: `isWithinFreeHistory` via `filterFreeHistory` in
`app/(tabs)/index.tsx` and `app/(tabs)/log.tsx`, and `initSubscription(String(profile.id))`
in `app/_layout.tsx`'s `SubscriptionBootstrap`, using `logIn` on user change. `npm test`
reported 54 passing (up from 51, post-parity wiring). Two conditions remained open:
sandbox purchase proof and the external-facing ASC IAP + RevenueCat dashboard
configuration. Hermes's routing scope was correspondingly narrowed: ASC IAP setup,
RevenueCat config, and the EAS production build route to internal TestFlight only —
no external tester invites until the remaining parity constraints are satisfied.

### Why this matters as a real-world test of the co-equal design

This is not a hypothetical worked example (compare the P1 case studies referenced in
[[HEPHAISTOS Phase 7 — Final Buildout Report]]) — it is a live product decision with
real App Review and client-trust stakes, arbitrated within a day. Several things the
co-equal design promises on paper actually happened here in practice:

1. Neither authority silently won. Hephaistos's velocity argument and Queen Keyport's
   parity argument were both preserved in the record rather than one being quietly
   dropped once Martin ruled.
2. The right-arm divergence (Philosopher vs. Power-Analyst) was surfaced rather than
   pre-resolved by Queen Keyport before it reached the operator — the operator saw the
   actual disagreement, not a smoothed synthesis.
3. The resolution was a genuine third option (Branch B), not a binary pick between the
   two named branches — arbitration produced a bounded compromise with concrete,
   checkable conditions, matching the "approve-with-constraints, not reject" governance
   vocabulary.
4. Hermes's routing scope was narrowed exactly to match the arbitrated conditions
   (internal-only, named unblock conditions) rather than either fully gated or fully
   opened — consistent with the rule that Hermes proceeds only after both co-equal
   authorities clear, or after operator arbitration, and does not adjudicate the
   conflict itself.

The one open question the source material itself flags: the `handoff-gate.py` script
that would eventually enforce this routing-eligibility check automatically is
currently a stub ("VERDICT: ROUTE_ELIGIBLE — Hermes may proceed (stub: not
enforced)"). The conflict-naming and arbitration discipline held up under real
pressure; the automated enforcement layer that would catch a *future* unresolved
conflict without a human noticing has not yet been built.

## Related

- [[Areas/PHAROS/HEPHAISTOS Agent Architecture|HEPHAISTOS Agent Architecture]]
- [[Areas/PHAROS/Architecture Translation Guide — Eight Operators to Three-Agent Stack]]
- [[RELAY-LEDGER — Live Governance Handoff Ledger]]
- [[HEPHAISTOS Phase 7 — Final Buildout Report]]
- [[Areas/PHAROS/Governance and PHAROS MOC|Governance and PHAROS MOC]]
