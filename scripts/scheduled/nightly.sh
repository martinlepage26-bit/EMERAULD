#!/usr/bin/env bash
# obsidian-nightly — daily 10:00 PM
# Consolidation pass: reconcile, synthesize, heal orphans, log.

export OBSIDIAN_VAULT_PATH="/home/martin/EMERAULD"
export PATH="/home/martin/.local/bin:/home/martin/.nvm/versions/node/v22.23.0/bin:$PATH"

VAULT="/home/martin/EMERAULD"
TODAY=$(date +%Y-%m-%d)
LOG="/tmp/obsidian-nightly.log"

cd "$VAULT" || exit 1

/home/martin/.local/bin/claude --dangerously-skip-permissions -p "
Read _CLAUDE.md and CLAUDE.md at the vault root first — follow their rules exactly.

TODAY is $TODAY. This is a sleeptime consolidation pass — the vault should be smarter tomorrow.

Phase 1 — Close the day:
- Read memory/daily/${TODAY}.md if it exists. Append a short end-of-day bullet list summarising what happened today (infer from session-state.md and any notes updated today with updated: $TODAY).

Phase 2 — Reconcile:
- Scan wiki/ for notes updated today (updated: $TODAY in frontmatter). Check if any claims in those notes contradict claims in older notes on the same topic. Flag contradictions with a > [!warning] Contradiction detected callout in the newer note rather than deleting old content.

Phase 3 — Synthesize:
- If two or more wiki/ notes updated today reference the same concept, tool, person, or project that does not yet have its own dedicated wiki note, create one. Apply EMERAULD linking rule: minimum 2 inline wikilinks.

Phase 4 — Heal orphans:
- Find notes created today (created: $TODAY) with zero incoming wikilinks in other notes. For each, find one existing related note and add an inline wikilink to the new note.

Phase 5 — Log:
- Append one line to session-state.md: nightly pass $TODAY — phases 1-4 complete, N reconciled, M synthesized, K orphans linked.
- Run vector store rebuild: /home/martin/.venvs/emerauld/bin/python3 /home/martin/EMERAULD/scripts/embed.py --changed

Do not ask questions. Do not delete or archive anything. Add and update only. Stop when done.
" >> "$LOG" 2>&1
