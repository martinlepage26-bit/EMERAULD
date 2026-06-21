AGATHA, DO NOT RUN

# martin_voice_optimizer.py
from __future__ import annotations

import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Dict, List, Tuple, Optional, Any

# Optional deps:
#   pip install pdfplumber python-docx
try:
    import pdfplumber  # type: ignore
except Exception:
    pdfplumber = None

try:
    import docx  # type: ignore
except Exception:
    docx = None


# ----------------------------
# Phrase banks (tune over time)
# ----------------------------
CONNECTORS_FR = [
    "cependant", "toutefois", "ainsi", "or", "en effet", "dès lors", "plus précisément",
    "de plus", "par ailleurs", "autrement dit", "en d'autres termes",
    "d'une part", "d'autre part", "notamment", "voire", "pourtant"
]

CONNECTORS_EN = [
    "however", "thus", "therefore", "moreover", "furthermore", "in other words", "that is",
    "for instance", "for example", "yet", "still", "nevertheless", "in fact",
    "more specifically", "on the one hand", "on the other hand"
]

HEDGES_FR = [
    "peut", "pourrait", "sembler", "semble", "en quelque sorte", "probablement",
    "sans doute", "il est possible", "il se peut"
]

HEDGES_EN = [
    "may", "might", "seems", "seem", "arguably", "perhaps", "possibly", "in a sense",
    "sort of", "kind of"
]

REF_HEADINGS = [
    "references", "bibliography", "works cited",
    "références", "bibliographie", "sources"
]


# ----------------------------
# Basic NLP utilities
# ----------------------------
WORD_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ]+(?:'[A-Za-zÀ-ÖØ-öø-ÿ]+)?", re.UNICODE)

def words(text: str) -> List[str]:
    return [w.lower() for w in WORD_RE.findall(text or "")]

def split_sentences(text: str) -> List[str]:
    # Good-enough sentence split for profiling
    text = (text or "").strip()
    if not text:
        return []
    parts = re.split(r"(?<=[\.\?\!])\s+(?=[A-ZÉÈÀÂÎÔÛÄËÏÖÜÇ0-9])", text)
    return [p.strip() for p in parts if p.strip()]

def split_paragraphs(text: str) -> List[str]:
    paras = [p.strip() for p in re.split(r"\n{2,}", text or "") if p.strip()]
    return paras

def count_phrases(text: str, phrases: List[str]) -> Dict[str, int]:
    t = (text or "").lower()
    return {ph: t.count(ph) for ph in phrases}

def pct(n: float, d: float) -> float:
    return 0.0 if d == 0 else (n / d) * 100.0


# ----------------------------
# File loading
# ----------------------------
def load_text(path: str | Path, max_pages: Optional[int] = None) -> str:
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(str(p))

    suffix = p.suffix.lower()

    if suffix == ".txt":
        return p.read_text(encoding="utf-8", errors="ignore")

    if suffix == ".docx":
        if docx is None:
            raise RuntimeError("python-docx not installed. Run: pip install python-docx")
        d = docx.Document(str(p))
        return "\n".join(par.text for par in d.paragraphs)

    if suffix == ".pdf":
        if pdfplumber is None:
            raise RuntimeError("pdfplumber not installed. Run: pip install pdfplumber")
        chunks: List[str] = []
        with pdfplumber.open(str(p)) as pdf:
            pages = pdf.pages if max_pages is None else pdf.pages[:max_pages]
            for page in pages:
                chunks.append(page.extract_text() or "")
        return "\n".join(chunks)

    raise ValueError(f"Unsupported file type: {suffix}")


# ----------------------------
# Citation detection
# ----------------------------
CITE_PAREN_YEAR_RE = re.compile(r"\(([^)]{0,100}?\b(19|20)\d{2}[a-z]?)\)")
CITE_AUTHOR_YEAR_RE = re.compile(r"\b[A-Z][A-Za-zÀ-ÖØ-öø-ÿ\-]+(?:\s+[A-Z][A-Za-zÀ-ÖØ-öø-ÿ\-]+)*\s*\(\s*(19|20)\d{2}[a-z]?\s*\)")
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.I)

def citation_stats(text: str) -> Dict[str, Any]:
    paren_year = CITE_PAREN_YEAR_RE.findall(text or "")
    author_year = CITE_AUTHOR_YEAR_RE.findall(text or "")
    dois = DOI_RE.findall(text or "")
    return {
        "paren_year_count": len(paren_year),
        "author_year_count": len(author_year),
        "doi_count": len(dois),
        "unique_dois": sorted(set(dois))[:50],  # cap for UI sanity
    }


def extract_references_section(text: str) -> Dict[str, Any]:
    """
    Heuristic: finds a heading like References / Bibliographie and returns everything after it.
    """
    t = text or ""
    lower = t.lower()

    hits: List[Tuple[int, str]] = []
    for h in REF_HEADINGS:
        idx = lower.find("\n" + h)
        if idx == -1:
            idx = lower.find(h + "\n")
        if idx != -1:
            hits.append((idx, h))

    if not hits:
        return {"found": False, "heading": None, "content": ""}

    hits.sort(key=lambda x: x[0])
    start_idx, heading = hits[0]
    content = t[start_idx:].strip()
    return {"found": True, "heading": heading, "content": content}


# ----------------------------
# Profiling + operator flags
# ----------------------------
@dataclass
class ParagraphFlag:
    index: int
    operator: str
    reason: str
    snippet: str

def abstraction_index(paragraph: str) -> float:
    """
    Simple heuristic: ratio of long nouns-ish words to total words.
    Not perfect, but stable enough for your UI triggers.
    """
    ws = words(paragraph)
    if not ws:
        return 0.0
    longish = [w for w in ws if len(w) >= 9]
    return len(longish) / len(ws)

def concrete_anchor_score(paragraph: str) -> float:
    """
    Cheap anchor proxy: presence of digits, proper nouns, named places, or quoted material.
    """
    score = 0.0
    if re.search(r"\b\d{2,}\b", paragraph):
        score += 1.0
    if re.search(r"“|”|\"|«|»", paragraph):
        score += 1.0
    if re.search(r"\b(Montréal|Montreal|Québec|Canada|UQAM)\b", paragraph):
        score += 1.0
    if re.search(r"\b[Ii]nterview\b|\bobservation\b|\bterrain\b|\bfieldwork\b", paragraph):
        score += 1.0
    return score

def profile_text(text: str) -> Dict[str, Any]:
    sents = split_sentences(text)
    paras = split_paragraphs(text)

    sent_lens = [len(words(s)) for s in sents if s.strip()]
    wcount = len(words(text))

    conn_fr = count_phrases(text, CONNECTORS_FR)
    conn_en = count_phrases(text, CONNECTORS_EN)
    hedge_fr = count_phrases(text, HEDGES_FR)
    hedge_en = count_phrases(text, HEDGES_EN)

    cite = citation_stats(text)
    refs = extract_references_section(text)

    # Operator flags
    flags: List[ParagraphFlag] = []
    for i, p in enumerate(paras):
        psents = split_sentences(p)
        abs_idx = abstraction_index(p)
        anchor = concrete_anchor_score(p)

        # CLAIM-EARLY trigger: if paragraph has many sentences and none of first 2 contain strong claim verbs
        claim_verbs = r"\b(je soutiens|j'avance|j'argumente|j'affirme|j'examine|j'analyse|I argue|I suggest|I show|I demonstrate)\b"
        if len(psents) >= 4:
            first_two = " ".join(psents[:2]).lower()
            if not re.search(claim_verbs, first_two):
                flags.append(ParagraphFlag(
                    index=i,
                    operator="CLAIM-EARLY",
                    reason="Claim language appears late in a long paragraph (>=4 sentences).",
                    snippet=p[:240].replace("\n", " ")
                ))

        # ANCHOR-INJECTION trigger
        if abs_idx >= 0.22 and anchor <= 0.0:
            flags.append(ParagraphFlag(
                index=i,
                operator="ANCHOR-INJECTION",
                reason=f"High abstraction index ({abs_idx:.2f}) and low anchor score.",
                snippet=p[:240].replace("\n", " ")
            ))

        # HEDGE-CALIBRATION trigger
        if re.search(r"\b(might|may|perhaps|seems|semble|pourrait|sans doute|il est possible)\b", p.lower()):
            # fire only if hedge cluster
            if len(re.findall(r"\b(might|may|perhaps|seems|semble|pourrait|sans doute|il est possible)\b", p.lower())) >= 3:
                flags.append(ParagraphFlag(
                    index=i,
                    operator="HEDGE-CALIBRATION",
                    reason="Multiple hedges detected in one paragraph.",
                    snippet=p[:240].replace("\n", " ")
                ))

    profile = {
        "word_count": wcount,
        "sentence_count": len(sents),
        "paragraph_count": len(paras),
        "mean_sentence_len_words": (sum(sent_lens) / len(sent_lens)) if sent_lens else 0.0,
        "p90_sentence_len_words": sorted(sent_lens)[int(0.9 * len(sent_lens))] if sent_lens else 0.0,
        "connectors_fr_total": sum(conn_fr.values()),
        "connectors_en_total": sum(conn_en.values()),
        "hedges_fr_total": sum(hedge_fr.values()),
        "hedges_en_total": sum(hedge_en.values()),
        "citation": cite,
        "references_section": refs,
        "operator_flags": [asdict(f) for f in flags],
    }
    return profile


def profile_file(path: str | Path, max_pages: Optional[int] = None) -> Dict[str, Any]:
    text = load_text(path, max_pages=max_pages)
    prof = profile_text(text)
    prof["file"] = str(path)
    return prof


def profile_corpus(folder: str | Path, out_json: Optional[str | Path] = None) -> Dict[str, Any]:
    folder = Path(folder)
    files = [p for p in folder.rglob("*") if p.suffix.lower() in {".pdf", ".docx", ".txt"}]
    results = []
    for f in files:
        try:
            results.append(profile_file(f, max_pages=30))  # cap to keep speed sane
        except Exception as e:
            results.append({"file": str(f), "error": str(e)})

    corpus = {
        "folder": str(folder),
        "n_files": len(files),
        "results": results
    }

    if out_json:
        Path(out_json).write_text(json.dumps(corpus, ensure_ascii=False, indent=2), encoding="utf-8")

    return corpus


if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser(description="Martin Voice Profiler + Operator Flagging")
    ap.add_argument("path", help="A file (pdf/docx/txt) or a folder to profile recursively.")
    ap.add_argument("--out", help="Write JSON output to this path.")
    args = ap.parse_args()

    p = Path(args.path)
    if p.is_dir():
        corpus = profile_corpus(p, out_json=args.out)
        print(json.dumps({"n_files": corpus["n_files"]}, indent=2))
    else:
        prof = profile_file(p, max_pages=40)
        if args.out:
            Path(args.out).write_text(json.dumps(prof, ensure_ascii=False, indent=2), encoding="utf-8")
        print(json.dumps(prof, ensure_ascii=False, indent=2))
