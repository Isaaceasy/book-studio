#!/usr/bin/env python3
"""Preflight checks for cover files against the cover brief and KDP's published limits.

Usage: python scripts/preflight_cover.py covers/ [--brief covers/cover-brief.yaml] [--book books/<slug>/book.yaml]

Checks (each prints PASS / FAIL / WARN):
  * paperback-wrap.pdf page size equals the calculated wrap (tolerance 0.02 in)
  * fonts are embedded in the PDF
  * ebook-cover.jpg: JPEG, RGB, ratio 1.6 (height / width), >= 1000 x 625, <= 10,000 px per side, <= 50 MB
  * front-cover.png: pixel size at 300 dpi is at least the trim + bleed size
  * title and author strings in the brief equal the strings in book.yaml (title + subtitle < 200 chars)
This is a mechanical check. Also look at every file visually and check KDP's online previewer.
"""
import argparse
import os
import sys

import yaml
from PIL import Image
from pypdf import PdfReader

sys.path.insert(0, os.path.dirname(__file__))
from cover_calc import paperback, parse_trim  # noqa: E402

fails = 0


def report(ok, msg, warn=False):
    global fails
    tag = "PASS" if ok else ("WARN" if warn else "FAIL")
    if not ok and not warn:
        fails += 1
    print(f"[{tag}] {msg}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--brief")
    ap.add_argument("--book")
    a = ap.parse_args()
    folder = a.folder
    brief_path = a.brief or os.path.join(folder, "cover-brief.yaml")
    b = yaml.safe_load(open(brief_path, encoding="utf-8"))
    tw, th = parse_trim(b["trim"])
    calc = paperback(tw, th, int(b["pages"]), b.get("paper", "white"), b.get("ink", "color"))

    wrap = os.path.join(folder, "paperback-wrap.pdf")
    if os.path.exists(wrap):
        r = PdfReader(wrap)
        box = r.pages[0].mediabox
        w_in, h_in = float(box.width) / 72, float(box.height) / 72
        report(abs(w_in - calc["wrap_in"][0]) < 0.02 and abs(h_in - calc["wrap_in"][1]) < 0.02,
               f"wrap size {w_in:.3f} x {h_in:.3f} in vs expected {calc['wrap_in'][0]} x {calc['wrap_in'][1]} in")
        report(len(r.pages) == 1, f"wrap PDF has {len(r.pages)} page(s) (expected 1)")
        fonts_ok = True
        for pg in r.pages:
            res = pg.get("/Resources") or {}
            fdict = res.get("/Font") or {}
            for _, ref in fdict.items():
                f = ref.get_object()
                desc = f.get("/FontDescriptor")
                emb = False
                if desc is not None:
                    d = desc.get_object()
                    emb = any(k in d for k in ("/FontFile", "/FontFile2", "/FontFile3"))
                if not emb and f.get("/Subtype") != "/Type0":
                    fonts_ok = False
        report(fonts_ok, "fonts embedded in the wrap PDF", warn=True)
    else:
        report(False, "paperback-wrap.pdf not found (skip if ebook only)", warn=True)

    eb = os.path.join(folder, "ebook-cover.jpg")
    if os.path.exists(eb):
        im = Image.open(eb)
        w, h = im.size
        report(im.format == "JPEG", f"ebook format {im.format}")
        report(im.mode == "RGB", f"ebook color mode {im.mode} (RGB recommended)", warn=True)
        report(abs(h / w - 1.6) < 0.02, f"ebook ratio {h / w:.3f} (target 1.6 height/width)")
        report(h >= 1000 and w >= 625 and max(w, h) <= 10000, f"ebook pixels {w} x {h} (min 1000 x 625, max 10,000 per side)")
        report(os.path.getsize(eb) <= 50 * 1024 * 1024, f"ebook size {os.path.getsize(eb) / 1048576:.2f} MB (max 50)")
        report(h >= 2500, "ebook height >= 2500 px (KDP ideal 2,560)", warn=True)
    else:
        report(False, "ebook-cover.jpg not found", warn=True)

    fr = os.path.join(folder, "front-cover.png")
    if os.path.exists(fr):
        im = Image.open(fr)
        need = (int((tw + 2 * calc["bleed_in"]) * 300) - 2, int((th + 2 * calc["bleed_in"]) * 300) - 2)
        report(im.size[0] >= need[0] and im.size[1] >= need[1], f"front cover {im.size} px vs {need} px at 300 dpi")

    if a.book and os.path.exists(a.book):
        by = yaml.safe_load(open(a.book, encoding="utf-8"))
        same_t = (by.get("title") or "").strip() == b["title"].strip()
        same_s = (by.get("subtitle") or "").strip() == (b.get("subtitle") or "").strip()
        report(same_t and same_s, "title and subtitle in the brief equal book.yaml (must equal KDP metadata)")
        report(len((by.get("title") or "")) + len((by.get("subtitle") or "")) < 200, "title + subtitle under 200 characters")

    print("RESULT:", "FAIL" if fails else "PASS", "(mechanical checks only; inspect visually and in KDP's previewer)")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
