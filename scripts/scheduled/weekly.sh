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

# --- OS health pre-computation (governed task weekly-os-health-20260708) ---
# Deterministic metrics interpolated into the prompt as literal values, per the
# HEPHAISTOS scope packet + Queen Keyport conditions 1-5: every metric is its own
# failure domain and degrades to a labeled placeholder, never kills the run.

# 1. FAILURES.md counts (QK condition 1: -f test first — no stderr leak from a missing-file redirection)
if [ -f "$LOGDIR/FAILURES.md" ]; then
  FAIL_TOTAL=$(wc -l < "$LOGDIR/FAILURES.md" 2>/dev/null || echo "unavailable")
  FAIL_WEEK=$(awk -v ws="$WEEK_START" '/^- [0-9][0-9][0-9][0-9]-[0-9][0-9]-[0-9][0-9]/ { d=substr($2,1,10); if (d >= ws) n++ } END { print n+0 }' "$LOGDIR/FAILURES.md" 2>/dev/null || echo "unavailable")
else
  FAIL_TOTAL=0
  FAIL_WEEK=0
fi

# 2. Graph counts from .graph_store/summary.json (two distinct fields, never conflated)
GRAPH_METRICS=$(/home/martin/.venvs/emerauld/bin/python3 -c "
import json
d = json.load(open('$VAULT/.graph_store/summary.json'))
print(d.get('zero_backlink', 'unavailable'), d.get('unresolved_links', 'unavailable'))
" 2>/dev/null || echo "unavailable unavailable")
ORPHANS=$(echo "$GRAPH_METRICS" | awk '{print $1}')
UNRESOLVED=$(echo "$GRAPH_METRICS" | awk '{print $2}')

# 3. Register line counts
# (pipefail scoped to each $( ) subshell — task #2 QK condition 1: PIPESTATUS read
# after a command-substitution assignment reflects the assignment, not the inner
# pipe, so it would mask failures as 0; subshell pipefail + $? is the tested form.)
SS_LINES=$( [ -f session-state.md ] && wc -l < session-state.md || echo "unavailable" )
AGENT_LINES=$(set -o pipefail; cat memory/agents/*.md 2>/dev/null | wc -l); RC=$?
[ "$RC" -eq 0 ] || AGENT_LINES="unavailable"

# 4. Contradiction callouts, open vs resolved — FILE counts, raw lanes excluded (task #1 QK condition 4).
# grep exit 1 = legitimate zero matches, not a failure; only exit >=2 degrades (task #2 QK condition 1).
OPEN_FLAGS=$(set -o pipefail; grep -rl '> \[!warning\] Contradiction detected' --include='*.md' --exclude-dir='raw sources' --exclude-dir=raw --exclude-dir=.git --exclude-dir=.trash --exclude-dir=node_modules . 2>/dev/null | wc -l); RC=$?
[ "$RC" -le 1 ] || OPEN_FLAGS="unavailable"
RESOLVED_FLAGS=$(set -o pipefail; grep -rl '> \[!success\] Contradiction resolved' --include='*.md' --exclude-dir='raw sources' --exclude-dir=raw --exclude-dir=.git --exclude-dir=.trash --exclude-dir=node_modules . 2>/dev/null | wc -l); RC=$?
[ "$RC" -le 1 ] || RESOLVED_FLAGS="unavailable"

# 5. Unresolved-link delta vs previous weekly review (bash-side parse, QK condition 3)
PREV_UNRESOLVED=""
PREV_REVIEW=$(ls -1 "wiki/"Weekly\ Review*.md 2>/dev/null | grep -v -- "$TODAY" | sort | tail -1)
if [ -n "$PREV_REVIEW" ]; then
  PREV_UNRESOLVED=$(grep -oP 'unresolved links: \K[0-9]+' "$PREV_REVIEW" 2>/dev/null | head -1)
fi
if [ -n "$PREV_UNRESOLVED" ] && [ "$UNRESOLVED" != "unavailable" ]; then
  UNRESOLVED_DELTA="$((UNRESOLVED - PREV_UNRESOLVED)) vs previous review ($PREV_UNRESOLVED)"
else
  UNRESOLVED_DELTA="baseline — no prior week to diff against"
fi
# --- end OS health pre-computation (isolated failure domain: nothing above exits the script) ---

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
   - ## OS health — copy these pre-computed metrics VERBATIM (they are deterministic ground truth computed by the script; do not recompute, round, or alter them):
     - Scheduled-run failures: $FAIL_WEEK this week, $FAIL_TOTAL all-time (Logs/scheduled/FAILURES.md)
     - Graph: $ORPHANS orphan notes (zero_backlink); unresolved links: $UNRESOLVED
     - Unresolved-link delta: $UNRESOLVED_DELTA
     - Registers: session-state.md $SS_LINES lines; memory/agents/ combined $AGENT_LINES lines
     - Contradiction flags: $OPEN_FLAGS files open, $RESOLVED_FLAGS files resolved
   - ## Related — wikilinks to daily notes and key project notes from this week
5. Append a link to the review from this week's last daily note.
6. Update VAULT ADDITIONS TRACKER: one line for the review note.

Do not ask questions. Do not delete anything. Stop when done.
" >> "$LOG" 2>&1
STATUS=$?
if [ $STATUS -ne 0 ]; then
  echo "- $TODAY $(date +%H:%M) weekly run FAILED (exit $STATUS) — see Logs/scheduled/weekly-$TODAY.log" >> "$LOGDIR/FAILURES.md"
fi
