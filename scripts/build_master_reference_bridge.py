#!/usr/bin/env python3
from __future__ import annotations

import csv
import re
from collections import defaultdict
from pathlib import Path

VAULT_ROOT = Path("/mnt/c/Users/softinfo/Documents/EMERAULD")
SOURCE_CSV = Path("/mnt/d/MASTER REFERENCE SAFE/annotated/MASTER ANNOTATED REFERENCE LIST.csv")
OUTPUT = VAULT_ROOT / "wiki/Master Reference Bridge Atlas — 2026-05-06.md"

SECTION_ORDER = [
    "ai_governance",
    "governance",
    "power_security",
    "methods",
    "gender_queer",
    "ritual_spirituality",
    "media_culture",
    "posthuman_ecology",
    "martin_public",
    "martin_scholarly",
    "martin_creative",
    "general",
]

SECTION_TITLES = {
    "ai_governance": "AI Governance, Policy, and Regulation",
    "governance": "Governance and Institutions",
    "power_security": "Power, Security, and Political Control",
    "methods": "Research Methods",
    "gender_queer": "Gender, Queer, and Embodiment Studies",
    "ritual_spirituality": "Ritual, Religion, and Spirituality",
    "media_culture": "Media and Cultural Analysis",
    "posthuman_ecology": "Posthumanism, Ecology, and the Anthropocene",
    "martin_public": "Martin — Public / Professional Surface",
    "martin_scholarly": "Martin — Scholarly Publication Surface",
    "martin_creative": "Martin — Creative / Compositional Surface",
    "general": "Tier 0 — General Theory or Context Building",
}

SECTION_HUBS = {
    "ai_governance": [
        "[[Recursive Governance Theory]]",
        "[[Evidence Discipline and Epistemics]]",
        "[[Governance Controls and Mechanisms]]",
        "[[AI Infrastructure Stack]]",
        "[[Governance and PHAROS MOC]]",
    ],
    "governance": [
        "[[Governance Controls and Mechanisms]]",
        "[[Authority, Legitimacy, and Post-Sovereignty]]",
        "[[Governance and PHAROS MOC]]",
    ],
    "power_security": [
        "[[Governance Controls and Mechanisms]]",
        "[[Consent and Boundary Frameworks]]",
        "[[Authority, Legitimacy, and Post-Sovereignty]]",
    ],
    "methods": [
        "[[Evidence Discipline and Epistemics]]",
        "[[Research and Papers MOC]]",
        "[[Academic Paper Pipeline]]",
        "[[Qualitative Handbook — Expanded Reference List]]",
    ],
    "gender_queer": [
        "[[Queer Theory Foundations]]",
        "[[Queer Sociology of Magic and Ritual]]",
        "[[Martin Lepage Professional Identity]]",
    ],
    "ritual_spirituality": [
        "[[Ritual, Magic, and Institutional Authority]]",
        "[[Queer Sociology of Magic and Ritual]]",
        "[[Queer Theory Foundations]]",
    ],
    "media_culture": [
        "[[Media Studies and Pop Culture Analysis]]",
        "[[Writing and Novels MOC]]",
        "[[Buffy Slayer Studies]]",
    ],
    "posthuman_ecology": [
        "[[Research and Papers MOC]]",
        "[[Novel and Creative Corpus]]",
        "[[The Rooted Archive — Nine Chambers of Plant, Spirit, and Knowledge]]",
        "[[Breath of the Astral Year — Astrology Monograph]]",
    ],
    "martin_public": [
        "[[Martin Lepage Professional Identity]]",
        "[[Martin Lepage — Professional Profile]]",
        "[[Martin Lepage — AI Governance Consulting Profile Assessment]]",
        "[[Martin Lepage — Skills by Life Domain]]",
    ],
    "martin_scholarly": [
        "[[Martin Lepage Professional Identity]]",
        "[[Martin Lepage — Professional Profile]]",
        "[[Martin Lepage Publications — Annotated Bibliography and Verification Leads]]",
        "[[Research and Papers MOC]]",
    ],
    "martin_creative": [
        "[[Martin Lepage — Professional Profile]]",
        "[[Writing and Novels MOC]]",
        "[[Novel and Creative Corpus]]",
        "[[HEXA Press — Publishing and Practice Initiative]]",
    ],
    "general": [
        "[[Research and Papers MOC]]",
        "[[Master Bibliography — Références bibliographiques 2025]]",
        "[[MASTER REFERENCE SAFE — Canonical Bibliography System]]",
    ],
}

SECTION_DEFINITIONS = {
    "ai_governance": "Work on AI systems, regulation, accountability, model behavior, governance controls, and policy response.",
    "governance": "Institutional governance, legitimacy, oversight, rule systems, and how power is organized through structures.",
    "power_security": "Security, coercion, surveillance, consent, boundary enforcement, and political control.",
    "methods": "Research design, qualitative method, evidence handling, analysis practice, and methodological reflection.",
    "gender_queer": "Gender, queer theory, embodiment, identity, intersectionality, and related social formation.",
    "ritual_spirituality": "Religion, ritual, magic, spirituality, sacred practice, and institutionalized symbolic systems.",
    "media_culture": "Media studies, pop culture, narrative production, fan text, and cultural interpretation.",
    "posthuman_ecology": "Posthumanism, ecology, more-than-human systems, environment, and the Anthropocene.",
    "martin_public": "Public-facing Martin materials: identity, consulting, skills, and the external professional surface.",
    "martin_scholarly": "Martin Lepage's scholarly publication surface: papers, chapters, and academic references.",
    "martin_creative": "Creative and compositional Martin materials: novels, monographs, fiction, and the writing surface.",
    "general": "Tier 0 bridge material: broad theory, context-setting, and references that bridge across multiple clusters without a narrower home.",
}

ALWAYS_EMIT_SECTIONS = {
    "martin_public",
    "martin_scholarly",
    "martin_creative",
}

TAG_TO_SECTION = {
    "ai_governance": "ai_governance",
    "governance": "governance",
    "power_security": "power_security",
    "methods": "methods",
    "gender_queer": "gender_queer",
    "ritual_spirituality": "ritual_spirituality",
    "media_culture": "media_culture",
    "posthuman_ecology": "posthuman_ecology",
}

TITLE_PATTERNS = [
    (re.compile(r"\b(ai|artificial intelligence|llm|language model|foundation model|machine learning|algorithmic)\b", re.I), [
        "[[Recursive Governance Theory]]",
        "[[Evidence Discipline and Epistemics]]",
        "[[AI Infrastructure Stack]]",
    ]),
    (re.compile(r"\b(governance|accountabil|transparency|legitimacy|regulation|policy|power|security|consent)\b", re.I), [
        "[[Governance Controls and Mechanisms]]",
        "[[Authority, Legitimacy, and Post-Sovereignty]]",
    ]),
    (re.compile(r"\b(queer|gender|trans|embodiment|femin|intersectional)\b", re.I), [
        "[[Queer Theory Foundations]]",
        "[[Queer Sociology of Magic and Ritual]]",
    ]),
    (re.compile(r"\b(ritual|magic|witch|wicca|pagan|spirit|religion|sacred)\b", re.I), [
        "[[Ritual, Magic, and Institutional Authority]]",
        "[[Queer Sociology of Magic and Ritual]]",
    ]),
    (re.compile(r"\b(buffy|charmed|love witch|disenchantment|avatar|reboot|jurassic|shadows|agatha)\b", re.I), [
        "[[Media Studies and Pop Culture Analysis]]",
        "[[Buffy Slayer Studies]]",
    ]),
    (re.compile(r"\b(method|methods|qualitative|ethnograph|discourse|process-tracing|stutter|crip|disability)\b", re.I), [
        "[[Evidence Discipline and Epistemics]]",
        "[[Research and Papers MOC]]",
    ]),
    (re.compile(r"\b(posthuman|ecolog|anthropocene|nature|ecocritic|vibrant matter)\b", re.I), [
        "[[Research and Papers MOC]]",
        "[[The Rooted Archive — Nine Chambers of Plant, Spirit, and Knowledge]]",
    ]),
    (re.compile(r"\b(novel|monograph|allegory|poem|screenplay|fiction|writing)\b", re.I), [
        "[[Writing and Novels MOC]]",
        "[[Novel and Creative Corpus]]",
    ]),
]


def normalize_tags(raw: str) -> list[str]:
    tags: list[str] = []
    for tag in (raw or "").split(";"):
        tag = tag.strip()
        if tag in TAG_TO_SECTION:
            tags.append(tag)
    return tags


def section_for_row(row: dict[str, str], tags: list[str], title: str) -> str:
    corpus_text = " ".join(
        part for part in [
            row.get("author", ""),
            row.get("title", ""),
            row.get("original_entry", ""),
        ]
        if part
    ).lower()
    if "lepage" in corpus_text:
        creative_markers = ("novel", "fiction", "poem", "allegory", "screenplay", "writing", "monograph")
        public_markers = ("profile", "consult", "consulting", "assessment", "interview", "bio", "public", "press", "cv", "curriculum vitae")
        if any(marker in corpus_text for marker in creative_markers):
            return "martin_creative"
        if any(marker in corpus_text for marker in public_markers):
            return "martin_public"
        return "martin_scholarly"
    for tag in tags:
        if tag in TAG_TO_SECTION:
            return TAG_TO_SECTION[tag]
    return infer_section_from_title(title)


def infer_section_from_title(title: str) -> str:
    for pattern, _ in TITLE_PATTERNS:
        if pattern.search(title):
            # Match by the first linked section in the pattern block.
            if "AI" in pattern.pattern or "ai" in pattern.pattern:
                return "ai_governance"
            if "governance" in pattern.pattern.lower() or "accountabil" in pattern.pattern.lower():
                return "governance"
            if "queer" in pattern.pattern.lower() or "gender" in pattern.pattern.lower():
                return "gender_queer"
            if "ritual" in pattern.pattern.lower() or "witch" in pattern.pattern.lower():
                return "ritual_spirituality"
            if "buffy" in pattern.pattern.lower() or "charmed" in pattern.pattern.lower() or "love witch" in pattern.pattern.lower() or "agatha" in pattern.pattern.lower():
                return "media_culture"
            if "method" in pattern.pattern.lower() or "stutter" in pattern.pattern.lower() or "disability" in pattern.pattern.lower():
                return "methods"
            if "posthuman" in pattern.pattern.lower() or "ecolog" in pattern.pattern.lower():
                return "posthuman_ecology"
            if "novel" in pattern.pattern.lower() or "monograph" in pattern.pattern.lower():
                return "media_culture"
    return "general"


def links_for_row(row: dict[str, str], title: str, tags: list[str]) -> list[str]:
    links: list[str] = []

    section = section_for_row(row, tags, title)
    links.extend(SECTION_HUBS[section])

    # Secondary tag bridges
    if "ai_governance" in tags:
        links.extend([
            "[[Recursive Governance Theory]]",
            "[[Evidence Discipline and Epistemics]]",
        ])
    if "governance" in tags:
        links.extend([
            "[[Governance Controls and Mechanisms]]",
            "[[Authority, Legitimacy, and Post-Sovereignty]]",
        ])
    if "power_security" in tags:
        links.extend([
            "[[Consent and Boundary Frameworks]]",
            "[[Governance Controls and Mechanisms]]",
        ])
    if "methods" in tags:
        links.extend([
            "[[Evidence Discipline and Epistemics]]",
            "[[Research and Papers MOC]]",
        ])
    if "gender_queer" in tags:
        links.extend([
            "[[Queer Theory Foundations]]",
            "[[Queer Sociology of Magic and Ritual]]",
        ])
    if "ritual_spirituality" in tags:
        links.extend([
            "[[Ritual, Magic, and Institutional Authority]]",
            "[[Queer Sociology of Magic and Ritual]]",
        ])
    if "media_culture" in tags:
        links.extend([
            "[[Media Studies and Pop Culture Analysis]]",
            "[[Writing and Novels MOC]]",
        ])
    if "posthuman_ecology" in tags:
        links.extend([
            "[[Research and Papers MOC]]",
            "[[The Rooted Archive — Nine Chambers of Plant, Spirit, and Knowledge]]",
        ])

    lowered = " ".join(
        part for part in [
            row.get("author", ""),
            row.get("title", ""),
            row.get("original_entry", ""),
        ]
        if part
    ).lower()
    for pattern, extra_links in TITLE_PATTERNS:
        if pattern.search(lowered):
            links.extend(extra_links)

    # Martin-specific bridges align with the new subtier split.
    if section == "martin_public":
        links.extend([
            "[[Martin Lepage — Professional Profile]]",
            "[[Martin Lepage — AI Governance Consulting Profile Assessment]]",
            "[[Martin Lepage — Skills by Life Domain]]",
        ])
    elif section == "martin_scholarly":
        links.extend([
            "[[Martin Lepage — Professional Profile]]",
            "[[Martin Lepage Publications — Annotated Bibliography and Verification Leads]]",
        ])
    elif section == "martin_creative":
        links.extend([
            "[[Writing and Novels MOC]]",
            "[[Novel and Creative Corpus]]",
            "[[HEXA Press — Publishing and Practice Initiative]]",
        ])

    deduped: list[str] = []
    seen: set[str] = set()
    for link in links:
        if link not in seen:
            seen.add(link)
            deduped.append(link)
    return deduped


def format_entry(row: dict[str, str]) -> str:
    title = (row.get("title") or "").strip()
    citation = (row.get("original_entry") or "").strip()
    if not citation:
        author = (row.get("author") or "").strip()
        year = (row.get("year") or "").strip()
        kind = (row.get("kind") or "").strip()
        citation = ", ".join(part for part in [author, year, title, kind] if part)
    tags = normalize_tags(row.get("tags", ""))
    links = links_for_row(row, title, tags)
    link_str = " · ".join(links)
    tag_str = row.get("tags", "").strip()
    if tag_str:
        return f"- `{citation}` — {link_str}  _tags: {tag_str}_"
    return f"- `{citation}` — {link_str}"


def build() -> None:
    groups: dict[str, list[str]] = defaultdict(list)
    counts: dict[str, int] = defaultdict(int)

    with SOURCE_CSV.open(encoding="utf-8", errors="ignore", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            title = (row.get("title") or "").strip()
            tags = normalize_tags(row.get("tags", ""))
            section = section_for_row(row, tags, title)
            counts[section] += 1
            groups[section].append(format_entry(row))

    lines: list[str] = []
    lines.extend([
        "---",
        "type: map",
        'aliases: ["Master reference bridge atlas", "Bibliography brain bridge", "Reference-list interconnectivity map"]',
        "tags: [bibliography, bridge, references, research, governance, ritual, queer, media, methods, infrastructure]",
        "status: active",
        "created: 2026-05-06",
        "updated: 2026-05-06",
        "---",
        "",
        "# Master Reference Bridge Atlas — 2026-05-06",
        "",
        "## Summary",
        "",
        "This is the interconnectivity pass for the master reference list. It treats the SAFE’s 1004 annotated bibliography entries as living research infrastructure and links each citation to the parts of the vault that already carry that theme, method, or lineage.",
        "",
        "## Bridge Rule",
        "",
        "- Each entry is placed under one primary theme section.",
        "- Each entry gets one or more links to the brain surfaces that hold its likely use.",
        "- Secondary tag or title matches add cross-links so a citation can travel across multiple vault clusters.",
        "",
        "## Tier Definitions",
        "",
    ])

    for key in SECTION_ORDER:
        lines.append(f"- **{SECTION_TITLES[key]}** — {SECTION_DEFINITIONS[key]}")
    lines.extend([
        "",
        "## Theme Summary",
        "",
    ])

    for key in SECTION_ORDER:
        lines.append(f"- {SECTION_TITLES[key]}: **{counts.get(key, 0)}**")
    lines.extend(["", "## Entries", ""])

    for key in SECTION_ORDER:
        entries = groups.get(key, [])
        if not entries and key not in ALWAYS_EMIT_SECTIONS:
            continue
        lines.append(f"### {SECTION_TITLES[key]}")
        lines.append("")
        lines.append("Hubs: " + " · ".join(SECTION_HUBS[key]))
        lines.append("")
        if key in ALWAYS_EMIT_SECTIONS and not entries:
            lines.append("No SAFE bibliography entries currently land here; this surface is present as a bridge into the Martin corpus.")
            lines.append("")
        lines.extend(entries)
        lines.append("")

    lines.extend([
        "## Related",
        "",
        "- [[MASTER REFERENCE SAFE — Canonical Bibliography System]]",
        "- [[Master Bibliography — Références bibliographiques 2025]]",
        "- [[Research and Papers MOC]]",
        "- [[Governance and PHAROS MOC]]",
        "- [[Writing and Novels MOC]]",
        "- [[Personal and Projects MOC]]",
        "- [[Home]]",
    ])

    OUTPUT.write_text("\n".join(lines) + "\n", encoding="utf-8")


if __name__ == "__main__":
    build()
