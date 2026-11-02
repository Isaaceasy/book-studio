#!/usr/bin/env python3
"""Read trademark search result pages the owner saved (MHTML or HTML) and list live marks.

Usage:
  python -X utf8 scripts/tm_scan.py "Trademark search*.mhtml" --terms "emergency nursing" fundamentals --classes 9 16 41

What it does: parses each saved USPTO results page, builds records (wordmark, status words,
classes, owner, goods snippet), keeps LIVE records, filters by terms and classes, prints a compact
table and a summary. It reads ONLY what is in the saved pages; it does not search anything.
Not legal advice. Pages the owner saved show only the first screens of results; say so in the report.
"""
import argparse
import email
import glob
import html
import re
import sys
from email import policy


def load_text(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    if path.lower().endswith((".mhtml", ".mht", ".eml")):
        msg = email.message_from_bytes(raw, policy=policy.default)
        parts = []
        for p in msg.walk():
            if p.get_content_type() == "text/html":
                try:
                    parts.append(p.get_content())
                except Exception:
                    parts.append(p.get_payload(decode=True).decode("utf-8", "ignore"))
        return "".join(parts)
    return raw.decode("utf-8", "ignore")


def records(text):
    plain = re.sub(r"<script.*?</script>|<style.*?</style>", " ", text, flags=re.S)
    plain = html.unescape(re.sub(r"<[^>]+>", "\n", plain))
    lines = [l.strip() for l in plain.split("\n") if l.strip()]
    out = []
    for i, l in enumerate(lines):
        if l == "Wordmark" and i + 2 < len(lines) and lines[i + 1] == "wordmark":
            seg = lines[i + 2:i + 36]

            def after(key):
                return seg[seg.index(key) + 1] if key in seg else ""

            status_block = seg[seg.index("Status") + 1: seg.index("Goods & services")] if "Goods & services" in seg and "Status" in seg else []
            live = "Live" in status_block
            out.append({
                "mark": seg[0],
                "live": live,
                "status": " ".join(status_block),
                "classes": after("Class"),
                "owner": after("Owners"),
                "goods": after("Goods & services"),
            })
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="+")
    ap.add_argument("--terms", nargs="*", default=[], help="keep marks containing ANY of these words (case-insensitive)")
    ap.add_argument("--classes", nargs="*", default=[], help="keep marks in ANY of these classes, e.g. 9 16 41")
    ap.add_argument("--all-status", action="store_true", help="include dead marks too")
    a = ap.parse_args()
    paths = []
    for f in a.files:
        paths.extend(glob.glob(f) or [f])
    seen = set()
    total = 0
    kept = []
    for p in sorted(paths):
        recs = records(load_text(p))
        total += len(recs)
        for r in recs:
            if not a.all_status and not r["live"]:
                continue
            u = r["mark"].upper()
            if a.terms and not any(t.upper() in u for t in a.terms):
                continue
            if a.classes:
                cls = set(re.findall(r"\d{3}", r["classes"]))
                if not any(c.zfill(3) in cls for c in a.classes):
                    continue
            key = (u, r["classes"], r["owner"])
            if key in seen:
                continue
            seen.add(key)
            kept.append(r)
    print(f"Files read: {len(paths)} | records parsed: {total} | kept: {len(kept)}")
    for r in kept:
        print(f"- {r['mark']} | {'LIVE' if r['live'] else 'dead'} | class {r['classes']} | {r['owner'][:70]} | {r['goods'][:80]}")
    exact = [r for r in kept if any(r['mark'].upper() == t.upper() for t in a.terms)]
    print(f"Exact matches to a search term: {len(exact)}")
    print("Reminder: only saved screens were read; this is not a clearance search or legal advice.")


if __name__ == "__main__":
    sys.exit(main())
