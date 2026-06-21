#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any, Iterable


SKIP_DIR_NAMES = {"$RECYCLE.BIN", "System Volume Information", ".Spotlight-V100", ".Trashes", ".obsidian"}
SKIP_FILE_NAMES = {"Thumbs.db", ".DS_Store", "desktop.ini"}

DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Z0-9]+\b", re.IGNORECASE)
ISBN13_RE = re.compile(r"\b97[89][0-9][- 0-9]{8,16}[0-9Xx]\b")


def _iso(ts: float) -> str:
    return datetime.fromtimestamp(ts, tz=UTC).isoformat()


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


def _run(cmd: list[str], *, timeout_s: int) -> tuple[int, str, str]:
    p = subprocess.run(
        cmd,
        capture_output=True,
        text=True,
        errors="replace",
        timeout=timeout_s,
    )
    return p.returncode, p.stdout, p.stderr


def _office_to_text(path: Path) -> str:
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


def _pdf_pages(meta: dict[str, str]) -> int:
    v = (meta.get("Pages") or "").strip()
    try:
        return int(v)
    except Exception:
        return 0


def _pdftotext(
    pdf: Path,
    *,
    page_first: int | None = None,
    page_last: int | None = None,
    timeout_s: int = 120,
) -> str:
    cmd = ["pdftotext", "-q"]
    if page_first is not None and page_last is not None:
        cmd += ["-f", str(page_first), "-l", str(page_last)]
    cmd += [str(pdf), "-"]
    code, out, err = _run(cmd, timeout_s=timeout_s)
    if code != 0:
        raise RuntimeError(err.strip() or f"pdftotext failed (code {code})")
    return out


def _select_pages(
    *,
    total: int,
    full_threshold: int,
    first_pages: int,
    last_pages: int,
) -> list[int]:
    if total <= 0:
        return [1]
    if total <= full_threshold:
        return list(range(1, total + 1))
    pages = set(range(1, min(first_pages, total) + 1))
    for p in range(max(1, total - last_pages + 1), total + 1):
        pages.add(p)
    return sorted(pages)


def _path_hash(rel_posix: str) -> str:
    return hashlib.sha1(rel_posix.encode("utf-8", errors="ignore")).hexdigest()[:12]


def _safe_out_name(name: str, rel_posix: str, suffix: str) -> str:
    # Avoid Windows path length bombs in output directories; keep provenance in frontmatter + status CSV.
    if len(name) <= 160:
        return name + suffix
    stem = name[:120].rstrip()
    return f"{stem}__{_path_hash(rel_posix)}{suffix}"


def _read_text_lossy(path: Path) -> str:
    data = path.read_bytes()
    for enc in ("utf-8-sig", "utf-8"):
        try:
            return data.decode(enc)
        except Exception:
            pass
    return data.decode("utf-8", errors="replace")


def _extract_signals(text: str) -> tuple[list[str], list[str]]:
    dois = sorted(set(m.group(0) for m in DOI_RE.finditer(text)))[:20]
    isbns = sorted(set(m.group(0) for m in ISBN13_RE.finditer(text)))[:20]
    return dois, isbns


def _iter_files(root: Path) -> Iterable[Path]:
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in SKIP_DIR_NAMES and not d.startswith("FOUND.")]
        for name in filenames:
            if name in SKIP_FILE_NAMES:
                continue
            yield Path(dirpath) / name


def _rel(root: Path, p: Path) -> Path:
    try:
        return p.relative_to(root)
    except Exception:
        return Path(str(p).lstrip("/").replace(":", ""))


def _render_pdf_pages(pdf: Path, pages: list[int], tmp: Path, dpi: int) -> list[Path]:
    images: list[Path] = []
    for page in pages:
        out_prefix = tmp / f"p{page:05d}"
        cmd = [
            "pdftoppm",
            "-f",
            str(page),
            "-l",
            str(page),
            "-singlefile",
            "-gray",
            "-png",
            "-r",
            str(dpi),
            str(pdf),
            str(out_prefix),
        ]
        code, _, err = _run(cmd, timeout_s=180)
        if code != 0:
            raise RuntimeError(err.strip() or f"pdftoppm failed (code {code})")
        img = out_prefix.with_suffix(".png")
        if not img.exists():
            # pdftoppm uses `prefix.png` for -singlefile, but be defensive.
            candidates = list(tmp.glob(out_prefix.name + "*.png"))
            if not candidates:
                raise RuntimeError(f"pdftoppm produced no image for page {page}")
            img = candidates[0]
        images.append(img)
    return images


def _node_ocr_images(
    *,
    ocrjs_dir: Path,
    images: list[Path],
    out_txt: Path,
    lang: str,
    cache_dir: Path,
) -> None:
    out_txt.parent.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)
    cmd = [
        "node",
        str(ocrjs_dir / "ocr_images.mjs"),
        "--lang",
        lang,
        "--cache",
        str(cache_dir),
        "--out",
        str(out_txt),
        *[str(p) for p in images],
    ]
    code, _, err = _run(cmd, timeout_s=60 * 30)
    if code != 0:
        raise RuntimeError(err.strip() or f"node ocr_images.mjs failed (code {code})")


@dataclass
class StatusRow:
    rel_path: str
    abs_path: str
    ext: str
    size_bytes: int
    mtime_utc: str
    pages_total: int
    pages_ocrd: str
    converted_md: str
    ocr_text: str
    doi: str
    isbn: str
    status: str
    error: str


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description="OCR pass for D:\\LIBRARY\\Review\\Unreadable into EMERAULD.")
    parser.add_argument("--library-root", default="/mnt/d/LIBRARY", help="Library root (default: /mnt/d/LIBRARY).")
    parser.add_argument(
        "--unreadable-subdir",
        default="Review/Unreadable",
        help="Relative subdir under library root (default: Review/Unreadable).",
    )
    parser.add_argument(
        "--intake-root",
        default="/mnt/c/Users/softinfo/Documents/EMERAULD/raw sources/D_LIBRARY_ingest_2026-04-26/ocr_unreadable",
        help="Output root inside EMERAULD raw sources.",
    )
    parser.add_argument(
        "--ocrjs-dir",
        default="/home/cerebrhoe/.cache/trismegiste_ocrjs",
        help="Directory containing ocr_images.mjs + node_modules.",
    )
    parser.add_argument("--lang", default="eng+fra", help="OCR languages for tesseract.js (default: eng+fra).")
    parser.add_argument("--dpi", type=int, default=120, help="Render DPI for pdftoppm (default: 120).")
    parser.add_argument("--full-pages-threshold", type=int, default=6, help="OCR all pages if <= N pages.")
    parser.add_argument("--first-pages", type=int, default=1, help="OCR first N pages for long PDFs.")
    parser.add_argument("--last-pages", type=int, default=1, help="OCR last N pages for long PDFs.")
    parser.add_argument("--text-first-pages", type=int, default=12, help="For text PDFs, extract first N pages.")
    parser.add_argument("--text-last-pages", type=int, default=2, help="For text PDFs, extract last N pages (if page count known).")
    parser.add_argument("--text-max-chars", type=int, default=180_000, help="Max chars of extracted text to embed in a note (0 = no limit).")
    parser.add_argument(
        "--max-pdf-mb",
        type=int,
        default=40,
        help="For very large PDFs, reduce OCR page coverage (default: 40MB). Use 0 to disable.",
    )
    parser.add_argument("--limit", type=int, default=0, help="Process only N files (0 = no limit).")
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing outputs.")
    args = parser.parse_args(argv)

    library_root = Path(args.library_root).resolve()
    unreadable_root = (library_root / args.unreadable_subdir).resolve()
    intake_root = Path(args.intake_root).resolve()
    ocrjs_dir = Path(args.ocrjs_dir).resolve()

    if not unreadable_root.exists():
        raise SystemExit(f"Unreadable dir not found: {unreadable_root}")
    if not (ocrjs_dir / "ocr_images.mjs").exists():
        raise SystemExit(f"Missing ocr_images.mjs in: {ocrjs_dir}")

    out_converted = intake_root / "converted_ocr"
    out_text = intake_root / "text"
    out_inventory = intake_root / "inventory"
    out_henry = intake_root / "henry"
    out_cache = intake_root / "tess-cache"
    for d in (out_converted, out_text, out_inventory, out_henry, out_cache):
        d.mkdir(parents=True, exist_ok=True)

    # MarkItDown for non-PDF conversions in Unreadable folder.
    md_converter = None
    try:
        from markitdown import MarkItDown  # type: ignore

        md_converter = MarkItDown(enable_plugins=True)
    except Exception:
        md_converter = None

    status_rows: list[StatusRow] = []
    henry_rows: list[dict[str, str]] = []

    files = list(_iter_files(unreadable_root))
    files.sort(key=lambda p: str(p).lower())
    if args.limit and args.limit > 0:
        files = files[: args.limit]

    for idx, p in enumerate(files, start=1):
        rel_under_unreadable = _rel(unreadable_root, p)
        rel_from_library = Path(args.unreadable_subdir) / rel_under_unreadable
        rel_posix = rel_from_library.as_posix()
        ext = p.suffix.lower()

        st = p.stat()
        pages_total = 0
        pages_ocrd: list[int] = []
        status = "ok"
        err = ""
        doi = ""
        isbn = ""
        converted_md_rel = ""
        ocr_text_rel = ""

        try:
            base_dir = out_converted / rel_from_library.parent
            base_dir.mkdir(parents=True, exist_ok=True)
            out_name = _safe_out_name(rel_from_library.name, rel_posix, ".md")
            out_md = base_dir / out_name

            if out_md.exists() and (not args.overwrite):
                converted_md_rel = str(out_md.relative_to(intake_root))
                md_text = out_md.read_text(encoding="utf-8", errors="replace")
                dois, isbns = _extract_signals(md_text)
                doi = ";".join(dois)
                isbn = ";".join(isbns)
            else:
                is_pdf = (ext == ".pdf") or p.name.startswith("%PDF-")
                if is_pdf:
                    meta = _pdfinfo(p)
                    pages_total = _pdf_pages(meta)
                    # Fast path: if this PDF has an extractable text layer, prefer pdftotext (better + faster than OCR).
                    probe_pages = min(5, pages_total) if pages_total else 5
                    pdf_text = ""
                    try:
                        pdf_text = _pdftotext(p, page_first=1, page_last=probe_pages, timeout_s=90)
                    except Exception:
                        pdf_text = ""

                    if len(pdf_text.strip()) >= 200:
                        # Avoid full extraction (slow for books). Capture first N pages plus last N pages for references.
                        text_parts: list[str] = []
                        first_n = args.text_first_pages if args.text_first_pages > 0 else probe_pages
                        last_n = args.text_last_pages if args.text_last_pages > 0 else 0
                        page_last_first = min(first_n, pages_total) if pages_total else first_n
                        try:
                            text_parts.append(_pdftotext(p, page_first=1, page_last=page_last_first, timeout_s=180))
                        except Exception:
                            text_parts.append(pdf_text)
                        if pages_total and last_n and pages_total > page_last_first:
                            start = max(1, pages_total - last_n + 1)
                            try:
                                tail = _pdftotext(p, page_first=start, page_last=pages_total, timeout_s=180)
                                text_parts.append("\n\n[...]\n\n")
                                text_parts.append(tail)
                            except Exception:
                                pass

                        pdf_text = "".join(text_parts).strip()
                        if args.text_max_chars and args.text_max_chars > 0 and len(pdf_text) > args.text_max_chars:
                            pdf_text = pdf_text[: args.text_max_chars] + "\n\n[TRUNCATED]\n"

                        dois, isbns = _extract_signals(pdf_text)
                        doi = ";".join(dois)
                        isbn = ";".join(isbns)
                        title = (meta.get("Title") or "").strip() or p.name

                        yml_lines = [
                            "---",
                            "type: raw",
                            "source_kind: pdf_text",
                            f"source_path: {str(p)}",
                            f"source_rel: {rel_posix}",
                            f"pages_total: {pages_total}",
                            f"text_first_pages: {page_last_first}",
                            f"text_last_pages: {last_n if pages_total and last_n and pages_total > page_last_first else 0}",
                            "pdfinfo:",
                        ]
                        for k in sorted(meta.keys()):
                            v = meta[k].replace("\n", " ").strip()
                            if v:
                                yml_lines.append(f"  {k}: {json.dumps(v, ensure_ascii=False)}")
                        yml_lines.append("---")

                        body_lines = [
                            *yml_lines,
                            "",
                            f"# {title}",
                            "",
                            "## Extracted Text",
                            "",
                            pdf_text.strip(),
                        ]
                        out_md.write_text("\n".join(body_lines).rstrip() + "\n", encoding="utf-8")
                        converted_md_rel = str(out_md.relative_to(intake_root))
                    else:
                        pages_ocrd = _select_pages(
                            total=pages_total,
                            full_threshold=args.full_pages_threshold,
                            first_pages=args.first_pages,
                            last_pages=args.last_pages,
                        )
                        if args.max_pdf_mb and (st.st_size > args.max_pdf_mb * 1024 * 1024):
                            pages_ocrd = sorted(set([1] + ([pages_total] if pages_total and pages_total != 1 else [])))

                        tmp = Path(tempfile.mkdtemp(prefix="unreadable_ocr_"))
                        try:
                            images = _render_pdf_pages(p, pages_ocrd, tmp, dpi=args.dpi)
                            txt_name = _safe_out_name(rel_from_library.name, rel_posix, ".ocr.txt")
                            out_txt = (out_text / rel_from_library.parent) / txt_name
                            _node_ocr_images(
                                ocrjs_dir=ocrjs_dir,
                                images=images,
                                out_txt=out_txt,
                                lang=args.lang,
                                cache_dir=out_cache,
                            )
                            text = out_txt.read_text(encoding="utf-8", errors="replace")
                            dois, isbns = _extract_signals(text)
                            doi = ";".join(dois)
                            isbn = ";".join(isbns)

                            partial = bool(pages_total and len(pages_ocrd) < pages_total)
                            title = (meta.get("Title") or "").strip() or p.name

                            yml_lines = [
                                "---",
                                "type: raw",
                                "source_kind: pdf_ocr",
                                f"source_path: {str(p)}",
                                f"source_rel: {rel_posix}",
                                f"ocr_engine: tesseract.js",
                                f"ocr_lang: {args.lang}",
                                f"pages_total: {pages_total}",
                                f"pages_ocrd: {json.dumps(pages_ocrd)}",
                                f"partial: {str(partial).lower()}",
                                f"ocr_text: {str(out_txt.relative_to(intake_root))}",
                                "pdfinfo:",
                            ]
                            for k in sorted(meta.keys()):
                                v = meta[k].replace("\n", " ").strip()
                                if v:
                                    yml_lines.append(f"  {k}: {json.dumps(v, ensure_ascii=False)}")
                            yml_lines.append("---")

                            body_lines = [
                                *yml_lines,
                                "",
                                f"# {title}",
                                "",
                                "## OCR Notes",
                                "",
                                "- This is an OCR extraction pass over `Review/Unreadable/` when `pdftotext` was empty/failed.",
                                "- Page strategy: full OCR for short PDFs; first + last pages for long PDFs.",
                                "",
                                "## Extracted Text",
                                "",
                                text.strip(),
                            ]
                            out_md.write_text("\n".join(body_lines).rstrip() + "\n", encoding="utf-8")
                            converted_md_rel = str(out_md.relative_to(intake_root))
                            ocr_text_rel = str(out_txt.relative_to(intake_root))
                        finally:
                            shutil.rmtree(tmp, ignore_errors=True)
                else:
                    # Non-PDF: capture with MarkItDown where possible, otherwise plaintext fallback.
                    if ext in {".txt", ".md", ".csv", ".json", ".xml"}:
                        text = _read_text_lossy(p)
                        out_md.write_text(
                            "\n".join(
                                [
                                    "---",
                                    "type: raw",
                                    "source_kind: text",
                                    f"source_path: {str(p)}",
                                    f"source_rel: {rel_posix}",
                                    "---",
                                    "",
                                    f"# {p.name}",
                                    "",
                                    "## Extracted Text",
                                    "",
                                    text.rstrip(),
                                    "",
                                ]
                            ),
                            encoding="utf-8",
                        )
                        converted_md_rel = str(out_md.relative_to(intake_root))
                        dois, isbns = _extract_signals(text)
                        doi = ";".join(dois)
                        isbn = ";".join(isbns)
                    elif ext in {".docx", ".doc", ".ppt", ".xls"}:
                        text = _office_to_text(p)
                        out_md.write_text(
                            "\n".join(
                                [
                                    "---",
                                    "type: raw",
                                    "source_kind: office_text",
                                    f"source_path: {str(p)}",
                                    f"source_rel: {rel_posix}",
                                    "---",
                                    "",
                                    f"# {p.name}",
                                    "",
                                    "## Extracted Text",
                                    "",
                                    text.rstrip(),
                                    "",
                                ]
                            ),
                            encoding="utf-8",
                        )
                        converted_md_rel = str(out_md.relative_to(intake_root))
                        dois, isbns = _extract_signals(text)
                        doi = ";".join(dois)
                        isbn = ";".join(isbns)
                    elif md_converter is not None and ext in {
                        ".doc",
                        ".docx",
                        ".ppt",
                        ".pptx",
                        ".xls",
                        ".xlsx",
                        ".rtf",
                        ".html",
                        ".htm",
                        ".epub",
                    }:
                        result = md_converter.convert_local(str(p))
                        md_text = (result.markdown or "").strip()
                        out_md.write_text(md_text + "\n", encoding="utf-8")
                        converted_md_rel = str(out_md.relative_to(intake_root))
                        dois, isbns = _extract_signals(md_text)
                        doi = ";".join(dois)
                        isbn = ";".join(isbns)
                    else:
                        status = "skipped"
                        err = "No converter available for non-PDF file"

            if doi or isbn:
                henry_rows.append(
                    {
                        "rel_path": rel_posix,
                        "ext": ext,
                        "doi": doi,
                        "isbn": isbn,
                        "converted_md": converted_md_rel,
                        "ocr_text": ocr_text_rel,
                    }
                )
        except Exception as e:
            status = "error"
            err = str(e)

        status_rows.append(
            StatusRow(
                rel_path=rel_posix,
                abs_path=str(p),
                ext=ext,
                size_bytes=int(st.st_size),
                mtime_utc=_iso(st.st_mtime),
                pages_total=pages_total,
                pages_ocrd=json.dumps(pages_ocrd) if pages_ocrd else "",
                converted_md=converted_md_rel,
                ocr_text=ocr_text_rel,
                doi=doi,
                isbn=isbn,
                status=status,
                error=err,
            )
        )

        if idx % 10 == 0:
            print(f"[library_d_unreadable_ocr] Progress: {idx}/{len(files)}", file=sys.stderr)

    status_csv = out_inventory / "ocr_status.csv"
    with status_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(
            [
                "rel_path",
                "abs_path",
                "ext",
                "size_bytes",
                "mtime_utc",
                "pages_total",
                "pages_ocrd",
                "converted_md",
                "ocr_text",
                "doi",
                "isbn",
                "status",
                "error",
            ]
        )
        for r in status_rows:
            w.writerow(
                [
                    r.rel_path,
                    r.abs_path,
                    r.ext,
                    r.size_bytes,
                    r.mtime_utc,
                    r.pages_total,
                    r.pages_ocrd,
                    r.converted_md,
                    r.ocr_text,
                    r.doi,
                    r.isbn,
                    r.status,
                    r.error,
                ]
            )

    henry_csv = out_henry / "MASTER_REFERENCE_CANDIDATES_OCR.csv"
    with henry_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["rel_path", "ext", "doi", "isbn", "converted_md", "ocr_text"])
        for row in henry_rows:
            w.writerow([row["rel_path"], row["ext"], row["doi"], row["isbn"], row["converted_md"], row["ocr_text"]])

    ok = sum(1 for r in status_rows if r.status == "ok")
    skipped = sum(1 for r in status_rows if r.status == "skipped")
    errors = sum(1 for r in status_rows if r.status == "error")
    pdfs = sum(1 for r in status_rows if r.ext.lower() == ".pdf" or r.rel_path.lower().endswith(".pdf"))
    converted = sum(1 for r in status_rows if r.converted_md)
    with (out_inventory / "OCR_SUMMARY.md").open("w", encoding="utf-8") as f:
        f.write(
            "\n".join(
                [
                    "# D:\\LIBRARY\\Review\\Unreadable — OCR Summary (2026-04-26)",
                    "",
                    f"- Files processed: {len(status_rows)}",
                    f"- Converted notes written: {converted}",
                    f"- PDFs detected: {pdfs}",
                    f"- Status: ok={ok} skipped={skipped} error={errors}",
                    "",
                    "## Outputs",
                    f"- Status CSV: `{status_csv.relative_to(intake_root)}`",
                    f"- Henry candidates (OCR): `{henry_csv.relative_to(intake_root)}`",
                    f"- Converted OCR notes: `{out_converted.relative_to(intake_root)}/`",
                    f"- OCR text: `{out_text.relative_to(intake_root)}/`",
                    "",
                ]
            )
            + "\n"
        )

    readme = intake_root / "00_README.md"
    readme.write_text(
        "\n".join(
            [
                "# D:\\LIBRARY — OCR pass for Review/Unreadable (2026-04-26)",
                "",
                f"- Input: `{unreadable_root}`",
                f"- OCR engine: tesseract.js (WASM) via `{ocrjs_dir}/ocr_images.mjs`",
                f"- OCR languages: `{args.lang}`",
                "",
                "## Where to look",
                f"- Summary: `{(out_inventory / 'OCR_SUMMARY.md').relative_to(intake_root)}`",
                f"- Status: `{(out_inventory / 'ocr_status.csv').relative_to(intake_root)}`",
                f"- Notes: `{out_converted.relative_to(intake_root)}/`",
                f"- Text: `{out_text.relative_to(intake_root)}/`",
                f"- Henry candidates: `{(out_henry / 'MASTER_REFERENCE_CANDIDATES_OCR.csv').relative_to(intake_root)}`",
                "",
                "## Page strategy",
                "- If PDF pages <= full threshold: OCR all pages.",
                "- Otherwise: OCR first N pages + last M pages (title/abstract + references).",
                "",
            ]
        )
        + "\n",
        encoding="utf-8",
    )

    print(str(readme))
    print(str(out_inventory / "OCR_SUMMARY.md"))
    print(str(status_csv))
    print(str(henry_csv))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
