#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable


SKIP_DIR_NAMES = {
    "$RECYCLE.BIN",
    "System Volume Information",
    ".Spotlight-V100",
    ".Trashes",
    ".obsidian",
}

SKIP_FILE_NAMES = {
    "Thumbs.db",
    ".DS_Store",
    "desktop.ini",
}

CONVERT_EXTS = {
    ".doc",
    ".docx",
    ".ppt",
    ".pptx",
    ".xls",
    ".xlsx",
    ".txt",
    ".md",
    ".rtf",
    ".html",
    ".htm",
    ".epub",
    ".csv",
    ".json",
    ".xml",
}

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
ISBN13_RE = re.compile(r"\b97[89][0-9][- 0-9]{8,16}[0-9Xx]\b")
YEAR_RE = re.compile(r"\b(19|20)\d{2}\b")


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=UTC).isoformat()


def _sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def _sniff_header(path: Path, n: int = 8) -> bytes:
    try:
        with path.open("rb") as f:
            return f.read(n)
    except Exception:
        return b""


def _is_probably_pdf(path: Path) -> bool:
    if path.suffix.lower() == ".pdf":
        return True
    return _sniff_header(path, n=8).startswith(b"%PDF-")


def _run(cmd: list[str], *, timeout_s: int = 120) -> tuple[int, str, str]:
    p = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        errors="replace",
        timeout=timeout_s,
    )
    return p.returncode, p.stdout, p.stderr


def _office_to_text(path: Path) -> str:
    """
    Best-effort office-to-text conversion using common Linux extractors.
    This is a fallback when MarkItDown is unavailable.
    """
    ext = path.suffix.lower()
    if ext == ".docx":
        code, out, err = _run(["docx2txt", str(path), "-"], timeout_s=180)
        if code != 0:
            raise RuntimeError(err.strip() or f"docx2txt failed (code {code})")
        return out
    if ext == ".doc":
        code, out, err = _run(["catdoc", str(path)], timeout_s=120)
        if code != 0:
            raise RuntimeError(err.strip() or f"catdoc failed (code {code})")
        return out
    if ext == ".ppt":
        code, out, err = _run(["catppt", str(path)], timeout_s=180)
        if code != 0:
            raise RuntimeError(err.strip() or f"catppt failed (code {code})")
        return out
    if ext == ".xls":
        code, out, err = _run(["xls2csv", str(path)], timeout_s=180)
        if code != 0:
            raise RuntimeError(err.strip() or f"xls2csv failed (code {code})")
        return out
    raise RuntimeError(f"Unsupported office extractor for extension: {ext}")


def _pdfinfo(path: Path) -> dict[str, str]:
    code, out, _ = _run(["pdfinfo", str(path)], timeout_s=60)
    if code != 0:
        return {}
    meta: dict[str, str] = {}
    for line in out.splitlines():
        if ":" not in line:
            continue
        k, v = line.split(":", 1)
        meta[k.strip()] = v.strip()
    return meta


def _pdftotext(path: Path, *, timeout_s: int = 180) -> str:
    with tempfile.NamedTemporaryFile(prefix="pdftotext_", suffix=".txt", delete=False) as tf:
        tmp = tf.name
    try:
        code, _, err = _run(["pdftotext", "-q", str(path), tmp], timeout_s=timeout_s)
        if code != 0:
            raise RuntimeError(err.strip() or f"pdftotext failed with code {code}")
        return Path(tmp).read_text(encoding="utf-8", errors="replace")
    finally:
        try:
            Path(tmp).unlink(missing_ok=True)
        except Exception:
            pass


def _write_pdf_markdown(
    *,
    source_path: Path,
    out_md: Path,
    sha256: str,
    rel: Path,
    max_chars: int,
) -> tuple[str, str, str]:
    meta = _pdfinfo(source_path)
    text = ""
    ocr_needed = False
    try:
        text = _pdftotext(source_path)
        if len(text.strip()) < 80:
            ocr_needed = True
    except Exception as e:
        ocr_needed = True
        text = f"[pdftotext error] {e}\n"

    if max_chars > 0 and len(text) > max_chars:
        text = text[:max_chars] + "\n\n[TRUNCATED]\n"

    title = meta.get("Title", "").strip() or source_path.name
    lines = [
        "---",
        "type: raw",
        "source_kind: pdf",
        f"source_path: {str(source_path)}",
        f"source_rel: {rel.as_posix()}",
        f"sha256: {sha256}",
        f"ocr_needed: {str(ocr_needed).lower()}",
        "pdfinfo:",
    ]
    for k in sorted(meta.keys()):
        v = meta[k].replace("\n", " ").strip()
        if not v:
            continue
        lines.append(f"  {k}: {json.dumps(v, ensure_ascii=False)}")
    lines += [
        "---",
        "",
        f"# {title}",
        "",
        "## PDF Metadata",
        "",
    ]
    if meta:
        for k in sorted(meta.keys()):
            v = meta[k].strip()
            if v:
                lines.append(f"- **{k}:** {v}")
    else:
        lines.append("- (pdfinfo unavailable or empty)")
    lines += [
        "",
        "## Extracted Text",
        "",
    ]
    if ocr_needed:
        lines.append("> OCR likely needed (text extraction was empty/failed).")
        lines.append("")
    lines.append(text.strip())
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")

    md_text = out_md.read_text(encoding="utf-8", errors="replace")
    title_guess = _guess_title(md_text, fallback=source_path.name)
    sig = _extract_signals(md_text, filename=source_path.name)
    doi = ";".join(sig["doi"])
    isbn = ";".join(sig["isbn"])
    return title_guess, doi, isbn


def _read_text_lossy(path: Path) -> str:
    data = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8"):
        try:
            return data.decode(enc)
        except Exception:
            pass
    return data.decode("utf-8", errors="replace")


def _write_plaintext_markdown(
    *,
    source_path: Path,
    out_md: Path,
    sha256: str,
    rel: Path,
) -> tuple[str, str, str]:
    text = _read_text_lossy(source_path)
    title = source_path.stem
    lines = [
        "---",
        "type: raw",
        "source_kind: text",
        f"source_path: {str(source_path)}",
        f"source_rel: {rel.as_posix()}",
        f"sha256: {sha256}",
        "---",
        "",
        f"# {title}",
        "",
        "## Extracted Text",
        "",
        text.rstrip(),
    ]
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    md_text = out_md.read_text(encoding="utf-8", errors="replace")
    title_guess = _guess_title(md_text, fallback=source_path.name)
    sig = _extract_signals(md_text, filename=source_path.name)
    doi = ";".join(sig["doi"])
    isbn = ";".join(sig["isbn"])
    return title_guess, doi, isbn


def _write_office_plaintext_markdown(
    *,
    source_path: Path,
    out_md: Path,
    sha256: str,
    rel: Path,
    source_kind: str,
) -> tuple[str, str, str]:
    text = _office_to_text(source_path)
    lines = [
        "---",
        "type: raw",
        f"source_kind: {source_kind}",
        f"source_path: {str(source_path)}",
        f"source_rel: {rel.as_posix()}",
        f"sha256: {sha256}",
        "---",
        "",
        f"# {source_path.name}",
        "",
        "## Extracted Text",
        "",
        text.rstrip(),
    ]
    out_md.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")
    md_text = out_md.read_text(encoding="utf-8", errors="replace")
    title_guess = _guess_title(md_text, fallback=source_path.name)
    sig = _extract_signals(md_text, filename=source_path.name)
    doi = ";".join(sig["doi"])
    isbn = ";".join(sig["isbn"])
    return title_guess, doi, isbn


def _iter_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [
            d
            for d in dirnames
            if d not in SKIP_DIR_NAMES and not d.startswith("FOUND.")
        ]
        for name in filenames:
            if name in SKIP_FILE_NAMES:
                continue
            yield Path(dirpath) / name


def _safe_rel(root: Path, p: Path) -> Path:
    try:
        return p.relative_to(root)
    except Exception:
        return Path(str(p).lstrip("/").replace(":", ""))


def _guess_title(md: str, fallback: str) -> str:
    for line in md.splitlines():
        line = line.strip()
        if not line:
            continue
        if line.startswith("# "):
            return line[2:].strip()[:240]
        # Some conversions start with a title-like line but no heading.
        if len(line) >= 8 and len(line) <= 180 and not line.startswith("```"):
            return line[:240]
        break
    return fallback[:240]


def _extract_signals(md: str, filename: str) -> dict[str, Any]:
    dois = sorted(set(m.group(0) for m in DOI_RE.finditer(md)))[:10]
    isbns = sorted(set(m.group(0) for m in ISBN13_RE.finditer(md)))[:10]
    years = sorted(set(YEAR_RE.findall(filename) or []))
    # YEAR_RE.findall returns tuples because of capturing group; rebuild properly.
    years = sorted(set(m.group(0) for m in YEAR_RE.finditer(filename)))[:10]
    return {
        "doi": dois,
        "isbn": isbns,
        "years_in_filename": years,
    }


@dataclass
class FileRow:
    rel_path: str
    abs_path: str
    ext: str
    size_bytes: int
    mtime_utc: str
    ctime_utc: str
    sha256: str
    converted_md: str
    title_guess: str
    doi: str
    isbn: str


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(
        description="Recursively scan D:\\LIBRARY and ingest raw conversions into EMERAULD."
    )
    parser.add_argument("--input", required=True, help="Root directory to scan (e.g. /mnt/d/LIBRARY).")
    parser.add_argument("--out", required=True, help="Output root (inside EMERAULD raw sources).")
    parser.add_argument("--max-hash-mb", type=int, default=200, help="Max file size (MB) to hash.")
    parser.add_argument("--max-convert-mb", type=int, default=200, help="Max file size (MB) to convert.")
    parser.add_argument(
        "--skip-convert-prefix",
        action="append",
        default=["Review/Unreadable"],
        help="Relative path prefix (from input root) to skip conversions (still inventoried). Repeatable.",
    )
    parser.add_argument("--progress-every", type=int, default=25, help="Log progress every N files.")
    parser.add_argument(
        "--pdf-text-max-chars",
        type=int,
        default=120_000,
        help="Max extracted PDF text chars to store per file (0 = no limit).",
    )
    parser.add_argument("--continue-on-error", action="store_true", help="Continue after failures.")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing converted .md outputs.")
    args = parser.parse_args(argv)

    input_root = Path(args.input).expanduser().resolve()
    out_root = Path(args.out).expanduser().resolve()

    if not input_root.exists() or not input_root.is_dir():
        raise SystemExit(f"Input root not found or not a directory: {input_root}")

    out_inventory = out_root / "inventory"
    out_converted = out_root / "converted"
    out_notes = out_root / "notes"
    out_henry = out_root / "henry"

    for d in (out_inventory, out_converted, out_notes, out_henry):
        d.mkdir(parents=True, exist_ok=True)

    # Lazy import so the script can still inventory even if MarkItDown isn't installed.
    md_converter = None
    try:
        from markitdown import MarkItDown  # type: ignore

        md_converter = MarkItDown(enable_plugins=True)
    except Exception as e:
        print(f"[library_d_ingest] MarkItDown unavailable; conversions disabled: {e}", file=sys.stderr)

    rows: list[FileRow] = []
    failures: list[dict[str, Any]] = []
    processed = 0

    for p in _iter_files(input_root):
        try:
            if not p.is_file():
                continue
            st = p.stat()
            rel = _safe_rel(input_root, p)
            ext = p.suffix.lower()
            rel_posix = rel.as_posix()
            processed += 1
            if args.progress_every > 0 and processed % args.progress_every == 0:
                print(f"[library_d_ingest] Progress: {processed} files…", file=sys.stderr)

            sha = ""
            if st.st_size <= args.max_hash_mb * 1024 * 1024:
                sha = _sha256(p)

            converted_md_rel = ""
            title_guess = ""
            doi = ""
            isbn = ""

            should_convert = (
                st.st_size <= args.max_convert_mb * 1024 * 1024
                and not any(
                    rel_posix == prefix or rel_posix.startswith(prefix.rstrip("/") + "/")
                    for prefix in (args.skip_convert_prefix or [])
                )
            )

            is_pdf = _is_probably_pdf(p)
            if should_convert and is_pdf:
                out_md = (out_converted / rel.parent) / (rel.name + ".md")
                out_md.parent.mkdir(parents=True, exist_ok=True)
                if out_md.exists() and not args.overwrite:
                    converted_md_rel = str(out_md.relative_to(out_root))
                    md_text = out_md.read_text(encoding="utf-8", errors="replace")
                    title_guess = _guess_title(md_text, fallback=p.name)
                    sig = _extract_signals(md_text, filename=p.name)
                    doi = ";".join(sig["doi"])
                    isbn = ";".join(sig["isbn"])
                else:
                    title_guess, doi, isbn = _write_pdf_markdown(
                        source_path=p,
                        out_md=out_md,
                        sha256=sha,
                        rel=rel,
                        max_chars=args.pdf_text_max_chars,
                    )
                    converted_md_rel = str(out_md.relative_to(out_root))

            plaintext_exts = {".txt", ".md", ".csv", ".json", ".xml"}
            if should_convert and (not is_pdf) and (ext in plaintext_exts):
                out_md = (out_converted / rel.parent) / (rel.name + ".md")
                out_md.parent.mkdir(parents=True, exist_ok=True)
                if out_md.exists() and not args.overwrite:
                    converted_md_rel = str(out_md.relative_to(out_root))
                    md_text = out_md.read_text(encoding="utf-8", errors="replace")
                    title_guess = _guess_title(md_text, fallback=p.name)
                    sig = _extract_signals(md_text, filename=p.name)
                    doi = ";".join(sig["doi"])
                    isbn = ";".join(sig["isbn"])
                else:
                    title_guess, doi, isbn = _write_plaintext_markdown(
                        source_path=p,
                        out_md=out_md,
                        sha256=sha,
                        rel=rel,
                    )
                    converted_md_rel = str(out_md.relative_to(out_root))

            # Office fallback conversions (when MarkItDown isn't available).
            if (
                should_convert
                and (not is_pdf)
                and (converted_md_rel == "")
                and (md_converter is None)
                and (ext in {".docx", ".doc", ".ppt", ".xls"})
            ):
                out_md = (out_converted / rel.parent) / (rel.name + ".md")
                out_md.parent.mkdir(parents=True, exist_ok=True)
                if out_md.exists() and not args.overwrite:
                    converted_md_rel = str(out_md.relative_to(out_root))
                    md_text = out_md.read_text(encoding="utf-8", errors="replace")
                    title_guess = _guess_title(md_text, fallback=p.name)
                    sig = _extract_signals(md_text, filename=p.name)
                    doi = ";".join(sig["doi"])
                    isbn = ";".join(sig["isbn"])
                else:
                    kind = {
                        ".docx": "docx_text",
                        ".doc": "doc_text",
                        ".ppt": "ppt_text",
                        ".xls": "xls_csv",
                    }[ext]
                    title_guess, doi, isbn = _write_office_plaintext_markdown(
                        source_path=p,
                        out_md=out_md,
                        sha256=sha,
                        rel=rel,
                        source_kind=kind,
                    )
                    converted_md_rel = str(out_md.relative_to(out_root))

            if (
                should_convert
                and (not is_pdf)
                and (converted_md_rel == "")
                and (md_converter is not None)
                and (ext in CONVERT_EXTS)
            ):
                out_md = (out_converted / rel.parent) / (rel.name + ".md")
                out_md.parent.mkdir(parents=True, exist_ok=True)
                if out_md.exists() and not args.overwrite:
                    converted_md_rel = str(out_md.relative_to(out_root))
                    # Best-effort signals from existing output.
                    md_text = out_md.read_text(encoding="utf-8", errors="replace")
                    title_guess = _guess_title(md_text, fallback=p.name)
                    sig = _extract_signals(md_text, filename=p.name)
                    doi = ";".join(sig["doi"])
                    isbn = ";".join(sig["isbn"])
                else:
                    result = md_converter.convert_local(str(p))
                    md_text = (result.markdown or "").strip()
                    out_md.write_text(md_text, encoding="utf-8")
                    converted_md_rel = str(out_md.relative_to(out_root))
                    title_guess = _guess_title(md_text, fallback=p.name)
                    sig = _extract_signals(md_text, filename=p.name)
                    doi = ";".join(sig["doi"])
                    isbn = ";".join(sig["isbn"])

            rows.append(
                FileRow(
                    rel_path=str(rel),
                    abs_path=str(p),
                    ext=ext,
                    size_bytes=int(st.st_size),
                    mtime_utc=_iso(st.st_mtime),
                    ctime_utc=_iso(st.st_ctime),
                    sha256=sha,
                    converted_md=converted_md_rel,
                    title_guess=title_guess,
                    doi=doi,
                    isbn=isbn,
                )
            )
        except Exception as e:
            failures.append({"path": str(p), "error": str(e)})
            print(f"[library_d_ingest] Failed: {p}: {e}", file=sys.stderr)
            if not args.continue_on_error:
                break

    # Write inventory
    inv_csv = out_inventory / "files.csv"
    with inv_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "rel_path",
                "abs_path",
                "ext",
                "size_bytes",
                "mtime_utc",
                "ctime_utc",
                "sha256",
                "converted_md",
                "title_guess",
                "doi",
                "isbn",
            ]
        )
        for r in rows:
            w.writerow(
                [
                    r.rel_path,
                    r.abs_path,
                    r.ext,
                    r.size_bytes,
                    r.mtime_utc,
                    r.ctime_utc,
                    r.sha256,
                    r.converted_md,
                    r.title_guess,
                    r.doi,
                    r.isbn,
                ]
            )

    inv_jsonl = out_inventory / "files.jsonl"
    with inv_jsonl.open("w", encoding="utf-8") as f:
        for r in rows:
            f.write(
                json.dumps(
                    {
                        "rel_path": r.rel_path,
                        "abs_path": r.abs_path,
                        "ext": r.ext,
                        "size_bytes": r.size_bytes,
                        "mtime_utc": r.mtime_utc,
                        "ctime_utc": r.ctime_utc,
                        "sha256": r.sha256,
                        "converted_md": r.converted_md,
                        "title_guess": r.title_guess,
                        "doi": r.doi.split(";") if r.doi else [],
                        "isbn": r.isbn.split(";") if r.isbn else [],
                    },
                    ensure_ascii=False,
                )
                + "\n"
            )

    # Duplicates by sha256 (within scanned tree)
    dup_rows: list[dict[str, Any]] = []
    by_sha: dict[str, list[FileRow]] = {}
    for r in rows:
        if not r.sha256:
            continue
        by_sha.setdefault(r.sha256, []).append(r)
    for sha, group in sorted(by_sha.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        if len(group) < 2:
            continue
        for r in group:
            dup_rows.append({"sha256": sha, "rel_path": r.rel_path, "size_bytes": r.size_bytes})

    dup_csv = out_inventory / "duplicates_by_sha256.csv"
    with dup_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sha256", "rel_path", "size_bytes"])
        for d in dup_rows:
            w.writerow([d["sha256"], d["rel_path"], d["size_bytes"]])

    # Henry candidates: anything with DOI/ISBN, plus all PDFs/EPUBs/DOCX that converted.
    henry_csv = out_henry / "MASTER_REFERENCE_CANDIDATES.csv"
    with henry_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rel_path", "ext", "title_guess", "doi", "isbn", "converted_md"])
        for r in rows:
            if not r.converted_md:
                continue
            if r.ext in {".pdf", ".epub", ".docx", ".doc"} or r.doi or r.isbn:
                w.writerow([r.rel_path, r.ext, r.title_guess, r.doi, r.isbn, r.converted_md])

    # Notes: one lightweight per top-level folder
    top_groups: dict[str, list[FileRow]] = {}
    for r in rows:
        parts = Path(r.rel_path).parts
        top = parts[0] if parts else "_root"
        top_groups.setdefault(top, []).append(r)

    for top, group in sorted(top_groups.items(), key=lambda kv: kv[0].lower()):
        total = len(group)
        converted = sum(1 for r in group if r.converted_md)
        size = sum(r.size_bytes for r in group)
        note = out_notes / f"{top}.md"
        lines = [
            f"# D:\\\\LIBRARY — {top}",
            "",
            "Raw capture note (auto-generated).",
            "",
            f"- Total files: {total}",
            f"- Total bytes: {size}",
            f"- Converted to markdown: {converted}",
            "",
            "## Notable converted items",
        ]
        listed = 0
        for r in group:
            if not r.converted_md:
                continue
            if listed >= 40:
                break
            lines.append(f"- `{r.converted_md}` — {r.title_guess or Path(r.rel_path).name}")
            listed += 1
        if listed == 0:
            lines.append("- (none)")
        note.write_text("\n".join(lines) + "\n", encoding="utf-8")

    failures_path = out_inventory / "failures.json"
    failures_path.write_text(json.dumps(failures, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")

    readme = out_root / "00_README.md"
    readme.write_text(
        "\n".join(
            [
                "# D:\\LIBRARY — Raw Intake (Trismégiste)",
                "",
                f"- Input scanned: `{input_root}`",
                f"- Generated: `{out_root}`",
                "",
                "## Outputs",
                f"- Inventory (CSV): `{inv_csv.relative_to(out_root)}`",
                f"- Inventory (JSONL): `{inv_jsonl.relative_to(out_root)}`",
                f"- Duplicates (hash): `{dup_csv.relative_to(out_root)}`",
                f"- Henry candidates: `{henry_csv.relative_to(out_root)}`",
                f"- Converted markdown: `{out_converted.relative_to(out_root)}/`",
                f"- Folder notes: `{out_notes.relative_to(out_root)}/`",
                "",
                "## Notes",
                "- This is capture-first: conversions are stored as raw artifacts for later synthesis into `wiki/`.",
                "- System folders/files are skipped; conversions are limited by file size thresholds.",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(str(readme))
    print(str(inv_csv))
    print(str(henry_csv))
    if failures:
        print(f"[library_d_ingest] Failures: {len(failures)} (see {failures_path})", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
