#!/usr/bin/env python3
"""
bookbuild.py - export and build tool for the Book Studio (Starter).

Commands
--------
  python scripts/bookbuild.py check
      Verifies that pandoc, PyYAML, pypdf and Playwright (Chromium) are installed.

  python scripts/bookbuild.py chapter books/<slug> chapters/ch01-name.md
      Builds previews/ch01-name.docx and previews/ch01-name.pdf for ONE chapter,
      using the book's trim size, margins and book.css.

  python scripts/bookbuild.py book books/<slug>
      Assembles ALL chapters (sorted by file name) with front matter and a table
      of contents into final/<slug>-manuscript.docx and final/<slug>-interior.pdf,
      then writes final/build-report.md (page count, margin check, missing images).

Requirements (one time):
  - Pandoc            https://pandoc.org/installing.html
  - Python 3.9+
  - pip install pyyaml pypdf playwright
  - python -m playwright install chromium
"""
import argparse
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None

DEFAULTS = {
    "trim_width_in": 6.0,
    "trim_height_in": 9.0,
    "margin_top_in": 0.75,
    "margin_bottom_in": 0.75,
    "margin_inside_in": 0.75,
    "margin_outside_in": 0.6,
    "color_interior": True,
    "title": "Untitled",
    "subtitle": "",
    "author": "",
    "language": "en",
    "copyright_year": date.today().year,
    "isbn": "",
}


# ----------------------------------------------------------------- helpers
def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def load_cfg(book_dir: Path) -> dict:
    cfg = dict(DEFAULTS)
    f = book_dir / "book.yaml"
    if not f.exists():
        die(f"{f} not found. Run /new-book first.")
    if yaml is None:
        die("PyYAML missing. Run: pip install pyyaml")
    data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    cfg.update({k: v for k, v in data.items() if v is not None})
    return cfg


def run(cmd, cwd=None):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if r.returncode != 0:
        die(f"Command failed: {' '.join(map(str, cmd))}\n{r.stderr}")
    return r.stdout


def required_gutter(pages: int) -> float:
    if pages <= 150:
        return 0.375
    if pages <= 300:
        return 0.5
    if pages <= 500:
        return 0.625
    if pages <= 700:
        return 0.75
    return 0.875


def page_css(cfg: dict) -> str:
    w, h = cfg["trim_width_in"], cfg["trim_height_in"]
    t, b = cfg["margin_top_in"], cfg["margin_bottom_in"]
    i, o = cfg["margin_inside_in"], cfg["margin_outside_in"]
    return f"""
@page {{ size: {w}in {h}in; margin: {t}in {o}in {b}in {i}in; }}
@page :right {{ margin-left: {i}in; margin-right: {o}in; }}
@page :left  {{ margin-left: {o}in; margin-right: {i}in; }}
"""


def read_css(book_dir: Path, root: Path) -> str:
    base = root / "templates" / "interior.css"
    css = base.read_text(encoding="utf-8") if base.exists() else ""
    custom = book_dir / "book.css"
    if custom.exists():
        css += "\n" + custom.read_text(encoding="utf-8")
    return css


def md_to_docx(md: Path, out: Path, book_dir: Path, root: Path, toc=False):
    cmd = ["pandoc", str(md.relative_to(book_dir) if md.is_relative_to(book_dir) else md),
           "-f", "markdown+smart", "-o", str(out), "--resource-path", str(book_dir)]
    ref = root / "templates" / "reference.docx"
    if ref.exists():
        cmd += ["--reference-doc", str(ref)]
    if toc:
        cmd += ["--toc", "--toc-depth=1"]
    run(cmd, cwd=book_dir)


def md_to_pdf(md: Path, out: Path, book_dir: Path, cfg: dict, root: Path, toc=False):
    from playwright.sync_api import sync_playwright

    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        css_file = td / "style.css"
        css_file.write_text(page_css(cfg) + read_css(book_dir, root), encoding="utf-8")
        html = td / "book.html"
        cmd = ["pandoc", str(md), "-f", "markdown+smart", "-s", "--embed-resources",
               "--css", str(css_file), "--resource-path", str(book_dir),
               "--metadata", f"title={cfg['title']}", "--metadata", "pagetitle=" + cfg["title"],
               "--metadata", f"lang={cfg['language']}", "-o", str(html)]
        if toc:
            cmd += ["--toc", "--toc-depth=1"]
        run(cmd, cwd=book_dir)
        # pandoc puts the metadata title in a title block; remove it (we write our own title page)
        text = html.read_text(encoding="utf-8")
        text = re.sub(r'<header id="title-block-header">.*?</header>', "", text, flags=re.S)
        html.write_text(text, encoding="utf-8")

        footer = ('<div style="font-size:8px;width:100%;text-align:center;">'
                  '<span class="pageNumber"></span></div>')

        def render():
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(html.as_uri())
                page.wait_for_load_state("networkidle")
                page.pdf(path=str(out), prefer_css_page_size=True, print_background=True,
                         display_header_footer=not cfg.get("page_decor"), header_template="<div></div>",
                         footer_template=footer)
                browser.close()

        # Part openers must start on a right-hand (odd) page. Chromium ignores
        # break-before: right, so pass 1 finds openers that landed on a left page
        # and the HTML gets an empty page inserted before them (repeat until stable).
        # A second pass floats figures: when a figure was pushed to the top of a page and
        # the page before it is less than 72 percent full, the figure (with its pointer
        # line) moves down past the next paragraph, so text fills the gap.
        from pypdf import PdfReader
        float_moves = {}
        for _ in range(40):
            render()
            if not cfg.get("openers_on_right"):
                break
            text = html.read_text(encoding="utf-8")
            pages = [norm(pg.extract_text() or "") for pg in PdfReader(str(out)).pages]
            changed, cur, pos = False, 0, 0
            for m in list(re.finditer(r"<h1\b[^>]*>(.*?)</h1>", text, flags=re.S)):
                if "titlemark" in m.group(0) or " front" in m.group(0) or 'class="front' in m.group(0):
                    continue
                key = norm(re.sub(r"<[^>]+>", "", m.group(1)))[:30]
                hit = next((i for i in range(cur, len(pages)) if key and pages[i].startswith(key)), None)
                if hit is None:
                    continue
                cur = hit
                has_blank = "blankpage" in text[max(0, m.start() - 60):m.start()]
                if hit % 2 == 1 and not has_blank:
                    text = text[:m.start()] + '<div class="blankpage">&nbsp;</div>' + text[m.start():]
                    changed = True
                    break  # re-render: later page numbers shift
                if hit % 2 == 1 and has_blank:
                    # the blank itself pushed the opener onto a left page: take it out
                    b = text.rfind('<div class="blankpage">', 0, m.start())
                    text = text[:b] + text[m.start():]
                    changed = True
                    break
            if changed:
                html.write_text(text, encoding="utf-8")
                continue
            if cfg.get("float_figures"):
                new_text = float_figures(text, out, pages, float_moves)
                if new_text != text:
                    html.write_text(new_text, encoding="utf-8")
                    continue
            break
        if cfg.get("page_decor"):
            sys.path.insert(0, str(Path(__file__).resolve().parent))
            from pagedeco import decorate
            decorate(out, cfg)



def page_fills(pdf: Path):
    """Share of the text area used on each page (0 to 1), from word positions."""
    r = subprocess.run(["pdftotext", "-bbox", str(pdf), "-"], capture_output=True, text=True)
    fills, h, lo, hi = [], 576.0, 0.0, 0.0
    for line in r.stdout.splitlines():
        m = re.match(r'\s*<page width="([\d.]+)" height="([\d.]+)"', line)
        if m:
            if fills or lo or hi:
                fills.append(hi)
            h = float(m.group(2)); hi = 0.0; lo = 1.0
            continue
        w = re.match(r'\s*<word xMin="[\d.]+" yMin="([\d.]+)" xMax="[\d.]+" yMax="([\d.]+)"', line)
        if w:
            y0, y1 = float(w.group(1)), float(w.group(2))
            if y0 > 0.07 * h and y1 < 0.93 * h:
                hi = max(hi, (y1 - 0.07 * h) / (0.86 * h))
    fills.append(hi)
    return fills


def float_figures(text: str, pdf: Path, pages, moves):
    """Move a figure (and its pointer paragraph) down one block when it left a gap."""
    import lxml.html as LH
    fills = page_fills(pdf)
    doc = LH.fromstring(text)
    changed = False
    for fig in doc.iter("figure"):
        cap = fig.find(".//figcaption")
        if cap is None:
            continue
        mm = re.match(r"\s*Figure\s+(\d+)\.", cap.text_content())
        if not mm:
            continue
        n = mm.group(1)
        key = norm(f"Figure {n}.")
        k = next((i for i, t in enumerate(pages) if t.startswith(key)), None)
        if k is None or k == 0 or moves.get(n, 0) >= 6:
            continue
        if fills[k - 1] >= 0.72:
            continue
        nxt = fig.getnext()
        if nxt is None or nxt.tag not in ("p", "div", "table") or (nxt.tag == "div" and "procedure" in (nxt.get("class") or "")):
            continue
        prev = fig.getprevious()
        group = [fig]
        if prev is not None and prev.tag == "p" and re.match(r"\s*Figure\s+" + n + r"\s", prev.text_content()):
            group = [prev, fig]
        anchor = nxt
        for el in group:
            el.getparent().remove(el)
        parent = anchor.getparent()
        idx = parent.index(anchor) + 1
        for j, el in enumerate(group):
            parent.insert(idx + j, el)
        moves[n] = moves.get(n, 0) + 1
        changed = True
        break  # one move per render keeps later pages predictable
    if not changed:
        return text
    return "<!DOCTYPE html>\n" + LH.tostring(doc, encoding="unicode")

def pdf_pages(pdf: Path) -> int:
    from pypdf import PdfReader
    return len(PdfReader(str(pdf)).pages)


def missing_images(md_text: str, book_dir: Path):
    missing = []
    for m in re.finditer(r"!\[[^\]]*\]\(([^)\s]+)", md_text):
        p = m.group(1)
        if p.startswith("http"):
            continue
        if not (book_dir / p).exists():
            missing.append(p)
    return missing



def toc_block(titles, pages=None):
    lines = ['<div class="toc">', '', '<p class="toc-heading">Contents</p>', '']
    for i, t in enumerate(titles):
        num = f'<span class="toc-page">{pages[i]}</span>' if pages else ""
        lines.append(f'<p class="toc-line"><span class="toc-title">{t}</span>{num}</p>')
        lines.append('')
    lines.append('</div>')
    lines.append('')
    return "\n".join(lines) + "\n"


def chapter_title(md_text: str) -> str:
    m = re.search(r"^#\s+(.+)$", md_text, flags=re.M)
    return m.group(1).strip() if m else "Untitled chapter"


def norm(text: str) -> str:
    """Letters and digits only, lowercase: robust to odd glyphs (e.g. colons) in PDF text."""
    return re.sub(r"[^0-9a-z]", "", text.lower())


def find_pages(pdf: Path, titles, start_index=3):
    """Return the printed page number of each chapter title (1-based PDF page)."""
    from pypdf import PdfReader
    reader = PdfReader(str(pdf))
    texts = [(pg.extract_text() or "") for pg in reader.pages]
    found, cur = [], start_index
    for t in titles:
        key = norm(t)
        hit = None
        for idx in range(cur, len(texts)):
            if key in norm(texts[idx]):
                hit = idx
                break
        if hit is None:
            found.append("")
        else:
            found.append(hit + 1)
            cur = hit + 1
    return found


def front_matter(cfg: dict) -> str:
    parts = [f'<div class="title-page">\n\n# {cfg["title"]}\n\n']
    if cfg.get("subtitle"):
        parts.append(f'<p class="subtitle">{cfg["subtitle"]}</p>\n\n')
    parts.append(f'<p class="author">{cfg.get("author", "")}</p>\n\n</div>\n\n')
    parts.append('<div class="copyright-page">\n\n')
    parts.append(f'Copyright &copy; {cfg["copyright_year"]} {cfg.get("author", "")}. All rights reserved.\n\n')
    parts.append("No part of this book may be reproduced without written permission "
                 "from the author, except for brief quotations in reviews.\n\n")
    if cfg.get("isbn"):
        parts.append(f'ISBN: {cfg["isbn"]}\n\n')
    parts.append("</div>\n\n")
    return "".join(parts)


# ---------------------------------------------------------------- commands
def cmd_check(_):
    ok = True
    for tool in ["pandoc"]:
        found = shutil.which(tool)
        print(f"[{'OK' if found else 'MISSING'}] {tool}")
        ok &= bool(found)
    for mod in ["yaml", "pypdf", "playwright"]:
        try:
            __import__(mod)
            print(f"[OK] python module {mod}")
        except ImportError:
            print(f"[MISSING] python module {mod}  ->  pip install {'pyyaml' if mod == 'yaml' else mod}")
            ok = False
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            p.chromium.launch().close()
        print("[OK] Playwright Chromium")
    except Exception as e:
        print(f"[MISSING] Playwright Chromium -> python -m playwright install chromium ({e})")
        ok = False
    print("\nAll good." if ok else "\nFix the items marked MISSING, then run check again.")
    sys.exit(0 if ok else 1)


def cmd_chapter(args):
    root = Path(__file__).resolve().parent.parent
    book_dir = Path(args.book).resolve()
    cfg = load_cfg(book_dir)
    md = (book_dir / args.chapter).resolve()
    if not md.exists():
        die(f"{md} not found")
    out_dir = book_dir / "previews"
    out_dir.mkdir(exist_ok=True)
    stem = md.stem
    text = md.read_text(encoding="utf-8")
    miss = missing_images(text, book_dir)
    if miss:
        print("WARNING: missing images:", ", ".join(miss))
    md_to_docx(md, out_dir / f"{stem}.docx", book_dir, root)
    md_to_pdf(md, out_dir / f"{stem}.pdf", book_dir, cfg, root)
    words = len(re.findall(r"\b\w+\b", text))
    pages = pdf_pages(out_dir / f"{stem}.pdf")
    print(f"Built previews/{stem}.docx and previews/{stem}.pdf  |  {words} words  |  {pages} pages")


def cmd_book(args):
    root = Path(__file__).resolve().parent.parent
    book_dir = Path(args.book).resolve()
    cfg = load_cfg(book_dir)
    chapters = sorted((book_dir / "chapters").glob("ch*.md"))
    if not chapters:
        die("No chapters found in chapters/ (expected files like ch01-name.md)")
    final = book_dir / "final"
    final.mkdir(exist_ok=True)
    slug = book_dir.name

    texts, all_missing = [], []
    for c in chapters:
        t = c.read_text(encoding="utf-8")
        all_missing += [(c.name, m) for m in missing_images(t, book_dir)]
        texts.append(t.strip())
    titles = [chapter_title(t) for t in texts]
    chapters_md = "\n\n".join(texts) + "\n"
    fm = front_matter(cfg)
    combined = final / "_combined.md"

    # Word manuscript: contents list without page numbers (Word paginates differently)
    combined.write_text(fm + toc_block(titles) + "\n" + chapters_md, encoding="utf-8")
    md_to_docx(combined, final / f"{slug}-manuscript.docx", book_dir, root)

    # PDF: two passes so the contents list shows the real page numbers
    pdf_out = final / f"{slug}-interior.pdf"
    combined.write_text(fm + toc_block(titles, ["0"] * len(titles)) + "\n" + chapters_md, encoding="utf-8")
    md_to_pdf(combined, pdf_out, book_dir, cfg, root)
    nums = find_pages(pdf_out, titles)
    combined.write_text(fm + toc_block(titles, nums) + "\n" + chapters_md, encoding="utf-8")
    md_to_pdf(combined, pdf_out, book_dir, cfg, root)
    nums2 = find_pages(pdf_out, titles)
    if nums2 != nums:  # contents page count shifted; one more pass
        combined.write_text(fm + toc_block(titles, nums2) + "\n" + chapters_md, encoding="utf-8")
        md_to_pdf(combined, pdf_out, book_dir, cfg, root)
    body = fm + chapters_md
    pages = pdf_pages(final / f"{slug}-interior.pdf")
    words = len(re.findall(r"\b\w+\b", body))

    need = required_gutter(pages)
    gutter = cfg["margin_inside_in"]
    outer_min = min(cfg["margin_outside_in"], cfg["margin_top_in"], cfg["margin_bottom_in"])
    problems = []
    if pages < 24:
        problems.append(f"Page count {pages} is below the KDP paperback minimum of 24.")
    if gutter < need:
        problems.append(f"Inside margin {gutter} in is below the {need} in needed for {pages} pages.")
    if outer_min < 0.25:
        problems.append("An outside/top/bottom margin is below 0.25 in.")
    if all_missing:
        problems.append("Missing images: " + ", ".join(f"{a}: {b}" for a, b in all_missing))

    report = [
        f"# Build report: {cfg['title']}",
        f"Built: {date.today().isoformat()}",
        "",
        f"- Chapters: {len(chapters)}",
        f"- Words (approx.): {words}",
        f"- Pages in interior PDF: {pages}",
        f"- Trim size: {cfg['trim_width_in']} x {cfg['trim_height_in']} in",
        f"- Margins (top/bottom/inside/outside): {cfg['margin_top_in']}/{cfg['margin_bottom_in']}/{cfg['margin_inside_in']}/{cfg['margin_outside_in']} in",
        f"- Gutter required for this page count: {need} in",
        f"- Color interior: {cfg['color_interior']}",
        "",
        "## Checks",
    ]
    report += [f"- PROBLEM: {p}" for p in problems] or ["- All automatic checks passed."]
    report += ["", "## Reminder",
               "Open the PDF yourself and look at every page, then use KDP's online previewer before publishing."]
    (final / "build-report.md").write_text("\n".join(report), encoding="utf-8")
    combined.unlink(missing_ok=True)
    print("\n".join(report))


def main():
    ap = argparse.ArgumentParser(description="Book Studio build tool")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    c = sub.add_parser("chapter")
    c.add_argument("book")
    c.add_argument("chapter")
    c.set_defaults(fn=cmd_chapter)
    b = sub.add_parser("book")
    b.add_argument("book")
    b.set_defaults(fn=cmd_book)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
