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

## 5. Authentication & Admin Auto-Login Mechanism

To facilitate easy access for administrators or specific users without going through a standard authentication flow, the application implements an automatic login/bypass mechanism.

### How it Works:
1. **Environment Variable Injection**: The system reads `NEXT_PUBLIC_ADMIN_API_KEY` from the environment.
2. **Auto-Population**: In `src/app/dashboard/layout.tsx`, a `useEffect` hook runs on mount. It checks if `kairos_api_key` already exists in `localStorage`. If it does not, it takes the value from `NEXT_PUBLIC_ADMIN_API_KEY` and automatically populates `localStorage`.
3. **Manual Fallback**: If no key is present in `localStorage` and the environment variable is not set (or fails to load), `src/app/dashboard/page.tsx` renders an "Admin Authentication" fallback screen. The user can manually input their root API key, which is then written to `localStorage` and immediately used to query the backend.

```typescript
// Auto-login logic (dashboard/layout.tsx)
useEffect(() => {
  if (!localStorage.getItem("kairos_api_key")) {
    const adminKey = process.env.NEXT_PUBLIC_ADMIN_API_KEY;
    if (adminKey) localStorage.setItem("kairos_api_key", adminKey);
  }
}, []);
```
This seamless design ensures that the dashboard owner can bypass traditional paywalls or login screens by simply supplying the correct environment variable during build/deployment.
