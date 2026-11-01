#!/usr/bin/env python3
"""Summarize the owner's real KDP sales and royalty exports (CSV or XLSX).

Usage:
  python scripts/royalty_report.py reports/inbox/ --out reports/

Reads every .csv and .xlsx in the folder. For each file it looks for the header row (the first row that contains
'Title' and 'Royalty') and maps common KDP columns: Title, ASIN/ISBN, Marketplace, Royalty Type, Transaction Type,
Units Sold, Units Refunded, Net Units Sold, Royalty, Currency (names matched case-insensitively, by prefix).
Currencies are kept SEPARATE. Nothing is invented: unknown columns are reported, not guessed.
XLSX is read without extra libraries (zip + XML), first sheets only.
"""
import argparse
import csv
import os
import re
import sys
import zipfile
from collections import defaultdict
from xml.etree import ElementTree as ET


def read_xlsx(path):
    z = zipfile.ZipFile(path)
    ns = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
    shared = []
    if "xl/sharedStrings.xml" in z.namelist():
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.findall("m:si", ns):
            shared.append("".join(t.text or "" for t in si.iter("{%s}t" % ns["m"])))
    sheets = sorted(n for n in z.namelist() if re.match(r"xl/worksheets/sheet\d+\.xml", n))
    out = []
    for sn in sheets:
        root = ET.fromstring(z.read(sn))
        rows = []
        for row in root.iter("{%s}row" % ns["m"]):
            cells = {}
            for c in row.findall("m:c", ns):
                ref = c.get("r")
                col = re.match(r"[A-Z]+", ref).group(0)
                v = c.find("m:v", ns)
                val = None
                if v is not None:
                    val = shared[int(v.text)] if c.get("t") == "s" else v.text
                elif c.get("t") == "inlineStr":
                    val = "".join(t.text or "" for t in c.iter("{%s}t" % ns["m"]))
                cells[col] = val
            if cells:
                keys = sorted(cells, key=lambda s: (len(s), s))
                rows.append([cells.get(k) for k in keys])
        out.append(rows)
    return out


def read_any(path):
    if path.lower().endswith(".csv"):
        with open(path, encoding="utf-8-sig", errors="replace", newline="") as fh:
            return [list(csv.reader(fh))]
    if path.lower().endswith(".xlsx"):
        return read_xlsx(path)
    return []


def num(x):
    try:
        return float(str(x).replace(",", "").replace("%", ""))
    except Exception:
        return 0.0


def find_cols(header):
    h = [str(c or "").strip().lower() for c in header]

    def idx(*names):
        for n in names:
            for i, c in enumerate(h):
                if c.startswith(n):
                    return i
        return None
    return {
        "title": idx("title"), "asin": idx("asin/isbn", "asin", "isbn"), "market": idx("marketplace"),
        "rtype": idx("royalty type"), "ttype": idx("transaction type"), "sold": idx("units sold"),
        "refund": idx("units refunded"), "net": idx("net units sold"), "royalty": idx("royalty"),
        "cur": idx("currency"), "format": idx("format"), "date": idx("date", "month"),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("folder")
    ap.add_argument("--out", default="reports")
    a = ap.parse_args()
    files = [os.path.join(a.folder, f) for f in sorted(os.listdir(a.folder)) if f.lower().endswith((".csv", ".xlsx"))]
    if not files:
        sys.exit("No .csv or .xlsx files found. Export your reports from KDP and put them in the folder.")
    agg = defaultdict(lambda: {"sold": 0.0, "refund": 0.0, "net": 0.0, "royalty": 0.0})
    notes = []
    for f in files:
        used = False
        for sheet in read_any(f):
            hdr_i = next((i for i, r in enumerate(sheet) if r and any("title" in str(c or "").lower() for c in r) and any("royalty" in str(c or "").lower() for c in r)), None)
            if hdr_i is None:
                continue
            cols = find_cols(sheet[hdr_i])
            if cols["title"] is None or cols["royalty"] is None:
                continue
            used = True
            for r in sheet[hdr_i + 1:]:
                def g(k):
                    i = cols[k]
                    return r[i] if i is not None and i < len(r) else None
                title = (g("title") or "").strip()
                if not title:
                    continue
                key = (title, (g("market") or "?"), (g("rtype") or g("format") or "?"), (g("cur") or "?"))
                d = agg[key]
                d["sold"] += num(g("sold")); d["refund"] += num(g("refund")); d["net"] += num(g("net")) or (num(g("sold")) - num(g("refund")))
                d["royalty"] += num(g("royalty"))
        if not used:
            notes.append(f"{os.path.basename(f)}: no recognizable royalty table (header with Title and Royalty not found)")
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "summary.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["title", "marketplace", "royalty_type", "currency", "units_sold", "units_refunded", "net_units", "royalty"])
        for (t, m, rt, c), d in sorted(agg.items()):
            w.writerow([t, m, rt, c, d["sold"], d["refund"], d["net"], round(d["royalty"], 2)])
    cur_tot = defaultdict(float)
    for (t, m, rt, c), d in agg.items():
        cur_tot[c] += d["royalty"]
    lines = ["# Royalty report", "", "Real exports only. Currencies are shown separately; no conversion without an owner-supplied rate.", ""]
    lines += [f"- Total royalty {c}: {v:,.2f}" for c, v in sorted(cur_tot.items())]
    lines += ["", "## By title and marketplace", ""]
    for (t, m, rt, c), d in sorted(agg.items(), key=lambda kv: -kv[1]["royalty"])[:40]:
        lines.append(f"- {t} | {m} | {rt} | {c}: {int(d['net'])} net units, royalty {d['royalty']:,.2f}")
    if notes:
        lines += ["", "## Files not recognized", ""] + [f"- {n}" for n in notes]
    open(os.path.join(a.out, "report.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print(f"Read {len(files)} file(s); {len(agg)} rows. Wrote {a.out}/report.md and summary.csv")
    for n in notes:
        print("NOTE:", n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
