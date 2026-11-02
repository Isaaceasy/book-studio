#!/usr/bin/env python3
"""Environment check. Run first, on every computer and in every cloud session.

Usage: python scripts/doctor.py [--json]
Prints what is installed, what is missing, and which pipeline stages each missing item blocks.
Exit code 0 = all required items present, 1 = a required item is missing.
Tool connections (browser, HiggsField) cannot be seen from a script: the doctor lists them as ASK THE ASSISTANT TO CONFIRM.
"""
import importlib
import json
import os
import shutil
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

PY_MODULES = [
    ("yaml", "pyyaml", True, "every stage (book.yaml)"),
    ("pypdf", "pypdf", True, "preflight, cover wrap, assembly"),
    ("docx", "python-docx", True, "Word previews, clearance pack, metadata docx"),
    ("PIL", "pillow", True, "covers, art, mockups, coloring pages"),
    ("numpy", "numpy", True, "cover art, coloring pages"),
    ("playwright", "playwright", True, "PDF interior, covers, A+ images"),
]


def find_git():
    g = shutil.which("git")
    if g:
        return g
    base = os.path.join(os.environ.get("LOCALAPPDATA", ""), "GitHubDesktop")
    if os.path.isdir(base):
        for d in sorted(os.listdir(base), reverse=True):
            p = os.path.join(base, d, "resources", "app", "git", "cmd", "git.exe")
            if os.path.exists(p):
                return p
    return None


def chromium_ok():
    try:
        from playwright.sync_api import sync_playwright
        with sync_playwright() as p:
            return os.path.exists(p.chromium.executable_path), p.chromium.executable_path
    except Exception as e:  # noqa
        return False, str(e)[:80]


def main():
    rows = []  # (name, ok, required, detail, blocks)
    v = sys.version_info
    rows.append(("Python >= 3.10", v >= (3, 10), True, f"{v.major}.{v.minor}.{v.micro}", "everything"))
    for mod, pipname, req, blocks in PY_MODULES:
        try:
            importlib.import_module(mod)
            rows.append((f"python: {pipname}", True, req, "installed", blocks))
        except Exception:
            rows.append((f"python: {pipname}", False, req, f"pip install {pipname}", blocks))
    ok, det = chromium_ok()
    rows.append(("Playwright Chromium", ok, True, det if ok else "python -m playwright install chromium", "PDF interior, covers, A+ images"))
    for exe, req, blocks, hint in [
        ("pandoc", True, "Markdown to Word / EPUB", "install pandoc (pandoc.org)"),
        ("soffice", False, "Word to PDF test copies (Word-format books)", "install LibreOffice"),
    ]:
        p = shutil.which(exe) or (shutil.which("libreoffice") if exe == "soffice" else None)
        rows.append((exe, bool(p), req, p or hint, blocks))
    g = find_git()
    rows.append(("git", bool(g), True, g or "install Git or GitHub Desktop", "commits, cloud runs"))
    fonts = os.path.join(ROOT, "fonts")
    rows.append(("fonts/ folder (static Inter etc.)", os.path.isdir(fonts) and len(os.listdir(fonts)) > 0, True, fonts, "covers (embedded fonts)"))
    for rel in ["CLAUDE.md", ".claude/skills", "profiles", "templates", "interiors/library", "docs/kdp-specs.md"]:
        rows.append((f"file: {rel}", os.path.exists(os.path.join(ROOT, rel)), True, rel, "framework integrity"))

    width = max(len(r[0]) for r in rows) + 2
    missing_req = 0
    print("BOOK STUDIO DOCTOR")
    print("-" * 78)
    for name, ok, req, detail, blocks in rows:
        tag = "OK     " if ok else ("MISSING" if req else "optional")
        if not ok and req:
            missing_req += 1
        print(f"{tag}  {name:<{width}} {detail if ok else detail}   [{blocks}]" if not ok else f"{tag}  {name:<{width}} {detail}")
    print("-" * 78)
    print("ASK THE ASSISTANT TO CONFIRM (a script cannot see these): built-in browser or Chrome tool for Amazon research;")
    print("HiggsField connection for images and upscales; audio tool (only for audiobooks); network access to KDP help pages.")
    print(f"RESULT: {'READY' if missing_req == 0 else str(missing_req) + ' required item(s) missing'}")
    if "--json" in sys.argv:
        print(json.dumps([dict(name=r[0], ok=r[1], required=r[2], detail=r[3], blocks=r[4]) for r in rows], indent=1))
    sys.exit(0 if missing_req == 0 else 1)


if __name__ == "__main__":
    main()
