# KAIROS unit economics

Every number below is derived, not asserted. Where a figure is an assumption rather than a measurement, it says so. Re-run this model whenever plan limits, model pricing, or the prompt structure changes, because all three move gross margin directly.

## Input prices

Claude Opus 5, per million tokens:

| Token class | Price |
|---|---|
| Input (uncached) | $5.00 |
| Output | $25.00 |
| Cache read | $0.50 |
| Cache write | $6.25 |

## Why the cached prefix is the whole cost story

Every generation call is assembled in stability order: an operator system prompt identical across all accounts, then the creator's strategy, then the volatile request. The first two are roughly 1,500 tokens and carry a cache breakpoint.

Without caching, those 1,500 tokens cost $0.0075 per call at full input price. With caching they cost $0.00075. At 300 accounts each making perhaps 900 calls a month, that difference alone is about $1,800 a month, which is the margin on ten Pro accounts.

This is also why `OPERATOR_SYSTEM` is marked as a deploy-level edit in the source. Changing one character invalidates every cached prefix in the fleet at once.

## Cost per operation

**Drafting one slot (three variants):**

| Component | Tokens | Cost |
|---|---|---|
| Cached prefix read | 1,500 | $0.00075 |
| Fresh input (angle, platform rules, past winners) | ~700 | $0.0035 |
| Output including thinking | ~1,800 | $0.045 |
| **Total** | | **~$0.049** |

**One reply (triage call plus drafting call):**

| Component | Cost |
|---|---|
| Triage at low effort | ~$0.012 |
| Reply draft at medium effort | ~$0.018 |
| **Total** | **~$0.030** |

**Calendar planning:** roughly $0.08 per channel per run, at high effort, running about twice a month per channel.

Two things follow. Replies are cheaper per unit than posts but far more numerous, so replies drive the cost of any heavy account. And output tokens dominate everything, which means effort level is the strongest cost lever in the system, well ahead of prompt trimming.

## Gross margin by plan, at full consumption

Stripe is charged at 2.9% plus $0.30. This is the pessimistic case: an account that consumes its entire monthly allowance.

| Plan | Price | Posts | Replies | AI cost | Stripe | COGS | Gross margin |
|---|---|---|---|---|---|---|---|
| Solo | $49 | 60 | 200 | $9.35 | $1.72 | $11.07 | **77.4%** |
| Pro | $149 | 200 | 800 | $34.88 | $4.62 | $39.50 | **73.5%** |
| Studio | $399 | 700 | 2,000 | $97.64 | $11.87 | $109.51 | **72.6%** |
| Agency | $999 | 2,000 | 5,000 | $258.80 | $29.27 | $288.07 | **71.2%** |

Every tier clears 70% at full consumption. That threshold is why the Studio and Agency reply allowances are set where they are: the first pass at this model gave Agency 8,000 replies and 2,500 posts, which put it at 59.7%, and the allowance was cut rather than the margin claim softened.

## Gross margin at realistic consumption

Allowance-cap usage is rare. Assuming accounts consume about 40% of their quota, which is typical for scheduling tools, blended gross margin lands near **88%**. The full-consumption table is the floor, not the forecast.

The gap between the two matters operationally: it means a small number of power users cannot threaten the business, because even at 100% consumption they are profitable.

## Infrastructure

Cloudflare Workers Paid is $5 a month. D1, R2, and KV at 300 accounts stay inside or just above free tiers. Budget $150 a month at the 90-day scale, which is a rounding error against $50,000 MRR and is the main argument for the Workers stack over a conventional server deployment.

## Contribution margin at the $50,000 target

Using the concentrated mix from the 90-day plan (25 Agency, 40 Studio, 62 Pro):

| Line | Monthly |
|---|---|
| Revenue | $50,173 |
| AI and Stripe at 40% consumption | ~$6,000 |
| Infrastructure | ~$150 |
| **Contribution** | **~$44,000** |

No salaries, because there are no employees. That is the whole point of the constraint: the plan reaches $50,000 MRR with roughly $44,000 a month of contribution rather than the $10,000 or so that the same revenue would produce with a team of four.

## What breaks this model

Three things, in order of likelihood.

**Reply volume outruns the estimate.** A creator whose account genuinely receives thousands of inbound messages a month is the margin risk, and the allowance caps in `PLANS` are the control. The caps are enforced in `governance.ts`, not merely displayed, which is the difference between a limit and a hope.

**Effort levels drift upward.** Every engine sets `output_config.effort` explicitly: planning at high, drafting at medium, triage at low. Raising drafting to high would add roughly 40% to the largest cost line in the system. Any change there should be justified by a measured quality difference, not a hunch.

**Model price changes.** The model id is an environment variable per deployment rather than a constant, so a change is a config edit. The numbers in this document would need re-deriving.
