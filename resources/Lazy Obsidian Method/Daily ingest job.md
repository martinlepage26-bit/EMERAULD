---
title: Daily ingest job
created: 2026-04-25
type: workflow
tags:
  - review
  - daily
---

# Daily ingest job

See also [[Index]].
Run once per day.

Review today’s new material in `00_Inbox/`, including Raw, Web Clips, Voice Memos, and Unprocessed.

For each item:
1. Preserve the raw source.
2. Create a short ingest summary.
3. Identify whether it belongs in Projects, Areas, Resources, or Archive.
4. Suggest which notes should be promoted into wiki-ready pages.
5. Add useful tags and possible backlinks.
6. Create or update a daily ingest log in `70_Agent Logs/Daily Ingest Logs/`.

Output:
- Cleaned note list
- Suggested promotions
- New links to create
- Possible duplicates
- Priority items
