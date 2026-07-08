import json
import os

graph_path = "/home/martin/EMERAULD/graphify-out/graph.json"

with open(graph_path, 'r') as f:
    graph = json.load(f)

percephal_node = {
    "id": "healing_the_fisher_king_percephal_diagnostic_protocol",
    "label": "Healing the Fisher King — Percephal Diagnostic Protocol",
    "file_type": "document",
    "source_file": "wiki/Healing the Fisher King — Percephal Diagnostic Protocol.md"
}

# Check if it already exists
if not any(n['id'] == percephal_node['id'] for n in graph['nodes']):
    graph['nodes'].append(percephal_node)

edges = [
    {"source": percephal_node["id"], "target": "fisher_king_hub_project_recovery_map", "relationship": "references"},
    {"source": percephal_node["id"], "target": "personal_and_projects_moc", "relationship": "references"},
    {"source": percephal_node["id"], "target": "projects_hub", "relationship": "references"},
    {"source": percephal_node["id"], "target": "emerauld", "relationship": "references"},
    {"source": percephal_node["id"], "target": "pharos_method_technical_reference", "relationship": "references"},
    {"source": percephal_node["id"], "target": "recursive_governance_method", "relationship": "references"},
    {"source": percephal_node["id"], "target": "mythocritique_to_pharos_the_2010_masters_thesis_as_methodological_keystone", "relationship": "references"},
    {"source": percephal_node["id"], "target": "master_project_tracker_2026", "relationship": "references"},
    {"source": percephal_node["id"], "target": "the_lost_loop_pattern_avoidance_through_system_building", "relationship": "references"},
    {"source": percephal_node["id"], "target": "posture_vs_execution_drift_the_practice_of_refusal", "relationship": "references"}
]

for edge in edges:
    if not any(e['source'] == edge['source'] and e['target'] == edge['target'] for e in graph['links']):
        graph['links'].append(edge)

with open(graph_path, 'w') as f:
    json.dump(graph, f, indent=2)

print("Injected Percephal protocol into graph.json!")
