import os
import re

wiki_dir = "/home/martin/EMERAULD/wiki"
files = []
for root, _, filenames in os.walk(wiki_dir):
    for f in filenames:
        if f.endswith('.md'):
            files.append(os.path.join(root, f))

# Map filename without extension to file path
notes = {os.path.basename(f)[:-3]: f for f in files}

# Also map lowercase for case-insensitive matching
notes_lower = {k.lower(): k for k in notes.keys()}

links_to = {k: set() for k in notes.keys()}

wikilink_pattern = re.compile(r'\[\[(.*?)\]\]')

for fpath in files:
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    src_note = os.path.basename(fpath)[:-3]

    links = wikilink_pattern.findall(content)
    for link in links:
        # handle aliases [[Note Name|Alias]]
        target = link.split('|')[0].strip()
        target_lower = target.lower()
        if target_lower in notes_lower:
            actual_target = notes_lower[target_lower]
            if actual_target != src_note:
                links_to[actual_target].add(src_note)

orphans = [n for n in notes.keys() if len(links_to[n]) == 0]
print("Orphans found:")
for o in sorted(orphans):
    print(o)
