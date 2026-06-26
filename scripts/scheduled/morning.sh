#!/usr/bin/env bash
# obsidian-morning — daily 8:00 AM
# Creates today's daily note, surfaces overdue tasks and stale active projects.

export OBSIDIAN_VAULT_PATH="/home/martin/EMERAULD"
export PATH="/home/martin/.local/bin:/home/martin/.nvm/versions/node/v22.23.0/bin:$PATH"

VAULT="/home/martin/EMERAULD"
TODAY=$(date +%Y-%m-%d)
LOG="/tmp/obsidian-morning.log"

cd "$VAULT" || exit 1

/home/martin/.local/bin/claude --dangerously-skip-permissions -p "
Read _CLAUDE.md and CLAUDE.md at the vault root first — follow their rules exactly.

TODAY is $TODAY.

Steps:
1. Create today's daily note at memory/daily/${TODAY}.md if it does not exist.
   Use the structure from any recent daily note in memory/daily/ as a template.
   Include sections: ## Focus, ## Tasks, ## Notes.
2. Scan wiki/ for project notes (type: wiki, tags containing 'project' or status: active).
   List any that have 'updated:' older than 7 days — flag them in today's daily note under ## Stale Projects.
3. Scan wiki/ for any notes containing task checkboxes (- [ ]) with dates before $TODAY — flag overdue ones in today's daily note under ## Overdue.
4. Update session-state.md: append one line noting morning agent ran on $TODAY.

Do not ask questions. Do not delete or archive anything. Add and update only. Stop when done.
" >> "$LOG" 2>&1
