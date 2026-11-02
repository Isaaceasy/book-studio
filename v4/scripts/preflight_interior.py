#!/usr/bin/env python3
"""Preflight checks for an interior PDF against the book's settings and common KDP rejections.

Usage: python scripts/preflight_interior.py books/<slug>/final/<file>.pdf --book books/<slug>/book.yaml

Checks:
  * every page has the trim size from book.yaml (tolerance 0.02 in) [or the size given by --trim 5x8]
  * page count is within KDP limits for the chosen ink (color min 72 pages; max 828 black / 600 standard color; verify live)
  * fonts are embedded (flags non-embedded fonts)
  * no link annotations (manuscripts must have no hyperlinks)
  * blank pages: counts nearly empty pages (some are intentional, e.g. right-hand openers)
  * images: lists the smallest image pixel size per page region (warns under 200 px/inch is not computable here; reports min pixels)
  * even/odd: reports odd page counts (KDP adds a blank page)
This is a mechanical check only. Always render and look at the pages, then use KDP's online previewer.
"""
import argparse
import sys

import yaml
from pypdf import PdfReader


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--book")
    ap.add_argument("--trim")
    a = ap.parse_args()
    cfg = yaml.safe_load(open(a.book, encoding="utf-8")) if a.book else {}
    if a.trim:
        tw, th = [float(x) for x in a.trim.lower().split("x")]
    else:
        tw, th = float(cfg.get("trim_width_in", 0)), float(cfg.get("trim_height_in", 0))
    ink_color = bool(cfg.get("color_interior", False))
    r = PdfReader(a.pdf)
    n = len(r.pages)
    problems = 0

    def rep(ok, msg, warn=False):
        nonlocal problems
        tag = "PASS" if ok else ("WARN" if warn else "FAIL")
        if not ok and not warn:
            problems += 1
        print(f"[{tag}] {msg}")

    bad = []
    for i, p in enumerate(r.pages):
        w, h = float(p.mediabox.width) / 72, float(p.mediabox.height) / 72
        if tw and (abs(w - tw) > 0.02 or abs(h - th) > 0.02):
            bad.append((i + 1, round(w, 3), round(h, 3)))
    if tw:
        rep(not bad, f"all pages are {tw} x {th} in" + (f"; off-size pages: {bad[:5]}" if bad else ""))
    rep(n >= 24, f"page count {n} (KDP minimum 24; color standard needs >= 72; verify live)")
    if ink_color:
        rep(72 <= n <= 600, "color interior page count within 72 to 600 (standard color)", warn=True)
    rep(n % 2 == 0, f"page count is {'even' if n % 2 == 0 else 'odd (KDP will add a blank page)'}", warn=True)

    unembedded, links, blank = set(), 0, []
    min_img = None
    for i, p in enumerate(r.pages):
        res = p.get("/Resources") or {}
        for _, ref in (res.get("/Font") or {}).items():
            f = ref.get_object()
            d = f.get("/FontDescriptor")
            emb = False
            if d is not None:
                dd = d.get_object()
                emb = any(k in dd for k in ("/FontFile", "/FontFile2", "/FontFile3"))
            if not emb and f.get("/Subtype") not in ("/Type0", "/Type3"):
                unembedded.add(str(f.get("/BaseFont")))
        for an in (p.get("/Annots") or []):
            o = an.get_object()
            if o.get("/Subtype") == "/Link":
                links += 1
        txt = (p.extract_text() or "").strip()
        try:
            imgs = list(p.images)
        except Exception:
            imgs = []
        if not txt and not imgs:
            blank.append(i + 1)
        for im in imgs:
            try:
                sz = im.image.size
                area = sz[0] * sz[1]
                if min_img is None or area < min_img[0]:
                    min_img = (area, sz, i + 1)
            except Exception:
                pass
    rep(not unembedded, "fonts embedded" + (f"; NOT embedded: {sorted(unembedded)[:6]}" if unembedded else ""), warn=True)
    rep(links == 0, f"link annotations found: {links} (manuscripts must have none)")
    rep(len(blank) <= max(10, n // 12), f"blank pages: {len(blank)} {blank[:12]} (intentional ones are fine; confirm)", warn=True)
    if min_img:
        print(f"[INFO] smallest embedded image: {min_img[1]} px on page {min_img[2]} (check it prints at 200+ dpi at its placed size)")
    print(f"RESULT: {'FAIL' if problems else 'PASS'} ({n} pages). Mechanical checks only; render and inspect pages, then use KDP's previewer.")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
