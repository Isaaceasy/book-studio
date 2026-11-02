---
name: ads-manager
description: Builds and maintains Amazon Ads plans for the owner's books: campaign structure (auto, keyword, product-target), bid logic from the owner's break-even ACOS, bulk sheets for manual upload, and weekly optimization from the owner's real Search Term and Targeting report exports (harvest winners, negate losers, adjust bids) with honest performance mathematics. Never creates or edits campaigns in an account; the owner uploads and clicks.
---

# /ads-manager: CAMPAIGN PLANS AND WEEKLY OPTIMIZATION FROM REAL DATA

## Purpose
GENIE Max "ads manager: campaign creation, weekly optimization, budget awareness and honest performance mathematics based on real campaign data". It reproduces the method in the owner's `Manual_Campaign_Plan.xlsx` (built from their Search Term and Targeting reports) and makes it repeatable for every book and marketplace.

## Inputs
The owner's real exports (never invented): Sponsored Products **Search Term** reports (columns seen: customer search term, keywords, impressions, clicks, total cost, purchases, sales, ACOS, KENP read) and **Targeting** reports (columns seen: budget currency, date range, campaign, ad group, targeting, match type, bid, impressions, clicks, CTR, total cost, purchases, sales, units, ROAS and more), by month and marketplace; the book's price and royalty per copy (from `/cms-research` or `reports/`); the owner's stated **break-even ACOS** (their plan used 25%; ask each book, because break-even ACOS = royalty per copy / list price); `final/KDP-metadata.md` (keywords); `competitors.csv` (product targets).

## Procedure
1. **Set the economics.** Compute break-even ACOS for each book and marketplace: royalty / price. Target ACOS below break-even; record the owner's rule thresholds in `ads/ads-rules.yaml` (defaults from the owner's plan: lower bid 20% after 15+ clicks with ACOS above break-even; raise bid 15% when ACOS under about half of break-even and the campaign hits budget early; negate a keyword after 10 clicks with no sale; negate an ASIN target after 5 clicks with no sale; add converting search terms as Exact and as Negative Exact in the campaign they came from; keep autos on at low bids for discovery; tiers A/B/C from ACOS and order count; single-sale terms bid lower).
2. **Analyze real data** with `python scripts/ads_analyze.py --search-terms <csv...> --targeting <csv...> --breakeven 0.25 --out ads/analysis/`: aggregates by search term and target across months and currencies (keep currencies separate; never add EUR to USD), computes clicks, spend, orders, sales, ACOS, conversion rate and confidence (orders and clicks), and applies the rules to list **harvest** (converting terms to add as Exact), **negate** (wasteful terms), **bid down**, **bid up**, and **watch** items. Multi-unit group orders can distort ACOS: flag terms whose sales are driven by one order.
3. **Plan structure** (`ads/campaign-plan.md`): per marketplace and book: an auto campaign (discovery), a phrase or broad keyword campaign, an exact campaign (proven terms), a product-targeting campaign (competitor ASINs from the CMS research, no brand misuse in ad copy), budgets as daily caps in local currency, "Dynamic bids: down only" unless the owner chooses otherwise, and negative lists. Note that book ads are sponsored ads (Sponsored Products and possibly Sponsored Brands); verify live eligibility and creative rules before suggesting formats.
4. **Bulk sheets for manual upload**: write CSV or XLSX files in the layout the owner can paste or upload (campaign, ad group, keyword, match type, bid, negatives); verify against Amazon Ads' current bulk-sheet help page before claiming a format.
5. **Weekly review report** (`ads/weekly/YYYY-MM-DD.md`): spend, sales, ACOS versus break-even, top winners and losers, actions list with exact bid changes, what to add as negatives, what to watch, and a plain statement of confidence (small samples are not conclusions). No promise of results.
6. **Honest math section**: show royalty per copy, break-even ACOS, spend needed per sale at the current conversion rate, the minimum clicks needed before a decision, and that ad sales are not all profit.
7. **Compliance**: ad copy must follow Amazon Ads policies (no unverifiable claims, no competitor names, no prices in some creatives, no review quotes); `/amazon-compliance` scope `ads`.

## Rules
- Use only the owner's real exports. If none exist, produce a launch plan with explicit assumptions and no performance numbers.
- Never log in to Amazon Ads, create or edit campaigns, change budgets or spend money. The owner applies the changes.
- Do not exaggerate: ACOS, not hope, decides.
