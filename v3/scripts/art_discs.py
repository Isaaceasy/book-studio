#!/usr/bin/env python3
"""Draw geometric cover art: a column of colored discs with letters (concept 'priority discs'), no AI involved.

Usage:
  python scripts/art_discs.py front.png --kind front --size 2400x3600 --bg "#F6F1EA" --from "#A31C2C" --to "#F2C6CC" --letters ABCDE
  python scripts/art_discs.py back.png  --kind back  --size 2400x3600 --bg "#F6F1EA" --from "#A31C2C" --to "#F2C6CC" --letters ABCDE

front: a vertical cascade of discs bleeding off the right edge (letters set with the static Inter font).
back : a quiet row of small discs along the bottom-left, low contrast, leaving the text area clean.
Everything is drawn at 2x and reduced for smooth edges. Art contains letters only because they are part of the concept
(the A-B-C-D-E primary survey); all title text is still set by cover_compose.py.
"""
import argparse
import os

from PIL import Image, ImageDraw, ImageFont


def hex2rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) for i in (0, 2, 4))


def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))


def lum(c):
    r, g, b = [x / 255 for x in c]
    return 0.2126 * r + 0.7152 * g + 0.0722 * b


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out")
    ap.add_argument("--kind", default="front", choices=["front", "back"])
    ap.add_argument("--size", default="2400x3600")
    ap.add_argument("--bg", default="#F6F1EA")
    ap.add_argument("--from", dest="c0", default="#A31C2C")
    ap.add_argument("--to", dest="c1", default="#F2C6CC")
    ap.add_argument("--letters", default="ABCDE")
    ap.add_argument("--font", default=os.path.join(os.path.dirname(__file__), "..", "fonts", "InterTT-ExtraBold.ttf"))
    a = ap.parse_args()
    W, H = [int(v) for v in a.size.lower().split("x")]
    S = 2
    im = Image.new("RGB", (W * S, H * S), hex2rgb(a.bg))
    d = ImageDraw.Draw(im)
    c0, c1 = hex2rgb(a.c0), hex2rgb(a.c1)
    n = len(a.letters)
    if a.kind == "front":
        dia = int(W * S * 0.36)
        cx = int(W * S * 0.97)
        top = int(H * S * 0.30)
        step = int((H * S * 0.66 - dia) / (n - 1)) if n > 1 else 0
        # draw from the last disc up to the first so upper discs overlap lower ones; each letter sits in the
        # visible lower part of its own disc and toward the left so it stays on the page
        for i in range(n - 1, -1, -1):
            ch = a.letters[i]
            t = i / max(1, n - 1)
            col = lerp(c0, c1, t)
            cy = top + dia // 2 + i * step
            d.ellipse((cx - dia // 2, cy - dia // 2, cx + dia // 2, cy + dia // 2), fill=col)
            fnt = ImageFont.truetype(a.font, int(dia * 0.36))
            tc = (255, 255, 255) if lum(col) < 0.55 else (60, 20, 28)
            d.text((cx - int(dia * 0.20), cy + int(dia * 0.20)), ch, font=fnt, fill=tc, anchor="mm")
    else:
        dia = int(W * S * 0.065)   # small enough that the row ends before the barcode zone (starts at about 56 percent of the panel width)
        gap = int(dia * 0.35)
        y = int(H * S * 0.90)
        x0 = int(W * S * 0.07)
        for i in range(n):
            t = i / max(1, n - 1)
            col = lerp(lerp(c0, hex2rgb(a.bg), 0.55), lerp(c1, hex2rgb(a.bg), 0.4), t)
            x = x0 + i * (dia + gap)
            d.ellipse((x, y, x + dia, y + dia), fill=col)
    im = im.resize((W, H), Image.LANCZOS)
    im.save(a.out)
    print(f"Saved {a.out} ({W}x{H}, {a.kind}). Drawn by script; no AI image involved.")


if __name__ == "__main__":
    main()
