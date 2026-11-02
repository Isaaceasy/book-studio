#!/usr/bin/env python3
"""
docxbuild.py - builds Word (.docx) books to the EMB / MEB framework house style.

House style (fixed, from the frameworks)
  US Letter 8.5 x 11 in, portrait, 1 in margins on all sides (6.5 in content width)
  Times New Roman 12 pt for every non-heading element, justified, line spacing 1.15
  Heading styles 1-7 (book.yaml: heading_style), Heading 1 = chapter/Part, Heading 2 = section/entry
  One Word "Dropped" drop cap (3 lines) on the first body paragraph of every chapter
  Native editable Word equations (write $...$ and $$...$$ in the Markdown)
  Tables exactly 6.5 in wide, zero indent, repeating header row, one 12 pt line after
  No hyperlinks, no bookmarks, no comments, no tracked changes, no placeholders
  Static (non-hyperlinked) table of contents with real page numbers, optional static index
  Front matter in lowercase Roman numerals, Arabic numbering restarts at 1 on Chapter 1

Commands
  python scripts/docxbuild.py check
  python scripts/docxbuild.py chapter books/<slug> chapters/ch01-x.md
        -> previews/ch01-x.docx + previews/ch01-x.pdf + QC printout
  python scripts/docxbuild.py book books/<slug>
        -> final/<slug>-manuscript.docx + .pdf + final/qc-report.md
  python scripts/docxbuild.py qc path/to/file.docx [--chapters N] [--floor WORDS]

Requirements: pandoc, LibreOffice (soffice) for the PDF test copy and page numbers,
  pip install python-docx pyyaml pypdf playwright ; python -m playwright install chromium
"""
import argparse
import copy
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile
from datetime import date
from pathlib import Path

try:
    import yaml
    from docx import Document
    from docx.enum.style import WD_STYLE_TYPE
    from docx.enum.text import WD_ALIGN_PARAGRAPH
    from docx.oxml import OxmlElement, parse_xml
    from docx.oxml.ns import nsdecls, qn
    from docx.shared import Inches, Pt, RGBColor
except ImportError:  # reported by `check`
    yaml = None
    Document = None

FONT = "Times New Roman"
W = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"
CONTENT_TWIPS = 9360  # 6.5 in

DEFAULTS = {
    "title": "Untitled", "subtitle": "", "author": "", "publisher": "", "language": "en",
    "region": "", "copyright_year": date.today().year, "isbn": "", "profile": "engineering",
    "heading_style": 1, "trim_width_in": 8.5, "trim_height_in": 11.0, "margin_in": 1.0,
    "chapter_word_floor": 10000, "chapter_word_ceiling": 12000, "image_count": 0,
    "accent": "1F4E79", "copyright_text": "", "dedication": "", "acknowledgements": "",
}

CHAPTER_WORDS_NUM = re.compile(r"^\d+\s*[:.\-\u2013\u2014]")
CHAPTER_WORDS = r"(Chapter|Part|Chapitre|Partie|Kapitel|Teil|Cap[ií]tulo|Parte)"
HEADING_STYLES = {
    1: "Black Banner", 2: "Rule Line", 3: "Numbered Block", 4: "Centered Classic",
    5: "Shaded Bar", 6: "Underline Accent", 7: "Minimal Modern",
}


# ------------------------------------------------------------------ utilities
def die(msg):
    print(f"ERROR: {msg}", file=sys.stderr)
    sys.exit(1)


def run(cmd, cwd=None, binary=False):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=not binary)
    if r.returncode != 0:
        err = r.stderr if not binary else r.stderr.decode("utf-8", "ignore")
        die(f"Command failed: {' '.join(map(str, cmd))}\n{err}")
    return r.stdout


def load_cfg(book_dir: Path) -> dict:
    cfg = dict(DEFAULTS)
    f = book_dir / "book.yaml"
    if not f.exists():
        die(f"{f} not found. Run /new-book first.")
    data = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    cfg.update({k: v for k, v in data.items() if v is not None})
    # The frameworks lock US Letter and 1 inch margins; book.yaml keeps the same keys for KDP
    cfg["trim_width_in"] = float(data.get("docx_trim_width_in", 8.5))
    cfg["trim_height_in"] = float(data.get("docx_trim_height_in", 11.0))
    cfg["margin_in"] = float(data.get("docx_margin_in", 1.0))
    cfg["heading_style"] = int(cfg.get("heading_style", 1))
    return cfg


def is_chapter(text: str) -> bool:
    """Chapter or Part headings (e.g. 'Chapter 3: ...', 'Part 2 - ...', 'Kapitel 4: ...')."""
    return bool(re.match(rf"^\s*{CHAPTER_WORDS}\s+(\d+|[IVXLC]+)\b", text, flags=re.I))


def h1_is_chapter(p_el) -> bool:
    text = para_text(p_el).strip()
    prev = p_el.getprevious()
    return (is_chapter(text) or bool(CHAPTER_WORDS_NUM.match(text))
            or (prev is not None and para_style(prev) == "ChapterNumber"))


def norm(text: str) -> str:
    return re.sub(r"[^0-9a-zÀ-ɏ]", "", text.lower())


def word_count(text: str) -> int:
    return len(re.findall(r"[^\W_]+(?:['’-][^\W_]+)*", text))


def soffice_pdf(docx_path: Path, out_dir: Path) -> Path:
    exe = shutil.which("soffice") or shutil.which("libreoffice")
    if not exe:
        die("LibreOffice (soffice) not found; it is needed for the PDF test copy.")
    out_dir.mkdir(parents=True, exist_ok=True)
    run([exe, "--headless", "--convert-to", "pdf", "--outdir", str(out_dir), str(docx_path)])
    return out_dir / (docx_path.stem + ".pdf")


def pdf_texts(pdf: Path):
    from pypdf import PdfReader
    return [(p.extract_text() or "") for p in PdfReader(str(pdf)).pages]


# ------------------------------------------------------------ XML style helpers
def set_rfonts(rpr, name=FONT):
    rf = rpr.find(qn("w:rFonts"))
    if rf is None:
        rf = OxmlElement("w:rFonts")
        rpr.insert(0, rf)
    for a in ("w:ascii", "w:hAnsi", "w:eastAsia", "w:cs"):
        rf.set(qn(a), name)
    for a in ("w:asciiTheme", "w:hAnsiTheme", "w:eastAsiaTheme", "w:cstheme"):
        if rf.get(qn(a)) is not None:
            del rf.attrib[qn(a)]


def style_font(style, size=12, bold=None, italic=None, color=None, caps=None):
    style.font.name = FONT
    set_rfonts(style.element.get_or_add_rPr())
    style.font.size = Pt(size)
    if bold is not None:
        style.font.bold = bold
    if italic is not None:
        style.font.italic = italic
    if caps is not None:
        style.font.all_caps = caps
    style.font.color.rgb = RGBColor.from_string(color) if color else None
    if color is None:
        rpr = style.element.get_or_add_rPr()
        c = rpr.find(qn("w:color"))
        if c is not None:
            rpr.remove(c)


def para_props(style, align=None, before=0, after=6, line=1.15, keep_next=None, page_break=None,
               left=None, right=None, first=None, widow=True):
    pf = style.paragraph_format
    if align is not None:
        pf.alignment = align
    pf.space_before = Pt(before)
    pf.space_after = Pt(after)
    pf.line_spacing = line
    if keep_next is not None:
        pf.keep_with_next = keep_next
    if page_break is not None:
        pf.page_break_before = page_break
    if left is not None:
        pf.left_indent = Inches(left)
    if right is not None:
        pf.right_indent = Inches(right)
    if first is not None:
        pf.first_line_indent = Inches(first)
    pf.widow_control = widow


def ppr_of(style):
    return style.element.get_or_add_pPr()


def clear_ppr_child(style, tag):
    ppr = ppr_of(style)
    for el in ppr.findall(qn(tag)):
        ppr.remove(el)


def set_borders(style, top=None, bottom=None, left=None, right=None, box=None, color="000000"):
    """Each value is eighths of a point (e.g. 4 = 0.5pt, 16 = 2pt) or None."""
    clear_ppr_child(style, "w:pBdr")
    sides = {"top": top, "left": left, "bottom": bottom, "right": right}
    if box is not None:
        sides = {k: box for k in sides}
    if not any(sides.values()):
        return
    pbdr = OxmlElement("w:pBdr")
    for side in ("top", "left", "bottom", "right"):
        v = sides[side]
        if v:
            el = OxmlElement(f"w:{side}")
            el.set(qn("w:val"), "single")
            el.set(qn("w:sz"), str(v))
            el.set(qn("w:space"), "4")
            el.set(qn("w:color"), color)
            pbdr.append(el)
    ppr_of(style).append(pbdr)


def set_shading(style, fill):
    clear_ppr_child(style, "w:shd")
    if fill:
        shd = OxmlElement("w:shd")
        shd.set(qn("w:val"), "clear")
        shd.set(qn("w:color"), "auto")
        shd.set(qn("w:fill"), fill)
        ppr_of(style).append(shd)


def set_tabs(style, positions):
    clear_ppr_child(style, "w:tabs")
    tabs = OxmlElement("w:tabs")
    for pos, kind, leader in positions:
        t = OxmlElement("w:tab")
        t.set(qn("w:val"), kind)
        t.set(qn("w:leader"), leader)
        t.set(qn("w:pos"), str(pos))
        tabs.append(t)
    ppr_of(style).append(tabs)


def get_style(doc, name, base="Normal"):
    for existing in doc.styles:
        if existing.name == name:
            return existing
    else:
        s = doc.styles.add_style(name, WD_STYLE_TYPE.PARAGRAPH)
        try:
            s.base_style = doc.styles[base]
        except KeyError:
            pass
        return s


def apply_h1_look(style, n, accent):
    """Heading 1 treatment for heading style n (1-7)."""
    for tag in ("w:pBdr", "w:shd", "w:ind"):
        clear_ppr_child(style, tag)
    pf = style.paragraph_format
    pf.page_break_before = True
    pf.keep_with_next = True
    if n == 1:      # Black Banner
        style_font(style, 20, True, False, "FFFFFF", True)
        para_props(style, WD_ALIGN_PARAGRAPH.CENTER, 24, 18, 1.15, True, True)
        set_shading(style, "000000")
    elif n == 2:    # Rule Line
        style_font(style, 20, True, False, "000000", True)
        para_props(style, WD_ALIGN_PARAGRAPH.CENTER, 24, 18, 1.15, True, True)
        set_borders(style, bottom=16)
    elif n == 3:    # Numbered Block
        style_font(style, 20, True, False, "000000", False)
        para_props(style, WD_ALIGN_PARAGRAPH.LEFT, 6, 18, 1.15, True, True)
    elif n == 4:    # Centered Classic
        style_font(style, 22, True, False, "000000", False)
        para_props(style, WD_ALIGN_PARAGRAPH.CENTER, 24, 18, 1.15, True, True)
    elif n == 5:    # Shaded Bar
        style_font(style, 18, True, False, "404040", True)
        para_props(style, WD_ALIGN_PARAGRAPH.LEFT, 24, 18, 1.15, True, True)
        set_shading(style, "D9D9D9")
    elif n == 6:    # Underline Accent
        style_font(style, 20, True, False, "000000", False)
        para_props(style, WD_ALIGN_PARAGRAPH.LEFT, 24, 18, 1.15, True, True)
        set_borders(style, bottom=24, color=accent)
    else:           # Minimal Modern
        style_font(style, 20, True, False, "000000", False)
        para_props(style, WD_ALIGN_PARAGRAPH.LEFT, 72, 24, 1.15, True, True)


def apply_h2_look(style, n, accent):
    for tag in ("w:pBdr", "w:shd"):
        clear_ppr_child(style, tag)
    style_font(style, 14, True, n == 4, "000000", False)
    align = WD_ALIGN_PARAGRAPH.CENTER if n == 4 else WD_ALIGN_PARAGRAPH.LEFT
    para_props(style, align, 18, 6, 1.15, True, False)
    if n == 2:
        set_borders(style, bottom=4)
    if n == 3:
        style.font.small_caps = True


def apply_callout_look(style, n, accent):
    for tag in ("w:pBdr", "w:shd", "w:ind"):
        clear_ppr_child(style, tag)
    style_font(style, 12)
    para_props(style, WD_ALIGN_PARAGRAPH.LEFT, 6, 6, 1.15, False, False, widow=True)
    grey = "F2F2F2"
    if n == 1:
        set_borders(style, box=4, color="808080"); set_shading(style, grey)
    elif n == 2:
        set_borders(style, left=24, color=accent)
        style.paragraph_format.left_indent = Inches(0.15)
    elif n == 3:
        set_borders(style, box=4, color="000000")
    elif n == 4:
        set_borders(style, top=2, bottom=2, color="000000")
    elif n == 5:
        set_shading(style, grey)
    elif n == 6:
        set_borders(style, bottom=6, color="000000")
    else:
        style.paragraph_format.left_indent = Inches(0.4)
        style.paragraph_format.right_indent = Inches(0.4)


# ------------------------------------------------------------- reference doc
def build_reference(cfg, out: Path):
    data = run(["pandoc", "--print-default-data-file", "reference.docx"], binary=True)
    out.write_bytes(data)
    doc = Document(str(out))
    n = cfg["heading_style"]
    accent = str(cfg["accent"]).lstrip("#")

    sec = doc.sections[0]
    sec.page_width = Inches(cfg["trim_width_in"])
    sec.page_height = Inches(cfg["trim_height_in"])
    for side in ("left_margin", "right_margin", "top_margin", "bottom_margin"):
        setattr(sec, side, Inches(cfg["margin_in"]))
    sec.header_distance = Inches(0.5)
    sec.footer_distance = Inches(0.5)

    st = doc.styles
    # document defaults -> Times New Roman 12
    rpr_default = st.element.find(qn("w:docDefaults"))
    if rpr_default is not None:
        rpr = rpr_default.find(".//" + qn("w:rPr"))
        if rpr is not None:
            set_rfonts(rpr)
            for tag in ("w:sz", "w:szCs"):
                el = rpr.find(qn(tag))
                if el is None:
                    el = OxmlElement(tag); rpr.append(el)
                el.set(qn("w:val"), "24")

    # body styles
    for name in ("Normal", "Body Text", "First Paragraph"):
        s = get_style(doc, name)
        style_font(s, 12)
        para_props(s, WD_ALIGN_PARAGRAPH.JUSTIFY, 0, 6, 1.15)
    for name in ("Compact", "Block Text", "Definition", "Definition Term", "Footnote Text", "Bibliography"):
        try:
            s = st[name]
        except KeyError:
            continue
        style_font(s, 12)
        para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 0, 3, 1.0)
    s = get_style(doc, "Table Caption")
    style_font(s, 12, True, False)
    para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 12, 6, 1.0, True)
    for name in ("Image Caption", "Caption"):
        s = get_style(doc, name)
        style_font(s, 12, False, True)
        para_props(s, WD_ALIGN_PARAGRAPH.CENTER, 4, 12, 1.0)
    for name in ("Figure", "Captioned Figure"):
        s = get_style(doc, name)
        style_font(s, 12)
        para_props(s, WD_ALIGN_PARAGRAPH.CENTER, 6, 4, 1.0, True)
    for name in ("List Paragraph",):
        s = get_style(doc, name)
        style_font(s, 12)
        para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 0, 4, 1.15)

    # headings
    h1 = get_style(doc, "Heading 1"); apply_h1_look(h1, n, accent)
    h2 = get_style(doc, "Heading 2"); apply_h2_look(h2, n, accent)
    for k in range(3, 10):
        try:
            s = st[f"Heading {k}"]
            style_font(s, 12, True, False, "000000")
        except KeyError:
            pass

    # custom styles
    fh = get_style(doc, "Front Heading", "Heading 1"); apply_h1_look(fh, n, accent)
    ppr = ppr_of(fh)
    for el in ppr.findall(qn("w:outlineLvl")):
        ppr.remove(el)
    th = get_style(doc, "TOC Heading", "Heading 1"); apply_h1_look(th, n, accent)
    for el in ppr_of(th).findall(qn("w:outlineLvl")):
        ppr_of(th).remove(el)
    cn = get_style(doc, "Chapter Number")
    style_font(cn, 40, True, False, accent)
    para_props(cn, WD_ALIGN_PARAGRAPH.LEFT, 24, 0, 1.0, True, True)

    s = get_style(doc, "Front Title"); style_font(s, 48, True, False, "000000", n in (1, 2, 5))
    para_props(s, WD_ALIGN_PARAGRAPH.CENTER, 120, 18, 1.0)
    s = get_style(doc, "Front Subtitle"); style_font(s, 20, False, True)
    para_props(s, WD_ALIGN_PARAGRAPH.CENTER, 6, 18, 1.0)
    s = get_style(doc, "Front Author"); style_font(s, 14)
    para_props(s, WD_ALIGN_PARAGRAPH.CENTER, 150, 6, 1.0)
    s = get_style(doc, "Front Publisher"); style_font(s, 12)
    para_props(s, WD_ALIGN_PARAGRAPH.CENTER, 90, 0, 1.0)
    s = get_style(doc, "Copyright Start"); style_font(s, 12)
    para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 0, 6, 1.0, False, True)
    s = get_style(doc, "Copyright Text"); style_font(s, 12)
    para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 0, 6, 1.0)
    s = get_style(doc, "Front Body", "Normal"); style_font(s, 12)
    para_props(s, WD_ALIGN_PARAGRAPH.JUSTIFY, 0, 6, 1.15)
    for name, left in (("TOC 1", 0.0), ("TOC 2", 0.3)):
        s = get_style(doc, name)
        style_font(s, 12, name == "TOC 1")
        para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 4 if name == "TOC 1" else 0, 2, 1.0, left=left)
        set_tabs(s, [(CONTENT_TWIPS, "right", "dot")])
    s = get_style(doc, "Index Entry"); style_font(s, 12)
    para_props(s, WD_ALIGN_PARAGRAPH.LEFT, 0, 2, 1.0)
    set_tabs(s, [(CONTENT_TWIPS, "right", "dot")])
    c = get_style(doc, "Callout"); apply_callout_look(c, n, accent)
    c.font.size = Pt(12)
    doc.save(str(out))


# --------------------------------------------------------- markdown assembly
def pandoc_from(cfg):
    lang = str(cfg["language"]).lower()
    return "markdown+smart" if lang.startswith("en") else "markdown-smart"


def render_svgs(md: str, book_dir: Path, tmp: Path) -> str:
    """Replace SVG image references by 300 dpi PNG renders (SVG source stays in images/)."""
    pattern = re.compile(r"!\[([^\]]*)\]\(([^)\s]+\.svg)\)(\{[^}]*\})?", re.I)
    found = pattern.findall(md)
    if not found:
        return md
    from playwright.sync_api import sync_playwright
    out_dir = tmp / "_svg"
    out_dir.mkdir(exist_ok=True)
    done = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for _cap, rel, _attr in found:
            if rel in done:
                continue
            src = (book_dir / rel).resolve()
            if not src.exists():
                continue
            page = browser.new_page(viewport={"width": 1950, "height": 1200})
            page.goto(src.as_uri())
            page.wait_for_load_state("load")
            dims = page.evaluate("""() => { const s=document.querySelector('svg'); if(!s) return null;
                const b=s.getBoundingClientRect(); return [b.width,b.height]; }""")
            if not dims or not dims[0]:
                page.close(); continue
            scale = 1950 / dims[0]
            png = out_dir / (Path(rel).stem + ".png")
            page.close()
            page = browser.new_page(viewport={"width": int(dims[0]), "height": int(dims[1])},
                                    device_scale_factor=scale)
            page.goto(src.as_uri())
            page.wait_for_load_state("load")
            page.screenshot(path=str(png))
            page.close()
            done[rel] = png
        browser.close()

    def sub(m):
        cap, rel, attr = m.group(1), m.group(2), m.group(3)
        png = done.get(rel)
        if not png:
            return m.group(0)
        return f"![{cap}]({png}){attr or '{width=6.5in}'}"
    return pattern.sub(sub, md)


def add_default_image_width(md: str) -> str:
    return re.sub(r"(!\[[^\]]*\]\([^)\s]+\))(?!\{)", r"\1{width=6.5in}", md)


def front_as_markdown(path: Path) -> str:
    """Front-matter files start with '# Title'; render that title in the Front Heading style."""
    text = path.read_text(encoding="utf-8").strip()
    m = re.match(r"#\s+(.+)\n", text)
    if m:
        text = f'::: {{custom-style="Front Heading"}}\n{m.group(1).strip()}\n:::\n\n' + text[m.end():]
    return text


def disclaimer_for(cfg) -> str:
    profile = cfg.get("profile", "engineering")
    base = ("This book is provided for educational and informational purposes. The author and publisher "
            "have made every effort to ensure the accuracy of the content at the time of writing, but "
            "make no warranty of any kind and accept no liability for any loss or damage arising from its use.")
    if profile == "medical":
        return (base + " This book is educational reference material and is not a substitute for professional "
                "medical advice, diagnosis, or treatment. Consult a qualified health professional about any "
                "personal medical decision. Anyone experiencing a medical emergency should contact local "
                "emergency services immediately. Never start, stop, or change a medicine without advice from a clinician.")
    if profile == "engineering":
        return (base + " Engineering calculations, standards, and design procedures must be independently "
                "verified by a qualified professional before they are used in any design, construction, "
                "or safety-critical decision.")
    return base


def build_front_md(cfg) -> str:
    n = cfg["heading_style"]
    title = cfg["title"].upper() if n in (1, 2, 5) else cfg["title"]
    parts = [f'::: {{custom-style="Front Title"}}\n{title}\n:::\n']
    if cfg.get("subtitle"):
        parts.append(f'::: {{custom-style="Front Subtitle"}}\n{cfg["subtitle"]}\n:::\n')
    if cfg.get("author"):
        parts.append(f'::: {{custom-style="Front Author"}}\n{cfg["author"]}\n:::\n')
    if cfg.get("publisher"):
        parts.append(f'::: {{custom-style="Front Publisher"}}\n{cfg["publisher"]}\n:::\n')
    author = cfg.get("author") or "the author"
    cr = [f'Copyright © {cfg["copyright_year"]} {author}. All rights reserved.',
          cfg["copyright_text"] or "No part of this publication may be reproduced, stored in a retrieval system, "
          "or transmitted in any form or by any means without the prior written permission of the copyright owner, "
          "except for brief quotations in critical reviews.",
          disclaimer_for(cfg)]
    if cfg.get("isbn"):
        cr.append(f'ISBN: {cfg["isbn"]}')
    parts.append(f'::: {{custom-style="Copyright Start"}}\n{cr[0]}\n:::\n')
    for t in cr[1:]:
        parts.append(f'::: {{custom-style="Copyright Text"}}\n{t}\n:::\n')
    return "\n".join(parts)


def read_md_dir(d: Path, pattern="*.md"):
    return sorted(d.glob(pattern)) if d.exists() else []


# ------------------------------------------------------------- post-processing
def body_el(doc):
    return doc.element.body


def strip_links_and_bookmarks(doc):
    body = body_el(doc)
    for h in list(body.iter(qn("w:hyperlink"))):
        parent = h.getparent()
        idx = parent.index(h)
        for child in list(h):
            parent.insert(idx, child)
            idx += 1
        parent.remove(h)
    for tag in ("w:bookmarkStart", "w:bookmarkEnd"):
        for el in list(body.iter(qn(tag))):
            el.getparent().remove(el)
    for run_el in body.iter(qn("w:rStyle")):
        if run_el.get(qn("w:val")) == "Hyperlink":
            run_el.getparent().remove(run_el)
    # drop hyperlink relationships
    part = doc.part
    for rid, rel in list(part.rels.items()):
        if rel.reltype.endswith("/hyperlink") or rel.reltype.endswith("/comments"):
            del part.rels[rid]


def fix_tables(doc):
    for tbl in body_el(doc).iter(qn("w:tbl")):
        tblPr = tbl.find(qn("w:tblPr"))
        if tblPr is None:
            tblPr = OxmlElement("w:tblPr"); tbl.insert(0, tblPr)
        for tag in ("w:tblW", "w:tblInd", "w:tblLayout", "w:tblBorders", "w:tblCellMar", "w:jc"):
            for el in tblPr.findall(qn(tag)):
                tblPr.remove(el)
        tblW = OxmlElement("w:tblW"); tblW.set(qn("w:w"), str(CONTENT_TWIPS)); tblW.set(qn("w:type"), "dxa")
        tblInd = OxmlElement("w:tblInd"); tblInd.set(qn("w:w"), "0"); tblInd.set(qn("w:type"), "dxa")
        layout = OxmlElement("w:tblLayout"); layout.set(qn("w:type"), "fixed")
        borders = parse_xml(
            f'<w:tblBorders {nsdecls("w")}>'
            + "".join(f'<w:{s} w:val="single" w:sz="4" w:space="0" w:color="808080"/>'
                      for s in ("top", "left", "bottom", "right", "insideH", "insideV"))
            + "</w:tblBorders>")
        mar = parse_xml(
            f'<w:tblCellMar {nsdecls("w")}><w:left w:w="100" w:type="dxa"/>'
            f'<w:right w:w="100" w:type="dxa"/></w:tblCellMar>')
        look = tblPr.find(qn("w:tblLook"))
        for el in (tblW, tblInd, borders, layout, mar):
            if look is not None:
                look.addprevious(el)
            else:
                tblPr.append(el)
        # grid: scale existing widths to exactly 6.5 in
        grid = tbl.find(qn("w:tblGrid"))
        cols = grid.findall(qn("w:gridCol")) if grid is not None else []
        if cols:
            widths = [int(c.get(qn("w:w")) or 0) for c in cols]
            total = sum(widths) or len(cols)
            if not sum(widths):
                widths = [1] * len(cols)
            new = [int(round(w * CONTENT_TWIPS / total)) for w in widths]
            new[-1] += CONTENT_TWIPS - sum(new)
            for c, w in zip(cols, new):
                c.set(qn("w:w"), str(w))
            for tr in tbl.findall(qn("w:tr")):
                for tc, w in zip(tr.findall(qn("w:tc")), new):
                    tcPr = tc.find(qn("w:tcPr"))
                    if tcPr is None:
                        tcPr = OxmlElement("w:tcPr"); tc.insert(0, tcPr)
                    for el in tcPr.findall(qn("w:tcW")):
                        tcPr.remove(el)
                    tcW = OxmlElement("w:tcW"); tcW.set(qn("w:w"), str(w)); tcW.set(qn("w:type"), "dxa")
                    tcPr.insert(0, tcW)
        rows = tbl.findall(qn("w:tr"))
        for i, tr in enumerate(rows):
            trPr = tr.find(qn("w:trPr"))
            if trPr is None:
                trPr = OxmlElement("w:trPr"); tr.insert(0, trPr)
            if trPr.find(qn("w:cantSplit")) is None:
                trPr.append(OxmlElement("w:cantSplit"))
            if i == 0 and trPr.find(qn("w:tblHeader")) is None:
                trPr.append(OxmlElement("w:tblHeader"))
            if i == 0:
                for r in tr.iter(qn("w:r")):
                    rPr = r.find(qn("w:rPr"))
                    if rPr is None:
                        rPr = OxmlElement("w:rPr"); r.insert(0, rPr)
                    if rPr.find(qn("w:b")) is None:
                        b_el = OxmlElement("w:b")
                        anchor = rPr.find(qn("w:rFonts"))
                        if anchor is None:
                            anchor = rPr.find(qn("w:rStyle"))
                        if anchor is not None:
                            anchor.addnext(b_el)
                        else:
                            rPr.insert(0, b_el)
        # one 12 pt line of space after the table (paragraph spacing, not an empty paragraph)
        nxt = tbl.getnext()
        if nxt is not None and nxt.tag == qn("w:p"):
            ppr = nxt.find(qn("w:pPr"))
            if ppr is None:
                ppr = OxmlElement("w:pPr"); nxt.insert(0, ppr)
            for el in ppr.findall(qn("w:spacing")):
                ppr.remove(el)
            sp = OxmlElement("w:spacing"); sp.set(qn("w:before"), "240")
            after_tags = ("w:ind", "w:contextualSpacing", "w:mirrorIndents", "w:jc", "w:textAlignment",
                          "w:outlineLvl", "w:rPr", "w:sectPr")
            anchor = next((c for c in ppr if c.tag in [qn(t) for t in after_tags]), None)
            if anchor is not None:
                anchor.addprevious(sp)
            else:
                ppr.append(sp)


def para_style(p_el):
    ppr = p_el.find(qn("w:pPr"))
    if ppr is None:
        return ""
    ps = ppr.find(qn("w:pStyle"))
    return ps.get(qn("w:val")) if ps is not None else ""


def para_text(p_el):
    return "".join(t.text or "" for t in p_el.iter(qn("w:t")))


def apply_dropcaps(doc, n_style):
    """Insert a Word 'Dropped' drop cap (3 lines) on the first body paragraph of every chapter."""
    count, problems = 0, []
    body = body_el(doc)
    h1s = [p for p in body.findall(qn("w:p")) if para_style(p) == "Heading1" and h1_is_chapter(p)]
    for h in h1s:
        el = h.getnext()
        target = None
        while el is not None:
            if el.tag == qn("w:p") and para_style(el) == "Heading1":
                break
            if el.tag == qn("w:p") and para_style(el) in ("FirstParagraph", "BodyText") \
                    and el.find(qn("w:pPr")) is not None and el.find(".//" + qn("w:numPr")) is None \
                    and para_text(el).strip():
                target = el
                break
            el = el.getnext()
        if target is None:
            problems.append(f"No body paragraph found for drop cap after heading: {para_text(h)[:50]}")
            continue
        runs = [r for r in target.findall(qn("w:r")) if r.find(qn("w:t")) is not None]
        if not runs:
            problems.append(f"Could not place drop cap in: {para_text(target)[:40]}")
            continue
        t_el = runs[0].find(qn("w:t"))
        txt = t_el.text or ""
        k = 0
        while k < len(txt) and not txt[k].isalpha():
            k += 1
        if k >= len(txt):
            problems.append(f"First body paragraph does not begin with a letter: {para_text(target)[:40]}")
            continue
        letter = txt[k]
        t_el.text = txt[k + 1:]
        t_el.set("{http://www.w3.org/XML/1998/namespace}space", "preserve")
        # exact line height of 3 body lines (12pt TNR at 1.15 ~ 15.9pt) -> 3 x 15.9pt
        line = 954
        cap = parse_xml(
            f'<w:p {nsdecls("w")}><w:pPr><w:keepNext/>'
            f'<w:framePr w:dropCap="drop" w:lines="3" w:wrap="around" w:vAnchor="text" w:hAnchor="text"/>'
            f'<w:spacing w:before="0" w:after="0" w:line="{line}" w:lineRule="exact"/>'
            f'<w:textAlignment w:val="baseline"/></w:pPr>'
            f'<w:r><w:rPr><w:rFonts w:ascii="{FONT}" w:hAnsi="{FONT}" w:cs="{FONT}"/>'
            f'<w:position w:val="-9"/><w:sz w:val="110"/><w:szCs w:val="110"/></w:rPr>'
            f'<w:t>{letter}</w:t></w:r></w:p>')
        target.addprevious(cap)
        count += 1
    return count, problems


def set_pgnum(sect, fmt=None, start=None):
    """Add w:pgNumType in schema order (directly after w:pgMar, before w:cols)."""
    for el in sect.findall(qn("w:pgNumType")):
        sect.remove(el)
    pg = OxmlElement("w:pgNumType")
    if fmt:
        pg.set(qn("w:fmt"), fmt)
    if start:
        pg.set(qn("w:start"), str(start))
    anchor = sect.find(qn("w:pgMar"))
    if anchor is not None:
        anchor.addnext(pg)
    else:
        sect.append(pg)


def sect_xml(doc, fmt=None, start=None, footer=False):
    base = copy.deepcopy(body_el(doc).find(qn("w:sectPr")))
    for tag in ("w:footerReference", "w:headerReference", "w:pgNumType", "w:titlePg", "w:type"):
        for el in base.findall(qn(tag)):
            base.remove(el)
    if fmt or start:
        set_pgnum(base, fmt, start)
    return base


def add_page_footer(section):
    footer = section.footer
    footer.is_linked_to_previous = False
    for p in list(footer.paragraphs):
        p._p.getparent().remove(p._p)
    p = footer.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    fld = parse_xml(
        f'<w:fldSimple {nsdecls("w")} w:instr="PAGE"><w:r><w:rPr><w:rFonts w:ascii="{FONT}" '
        f'w:hAnsi="{FONT}" w:cs="{FONT}"/><w:sz w:val="24"/></w:rPr><w:t>1</w:t></w:r></w:fldSimple>')
    p._p.append(fld)


def apply_sections(doc, book_mode):
    body = body_el(doc)
    ps = [p for p in body.findall(qn("w:p"))]
    final = body.find(qn("w:sectPr"))
    # Final section: Arabic numbering from 1 with a footer page number
    for el in final.findall(qn("w:pgNumType")):
        final.remove(el)
    if not book_mode:
        set_pgnum(final, None, 1)
        add_page_footer(doc.sections[-1])
        return
    last_copy = None
    for p in ps:
        if para_style(p) in ("CopyrightText", "CopyrightStart"):
            last_copy = p
    first_chapter = next((p for p in ps if para_style(p) == "Heading1"), None)
    before_ch = first_chapter.getprevious() if first_chapter is not None else None
    marks = []
    if last_copy is not None:
        marks.append((last_copy, sect_xml(doc)))
    if before_ch is not None and before_ch is not last_copy:
        marks.append((before_ch, sect_xml(doc, "lowerRoman", 3)))
    for p_el, sp in marks:
        if p_el.tag != qn("w:p"):
            continue
        ppr = p_el.find(qn("w:pPr"))
        if ppr is None:
            ppr = OxmlElement("w:pPr"); p_el.insert(0, ppr)
        ppr.append(sp)
    set_pgnum(final, "decimal", 1)
    secs = doc.sections
    for i, s in enumerate(secs):
        if i == 0 and len(secs) > 1 and last_copy is not None:
            continue  # title + copyright pages: no visible page number
        add_page_footer(s)


def collect_headings(doc):
    out = []
    in_body = False
    for p in body_el(doc).findall(qn("w:p")):
        sty = para_style(p)
        if sty == "Heading1":
            in_body = True
            out.append((1, para_text(p).strip()))
        elif sty == "Heading2" and in_body:
            out.append((2, para_text(p).strip()))
    return out


def fill_placeholder(doc, marker, entries, style_for):
    """Replace a placeholder paragraph with static entries; entries = [(level, text, page)]."""
    body = body_el(doc)
    ph = next((p for p in body.findall(qn("w:p")) if para_text(p).strip() == marker), None)
    if ph is None:
        return False
    for level, text, page in entries:
        p = parse_xml(
            f'<w:p {nsdecls("w")}><w:pPr><w:pStyle w:val="{style_for(level)}"/></w:pPr>'
            f'<w:r><w:t xml:space="preserve"></w:t></w:r></w:p>')
        runs = p.findall(qn("w:r"))
        runs[0].find(qn("w:t")).text = text
        tab = OxmlElement("w:r"); tab.append(OxmlElement("w:tab"))
        p.append(tab)
        r = OxmlElement("w:r"); t = OxmlElement("w:t"); t.text = str(page); r.append(t)
        p.append(r)
        ph.addprevious(p)
    ph.getparent().remove(ph)
    return True


def split_number_heading(doc):
    """Heading style 3: show the chapter number as a separate oversized number."""
    pat = re.compile(rf"^{CHAPTER_WORDS}\s+(\d+)\s*[:.\-–—]\s*(.+)$", re.I)
    for p in body_el(doc).findall(qn("w:p")):
        if para_style(p) != "Heading1":
            continue
        m = pat.match(para_text(p).strip())
        if not m:
            continue
        ts = list(p.iter(qn("w:t")))
        ts[0].text = m.group(3)
        for extra in ts[1:]:
            extra.text = ""
        nump = parse_xml(
            f'<w:p {nsdecls("w")}><w:pPr><w:pStyle w:val="ChapterNumber"/><w:pageBreakBefore/></w:pPr>'
            f'<w:r><w:t>{m.group(1).upper()} {m.group(2)}</w:t></w:r></w:p>')
        p.addprevious(nump)
        ppr = p.find(qn("w:pPr"))
        pb = OxmlElement("w:pageBreakBefore"); pb.set(qn("w:val"), "0")
        ppr.append(pb)


def postprocess(docx_path: Path, cfg, book_mode, toc_entries=None, index_entries=None):
    doc = Document(str(docx_path))
    strip_links_and_bookmarks(doc)
    fix_tables(doc)
    if cfg["heading_style"] == 3:
        split_number_heading(doc)
    if book_mode:
        heads = collect_headings(doc)
        entries = toc_entries or [(lvl, txt, "000") for lvl, txt in heads]
        fill_placeholder(doc, "@@TOC@@", entries, lambda lvl: "TOC1" if lvl == 1 else "TOC2")
        if index_entries is not None:
            fill_placeholder(doc, "@@INDEX@@", index_entries, lambda lvl: "IndexEntry")
    dc, problems = apply_dropcaps(doc, cfg["heading_style"])
    apply_sections(doc, book_mode)
    doc.core_properties.title = cfg["title"]
    doc.core_properties.author = cfg.get("author") or ""
    doc.core_properties.comments = ""
    doc.save(str(docx_path))
    return dc, problems, doc


# ------------------------------------------------------------------ pagination
def body_start_index(texts):
    for i, t in enumerate(texts):
        lines = [ln.strip() for ln in t.splitlines() if ln.strip()]
        if lines and lines[-1] == "1" and i > 0:
            return i
    return None


def find_heading_pages(texts, headings, start):
    pages, cur = [], start
    for _lvl, txt in headings:
        key = norm(txt)
        hit = None
        for i in range(cur, len(texts)):
            if key and key in norm(texts[i]):
                hit = i
                break
        if hit is None:
            pages.append("")
        else:
            pages.append(hit - start + 1)
            cur = hit
    return pages


def index_pages(texts, terms, start, end):
    out = []
    for term in terms:
        key = norm(term)
        hits = [str(i - start + 1) for i in range(start, end) if key and key in norm(texts[i])]
        out.append((1, term, ", ".join(hits[:12]) if hits else "-"))
    return out


# ------------------------------------------------------------------------ build
def run_pandoc(md_path: Path, out: Path, ref: Path, cfg, book_dir: Path):
    cmd = ["pandoc", str(md_path), "-f", pandoc_from(cfg), "-o", str(out), "--reference-doc", str(ref),
           "--resource-path", str(book_dir), "-M", f"lang={cfg['language']}"]
    run(cmd, cwd=book_dir)


def build_one(md_text, cfg, book_dir, out_docx: Path, book_mode, toc_entries=None, index_entries=None):
    with tempfile.TemporaryDirectory() as td:
        td = Path(td)
        ref = td / "reference.docx"
        build_reference(cfg, ref)
        md_text = render_svgs(md_text, book_dir, td)
        md_text = add_default_image_width(md_text)
        mdf = td / "in.md"
        mdf.write_text(md_text, encoding="utf-8")
        run_pandoc(mdf, out_docx, ref, cfg, book_dir)
    return postprocess(out_docx, cfg, book_mode, toc_entries, index_entries)


def qc(docx_path: Path, cfg=None, expected_chapters=None, floor=None, ceiling=None, image_count=None,
       pdf_path: Path = None, quiet=False):
    """Run the framework's automatic checks. Returns (problems, info)."""
    cfg = cfg or dict(DEFAULTS)
    problems, info = [], {}
    doc = Document(str(docx_path))
    body = body_el(doc)

    for i, s in enumerate(doc.sections):
        dims = (round(s.page_width.inches, 2), round(s.page_height.inches, 2))
        mar = tuple(round(x.inches, 2) for x in (s.left_margin, s.right_margin, s.top_margin, s.bottom_margin))
        if dims != (8.5, 11.0):
            problems.append(f"Section {i + 1}: page size {dims} is not US Letter 8.5 x 11 in.")
        if mar != (1.0, 1.0, 1.0, 1.0):
            problems.append(f"Section {i + 1}: margins {mar} are not exactly 1 in.")

    with zipfile.ZipFile(docx_path) as z:
        names = z.namelist()
        xml = z.read("word/document.xml").decode("utf8")
        rels = z.read("word/_rels/document.xml.rels").decode("utf8")
    if "w:hyperlink" in xml or "/hyperlink" in rels:
        problems.append("Hyperlinks or hyperlink relationships are present.")
    if "w:bookmarkStart" in xml:
        problems.append("Bookmarks are present.")
    if any("comments" in n for n in names):
        problems.append("A comments part is present.")
    if "<w:ins " in xml or "<w:del " in xml:
        problems.append("Tracked changes are present.")
    if 'w:dropCap="margin"' in xml:
        problems.append("A drop cap uses the In margin position; it must be Dropped.")

    chapters = [p for p in body.findall(qn("w:p")) if para_style(p) == "Heading1" and h1_is_chapter(p)]
    drops = xml.count('w:dropCap="drop"')
    info["chapters"] = len(chapters)
    info["dropcaps"] = drops
    if drops != len(chapters):
        problems.append(f"Drop caps: found {drops}, expected exactly one per chapter ({len(chapters)}).")
    if expected_chapters and len(chapters) != expected_chapters:
        problems.append(f"Chapter count {len(chapters)} differs from expected {expected_chapters}.")

    # text scans
    all_text = "\n".join(para_text(p) for p in body.iter(qn("w:p")))
    for pat, label in ((r"\[FIGURE", "[FIGURE] marker"), (r"\bTODO\b|\bTBD\b", "TODO/TBD"),
                       (r"lorem ipsum", "lorem ipsum"), (r"\[insert", "[insert ...] placeholder"),
                       (r"Error! Bookmark", "broken field"), (r"https?://|www\.|\bdoi:", "URL or DOI"),
                       (r"\\frac|\\sqrt|\$\$|\\begin\{", "visible LaTeX"),
                       (r"^\s*(References|Bibliography|Works Cited|Sources)\s*$", "reference list heading")):
        if re.search(pat, all_text, flags=re.I | re.M):
            problems.append(f"Found {label} in the manuscript text.")

    # equations / images
    info["equations"] = xml.count("<m:oMath>") + xml.count("<m:oMath ")
    info["images"] = xml.count("<pic:pic")
    if image_count is not None and info["images"] != image_count and image_count >= 0:
        problems.append(f"Figure count {info['images']} differs from the approved allocation {image_count}.")

    # tables
    tbls = list(body.iter(qn("w:tbl")))
    info["tables"] = len(tbls)
    for k, t in enumerate(tbls, 1):
        w = t.find(qn("w:tblPr") + "/" + qn("w:tblW"))
        ind = t.find(qn("w:tblPr") + "/" + qn("w:tblInd"))
        if w is None or w.get(qn("w:w")) != str(CONTENT_TWIPS):
            problems.append(f"Table {k}: width is not exactly 6.5 in.")
        if ind is None or ind.get(qn("w:w")) != "0":
            problems.append(f"Table {k}: indentation is not zero.")
        nxt = t.getnext()
        if nxt is not None and nxt.tag == qn("w:p"):
            sp = nxt.find(qn("w:pPr") + "/" + qn("w:spacing"))
            if sp is None or sp.get(qn("w:before")) != "240":
                problems.append(f"Table {k}: no 12 pt space after the table.")

    # fonts: direct run sizes / fonts on non-heading, non-front paragraphs
    big = 0
    for p in body.findall(qn("w:p")):
        sty = para_style(p)
        if sty.startswith(("Heading", "Front", "Chapter", "TOCHeading")) or p.find(".//" + qn("w:framePr")) is not None:
            continue
        for sz in p.iter(qn("w:sz")):
            if sz.get(qn("w:val")) not in (None, "24"):
                big += 1
        for rf in p.iter(qn("w:rFonts")):
            if rf.get(qn("w:ascii")) not in (None, FONT):
                big += 1
    if big:
        problems.append(f"{big} runs use a size other than 12 pt or a font other than Times New Roman.")

    # empty paragraphs used for spacing
    empties = 0
    MATH = "{http://schemas.openxmlformats.org/officeDocument/2006/math}oMath"
    for p in body.findall(qn("w:p")):
        if (not para_text(p).strip() and p.find(".//" + qn("w:drawing")) is None
                and p.find(".//" + MATH) is None and p.find(".//" + qn("w:sectPr")) is None
                and p.find(".//" + qn("w:br")) is None and p.find(".//" + qn("w:framePr")) is None):
            empties += 1
    if empties:
        problems.append(f"{empties} empty paragraphs found (spacing must use paragraph spacing).")

    # per-chapter word counts (prose, excluding tables)
    counts, cur, name = {}, 0, None
    for el in body:
        if el.tag == qn("w:tbl"):
            continue
        if el.tag == qn("w:p"):
            sty = para_style(el)
            txt = para_text(el)
            if sty == "Heading1":
                if name is not None:
                    counts[name] = cur
                if h1_is_chapter(el):
                    name, cur = txt.strip(), word_count(txt)
                else:
                    name = None
            elif name is not None and not sty.startswith(("TOC", "Index", "Front")):
                cur += word_count(txt)
    if name is not None:
        counts[name] = cur
    info["chapter_words"] = counts
    if floor:
        for ch, wc in counts.items():
            if wc < floor:
                problems.append(f"Chapter '{ch[:50]}' has {wc} words, below the floor of {floor}.")
            elif ceiling and wc > ceiling * 1.25:
                problems.append(f"Chapter '{ch[:50]}' has {wc} words, far above the {ceiling} guide.")

    if pdf_path and pdf_path.exists():
        from pypdf import PdfReader
        info["pdf_pages"] = len(PdfReader(str(pdf_path)).pages)
    if not quiet:
        print(f"QC for {docx_path.name}: {len(problems)} problem(s)")
        for p in problems:
            print(" - " + p)
        print("Info:", {k: v for k, v in info.items() if k != "chapter_words"})
        for ch, wc in counts.items():
            print(f"   {wc:>7} words  {ch[:70]}")
    return problems, info


# ---------------------------------------------------------------------- commands
def cmd_check(_):
    ok = True
    for tool in ("pandoc", "soffice"):
        found = shutil.which(tool) or (tool == "soffice" and shutil.which("libreoffice"))
        print(f"[{'OK' if found else 'MISSING'}] {tool}")
        ok &= bool(found)
    for mod in ("docx", "yaml", "pypdf", "playwright"):
        try:
            __import__(mod); print(f"[OK] python module {mod}")
        except ImportError:
            pipname = {"docx": "python-docx", "yaml": "pyyaml"}.get(mod, mod)
            print(f"[MISSING] python module {mod} -> pip install {pipname}"); ok = False
    print("\nAll good." if ok else "\nFix the MISSING items, then run check again.")
    sys.exit(0 if ok else 1)


def cmd_chapter(args):
    book_dir = Path(args.book).resolve()
    cfg = load_cfg(book_dir)
    md = (book_dir / args.chapter).resolve()
    if not md.exists():
        die(f"{md} not found")
    out_dir = book_dir / "previews"
    out_dir.mkdir(exist_ok=True)
    out = out_dir / f"{md.stem}.docx"
    dc, problems, _ = build_one(md.read_text(encoding="utf-8"), cfg, book_dir, out, book_mode=False)
    pdf = soffice_pdf(out, out_dir)
    probs, info = qc(out, cfg, expected_chapters=1, floor=None, pdf_path=pdf, quiet=True)
    probs += problems
    wc = sum(info.get("chapter_words", {}).values())
    print(f"Built {out.name} and {pdf.name} | {wc} words (excluding tables) | {info.get('pdf_pages')} pages")
    floor = cfg["chapter_word_floor"]
    if wc < floor:
        probs.append(f"Chapter has {wc} words, below the floor of {floor} (Stage 2.5).")
    print(f"QC: {len(probs)} problem(s)")
    for p in probs:
        print(" - " + p)


def cmd_book(args):
    book_dir = Path(args.book).resolve()
    cfg = load_cfg(book_dir)
    slug = book_dir.name
    final = book_dir / "final"
    final.mkdir(exist_ok=True)
    chapters = read_md_dir(book_dir / "chapters", "ch*.md")
    if not chapters:
        die("No chapters found in chapters/ (files like ch01-name.md).")
    parts = [build_front_md(cfg)]
    for f in read_md_dir(book_dir / "front"):
        parts.append(front_as_markdown(f))
    parts.append('::: {custom-style="TOC Heading"}\nContents\n:::\n\n@@TOC@@\n')
    for c in chapters:
        parts.append(c.read_text(encoding="utf-8").strip())
    for f in read_md_dir(book_dir / "back"):
        parts.append(f.read_text(encoding="utf-8").strip())
    terms_file = book_dir / "back" / "index-terms.txt"
    terms = []
    if terms_file.exists():
        terms = [t.strip() for t in terms_file.read_text(encoding="utf-8").splitlines() if t.strip()]
        parts = [p for p in parts]  # index terms file is not markdown content
    # drop an accidental index-terms .md; the .txt file is read separately
    if terms:
        parts.append("# Index\n\n@@INDEX@@\n")
    md_all = "\n\n".join(parts) + "\n"

    out = final / f"{slug}-manuscript.docx"
    toc_entries = idx_entries = None
    for attempt in range(3):
        build_one(md_all, cfg, book_dir, out, book_mode=True, toc_entries=toc_entries,
                  index_entries=idx_entries if terms else None)
        pdf = soffice_pdf(out, final)
        texts = pdf_texts(pdf)
        start = body_start_index(texts)
        if start is None:
            print("WARNING: could not find the first body page; TOC page numbers not computed.")
            break
        doc = Document(str(out))
        heads = collect_headings(doc)
        pages = find_heading_pages(texts, heads, start)
        new_toc = [(lvl, txt, pg) for (lvl, txt), pg in zip(heads, pages)]
        new_idx = None
        if terms:
            idx_page = next((i for i in range(start, len(texts)) if re.match(r"\s*Index\b", texts[i])), len(texts))
            new_idx = [(lvl, t, pg) for lvl, t, pg in index_pages(texts, terms, start, idx_page)]
        if new_toc == toc_entries and new_idx == idx_entries:
            break
        toc_entries, idx_entries = new_toc, new_idx
        # rebuild with real numbers (loop re-renders until numbers are stable)
    probs, info = qc(out, cfg, floor=cfg["chapter_word_floor"], ceiling=cfg["chapter_word_ceiling"],
                     image_count=cfg["image_count"] if cfg["image_count"] else None, pdf_path=pdf, quiet=True)
    lines = [f"# Quality-control report: {cfg['title']}", f"Date: {date.today().isoformat()}", "",
             f"- Chapters: {info['chapters']}", f"- Drop caps: {info['dropcaps']}",
             f"- Equations (native Word): {info['equations']}", f"- Figures: {info['images']}",
             f"- Tables: {info['tables']}", f"- PDF test copy pages (LibreOffice): {info.get('pdf_pages')}", "",
             "## Chapter word counts (excluding tables)"]
    lines += [f"- {w}: {c}" for c, w in info["chapter_words"].items()]
    lines += ["", "## Automatic checks"]
    lines += [f"- PROBLEM: {p}" for p in probs] or ["- All automatic checks passed."]
    lines += ["", "## Still needs a human",
              "- Open the DOCX in Microsoft Word, page through it, and check the contents-page numbers "
              "(they were computed from a LibreOffice rendering; Word can paginate slightly differently).",
              "- Confirm every drop cap sits inside the text area and every table sits inside the margins.",
              "- Clinical / technical clearance of the audit table, where the profile requires it."]
    (final / "qc-report.md").write_text("\n".join(lines), encoding="utf-8")
    print("\n".join(lines))


def cmd_qc(args):
    probs, _ = qc(Path(args.docx), floor=args.floor, expected_chapters=args.chapters)
    sys.exit(1 if probs else 0)


def main():
    if Document is None:
        print("Missing Python modules. Run: pip install python-docx pyyaml pypdf playwright")
    ap = argparse.ArgumentParser(description="Book Studio Word build tool (EMB/MEB house style)")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check").set_defaults(fn=cmd_check)
    c = sub.add_parser("chapter"); c.add_argument("book"); c.add_argument("chapter"); c.set_defaults(fn=cmd_chapter)
    b = sub.add_parser("book"); b.add_argument("book"); b.set_defaults(fn=cmd_book)
    q = sub.add_parser("qc"); q.add_argument("docx"); q.add_argument("--chapters", type=int)
    q.add_argument("--floor", type=int); q.set_defaults(fn=cmd_qc)
    a = ap.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
