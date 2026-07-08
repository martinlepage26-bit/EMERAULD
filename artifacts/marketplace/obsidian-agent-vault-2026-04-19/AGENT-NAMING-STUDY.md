---
type: artifact
title: Agent Naming Study
aliases:
- artifacts/marketplace/obsidian-agent-vault-2026-04-19/AGENT-NAMING-STUDY
tags:
- artifact
- agents
- artifacts
- marketplace
- collisions
- collision
- guide
- astra
- names
- color-orange
status: preserved
created: '2026-04-19'
updated: '2026-06-26'
vault_area: artifacts
canonical_path: artifacts/marketplace/obsidian-agent-vault-2026-04-19/AGENT-NAMING-STUDY.md
backlink_count: 3
backlinks:
- '[[wiki/Ask Vault — EMERAULD Vault Briefing Skill]]'
- '[[Areas/PHAROS/Governance and PHAROS MOC]]'
- '[[wiki/archive/Orphan Index — Artifacts And Archives — 2026-05-06]]'
---

# Agent Naming Study

Build: `obsidian-agent-vault-2026-04-19`
Date: 2026-04-19

## Scope

This naming pass covers the buyer-facing agent roles inside the sanitized vault package, not the private EMERAULD or PHAROS agent ecosystem.

The buyer vault should keep functional file names where they matter for tool compatibility, especially `CLAUDE.md`, but the named roles inside the product can become more distinctive and less vendor-bound.

## Market Read

The 2026 and early-2027 AI-agent market has three dominant naming lanes:

1. **Human names:** Claude, Devin, Jules, Lindy, Cody.
2. **Function names:** Copilot, Codex, Agentforce, Action Agent, Agentspace.
3. **Mythic / celestial / navigation names:** Gemini, Astra, Atlas, Comet, Mariner, Neon.

The third lane fits Obsidian Agent Vault best, but direct names are crowded. Current search results show visible AI/product collisions for `Astra`, `Vela`, `Lyra`, `Clio`, `Aster`, `Theia`, `Mira`, `Oria`, `Kairon`, `Vesper`, `Oryn`, `Elen`, `Auren`, `Velora`, `Elion`, and `Kleia`.

The right move: stay near mythos, but avoid nomos. Use coined names that feel old, luminous, and navigational without naming gods, laws, rulers, or institutional authority.

## Naming Principles

- Prefer 2-3 syllables.
- Prefer vowel-forward names with soft consonants.
- Avoid direct gods, titans, legal-authority words, and obvious platform collisions.
- Avoid names that sound like compliance software.
- Make each name carry a role, not a costume.
- Use `Name - Role` in the buyer-facing copy so the function stays legible.

## Do Not Use

- `Astra` - Google Project Astra collision.
- `Atlas` - OpenAI/ChatGPT Atlas collision and too heavy.
- `Gemini` - Google collision.
- `Lyra` - multiple AI assistants already visible.
- `Vela` - YC and other AI-agent collisions.
- `Clio` - Anthropic/AI-insights and legal-tech collisions.
- `Aster` - SK Telecom AI agent and 2026 research-agent collision.
- `Theia` - Eclipse Theia and multiple AI-assistant collisions.
- `Mira` - several consumer AI-agent collisions.
- `Oria` - visible AI companion / AI design / trademark activity.
- `Kairon` - active agentic platform collision.
- `Oryn` - active AI-agent payment, brand-memory, research, health, and other product collisions.
- `Elen` - active decision-network-for-agents collision.
- `Auren` - active health-AI collision.
- `Velora` - active AI-agent-builder, voice-agent, DeFi-agent, and automation collisions.
- `Elion` - active AI-agent platform collision.
- `Kleia` - active AI-orchestration, AI-companion, and AI-technology collisions.
- `Sage`, `Nova`, `Echo`, `Aura`, `Sora` - too saturated or platform-confusable.

## Suggested Names by Buyer-Vault Role

### 1. Context / Orientation Agent

This role reads the standing context, orients the session, and tells the user where the work lives.

1. **Caelir - Context Guide**
   - Best pick.
   - Carries `caelum` / sky-field and "clear" without using a direct celestial product name.
   - Strong fit for the file that gives the agent its map before work begins.
   - No obvious AI-agent product collision found in the 2026-04-19 collision pass.

2. **Orival - Context Guide**
   - Evokes Orion and orientation without using either word directly.
   - Slightly more branded and less soft than Caelir.

3. **Neralis - Context Guide**
   - Old-water / passage feeling; useful if the product wants a calmer navigator tone.
   - More fantasy-coded than Caelir, so weaker for a practical buyer template.

### 2. Raw-to-Wiki Synthesis Agent

This role turns messy captures into linked, durable wiki notes.

1. **Ilyris - Synthesis Guide**
   - Best pick.
   - Keeps the Lyra / harmony signal while moving away from the crowded `Lyra` and `Lyris` surfaces.
   - Good fit for turning fragments into a coherent note.

2. **Lioren - Synthesis Guide**
   - Light and ordered without becoming another `Lumen` / `Aura` / `Nova` name.
   - Feels warm and constructive.

3. **Asterin - Synthesis Guide**
   - Star-rooted and procedural.
   - Stronger as a technical product name, weaker as a human companion name.

### 3. Link / Map Agent

This role maintains backlinks, maps of content, and traversal paths.

1. **Ariun - Link Guide**
   - Best pick.
   - Carries Ariadne's thread without using the full mythological name.
   - Perfect semantic fit for navigation through complexity.

2. **Ariad - Link Guide**
   - Still a strong fallback.
   - Carries the thread signal clearly, but has more non-AI brand presence than Ariun.

3. **Ionia - Link Guide**
   - Classical geography rather than deity.
   - Good for network and region-of-knowledge feeling, but less immediately functional.

### 4. Archive / Provenance Agent

This role keeps raw sources, archive material, and evidence boundaries clean.

1. **Mnara - Archive Guide**
   - Best pick.
   - Memory-rooted without using `Mneme`, `Mnemosyne`, `Memo`, or `Memory`.
   - Proprietary-feeling and clean in the collision pass.

2. **Mneris - Archive Guide**
   - Stronger mythic echo than Mnara.
   - Slightly stranger on first read, so weaker for marketplace speed.

3. **Ione - Archive Guide**
   - Quiet, old, and elegant.
   - Good archive tone; weaker role signal than Mnara.

## Recommended Naming Set

Use this as the default if no further discussion is needed:

- **Caelir - Context Guide**
- **Ilyris - Synthesis Guide**
- **Ariun - Link Guide**
- **Mnara - Archive Guide**

This set is coherent: four short names, all mythic-adjacent, none heavy-handed, each tied to a clear operational role.

## Where to Apply

Recommended package edits:

- Keep `CLAUDE.md` as a filename for Claude Code compatibility.
- Change the visible heading to `# Caelir - Context Guide`.
- Add a short line under the heading: `This file gives the agent its standing map before work begins.`
- Rename the visible title of `skills/synthesis_prompt.md` to `# Ilyris - Synthesis Guide`.
- Add companion skill files:
  - `skills/link_guide.md`
  - `skills/archive_guide.md`
- Include `scripts/rename_guides.py` so buyers can change the visible guide names without editing every file manually.

Do not rename the folders. Folder names should stay functional: `raw`, `wiki`, `skills`, `archive`, `templates`.

## Sources Used

- MIT / AI Agent Index 2025: agent product names and category spread, including Claude Code, Manus, Codex, Comet, Agentforce, Jules, and Atlas.
  - https://aiagentindex.mit.edu/data/2025-AI-Agent-Index.pdf
- AgentMarketCap 2026 agent list: current visible naming collisions and category signals, including Project Astra, Devin, Manus, Codex CLI, Cursor, and other named agents.
  - https://agentmarketcap.ai/
- arXiv 2026 coding-agent comparison: confirms major coding-agent market set: Codex, Copilot, Devin, Cursor, Claude Code.
  - https://arxiv.org/abs/2602.08915
- Anthropic 2026 enterprise-agent briefing: confirms enterprise agents are spreading beyond coding into knowledge-worker workflows.
  - https://www.anthropic.com/events/the-briefing-enterprise-agents-virtual-event
- SSA 2024 names release: used only as a weak trend signal for soft-vowel, cross-cultural, rising-name patterns.
  - https://www.ssa.gov/blog/en/posts/2025-05-09.html
- Collision checks on candidate names, including Oryn, Elen, Auren, Velora, Elion, and Kleia, were run on 2026-04-19.

## Related

- [[Governance and PHAROS MOC]]
- [[Ask Vault — EMERAULD Vault Briefing Skill]]
