from __future__ import annotations

from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "obsidian_agent_vault_setup_guide_2026-04-14.pdf"


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)

    styles = getSampleStyleSheet()
    styles.add(
        ParagraphStyle(
            name="GuideTitle",
            parent=styles["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            textColor=HexColor("#111111"),
            alignment=TA_CENTER,
            spaceAfter=10,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideSubtitle",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12,
            textColor=HexColor("#333333"),
            alignment=TA_CENTER,
            spaceAfter=14,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideHeading",
            parent=styles["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=10.5,
            leading=13,
            textColor=HexColor("#111111"),
            spaceBefore=4,
            spaceAfter=4,
        )
    )
    styles.add(
        ParagraphStyle(
            name="GuideBody",
            parent=styles["BodyText"],
            fontName="Helvetica",
            fontSize=8.9,
            leading=11.1,
            textColor=HexColor("#222222"),
            spaceAfter=4,
        )
    )

    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.58 * inch,
        rightMargin=0.58 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.5 * inch,
        title="Obsidian Agent Vault — Setup Guide",
        author="Codex",
    )

    story = [
        Paragraph("Obsidian Agent Vault — 10-Minute Setup Guide", styles["GuideTitle"]),
        Paragraph(
            "Install the vault, load your context once, and give Claude Code or any "
            "file-aware agent a memory layer it can actually navigate.",
            styles["GuideSubtitle"],
        ),
        Paragraph("What You Receive", styles["GuideHeading"]),
        Paragraph(
            "Vault zip with <b>raw/</b>, <b>wiki/</b>, <b>skills/</b>, and "
            "<b>archive/</b>; hub-note templates; a <b>CLAUDE.md</b> starter; a "
            "<b>skill.md</b> template; and a synthesis prompt for turning raw notes "
            "into linked wiki notes.",
            styles["GuideBody"],
        ),
        Paragraph("Setup in 5 Steps", styles["GuideHeading"]),
        Paragraph(
            "<b>1. Unzip the vault.</b> Put the folder somewhere stable on your "
            "machine so your notes and agent files live in one place.",
            styles["GuideBody"],
        ),
        Paragraph(
            "<b>2. Open it in Obsidian.</b> Use “Open folder as vault” and point "
            "Obsidian to the unzipped folder.",
            styles["GuideBody"],
        ),
        Paragraph(
            "<b>3. Edit CLAUDE.md first.</b> Add your name, active projects, stack, "
            "preferences, and any standing rules the agent should always know.",
            styles["GuideBody"],
        ),
        Paragraph(
            "<b>4. Use the folders on purpose.</b> Put fresh captures in "
            "<b>raw/</b>; durable knowledge in <b>wiki/</b>; repeatable workflows in "
            "<b>skills/</b>; finished or stale material in <b>archive/</b>.",
            styles["GuideBody"],
        ),
        Paragraph(
            "<b>5. Create your first retrieval loop.</b> Drop one real note into "
            "<b>raw/</b>, ask the agent to synthesize it into <b>wiki/</b>, then make "
            "sure the result links back to a hub or project note.",
            styles["GuideBody"],
        ),
        Paragraph("How the Agent Should Work", styles["GuideHeading"]),
        Paragraph(
            "The agent should read <b>CLAUDE.md</b> first, navigate through linked "
            "wiki notes second, and only fall back to raw material when needed. A note "
            "without links is stored text, not usable memory.",
            styles["GuideBody"],
        ),
        Paragraph("Success Check", styles["GuideHeading"]),
        Paragraph(
            "You are set up when the agent can answer a project question without you "
            "re-pasting context, can follow links from a hub note into the right page, "
            "and can turn a raw note into a linked wiki note in one pass.",
            styles["GuideBody"],
        ),
        Paragraph("Recommended Next Moves", styles["GuideHeading"]),
        Paragraph(
            "Add one hub note for your main project, one skill file for a repeated "
            "workflow, and one plugin only if it clearly improves structure or search. "
            "Do not add complexity before the basic vault loop is working.",
            styles["GuideBody"],
        ),
        Spacer(1, 8),
        Paragraph(
            "Template pack: $49 · Guided setup: $299 · Team implementation: $2,500",
            styles["GuideSubtitle"],
        ),
    ]

    doc.build(story)
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
