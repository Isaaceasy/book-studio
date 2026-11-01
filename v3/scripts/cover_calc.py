#!/usr/bin/env python3
"""KDP cover calculator for paperback wraps and ebook covers.

Usage:
  python scripts/cover_calc.py --trim 5x8 --pages 160 --paper white --ink bw
  python scripts/cover_calc.py --trim 6x9 --pages 220 --paper cream --ink bw --json
  python scripts/cover_calc.py --ebook

IMPORTANT: the constants below are DEFAULTS read from KDP help pages and secondary
sources on the dates noted in docs/kdp-specs.md. KDP's own cover template or calculator
for your exact trim, paper and ink is authoritative. Override any value on the command line
(--spine-per-page, --bleed) and cross-check before uploading.
"""
import argparse
import json
import sys

# Spine thickness per page in inches (verify live; see docs/kdp-specs.md).
SPINE_PER_PAGE = {
    ("bw", "white"): 0.002252,      # KDP help page (2026-11-02): page count x 0.002252
    ("bw", "cream"): 0.0025,        # KDP help page (2026-11-02): page count x 0.0025
    ("color", "white"): 0.002252,   # third-party source; VERIFY against KDP's color section
    ("premium", "white"): 0.002252, # third-party source; VERIFY
}
BLEED_IN = 0.125                    # per outside edge (KDP default)
SAFE_MARGIN_IN = 0.25               # keep text this far inside the trim edge (practical default)
SPINE_TEXT_MIN_PAGES = 80           # KDP Cover Creator help says 80 (some sources say 79); VERIFY
BARCODE_W_IN, BARCODE_H_IN = 2.0, 1.2   # clean area to reserve on the back cover (owner guide); KDP adds the barcode
BARCODE_MARGIN_IN = 0.25            # distance from the trim edges; VERIFY on KDP's template
DPI = 300

EBOOK = {
    "ideal_px_h": 2560, "ideal_px_w": 1600, "ratio": 1.6,
    "min_px": (1000, 625), "max_px_side": 10000, "formats": ["JPEG", "TIFF"],
    "color": "RGB", "max_mb": 50,
}


def parse_trim(s):
    w, h = s.lower().replace("in", "").split("x")
    return float(w), float(h)


def paperback(trim_w, trim_h, pages, paper="white", ink="bw", spine_per_page=None, bleed=BLEED_IN):
    key = (ink, paper)
    if spine_per_page is None:
        if key not in SPINE_PER_PAGE:
            raise SystemExit(f"No default spine factor for ink={ink} paper={paper}; pass --spine-per-page")
        spine_per_page = SPINE_PER_PAGE[key]
    spine = round(pages * spine_per_page, 4)
    wrap_w = round(2 * bleed + 2 * trim_w + spine, 4)
    wrap_h = round(trim_h + 2 * bleed, 4)
    # panel rectangles in inches, origin top-left of the full wrap including bleed
    back = {"x": bleed, "y": bleed, "w": trim_w, "h": trim_h}
    spine_p = {"x": bleed + trim_w, "y": bleed, "w": spine, "h": trim_h}
    front = {"x": bleed + trim_w + spine, "y": bleed, "w": trim_w, "h": trim_h}
    barcode = {
        "x": round(bleed + trim_w - BARCODE_MARGIN_IN - BARCODE_W_IN, 4),
        "y": round(bleed + trim_h - BARCODE_MARGIN_IN - BARCODE_H_IN, 4),
        "w": BARCODE_W_IN, "h": BARCODE_H_IN,
    }
    px = lambda v: int(round(v * DPI))
    return {
        "trim_in": [trim_w, trim_h], "pages": pages, "paper": paper, "ink": ink,
        "spine_per_page_in": spine_per_page, "spine_in": spine, "bleed_in": bleed,
        "wrap_in": [wrap_w, wrap_h], "wrap_px_300dpi": [px(wrap_w), px(wrap_h)],
        "panels_in": {"back": back, "spine": spine_p, "front": front},
        "barcode_zone_in": barcode, "safe_margin_in": SAFE_MARGIN_IN,
        "spine_text_allowed": pages >= SPINE_TEXT_MIN_PAGES and spine >= 0.25,
        "spine_text_min_pages": SPINE_TEXT_MIN_PAGES,
        "front_cover_px_300dpi_with_bleed": [px(trim_w + 2 * bleed), px(trim_h + 2 * bleed)],
        "notes": [
            "Verify every number against KDP's cover template for this trim, paper and ink.",
            "Recompute whenever the final page count changes.",
        ],
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trim", help="e.g. 5x8, 6x9, 8.5x11")
    ap.add_argument("--pages", type=int)
    ap.add_argument("--paper", default="white", choices=["white", "cream"])
    ap.add_argument("--ink", default="bw", choices=["bw", "color", "premium"])
    ap.add_argument("--spine-per-page", type=float)
    ap.add_argument("--bleed", type=float, default=BLEED_IN)
    ap.add_argument("--ebook", action="store_true", help="print the ebook cover spec")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.ebook:
        print(json.dumps(EBOOK, indent=2))
        return
    if not (a.trim and a.pages):
        ap.error("--trim and --pages are required for a paperback")
    w, h = parse_trim(a.trim)
    r = paperback(w, h, a.pages, a.paper, a.ink, a.spine_per_page, a.bleed)
    if a.json:
        print(json.dumps(r, indent=2))
        return
    print(f"Trim {w} x {h} in | {a.pages} pages | {a.ink} ink, {a.paper} paper")
    print(f"Spine width: {r['spine_in']} in (factor {r['spine_per_page_in']} per page)")
    print(f"Full wrap incl. bleed: {r['wrap_in'][0]} x {r['wrap_in'][1]} in = {r['wrap_px_300dpi'][0]} x {r['wrap_px_300dpi'][1]} px at 300 dpi")
    print(f"Spine text allowed: {r['spine_text_allowed']} (min {SPINE_TEXT_MIN_PAGES} pages, and spine at least 0.25 in)")
    print(f"Barcode zone (back cover, inches from wrap top-left): {r['barcode_zone_in']}")
    for k, v in r["panels_in"].items():
        print(f"  {k:5s}: x={v['x']:.4f} y={v['y']:.4f} w={v['w']:.4f} h={v['h']:.4f}")
    print("Verify against KDP's template before use.")


if __name__ == "__main__":
    sys.exit(main())
