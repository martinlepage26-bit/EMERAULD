# Kairos Sales Page Spec: "Tabloid Front Page"

Status: spec, not yet built. Replaces the copy and layout of `frontend/src/app/page.tsx`.
Reader we write for: a 55-year-old plumber in Laval who is not good with computers, feels guilty he never posts, and reads French first.
Style: a UK tabloid front page. One huge headline. Short sentences. Words a 12-year-old knows. Honest.

---

## 1. Scoring of the three drafts

Scored 1 to 10 from the plumber's point of view.

| Criterion | A: Tabloid front page ("SOCIAL MEDIA? SORTED.") | B: Your mate over a beer (before/after week) | C: Problem, then relief ("YOUR FACEBOOK PAGE IS EMPTY") |
|---|---|---|---|
| Understood in 5 seconds | 9 | 7 | 9 |
| Trust (no hype, honest) | 7 | 6 | 8 |
| Makes me want to try it | 8 | 8 | 8 |
| Simplicity of words | 8 | 9 | 9 |
| Bilingual fit | 8 | 6 | 7 |
| **Total / 50** | **40** | **36** | **41** |

Why:

- **A** has the cleanest headline and the best structure (THE FACTS box, masthead with a visible EN / FR switch, full pricing with message limits). It loses trust points for the red "EXCLUSIVE" flash (pure hype, nothing is exclusive) and for "most local shops only need SOLO" (an unproven claim). Its French headline is the strongest of the three.
- **B** has the most human writing and the best "you're still the boss" list, plus the honest "We can't promise more customers" answer. It loses on trust because the invented neighbour will be read as a testimonial however much small print is added, and because the closing headline promises "back up and running by next week". Its French headline only works if the page is Facebook and the month is March, so it does not travel.
- **C** has the best "why" section ("You're not lazy. You're busy." / "Which one would you call?") and the calmest tone. It loses a little on bilingual fit (it answers "Yes" to French before that is confirmed) and on trust for the "MOST SMALL SHOPS START HERE" arrow. It also slips between "we" and "Kairos", which confuses who is doing the work.

**Verdict:** A's frame and hero, C's "why", B's control list and honest FAQ answers, with B's before/after week kept only as a generic "your week" (no invented person).

---

## 2. Headline

**Chosen:** `SOCIAL MEDIA? SORTED.`
**French:** `RÉSEAUX SOCIAUX? C'EST RÉGLÉ.`

Why it wins: three words, read in one glance, names the problem and the relief together, and names no network we have not confirmed. The French version is just as short and sounds natural in Quebec.

**A/B alternates:**

1. `STOP FEELING GUILTY ABOUT FACEBOOK` (FR: `ARRÊTEZ DE VOUS SENTIR COUPABLE POUR FACEBOOK`). Goes straight at the guilt. [CONFIRM: Facebook is connected today before running this one.]
2. `YOUR PAGE IS EMPTY. YOUR CUSTOMERS NOTICED.` (FR: `VOTRE PAGE EST VIDE. VOS CLIENTS L'ONT REMARQUÉ.`). Sharper, fear-led. Test against the chosen headline to see whether relief or worry gets more invite requests.

Test one alternate at a time against the chosen headline. Measure invite requests, not clicks.

---

## 3. Design system (applies to every section)

- **Headline type:** very large, heavy, condensed sans-serif in capitals (for example Anton, Oswald 700 or Bebas Neue). Hero headline fills the full width of the screen: about `clamp(3rem, 14vw, 9rem)`, line-height 0.9, tight letter-spacing.
- **Body type:** a plain, readable serif or sans at 18px minimum on mobile (20px on desktop). Line length 60 characters or less. No light grey text; body is near-black on white.
- **Colour:** black and white only, plus **one accent: tabloid red (`#E10600`)**. Red is used for step numbers, the main button and at most one underline or circle per section. No gradients. No second accent (drop the yellow buttons from drafts A and C).
- **Rules and boxes:** thick black rules (4px) between sections, like newspaper columns. Boxed items (THE FACTS, the control checklist) use a 4px black border and no rounded corners.
- **Buttons:** big, square-cornered, red with white capital text, at least 56px tall and full width on mobile. One button label across the page (see Section 12).
- **Images:** real phone screenshots of Kairos, or plain photos of real work (a van, a counter, a shopfront). [NEEDS REAL PROOF: real photos. No stock models posed as customers.]
- **Tone rules:** short sentences. One idea per line. No exclamation marks except in a headline if a test proves it helps. No "EXCLUSIVE", "BREAKING", "LAST CHANCE" flashes: they are hype and the reader can tell.

**Mobile-first (build the phone version first, then widen):**

- Single column on phones. Two columns only from `md` up, for the "why" section and the FAQ.
- Headline must be readable without zoom and must not break mid-word. Test at 360px width in both English and French (French runs about 20% longer).
- Sticky bottom bar on phones after the hero scrolls away: one red button, "Ask for an invite". Hide it when the final call to action is on screen.
- Tap targets at least 48px. The EN / FR switch is a large two-button toggle, not a small link.
- Nothing hidden behind hover. No carousels. No auto-playing video.
- Pricing cards stack vertically on phones, Solo first.

---

## 4. Section 1: Masthead

**Purpose:** set the newspaper look straight away and put the language switch where nobody can miss it.

**Copy:**

```
KAIROS                                   [ EN | FR ]
Quebec edition                         Log in
```

**Visual / layout:** thin black bar, white text. "KAIROS" in the condensed headline face, small. Today's date can sit under it in small type (it is a newspaper joke, and it is always true). The EN | FR toggle is two chunky buttons, the active one filled white. "Log in" is a plain text link that goes to `/dashboard` (keep the current behaviour).

Dropped from draft A: "Free to read" (it is not a newspaper; the joke confuses a novice) and "THE KAIROS DAILY" (the product is not daily news).

**Mobile:** one row. KAIROS left, EN | FR right, "Log in" tucked into the same row as a small link.

---

## 5. Section 2: Hero (front page splash)

**Purpose:** stop the scroll, name the guilt, give the relief, all before the first thumb swipe.

**English copy:**

```
SOCIAL MEDIA? SORTED.

You run a business. You don't have time to post every week.
Kairos writes your posts in your own words, puts them out at the
right time and sorts your messages. You just say yes.

[ ASK FOR AN INVITE ]
14 days free. Nothing is posted unless you say yes.

THE FACTS
1. You tell Kairos about your business. Once.
2. It plans two weeks of posts ahead.
3. It writes 3 versions of every post. You pick one.
4. It posts at a good time for you.
5. New customers and complaints always come to YOU first.
6. From $49 a month. First 14 days free.
```

**French copy (hero):**

```
RÉSEAUX SOCIAUX? C'EST RÉGLÉ.

Vous avez une entreprise à faire rouler. Vous n'avez pas le temps
de publier chaque semaine. Kairos écrit vos publications avec vos
mots, les met en ligne au bon moment et trie vos messages.
Vous n'avez qu'à dire oui.

[ DEMANDER UNE INVITATION ]
14 jours gratuits. Rien n'est publié sans votre accord.

LES FAITS
1. Vous présentez votre entreprise à Kairos. Une seule fois.
2. Kairos planifie deux semaines de publications à l'avance.
3. Il écrit 3 versions de chaque publication. Vous en choisissez une.
4. Il publie au bon moment pour vous.
5. Les nouveaux clients et les plaintes vous arrivent TOUJOURS à vous d'abord.
6. À partir de 49 $ par mois. Les 14 premiers jours sont gratuits.
```

[CONFIRM: French copy reviewed by a native Quebec French speaker before launch. "À partir de 49 $" assumes CAD; see pricing confirmations.]

**Visual / layout:** the headline fills the width in black on white. Under it, the subhead in large body type (22px mobile). The red button sits directly under the subhead. THE FACTS box sits beside the headline on desktop and under the button on mobile: 4px black border, numbered lines, with "YOU" in capitals and red on line 5. To the right on desktop: a real phone screenshot of the "pick one of three" screen. [NEEDS REAL PROOF: real screenshot from the product, not a mock-up that shows features that do not exist.]

**Mobile:** headline, subhead, button, small print, then THE FACTS box, then the screenshot. The button must be visible without scrolling on a 360 x 640 screen.

---

## 6. Section 3: Why this matters to you

**Purpose:** explain, in everyday words, why a quiet page costs calls and why taking the job off his plate helps (time, guilt, looking busy and trusted, getting calls).

**Copy (from draft C, with draft A's closing lines):**

```
YOU'RE NOT LAZY. YOU'RE BUSY.

You work all day.
At night, the last thing you want is to write a post.
So you don't. Then you feel bad about it.

Here's the thing.
Before people call you, they look you up.
If your last post is from last year, they wonder:
are these people still open?
Then they call the next name on the list.

A page with fresh posts looks busy.
Busy looks trusted.
Trusted gets the call.

Kairos keeps your page fresh, so you can get back to the work that pays.

YOU GET BACK: the evenings you spent staring at a blank post.
YOU LOSE: the guilt.
```

**Visual / layout:** a two-panel picture, side by side like a "spot the difference" spread. Left: a phone showing a page whose last post is months old, date circled in red. Right: the same page with fresh posts. Big caption across both: **WHICH ONE WOULD YOU CALL?** Body text in two narrow newspaper columns on desktop, one column on mobile. "YOU GET BACK / YOU LOSE" set as a bold two-line box.

**Mobile:** picture first (stacked, old page above new page), then the text.

Honesty note: this section makes no number claims. Do not add "X% of customers check social media" or "saves X hours" without a real, cited source. [NEEDS REAL PROOF]

---

## 7. Section 4: Your week, before and after

**Purpose:** make the benefit concrete. Kept from draft B, but told about "you", not about an invented neighbour, so nobody can mistake it for a customer story.

**Copy:**

```
YOUR WEEK. BEFORE AND AFTER.

BEFORE
Monday: "I should post something." You don't.
Wednesday: A customer asks, "Are you still open? Your page looks dead."
Friday: You post a blurry photo at 11 at night.
Sunday: You feel bad about it. Again.
Messages sit there for days. Some were people wanting a quote.

AFTER
Monday: Your phone says, "Three posts ready. Pick one." You pick one.
Wednesday: Your post goes out in the morning, when people are looking.
Friday: Someone asks for a price. Kairos flags it for you straight away.
         You call back the same day.
Sunday: Nothing to feel bad about.
```

**Visual / layout:** two columns headed BEFORE (grey, strikethrough-style messy phone) and AFTER (clean phone, red tick). Days in bold capitals down the left edge.

**Mobile:** BEFORE block, then AFTER block, stacked. Keep each day on one line where possible.

[CONFIRM: owners are told on their phone when posts are ready (push, text or email) before printing "Your phone says". If not, change to "Kairos has three posts ready."]

---

## 8. Section 5: How it works. Three steps. That's it.

**Purpose:** show a nervous beginner it takes three easy steps and no skills.

**Copy:**

```
HOW IT WORKS. THREE STEPS. THAT'S IT.

1  TELL KAIROS ABOUT YOUR BUSINESS. ONCE.
   What you do. How you talk. What you want to be known for.
   Like "we fix leaks fast and we're friendly."
   You do this one time.

2  PICK THE ONE YOU LIKE.
   Kairos keeps the next two weeks of posts ready.
   For every post, it writes three versions that sound like you.
   Tap the one you like. Change a word if you want. Or skip it.

3  IT GOES OUT FOR YOU.
   Kairos posts it at a good time.
   It reads your messages and writes replies to simple questions.
   People asking for a price, and anyone unhappy, always wait for you.
   Over time it sees which subjects get people talking,
   and does more of those.
```

**Visual / layout:** three giant red numerals (at least 120px on mobile, 200px on desktop) stacked down the page, each with its step headline in the condensed face and a real phone screenshot: the short "about your business" form, the three post choices with a tick, the two-week calendar with filled days. [NEEDS REAL PROOF: real screenshots.]

**Mobile:** numeral, headline, text, screenshot, repeated three times. No side-by-side.

Consistency rule: "Kairos" or "it" does the work everywhere. Never "we write the posts" (draft C) because it suggests a person writes them.

---

## 9. Section 6: You're the boss. Always.

**Purpose:** kill the top fear for this reader: a robot saying something stupid in his name.

**Copy:**

```
YOU'RE THE BOSS. ALWAYS.

Nothing goes out unless you say yes. Full stop.

[x] You pick every post before it goes out.
[x] You can change any word, or throw the whole thing out.
[x] You can give Kairos words it must never use.
[x] People asking for a price always come to you. Kairos never answers them for you.
[x] Complaints always come to you. Kairos never answers them for you.
[x] Want it to post without asking first? You can switch that on.
    It stays off until you do.

Kairos does the typing. You make the decisions.
```

**Visual / layout:** a big 4px-bordered box with heavy black ticks. Above it, a red rubber-stamp graphic: **APPROVED BY YOU**. On desktop, beside the box, a light switch drawn in the OFF position with the caption "Off until YOU say so."

**Mobile:** stamp, then the box full width. Ticks at least 28px.

[CONFIRM: "Pause it any time" from draft A was dropped. Add it back only if a pause control exists in the product.]

---

## 10. Section 7: What it costs

**Purpose:** make the price easy to read with no tech words. Numbers are exactly as set in the product; do not change them.

**Copy:**

```
WHAT IT COSTS

Try it free for 14 days. After that, pick one.

SOLO  $49 a month
For one small business.
2 social pages (for example Facebook and Instagram).
Up to 60 posts a month. That's about two a day.
Answers up to 200 simple messages a month.

PRO  $149 a month
For a busier business.
Up to 5 social pages.
Up to 200 posts a month.
Answers up to 800 simple messages a month.

STUDIO  $399 a month
For a business with several locations or brands.
Up to 15 social pages.
Up to 700 posts a month.
Answers up to 2,000 simple messages a month.

AGENCY  $999 a month
For people who run social media for other businesses.
Up to 50 social pages.
Up to 2,000 posts a month.
Answers up to 5,000 simple messages a month.

Not sure? Start with Solo. You can move up later.
```

**Visual / layout:** four plain price boxes like a classified-ads page. Price in huge condensed type. Solo first and largest; Studio and Agency visibly smaller and lower on the page. No comparison grid. No "MOST POPULAR" or "MOST PICKED" badge. Each box has the same red button (label per Section 12).

**Mobile:** stacked, Solo first. Studio and Agency can sit behind a plain "Bigger businesses and agencies" heading so the plumber sees Solo and Pro first.

Confirmations before printing:

- [CONFIRM: prices are CAD or USD, and whether taxes are extra. Add "plus taxes" if so.]
- [CONFIRM: which social networks are connected today. Only name "Facebook and Instagram" if both work now.]
- [CONFIRM: "You can move up later" (plan changes exist) and cancel terms.]
- [CONFIRM: whether a card is needed to start the 14 days.]
- "Answers up to N simple messages" maps to the current `replies` limits (200 / 800 / 2,000 / 5,000), which are routine replies only. Leads and complaints are never auto-answered.

Dropped: "$49 is less than a couple of hours of paying someone" (draft B) and "most local shops only need SOLO" (draft A). Both need proof. [NEEDS REAL PROOF]

---

## 11. Section 8: Questions people ask

**Purpose:** answer beginner worries in one or two plain sentences each.

**Copy:**

```
QUESTIONS PEOPLE ASK

I'm not good with computers. Can I use this?
Yes. If you can send a text, you can use Kairos.
You answer some questions once. Then you mostly just tap yes.

Will it sound like a robot?
It writes in the way you describe yourself, and gives you three
versions to pick from. If one doesn't sound like you, change it or skip it.

Will it post something silly without asking me?
No. Nothing goes out until you say yes, unless you switch that on yourself.

What if a customer sends an angry message?
Kairos won't answer it. It flags it and sends it to you.

What if someone asks for a price?
That comes to you too. Kairos never answers a new customer on its own.

Does it work in French?
[CONFIRM before printing: posts can be written in French, English or both,
for each business. If yes: "Yes. French, English or both. It's made for Quebec."]

Will this get me more customers?
We can't promise that, and nobody honest can. What Kairos does is keep
your page looking open and cared for, and make sure you never miss a
message from someone who wants to hire you.

How much time does it take each week?
[NEEDS REAL PROOF: measure with real users before printing a number.
Until then: "A few minutes to pick your posts."]

Why can't I just sign up?
We're letting businesses in a few at a time, so we can look after each one properly.
Ask for an invite and we'll get back to you.

What happens after the 14 free days?
[CONFIRM exact trial-to-paid behaviour and cancel terms before printing an answer.]
```

**Visual / layout:** a newspaper "Your questions answered" column. Questions in bold condensed capitals, answers in body type. Two narrow columns on desktop.

**Mobile:** one column, all answers open (no accordions: a novice may not know to tap).

---

## 12. Section 9: Final call to action

**Purpose:** one calm, low-pressure next step that matches invite-only access.

**English copy:**

```
STOP WORRYING ABOUT SOCIAL MEDIA. STARTING TODAY.

Tell us about your business. Try it free for 14 days.
Nothing goes out unless you say yes.

[ ASK FOR AN INVITE ]
Invitation only for now. From $49 a month after your free 14 days.
```

**French copy (call to action):**

```
FINI LE STRESS DES RÉSEAUX SOCIAUX. DÈS AUJOURD'HUI.

Parlez-nous de votre entreprise. Essayez Kairos gratuitement pendant 14 jours.
Rien n'est publié sans votre oui.

[ DEMANDER UNE INVITATION ]
Sur invitation seulement pour l'instant. À partir de 49 $ par mois après vos 14 jours gratuits.
```

**Button labels (whole page, both languages):**

| State | English | French |
|---|---|---|
| Signup closed (current) | ASK FOR AN INVITE | DEMANDER UNE INVITATION |
| Signup open | START MY 14 FREE DAYS | COMMENCER MES 14 JOURS GRATUITS |

**Visual / layout:** full-width black band, giant white headline in the condensed face, one big red button. Beside the button on desktop, the same phone from the hero now showing a post dated "Today" with a red tick.

**Mobile:** headline wraps to three or four lines at most; button full width.

**Footer:** "© [year] Kairos. Made in Quebec." [CONFIRM "Made in Quebec" is true; otherwise keep "© [year] Kairos."] Add a contact email link and, when they exist, privacy and terms links.

---

## 13. Words banned from the page

Never use these, in English or French:

- AI-powered, AI (as a selling word), IA
- leverage, optimize / optimise, optimiser
- workflow, flux de travail
- engagement, engagement rate, taux d'engagement
- synergy, synergie
- platform, plateforme
- autonomous, autonome
- automate / automation / automatisation (say "does it for you")
- content, contenu (say "posts", "publications")
- channel(s), canal / canaux (say "social pages", "pages")
- algorithm, algorithme
- dashboard, tableau de bord (in selling copy; the "Log in" link is fine)
- seamless, solution, cutting-edge, revolutionary, game-changer, next-level, supercharge, unlock, empower
- audience growth, grow your audience
- "The opportune moment" (current tagline: means nothing to this reader)
- EXCLUSIVE, BREAKING, LAST CHANCE, limited time
- guaranteed, garanti (no guarantees of any kind)
- em dashes: never, anywhere on the page, in either language

---

## 14. Every item that needs real proof or confirmation

**[NEEDS REAL PROOF]** (do not print until real evidence exists):

1. Any claim that Kairos brings more calls, customers or sales.
2. Any number of hours or minutes saved per week (including "a few minutes" if challenged; replace with a measured figure).
3. Any figure on how many people check social media before hiring a local business (needs a real, cited source).
4. Any "most popular", "most picked" or "most small shops start here" badge or arrow (needs real plan-mix data). This also means removing the current "MOST POPULAR" badge on Pro.
5. "Most local shops only need Solo" style advice framed as fact.
6. Any price comparison against hiring someone ("less than two hours of a freelancer").
7. Any customer name, quote, logo, photo, star rating or case study.
8. Real product screenshots for hero, steps and CTA (no mock-ups showing features that do not exist).
9. Real photos of real work (van, counter, shopfront). No stock models posed as customers.

**[CONFIRM]** (product facts to check before printing):

1. Which social networks are connected today (before naming Facebook, Instagram or Google anywhere, including headline alternate 1).
2. Posts can be written in French, English or both, per business.
3. Prices are CAD or USD; taxes extra or included.
4. Whether a card is needed to start the 14-day trial.
5. What happens when the trial ends (auto-charge or not).
6. Cancel terms (monthly, no contract?).
7. Plan changes allowed ("move up later").
8. How owners are told posts are ready (push, text, email) for "Your phone says".
9. Whether a pause control exists (only then add "Pause it any time").
10. "Made in Quebec" in the footer.
11. French copy reviewed by a native Quebec French speaker.

---

## 15. Implementation notes for replacing `frontend/src/app/page.tsx`

Read `frontend/AGENTS.md` first: this repo's Next.js version has breaking changes, so check `node_modules/next/dist/docs/` before using `next/font` or any new API.

**Keep exactly:**

- `"use client"`, `getPublicConfig()` from `@/lib/api`, and the `signupEnabled` state.
- `SignupDialog` from `@/components/SignupDialog` with props `planId`, `planName`, `signupEnabled`, `onClose`. When `signupEnabled` is false the dialog already shows the "Request access" mailto path; keep that invite-only behaviour. Every button on the page (hero, sticky mobile bar, pricing boxes, final CTA) opens this dialog.
- Plan ids `solo`, `pro`, `studio`, `agency` and names `Solo`, `Pro`, `Studio`, `Agency`. Hero, sticky bar and final CTA open the dialog with `{ id: "solo", name: "Solo" }`.
- Pricing numbers exactly: Solo $49 / 2 / 60 / 200, Pro $149 / 5 / 200 / 800, Studio $399 / 15 / 700 / 2,000, Agency $999 / 50 / 2,000 / 5,000 (price / pages / posts / replies). Keep them in one `PLANS` array so the numbers live in one place.
- The "Log in" link to `/dashboard`.

**Change:**

- Button label comes from `signupEnabled`: closed shows "Ask for an invite" / "Demander une invitation"; open shows "Start my 14 free days" / "Commencer mes 14 jours gratuits".
- Recommended: start `signupEnabled` as `false` instead of `true`, so a closed-signup visitor never sees "Start" flash before `/v1/config` answers. Note that `getPublicConfig()` returns `signupEnabled: true` when the config call fails; the server still refuses signups unless `SIGNUP_ENABLED` is exactly `"true"`, so this is a copy issue, not a security one. Changing the fallback in `lib/api.ts` is outside this page and should be a separate decision.
- Remove the `popular` prop / "MOST POPULAR" badge on Pro (see proof item 4).
- Rename "Channels" to "social pages" and "Auto-replies/mo" to "simple messages answered a month".
- Remove the old hero ("The opportune moment. Every time."), the five feature cards and the footer tagline "Built for the opportune moment."
- Nav: drop "Features" and "Pricing" links from the masthead on mobile; keep them on desktop only as "How it works" and "What it costs" anchors (`#how`, `#pricing`).

**Bilingual:**

- Put all copy in one `COPY` object keyed by `en` and `fr`, and a `lang` state driven by the masthead toggle. Default from `navigator.language` starting with `fr`, then remember the choice in `localStorage`. Set `document.documentElement.lang` when it changes.
- This spec gives final French for the hero, THE FACTS and the final call to action. The rest of the French is [CONFIRM: translation by a native Quebec French speaker]; until then, the French view may show English for the middle sections rather than machine translation.
- French prices use Quebec format: `49 $`, `2 000`.

**Structure (suggested components in the same file):** `Masthead`, `Hero`, `FactsBox`, `WhySection`, `BeforeAfter`, `Steps`, `BossBox`, `Pricing` (maps `PLANS`), `Faq`, `FinalCta`, `StickyMobileCta`, `Footer`.

**Styling:** Tailwind as today. Add the condensed headline font (check Next docs first) as a CSS variable used via a `font-headline` utility. Accent colour `#E10600` only. Square corners (`rounded-none`) on boxes and buttons. Minimum body `text-lg` on mobile.

**Accessibility:** one `<h1>` (the headline). Step numbers are decorative (`aria-hidden`) with the step headline as `<h3>`. Red on white and white on red must pass 4.5:1 for button text (bold 18px+ passes at 3:1). The EN / FR toggle uses `aria-pressed`.

**Done when:**

1. Page renders at 360px with the hero button visible without scrolling, in English and French.
2. A search for the em dash character (U+2014) on the page finds nothing, and none of the banned words appear in the copy.
3. With `SIGNUP_ENABLED` unset, every button says "Ask for an invite" and opens the dialog's request-access path.
4. Pricing numbers match Section 10 exactly.
5. Every [NEEDS REAL PROOF] and [CONFIRM] item is either resolved or left out of the live copy (placeholders never ship).

---

## 16. Animations: showing the loop without the jargon

**Purpose:** a novice should *see* how Kairos works before reading a word of it. Each animation shows one plain idea, plays quietly, and never needs a caption longer than five words. Nothing on the page says "loop", "automation", "AI" or "algorithm". The animation is the explanation.

**Rules for every animation:**

- **Subtle.** Movements take 400 to 700ms with a soft ease-out. Nothing bounces, spins, flashes or zooms. No sound.
- **Plays when seen.** Each animation starts when it scrolls into view (IntersectionObserver, 40% visible) and plays once, except the circle in 16.2, which turns slowly for as long as it is on screen.
- **Always readable when still.** The final frame of every animation makes sense on its own, so a paused or reduced-motion visitor loses nothing.
- **Reduced motion.** With `prefers-reduced-motion: reduce`, show the final frame with no movement.
- **Real text stays outside the drawing.** Labels inside an animation are short (one to three words) and duplicated in a caption below it, so screen readers and translators get them. Each animation is `aria-hidden` with a visible caption.
- **No fake numbers.** Animations show shapes, ticks and bars, never follower counts, sales figures or percentages.
- **Built in plain CSS and inline SVG.** No animation library, no video, no GIF. Under 15 KB total. Same black, white and tabloid red as the page.
- **Bilingual.** Every label has an EN and a FR version (FR in brackets below).

### 16.1 Hero: "Your week, filled"

Sits beside the headline on desktop, under it on phones.

1. Seven empty day boxes in a row, labelled M T W T F S S (L M M J V S D).
2. One by one, left to right, small post cards drop into four of the days (150ms apart).
3. A small red tick appears on the first card.

Caption: **"Your week, filled. You just pick."** ("Votre semaine, remplie. Vous choisissez.")

The idea it carries: an empty page becomes a full week, and you only tick.

### 16.2 The circle: how it keeps getting better

Sits between Section 5 (How it works) and Section 6 (You're the boss). This is the one animation that explains the loop.

A plain circle with four stops, like a clock face at 12, 3, 6 and 9. A small red dot travels round it, taking about 10 seconds for a full turn. As the dot reaches each stop, that stop's icon darkens and its label appears in bold:

| Stop | Icon | Label (EN) | Label (FR) |
|---|---|---|---|
| 12 o'clock | a small card with a tick | **You pick** | **Vous choisissez** |
| 3 o'clock | a paper plane | **It posts** | **Ça publie** |
| 6 o'clock | a speech bubble and a heart | **People react** | **Les gens réagissent** |
| 9 o'clock | a small bar chart growing | **It learns** | **Ça apprend** |

After "It learns", the dot passes 12 again and the card at "You pick" becomes very slightly larger each lap, up to three laps: the plain signal that each round is better than the last.

Caption underneath: **"Every week it sees what your customers like, and does more of that. You still pick."** ("Chaque semaine, il voit ce que vos clients aiment et en fait plus. C'est toujours vous qui choisissez.")

Why a circle and not arrows: a circle says "this keeps going on its own" without the word "automatic". The "You pick" stop sits at 12 o'clock, the top, on purpose: the owner is always at the top of the circle.

### 16.3 Step 2: "Pick the one you like"

Inside Section 5, next to step 2.

1. Three post cards fan in side by side.
2. After a short pause, a red tick lands on the middle card.
3. The other two slide down and fade out. The chosen card moves into a small calendar day.

Caption: **"Three versions. You tap one."** ("Trois versions. Vous en touchez une.")

### 16.4 Step 3: "Messages, sorted"

Inside Section 5, next to step 3.

1. Two message bubbles arrive, one after the other.
2. The first gets a small grey tag, **Simple question** (*Question simple*). A reply bubble slides in beneath it.
3. The second gets a red tag, **Wants a price** (*Veut un prix*), and a red label, **Waiting for you** (*Vous attend*). No reply appears.

Caption: **"Easy ones answered. Important ones wait for you."** ("Les faciles, c'est réglé. Les importants vous attendent.")

This is the trust moment: the visitor sees that Kairos holds back on the things that matter.

### 16.5 Results: "More of what works"

Inside Section 4 (the week before and after), on the "after" side.

Three thin horizontal bars labelled with plain subjects (e.g. **Tips**, **Before and after**, **About us**). One bar grows slowly and the others shrink a little, over about 1.2 seconds.

Caption: **"It notices what people like."** ("Il remarque ce que les gens aiment.")

No percentages, no axis, no numbers.

### 16.6 What not to animate

The headline, the prices, the FAQ, the buttons (apart from a normal hover darken) and the sticky bottom bar. Motion is for explaining, never for selling.

### 16.7 Preview

A working preview of 16.1 to 16.5 in plain HTML, CSS and SVG, with the reduced-motion fallback, is in `docs/sales-page-animations-preview.html`. Open it in a browser. It is a reference for the build, not production code.
