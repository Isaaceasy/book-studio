#!/usr/bin/env python3
"""Catalog dashboard: one table of every book, its stage, risk gates and open items, built from the files in each book folder.

Usage: python scripts/catalog.py [books_dir]   (default: ./books)  -> prints and writes books/CATALOG.md
Stage is inferred from which files exist, so it never contradicts the folder.
"""
import os
import re
import sys

import yaml

STAGES = [
    ("0 intake", ["brief.md", "book.yaml"]),
    ("1 cms", ["cms-research.md", "market-research.md"]),
    ("2 title", ["title-lab.md", "title-check.md"]),
    ("3 outline", ["outline.md"]),
    ("4 design", ["book.css"]),
    ("5 chapters", None),
    ("6 assembled", None),
    ("8 covers", ["covers/paperback-wrap.pdf"]),
    ("9 metadata", ["final/KDP-metadata.docx", "final/KDP-metadata.md"]),
    ("10 release", ["release/MANIFEST.md"]),
]


def has_any(book, names):
    return any(os.path.exists(os.path.join(book, n)) for n in names)


def stage(book):
    done = []
    for label, names in STAGES:
        if label.startswith("5"):
            ok = os.path.isdir(os.path.join(book, "chapters")) and any(n.endswith(".md") for n in os.listdir(os.path.join(book, "chapters")))
        elif label.startswith("6"):
            f = os.path.join(book, "final")
            ok = os.path.isdir(f) and any(n.endswith(".pdf") and "interior" in n for n in os.listdir(f))
        else:
            ok = has_any(book, names)
        if ok:
            done.append(label)
    return done


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "books"
    rows = []
    for slug in sorted(os.listdir(root)):
        b = os.path.join(root, slug)
        y = os.path.join(b, "book.yaml")
        if not os.path.exists(y):
            continue
        cfg = yaml.safe_load(open(y, encoding="utf-8")) or {}
        done = stage(b)
        last = done[-1] if done else "none"
        gate = "-"
        rr = os.path.join(b, "risk-register.md")
        if os.path.exists(rr):
            t = open(rr, encoding="utf-8").read()
            gs = []
            for g in ("R1 CONCEPT", "R2 BUILD", "R3 RELEASE"):
                m = re.findall(r"\|\s*" + g + r"\s*\|[^|]*\|\s*([^|]*)\|", t)
                gs.append((m[0].strip() if m and m[0].strip() else "-")[:14])
            gate = " / ".join(gs)
        n_ch = len([n for n in os.listdir(os.path.join(b, "chapters"))]) if os.path.isdir(os.path.join(b, "chapters")) else 0
        rows.append((slug, cfg.get("title", ""), cfg.get("profile", ""), cfg.get("run_mode", ""), last, n_ch, gate))
    out = ["# CATALOG", "", "| Book | Title | Profile | Mode | Furthest stage | Chapter files | Gates R1 / R2 / R3 |", "|---|---|---|---|---|---|---|"]
    for r in rows:
        out.append("| " + " | ".join(str(x) for x in r) + " |")
    text = "\n".join(out) + "\n"
    print(text)
    open(os.path.join(root, "CATALOG.md"), "w", encoding="utf-8").write(text)


if __name__ == "__main__":
    main()
