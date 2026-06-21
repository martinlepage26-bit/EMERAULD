from __future__ import annotations

import re
import json
import time
from dataclasses import dataclass
from typing import Optional, List, Dict, Tuple
import requests

CROSSREF = "https://api.crossref.org/works"
OPENALEX = "https://api.openalex.org/works"

# ---------- helpers ----------

def strip_leading_footnote_number(line: str) -> str:
    # removes leading "1 ", "[1] ", "(1) ", "1. " etc, but NOT years like "2018  “Title...”"
    s = line.strip()
    if re.match(r"^\d{4}\b", s):
        return s  # keep year-leading entries
    return re.sub(r"^\s*(\[\d+\]|\(\d+\)|\d+)\s*[\.\)]?\s*", "", s).strip()

def looks_like_reference(line: str) -> bool:
    # simple filter: has a year somewhere, or has italic-like title punctuation, or has publisher-ish separators
    return bool(re.search(r"\b(18|19|20)\d{2}\b", line)) or (":" in line and "," in line) or ("doi" in line.lower())

def normalize_spaces(s: str) -> str:
    return re.sub(r"\s+", " ", s).strip()

def extract_title_guess(line: str) -> Optional[str]:
    """
    Best-effort title extraction:
    - if quotes present, take quoted segment
    - else, take segment after year ) or year. up to next period
    """
    s = line.strip()

    m = re.search(r"[“\"](.+?)[”\"]", s)
    if m:
        return normalize_spaces(m.group(1))

    # patterns like: Author (2010) Title. Place: Publisher.
    m = re.search(r"\b(18|19|20)\d{2}\b[)\.]?\s*(.+)", s)
    if m:
        tail = m.group(2)
        # stop at first ". " that looks like end of title
        parts = re.split(r"\.\s+", tail, maxsplit=1)
        if parts and len(parts[0]) >= 6:
            return normalize_spaces(parts[0].rstrip("."))
    return None

def has_author_year(line: str) -> bool:
    return bool(re.match(r"^[A-ZÀ-ÖØ-Ý][^,]{1,60},\s", line)) and bool(re.search(r"\b(18|19|20)\d{2}\b", line))

# ---------- lookups ----------

@dataclass
class LookupResult:
    author: Optional[str] = None
    year: Optional[str] = None
    title: Optional[str] = None
    container: Optional[str] = None
    publisher: Optional[str] = None
    doi: Optional[str] = None

def crossref_lookup_by_title(title: str) -> Optional[LookupResult]:
    params = {"query.title": title, "rows": 1}
    r = requests.get(CROSSREF, params=params, timeout=20)
    r.raise_for_status()
    items = r.json().get("message", {}).get("items", [])
    if not items:
        return None
    it = items[0]
    year = None
    for key in ("published-print", "published-online", "created"):
        dp = it.get(key, {}).get("date-parts")
        if dp and dp[0]:
            year = str(dp[0][0])
            break
    authors = it.get("author") or []
    author = None
    if authors:
        a0 = authors[0]
        family = a0.get("family")
        given = a0.get("given")
        if family and given:
            author = f"{family}, {given}"
        elif family:
            author = family
    title_out = (it.get("title") or [None])[0]
    container = (it.get("container-title") or [None])[0]
    publisher = it.get("publisher")
    doi = it.get("DOI")
    return LookupResult(author=author, year=year, title=title_out, container=container, publisher=publisher, doi=doi)

def openalex_lookup_by_title(title: str) -> Optional[LookupResult]:
    # OpenAlex search by title
    params = {"search": title, "per-page": 1}
    r = requests.get(OPENALEX, params=params, timeout=20)
    r.raise_for_status()
    results = r.json().get("results", [])
    if not results:
        return None
    it = results[0]
    year = it.get("publication_year")
    authorships = it.get("authorships") or []
    author = None
    if authorships:
        name = authorships[0].get("author", {}).get("display_name")
        if name:
            # convert "First Last" to "Last, First" best-effort
            parts = name.split()
            if len(parts) >= 2:
                author = f"{parts[-1]}, {' '.join(parts[:-1])}"
            else:
                author = name
    title_out = it.get("display_name")
    doi = None
    ids = it.get("ids") or {}
    if "doi" in ids:
        doi = ids["doi"].replace("https://doi.org/", "")
    host = (it.get("host_venue") or {}).get("display_name")
    return LookupResult(author=author, year=str(year) if year else None, title=title_out, container=host, doi=doi)

def enrich_missing(line: str) -> Tuple[str, Optional[LookupResult]]:
    if has_author_year(line):
        return line, None

    title = extract_title_guess(line)
    if not title:
        return line, None

    # try Crossref then OpenAlex
    res = None
    try:
        res = crossref_lookup_by_title(title)
        time.sleep(0.2)
    except Exception:
        res = None
    if not res:
        try:
            res = openalex_lookup_by_title(title)
            time.sleep(0.2)
        except Exception:
            res = None

    if not res or not res.author or not res.year or not res.title:
        return line, res

    # Minimal Harvard-ish reconstruction (best-effort)
    rebuilt = f"{res.author} ({res.year}) {res.title}."
    if res.publisher:
        rebuilt += f" {res.publisher}."
    if res.container:
        rebuilt += f" {res.container}."
    if res.doi:
        rebuilt += f" doi: {res.doi}."
    return normalize_spaces(rebuilt), res

# ---------- grouping + sort ----------

def author_key(line: str) -> str:
    m = re.match(r"^([^,(]{2,80}),", line)
    if m:
        return normalize_spaces(m.group(1)).lower()
    # if no author, push to end
    return "~~~"

def group_and_sort(lines: List[str]) -> List[str]:
    # sort by author then year then title-ish
    cleaned = [normalize_spaces(l) for l in lines if l.strip()]
    cleaned.sort(key=lambda x: (author_key(x), x.lower()))

    output: List[str] = []
    last_author = None
    for l in cleaned:
        ak = author_key(l)
        # if missing author, just print as-is
        if ak == "~~~":
            output.append(l)
            continue

        # print with underline for same author blocks
        author_print = re.match(r"^([^,]{2,80}),", l).group(1)
        if last_author and ak == last_author:
            output.append(re.sub(r"^[^,]{2,80},", "__________,", l, count=1))
        else:
            output.append(l)
            last_author = ak
    return output

# ---------- main ----------

def main(in_path: str, out_path: str = "master_sorted.txt", audit_path: str = "missing_lookup_audit.json"):
    raw = open(in_path, "r", encoding="utf-8").read().splitlines()
    # strip footnote numbering + keep only reference-like lines
    base = []
    for line in raw:
        line = strip_leading_footnote_number(line)
        if looks_like_reference(line):
            base.append(line)

    enriched = []
    audit: List[Dict] = []
    for line in base:
        fixed, meta = enrich_missing(line)
        enriched.append(fixed)
        if meta and (not has_author_year(fixed)):
            audit.append({"original": line, "title_guess": extract_title_guess(line), "lookup": meta.__dict__})

    final_lines = group_and_sort(list(dict.fromkeys(enriched)))  # dedupe while preserving
    open(out_path, "w", encoding="utf-8").write("\n".join(final_lines) + "\n")
    open(audit_path, "w", encoding="utf-8").write(json.dumps(audit, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python bib_rebuild.py merged_refs_raw.txt")
        raise SystemExit(2)
    main(sys.argv[1])
