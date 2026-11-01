#!/usr/bin/env python3
"""Place the REAL front cover into a simple standing-book mockup (slight perspective, spine strip, soft shadow).

Usage:
  python scripts/mockup_cover.py covers/front-cover.png out.png --size 970x600 --bg "#1b2430" [--bg-image scene.png] [--spine "#a31c2c"] [--height 0.82] [--side left|right|center]

Why a script: image generators redraw covers and change lettering. The owner's A+ prompt kit demands "use my uploaded cover exactly as provided".
This script uses the exact cover pixels. For richer scenes, generate a scene WITHOUT any book (HiggsField), pass it as --bg-image, and let this script composite the cover.
Not a photoreal 3D render: it is a clean stylized mockup, labelled as a mockup in the A+ copy where needed.
"""
import argparse

from PIL import Image, ImageDraw, ImageFilter


def find_coeffs(pa, pb):
    """Coefficients for PIL perspective transform mapping output points pa to input points pb."""
    import numpy as np
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])
    A = np.array(matrix, dtype=float)
    B = np.array(pb).reshape(8)
    return np.linalg.solve(A, B).tolist()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cover")
    ap.add_argument("out")
    ap.add_argument("--size", default="970x600")
    ap.add_argument("--bg", default="#1b2430")
    ap.add_argument("--bg-image")
    ap.add_argument("--spine", default="#222222")
    ap.add_argument("--height", type=float, default=0.82, help="cover height as a fraction of the canvas height")
    ap.add_argument("--side", default="center", choices=["left", "right", "center"])
    ap.add_argument("--tilt", type=float, default=0.035, help="perspective: far-edge shrink as a fraction of cover height")
    a = ap.parse_args()
    W, H = [int(v) for v in a.size.lower().split("x")]
    canvas = Image.open(a.bg_image).convert("RGB").resize((W, H)) if a.bg_image else Image.new("RGB", (W, H), a.bg)
    cov = Image.open(a.cover).convert("RGB")
    ch = int(H * a.height)
    cw = int(cov.size[0] * ch / cov.size[1])
    cov = cov.resize((cw, ch), Image.LANCZOS)
    ox = {"left": int(W * 0.12), "right": W - cw - int(W * 0.12), "center": (W - cw) // 2}[a.side]
    oy = (H - ch) // 2
    dy = int(ch * a.tilt)
    # destination quad (TL, TR, BR, BL): right edge slightly shorter -> turned away
    dst = [(ox, oy), (ox + cw, oy + dy), (ox + cw, oy + ch - dy), (ox, oy + ch)]
    src = [(0, 0), (cw, 0), (cw, ch), (0, ch)]
    coeffs = find_coeffs(dst, src)
    warped = cov.transform((W, H), Image.PERSPECTIVE, coeffs, Image.BICUBIC)
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).polygon(dst, fill=255)
    # shadow
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).polygon([(x + 18, y + 16) for x, y in dst], fill=150)
    sh = sh.filter(ImageFilter.GaussianBlur(16))
    canvas.paste(Image.new("RGB", (W, H), (0, 0, 0)), (0, 0), sh)
    # spine strip (thin, darker) on the left edge for a 3D hint
    strip = [(ox - 12, oy + 5), (ox, oy), (ox, oy + ch), (ox - 12, oy + ch - 5)]
    ImageDraw.Draw(canvas).polygon(strip, fill=a.spine)
    canvas.paste(warped, (0, 0), mask)
    canvas.save(a.out, quality=95)
    print(f"Saved {a.out} ({W}x{H}). The cover pixels are the supplied file; this is a stylized mockup, not a photo.")


if __name__ == "__main__":
    main()
