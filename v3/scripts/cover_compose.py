#!/usr/bin/env python3
"""Compose exact-text covers from a cover brief (YAML) using HTML/CSS rendered by Chromium.

Usage:
  python scripts/cover_compose.py covers/cover-brief.yaml [--out covers]

The brief (see templates/cover-brief.yaml) supplies the final strings, trim, page count, art file
paths and style tokens. Output:
  paperback-wrap.pdf   exact wrap size (back + spine + front, with bleed), text as vector
  ebook-cover.jpg      front cover at 1600 x 2560 px (width x height), RGB JPEG
  front-cover.png      high-resolution front cover (trim + bleed at 300 dpi)
  thumbnail-test.png   150 px wide front cover to test legibility
Art is generated elsewhere (HiggsField) WITHOUT text; every word here is set by this script.
"""
import argparse
import html
import os
import sys
from pathlib import Path

import yaml

sys.path.insert(0, os.path.dirname(__file__))
from cover_calc import paperback, parse_trim  # noqa: E402

DEFAULTS = {
    "palette": {"bg": "#14213d", "title": "#ffffff", "subtitle": "#e5e5e5", "author": "#ffd166", "accent": "#a31c2c"},
    "fonts": {"title": "Inter", "body": "Inter"},
    "title_size_pt": 40,
    "subtitle_size_pt": 15,
    "author_size_pt": 15,
    "overlay_opacity": 0.35,
}


def merge(a, b):
    out = dict(a)
    for k, v in (b or {}).items():
        out[k] = merge(out[k], v) if isinstance(v, dict) and isinstance(out.get(k), dict) else v
    return out


def front_html(b, w, h, art):
    p = b["palette"]
    f = b["fonts"]
    bg = f"background:url('{art}') center/cover no-repeat;" if art else f"background:{p['bg']};"
    return f"""
    <div class="front" style="{bg}">
      <div class="shade"></div>
      <div class="text">
        <div class="title">{html.escape(b['title'])}</div>
        <div class="subtitle">{html.escape(b.get('subtitle', ''))}</div>
        <div class="author">{html.escape(b['author'])}</div>
      </div>
    </div>"""


def build_html(b, calc):
    p, f = b["palette"], b["fonts"]
    bleed = calc["bleed_in"]
    W, H = calc["wrap_in"]
    pan = calc["panels_in"]
    safe = calc["safe_margin_in"]
    spine_ok = calc["spine_text_allowed"] and b.get("spine_text", True)
    front_art = Path(b["art"]["front"]).resolve().as_uri() if b.get("art", {}).get("front") else ""
    back_art = Path(b["art"]["back"]).resolve().as_uri() if b.get("art", {}).get("back") else ""
    bc = calc["barcode_zone_in"]
    back_paras = "".join(f"<p>{html.escape(t)}</p>" for t in b.get("back_paragraphs", []))
    css = f"""
    @page {{ size: {W}in {H}in; margin: 0; }}
    html,body {{ margin:0; padding:0; }}
    body {{ width:{W}in; height:{H}in; position:relative; font-family:'{f['body']}', Arial, sans-serif; background:{p['bg']}; }}
    .abs {{ position:absolute; overflow:hidden; }}
    .panel-bg {{ position:absolute; inset:0; }}
    .shade {{ position:absolute; inset:0; background:rgba(0,0,0,{b['overlay_opacity']}); }}
    .text {{ position:absolute; left:{safe}in; right:{safe}in; top:{safe+0.35}in; display:flex; flex-direction:column; gap:0.18in; }}
    .title {{ font-family:'{f['title']}'; font-weight:800; font-size:{b['title_size_pt']}pt; line-height:1.04; color:{p['title']}; }}
    .subtitle {{ font-size:{b['subtitle_size_pt']}pt; line-height:1.25; color:{p['subtitle']}; }}
    .author {{ position:absolute; left:0; right:0; top:{pan['front']['h']-safe*2-1.0}in; font-weight:700; font-size:{b['author_size_pt']}pt; letter-spacing:.08em; text-transform:uppercase; color:{p['author']}; }}
    .back-text {{ position:absolute; left:{safe+0.1}in; right:{safe+0.1}in; top:{safe+0.4}in; color:{p['title']}; }}
    .back-text h2 {{ font-size:18pt; margin:0 0 .15in 0; line-height:1.15; }}
    .back-text p {{ font-size:10.5pt; line-height:1.4; margin:0 0 .1in 0; text-align:justify; }}
    .spine {{ display:flex; align-items:center; justify-content:center; }}
    .spine span {{ writing-mode:vertical-rl; transform:rotate(180deg); white-space:nowrap; font-weight:700; font-size:{min(14, max(8, calc['spine_in']*72*0.5)):.1f}pt; color:{p['title']}; letter-spacing:.04em; }}
    """
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body>
    <!-- back -->
    <div class="abs" style="left:0;top:0;width:{pan['back']['x']+pan['back']['w']}in;height:{H}in;{('background:url('+repr(back_art)+') center/cover no-repeat;') if back_art else 'background:'+p['bg']+';'}">
      <div class="shade"></div>
    </div>
    <div class="abs back-text" style="left:{pan['back']['x']+safe+0.1}in;top:{pan['back']['y']+safe+0.4}in;width:{pan['back']['w']-2*safe-0.2}in;">
      <h2>{html.escape(b.get('back_headline',''))}</h2>{back_paras}
    </div>
    <!-- barcode zone kept clear: draw a white rectangle KDP will overprint -->
    <div class="abs" style="left:{bc['x']}in;top:{bc['y']}in;width:{bc['w']}in;height:{bc['h']}in;background:#ffffff;"></div>
    <!-- spine -->
    <div class="abs spine" style="left:{pan['spine']['x']}in;top:0;width:{pan['spine']['w']}in;height:{H}in;background:{p['accent']};">
      {('<span>'+html.escape(b['title'])+' &nbsp;|&nbsp; '+html.escape(b['author'])+'</span>') if spine_ok else ''}
    </div>
    <!-- front -->
    <div class="abs" style="left:{pan['front']['x']}in;top:0;width:{pan['front']['w']+bleed}in;height:{H}in;{('background:url('+repr(front_art)+') center/cover no-repeat;') if front_art else 'background:'+p['bg']+';'}">
      <div class="shade"></div>
      <div style="position:absolute;left:{safe}in;right:{safe+bleed}in;top:{bleed+safe+0.35}in;bottom:{bleed+safe}in;">
        <div class="title">{html.escape(b['title'])}</div>
        <div class="subtitle" style="margin-top:.18in">{html.escape(b.get('subtitle',''))}</div>
        <div class="author" style="top:auto;bottom:0;">{html.escape(b['author'])}</div>
      </div>
    </div>
    </body></html>"""


def front_only_html(b, trim_w, trim_h, bleed, with_bleed=True):
    p, f = b["palette"], b["fonts"]
    art = Path(b["art"]["front"]).resolve().as_uri() if b.get("art", {}).get("front") else ""
    W = trim_w + (2 * bleed if with_bleed else 0)
    H = trim_h + (2 * bleed if with_bleed else 0)
    pad = 0.45 + (bleed if with_bleed else 0)
    bgcss = f"background:url('{art}') center/cover no-repeat;" if art else f"background:{p['bg']};"
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>
    @page {{ size:{W}in {H}in; margin:0; }} html,body{{margin:0;}}
    .c{{ width:{W}in;height:{H}in;position:relative;{bgcss} font-family:'{f['body']}',Arial,sans-serif; }}
    .s{{ position:absolute;inset:0;background:rgba(0,0,0,{b['overlay_opacity']}); }}
    .t{{ position:absolute;left:{pad}in;right:{pad}in;top:{pad+0.35}in; }}
    .title{{ font-family:'{f['title']}';font-weight:800;font-size:{b['title_size_pt']}pt;line-height:1.04;color:{p['title']}; }}
    .sub{{ margin-top:.18in;font-size:{b['subtitle_size_pt']}pt;line-height:1.25;color:{p['subtitle']}; }}
    .a{{ position:absolute;left:{pad}in;right:{pad}in;bottom:{pad}in;font-weight:700;font-size:{b['author_size_pt']}pt;letter-spacing:.08em;text-transform:uppercase;color:{p['author']}; }}
    </style></head><body><div class="c"><div class="s"></div>
    <div class="t"><div class="title">{html.escape(b['title'])}</div><div class="sub">{html.escape(b.get('subtitle',''))}</div></div>
    <div class="a">{html.escape(b['author'])}</div></div></body></html>"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("brief")
    ap.add_argument("--out", default="covers")
    a = ap.parse_args()
    b = merge(DEFAULTS, yaml.safe_load(open(a.brief, encoding="utf-8")))
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    tw, th = parse_trim(b["trim"])
    calc = paperback(tw, th, int(b["pages"]), b.get("paper", "white"), b.get("ink", "color"))
    from playwright.sync_api import sync_playwright
    with sync_playwright() as pw:
        br = pw.chromium.launch()
        pg = br.new_page()
        if b.get("paperback", True):
            pg.set_content(build_html(b, calc))
            pg.pdf(path=str(out / "paperback-wrap.pdf"), width=f"{calc['wrap_in'][0]}in", height=f"{calc['wrap_in'][1]}in", print_background=True)
        # front cover at trim+bleed (high-res PNG)
        pg2 = br.new_page(viewport={"width": int((tw + 2 * calc['bleed_in']) * 96), "height": int((th + 2 * calc['bleed_in']) * 96)}, device_scale_factor=300 / 96)
        pg2.set_content(front_only_html(b, tw, th, calc["bleed_in"], True))
        pg2.screenshot(path=str(out / "front-cover.png"))
        # ebook cover 1600 x 2560 (width x height), no bleed
        pg3 = br.new_page(viewport={"width": 1600 // 2, "height": 2560 // 2}, device_scale_factor=2)
        eb = front_only_html(b, 1600 / 96 / 2 * 1.0, 2560 / 96 / 2 * 1.0, 0, False)
        pg3.set_content(eb)
        pg3.screenshot(path=str(out / "ebook-cover.png"))
        br.close()
    from PIL import Image
    im = Image.open(out / "ebook-cover.png").convert("RGB")
    im = im.resize((1600, 2560))
    im.save(out / "ebook-cover.jpg", quality=92)
    (out / "ebook-cover.png").unlink(missing_ok=True)
    th_im = Image.open(out / "front-cover.png").convert("RGB")
    th_im.thumbnail((150, 240))
    th_im.save(out / "thumbnail-test.png")
    print("Wrote:", ", ".join(sorted(os.listdir(out))))
    print("Spine width", calc["spine_in"], "in; wrap", calc["wrap_in"], "in. Now run preflight_cover.py and view the files.")


if __name__ == "__main__":
    sys.exit(main())
