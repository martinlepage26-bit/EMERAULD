#!/usr/bin/env bash
# obsidian-weekly — every Friday 6:00 PM
# Generates a weekly review note from memory/daily/ and wiki/ activity.

export OBSIDIAN_VAULT_PATH="/home/martin/EMERAULD"
export PATH="/home/martin/.local/bin:/home/martin/.nvm/versions/node/v22.23.0/bin:$PATH"

VAULT="/home/martin/EMERAULD"
TODAY=$(date +%Y-%m-%d)
WEEK_START=$(date -d "last Monday" +%Y-%m-%d 2>/dev/null || date -v-Mon +%Y-%m-%d)
LOGDIR="$VAULT/Logs/scheduled"
mkdir -p "$LOGDIR"
LOG="$LOGDIR/weekly-$TODAY.log"

cd "$VAULT" || exit 1

/home/martin/.local/bin/claude --dangerously-skip-permissions -p "
Read _CLAUDE.md and CLAUDE.md at the vault root first — follow their rules exactly.

TODAY is $TODAY. WEEK_START is $WEEK_START.

Generate a weekly review note:

1. Read all daily notes in memory/daily/ from $WEEK_START to $TODAY.
2. Read session-state.md for decisions and threads from this week.
3. Scan Areas/, Resources/, wiki/, and projects/ (top level) for notes with updated: between $WEEK_START and $TODAY.
4. Synthesize a weekly review note at wiki/Weekly Review — ${TODAY}.md with:
   - Frontmatter: type: wiki, tags: [review, weekly], status: active, created: $TODAY, updated: $TODAY
   - Preamble: > For future Claude: weekly review for the week of $WEEK_START. Load to understand what Martin worked on, decided, and learned this week.
   - ## Summary — 3-5 bullets of what happened
   - ## Decisions — decisions made this week (from session-state.md Key Decisions and daily notes)
   - ## Projects — active projects touched this week with status
   - ## Learnings — insights or lessons from this week
   - ## Carry Forward — open threads, next steps
   - ## Related — wikilinks to daily notes and key project notes from this week
5. Append a link to the review from this week's last daily note.
6. Update VAULT ADDITIONS TRACKER: one line for the review note.

Do not ask questions. Do not delete anything. Stop when done.
" >> "$LOG" 2>&1
STATUS=$?
if [ $STATUS -ne 0 ]; then
  echo "- $TODAY $(date +%H:%M) weekly run FAILED (exit $STATUS) — see Logs/scheduled/weekly-$TODAY.log" >> "$LOGDIR/FAILURES.md"
fi
