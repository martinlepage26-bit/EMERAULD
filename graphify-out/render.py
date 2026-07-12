import os

template_path = "/home/martin/EMERAULD/graphify-out/.graphify_extraction_template.txt"
file_list_path = "/home/martin/EMERAULD/graphify-out/.graphify_chunk_files_20.txt"

with open(template_path, 'r') as f:
    template = f.read()

with open(file_list_path, 'r') as f:
    file_list = f.read().strip()

template = template.replace("FILE_LIST", file_list)
template = template.replace("CHUNK_NUM", "20")
template = template.replace("TOTAL_CHUNKS", "56")
template = template.replace("DEEP_MODE", "false")
template = template.replace("CHUNK_PATH", "/home/martin/EMERAULD/graphify-out/.graphify_chunk_20.json")

with open("/home/martin/EMERAULD/graphify-out/rendered_prompt.txt", "w") as f:
    f.write(template)
