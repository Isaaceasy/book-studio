#!/usr/bin/env python3
"""
pagedeco.py - page furniture for the KDP PDF (running headers, page numbers,
Part edge tabs). Used by bookbuild.py when book.yaml has `page_decor: true`.

How it works (plain language):
  1. Reads the finished interior PDF and finds the page where each Part opens.
     A Part opener page shows its label in capitals, for example "PART 3"
     (back-matter sections show "REFERENCE").
  2. Draws a transparent overlay page for every PDF page: running header,
     page number at the outer bottom corner, and a coloured tab on the outer
     edge. The current Part's tab is solid crimson with the Part number; the
     other tabs are pale, so the stepped tab column reads like the owner's
     reference books.
  3. Merges the overlay on top of the page with pypdf.
Pages with no text (intentional blanks) and the title and copyright pages get
no furniture. Part opener pages get the tab and page number but no header.
Everything stays inside the KDP no-bleed safe area (outside margin 0.25 in or
more from the trim edge).
"""
import re
import tempfile
from pathlib import Path


def _norm(t):
    return re.sub(r"[^0-9a-z]", "", t.lower())


def _classify(texts, cfg):
    """Return, for each page, (section, is_opener, is_blank).
    section is '1'..'6', 'R' (reference/back matter) or None (front matter).
    Openers are found by matching the first text on the page against the Part
    titles (cfg part_titles, in order) and the back-matter titles
    (cfg reference_openers). Generated CSS text is not in the PDF text layer, so
    titles are the reliable marker."""
    part_keys = [(_norm(t), str(i + 1)) for i, t in enumerate(cfg.get("part_titles", []))]
    ref_keys = [_norm(t) for t in cfg.get("reference_openers", [])]
    out, cur = [], None
    for t in texts:
        stripped = t.strip()
        head = _norm(" ".join(l.strip() for l in stripped.splitlines()[:6]))
        opener = False
        for key, sec in part_keys:
            if key and head.startswith(key[:30]):
                cur, opener = sec, True
                break
        else:
            for key in ref_keys:
                if cur is not None and key and head.startswith(key[:20]):
                    cur, opener = "R", True
                    break
        out.append((cur, opener, len(stripped) < 3))
    return out


def decorate(pdf_path: Path, cfg: dict):
    from pypdf import PdfReader, PdfWriter
    from playwright.sync_api import sync_playwright

    w, h = cfg["trim_width_in"], cfg["trim_height_in"]
    reader = PdfReader(str(pdf_path))
    texts = [(p.extract_text() or "") for p in reader.pages]
    info = _classify(texts, cfg)
    names = cfg.get("part_short_names", {})        # {1: "The Emergency Approach", ...}
    book_short = cfg.get("running_title", cfg.get("title", ""))
    accent, slate = "#a31c2c", "#2c3a48"
    n_tabs = 7                                      # six Parts plus reference
    tab_h, tab_gap, tab_top = 0.46, 0.07, 0.95
    outer = cfg["margin_outside_in"]

    pages_html = []
    for i, (sec, opener, blank) in enumerate(info):
        right = (i % 2 == 0)                        # page 1 is a right-hand page
        num = i + 1
        front = sec is None
        show = (not blank) and i >= 2               # no furniture on title/copyright pages
        parts = []
        if show:
            side = "right" if right else "left"
            # page number at the outer bottom corner
            parts.append(f'<div class="pn {side}">{num}</div>')
            if not opener and not front:
                label = names.get(int(sec), "Reference") if sec != "R" else "Reference"
                head = (f'<span class="rt">{label}</span>' if right else f'<span class="rt">{book_short}</span>')
                parts.append(f'<div class="hd {side}">{head}</div>')
            if not front:
                for k in range(n_tabs):
                    cur = (str(k + 1) == sec) or (k == 6 and sec == "R")
                    colour = (slate if k == 6 else accent) if cur else ("#e6dfe0" if k < 6 else "#d8dde3")
                    txtc = "#fff" if cur else "#9a8f91"
                    lab = str(k + 1) if k < 6 else "R"
                    y = tab_top + k * (tab_h + tab_gap)
                    parts.append(f'<div class="tab {side}" style="top:{y}in;background:{colour};color:{txtc}">{lab}</div>')
        pages_html.append(f'<div class="pg">{"".join(parts)}</div>')

    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>
    @page {{ size: {w}in {h}in; margin: 0; }}
    html,body {{ margin:0; padding:0; }}
    .pg {{ position:relative; width:{w}in; height:{h}in; overflow:hidden; page-break-after:always; font-family:"Inter","Arial",sans-serif; }}
    .hd {{ position:absolute; top:0.3in; font-size:7pt; letter-spacing:0.12em; text-transform:uppercase; color:#5a5e66; }}
    .hd.right {{ right:{outer}in; text-align:right; }} .hd.left {{ left:{outer}in; }}
    .hd .rt {{ border-bottom:1.2px solid {accent}; padding-bottom:3px; }}
    .pn {{ position:absolute; bottom:0.32in; font-size:8pt; font-weight:600; color:{accent}; }}
    .pn.right {{ right:{outer}in; }} .pn.left {{ left:{outer}in; }}
    .tab {{ position:absolute; width:0.2in; height:{tab_h}in; font-size:7pt; font-weight:700; line-height:{tab_h}in; text-align:center; }}
    .tab.right {{ right:0.27in; border-radius:3px 0 0 3px; }} .tab.left {{ left:0.27in; border-radius:0 3px 3px 0; }}
    </style></head><body>{"".join(pages_html)}</body></html>"""

    with tempfile.TemporaryDirectory() as td:
        hp, op = Path(td) / "o.html", Path(td) / "o.pdf"
        hp.write_text(html, encoding="utf-8")
        with sync_playwright() as p:
            b = p.chromium.launch()
            pg = b.new_page()
            pg.goto(hp.as_uri())
            pg.pdf(path=str(op), prefer_css_page_size=True, print_background=True)
            b.close()
        ov = PdfReader(str(op))
        wr = PdfWriter()
        for i, page in enumerate(reader.pages):
            if i < len(ov.pages):
                page.merge_page(ov.pages[i])
            wr.add_page(page)
        tmp = Path(td) / "m.pdf"
        with open(tmp, "wb") as f:
            wr.write(f)
        pdf_path.write_bytes(tmp.read_bytes())
