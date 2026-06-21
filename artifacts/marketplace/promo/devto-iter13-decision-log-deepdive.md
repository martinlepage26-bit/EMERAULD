---
title: The one Obsidian note that stopped Claude from re-proposing ideas I'd already rejected
published: false
tags: [ai, obsidian, claudeai, devtools]
canonical_url:
description: A deep dive into the Decision Log note type — the single highest-leverage addition to any AI-assisted development workflow.
---

# The one Obsidian note that stopped Claude from re-proposing ideas I'd already rejected

There's a specific failure pattern that shows up after a few months of AI-assisted development.

You're in a session. The agent proposes an approach. You push back — you tried that, it didn't work, here's why. The session continues. Two weeks later, different session, different context: the agent proposes the same approach again. With confident reasoning that sounds better than your original objection.

This isn't hallucination. It's a record-keeping problem. The reasoning behind your rejection only existed in a closed chat window. From the agent's perspective, starting fresh, the approach looks reasonable.

The fix is one note type: a Decision Log with a mandatory "Alternatives Rejected" section.

---

## What makes a Decision Log different from a regular note

Most notes capture what is. Decision Logs capture what was chosen, what was ruled out, and — critically — why.

The "why rejected" is the load-bearing part. Without it, you have a record of decisions. With it, you have a record the agent can reason from.

Here's the format I use:

```markdown
---
type: decision
status: locked
date: 2026-03-12
---

# Decision — Auth Layer Scope

## Decision
Keep authentication separate from the API gateway layer.

## Context
[[Project Hub — CompassAI]] — this decision came up during the evidence endpoint
security audit when rate-limit telemetry was being added.

## Reasoning
Latency isolation: auth path and data path have different SLA requirements.
Independent scaling: auth service can be scaled without coupling to API deploy cycles.
Test isolation: auth logic stays testable independently of gateway routing.

## Alternatives Rejected

**Unified middleware:**
Rejected because it couples deploy cycles — a change to auth requires redeploying
the gateway, and vice versa. Also adds latency on every request, not just auth ones.
Profiled at +18ms median on the evidence ingest path.

**Auth-in-gateway:**
Rejected because it obscures auth logic from the backend team. Makes unit testing
harder (can't test auth without spinning up the gateway mock). Discovered during
the initial security review that this pattern makes CORS enforcement ambiguous.

## Open Questions
- [ ] Whether internal service-to-service calls should bypass gateway or proxy through
- [ ] Token refresh: handle at gateway or push to client?

## Links
[[Active Constraints — CompassAI]] · [[Decision — Rate Limit Telemetry Scope]]
```

---

## Why each section is there

**`## Decision`** — one sentence, no hedging. If you can't write the decision in one sentence, it's not a decision yet.

**`## Context`** — links back to the project hub and names the moment when this decision was made. Gives the agent temporal and project context so it understands why this mattered when it mattered.

**`## Reasoning`** — the affirmative case. What made the chosen option correct. Keep it to 3-5 sentences. If it's longer, you're defending a bad decision.

**`## Alternatives Rejected`** — the section that does the actual work. Name each alternative, give a specific reason it was rejected, and include any concrete data if you have it (latency numbers, test failure rates, code review findings). Generic rejections ("too complex") don't help the agent or future-you. Specific rejections do.

**`## Open Questions`** — the uncertainty that this decision leaves open. Checked off when resolved, linked to a new decision note when they become a decision.

**`## Links`** — inline links to adjacent notes. The decision log is useless if it's an orphan. It needs to be reachable from the project hub and linked to the constraints it produced.

---

## How the agent uses it

When you wire the decision log into your project hub:

```markdown
# Project Hub — CompassAI

## Decisions
[[Decision — Auth Layer Scope]]
[[Decision — Rate Limit Telemetry Scope]]
[[Decision — DB Schema for Evidence Records]]
```

And your `CLAUDE.md` points to the hub, the agent traverses this graph at the start of each session. It reads the decision log before making architectural suggestions. It sees "Unified middleware — rejected because it couples deploy cycles" and doesn't propose unified middleware.

The rejection is visible before the suggestion happens. The proposal never surfaces.

---

## The pattern that makes this work at scale

A single decision log is useful. Twenty linked decision logs are a project memory.

The key discipline: **create a decision log every time you make a non-trivial architectural, product, or process decision** — not just the big ones. A decision about which HTTP status code to return on a specific error condition is worth logging if you spent more than five minutes reasoning about it.

The cost is ~5 minutes per decision at creation time. The return is every future session where the agent doesn't re-open a closed question.

---

## The two mistakes that break this

**Mistake 1: Rejected alternatives without specific reasons.**

"Auth-in-gateway: rejected — too complex" tells the agent nothing it can reason from. The agent doesn't know what "too complex" means in this context. The next session it might propose auth-in-gateway again because the complexity trade-off looks different with a different feature set.

"Auth-in-gateway: rejected — obscures auth logic from backend team, makes unit testing without gateway mock impractical, causes CORS ambiguity during security review" is specific enough to foreclose the option.

**Mistake 2: Decision logs with no backlinks.**

A decision log that isn't linked from the project hub doesn't exist to the agent during traversal. It only shows up if the agent explicitly searches for it, which doesn't happen automatically. Wire every decision log into the hub under `## Decisions`. Wire the constraints it produced into `Active Constraints`. Bidirectional links mean the agent reaches it from either direction.

---

## Starting point

If you want to try this without restructuring your entire note system: just create one Decision Log for the last significant architectural decision you made on your current project.

Use the format above. Write the "Alternatives Rejected" section even if it feels like overkill. Link it back to whatever project hub or `CLAUDE.md` you already have.

Run one session with the agent, give it access to that note, and watch whether it proposes the rejected alternative.

If it doesn't — that's the pattern working.

---

The full vault structure (hub templates, all note types, linking discipline, skill guides, optional local runtime) is packaged as a $49 template: **[Obsidian Agent Vault](https://pharosml.gumroad.com/l/kvbhdo)**

The Decision Log template ships as part of it, along with the other three note types (project hub, active constraints, open questions). But the format above is enough to start.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
