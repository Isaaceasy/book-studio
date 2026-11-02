---
name: royalty-report
description: Turns the owner's real KDP sales and royalty exports (and optionally Amazon Ads exports) into clear reports per book, marketplace, format and month: units, royalties by currency, print-cost and royalty checks, trends and returns, with honest labelling of estimates. Never invents sales or earnings and never adds different currencies together without an owner-supplied rate. Use monthly or on request.
---

# /royalty-report: REAL SALES AND ROYALTY REPORTING

## Purpose
GENIE Max "royalty reporting: organizes real sales and royalty information into clear performance reports; no invented sales figures or earnings claims".

## Inputs
The owner's real exports from their KDP Reports (royalty estimator, month-to-date, prior-month royalties, orders and KENP exports as CSV or XLSX files placed in `reports/inbox/`), optional Amazon Ads exports (for `ads-manager`), and exchange rates only if the owner supplies them.

## Procedure
1. **Inventory the files** (`reports/inbox/`): list each file, its period, marketplaces and columns found. If columns are not recognized, show the header row and ask; never guess a mapping.
2. **Normalize** with `python scripts/royalty_report.py reports/inbox/ --out reports/` (reads CSV and XLSX; maps common KDP export columns: title, ASIN or ISBN, format, marketplace, units sold or ordered, units refunded, royalty type and rate, royalty, currency, date). It keeps each currency separate, flags missing columns, and writes `reports/summary.csv` and `reports/report-YYYY-MM.md`.
3. **Report** per book, marketplace, format and month: units, refunds, royalty per unit, royalty by currency, KENP pages read if present, best and worst months, and a trend note. When the owner supplied rates, add a converted total labelled with the rates and dates used; otherwise show currencies separately.
4. **Sanity checks**: royalty per paperback unit versus the computed value from the live print-cost table and list price (flag deviations, which may come from marketplace price differences or expanded distribution at 40 percent); refund rates; units with zero royalty.
5. **Ads join (optional)**: if ads exports exist, show spend versus sales and royalty per marketplace (never total ad sales as profit): net contribution = royalty minus ad spend, per currency.
6. **Insights**: three plain observations backed by the numbers (for example which marketplace over- or under-performs a title, price tests worth running, editions worth adding). Label estimates and unknowns.
7. **Taxes and payments are out of scope**; say so if asked and suggest the owner consult a professional.

## Rules
- Only real data. If the data is partial, the report states the gap. No earnings claims for marketing.
- Never add figures in different currencies without an owner-provided rate.
