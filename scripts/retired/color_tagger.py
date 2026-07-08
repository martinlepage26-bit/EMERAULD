import yaml
from pathlib import Path

ROOT = Path("/home/martin/EMERAULD")

# Elemental Correspondences
COLOR_KEYWORDS = {
    "red": ["fire", "conflict", "action", "attack", "threat", "security", "red-team", "danger", "risk", "execute", "force", "power", "war", "urgent", "critical"],
    "orange": ["construct", "system", "framework", "tool", "build", "process", "setup", "create", "design", "operation", "agent", "script", "code"],
    "lime": ["new", "raw", "spark", "idea", "initial", "draft", "intake", "start", "fresh", "quick", "scratch", "seed"],
    "green": ["nature", "plant", "root", "history", "earth", "archive", "memory", "grow", "established", "base", "ground", "life", "wealth"],
    "teal": ["network", "web", "tech", "digital", "internet", "link", "connect", "api", "integration", "communication", "bridge", "node", "graph"],
    "blue": ["deep", "thought", "psychology", "analysis", "emotion", "water", "fluid", "logic", "science", "research", "study", "data"],
    "violet": ["spirit", "magic", "esoteric", "theory", "abstract", "occult", "dream", "philosophy", "aether", "mind", "concept"],
    "purple": ["governance", "law", "rule", "protocol", "control", "index", "master", "authoritative", "policy", "admin", "manage", "lead"],
    "pink": ["care", "empathy", "human", "community", "social", "peer", "harmony", "love", "heart", "help", "support", "ethics"]
}

def split_frontmatter(text):
    if not text.startswith("---\n"):
        return {}, text, ""
    end = text.find("\n---", 4)
    if end == -1:
        return {}, text, ""
    raw = text[4:end]
    body = text[end + 4 :].lstrip("\n")
    try:
        meta = yaml.safe_load(raw) or {}
    except Exception:
        meta = {}
    return meta, body, text[:end+4]

def assign_color(tags, title, body):
    scores = {color: 0 for color in COLOR_KEYWORDS}
    
    # Check against tags
    for tag in tags:
        tag_lower = str(tag).lower()
        for color, keywords in COLOR_KEYWORDS.items():
            if any(kw in tag_lower for kw in keywords):
                scores[color] += 3
                
    # Check against title
    title_lower = str(title).lower()
    for color, keywords in COLOR_KEYWORDS.items():
        if any(kw in title_lower for kw in keywords):
            scores[color] += 2
            
    # Quick text scan of body
    body_lower = body.lower()
    for color, keywords in COLOR_KEYWORDS.items():
        for kw in keywords:
            scores[color] += body_lower.count(kw) * 0.1
            
    # Determine max color
    max_score = max(scores.values())
    if max_score > 0:
        # Get all colors with max score
        candidates = [c for c, v in scores.items() if v == max_score]
        # Tie breaker: deterministic based on title hash length to stay stable
        return candidates[len(title) % len(candidates)]
        
    # Default color if no matches (e.g. gray, but user asked for these 9)
    # We will deterministically pick one based on title length
    colors = list(COLOR_KEYWORDS.keys())
    return colors[len(title) % len(colors)]


def main():
    paths = list(ROOT.rglob("*.md"))
    paths = [p for p in paths if not any(part == ".git" or part == ".trash" or part == "raw sources" for part in p.parts)]
    
    updated_count = 0
    color_distribution = {c: 0 for c in COLOR_KEYWORDS}
    
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            meta, body, _ = split_frontmatter(text)
            
            existing_tags = meta.get("tags")
            if existing_tags is None:
                existing_tags = []
            elif isinstance(existing_tags, str):
                existing_tags = [existing_tags]
            elif not isinstance(existing_tags, list):
                existing_tags = list(existing_tags)
                
            title = meta.get("title", path.stem)
            
            color = assign_color(existing_tags, title, body)
            color_tag = f"color-{color}"
            
            original_tags_set = {str(t).lower() for t in existing_tags}
            
            # Remove any old color tags if present so we don't duplicate
            filtered_tags = [t for t in existing_tags if not str(t).startswith("color-")]
            
            if color_tag not in {str(t).lower() for t in filtered_tags}:
                filtered_tags.append(color_tag)
                meta["tags"] = filtered_tags
                
                new_fm_raw = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, default_flow_style=False)
                new_content = f"---\n{new_fm_raw}---\n\n{body.lstrip()}"
                
                path.write_text(new_content, encoding="utf-8")
                updated_count += 1
                
            color_distribution[color] += 1
                
        except Exception as e:
            print(f"Error updating {path}: {e}")
            
    print(f"Added elemental color tags to {updated_count} files.")
    print("Color Distribution:")
    for c, count in color_distribution.items():
        print(f"  {c}: {count}")

if __name__ == "__main__":
    main()
