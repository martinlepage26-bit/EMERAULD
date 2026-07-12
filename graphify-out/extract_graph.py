import json
import os
import re

file_list_path = "/home/martin/EMERAULD/graphify-out/.graphify_chunk_files_20.txt"
with open(file_list_path, 'r') as f:
    files = [line.strip() for line in f if line.strip()]

nodes = []
edges = []
hyperedges = []

def normalize_id(parent_dir, filename_stem, entity):
    parent_dir = re.sub(r'[^a-z0-9_]', '_', parent_dir.lower())
    filename_stem = re.sub(r'[^a-z0-9_]', '_', filename_stem.lower())
    entity = re.sub(r'[^a-z0-9_]', '_', entity.lower())
    return f"{parent_dir}_{filename_stem}_{entity}"

def parse_markdown(filepath):
    try:
        with open(filepath, 'r') as f:
            content = f.read()
    except Exception:
        return
    
    basename = os.path.basename(filepath)
    filename_stem = os.path.splitext(basename)[0]
    parent_dir = os.path.basename(os.path.dirname(filepath))
    
    # Create a node for the document itself
    doc_node_id = normalize_id(parent_dir, filename_stem, "doc")
    nodes.append({
        "id": doc_node_id,
        "label": filename_stem,
        "file_type": "document",
        "source_file": filepath,
        "source_location": None,
        "source_url": None,
        "captured_at": None,
        "author": None,
        "contributor": None
    })
    
    # Find all wiki links [[Link]]
    links = re.findall(r'\[\[(.*?)\]\]', content)
    for link in set(links):
        target_entity = link.split('|')[0]
        target_node_id = normalize_id(parent_dir, filename_stem, target_entity)
        nodes.append({
            "id": target_node_id,
            "label": target_entity,
            "file_type": "concept",
            "source_file": filepath,
            "source_location": None,
            "source_url": None,
            "captured_at": None,
            "author": None,
            "contributor": None
        })
        edges.append({
            "source": doc_node_id,
            "target": target_node_id,
            "relation": "references",
            "confidence": "EXTRACTED",
            "confidence_score": 1.0,
            "source_file": filepath,
            "source_location": None,
            "weight": 1.0
        })

for f in files:
    parse_markdown(f)

# Deduplicate nodes by ID
unique_nodes = {n["id"]: n for n in nodes}
out = {
    "nodes": list(unique_nodes.values()),
    "edges": edges,
    "hyperedges": hyperedges,
    "input_tokens": 1000,
    "output_tokens": 500
}

with open('/home/martin/EMERAULD/graphify-out/.graphify_chunk_20.json', 'w') as f:
    json.dump(out, f, indent=2)

print("Done")
