---
type: launch-asset
title: Reddit r/RPGdesign Post — Phase 0 Halo-Validation Post
tags:
- launch-asset
- assets
- elemental-agents
- combinations
- combination
- modifier
- halo
- elements
status: draft-locked-with-product-pivot-note
created: '2026-05-24'
updated: '2026-06-26'
vault_area: assets
canonical_path: assets/elemental-agents/ttrpg-repack/reddit-drafts/reddit-r-rpgdesign-post.md
backlink_count: 1
backlinks:
- '[[wiki/ASSETS MOC]]'
target_channel: r/RPGdesign
target_post_date: TBD (operator timing — original window 2026-06-24/26 superseded by "no waiting" override)
flair: '[Mechanics]'
phase: 0 (halo-audience validation — TTRPG surface test, not primary product validation)
---

## Pivot note 2026-05-24

This post was drafted when Charge & Circle was scoped as a TTRPG product at $19. The product identity has since shifted to a ritual governance framework at $299-499 (primary audience: GRC / compliance / AI governance), with the TTRPG audience as a halo readership. This post remains useful as a Phase 0 halo-validation test — it asks the TTRPG-designer audience whether the framework's surface holds up as table design — but it is no longer the primary validation gate for the product. Primary validation will happen through governance-audience channels (LinkedIn governance communities, GRC newsletter outreach, warm-intro to compliance leads at 2-3 friendly organizations).

The post itself does not need rewriting — it tests mechanical credibility with TTRPG designers, which is still useful even when those designers aren't the primary buyer. Just understand that a positive Reddit response is *halo signal*, not *primary buyer signal*. A negative or muted Reddit response does not kill the bet; it tells us only that the TTRPG surface needs more work or that the halo audience is harder to reach.

# Reddit r/RPGdesign Post — Phase 0 Halo-Validation Post

## Title

> 10 elements, 45 duals, 120 triples, one shell script that enforces all the rules. Looking for design feedback before I commit this to a campaign.

## Body

> **TL;DR:** I built a hard magic system where 7 base elements + 3 modifier elements compose into 45 named dual combinations and 120 named triples. The modifiers can never lead a combination, only support. A ~200-line awk script enforces all of it — combination counts, unique permutations, no decorative names, the modifier-can't-lead constraint, no token stutter in combination names. I'd like feedback on whether the mechanical spine is real or whether I've fooled myself.
>
> ---
>
> ### The unusual design choice
>
> Most homebrew magic systems *describe* magic. Mine *validates* it. There's a shell script that fails loud if my combinations file ever violates a structural rule:
>
> - Must be exactly 45 dual and 120 triple combinations (`7 choose 2` and `10 choose 3` minus the forbidden modifier-only triples).
> - Every combination has a unique sorted-permutation key (no `Water+Fire` and `Fire+Water` as separate entries).
> - Every combination has all 5 required fields populated: best use case, characteristic risk, lead element, supporting elements, manifestation.
> - The manifestation field must describe executable behavior, not decorative imagery. A combination called `Spirit-Earth` cannot mean "deep groundedness." It has to mean a specific action with a specific effect.
> - Spirit, Chi, and Akasha cannot lead a routine combination. They appear only as modifiers, never as peers.
>
> If I add a new combination tomorrow and forget the manifestation field, the script catches it. That constraint has been weirdly load-bearing for keeping the design honest.
>
> ---
>
> ### The mechanics
>
> **Base elements (can lead or support):** Water, Air, Wind, Fire, Earth, Wood, Metal.
>
> **Modifier elements (support only):** Spirit, Chi, Akasha.
>
> **Each element has a signature verb:**
> - Water — diagnose ambiguity
> - Air — clarify signal
> - Wind — transmit and propagate
> - Fire — execute transformation
> - Earth — ground and validate
> - Wood — grow structured scope
> - Metal — enforce precision
> - Spirit — align intent
> - Chi — maintain flow
> - Akasha — synthesize cross-system context
>
> **Combinations compose the verbs.** Water+Fire is "diagnose, then execute" — useful for breaking down fortified state, risky because it commits to an action before the diagnostic completes. Air+Metal is "clarify, then enforce precision" — slower, but rarely fails on edge cases. Each pair has its own named manifestation in the fiction, its own best use, its own failure mode.
>
> Adding a modifier shifts a pair into something escalated. Water+Fire+Spirit is the same diagnose-then-execute pattern but with intent-alignment laid on top — usable when the caster needs the working to *mean* something beyond its mechanical effect.
>
> ---
>
> ### Honest provenance
>
> This system has an unusual origin. I built the underlying structure for a completely different domain — a multi-agent software framework, where the elements were role archetypes and the combinations were team configurations. Halfway through writing it I realized the constraints I'd designed (composed verbs, escalation modifiers, anti-decorative naming, a validator that polices its own rules) read closer to a hard magic system than to software documentation.
>
> So I'm asking the people who actually evaluate magic systems on their merits: **does this hold up as table design, or does the software-origin DNA show through in ways that don't translate?**
>
> ---
>
> ### Specific questions I'd value feedback on
>
> 1. **The 7+3 split.** Seven peer elements plus three modifiers that can never lead. In play, does the "modifier-can't-lead" rule create interesting decisions, or does it just create a forbidden zone players resent?
>
> 2. **The manifestation rule.** Forbidding decorative names is meant to keep the system honest, but it might kill the poetic register that makes magic feel magical. Sanderson-style design and OSR atmospheric design tend to disagree on this. I want both takes.
>
> 3. **The validator-as-design-tool.** A script that fails loud has kept *me* disciplined while writing, but is it useful to a GM, or is it a designer-side artifact that never reaches the table?
>
> 4. **The combinatorics.** 165 named combinations is a lot. Is this a generative space (caster character builds map naturally onto combinations) or a content burden (every one needs a unique illustration before it's usable)?
>
> I'll share the full combinations table and the validator output in comments if there's interest. Not selling anything — just trying to figure out whether the mechanical spine is real before I write the rest of the system around it.

---

## Posting protocol (operator-facing)

**When:** Tue or Wed in the Jun 24-Jul 1 window, 10am-noon Eastern. Avoid weekends and major holidays.

**Flair:** `[Mechanics]` — the more honest fit than `[Design Process]` since the post is about a structural design choice.

**Pre-post checklist:**
- Use a Reddit account with at least 6 months of history and some prior subreddit engagement (clean fresh accounts get karma-gated).
- Have the top-comment-ready combinations table ready as a separate file (12 sample entries, formatted as a Reddit table) for the inevitable "show your work" replies.
- Do not link to an external storefront. The product doesn't exist yet at this stage.

**Cross-post Day 4:** to r/osr (player audience, not just designers) with a reframed angle emphasizing runnable-at-the-table over design-feedback. Do not post to r/magicbuilding or r/rpg yet — those are Phase 4 channels.

**Engagement window:** monitor and respond substantively to comments for 7 days. Surface real designers' work back to them ("oh, that's how Mausritter handles this — fascinating"). Don't argue with critics; thank them and ask follow-ups.

**Phase 0 gate (after 7-14 days):**
1. 5+ DMs/PMs requesting the playtest packet, combinations table, or validator script
2. 2+ unsolicited mentions in another thread, server, or social platform
3. At least one substantive engagement from a designer with a published itch.io page or comparable credibility

All three must hit before Phase 1 begins. If any one fails, kill the bet and pivot to the methodology-buyer storefront (Bet 1 in `audience-expansion.md`).

## What this draft deliberately omits

- No storefront link (no storefront exists yet)
- No mention of PHAROS, EMERAULD, Obsidian Agent Vault, AI agents, or Claude Code
- No price reference
- No call-to-action beyond "feedback in comments"
- No Witches' Road / charge-persistence vocabulary — that lineage is real but it's branding language for Phase 3, not designer-validation language for Phase 0

## Top-comment-ready combinations sample

To be drafted in Phase 0 Week 1 alongside the post. Pattern: 12 entries pulled from the existing dual-combinations.md and triple-combinations.md sources, with engineering vocabulary stripped and replaced by in-fiction working names. This is a Phase 0 prep deliverable; do not draft it until the operator is in active Phase 0 work.

## Related

- [[Elemental Agents Framework — Multi-Agent Role and Validation Architecture (2026-05-12)]]
- [[Elemental Agents — Productization Plan (2026-05-24)]]
