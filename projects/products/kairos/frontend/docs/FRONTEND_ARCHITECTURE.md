# Kairos Frontend Architecture

This document provides a comprehensive overview of the architecture, layout, components, and integration mechanisms for the Kairos Next.js frontend application.

## 1. Directory Structure & App Router

The application is built using the **Next.js App Router** (version 16.3.5) with **React 19**, and leverages **Tailwind CSS** for styling. 

```text
src/
├── lib/
│   └── api.ts             # API origin, key storage, authed fetch, error type
├── components/
│   ├── SignupDialog.tsx   # Account creation, key reveal, checkout handoff
│   └── LoadState.tsx      # Shared error, empty, and loading states
└── app/
    ├── layout.tsx         # Root HTML/Body structure and font definitions
    ├── page.tsx           # Public-facing landing page
    └── dashboard/         # Key-gated dashboard area
        ├── layout.tsx     # Key gate + shell (Sidebar & Main content)
        ├── page.tsx       # Dashboard overview page
        ├── calendar/      # Calendar view
        ├── inbox/         # Inbox view
        ├── insights/      # Analytics and insights
        └── posts/         # Posts and Drafts view
```

## 2. Layouts

The application's layouts are split between the root and the dashboard:

- **Root Layout (`src/app/layout.tsx`)**: Establishes the `<html>` and `<body>` tags, sets up the antialiasing, and injects the "Geist" custom fonts (`Geist_Sans` and `Geist_Mono`). It applies standard full-height Tailwind utility classes.
- **Dashboard Layout (`src/app/dashboard/layout.tsx`)**: This acts as the shell for the application's core functionality. It consists of:
  - **Sidebar (`<aside>`)**: A 64-width left navigation pane containing links to Overview, Calendar, Posts & Drafts, Inbox, and Insights. It uses the `NavItem` component and Lucide React icons, and offers a "Disconnect this browser" action at the bottom that clears the stored key.
  - **Main Content (`<main>`)**: A flex-1 container that wraps the specific dashboard sub-route pages in a centered, max-width layout.

## 3. Core Components

The UI relies heavily on lightweight functional components defined locally within the pages and layouts:

- **`NavItem`**: Located in `dashboard/layout.tsx`, this component renders sidebar links with consistent padding, hover states, and icons.
- **`StatCard`**: Located in `dashboard/page.tsx`, this component renders a simple white card displaying a title and a prominent value (used for metrics like "Connected Channels", "Plan", and "Account Status").
- **`LoadError` / `EmptyState` / `Loading`** (`components/LoadState.tsx`): Every page previously swallowed fetch failures into `console.error` and rendered its empty state, so a broken API was indistinguishable from an account with no data. These separate the two.
- **`SignupDialog`** (`components/SignupDialog.tsx`): Drives account creation from the landing page. See §6.
- **Icons**: The application uses `lucide-react` for consistent SVG iconography (e.g., `LayoutDashboard`, `Calendar`, `Play`, `Pause`).

## 4. Backend Integration

All API access goes through `src/lib/api.ts`. The origin was previously pasted
into six components, and when the Worker moved off its workers.dev hostname
every one of them had to be found by hand.

- `API_BASE` — `NEXT_PUBLIC_API_BASE` if set, else `https://kairos.govern-ai.ca`.
  Point it at a local Worker for development; see `.env.example`.
- `authedFetch(path)` — attaches `Authorization: Bearer <stored key>`.
- `apiFetch(path)` — unauthenticated, used by signup which mints the key.
- `ApiError` — carries the Worker's `{ error: { code, message } }` envelope, so
  pages can distinguish a revoked key (401) from a genuine empty result.

### Response shapes

The dashboard reads these exact keys. They are worth stating because an earlier
version read `post.content`, `data.messages`, `hours_saved`, `account.plan_id`
and `controls.autopilot`, none of which the API returns, so every page rendered
placeholder or empty content regardless of the account's real state.

| Endpoint | Returns |
|---|---|
| `GET /v1/me` | `{ account: { plan, status, trial_ends_at, … }, plan: PlanDefinition, controls: { autopilot_publishing, autopilot_replies, paused_until, daily_*_cap }, channels: [] }` |
| `GET /v1/calendar` | `{ slots: [{ id, scheduled_for, status, platform, handle, pillar, hook, … }] }` |
| `GET /v1/posts?status=` | `{ posts: [{ id, hook, body, status, variant, platform, … }] }` |
| `GET /v1/inbox` | `{ conversations: [{ id, author_handle, intent, priority, status, latest_message, pending_draft_id, … }] }` |
| `GET /v1/insights` | `{ window, totals, pillars: [{ name, weight, posts, avg_score }], usage: { postsPublished, repliesSent, planLimits }, hoursSaved: { hours, basis } }` |

Autopilot is two independent flags (`autopilot_publishing`, `autopilot_replies`),
not one boolean, and slot/post statuses come from `migrations/0001_init.sql`:
slots are `planned|drafting|ready|approved|publishing|published|failed|skipped`
and posts are `draft|approved|publishing|published|failed|rejected`.

### CORS

The dashboard runs on its own origin, so every call is cross-origin. The Worker
answers preflights from origins listed in its `DASHBOARD_ORIGINS` var, ahead of
auth — an `OPTIONS` carries no `Authorization` header by definition, so routing
it through auth would 401 the preflight and the browser would never send the
real request. An unlisted origin gets no CORS headers at all.

## 5. Authentication

The dashboard authenticates with the same API key the backend issues at account
creation (`kai_sk_…`). There is no session layer on the backend yet; every
request carries the key as `Authorization: Bearer <key>`.

### How it works
1. **Layout gate.** `src/app/dashboard/layout.tsx` is the single gate for all
   five dashboard routes. Before rendering children it reads `kairos_api_key`
   from `localStorage` and verifies it against `GET /v1/me`.
2. **Verify on every mount.** A stored key can be revoked server-side, so
   presence is not trusted. If verification fails the key is removed from
   `localStorage` and the connect screen is shown with an explanation.
3. **Connect screen.** With no valid key, the layout renders a form that accepts
   a key, verifies it against the API before storing it, and reports a rejected
   key rather than saving it and failing silently on the next page.
4. **Disconnect.** The sidebar clears the stored key for that browser.

Because the gate lives in the layout, the four pages it wraps
(calendar, posts, inbox, insights) only mount once a verified key is present and
can read `localStorage` directly.

### Why there is no environment-variable login
An earlier version read `NEXT_PUBLIC_ADMIN_API_KEY` at build time and seeded
`localStorage` from it. Next.js inlines every `NEXT_PUBLIC_`-prefixed variable
into the client bundle, so that build would have shipped a working
account key to every visitor. Do not reintroduce a key through the environment.
The key belongs in the browser that typed it, and nowhere in the build output.

## 6. Signup and checkout

`POST /v1/billing/checkout` requires a bearer key, and a visitor has none until
an account exists, so signup is the first half of checkout rather than a
separate flow. `SignupDialog` runs it in order:

1. `POST /v1/accounts` with email, display name, and the browser's resolved
   timezone. A 14-day trial starts immediately with autopilot off.
2. The response carries the API key **once** — the Worker stores only a SHA-256
   digest and cannot return it again. The dialog shows it with a copy button and
   says so plainly before offering to continue.
3. `POST /v1/billing/checkout` with `{ priceLookupKey: "kairos_<plan>_monthly" }`
   and the new key, then redirects to the returned Stripe URL.

An earlier version posted `{ plan: "pro" }` with no `Authorization` header, so
every pricing button failed twice over: 401 from the auth middleware, and 400
from the payload schema had it ever got past. Failures now render inline; the
page raises no `alert()`.

## 7. Testing

`npm test` runs Jest with jsdom. Coverage is on the logic that can silently
ship a credential or silently show the wrong thing:

- `src/lib/__tests__/api.test.ts` — key storage, the error envelope, bearer
  attachment, the no-key short circuit, `verifyKey` returning false rather than
  throwing when the request cannot be made at all (the CORS and offline case),
  and the checkout payload shape.
- `src/app/dashboard/__tests__/layout.test.tsx` — the gate: children never
  render before a key verifies, a key is never read from the build environment,
  a revoked key is cleared and explained, a rejected key is not written to
  storage, and disconnect closes the dashboard.

## 8. Deployment

The dashboard is a **static export** (`output: "export"` in `next.config.ts`).
Every route is a client component fetching the Worker API at runtime, so there
is nothing for a Next server to do and `next build` emits plain assets to
`out/`. `trailingSlash: true` makes Pages serve `/dashboard/` from
`dashboard/index.html`; without it nested routes resolve inconsistently.

```bash
npm run deploy   # next build && wrangler pages deploy out --project-name=kairos-dashboard --branch=main
```

- Cloudflare Pages project: `kairos-dashboard`
- Production origin: **https://kairos-dashboard-dy4.pages.dev**
- Account: `1713c51cc6fbcf8d7143526b93495b76`, the same one the Worker is in.
  Pin it (`account_id` in `wrangler.jsonc`, or `CLOUDFLARE_ACCOUNT_ID`) because
  these credentials can see two accounts and cannot choose non-interactively.

### After changing the origin

The Worker's `DASHBOARD_ORIGINS` must name this origin exactly, and a redeploy
of the Worker is required for the change to take effect. Two gotchas:

- Matching is exact. Per-deployment preview URLs
  (`<hash>.kairos-dashboard-dy4.pages.dev`) are **not** admitted. Add one to
  `DASHBOARD_ORIGINS` to test a preview against live data.
- Preflight responses are cached per origin (`Vary: Origin`), so a stale cached
  preflight can make a correct allowlist look broken. `max-age` is 1 hour, not
  the usual day, to bound that. When verifying with curl, add a cache-busting
  query param or you may be reading a cached answer.
