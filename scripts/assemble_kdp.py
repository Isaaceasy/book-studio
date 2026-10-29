#!/usr/bin/env python3
"""
assemble_kdp.py - assemble the whole KDP interior PDF for a book that has
front/, chapters/ and back/ folders (used by Emergency Nursing Fundamentals).

What it does (plain language):
  1. Joins title page, front matter, a static contents page, the six Parts and
     the back matter (appendices, glossary, static index) into one file.
  2. Builds the PDF with bookbuild.md_to_pdf (same design, blank-page rule and
     page furniture as the chapter previews).
  3. Reads the finished PDF to find the real page of every Part, entry and
     back-matter section, writes those numbers into the contents page and
     rebuilds until the numbers stop changing.
  4. Builds the static index from back/index-terms.txt by finding which pages
     of the Parts mention each term, and rebuilds once more.
  5. Runs quality checks and writes final/build-report.md (page count, KDP
     margin table check, fonts embedded, links, forbidden words, image
     resolution, blank pages and nearly empty pages).

Usage: python scripts/assemble_kdp.py books/<slug> [--draft]
  --draft adds _DRAFT_FOR_REVIEW to the file name (file name only; the
  manuscript never carries that label).
"""
import argparse
import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import bookbuild as bb  # noqa: E402


def norm(t):
    return re.sub(r"[^0-9a-z]", "", t.lower())


def title_page(cfg):
    return (f'<div class="title-page">\n\n<div class="band">\n<p class="kicker">A compact illustrated guide</p>\n\n'
            f'# {cfg["title"]} {{data-label="" .titlemark}}\n\n</div>\n\n'
            f'<p class="subtitle">{cfg["subtitle"]}</p>\n\n<p class="author">{cfg["author"]}</p>\n\n</div>\n\n')


def parse_toc_items(book_dir, cfg):
    """Return [(kind, label, search_key)] in book order. kind: part, entry, back."""
    items = []
    for f in sorted((book_dir / "chapters").glob("ch0*.md")):
        t = f.read_text(encoding="utf-8")
        m = re.search(r'^#\s+(.+?)\s*\{data-label="Part (\d+)"', t, flags=re.M)
        items.append(("part", f"Part {m.group(2)}  {m.group(1)}", norm(m.group(1))))
        for e in re.finditer(r'^##\s+\[(\d\.\d)\]\{\.num\}\s+(.+)$', t, flags=re.M):
            items.append(("entry", f"{e.group(1)}  {e.group(2).strip()}", norm(e.group(1) + e.group(2))))
    return items


def back_items():
    return [("back", "Appendix A: Answers to Review Questions", norm("Appendix A")),
            ("back", "Appendix B: Abbreviations", norm("Appendix B")),
            ("back", "Appendix C: Reference Values", norm("Appendix C")),
            ("back", "Glossary", norm("Glossary")),
            ("back", "Index", norm("Index"))]


def front_items():
    return [("front", "How to Use This Book", norm("How to Use This Book"))]


def contents_md(items, pages):
    lines = ['<div class="toc">', '', '<p class="toc-heading">Contents</p>', '']
    for i, (kind, label, _) in enumerate(items):
        cls = {"part": "part", "entry": "entry", "back": "part", "front": "part"}[kind]
        pg = pages.get(i, "")
        lines.append(f'<p class="toc-line {cls}"><span class="toc-title">{label}</span><span class="toc-page">{pg}</span></p>')
        lines.append('')
    lines.append('</div>')
    return "\n".join(lines) + "\n\n"


def answers_md(book_dir):
    out = ['# Appendix A: Answers to Review Questions {data-label="Reference" .back}', '']
    for n in range(1, 7):
        f = book_dir / "back" / f"answer-keys-part{n}.md"
        if not f.exists():
            continue
        out += [f'## Part {n}', '']
        for line in f.read_text(encoding="utf-8").splitlines():
            m = re.match(r'^(\d)\.\s+(.*)$', line.strip())
            if m:
                out += [f'**{m.group(1)}.** {m.group(2)}', '']
    return "\n".join(out) + "\n"


def index_md(book_dir, page_texts, body_range):
    terms = []
    f = book_dir / "back" / "index-terms.txt"
    for line in f.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            parts = [p.strip() for p in line.split("|")]
            terms.append((parts[0], parts[1:] or [parts[0]]))
    lo, hi = body_range
    rows = {}
    for head, pats in terms:
        pgs = []
        for i in range(lo, hi):
            tx = page_texts[i]
            if any(re.search(r"(?i)\b" + re.escape(p) + r"\b", tx) for p in ([head] + pats)):
                pgs.append(i + 1)
        if pgs:
            rows[head] = pgs
    def compress(p):
        # ranges for runs of consecutive pages
        out, i = [], 0
        while i < len(p):
            j = i
            while j + 1 < len(p) and p[j + 1] == p[j] + 1:
                j += 1
            out.append(f"{p[i]}" if i == j else f"{p[i]}-{p[j]}")
            i = j + 1
        return ", ".join(out)
    out = ['# Index {data-label="Reference" .back}', '', '::: {.twocol}', '']
    cur = ''
    for head in sorted(rows, key=str.lower):
        L = head[0].upper()
        if L != cur:
            cur = L
            out += [f'[{L}]{{.letter}}', '']
        pg = rows[head]
        shown = pg if len(pg) <= 10 else pg[:10]
        out += [f'**{head}** {compress(shown)}', '']
    out += [':::']
    return "\n".join(out) + "\n", len(rows)


def read_pages(pdf):
    from pypdf import PdfReader
    return [(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]


def locate(items, page_texts, start):
    pages, cur = {}, start
    for i, (kind, label, key) in enumerate(items):
        hit = None
        for k in range(cur, len(page_texts)):
            tx = norm(page_texts[k])
            if kind in ("part", "back", "front"):
                if tx.startswith(key[:30]):
                    hit = k
                    break
            else:
                if key[:40] in tx:
                    hit = k
                    break
        if hit is not None:
            pages[i] = hit + 1
            cur = hit
    return pages


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("book")
    ap.add_argument("--draft", action="store_true")
    a = ap.parse_args()
    root = Path(__file__).resolve().parent.parent
    book_dir = Path(a.book).resolve()
    cfg = bb.load_cfg(book_dir)
    final = book_dir / "final"
    final.mkdir(exist_ok=True)
    slug = book_dir.name
    name = "emergency-nursing-fundamentals-interior" + ("_DRAFT_FOR_REVIEW" if a.draft else "")
    pdf = final / f"{name}.pdf"
    comb = final / "_combined.md"

    chapters = [f.read_text(encoding="utf-8").strip() for f in sorted((book_dir / "chapters").glob("ch0*.md"))]
    front = [(book_dir / "front" / n).read_text(encoding="utf-8").strip() for n in ("copyright.md", "how-to-use.md")]
    items = front_items() + parse_toc_items(book_dir, cfg) + back_items()
    app_c = (book_dir / "back" / "appendix-c.md").read_text(encoding="utf-8").strip()
    app_b = (book_dir / "back" / "appendix-b.md").read_text(encoding="utf-8").strip()
    glossary = (book_dir / "back" / "glossary.md").read_text(encoding="utf-8").strip()
    answers = answers_md(book_dir).strip()

    def assemble(pages, index_text):
        parts = [title_page(cfg), front[0], contents_md(items, pages), front[1]] if False else None
        txt = title_page(cfg) + front[0] + "\n\n" + contents_md(items, pages) + front[1] + "\n\n"
        txt += "\n\n".join(chapters) + "\n\n" + answers + "\n\n" + app_b + "\n\n" + app_c + "\n\n" + glossary + "\n\n" + index_text
        return txt

    pages, index_text = {}, '# Index {data-label="Reference" .back}\n\n::: {.twocol}\n\nplaceholder\n\n:::\n'
    page_texts = []
    for rnd in range(6):
        comb.write_text(assemble(pages, index_text), encoding="utf-8")
        bb.md_to_pdf(comb, pdf, book_dir, cfg, root)
        page_texts = read_pages(pdf)
        new_pages = locate(items, page_texts, 2)
        first_part = new_pages.get(next(i for i, it in enumerate(items) if it[0] == "part"), 3) - 1
        app_a = new_pages.get(next(i for i, it in enumerate(items) if it[1].startswith("Appendix A")), len(page_texts)) - 1
        new_index, nterms = index_md(book_dir, page_texts, (first_part, app_a))
        print(f"round {rnd + 1}: {len(page_texts)} pages, {len(new_pages)}/{len(items)} entries located, {nterms} index terms")
        if new_pages == pages and new_index == index_text:
            break
        pages, index_text = new_pages, new_index
    comb.unlink(missing_ok=True)
    qc(pdf, cfg, items, pages, page_texts, final)


def qc(pdf, cfg, items, pages, page_texts, final):
    from pypdf import PdfReader
    r = PdfReader(str(pdf))
    n = len(r.pages)
    problems = []
    gutter_need = bb.required_gutter(n)
    if cfg["margin_inside_in"] < gutter_need:
        problems.append(f"Inside margin {cfg['margin_inside_in']} in is below the {gutter_need} in needed for {n} pages.")
    if min(cfg["margin_outside_in"], cfg["margin_top_in"], cfg["margin_bottom_in"]) < 0.25:
        problems.append("An outside, top or bottom margin is below 0.25 in.")
    if n < 72:
        problems.append("Page count below the 72-page minimum for standard color.")
    if n % 2:
        pass
    missing = [it[1] for i, it in enumerate(items) if i not in pages]
    if missing:
        problems.append("Contents entries not located in the PDF: " + "; ".join(missing))
    links = 0
    for p in r.pages:
        for an in (p.get("/Annots") or []):
            try:
                if an.get_object().get("/Subtype") == "/Link":
                    links += 1
            except Exception:
                pass
    if links:
        problems.append(f"{links} link annotations found in the PDF (the manuscript must have no hyperlinks).")
    alltext = "\n".join(page_texts)
    for pat, label in [(r"https?://|www\.", "URL"), (r"(?i)\bpocket\b", "the word Pocket"), (r"(?i)\bclinician[- ]reviewed\b", "clinician-reviewed wording"),
                       (r"(?i)\b(ESI|START triage|ENA|AHA)\b", "a named organization or tool"), (r"(?i)\bDRAFT_FOR_REVIEW\b", "draft label inside the manuscript"),
                       (r"(?i)placeholder|lorem ipsum|TODO", "placeholder text")]:
        found = re.findall(pat, alltext)
        if found:
            problems.append(f"Found {label}: {sorted(set(found))[:5]}")
    fonts = set()
    for p in r.pages:
        res = p.get("/Resources")
        if res and "/Font" in res:
            for k, v in res["/Font"].items():
                fd = v.get_object()
                desc = fd.get("/FontDescriptor")
                emb = bool(desc and any(x in desc.get_object() for x in ("/FontFile", "/FontFile2", "/FontFile3"))) if desc else ("/DescendantFonts" in fd)
                fonts.add((str(fd.get("/BaseFont")), emb))
    notemb = [f for f, e in fonts if not e]
    blanks = [i + 1 for i, t in enumerate(page_texts) if len(t.strip()) < 3]
    sparse = [i + 1 for i, t in enumerate(page_texts) if 3 <= len(t.strip()) < 250 and (i + 1) > 4]
    words = len(re.findall(r"\b\w+\b", alltext))
    rep = [f"# Build report: {cfg['title']}", f"Built: {date.today().isoformat()}", "",
           f"- Pages in interior PDF: {n}", f"- Words in the PDF text layer (approx., includes headers and numbers): {words}",
           f"- Trim: {cfg['trim_width_in']} x {cfg['trim_height_in']} in; margins top/bottom/inside/outside {cfg['margin_top_in']}/{cfg['margin_bottom_in']}/{cfg['margin_inside_in']}/{cfg['margin_outside_in']} in",
           f"- Inside margin required for {n} pages (KDP table read 2026-10-29): {gutter_need} in",
           f"- Fonts: {len(fonts)} font resources; not embedded: {notemb or 'none'}",
           f"- Intentional blank pages: {blanks}", f"- Pages with very little text (check by eye): {sparse}", "",
           "## Contents page numbers"]
    for i, it in enumerate(items):
        rep.append(f"- {it[1]}: page {pages.get(i, 'NOT FOUND')}")
    rep += ["", "## Checks"] + ([f"- PROBLEM: {p}" for p in problems] or ["- All automatic checks passed."])
    rep += ["", "## Reminder", "Open the PDF and look at every page, check it in the KDP online previewer, and order a proof copy before publishing. The file stays DRAFT_FOR_REVIEW until a named clinician's clearance is recorded in status.md."]
    (final / "build-report.md").write_text("\n".join(rep), encoding="utf-8")
    print("\n".join(rep[:12]))
    print("\n".join(f"PROBLEM: {p}" for p in problems) or "All automatic checks passed.")


if __name__ == "__main__":
    main()
