import re
from pathlib import Path

ROOT = Path("/home/martin/EMERAULD")
INDEX_PATH = ROOT / "wiki/Orphan Index — Vault-Level Graph Repair 2026-05-06.md"
HOME_PATH = ROOT / "wiki/Home.md"

def split_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text
    body = text[end + 4 :].lstrip("\n")
    return {}, body

def is_empty(path):
    if not path.exists():
        return True
    _, body = split_frontmatter(path.read_text(encoding="utf-8", errors="ignore"))
    return len(body.strip()) == 0

def main():
    content = INDEX_PATH.read_text(encoding="utf-8")
    links = re.findall(r"^- \[\[(.*?)\]\]", content, re.MULTILINE)
    
    orphans = []
    for link in links:
        path = ROOT / (link + ".md")
        if not path.exists():
            path = ROOT / link # Maybe no .md suffix in the link, but wait, usually wikilinks imply .md
            if not path.exists() and not link.endswith(".md"):
                path = ROOT / (link + ".md")
                
        if path.exists():
            orphans.append(path)

    deleted_count = 0
    valid_orphans = []
    
    for path in orphans:
        if is_empty(path):
            path.unlink()
            deleted_count += 1
            print(f"Deleted empty orphan: {path.relative_to(ROOT)}")
        else:
            valid_orphans.append(path)
            
    print(f"Deleted {deleted_count} empty orphan files.")

    # Group by top directory
    groups = {}
    for path in valid_orphans:
        rel = path.relative_to(ROOT)
        top = rel.parts[0]
        if top in {".trash", "archive"}:
            continue
        groups.setdefault(top, []).append(path)
        
    mocs_created = []
    
    for top, paths in groups.items():
        if top == "wiki":
            moc_name = "Wiki MOC.md"
        else:
            moc_name = f"{top.upper()} MOC.md"
            
        moc_path = ROOT / "wiki" / moc_name
        
        # Read or create MOC
        if moc_path.exists():
            moc_text = moc_path.read_text(encoding="utf-8")
        else:
            moc_text = f"---\ntype: moc\ntitle: {top} MOC\n---\n\n# {top} MOC\n\n"
            mocs_created.append(moc_name)
            
        # Append links if not present
        appended = 0
        for p in paths:
            rel_no_ext = p.relative_to(ROOT).with_suffix("").as_posix()
            link_str = f"- [[{rel_no_ext}]]"
            if link_str not in moc_text:
                if appended == 0:
                    moc_text += "\n## Recovered Orphans (2026-07-01)\n\n"
                moc_text += f"{link_str}\n"
                appended += 1
                
        if appended > 0:
            moc_path.write_text(moc_text, encoding="utf-8")
            print(f"Added {appended} links to {moc_name}")

    # Ensure Home.md links to the new MOCs
    if HOME_PATH.exists():
        home_text = HOME_PATH.read_text(encoding="utf-8")
        home_appended = 0
        
        for moc_name in mocs_created:
            moc_rel = f"wiki/{moc_name[:-3]}"
            link_str = f"- [[{moc_rel}]]"
            if link_str not in home_text:
                if home_appended == 0:
                    home_text += "\n## Directory MOCs\n\n"
                home_text += f"{link_str}\n"
                home_appended += 1
                
        if home_appended > 0:
            HOME_PATH.write_text(home_text, encoding="utf-8")
            print(f"Added {home_appended} MOC links to Home.md")

if __name__ == "__main__":
    main()
