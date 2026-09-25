# Kairos design iteration: the decision queue

Status: proposal for review. Date: 2026-09-24. No source file was changed to write this.
Code references are to the working tree on branch `claude/creator-subscription-automation-julwbc`, including uncommitted edits. Lines marked TODAY describe the current code. Everything else is PROPOSED.

## 1. Summary

Three directions were judged: an owner-first decision queue, an onboarding-first wizard, and a calendar-centric planner. The winner is the **decision queue** ("À décider / To decide"), with two grafts:

- From onboarding-first: setup is a forced, resumable sequence that shows a **sample week of real drafts before asking for a channel**, and the account carries a `setup_state`.
- From calendar-centric: a **pre-flight publish check** on every approved post, a **held** slot status with a stored reason, deep-linkable slot and decision URLs, and a calendar side sheet that reuses the queue cards.

The queue is also the contract for the MCP server: `list_decisions` and `resolve_decision` are the same actions the owner takes on screen, through one gated path.

Nothing in this design works until the **gate fix** ships. TODAY there is no setting in which "I approve, then it posts" works:

- `src/lib/governance.ts:48` denies publishing whenever `autopilot_publishing` is 0, which is the default (`governance.ts:23`, `src/routes/accounts.ts:85`).
- `src/engines/publishing.ts:70-88` then sets the slot to `skipped`, writes an audit row, and never retries. The enqueue scan only reads `approved` slots (`publishing.ts:23`), and the idempotency key `publish:<postId>` is permanent (`publishing.ts:40`).
- With autopilot on, drafts skip review entirely (`src/engines/content.ts:52, 139, 175`).

The landing page promise "nothing goes out until you approve it" is therefore false today. That makes the gate fix the first item of iteration 1, and it needs Martin's explicit sign-off because it changes what the publish gate guarantees.

## 2. Scoring

Scores run from 1 to 10, and higher is better on every row. For "Build effort", a higher score means less work.

| Criterion | Decision queue | Onboarding-first | Calendar-centric |
|---|---|---|---|
| Time to value for a new owner | 7 | 10 | 6 |
| Daily effort for the owner (low effort scores high) | 9 | 5 | 6 |
| Fit with existing API and code | 8 | 7 | 5 |
| Client demo impact | 8 | 8 | 9 |
| Build effort (proposal estimate) | 6 (24 d) | 7 (17 d) | 3 (38 d) |
| **Total / 50** | **38** | **37** | **29** |

Why each score:

- **Decision queue.** It fixes the problem owners have every week: they have to visit four pages to find out whether anything needs them (`frontend/src/components/DashboardShell.tsx:94-98`). Its setup-as-cards is lighter than a full wizard, so time to value comes in below onboarding-first. API fit is high because the aggregator mostly reads tables that already exist (slots, posts, conversations, reply_drafts, audit_events). It resolves through routes that already exist: `POST /v1/posts/:id/approve` already accepts a body (`src/routes/workspace.ts:76, 91-93`) and so does `POST /v1/replies/:id/approve` (`src/routes/inbox.ts:69, 85`).
- **Onboarding-first.** It has the best first 10 minutes. After setup, though, the owner is back on today's five pages, so daily effort barely improves. Its sample week needs a draft path that runs without a channel or slot, because the planner requires a connected channel (`src/engines/strategy.ts:70-77`). That path is new infrastructure.
- **Calendar-centric.** It demos best, since a week grid is easy to read in a pitch. It is the most expensive option, it is cramped on phones, and messages do not map to days: conversations have no `post_id` today. It also needs a new slot-lifecycle API and has to handle collisions on the unique (channel_id, scheduled_for) index.

The queue wins because it improves the week-to-week experience, and that experience decides whether the owner keeps paying. Its weak spot, time to value, is exactly what the onboarding graft fixes.

## 3. Chosen information architecture

Top level. Phones get a bottom bar with 3 tabs. Desktop gets a left rail.

1. **À décider / To decide** (`/dashboard`, home, with a badge count). This is the only place the owner has to look.
2. **En coulisses / Behind the scenes** (`/dashboard/behind`) with 4 sub-tabs: Calendrier / Calendar, Publié / Published, Journal / Activity, Résultats / Results.
3. **Réglages / Settings** (`/dashboard/settings/*`): Entreprise et voix / Business and voice, Sujets / Topics, Réseaux / Channels, Contrôle / Autopilot, Forfait / Plan and billing, Langue / Language, Connexion / Sign-in.

Routing rules:

- If `setup_state` is not `complete`, the home queue shows only setup cards (graft from onboarding-first). Other tabs stay reachable but display a "Finish setup first" banner. The owner is not hard-trapped, which protects accounts Martin configured by hand and the dev demo account.
- The URL carries state. `/dashboard?d=<decisionId>` opens one card and `/dashboard/behind/calendar?slot=<id>` opens a slot side sheet. Emails and MCP responses link to these URLs.
- Old routes redirect. `/dashboard/posts` goes to `/dashboard?kind=draft_choice`, `/dashboard/inbox` goes to `/dashboard?kind=conversation`, and `/dashboard/insights` goes to `/dashboard/behind/results`. This also removes the dead anchor at `frontend/src/app/dashboard/calendar/page.tsx:70`.

Queue item kinds, in fixed priority order (sorted by deadline within each kind):

| # | Kind | Source (TODAY) |
|---|---|---|
| a | `blocker`: setup step, channel disconnected, trial ended, paused, allowance used | strategy, pillars and channels presence; accounts.status; governance reasons (`governance.ts:44-67`) |
| b | `held_post`: approved but not posted, with a reason | slots in `skipped` (later `held`) joined to the latest `publish.blocked` audit row (`publishing.ts:77-86`) |
| c | `conversation`: lead, complaint or collab | intents that `canAutoReply` always refuses (`governance.ts:93-95`) |
| d | `reply_draft`: routine reply awaiting review | reply_drafts with status `pending` |
| e | `draft_choice`: pick 1 of 3 for a slot | slots with status `ready` |
| f | `fyi`: weekly digest, dismissible | audit_events count |

Language:

- UI locale is a new `accounts.locale` field, `fr-CA` or `en-CA`. It defaults to fr-CA and the header has a toggle. TODAY the root layout hardcodes `lang="en"` (`frontend/src/app/layout.tsx:29`).
- Content language is set per channel (`fr`, `en`, `fr_en`) and is passed into `src/ai/prompts.ts`.
- All times display in `accounts.timezone` (`src/lib/types.ts:5`). French uses the 24 h format "9 h 00" and English uses "9:00 AM".

Vocabulary, used everywhere:

| Instead of | Say |
|---|---|
| pillar | topic / sujet |
| API key (for the owner) | access key / clé d'accès |
| autopilot flags | Mode de contrôle / Control mode |
| `simulated` platform | Mode pratique, non publié / Practice mode, not posted |
| `lead` | Wants to buy / Veut acheter |
| `hostile` | Unhappy customer / Client mécontent |
| `collab` | Partnership idea / Idée de partenariat |

## 4. Screen-by-screen spec

Rules that apply to every screen:

- **Loading** uses skeletons shaped like the final cards, never the bare "Loading…" text.
- **Action errors** show as a toast on the card, with Retry. The list stays in place. TODAY an action error replaces the whole page (`frontend/src/app/dashboard/posts/page.tsx:99-101`).
- **Load errors** show "Impossible de vérifier / We could not check" with Retry. They never show an empty state.
- **Server messages** are mapped from stable error codes to FR/EN text. TODAY raw server strings are shown (`frontend/src/components/LoadState.tsx:15-16`).
- **Network failures never sign the owner out.** TODAY `verifyKey` treats any failure as a bad key (`frontend/src/lib/api.ts:87-95`), and the shell then deletes the key (`DashboardShell.tsx:34-36`).

### 4.1 To decide (home queue)

- **Layout, phone:**
  - Status strip at the top with a count, in one of four states: green "Kairos travaille / Kairos is running", amber "Configuration 2 sur 5 / Setup 2 of 5", red "En pause : essai terminé / Paused: trial ended", grey "Mode test / Test mode (DRY_RUN)" on dev.
  - Below it, one full-width card per screen, with "Suivant / Next" and swipe to move on.
  - Footer: "Prochaine action : rédiger la publication de jeudi, vers 5 h 10 / Next: draft Thursday's post, about 5:10 AM", in account time.
- **Layout, desktop:** a two-pane view. The list sits on the left with kind chips as filters, and the selected card opens on the right.
- **States:**
  - Setting up: only setup cards are shown, plus a progress strip.
  - Empty: "Rien à décider. Kairos s'occupe du reste. / Nothing to decide. Kairos is handling the rest." followed by the next 3 scheduled actions. This state is only allowed when there are no blockers.
  - Paused: the reason and a Resume or Fix button.
  - Drafting (common in agent mode): an "En rédaction / Drafting" card with live job status from `GET /v1/jobs`, reading "usually within the hour on this instance".
  - The copy "You're all caught up" is removed (`frontend/src/app/dashboard/inbox/page.tsx:66-68`).
- **Primary action:** the one button on the top card.
- **Copy notes:** every card leads with a one-line reason, for example "Publie jeudi 9 h sur LinkedIn" or "Client potentiel, il y a 2 h". There is one primary button, and at most two more actions sit behind "…". A deadline chip shows the slot time.

### 4.2 Draft choice card

- **Layout:**
  - Header: platform icon, handle, local date and time, and topic.
  - Three options, as a swipe carousel on phones and side by side on desktop. Each option is a platform-shaped preview: a counter against 280 for X, the "see more" fold for LinkedIn, a language tag, and a "Mode pratique" tag for Instagram and Threads (`src/adapters/registry.ts:10-13, 21-24`).
  - Tapping the text edits it in place, and the edit is saved as a draft edit, not an approval.
  - Secondary actions: "Autres idées / Other ideas" (redraft), the nudges Plus court / Plus chaleureux / Plus direct (shorter, warmer, more direct), and "Sauter ce jour / Skip this day" with reason chips. Skip is followed by an undo toast for 8 s.
- **States:**
  - Pre-flight line under the button (graft from calendar-centric): "Sera publié : réseau connecté, sous la limite du jour, forfait OK / Will post: channel connected, under daily limit, plan OK", or the exact blocker with a fix link.
  - Redrafting: skeleton panes that read "Option 2 sur 3 en rédaction".
  - Error: a toast with Retry.
- **Primary action:** "Publier celle-ci / Use this one". It sends the visible, possibly edited, body to `POST /v1/posts/:id/approve`. TODAY the UI sends `{}` (`posts/page.tsx:97`) even though the API accepts a body (`workspace.ts:76, 91-93`).
- **Copy notes:** the button names the time after approval: "Prévu jeudi 9 h / Scheduled Thu 9:00 AM".
- **Batch:** a week header "5 publications cette semaine" offers "Voir mes choix suggérés / Review suggested picks". It lists every post and needs one confirm. Nothing is approved blind.

### 4.3 Reply and lead card

- **Layout:**
  - Author, platform, and the intent in plain words.
  - A "Pourquoi c'est ici / Why this is here" chip, for example "Kairos ne répond jamais seul aux clients potentiels / Kairos never auto-answers leads".
  - The last 3 messages from `GET /v1/inbox/:id` (`inbox.ts:48-67`), which the UI never calls TODAY.
  - The drafted reply in an editable box, with its language shown.
  - Secondary actions: Écrire ma réponse / Write my own, Marquer traité / Mark done, Ignorer / Ignore, Ouvrir sur LinkedIn / Open on LinkedIn.
- **States:**
  - No draft: an empty composer and a "Write my own" primary action.
  - Sending: the card stays with a spinner until the send is confirmed.
  - Failed: "Non envoyé : LinkedIn est déconnecté / Not sent: LinkedIn is disconnected", with Reconnect.
- **Primary action:** "Envoyer / Send", with the visible text, through `POST /v1/replies/:id/approve` with a body.
- **Note on uncommitted work:** the working tree already adds `pending_draft_body` to the inbox list (`src/routes/inbox.ts:33-35`) and renders it (`inbox/page.tsx`, "Suggested reply"). That removes the blind send for now. It still marks the row answered optimistically, and `handleReplySend` still returns silently on a disconnected channel (`src/engines/engagement.ts:328`).

### 4.4 Held post card

- **Layout:**
  - Red edge, the post text, and the original time.
  - A headline mapped from the governance reason:
    - "Non publié : limite de 10 par jour atteinte / Not posted: daily limit of 10 reached"
    - "Non publié : LinkedIn déconnecté / Not posted: LinkedIn disconnected"
    - "Non publié : forfait du mois utilisé / Not posted: monthly allowance used"
  - Secondary actions: Replanifier / Reschedule, Abandonner / Drop it.
- **States:** retrying, which uses the new idempotency key, and resolved, which shows a success toast before the card leaves.
- **Primary action:** the fix for that reason: "Publier maintenant / Post now", "Reconnecter", "Augmenter la limite / Raise today's limit", or "Changer de forfait / Upgrade".

### 4.5 Setup cards (graft from onboarding-first)

There are five cards, forced in order and resumable across devices through `setup_state`:

1. **Langue / Language.** Three tiles: Français, English, Les deux / Both. Picking one advances immediately.
2. **Votre entreprise / Your business.**
   - Iteration 1: three short plain-language fields.
   - Iteration 2: paste a website or 3 past posts, and Kairos proposes positioning, audience, tone, proof points, CTAs and words to avoid. The owner edits them.
3. **Sujets / Topics.** 4 to 6 suggested topics with toggles, and a "moins / normal / plus" control mapped to weights 0.5, 1 and 2 (the API range is 0.1 to 3, `accounts.ts:219-223`). At least 2 must be selected.
4. **Semaine d'essai / Sample week** (iteration 2). 3 slots with 3 drafts each, drafted without a channel. The owner picks and edits them, and the picks seed the first real slots. Before iteration 2, this card is skipped.
5. **Réseau et contrôle / Channel and control.**
   - Platform tiles. X and LinkedIn are labelled "Publie pour vrai / Posts for real". Instagram and Threads are labelled "Mode pratique".
   - A posts-per-week stepper that defaults to 3.
   - The control mode radios, with "J'approuve chaque publication / I approve every post" as the default.
   - Button: "Planifier mes deux premières semaines / Plan my first two weeks" (`POST /v1/calendar/plan`, `workspace.ts:41`).
   - Until OAuth ships, the raw-token path stays behind "Avancé".

- **States:** after card 5, the queue shows "Kairos prépare vos premières publications" with job progress.
- **Error:** inline on the failing card. Retries are idempotent (Idempotency-Key on POST pillars and channels).
- **Primary action:** "C'est bien ça, continuer / Looks right, continue".

### 4.6 Settings: Contrôle / Autopilot

- **Layout:**
  - Three radio cards:
    1. "J'approuve chaque publication / I approve every post" (default).
    2. "Kairos planifie, je peux refuser jusqu'à 2 h avant / Kairos schedules, I can veto until 2 h before".
    3. "Pilote automatique complet / Full autopilot".
  - A "Pause jusqu'au / Pause until" date picker.
  - Daily caps shown as plain numbers.
  - Reply rules as a table of intents with three choices: Envoyer seul / Send on its own, Me demander / Ask me, Ignorer / Ignore. Lead, complaint and collab are locked to "Ask me", with the lock explained (`governance.ts:93-95`).
- **States:** a preview of the effect before saving: "5 publications à venir seront planifiées automatiquement".
- **Primary action:** "Enregistrer / Save". It writes `PUT /v1/controls` and `PUT /v1/reply-rules` (`accounts.ts:340`, `inbox.ts:165`) plus an Activity row.
- **Copy note:** modes 2 and 3 need a second confirm step on screen, and they can never be set from an agent key.

### 4.7 Behind the scenes: Calendar

- **Layout:**
  - A week strip on phones and a 3-week grid on desktop covering 7 days back and 14 ahead, in account time.
  - Chips show both a colour and a word, with the legend always visible.
  - Tapping a chip opens a side sheet with status, reason, history and the same queue card component.
  - Filters for channel and topic.
  - A "Fermé ce jour / Closed this day" toggle, for example for Quebec statutory holidays and the construction holiday.
- **States:** the empty state explains why ("Aucun réseau connecté") and links to the fix.
- **Primary action:** open the slot.

### 4.8 Behind the scenes: Activity, Published, Results

- **Activity.**
  - A reverse-chronological timeline in plain FR/EN built from audit_events, for example "Publication retenue : limite du jour" or "Réponse de routine envoyée à @x".
  - The empty state reads "Rien encore. Les actions de Kairos apparaîtront ici."
- **Published.**
  - A paged list with per-post results.
  - The 200-row cap goes away. TODAY that cap is at `posts/page.tsx:66` and `workspace.ts:56`.
- **Results.**
  - Two separate bars per topic: "Performance" (engagement compared with your average) and "Place accordée / Room it gets" (weight). TODAY the weight is displayed as if it were performance (`frontend/src/app/dashboard/insights/page.tsx:94`).
  - The "Hours saved" card is relabelled "30 derniers jours / last 30 days" (`workspace.ts:238`).
  - Usage bars show the reset date.

### 4.9 Settings: Plan and billing

- **Layout:**
  - Current plan, trial days left, usage bars with the reset date, and CAD prices "taxes en sus (TPS/TVQ)" from `GET /v1/plans` (`src/routes/billing.ts:94`).
  - A Stripe portal button.
- **States:**
  - Trial ending in 3 days or less: a blocker card on the queue.
  - Trial ended: a red status strip.
- **Primary action:** "Choisir un forfait / Choose a plan" before payment, and "Gérer la facturation / Manage billing" after.
- **Return URLs:** Stripe returns here instead of the API-origin HTML pages (`src/engines/billing.ts:61-62`, `src/routes/billing.ts:50-84`).

### 4.10 Sign-in and landing

- **Sign-in:**
  - Iteration 1 keeps the access key, but with no sign-out on network errors, a confirm before signing out, and a link back to home and to "Demander l'accès".
  - Iteration 3 adds an email magic link. Keys become MCP and device credentials only.
- **Landing:**
  - FR-first hero: "Kairos prépare vos publications. Vous décidez en un geste."
  - A queue screenshot and an honest network list.
  - An invite form stored server side, replacing the mailto (`frontend/src/components/SignupDialog.tsx:104-118`).
  - Privacy and terms links (Law 25).
  - The line "nothing goes out until you approve it" only ships after the gate fix.

## 5. Flows

### 5.1 Onboarding (first sign-in)

1. The owner signs in. The shell reads `setup_state` from `GET /v1/me` and the queue shows setup card 1 of 5.
2. The owner picks a language. The client calls `PATCH /v1/account {locale, contentLanguage}`, the UI switches language, and `setup_state` becomes `business`.
3. The owner fills in Business: 3 fields in iteration 1, or a pasted URL or posts followed by `POST /v1/strategy/suggest` in iteration 2. They edit the result and confirm. The client calls `PUT /v1/strategy`.
4. The owner toggles the suggested topics, sets weights and confirms. The client calls `POST /v1/pillars` once per topic, with an Idempotency-Key.
5. (Iteration 2) Sample week: `POST /v1/onboarding/sample-week` queues 3 x 3 drafts with no channel. Panes fill in progressively. The owner picks and edits, and the picks are stored.
6. The owner connects a channel, sets posts per week, and keeps "I approve every post". The client calls `POST /v1/channels`, then `PUT /v1/controls {mode:'manual'}`, then `POST /v1/calendar/plan`.
7. The queue switches to "Kairos prépare vos premières publications" with job progress. When the drafts are ready, draft choice cards appear.

### 5.2 Daily review

1. The owner opens `/dashboard`, and the status strip reads green with a count of 3.
2. The top card is a held post: "Not posted: LinkedIn disconnected". The owner taps Reconnect. The card clears once the channel status is `connected` and the post is re-enqueued.
3. The next card is a draft choice for Thursday. The owner swipes to option 2, edits one word, and sees the pre-flight line "Will post". They tap "Use this one". The client calls `POST /v1/decisions/:id/resolve {action:'approve', body}`, which calls the approve logic. A toast confirms "Scheduled Thu 9:00 AM" and the card leaves.
4. The next card is a routine reply draft. The owner reads it and taps Send. The card shows "Sending…", then clears when `reply.sent` is confirmed.
5. The queue is now empty: "Nothing to decide", with the next 3 scheduled actions.

### 5.3 Replying to a lead

1. The inbound DM is classified as intent `lead`. `canAutoReply` refuses (`governance.ts:93-95`), and a reply draft is created as `pending`.
2. A `conversation` card appears at priority c: "Veut acheter · @boulangerie_x · il y a 2 h", with the chip "Kairos never auto-answers leads".
3. The owner reads the thread excerpt (the last 3 messages) and the draft in the editable box. They adjust the price mention.
4. The owner taps Send. The client calls `POST /v1/decisions/:id/resolve {action:'send', body}`. The server re-checks the account status, pause, the daily reply cap and channel connection, then enqueues `reply.send`.
5. On success, the card clears and Activity logs "Réponse envoyée à @boulangerie_x (par vous)".
6. On failure, the draft is marked `failed` with a reason. The card stays, turns red "Non envoyé : …", and offers the fix.

### 5.4 Changing autopilot

1. The owner opens Settings, then Contrôle. The screen reads the current mode from `GET /v1/controls`.
2. The owner selects "Kairos schedules, I can veto". The preview reads "5 upcoming posts will be auto-scheduled; you can refuse until 2 h before each".
3. The owner taps Save, and a confirm dialog repeats the effect in one sentence. The owner confirms.
4. The client calls `PUT /v1/controls {mode:'veto_window', vetoHours:2}`. The server maps the mode onto the existing flags, audits `controls.changed`, and Activity shows "Vous avez choisi : Kairos planifie, vous pouvez refuser".
5. From then on, draft choice cards show "Auto-planifié, touchez pour changer" and have a deadline chip at the veto cutoff.
6. When the request comes from an agent (MCP) key, it gets a 403 `controls_owner_only` for modes 2 and 3.

## 6. API changes required

Shapes are sketches. All routes are account-scoped behind the existing auth. Error responses carry a stable `code` alongside the message.

| # | Endpoint | Request | Response | Iter |
|---|---|---|---|---|
| 1 | **Gate fix** in `canPublish` (`governance.ts:43-70`) | none | Skip check 3 when `post.approved_by` starts with `key:` and mode is `manual` or `veto_window`. Keep status, pause, daily cap and monthly allowance. The signature becomes `canPublish(env, account, post)` | 1 |
| 2 | Held status in `handlePublishDispatch` (`publishing.ts:70-88`) | none | Set the slot to `held` (new status; needs a migration if statuses are CHECK-constrained) with `hold_reason_code`. Re-enqueue with key `publish:<postId>:<attempt>` | 1 |
| 3 | Reply send recheck in `handleReplySend` (`engagement.ts:300-369`) | none | Re-check status, `paused_until`, the reply cap and the allowance. On a disconnected channel, set the draft to `failed` with `fail_reason_code` instead of returning silently (`:328`) | 1 |
| 4 | `GET /v1/decisions?kind=&cursor=` | query | `{items:[{id, kind, priority, deadline, reasonCode, payload, actions:[{id, label_key, primary}]}], counts:{…}, status:{state:'running'|'setup'|'paused'|'test', nextAction}}`. The id is `kind:entityId` | 1 |
| 5 | `POST /v1/decisions/:id/resolve` | `{action, body?, reason?}` | `{ok, result:{…}, nextDecisionId?}`. Dispatches to the existing approve and reject handlers and writes one audit row | 1 |
| 6 | `GET /v1/posts/:id/publish-check` | none | `{willPublish:boolean, checks:[{code, pass}]}`, a dry run of `canPublish` | 1 |
| 7 | `POST /v1/posts/:id/retry` | none | `{jobId}`, re-enqueue with a new key | 1 |
| 8 | `GET /v1/strategy`, `GET /v1/controls`, `GET /v1/channels` | none | The saved objects (only PUT/POST exist today, `accounts.ts:183, 266, 340`) | 1 |
| 9 | `setup_state` on `GET /v1/me`; `PATCH /v1/account {locale, contentLanguage, setupState}` | JSON | Updated account. Backfill `complete` where a strategy, a topic and a channel all exist | 1 |
| 10 | Idempotency-Key header on `POST /v1/pillars`, `POST /v1/channels` | header | Same response on replay | 1 |
| 11 | `GET /v1/jobs?kind=&status=` | query | `[{id, kind, status, createdAt, entityId}]` | 1 |
| 12 | `PUT /v1/controls {mode:'manual'|'veto_window'|'autopilot', vetoHours?, pausedUntil?, caps?}` | JSON | Controls. Maps onto the existing flags. `content.ts:52, 139, 175` auto-approves only in `autopilot`, and `veto_window` auto-approves with a cutoff | 2 |
| 13 | `PATCH /v1/posts/:id {body, hook}`, `PATCH /v1/replies/:id {body}` | JSON | The draft, still in draft status | 2 |
| 14 | `POST /v1/slots/:id/redraft {nudge?, reason?}` | JSON | `{jobId}`, metered through `canGenerate` | 2 |
| 15 | `PATCH /v1/slots/:id {scheduledFor?, status?:'closed'|'cancelled'}` | JSON | Slot, or 409 on a (channel_id, scheduled_for) collision | 2 |
| 16 | `POST /v1/conversations/:id/status {status:'done'|'ignored'}`, `POST /v1/conversations/:id/replies {body}` | JSON | Conversation, and a queued send | 2 |
| 17 | `PATCH`/`DELETE /v1/pillars/:id`, `GET /v1/reply-rules`, `PATCH`/`DELETE /v1/channels/:id` | JSON | Updated objects (auth is already mounted on `/v1/pillars/*`, `accounts.ts:152`) | 2 |
| 18 | `GET /v1/activity?cursor=` | query | `[{at, actor, action, entity, reasonCode}]`. The client maps it to FR/EN | 2 |
| 19 | `GET /v1/calendar?from=&to=&channel=&pillar=` | query | Adds a lower bound (none today, `workspace.ts:24-35`) and includes the hold reason | 2 |
| 20 | `POST /v1/strategy/suggest {url?, samplePosts?}` | JSON | `{jobId}`, then the result `{strategy, pillars}`. SSRF-safe fetch, metered, capped | 2 |
| 21 | `POST /v1/onboarding/sample-week`, `…/:id/regenerate` | JSON | `{jobId}`. Uses a separate `sample_drafts` table with no path to `publish.dispatch`. Capped at 2 runs | 2 |
| 22 | Prompt change: `content_language` on channels plus a strategy default, honoured in `src/ai/prompts.ts` | none | Drafts in Quebec French when chosen | 2 |
| 23 | `POST /v1/access-requests` (public, Turnstile, rate limited), `POST /v1/admin/invites` (operator) | JSON | `{ok}` | 3 |
| 24 | `POST /v1/auth/link`, `GET /v1/auth/callback`, `GET`/`DELETE /v1/keys`, key scopes (`read`, `draft`, `approve`, `controls`) | JSON | Session and key list | 3 |
| 25 | `POST /v1/billing/portal`; return URLs moved to the dashboard | none | `{url}` | 3 |
| 26 | Daily digest email (Cloudflare Email Service) with `/dashboard?d=` links | none | none | 3 |
| 27 | MCP server over the same routes: `list_decisions`, `get_decision`, `resolve_decision` (two-step confirm token), `edit_draft`, `redraft_slot`, `get_activity`, `get_results`, `pause_until`, `update_voice`, `manage_topics`, `plan_now`. Agent keys can never raise caps or choose modes 2 and 3 | none | none | 3 |

## 7. Build plan

Each iteration ends in a working, demo-able state on CT920 (DRY_RUN=true, agent mode). Effort is engineer-days.

### Iteration 1: "It tells the truth and it posts what you approve" (about 9 days)

| Item | Days |
|---|---|
| Gate fix plus `held` status plus retry key, with one test per `canPublish` check and approved_by `key:*` vs `autopilot` (API 1, 2, 6, 7) | 2 |
| Reply send recheck and failed state (API 3) | 0.5 |
| `verifyKey` no longer signs out on network errors, and sign-out asks for confirmation | 0.5 |
| `GET /v1/decisions` plus resolve dispatcher, tested per kind (API 4, 5) | 2 |
| Read-backs, `setup_state`, idempotent pillars and channels, jobs read (API 8 to 11) | 1 |
| Queue home: status strip, cards for blocker, held_post, conversation, reply_draft and draft_choice (with inline edit sent as the approve body), empty, loading and error states | 2 |
| Setup cards 1, 2, 3 and 5 (manual forms, no inference, raw handle path in dev), FR/EN strings for the queue and setup only, account-time display | 1 |

Demo script: sign in with the demo account and watch setup show 4 cards. Complete them and plan. Watch "Drafting…" resolve into draft cards. Edit and approve one. In DRY_RUN it publishes. Disconnect the channel and watch a held card appear with a Reconnect fix.

Not in iteration 1: autopilot modes UI (the default stays manual, which now works), inference, sample week, calendar redesign.

### Iteration 2: "Setup in 10 minutes, control you understand" (about 9 days)

- Voice suggestion from a URL or posts, with SSRF hardening, metering and caps: 2 days.
- Sample week before the channel, then seeding the first slots from the picks: 2 days.
- Control modes screen plus the mode mapping in content.ts: 1.5 days.
- Draft edit, redraft and nudges, skip with undo and reason, conversation done and ignore, write my own: 1.5 days.
- Behind the scenes: calendar with past days, legend, side sheet and closed days, plus Activity: 1.5 days.
- Content language in prompts, reviewed by a native Quebec speaker: 0.5 days.

Demo: paste a Quebec business website, get a French voice and a sample week in minutes, switch to veto mode, and show the Activity timeline.

### Iteration 3: "Ready for strangers on kairos.pharos-ai.ca" (about 8 days)

- Magic-link sign-in, scoped keys and revoke: 2 days.
- Invite form plus operator approve: 1 day.
- Billing page, Stripe portal, return URLs, trial blocker cards: 1.5 days.
- Daily digest email with deep links, including SPF and DKIM on pharos-ai.ca: 1 day.
- MCP server v1 over the decisions API, with a two-step confirm: 1.5 days.
- FR-first landing, honest networks, privacy and terms: 1 day.

Demo: a new visitor requests access, Martin approves, the visitor signs in by email and finishes setup, then Claude (through MCP) lists decisions and resolves one after the owner confirms.

Total: about 26 days. That is slightly above the queue proposal's 24 days because of the grafted sample week and pre-flight check.

## 8. Risks and mitigations

- **The gate change redefines "autopilot off".** Mitigation: explicit sign-off, per-check tests, and the landing copy changes in the same release.
- **Queue overload** (14 slots x 3 variants plus inbox). Mitigation: week grouping, "Review suggested picks" with one visible confirm, and veto mode.
- **One tap makes blind taps easier.** Mitigation: leads and complaints always show the text, batch approval lists every post, and MCP needs a confirm token.
- **The aggregator is a single point of truth.** Mitigation: tests per kind, and a failure shows "We could not check", never "nothing to decide".
- **Agent-mode latency on CT920.** Mitigation: real job status is required before any demo. Measure p50 and p95 drafting time first.
- **Simulated Instagram and Threads.** Mitigation: a "Mode pratique" label on every card, calendar chip and result.
- **Quebec French quality and Bill 96 / Law 25.** Mitigation: native review of UI and prompt output, French privacy policy and terms, and a named privacy officer before public launch on CT947.

## 9. Open questions for the owners

1. Do you approve the gate change, so that a post you approved publishes with autopilot off while pause, caps and allowance still apply?
2. What should happen to posts that were approved and then silently skipped before the fix? Options are to show them as held cards, or to drop them.
3. What is the default content language for new Quebec accounts: French only, or French then English?
4. What veto window should mode 2 use: 2 h, 24 h, or owner-set?
5. Should an MCP agent key ever be allowed to approve posts or send replies after a confirm, or only draft and read?
6. Which email address and domain should send magic links and digests, and who is the named Law 25 privacy officer?
7. Should prices display in CAD before public launch, and is a card required for the trial?
8. Does "Closed this day" need a built-in list of Quebec holidays (including the construction holiday), or should owners set it manually?
9. Before OAuth, is the raw-token channel path acceptable for invited pilot clients, or should Martin connect channels for them?
10. What sample-week cap per trial account is acceptable, given the model spend before payment?
