# skills/

**Purpose:** Reusable agent instructions. Each file here teaches the agent how to do one thing well.

A skill file is not a note - it's an instruction set. The agent reads it, follows it, and produces a result.

## Guide Set

- `../CLAUDE.md` - **Caelir**, the context guide.
- `synthesis_prompt.md` - **Ilyris**, the synthesis guide.
- `link_guide.md` - **Ariun**, the link guide.
- `archive_guide.md` - **Mnara**, the archive guide.

**What belongs here:**
- Synthesis prompts, such as "convert raw note to wiki note"
- Review checklists, such as "audit all wiki notes for broken links"
- Workflow instructions, such as "process a new client intake"
- Formatting standards, such as "how to write a hub note in this vault"

**Rules for the agent:**
- Read the skill file before executing the workflow it describes.
- Follow the steps in order.
- If the skill references other vault locations (raw/, wiki/, etc.), navigate there.

**Rules for the human:**
- One skill per file. Keep them focused.
- Name the file after the workflow, such as `synthesis_prompt.md`, `link_audit.md`, or `client_intake.md`.
- Use the template in `skill_template.md` to start.

## Related

- [[Research and Papers MOC]]
- [[hashnode-iter34-skill-guides]]
