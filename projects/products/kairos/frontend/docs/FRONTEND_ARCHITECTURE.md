# Kairos Frontend Architecture

This document provides a comprehensive overview of the architecture, layout, components, and integration mechanisms for the Kairos Next.js frontend application.

## 1. Directory Structure & App Router

The application is built using the **Next.js App Router** (version 16.3.5) with **React 19**, and leverages **Tailwind CSS** for styling. 

```text
src/
└── app/
    ├── layout.tsx         # Root HTML/Body structure and font definitions
    ├── page.tsx           # Public-facing landing page
    └── dashboard/         # Protected/Admin dashboard area
        ├── layout.tsx     # Dashboard shell (Sidebar & Main content)
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
  - **Sidebar (`<aside>`)**: A 64-width left navigation pane containing links to Overview, Calendar, Posts & Drafts, Inbox, and Insights. It uses the `NavItem` component and Lucide React icons. It clearly displays an "Admin Bypass Enabled" indicator at the bottom.
  - **Main Content (`<main>`)**: A flex-1 container that wraps the specific dashboard sub-route pages in a centered, max-width layout.

## 3. Core Components

The UI relies heavily on lightweight functional components defined locally within the pages and layouts:

- **`NavItem`**: Located in `dashboard/layout.tsx`, this component renders sidebar links with consistent padding, hover states, and icons.
- **`StatCard`**: Located in `dashboard/page.tsx`, this component renders a simple white card displaying a title and a prominent value (used for metrics like "Connected Channels", "Plan", and "Account Status").
- **Icons**: The application uses `lucide-react` for consistent SVG iconography (e.g., `LayoutDashboard`, `Calendar`, `Play`, `Pause`).

## 4. Backend Integration

The frontend communicates with the Kairos backend (hosted at `https://kairos.govern-ai.ca`) primarily via client-side fetch requests.

### Data Fetching Mechanism
In `src/app/dashboard/page.tsx`, data fetching is handled within a standard `useEffect` hook:
1. It retrieves the `kairos_api_key` from the browser's `localStorage`.
2. A `fetch` request is sent to `https://kairos.govern-ai.ca/v1/me`.
3. The request includes the authorization header: `Authorization: Bearer <key>`.
4. The retrieved JSON payload controls the UI state, displaying the user's plan, channel count, account status, and whether the automated system "Autopilot" is active or paused.

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
