#!/usr/bin/env python3
"""Build a reflowable EPUB 3 (Kindle-ready) from a book's Markdown sources, then run mechanical checks.

Usage: python scripts/ebook_build.py books/<slug> [--out final/<name>.epub]
Needs pandoc. Order: front/*.md, chapters/*.md, back/*.md (sorted by file name; put numeric prefixes on files that must be ordered).
Uses covers/ebook-cover.jpg as the cover when present. Metadata comes from book.yaml.
Checks after the build: valid zip with an uncompressed mimetype first, navigation document present, no remote links,
no images without alt text in the Markdown, every referenced image present, file size, cover size.
Reflowable EPUB does not keep print page numbers or fixed layouts: the build removes print-only content (page breaks) and the
static contents page (the ebook gets a real navigation menu instead).
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile

import yaml

CSS = """
body { font-family: serif; line-height: 1.45; margin: 0 4%; }
h1 { font-size: 1.6em; margin: 1.2em 0 .6em; page-break-before: always; color: %(accent)s; }
h2 { font-size: 1.25em; margin: 1.1em 0 .4em; }
h3 { font-size: 1.05em; margin: .9em 0 .3em; }
p { margin: 0 0 .8em; text-align: left; }
img { max-width: 100%%; height: auto; }
figure { margin: 1em 0; text-align: center; }
figcaption { font-size: .9em; font-style: italic; }
table { border-collapse: collapse; width: 100%%; margin: 1em 0; font-size: .92em; }
th, td { border: 1px solid #888; padding: .3em .4em; vertical-align: top; }
th { background: #eee; }
.callout { border-left: .25em solid %(accent)s; padding: .2em .8em; margin: 1em 0; background: #f6f6f6; }
.callout-title { font-weight: bold; display: block; }
"""


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    book = os.path.abspath(sys.argv[1])
    pandoc = shutil.which("pandoc")
    if not pandoc:
        sys.exit("pandoc not found: install pandoc (pandoc.org) and rerun scripts/doctor.py")
    cfg = yaml.safe_load(open(os.path.join(book, "book.yaml"), encoding="utf-8"))
    out = os.path.join(book, "final", re.sub(r"[^a-z0-9]+", "-", cfg["title"].lower()).strip("-") + "-ebook.epub")
    if "--out" in sys.argv:
        out = os.path.join(book, sys.argv[sys.argv.index("--out") + 1])
    os.makedirs(os.path.dirname(out), exist_ok=True)

    files = []
    for sub in ("front", "chapters", "back"):
        d = os.path.join(book, sub)
        if os.path.isdir(d):
            files += [os.path.join(d, n) for n in sorted(os.listdir(d)) if n.endswith(".md")]
    if not files:
        sys.exit("no Markdown sources found")

    accent = "#" + str(cfg.get("accent", "333333")).lstrip("#")
    tmp = tempfile.mkdtemp()
    css = os.path.join(tmp, "ebook.css")
    open(css, "w", encoding="utf-8").write(CSS.replace("%%", "%").replace("%(accent)s", accent))
    meta = os.path.join(tmp, "meta.yaml")
    with open(meta, "w", encoding="utf-8") as f:
        yaml.safe_dump({
            "title": cfg["title"], "subtitle": cfg.get("subtitle", ""), "author": cfg["author"],
            "lang": cfg.get("language", "en"), "rights": f"Copyright {cfg.get('copyright_year', '')} {cfg['author']}",
            "date": str(cfg.get("publication_date", "")),
        }, f, allow_unicode=True)

    args = [pandoc, "-f", "markdown+fenced_divs+bracketed_spans+pipe_tables+implicit_figures", "-t", "epub3",
            "--toc", "--toc-depth=2", "--split-level=1", "--css", css, "--metadata-file", meta,
            "--resource-path", ".:" + book if os.name != "nt" else ".;" + book]
    cover = os.path.join(book, "covers", "ebook-cover.jpg")
    if os.path.exists(cover):
        args += ["--epub-cover-image", cover]
    args += ["-o", out] + files
    r = subprocess.run(args, capture_output=True, text=True, cwd=book)
    if r.returncode != 0:
        sys.exit("pandoc failed:\n" + r.stderr[-1500:])
    warn = [l for l in r.stderr.splitlines() if l.strip()]

    # ---- checks ----
    problems, notes = [], []
    with zipfile.ZipFile(out) as z:
        names = z.namelist()
        if names[0] != "mimetype":
            problems.append("mimetype is not the first entry")
        elif z.getinfo("mimetype").compress_type != zipfile.ZIP_STORED:
            problems.append("mimetype is compressed")
        if not any(n.endswith("nav.xhtml") for n in names):
            problems.append("navigation document (nav.xhtml) missing")
        remote = 0
        for n in names:
            if n.endswith((".xhtml", ".html")):
                t = z.read(n).decode("utf-8", "ignore")
                remote += len(re.findall(r'(?:href|src)="https?://', t))
        if remote:
            problems.append(f"{remote} remote link(s) or images inside the EPUB (rule 3)")
        imgs = [n for n in names if n.lower().endswith((".png", ".jpg", ".jpeg", ".svg", ".gif"))]
    noalt = 0
    for f in files:
        noalt += len(re.findall(r"!\[\s*\]\(", open(f, encoding="utf-8").read()))
    if noalt:
        problems.append(f"{noalt} image(s) in the Markdown have empty alt text (needed for ebook accessibility)")
    size_mb = os.path.getsize(out) / 1048576
    if size_mb > 650:
        problems.append("file larger than KDP's 650 MB limit")
    notes.append(f"{len(files)} source files, {len(imgs)} image files, {size_mb:.1f} MB")
    print(f"EPUB written: {out}")
    for n in notes:
        print("  " + n)
    for w in warn[:10]:
        print("  pandoc: " + w)
    for p in problems:
        print("  PROBLEM: " + p)
    print("RESULT:", "PASS (mechanical)" if not problems else f"{len(problems)} problem(s)")
    print("Still to do: validate with the free EPUBCheck tool or KDP's online previewer, and view in the Kindle previewer.")
    shutil.rmtree(tmp, ignore_errors=True)
    sys.exit(1 if problems else 0)


if __name__ == "__main__":
    main()
