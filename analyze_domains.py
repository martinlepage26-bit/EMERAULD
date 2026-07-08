import json
from collections import defaultdict

graph_path = "/home/martin/EMERAULD/graphify-out/graph.json"

with open(graph_path, 'r') as f:
    graph = json.load(f)

# Count nodes per community
community_counts = defaultdict(int)
community_files = defaultdict(list)

for node in graph.get('nodes', []):
    comm = node.get('community', 'Unknown')
    community_counts[comm] += 1
    # store a few sample files to understand what the community is
    if len(community_files[comm]) < 5:
        source = node.get('source_file', '')
        if source:
            community_files[comm].append(source)

# Sort communities by size
sorted_comms = sorted(community_counts.items(), key=lambda x: x[1], reverse=True)

print("Top 10 Largest Domains (Communities) in the Graph:")
for comm, count in sorted_comms[:10]:
    print(f"\n{comm}: {count} nodes")
    for file in community_files[comm]:
        print(f"  - {file}")
