import json
import re
import os

files = [
    "/home/martin/EMERAULD/Areas/PHAROS/CONTROL 2 — External Data Lifecycle Protocol (Regulatory Grounding).md",
    "/home/martin/EMERAULD/Areas/PHAROS/CONTROL 3 — Architecture Deprecation Protocol (Regulatory Grounding).md",
    "/home/martin/EMERAULD/Areas/PHAROS/Claude Code Skill Corpus.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Conceptual Vocabulary — Praxis, Politics, Strategy, Form, Systems.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Control Protocols MOC.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Elemental Agents Framework.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Epistemic AI Purple Teaming.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Epistemic Operator — Operational Specification.md",
    "/home/martin/EMERAULD/Areas/PHAROS/External Data Refresh Calendar — Phase 1 Build.md",
    "/home/martin/EMERAULD/Areas/PHAROS/External Data Registry — Phase 1 Build.md",
    "/home/martin/EMERAULD/Areas/PHAROS/First Method Paper — Recursive AI Governance as Executable Method.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Founder Charter — Lepage and Stocker.md",
    "/home/martin/EMERAULD/Areas/PHAROS/GSD Tier 1 — Core Workflow Skills Hub.md",
    "/home/martin/EMERAULD/Areas/PHAROS/GSD Tier 2 — Knowledge Synthesis Skills.md",
    "/home/martin/EMERAULD/Areas/PHAROS/GSD Tier 3 — Communication and Artifact Skills.md",
    "/home/martin/EMERAULD/Areas/PHAROS/GSD Tier 4 — Personal Capabilities.md",
    "/home/martin/EMERAULD/Areas/PHAROS/GSD — Get-Shit-Done Claude Code System.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Global Publication Search — PHAROS Method and Variants.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Governance Controls Integration Dashboard.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Governance Controls — Incident Response (Control Failure Procedures).md",
    "/home/martin/EMERAULD/Areas/PHAROS/Governance Controls — Monitoring Plan & Automation Roadmap.md",
    "/home/martin/EMERAULD/Areas/PHAROS/Governance Typology — Recursive AI Governance Taxonomy.md"
]

def make_id(filepath, entity):
    parent = os.path.basename(os.path.dirname(filepath))
    stem = os.path.splitext(os.path.basename(filepath))[0]
    raw = f"{parent}_{stem}_{entity}"
    return re.sub(r'[^a-z0-9]', '_', raw.lower()).strip('_')

nodes = []
edges = []

def add_node(filepath, name, type, properties):
    nodes.append({
        "id": make_id(filepath, name),
        "name": name,
        "type": type,
        "properties": properties,
        "source_file": filepath
    })

def add_edge(source_filepath, source_entity, target_filepath, target_entity, rel_type, evidence, confidence, extraction_type):
    edges.append({
        "source": make_id(source_filepath, source_entity),
        "target": make_id(target_filepath, target_entity),
        "type": rel_type,
        "evidence": evidence,
        "confidence": confidence,
        "extraction_type": extraction_type
    })

add_node(files[0], "External Data Lifecycle Protocol", "PROTOCOL", {"regulatory_anchors": ["GDPR", "CCPA", "HIPAA", "FINRA"]})
add_node(files[0], "External Data Registry", "SYSTEM", {"purpose": "Inventory external dependencies"})
add_edge(files[0], "External Data Lifecycle Protocol", files[0], "External Data Registry", "DEPENDS_ON", "Registry holds the data", 0.9, "EXTRACTED")

add_node(files[1], "Architecture Deprecation Protocol", "PROTOCOL", {"regulatory_anchors": ["ISO 15489", "ITIL"]})
add_node(files[1], "Supersession Registry", "SYSTEM", {"purpose": "Track architecture succession"})
add_edge(files[1], "Architecture Deprecation Protocol", files[1], "Supersession Registry", "DEPENDS_ON", "Registry tracks transitions", 0.9, "EXTRACTED")

add_node(files[2], "Claude Code Skill Corpus", "SYSTEM", {"purpose": "Repository of Claude capabilities"})
add_node(files[3], "Conceptual Vocabulary", "DOCUMENT", {"purpose": "Defines key terms for PHAROS"})
add_node(files[4], "Control Protocols MOC", "DOCUMENT", {"purpose": "Map of Content for Controls"})

add_node(files[5], "Elemental Agents Framework", "FRAMEWORK", {"purpose": "Metaphorical AI agent roles"})
add_node(files[5], "WIND", "AGENT_ROLE", {"purpose": "Exploratory logic"})
add_edge(files[5], "Elemental Agents Framework", files[5], "WIND", "CONTAINS", "Part of the framework", 0.9, "EXTRACTED")

add_node(files[6], "Epistemic AI Purple Teaming", "METHODOLOGY", {"purpose": "Test boundaries of LLM belief"})
add_node(files[7], "Epistemic Operator", "ROLE", {"purpose": "Accountable human layer"})
add_node(files[8], "External Data Refresh Calendar", "DOCUMENT", {"purpose": "Schedule for checking policies"})
add_node(files[9], "External Data Registry Phase 1", "SYSTEM", {"purpose": "Initial build of registry"})

add_node(files[10], "Recursive AI Governance as Executable Method", "PAPER", {"purpose": "Primary method paper"})
add_node(files[11], "Founder Charter", "DOCUMENT", {"purpose": "Decision rights structure"})
add_node(files[11], "Martin Lepage", "PERSON", {"role": "Technical Operator"})
add_node(files[11], "Martin Stocker", "PERSON", {"role": "Commercial Operator"})
add_edge(files[11], "Founder Charter", files[11], "Martin Lepage", "GOVERNS", "Defines roles", 0.9, "EXTRACTED")

add_node(files[12], "GSD Tier 1", "SYSTEM", {"purpose": "Core workflow skills"})
add_node(files[13], "GSD Tier 2", "SYSTEM", {"purpose": "Knowledge synthesis skills"})
add_node(files[14], "GSD Tier 3", "SYSTEM", {"purpose": "Communication skills"})
add_node(files[15], "GSD Tier 4", "SYSTEM", {"purpose": "Personal capabilities"})
add_node(files[16], "Get-Shit-Done System", "TOOL", {"purpose": "Context rot mitigation"})

add_node(files[17], "Global Publication Search", "REPORT", {"purpose": "Prior art research for PHAROS"})
add_node(files[18], "Governance Controls Integration Dashboard", "DASHBOARD", {"purpose": "Layer 0.5 gate monitor"})
add_node(files[19], "Incident Response Procedures", "PROTOCOL", {"purpose": "Handling control failures"})
add_node(files[20], "Monitoring Plan and Automation Roadmap", "ROADMAP", {"purpose": "Transition to automated controls"})
add_node(files[21], "Governance Typology", "TAXONOMY", {"purpose": "Classification of governance documents"})

out = {
    "chunk_id": "04",
    "files_processed": len(files),
    "nodes": nodes,
    "edges": edges
}

with open("/home/martin/EMERAULD/graphify-out/.graphify_chunk_04.json", "w") as f:
    json.dump(out, f, indent=2)

print("Done")
