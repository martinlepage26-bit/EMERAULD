# KAIROS: 90 days to $50,000 MRR

One operator, no employees, AI tooling, ninety days.

## The finding that should shape everything else

$50,000 of monthly recurring revenue is not one target. It is two very different businesses depending on who you sell to, and only one of them is reachable in ninety days by a single person.

| Path | Accounts needed | Closes per working day | Verdict |
|---|---|---|---|
| Solo creators at $49 | 1,020 | 15.7 | Not reachable |
| Mixed self-serve, ARPU ~$175 | 287 | 4.4 | Reachable only with an existing audience |
| Concentrated, ARPU ~$395 | 127 | 2.0 | **Reachable** |

The volume path fails on arithmetic before it fails on effort. At a 3% trial-to-paid conversion rate, which is normal for self-serve creator tools, 1,020 paying solo accounts requires about 34,000 trials in ninety days. Nobody generates that from a standing start without either a large existing audience or paid acquisition spend that the plan does not have.

The concentrated path needs 127 customers. That is two closes per working day, which is an ordinary founder-led sales cadence.

So the strategy is: **sell to people who manage other people's accounts.** An agency running fifteen client accounts feels the scheduling and reply burden fifteen times over, has a budget line for tools, and evaluates on hours saved rather than on price. The same product, positioned at the same build cost, produces a twenty-fold difference in ARPU depending on which buyer you point it at.

## Target mix at day 90

| Plan | Price | Accounts | MRR |
|---|---|---|---|
| Agency | $999 | 25 | $24,975 |
| Studio | $399 | 40 | $15,960 |
| Pro | $149 | 62 | $9,238 |
| **Total** | | **127** | **$50,173** |

Solo at $49 stays in the product but is not a target segment. It exists as the trial landing spot and the referral surface, and some Solo accounts grow into Pro. Treating it as a revenue line is what pulls a solo founder into supporting a thousand low-value accounts.

## The three phases

### Days 1 to 30: prove the product on ten accounts you recruited by hand

The goal of month one is not revenue. It is a working system with real creators on it, because everything in months two and three is sold on evidence produced here.

Ship in this order, because each unlocks the next:

1. Onboarding, planning, and drafting with autopilot off. A creator connects a channel, sees a filled calendar within minutes, and approves posts by hand. This alone is demonstrable value and carries no risk of publishing something embarrassing.
2. Publishing with autopilot, gated by the daily caps in `automation_controls`.
3. Inbound triage and reply drafting, still review-only.
4. Metrics collection and the growth rebalance loop.

Recruit ten creators directly. Not a waitlist, not a launch: ten individual conversations with people who currently spend hours a week on this. Give them the product free for the ninety days in exchange for the right to use their numbers.

**Exit test for month one:** at least six of the ten have autopilot publishing on and have left it on for two consecutive weeks. If creators keep autopilot off, they do not trust the drafts, and no amount of selling fixes that. That is a product problem and month two should be spent on it instead.

### Days 31 to 60: convert the evidence into agency deals

Now the product has thirty days of real output, and the `/v1/insights` endpoint can state hours saved with its arithmetic shown rather than as a marketing claim.

Agencies are the month-two focus, because a single Agency close is worth twenty Solo closes and takes roughly three conversations.

The motion, run daily:

- Two outbound conversations per working day with agency owners, sourced from the client lists of the ten pilot creators, from agency directories, and from the communities the pilot creators are already in.
- The demo is not a feature tour. It is: connect one of their real client accounts, generate the calendar live, and let them read what it drafted in their client's voice. The product either survives that or it does not.
- Price on their cost of labour. An agency paying someone $3,000 a month to schedule and reply is evaluating $999 against $3,000, not against $49.

Ship in month two what agencies specifically need and solo creators do not: multi-account switching, per-client approval queues, and a white-label view.

**Exit test for month two:** $15,000 MRR, with at least 8 Agency accounts. If Agency closes are not happening but Studio closes are, the wedge is wrong and month three should push Studio instead. That is a real possibility and the plan should not resist it.

### Days 61 to 90: make the system sell itself

Month three is where the compounding mechanisms have to carry weight, because two closes a day does not scale past one person.

Three loops, in order of expected contribution:

**Referral.** Already built: a referral qualifies when the referred account pays, not when it signs up, because rewarding signups pays for fake accounts. An agency that refers two peers is worth more than a month of outbound.

**Proof pages.** Each creator gets a public page showing what the system produced for them. This is the honest version of a viral loop: it is useful to the creator as a portfolio and it is a persistent inbound surface. It requires no new persuasion from the operator.

**The product's own output.** KAIROS runs the KAIROS account. Every post is a live demonstration, and the cost is zero because the system is already built.

**Exit test for month three:** $50,000 MRR, and more importantly, at least 30% of new accounts arriving from referral or inbound rather than outbound. Hitting the revenue number entirely through founder outbound means day 91 starts from the same place as day 61.

## Weekly operating rhythm

The system is designed so that operating it is a fixed cost in hours rather than a growing one:

| Cadence | Work |
|---|---|
| Daily, 30 min | Review the dead-letter queue at `/health`. Any job in `dead` is a creator whose post did not go out. |
| Daily, 2 hours | Sales conversations. This is the only line that does not compress. |
| Weekly, 1 hour | Read the audit log for `publish.blocked` and `reply.queued_for_review`. Blocked publishes are where the governance gates are miscalibrated. |
| Weekly, 2 hours | Ship one thing that removes a support question permanently. |
| Monthly | Re-derive `docs/UNIT-ECONOMICS.md` against actual token spend from `usage_counters`. |

## What has to be true, and how you will know it is not

Stating these in advance is what makes them useful. Each has a date and a response.

**Creators will leave autopilot on.** The whole value proposition collapses if every post needs approval, because then the product saves minutes rather than hours. Measured by the autopilot-on rate among active accounts. Check at day 30. If it is below 60%, stop selling and fix draft quality.

**Agencies will pay $999.** Measured by close rate on agency conversations. Check at day 45. Below 10% after twenty conversations means the price or the buyer is wrong; test $499 with more accounts before concluding the segment is dead.

**Churn stays under 5% monthly.** A subscription business at 10% monthly churn cannot compound, and at 127 accounts you would be replacing six a month just to stand still. Check at day 60, once the first cohort has had a renewal decision.

**One person can support 127 accounts.** Measured by support hours per week. Check continuously. Above ten hours a week, the next build item is whatever is generating the tickets, not the next feature.

## The honest risks

**Platform API access is the existential one.** X and LinkedIn both restrict automated posting and both have changed terms with little notice. The adapter layer isolates this, and the simulation path means the product still functions if an API closes, but a platform ban would remove a channel and the customers who came for it. Mitigation is breadth across platforms and not letting any one exceed half of publishing volume.

**Automation quality is reputational, and the reputation at risk is the creator's, not yours.** This is why `governance.ts` refuses to auto-send replies to leads, collaborations, and hostile threads regardless of configuration, and why the banned-phrase list is enforced in code after generation rather than trusted to the prompt. One publicly embarrassing auto-reply costs more than a month of sales.

**Ninety days is aggressive and the plan should be read as such.** The concentrated path is reachable, not likely. The most probable outcome is somewhere between the day-60 and day-90 targets, arriving around day 120. A plan that only works if every phase hits on schedule is not a plan. The phase exit tests exist so that a miss is detected in week five rather than week twelve, when there is still time to change the approach rather than just the effort.
