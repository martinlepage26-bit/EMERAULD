"""
Personal-Assistant Agent MCP Server
Vault: vlt_011Ca4JWpYokA1iNPqWWJjrx

Exposes the 12-agent personal-assistant ecosystem (vault maintenance + content
commercialization) as callable MCP tools for Claude Console.

Run:
    python server.py [--transport sse|stdio] [--port 8000]
"""

import os
import sys
import json
import argparse
from pathlib import Path

from fastmcp import FastMCP

# ---------------------------------------------------------------------------
# Vault config
# ---------------------------------------------------------------------------
VAULT_ID = "vlt_011Ca4JWpYokA1iNPqWWJjrx"
VAULT_ROOT = Path(__file__).parent.parent.parent  # EMERAULD/
AGENTS_ROOT = Path(__file__).parent.parent         # personal-assistant-agents/

mcp = FastMCP(
    name="personal-assistant",
    instructions=(
        "You are connected to the Personal-Assistant Agent ecosystem. "
        "It has two operating modes: (1) vault maintenance — ingesting, synthesising, "
        "linking, and retrieving notes in the EMERAULD knowledge vault; "
        "(2) content commercialisation — inventorying, pricing, listing, dispatching, "
        "and optimising owned content across marketplaces. "
        "Start with `triage` to route any ambiguous request. "
        f"Vault ID: {VAULT_ID}"
    ),
)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _skill_path(agent_slug: str) -> Path:
    return AGENTS_ROOT / agent_slug / "SKILL.md"


def _read_skill(agent_slug: str) -> str:
    p = _skill_path(agent_slug)
    if p.exists():
        return p.read_text(encoding="utf-8")
    return f"[SKILL.md not found for {agent_slug}]"


def _agent_result(agent: str, lane: str, output: dict) -> dict:
    return {
        "agent": agent,
        "vault_id": VAULT_ID,
        "lane": lane,
        "output": output,
    }


# ---------------------------------------------------------------------------
# Tier 0 — Routing
# ---------------------------------------------------------------------------

@mcp.tool()
def triage(request: str, context: str = "") -> dict:
    """
    Route any incoming request across vault-maintenance and marketplace lanes.
    Returns the recommended agent chain and handoff inputs.

    Args:
        request: The raw user ask, note, or asset packet.
        context: Optional: hub notes, product context, or goals already stated.
    """
    skill = _read_skill("intake-triager")
    # The tool surfaces the routing logic; Claude executes it given the skill.
    return _agent_result(
        agent="intake-triager",
        lane="routing",
        output={
            "skill_loaded": True,
            "request_received": request,
            "context_received": context or "(none)",
            "instruction": (
                "Apply the Intake Triager skill to the request. "
                "Separate work into vault, retrieval, commercialisation, or post-launch lanes. "
                "Return: chosen lane(s), next agent(s), required inputs, open risks."
            ),
            "skill_excerpt": skill[:1200],
        },
    )


# ---------------------------------------------------------------------------
# Vault Maintenance Lane
# ---------------------------------------------------------------------------

@mcp.tool()
def archive_raw(
    content: str,
    source: str,
    commercial_intent: str = "unspecified",
) -> dict:
    """
    Preserve raw source material with stable filename, provenance, and
    commercial trace before any editing or selling.

    Args:
        content: The raw material to archive (text, excerpt, or description).
        source: Origin of the material (URL, filename, meeting, date, etc.).
        commercial_intent: What the operator plans to do with this content.
    """
    skill = _read_skill("raw-archivist")
    suggested_filename = (
        source.replace(" ", "-").replace("/", "-").replace(":", "").lower()[:60]
        + ".md"
    )
    return _agent_result(
        agent="raw-archivist",
        lane="vault-maintenance",
        output={
            "action": "archive",
            "suggested_path": f"raw sources/{suggested_filename}",
            "source": source,
            "commercial_intent": commercial_intent,
            "next_handoff": "synthesise_note or rights_check",
            "instruction": (
                "Apply Raw Archivist skill. Preserve provenance. "
                "Do not edit the raw content. Return canonical filename and trace."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def synthesise_note(
    raw_content: str,
    source_file: str = "",
    output_type: str = "wiki_note",
) -> dict:
    """
    Turn raw material into a durable wiki note, editorial brief, or structured
    content packet without losing source trace.

    Args:
        raw_content: The source text to synthesise.
        source_file: Path to the raw source file in the vault.
        output_type: One of: wiki_note, editorial_brief, content_packet.
    """
    skill = _read_skill("synthesis-editor")
    return _agent_result(
        agent="synthesis-editor",
        lane="vault-maintenance",
        output={
            "output_type": output_type,
            "source_file": source_file or "(inline content)",
            "instruction": (
                "Apply Synthesis Editor skill. Produce a durable retrieval object. "
                "Preserve source trace. Link to related wiki notes. "
                "Return: note, chosen title, source trace, next handoff."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def normalize_metadata(
    note_path: str,
    issues: str = "",
) -> dict:
    """
    Normalize frontmatter, source fields, rights flags, status markers, and
    backlinks so the vault stays coherent.

    Args:
        note_path: Relative path to the note inside the EMERAULD vault.
        issues: Known metadata problems or missing fields.
    """
    skill = _read_skill("metadata-link-warden")
    return _agent_result(
        agent="metadata-link-warden",
        lane="vault-maintenance",
        output={
            "note_path": note_path,
            "reported_issues": issues or "(none stated)",
            "instruction": (
                "Apply Metadata and Link Warden skill. "
                "Return: normalized frontmatter and link structure, "
                "unresolved gaps, required topology or rights follow-up."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def map_vault(
    topic: str = "",
    cluster_notes: list[str] | None = None,
) -> dict:
    """
    Build or update hub structures, topic maps, and retrieval packets so
    humans and agents can find context quickly.

    Args:
        topic: The topic or cluster to map (leave blank to request full audit).
        cluster_notes: Optional list of note filenames already known to belong.
    """
    skill = _read_skill("graph-retrieval-cartographer")
    return _agent_result(
        agent="graph-retrieval-cartographer",
        lane="vault-maintenance",
        output={
            "topic": topic or "(full vault audit)",
            "seed_notes": cluster_notes or [],
            "instruction": (
                "Apply Graph and Retrieval Cartographer skill. "
                "Return: updated hub or map note, organization logic, "
                "source notes included, missing or contradictory material."
            ),
            "skill_excerpt": skill[:800],
        },
    )


# ---------------------------------------------------------------------------
# Content Commercialisation Lane
# ---------------------------------------------------------------------------

@mcp.tool()
def inventory_content(
    content_description: str,
    known_assets: list[str] | None = None,
) -> dict:
    """
    Map owned content into reusable assets, product families, and saleable
    inventory before marketplace work begins.

    Args:
        content_description: Description of the content corpus or asset set.
        known_assets: Optional list of already-identified asset filenames/titles.
    """
    skill = _read_skill("content-inventory-cartographer")
    return _agent_result(
        agent="content-inventory-cartographer",
        lane="commercialisation",
        output={
            "content_description": content_description,
            "known_assets": known_assets or [],
            "instruction": (
                "Apply Content Inventory Cartographer skill. "
                "Return: inventory map, candidate SKUs/bundles/derivatives, "
                "readiness notes, missing-piece flags, next commercialisation handoffs."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def scout_demand(
    product_idea: str,
    target_marketplaces: list[str] | None = None,
) -> dict:
    """
    Read marketplace demand, competitor patterns, and channel fit for an
    owned content candidate.

    Args:
        product_idea: What the content product is or could be.
        target_marketplaces: e.g. ["Gumroad", "Etsy", "Udemy", "Substack"].
    """
    skill = _read_skill("demand-scout")
    return _agent_result(
        agent="demand-scout",
        lane="commercialisation",
        output={
            "product_idea": product_idea,
            "target_marketplaces": target_marketplaces or ["(unspecified)"],
            "instruction": (
                "Apply Demand Scout skill. "
                "Return: opportunity ranking, marketplaces or buyer segments worth testing, "
                "demand and saturation signals, recommended next step."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def check_rights(
    content_candidates: list[str],
    marketplaces: list[str] | None = None,
) -> dict:
    """
    Check rights, licensing, usage limits, and marketplace-policy fit for
    content before packaging or dispatch.

    Args:
        content_candidates: List of content titles or asset identifiers.
        marketplaces: Target marketplaces to check policy compliance for.
    """
    skill = _read_skill("rights-policy-warden")
    return _agent_result(
        agent="rights-policy-warden",
        lane="commercialisation",
        output={
            "content_candidates": content_candidates,
            "marketplaces": marketplaces or ["(unspecified)"],
            "instruction": (
                "Apply Rights and Policy Warden skill. "
                "Return: rights/policy status per candidate, allowed/restricted/blocked uses, "
                "required attributions, next safe commercialisation handoff."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def design_offer(
    content_title: str,
    rights_cleared: bool = False,
    demand_signals: str = "",
    target_price_range: str = "",
) -> dict:
    """
    Package safe, owned content into sellable offers, bundles, tiers, and
    price ladders matched to marketplace reality.

    Args:
        content_title: The content product to package.
        rights_cleared: Whether rights_check has been run and cleared.
        demand_signals: Summary of demand-scout findings.
        target_price_range: e.g. "$9–$49" or "freemium + $29 pro".
    """
    skill = _read_skill("offer-pricing-architect")
    return _agent_result(
        agent="offer-pricing-architect",
        lane="commercialisation",
        output={
            "content_title": content_title,
            "rights_cleared": rights_cleared,
            "demand_signals": demand_signals or "(not provided)",
            "target_price_range": target_price_range or "(not specified)",
            "warning": (
                None if rights_cleared
                else "Rights have not been confirmed cleared. Run check_rights first."
            ),
            "instruction": (
                "Apply Offer and Pricing Architect skill. "
                "Return: offer brief, SKU/bundle/tier structure, "
                "price ladder or anchor logic, exclusions and fulfillment notes."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def write_listing(
    offer_brief: str,
    marketplace: str,
    tone: str = "professional",
) -> dict:
    """
    Create marketplace-facing titles, copy, keywords, thumbnails, previews,
    and merchandising assets for an approved offer.

    Args:
        offer_brief: The offer brief from design_offer.
        marketplace: Target platform (e.g. "Gumroad", "Etsy", "Amazon KDP").
        tone: Writing tone (e.g. "professional", "conversational", "academic").
    """
    skill = _read_skill("listing-creative-director")
    return _agent_result(
        agent="listing-creative-director",
        lane="commercialisation",
        output={
            "offer_brief": offer_brief[:500],
            "marketplace": marketplace,
            "tone": tone,
            "instruction": (
                "Apply Listing Creative Director skill. "
                "Return: listing packet (titles, body copy, bullets, FAQs, keywords), "
                "preview/merchandising asset specs, platform-specific notes."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def dispatch_to_marketplace(
    listing_packet: str,
    marketplace: str,
    credentials_confirmed: bool = False,
) -> dict:
    """
    Route a finished offer and listing packet into marketplace-specific launch
    packets, submission checklists, and launch sequences.

    Args:
        listing_packet: Output from write_listing.
        marketplace: The target platform.
        credentials_confirmed: Whether marketplace credentials/account are ready.
    """
    skill = _read_skill("marketplace-dispatcher")
    return _agent_result(
        agent="marketplace-dispatcher",
        lane="commercialisation",
        output={
            "marketplace": marketplace,
            "credentials_confirmed": credentials_confirmed,
            "listing_preview": listing_packet[:300],
            "warning": (
                None if credentials_confirmed
                else "Marketplace credentials not confirmed. Verify account access before dispatch."
            ),
            "instruction": (
                "Apply Marketplace Dispatcher skill. "
                "Return: marketplace-specific launch packets, launch sequence/checklist, "
                "blockers or missing credentials, post-launch metrics to watch."
            ),
            "skill_excerpt": skill[:800],
        },
    )


@mcp.tool()
def optimise_revenue(
    product_id: str,
    sales_signals: str,
    support_issues: str = "",
) -> dict:
    """
    Interpret sales data, buyer-support signals, and review patterns; feed
    iteration back to upstream agents.

    Args:
        product_id: Identifier for the launched product.
        sales_signals: Sales data summary (revenue, conversion rate, refunds, etc.).
        support_issues: Common buyer questions, complaints, or refund reasons.
    """
    skill = _read_skill("revenue-support-optimizer")
    return _agent_result(
        agent="revenue-support-optimizer",
        lane="post-launch",
        output={
            "product_id": product_id,
            "sales_signals": sales_signals,
            "support_issues": support_issues or "(none reported)",
            "instruction": (
                "Apply Revenue and Support Optimizer skill. "
                "Return: post-launch signal summary, likely causes of performance/support friction, "
                "recommended upstream revisions or experiments, evidence gaps."
            ),
            "skill_excerpt": skill[:800],
        },
    )


# ---------------------------------------------------------------------------
# Utility tools
# ---------------------------------------------------------------------------

@mcp.tool()
def list_agents() -> dict:
    """List all available agents with their lane and one-line description."""
    roster = [
        {"slug": "intake-triager",              "lane": "routing",            "description": "Route mixed requests across vault-maintenance and marketplace lanes."},
        {"slug": "raw-archivist",               "lane": "vault-maintenance",  "description": "Preserve raw source material with provenance and commercial trace."},
        {"slug": "synthesis-editor",            "lane": "vault-maintenance",  "description": "Turn raw material into durable wiki notes or content packets."},
        {"slug": "metadata-link-warden",        "lane": "vault-maintenance",  "description": "Normalize frontmatter, links, and backlinks across the vault."},
        {"slug": "graph-retrieval-cartographer","lane": "vault-maintenance",  "description": "Build hub structures, topic maps, and retrieval packets."},
        {"slug": "content-inventory-cartographer","lane": "commercialisation","description": "Map owned content into saleable inventory and product families."},
        {"slug": "demand-scout",                "lane": "commercialisation",  "description": "Read marketplace demand, competitor patterns, and channel fit."},
        {"slug": "rights-policy-warden",        "lane": "commercialisation",  "description": "Check rights, licensing, and marketplace-policy fit."},
        {"slug": "offer-pricing-architect",     "lane": "commercialisation",  "description": "Package content into offers, bundles, tiers, and price ladders."},
        {"slug": "listing-creative-director",   "lane": "commercialisation",  "description": "Create marketplace-facing copy, keywords, and merchandising assets."},
        {"slug": "marketplace-dispatcher",      "lane": "commercialisation",  "description": "Route approved offers into marketplace-specific launch packets."},
        {"slug": "revenue-support-optimizer",   "lane": "post-launch",        "description": "Interpret sales and support signals; feed iteration upstream."},
    ]
    return {
        "vault_id": VAULT_ID,
        "agent_count": len(roster),
        "agents": roster,
        "typical_routes": {
            "vault_maintenance": "triage → archive_raw → synthesise_note → normalize_metadata → map_vault",
            "content_to_market": "inventory_content → scout_demand → check_rights → design_offer → write_listing → dispatch_to_marketplace",
            "post_launch_loop":  "optimise_revenue → design_offer / write_listing / dispatch_to_marketplace / scout_demand",
        },
    }


@mcp.tool()
def get_agent_skill(agent_slug: str) -> dict:
    """
    Return the full SKILL.md content for a specific agent.

    Args:
        agent_slug: e.g. "intake-triager", "synthesis-editor", "demand-scout"
    """
    valid = [
        "intake-triager", "raw-archivist", "synthesis-editor",
        "metadata-link-warden", "graph-retrieval-cartographer",
        "content-inventory-cartographer", "demand-scout",
        "rights-policy-warden", "offer-pricing-architect",
        "listing-creative-director", "marketplace-dispatcher",
        "revenue-support-optimizer",
    ]
    if agent_slug not in valid:
        return {"error": f"Unknown agent slug '{agent_slug}'. Valid: {valid}"}
    return {
        "agent_slug": agent_slug,
        "vault_id": VAULT_ID,
        "skill": _read_skill(agent_slug),
    }


@mcp.resource("vault://info")
def vault_info() -> str:
    """Return vault metadata and ecosystem overview."""
    return json.dumps({
        "vault_id": VAULT_ID,
        "vault_root": str(VAULT_ROOT),
        "agents_root": str(AGENTS_ROOT),
        "agent_count": 12,
        "lanes": ["routing", "vault-maintenance", "commercialisation", "post-launch"],
    }, indent=2)


# ---------------------------------------------------------------------------
# Entrypoint
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Personal-Assistant MCP Server")
    parser.add_argument(
        "--transport",
        choices=["stdio", "sse"],
        default="stdio",
        help="Transport protocol (default: stdio for Claude Desktop/Console)",
    )
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for SSE transport (default: 8000)",
    )
    args = parser.parse_args()

    if args.transport == "sse":
        mcp.run(transport="sse", port=args.port)
    else:
        mcp.run(transport="stdio")
