import math, json
from pathlib import Path

uncached = Path('graphify-out/.graphify_uncached.txt').read_text(encoding='utf-8').splitlines()
uncached = [f for f in uncached if f.strip()]

images = [f for f in uncached if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.svg', '.webp'))]
docs = [f for f in uncached if f not in images]

chunk_size = 22
doc_chunks = [docs[i:i + chunk_size] for i in range(0, len(docs), chunk_size)]
all_chunks = doc_chunks + [[img] for img in images]
total_chunks = len(all_chunks)

prompt_template = Path('/home/martin/.gemini/antigravity-cli/skills/graphify/references/extraction-spec.md').read_text(encoding='utf-8')
if '```' in prompt_template:
    prompt_template = prompt_template.split('```')[1]

Path('graphify-out/.graphify_extraction_template.txt').write_text(prompt_template.strip(), encoding='utf-8')

cwd = Path('/home/martin/EMERAULD')

subagents_json = []
for i, chunk in enumerate(all_chunks, 1):
    chunk_path_txt = cwd / f'graphify-out/.graphify_chunk_files_{i:02d}.txt'
    chunk_path_txt.write_text('\n'.join(chunk), encoding='utf-8')
    chunk_out = cwd / f'graphify-out/.graphify_chunk_{i:02d}.json'
    
    prompt = f"""Read the exact prompt template from {cwd}/graphify-out/.graphify_extraction_template.txt.
Substitute the following values into that template:
FILE_LIST = The files listed in {chunk_path_txt}
CHUNK_NUM = {i}
TOTAL_CHUNKS = {total_chunks}
DEEP_MODE = false
CHUNK_PATH = {chunk_out}

Follow the template exactly and write your output to {chunk_out} using the write_to_file tool."""
    
    subagents_json.append({
        'TypeName': 'self',
        'Role': f'Graphify Extractor Chunk {i:02d}',
        'Prompt': prompt
    })

Path('graphify-out/.graphify_subagents.json').write_text(json.dumps(subagents_json, indent=2), encoding='utf-8')
print(f"Generated {total_chunks} chunks.")
