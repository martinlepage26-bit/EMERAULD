---
type: wiki
title: Reddit Data API — Access Terms and Rate Limits
aliases:
- Reddit API
- Reddit Data API
- r/redditdev rate limits
tags:
- reference
- api
- reddit
- rate-limits
- oauth
- tooling
- resources
- reddit-data-api-access-terms-and-rate-limits-md
- deletion
- rate
- ingestion
- color-teal
status: active
created: '2026-04-20'
updated: '2026-06-26'
vault_area: Resources
canonical_path: Resources/Reddit Data API — Access Terms and Rate Limits.md
backlink_count: 9
backlinks:
- '[[Areas/PHAROS/CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)]]'
- '[[archive/wiki-2026-07-08/Governance Controls — Baseline Assessment (2026-04-26)]]'
- '[[Areas/PHAROS/OPEN RISKS — Three Governance Blindspots Requiring Recursive Control]]'
- '[[wiki/OUTLIERS — Five Notes That Break the Architecture]]'
- '[[Areas/Personal/Personal and Projects MOC]]'
- '[[Resources/Privacy as Contextual Integrity — Nissenbaum 2004 (Public Surveillance)]]'
- '[[archive/session-state/session-state-001]]'
- '[[memory/clients/helix-prospects/HELIX-potential-clients-2026-05-06/2026-05-05_koïos-intelligence]]'
- '[[memory/clients/helix-prospects/HELIX-regional-prospect-deep-sweep-2026-05-06/2026-05-05_solace-platform-solace]]'
---

# Reddit Data API — Access Terms and Rate Limits

## Summary

Operational reference for the Reddit Data API's authentication, rate limits, user-agent rules, and data-deletion obligations. Clipped from Reddit's official support article on 2026-04-20 and normalized here because the API's policy surface shifts fast enough that a vault-local snapshot is useful for any future [[claude-mem Plugin — Session Memory Layer|memory-layer]] or clipping-ingest work that touches Reddit. Relevant to [[Obsidian Second Brain Product]] where Reddit is a potential data source for thought-leadership seeding.

## Context

Source: `Clippings/Reddit Data API Wiki.md` (official Reddit support article, published 2026-03-02, clipped 2026-04-20). Reddit's legacy API documentation is explicitly flagged as potentially stale — the Developer Terms and Data API Terms are the authoritative contracts. This note captures the operational essentials: what you need to access the API legally, how hard Reddit will throttle you, and what you must delete. It does **not** replace the live Developer Terms; treat this as a snapshot.

## Details

### Authentication

- OAuth 2.0 is **required**. Unauthenticated traffic is blocked; the default rate limit does not apply to non-OAuth traffic.
- Clients must register an OAuth application and use the issued client ID.
- Reddit can and will freely throttle or block unidentified Data API users.

### User-Agent format (mandatory)

```
<platform>:<app ID>:<version string> (by /u/<reddit username>)
```

Example: `User-Agent: android:com.example.myredditapp:v1.2.3 (by /u/kemitche)`

- Generic User-Agents like `Python/urllib` or `Java` are drastically rate-limited by default.
- Version strings enable Reddit to block old broken versions safely — update them on each release.
- Lying about the User-Agent is an explicit policy violation.

### Rate Limits (Free Tier)

- **100 queries per minute (QPM)** per OAuth client ID, averaged over a 10-minute window (bursting tolerated).
- Response headers to monitor:
  - `X-Ratelimit-Used` — approximate requests used in period
  - `X-Ratelimit-Remaining` — approximate requests left
  - `X-Ratelimit-Reset` — seconds until end of period
- Chat rate limits: **2,000 messages/day per recipient**, **3,000 messages/day total**.
- Bot API users can join up to **300 chat rooms/day**.
- Mod-bot operators needing higher limits must contact Reddit via their ticket form.

### Data-Deletion Obligations

This is the heaviest policy surface and easy to miss. If a post, comment, or user account is deleted on Reddit, you **must** delete all derived content and user-identifying info in your possession.

- **Post/comment deletion**: delete title, body, embedded URLs, and any derived artifacts.
- **Account deletion**: delete all user-ID info (`t2_*`), author name, profile URL, avatar URL, user flair, and all references to the author across posts/comments they created.
- Recommended compliance practice: routinely delete stored user data within 48 hours.
- De-identified or anonymized retained content still violates the terms. Disassociation is not sufficient.

### Technical Entry Points

- [Reddit's live API docs](http://www.reddit.com/dev/api) — authoritative endpoint reference
- [OAuth2 setup](https://github.com/reddit-archive/reddit/wiki/OAuth2) — auth flow
- [OAuth2 app types](https://github.com/reddit-archive/reddit/wiki/OAuth2-App-Types) — script vs web vs installed
- [Submit post API](https://github.com/reddit-archive/reddit/wiki/API:-submit) — posting reference
- [r/redditdev](https://reddit.com/r/redditdev) — official update channel

## Key Ideas

- **OAuth + User-Agent are gates, not suggestions.** Misconfigure either and Reddit will throttle transparently.
- **Deletion propagation is the real compliance risk.** Most integrations fail on this boundary, not on rate limits. A 48-hour sweep is the minimum practical hygiene.
- **The QPM limit is generous for research use** but tight for any scraping-style ingestion — expect to design around bursts with cooldowns.

## Insights

- The 48-hour deletion cadence is a natural fit for a scheduled job rather than event-driven — Reddit's deletion notifications are not a reliable push channel.
- For a [[Obsidian Second Brain Product|second-brain]] workflow that ingests Reddit discussions, the deletion obligation implies the vault itself is regulated storage once Reddit content lands in it. That's a non-trivial compliance surface — exactly the gap [[OUTLIERS — Five Notes That Break the Architecture|the Outliers analysis]] flags as Outlier 4 and that [[CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding)|Control 2 (External Data Lifecycle)]] addresses through registry, expiry, refresh schedule, and quarantine semantics.
- The rate-limit headers are cleanly named — easy to wire into any middleware.
- Conceptually, Reddit ingestion is a [[Privacy as Contextual Integrity — Nissenbaum 2004 (Public Surveillance)|cross-context information flow]] case: subreddit discussion → vault → derived governance product is a context-transfer that must be audited against the source context's distribution norms, not just against API rate-limit hygiene.

## Open Questions

- Is there a paid tier with higher rate limits that would matter for consulting or research ingestion use-cases?
- How does Reddit's Responsible Builder Policy interact with the Data API Terms when the two seem to overlap?
- For academic research, does Reddit have a separate program with modified deletion obligations?

## Related

- [[Obsidian Second Brain Product]] — product ingestion surfaces
- [[claude-mem Plugin — Session Memory Layer]] — similar ingestion/memory discipline
- [[Claude Code Skill Corpus]] — potentially relevant for building an ingestion skill

- [[CREDENTIALS]]
- [[README]]
- [[readme]]
- [[CHANGELOG]]
- [[HISTORY]]
- [[Connector]]
- [[RetryAgent]]
- [[RetryHandler]]
- [[SnapshotAgent]]
- [[Socks5ProxyAgent]]
- [[2026-05-05_koïos-intelligence]]
- [[2026-05-05_solace-platform-solace]]
- [[2022 - job_application.pdf - 2022 - job_application.pdf.pdf - 2022 - job_application.pdf - 2022 - jo]]
- [[2025 - report [2]_1]]
- [[2026 - Martin Lepage - report]]
- [[Introduction (2)]]
## Sources

- `Clippings/Reddit Data API Wiki.md` — Reddit Help Center article
- Source URL: https://support.reddithelp.com/hc/en-us/articles/16160319875092-Reddit-Data-API-Wiki
- Published 2026-03-02; clipped 2026-04-20
