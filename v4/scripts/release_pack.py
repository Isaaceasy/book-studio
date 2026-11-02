#!/usr/bin/env python3
"""Build the release folder for a book: copies the upload files, writes MANIFEST.md (sha256, size) and OWNER-CHECKLIST.md.

Usage: python scripts/release_pack.py books/<slug> [--hold]
Looks for (first match wins):
  interior PDF   final/*interior*.pdf
  ebook EPUB     final/*ebook*.epub
  paperback wrap covers/paperback-wrap.pdf
  ebook cover    covers/ebook-cover.jpg
  metadata       final/KDP-metadata.docx, final/KDP-metadata.md
  upload guide   final/KDP-upload-guide.md
  A+ images      release/aplus/*  (already in place)
--hold  marks the packet WITHHELD (used when risk gate R3 is BLOCKED): files are listed but not copied into release/upload-ready/.
Reads books/<slug>/risk-register.md to print the gate state; never uploads anything.
"""
import glob
import hashlib
import os
import re
import shutil
import sys
import datetime


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def first(book, pats):
    for p in pats:
        m = sorted(glob.glob(os.path.join(book, p)))
        if m:
            return m[0]
    return None


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    book = os.path.abspath(sys.argv[1])
    hold = "--hold" in sys.argv
    rel = os.path.join(book, "release")
    dest = os.path.join(rel, "upload-ready")
    os.makedirs(rel, exist_ok=True)
    items = [
        ("Interior PDF (paperback)", ["final/*interior*.pdf"]),
        ("Ebook EPUB", ["final/*ebook*.epub"]),
        ("Paperback cover wrap PDF", ["covers/paperback-wrap.pdf"]),
        ("Ebook cover JPG", ["covers/ebook-cover.jpg"]),
        ("KDP metadata (Word)", ["final/KDP-metadata.docx"]),
        ("KDP metadata (text)", ["final/KDP-metadata.md"]),
        ("Upload guide", ["final/KDP-upload-guide.md", "final/KDP-UPLOAD-GUIDE.md"]),
    ]
    gate = "NO RISK REGISTER"
    rr = os.path.join(book, "risk-register.md")
    if os.path.exists(rr):
        t = open(rr, encoding="utf-8").read()
        m = re.findall(r"\|\s*R3 RELEASE\s*\|[^|]*\|\s*([^|]*)\|", t)
        gate = (m[0].strip() if m and m[0].strip() else "R3 NOT RUN")
    if gate.upper().startswith("BLOCKED") or gate in ("R3 NOT RUN", "NO RISK REGISTER"):
        hold = True
    if not hold:
        os.makedirs(dest, exist_ok=True)
    rows = []
    for label, pats in items:
        p = first(book, pats)
        if not p:
            rows.append((label, "MISSING", "", ""))
            continue
        if not hold:
            shutil.copy2(p, os.path.join(dest, os.path.basename(p)))
        rows.append((label, os.path.relpath(p, book).replace("\\", "/"), f"{os.path.getsize(p) / 1048576:.2f} MB", sha(p)))
    now = datetime.date.today().isoformat()
    with open(os.path.join(rel, "MANIFEST.md"), "w", encoding="utf-8") as f:
        f.write(f"# Release manifest ({now})\n\nRisk gate R3: **{gate}**. Packet: **{'WITHHELD (files listed, not copied)' if hold else 'READY in release/upload-ready/'}**\n\n")
        f.write("| Item | Source | Size | SHA-256 |\n|---|---|---|---|\n")
        for r in rows:
            f.write("| " + " | ".join(r) + " |\n")
    with open(os.path.join(rel, "OWNER-CHECKLIST.md"), "w", encoding="utf-8") as f:
        f.write(f"# Owner checklist (only you can do these) {now}\n\n")
        for s in [
            "Sign in to your own KDP account yourself (Claude never enters passwords).",
            "Run the registry (USPTO) search for the title and series name if not done; save the result pages.",
            "Read the written expert sign-off record (medical, engineering, legal, financial profiles) and confirm it exists as a file you hold.",
            "Upload the files from release/upload-ready/ and enter the fields from final/KDP-upload-guide.md.",
            "Answer the AI-generated content questions using the facts in status.md.",
            "View the paperback and ebook in KDP's online previewer; fix anything that looks wrong and rebuild.",
            "Order a proof copy; check spine position, color, sharpness and page edges.",
            "Set prices and territories yourself; confirm the royalty shown.",
            "Press Publish yourself.",
        ]:
            f.write(f"- [ ] {s}\n")
    missing = [r[0] for r in rows if r[1] == "MISSING"]
    print(f"release/ written. Gate R3: {gate}. {'WITHHELD' if hold else 'READY'}. Missing: {', '.join(missing) or 'none'}")


if __name__ == "__main__":
    main()
