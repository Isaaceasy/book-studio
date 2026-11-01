#!/usr/bin/env python3
"""Analyze the owner's real Amazon Ads exports and propose actions by explicit rules.

Usage:
  python scripts/ads_analyze.py --search-terms "Search_Term_*.csv" --targeting "Targeting_*.csv" \
         --breakeven 0.25 --out ads/analysis [--min-clicks-down 15 --min-clicks-negate 10 --min-asin-negate 5]

Inputs are CSV exports from Amazon Ads (Sponsored Products). Recognized columns (case-insensitive):
  Search Term report: Customer search term, Keywords, Impressions, Clicks, Total cost (XXX), Purchases, Sales (XXX), ACOS
  Targeting report:   Budget currency, Campaign name, Ad group name, Targeting, Targeting match type, Impressions, Clicks,
                      Total cost, Purchases, Sales
Currencies are kept SEPARATE; amounts in different currencies are never added together.
Rules (defaults from the owner's Manual Campaign Plan; change with options or ads/ads-rules.yaml):
  HARVEST  : purchases >= 1 and ACOS <= break-even  -> add as Exact (and negate in the source campaign)
  NEGATE   : clicks >= N with 0 purchases (search terms N=10, ASIN targets N=5)
  BID DOWN : clicks >= 15 and ACOS > break-even (lower bid ~20%)
  BID UP   : ACOS <= 0.5 x break-even and purchases >= 2 (raise bid ~15% if the campaign hits budget early)
  WATCH    : everything else with spend
A single order can drive ACOS (multi-unit orders): terms whose sales come from 1 purchase are flagged LOW-CONFIDENCE.
Outputs: summary.md and actions.csv in the output folder. Real data only; no performance promises.
"""
import argparse
import csv
import glob
import os
import re
import sys
from collections import defaultdict


AUTO_TARGETS = {"close-match", "loose-match", "substitutes", "complements"}


def num(x):
    if x is None:
        return 0.0
    x = str(x).strip().replace("%", "").replace(",", "")
    try:
        return float(x)
    except ValueError:
        return 0.0


def read_csv(path):
    with open(path, encoding="utf-8-sig", errors="replace", newline="") as fh:
        return list(csv.DictReader(fh))


def pick(row, *names):
    low = {k.lower(): v for k, v in row.items() if k}
    for n in names:
        for k in low:
            if k.startswith(n.lower()):
                return low[k]
    return None


def cur_from_header(row, base):
    for k in row:
        m = re.match(rf"{base}\s*\(([A-Za-z]{{3}})\)", k or "", re.I)
        if m:
            return m.group(1).upper()
    return "?"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--search-terms", nargs="*", default=[])
    ap.add_argument("--targeting", nargs="*", default=[])
    ap.add_argument("--breakeven", type=float, default=0.25, help="break-even ACOS = royalty per copy / list price")
    ap.add_argument("--min-clicks-down", type=int, default=15)
    ap.add_argument("--min-clicks-negate", type=int, default=10)
    ap.add_argument("--min-asin-negate", type=int, default=5)
    ap.add_argument("--out", default="ads/analysis")
    a = ap.parse_args()

    agg = defaultdict(lambda: {"imp": 0, "clk": 0, "cost": 0.0, "ord": 0, "sales": 0.0, "src": set()})
    files = []
    for pat in a.search_terms:
        files += [("term", f) for f in (glob.glob(pat) or [pat])]
    for pat in a.targeting:
        files += [("target", f) for f in (glob.glob(pat) or [pat])]
    if not files:
        sys.exit("No input files. Provide --search-terms and/or --targeting CSV exports.")
    for kind, f in files:
        rows = read_csv(f)
        if not rows:
            continue
        for r in rows:
            if kind == "term":
                key_text = pick(r, "Customer search term")
                cur = cur_from_header(r, "Total cost")
                camp = pick(r, "Keywords") or ""
                cost = num(pick(r, "Total cost"))
                sales = num(pick(r, "Sales"))
            else:
                key_text = pick(r, "Targeting")
                cur = (pick(r, "Budget currency") or "?").upper()
                camp = pick(r, "Campaign name") or ""
                cost = num(pick(r, "Total cost"))
                sales = num(pick(r, "Sales"))
            if not key_text:
                continue
            is_asin = bool(re.fullmatch(r"[Bb0-9][A-Za-z0-9]{9}", key_text.strip())) or key_text.lower().startswith("asin=")
            k = (kind, cur, key_text.strip().lower(), "asin" if is_asin else "text")
            d = agg[k]
            d["imp"] += num(pick(r, "Impressions"))
            d["clk"] += num(pick(r, "Clicks"))
            d["cost"] += cost
            d["ord"] += num(pick(r, "Purchases"))
            d["sales"] += sales
            d["src"].add(os.path.basename(f))

    be = a.breakeven
    actions = []
    for (kind, cur, text, tp), d in agg.items():
        clicks, orders, cost, sales = d["clk"], d["ord"], d["cost"], d["sales"]
        acos = cost / sales if sales > 0 else None
        neg_n = a.min_asin_negate if tp == "asin" else a.min_clicks_negate
        if text in AUTO_TARGETS:
            # Amazon's automatic-targeting groups are not keywords: manage the group bid, never harvest or negate them
            if cost <= 0:
                continue
            act = "AUTO-TARGET GROUP (adjust group bid by ACOS; not harvestable)"
        elif orders >= 1 and acos is not None and acos <= be:
            act = "HARVEST (add as Exact; negate in source campaign)"
        elif clicks >= neg_n and orders == 0:
            act = "NEGATE (clicks without a sale)"
        elif clicks >= a.min_clicks_down and acos is not None and acos > be:
            act = "BID DOWN ~20%"
        elif acos is not None and acos <= 0.5 * be and orders >= 2:
            act = "BID UP ~15% if budget-limited"
        elif cost > 0:
            act = "WATCH"
        else:
            continue
        conf = "LOW-CONFIDENCE (1 order or <15 clicks)" if (orders <= 1 or clicks < 15) else "ok"
        actions.append([kind, cur, text, tp, int(d["imp"]), int(clicks), round(cost, 2), int(orders), round(sales, 2),
                        "" if acos is None else round(acos, 4), act, conf, ";".join(sorted(d["src"]))])

    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, "actions.csv"), "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["kind", "currency", "term_or_target", "type", "impressions", "clicks", "cost", "orders", "sales", "acos", "action", "confidence", "files"])
        w.writerows(sorted(actions, key=lambda r: (r[1], r[10], -r[6])))

    # summary per currency
    tot = defaultdict(lambda: {"cost": 0.0, "sales": 0.0, "orders": 0})
    for r in actions:
        if r[0] == "target":
            t = tot[r[1]]
            t["cost"] += r[6]; t["sales"] += r[8]; t["orders"] += r[7]
    lines = [f"# Ads analysis (break-even ACOS {be:.0%})", "", "Currencies are kept separate. Real exports only; no performance promises.", ""]
    for cur, t in sorted(tot.items()):
        acos = (t["cost"] / t["sales"]) if t["sales"] else None
        lines.append(f"- {cur} (targeting reports): spend {t['cost']:.2f}, sales {t['sales']:.2f}, orders {int(t['orders'])}, ACOS {('n/a' if acos is None else f'{acos:.1%}')}")
    counts = defaultdict(int)
    for r in actions:
        counts[r[10].split(" ")[0]] += 1
    lines += ["", "## Action counts", ""] + [f"- {k}: {v}" for k, v in sorted(counts.items())]
    lines += ["", "## Top harvest candidates (lowest ACOS, most orders)", ""]
    for r in sorted([r for r in actions if r[10].startswith("HARVEST")], key=lambda r: (-r[7], r[9] if r[9] != "" else 9))[:15]:
        lines.append(f"- [{r[1]}] {r[2]} ({r[3]}): {r[5]} clicks, {r[7]} orders, ACOS {r[9]}, {r[11]}")
    lines += ["", "## Biggest waste (negate candidates by spend)", ""]
    for r in sorted([r for r in actions if r[10].startswith("NEGATE")], key=lambda r: -r[6])[:15]:
        lines.append(f"- [{r[1]}] {r[2]} ({r[3]}): {r[5]} clicks, cost {r[6]}, 0 orders")
    lines += ["", "Apply changes yourself in Amazon Ads; Claude never edits campaigns.", ""]
    open(os.path.join(a.out, "summary.md"), "w", encoding="utf-8").write("\n".join(lines))
    print(f"Read {len(files)} file(s); {len(actions)} actionable rows. Wrote {a.out}/summary.md and actions.csv")
    return 0


if __name__ == "__main__":
    sys.exit(main())
