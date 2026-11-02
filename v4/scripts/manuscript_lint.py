#!/usr/bin/env python3
"""Manuscript linter: the mechanical checks from CLAUDE.md, run in seconds on a whole book.

Usage: python scripts/manuscript_lint.py books/<slug> [--json] [--strict]
Reads book.yaml, then every .md in front/, chapters/, back/ (and the book root files that carry the title).
Checks (heuristics; a human or the editor agent still reads the text):
  PLACEHOLDER  TODO, TBD, lorem, XXX, [INSERT ...], {{...}}, bracketed ALL-CAPS instructions
  LINK         http(s)://, www., markdown links, doi: (skipped for doi/URL when citation_mode allows plain-text refs)
  PHRASE       banned filler phrases from CLAUDE.md section 6
  OPENERS      sentence openers repeated too often (Moreover, Furthermore, Additionally)
  DASH         em-dash density per 1,000 words
  WORDS        chapter word count against chapter_word_floor / ceiling in book.yaml (tables and callout titles excluded roughly)
  NAME         author / title spelling variants across files (near-miss detection)
  BIAS         answer keys where the correct option is the longest option (needs answer-keys and the chapter's lettered options)
  CITATION     bracketed numeric citations when citation_mode is none
Exit code 1 when any ERROR is found (WARN never fails unless --strict).
"""
import difflib
import json
import os
import re
import sys

try:
    import yaml
except ImportError:
    sys.exit("pyyaml missing: pip install pyyaml")

BANNED = [
    "in today's fast-paced world", "in the ever-evolving landscape", "have you ever wondered", "it's no secret that",
    "let's dive in", "delve", "unlock", "unleash", "embark on a journey", "in conclusion", "game-changer", "navigate the complexities",
    "it is important to note that", "a testament to",
]
OPENERS = ["moreover", "furthermore", "additionally"]
PLACEHOLDER = re.compile(r"\b(TODO|TBD|FIXME|XXX|lorem ipsum)\b|\[(INSERT|ADD|PLACEHOLDER|TO BE|FIGURE SLOT)[^\]]*\]|\{\{[^}]*\}\}", re.I)
LINK = re.compile(r"https?://|www\.\S+\.\S+|(?<!!)\[[^\]]*\]\((?!images/)[^)]*\)", re.I)  # images ![..](images/..) are allowed
DOI = re.compile(r"\bdoi:\s*\S+|10\.\d{4,9}/\S+", re.I)
NUMCITE = re.compile(r"\[\d+(?:[,–\-]\s*\d+)*\]")


def strip_md(text):
    text = re.sub(r"^:::.*$", "", text, flags=re.M)
    text = re.sub(r"\{[^}]*\}", "", text)
    text = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"[#*_`>|]", " ", text)
    return text


def words(text):
    return len(re.findall(r"[A-Za-z0-9À-ɏ'’-]+", strip_md(text)))


def body_words(text):
    """Word count excluding table rows and image lines (rough match to 'excluding tables')."""
    keep = [l for l in text.splitlines() if not l.strip().startswith("|") and not l.strip().startswith("![")]
    return words("\n".join(keep))


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    book = sys.argv[1]
    strict = "--strict" in sys.argv
    cfg = yaml.safe_load(open(os.path.join(book, "book.yaml"), encoding="utf-8"))
    cit = str(cfg.get("citation_mode", "none"))
    floor = cfg.get("chapter_word_floor")
    ceil = cfg.get("chapter_word_ceiling")
    findings = []  # (level, code, file, line, message)

    def add(level, code, f, line, msg):
        findings.append((level, code, os.path.relpath(f, book) if f else "", line, msg))

    files = []
    for sub in ("front", "chapters", "back"):
        d = os.path.join(book, sub)
        if os.path.isdir(d):
            for n in sorted(os.listdir(d)):
                if n.endswith(".md"):
                    files.append(os.path.join(d, n))
    for n in ("brief.md",):
        pass
    totals = {}
    all_text = {}
    for f in files:
        t = open(f, encoding="utf-8").read()
        all_text[f] = t
        lines = t.splitlines()
        for i, l in enumerate(lines, 1):
            m = PLACEHOLDER.search(l)
            if m:
                add("ERROR", "PLACEHOLDER", f, i, f"placeholder text: {m.group(0)[:40]}")
            if LINK.search(re.sub(r"!\[[^\]]*\]\([^)]*\)", "", l)):
                add("ERROR", "LINK", f, i, "hyperlink or URL in manuscript (rule 3)")
            if DOI.search(l) and cit == "none":
                add("ERROR", "LINK", f, i, "DOI in manuscript while citation_mode is none")
            low = l.lower()
            for ph in BANNED:
                if re.search(r"\b" + re.escape(ph) + r"\b", low):
                    add("WARN", "PHRASE", f, i, f"banned phrase: {ph}")
            if cit == "none" and NUMCITE.search(l) and not l.lstrip().startswith(("|", "![")):
                add("WARN", "CITATION", f, i, "bracketed number looks like a citation while citation_mode is none")
        plain = strip_md(t).lower()
        n = max(1, words(t))
        for o in OPENERS:
            c = len(re.findall(r"(?:^|[.!?]\s+)" + o + r"\b", plain))
            if c >= 3:
                add("WARN", "OPENERS", f, 0, f"'{o}' opens {c} sentences")
        dashes = t.count("—")
        if dashes / n * 1000 > 6:
            add("WARN", "DASH", f, 0, f"{dashes} em-dashes ({dashes / n * 1000:.1f} per 1,000 words)")
        if "/chapters" in f.replace("\\", "/") or os.sep + "chapters" + os.sep in f:
            bw = body_words(t)
            totals[f] = bw
            if floor and bw < floor:
                add("ERROR", "WORDS", f, 0, f"{bw} words, floor {floor} (UNDER-FLOOR unless recorded in status.md)")
            if ceil and bw > ceil * 1.1:
                add("WARN", "WORDS", f, 0, f"{bw} words, ceiling {ceil}")

    # NAME consistency: author and title variants
    author = str(cfg.get("author", "")).strip()
    title = str(cfg.get("title", "")).strip()
    for label, canon in (("author", author), ("title", title)):
        if not canon:
            continue
        pat = re.compile(r"\b" + r"\s+".join(re.escape(w) for w in canon.split()[:2]) + r"\w*", re.I)
        seen = {}
        for f, t in all_text.items():
            for m in pat.finditer(t):
                seen.setdefault(m.group(0), []).append(f)
        for variant, fl in seen.items():
            if variant != canon.split()[0] + " " + canon.split()[1] and not canon.startswith(variant):
                add("WARN", "NAME", fl[0], 0, f"{label} variant '{variant}' differs from book.yaml '{canon}'")
        # near-miss on full canonical string
        if label == "author":
            for f, t in all_text.items():
                for m in re.finditer(r"\b[A-Z][a-z]+ [A-Z][a-z]+ [A-Z][a-z]+\b", t):
                    s = m.group(0)
                    r = difflib.SequenceMatcher(None, s.lower(), canon.lower()).ratio()
                    if 0.8 <= r < 1.0:
                        add("ERROR", "NAME", f, 0, f"near-miss of author name: '{s}' vs '{canon}'")

    # BIAS: answer keys "N. X." where X is the letter; compare lengths of lettered options in the matching chapter
    keys = [f for f in all_text if "answer-key" in os.path.basename(f)]
    chapter_files = [f for f in all_text if os.sep + "chapters" + os.sep in f]
    longest_hits = tot = 0
    for kf in keys:
        m = re.search(r"part(\d+)", os.path.basename(kf))
        if not m:
            continue
        num = int(m.group(1))
        cands = [c for c in chapter_files if re.search(r"ch0*%d\b" % num, os.path.basename(c))]
        if not cands:
            continue
        ctext = all_text[cands[0]]
        opts = {}
        for ln in ctext.splitlines():
            om = re.match(r"^\s*(\d+)\.\s+(.*)", ln)
            lm = re.match(r"^\s*\(?([A-D])[\.\)]\s+(.*)", ln)
            if om:
                cur = int(om.group(1))
                opts.setdefault(cur, {})
            elif lm and opts:
                opts[cur][lm.group(1)] = len(lm.group(2))
        for ln in all_text[kf].splitlines():
            km = re.match(r"^\s*(\d+)\.\s+([A-D])\.", ln)
            if km and int(km.group(1)) in opts and len(opts[int(km.group(1))]) == 4:
                q = opts[int(km.group(1))]
                tot += 1
                if max(q, key=q.get) == km.group(2):
                    longest_hits += 1
    if tot >= 8 and longest_hits / tot > 0.5:
        add("WARN", "BIAS", "", 0, f"correct option is the longest in {longest_hits}/{tot} questions ({100 * longest_hits // tot}%): rebalance option lengths")

    errs = [f for f in findings if f[0] == "ERROR"]
    warns = [f for f in findings if f[0] == "WARN"]
    if "--json" in sys.argv:
        print(json.dumps([dict(level=a, code=b, file=c, line=d, message=e) for a, b, c, d, e in findings], indent=1))
    else:
        print(f"MANUSCRIPT LINT: {book}")
        print(f"files: {len(files)} | chapters measured: {len(totals)} | citation_mode: {cit}")
        for f, w in sorted(totals.items()):
            print(f"  {os.path.basename(f)}: {w} body words")
        for lvl, code, f, line, msg in findings[:200]:
            print(f"{lvl:<5} {code:<11} {f}{(':' + str(line)) if line else ''}  {msg}")
        if len(findings) > 200:
            print(f"... {len(findings) - 200} more")
        print(f"RESULT: {len(errs)} error(s), {len(warns)} warning(s)")
    sys.exit(1 if errs or (strict and warns) else 0)


if __name__ == "__main__":
    main()
