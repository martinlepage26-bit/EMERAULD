---
title: Nightly review job
created: 2026-04-25
type: workflow
tags:
  - review
  - nightly
---

# Nightly review job

Run once per night.

Inputs:
- Today’s daily notes
- Daily ingest logs
- Lessons learned
- Agent logs
- Memory or operating-system notes
- Active project dashboards

Tasks:
1. Refresh `60_Dashboards/Daily Dashboard.md`.
2. Refresh `60_Dashboards/Priority Dashboard.md`.
3. Update memory-style notes where useful.
4. Identify the most important unresolved priority.
5. Identify stale, noisy, or duplicate notes.
6. Back up or summarize important agent logs.
7. Create a nightly review log.

Output:
- Critical priority refresh
- Dashboard updates
- Suggested cleanup
- Memory updates
- Backup summary

