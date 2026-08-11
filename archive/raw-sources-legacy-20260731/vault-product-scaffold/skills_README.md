---
type: raw-source
title: skills_README
tags:
- raw-source
status: preserved
created: '2026-06-21'
vault_area: raw sources
canonical_path: raw sources/vault-product-scaffold/skills_README.md
---

# skills/

See also [[Manuscript Pipeline MOC]].
See also [[README]].
**Purpose:** Reusable agent instructions. Each file here teaches the agent how to do one thing well.

A skill file is not a note — it's an instruction set. The agent reads it, follows it, and produces a result.

**What belongs here:**
- Synthesis prompts (e.g., "convert raw note to wiki note")
- Review checklists (e.g., "audit all wiki notes for broken links")
- Workflow instructions (e.g., "process a new client intake")
- Formatting standards (e.g., "how to write a hub note in this vault")

**Rules for the agent:**
- Read the skill file before executing the workflow it describes.
- Follow the steps in order.
- If the skill references other vault locations (raw/, wiki/, etc.), navigate there.

**Rules for the human:**
- One skill per file. Keep them focused.
- Name the file after the workflow: `synthesis_prompt.md`, `link_audit.md`, `client_intake.md`.
- Use the template in `skill_template.md` to start.
