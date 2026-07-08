import re
import math
from pathlib import Path
from collections import defaultdict, Counter
import yaml

ROOT = Path("/home/martin/EMERAULD")

STOPWORDS = {
    "about", "above", "after", "again", "against", "all", "am", "an", "and", "any", "are", "aren", "as", "at",
    "be", "because", "been", "before", "being", "below", "between", "both", "but", "by", "can", "cannot", "could",
    "did", "do", "does", "doing", "down", "during", "each", "few", "for", "from", "further", "had", "has", "have",
    "having", "he", "her", "here", "hers", "herself", "him", "himself", "his", "how", "if", "in", "into", "is",
    "it", "its", "itself", "just", "me", "more", "most", "my", "myself", "no", "nor", "not", "now", "of", "off",
    "on", "once", "only", "or", "other", "our", "ours", "ourselves", "out", "over", "own", "same", "she", "should",
    "so", "some", "such", "than", "that", "the", "their", "theirs", "them", "themselves", "then", "there", "these",
    "they", "this", "those", "through", "to", "too", "under", "until", "up", "very", "was", "we", "were", "what",
    "when", "where", "which", "while", "who", "whom", "why", "will", "with", "you", "your", "yours", "yourself",
    "yourselves", "would", "could", "should", "like", "also", "many", "much", "well", "even", "one", "two", "three",
    "first", "new", "used", "make", "way", "may", "often", "use", "using", "however", "although", "within", "without",
    "among", "whether", "always", "since", "yet", "still", "much", "must", "might", "shall", "can't", "won't", "don't",
    "didn't", "hasn't", "haven't", "isn't", "aren't", "wasn't", "weren't", "doesn't", "wouldn't", "shouldn't",
    "couldn't", "it's", "i'm", "you're", "they're", "we're", "he's", "she's", "that's", "there's", "what's", "who's",
    "where's", "when's", "why's", "how's", "let's", "time", "year", "people", "way", "day", "man", "thing", "woman",
    "life", "child", "world", "school", "state", "family", "student", "group", "country", "problem", "hand", "part",
    "place", "case", "week", "company", "system", "program", "question", "work", "government", "number", "night",
    "point", "home", "water", "room", "mother", "area", "money", "story", "fact", "month", "lot", "right", "study",
    "book", "eye", "job", "word", "business", "issue", "side", "kind", "head", "house", "service", "friend", "father",
    "power", "hour", "game", "line", "end", "member", "law", "car", "city", "community", "name", "president", "team",
    "minute", "idea", "kid", "body", "information", "back", "parent", "face", "others", "level", "office", "door",
    "health", "person", "art", "war", "history", "party", "result", "change", "morning", "reason", "research",
    "girl", "guy", "moment", "air", "teacher", "force", "education", "footnote", "http", "https", "www", "com",
    "org", "net", "html", "pdf", "file", "page", "image", "data", "text", "note", "notes", "type", "link", "links",
    "document", "doc", "docx", "md", "markdown", "vault", "index", "wiki", "folder", "directory", "path", "name",
    "tags", "tag", "frontmatter", "yaml", "content", "contents", "list", "item", "items", "metadata", "meta"
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

def tokenize(text):
    text = text.lower()
    text = re.sub(r'[^a-z]', ' ', text)
    words = text.split()
    return [w for w in words if len(w) > 3 and w not in STOPWORDS]

def main():
    paths = list(ROOT.rglob("*.md"))
    paths = [p for p in paths if not any(part == ".git" or part == ".trash" or part == "raw sources" for part in p.parts)]
    
    doc_words = {}
    df = Counter()
    
    print(f"Reading {len(paths)} files...")
    
    # Pass 1: compute DF
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
            
        _, body, _ = split_frontmatter(text)
        words = tokenize(body)
        unique_words = set(words)
        for w in unique_words:
            df[w] += 1
        doc_words[path] = words
        
    num_docs = len(doc_words)
    print(f"Computing TF-IDF for {num_docs} documents...")
    
    idf = {w: math.log(num_docs / (1 + count)) for w, count in df.items()}
    
    # Pass 2: compute TF-IDF and update frontmatter
    updated_count = 0
    
    for path, words in doc_words.items():
        if not words:
            continue
            
        tf = Counter(words)
        tfidf = {w: tf[w] * idf[w] for w in tf}
        
        top_words = sorted(tfidf.items(), key=lambda x: x[1], reverse=True)[:5]
        new_tags = [w for w, _ in top_words]
        
        if not new_tags:
            continue
            
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
            meta, body, fm_raw = split_frontmatter(text)
            
            existing_tags = meta.get("tags")
            if existing_tags is None:
                existing_tags = []
            elif isinstance(existing_tags, str):
                existing_tags = [existing_tags]
            elif not isinstance(existing_tags, list):
                existing_tags = list(existing_tags)
                
            original_tags_set = {str(t).lower() for t in existing_tags}
            added = False
            
            for t in new_tags:
                if t not in original_tags_set:
                    existing_tags.append(t)
                    original_tags_set.add(t)
                    added = True
                    
            if added:
                meta["tags"] = existing_tags
                new_fm_raw = yaml.safe_dump(meta, sort_keys=False, allow_unicode=True, default_flow_style=False)
                new_content = f"---\n{new_fm_raw}---\n\n{body.lstrip()}"
                
                path.write_text(new_content, encoding="utf-8")
                updated_count += 1
                
        except Exception as e:
            print(f"Error updating {path}: {e}")
            
    print(f"Added semantic tags to {updated_count} files.")

if __name__ == "__main__":
    main()
