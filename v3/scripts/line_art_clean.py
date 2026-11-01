#!/usr/bin/env python3
"""Clean AI-generated coloring-page line art into print-ready black lines on white.

Usage:
  python scripts/line_art_clean.py in.png out.png --size 2550x3300 [--threshold 160] [--thicken 1] [--margin 150]

Steps: grayscale -> threshold to pure black/white -> remove isolated specks -> optional line thickening ->
fit inside the page minus margin with white padding -> save at 300 dpi. Prints a report (black ratio, speck
count, size) so a weak page (too heavy, too faint, nearly empty) is regenerated rather than shipped.
Requires Pillow and numpy.
"""
import argparse
import sys

import numpy as np
from PIL import Image, ImageFilter


def remove_specks(binary, min_pixels=12):
    """binary: 2D bool array True=black. Remove connected components smaller than min_pixels (4-connectivity)."""
    h, w = binary.shape
    seen = np.zeros_like(binary, dtype=bool)
    removed = 0
    for y in range(h):
        row = binary[y]
        for x in range(w):
            if row[x] and not seen[y, x]:
                stack = [(y, x)]
                comp = []
                seen[y, x] = True
                while stack:
                    cy, cx = stack.pop()
                    comp.append((cy, cx))
                    for ny, nx in ((cy + 1, cx), (cy - 1, cx), (cy, cx + 1), (cy, cx - 1)):
                        if 0 <= ny < h and 0 <= nx < w and binary[ny, nx] and not seen[ny, nx]:
                            seen[ny, nx] = True
                            stack.append((ny, nx))
                if len(comp) < min_pixels:
                    for cy, cx in comp:
                        binary[cy, cx] = False
                    removed += 1
    return removed


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("dst")
    ap.add_argument("--size", default="2550x3300")
    ap.add_argument("--threshold", type=int, default=160)
    ap.add_argument("--thicken", type=int, default=0, help="number of dilation passes")
    ap.add_argument("--margin", type=int, default=150, help="white margin in pixels at 300 dpi")
    ap.add_argument("--speck", type=int, default=12)
    a = ap.parse_args()
    W, H = [int(v) for v in a.size.lower().split("x")]
    im = Image.open(a.src).convert("L")
    # work at a size close to the target to keep line weight predictable
    scale = min((W - 2 * a.margin) / im.size[0], (H - 2 * a.margin) / im.size[1])
    im = im.resize((max(1, int(im.size[0] * scale)), max(1, int(im.size[1] * scale))), Image.LANCZOS)
    arr = np.array(im) < a.threshold
    removed = remove_specks(arr, a.speck)
    out = Image.fromarray(np.where(arr, 0, 255).astype("uint8"))
    for _ in range(a.thicken):
        out = out.filter(ImageFilter.MinFilter(3))
    page = Image.new("L", (W, H), 255)
    page.paste(out, ((W - out.size[0]) // 2, (H - out.size[1]) // 2))
    page = page.convert("1")
    page.save(a.dst, dpi=(300, 300))
    final = np.array(page) == 0
    ratio = final.mean()
    print(f"Saved {a.dst} at {W}x{H}px (300 dpi). Black ratio {ratio:.3%}. Specks removed: {removed}.")
    if ratio < 0.02:
        print("WARN: very little ink: page may be too faint or empty; regenerate.")
    if ratio > 0.35:
        print("WARN: heavy black areas: coloring page may be hard to color; regenerate with no filled areas.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
