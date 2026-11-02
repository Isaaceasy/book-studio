#!/usr/bin/env python3
"""Status keeper: keeps the top of status.md truthful and flags contradictions.

Usage: python scripts/status_keeper.py books/<slug> [--write]
Builds an AUTO block (between <!-- STATUS-AUTO:BEGIN --> and <!-- STATUS-AUTO:END -->) at the top of status.md from the files that
exist, the R1/R2/R3 gates, and the lint result summary if reports/lint.txt exists. Without --write it only prints.
Warns when status.md holds lines that contradict each other (for example 'cleared' and 'NO CLEARANCE'), so superseded decisions
can be moved to status-archive.md by the assistant (lesson L10). It never deletes text.
"""
import datetime
import os
import re
import sys

BEGIN, END = "<!-- STATUS-AUTO:BEGIN -->", "<!-- STATUS-AUTO:END -->"

PAIRS = [
    (r"\bno clearance\b|\bNOT cleared\b|\bnot yet cleared\b|NAMED NO CLEARANCE", r"\bfully cleared\b|\bcleared on the owner'?s word\b|\bclinician cleared\b|\bsign-?off received\b"),
    (r"\bGO\b verdict", r"\bNO-GO\b verdict"),
    (r"\bAUTONOMOUS\b.*\bnot\b.*chosen", r"run_mode:\s*\"?AUTONOMOUS"),
]


def exists(b, *p):
    return os.path.exists(os.path.join(b, *p))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    b = sys.argv[1]
    sp = os.path.join(b, "status.md")
    t = open(sp, encoding="utf-8").read() if os.path.exists(sp) else ""
    marks = [
        ("Brief and settings", exists(b, "brief.md") and exists(b, "book.yaml")),
        ("CMS research", exists(b, "cms-research.md") or exists(b, "market-research.md")),
        ("Product spec", exists(b, "product-spec.md")),
        ("Title lab / check", exists(b, "title-lab.md") or exists(b, "title-check.md")),
        ("Risk register", exists(b, "risk-register.md")),
        ("Outline / style guide / bible", exists(b, "outline.md") and exists(b, "style-guide.md") and exists(b, "book-bible.md")),
        ("Interior design (book.css)", exists(b, "book.css")),
        ("Chapters written", exists(b, "chapters") and len([n for n in os.listdir(os.path.join(b, "chapters")) if n.endswith(".md")]) > 0),
        ("Interior PDF built", exists(b, "final") and any("interior" in n and n.endswith(".pdf") for n in os.listdir(os.path.join(b, "final")))),
        ("Ebook EPUB built", exists(b, "final") and any(n.endswith(".epub") for n in os.listdir(os.path.join(b, "final")))),
        ("Covers (wrap + ebook)", exists(b, "covers", "paperback-wrap.pdf") and exists(b, "covers", "ebook-cover.jpg")),
        ("KDP metadata", exists(b, "final", "KDP-metadata.docx") or exists(b, "final", "KDP-metadata.md")),
        ("Release manifest", exists(b, "release", "MANIFEST.md")),
    ]
    gates = ""
    rr = os.path.join(b, "risk-register.md")
    if os.path.exists(rr):
        rt = open(rr, encoding="utf-8").read()
        for g in ("R1 CONCEPT", "R2 BUILD", "R3 RELEASE"):
            m = re.findall(r"\|\s*" + g + r"\s*\|[^|]*\|\s*([^|]*)\|", rt)
            gates += f"{g.split()[0]}={(m[0].strip() if m and m[0].strip() else 'not run')}  "
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [BEGIN, f"## CURRENT STATE (auto, {now}; edit decisions below, not this block)"]
    for name, ok in marks:
        lines.append(f"- [{'x' if ok else ' '}] {name}")
    if gates:
        lines.append(f"- Risk gates: {gates.strip()}")
    lines.append(END)
    block = "\n".join(lines)

    bad = []
    for a, c in PAIRS:
        if re.search(a, t, re.I) and re.search(c, t, re.I):
            bad.append((a, c))
    if BEGIN in t:
        new = re.sub(re.escape(BEGIN) + r".*?" + re.escape(END), lambda m: block, t, flags=re.S)
    else:
        new = block + "\n\n" + t
    print(block)
    for a, c in bad:
        print(f"WARNING: status.md seems to contain both '{a}' and '{c}'. Move the superseded decision to status-archive.md.")
    if "--write" in sys.argv:
        open(sp, "w", encoding="utf-8").write(new)
        print("status.md updated")


if __name__ == "__main__":
    main()
