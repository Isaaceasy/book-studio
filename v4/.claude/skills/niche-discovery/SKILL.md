---
name: niche-discovery
description: Optional stage before /new-book. Finds and evaluates book opportunities from live marketplace signals (bestseller subcategories, rising newcomers, autocomplete, price bands, competition patterns, category fit) and returns a ranked shortlist of 5 to 10 niches with evidence, a recommended pick and the format to test. Use when the owner has no idea yet, wants alternatives to a NO-GO, or wants to expand the catalog.
---

# /niche-discovery: FIND AND VALIDATE BOOK OPPORTUNITIES

## Purpose
GENIE Pro "niche discovery and validation": find niches worth entering using current marketplace signals, buyer intent, competition patterns and category fit, then validate the best with a short CMS pass. Evidence only; no invented sales numbers.

## Research gate
Same Mandatory Research Gate as `/cms-research`: live research, Research Proof block, honest limitations, no signing in, no fabricated actions.

## Inputs
The owner's interests, languages, profiles they can produce, budget for figures and review (some niches need expert clearance), existing catalog (`books/`), and optional exports the owner has (for example their own KDP or ads reports, saved research files).

## Procedure
1. **Frame the search.** Ask one question block: broad area or none, languages and marketplaces, profiles to avoid, whether expert review is available, preferred formats (low, medium or high production effort), and revenue goal per book (as a target, not a promise).
2. **Scan categories.** Open the relevant Amazon bestseller subcategories and "New Releases" lists and record: category path, number of top-100 titles that are under 12 months old, price range, format mix, and the presence of big publishers. Rising newcomers ranking well signal room for new books.
3. **Collect seed ideas** (aim for 15 to 25) from: subcategory gaps, autocomplete on audience and problem phrases, Google trend language, questions in public forums (read-only), seasonal angles with lead time, and the owner's catalog adjacencies.
4. **Score each idea** (table): demand evidence (ranks seen), competition strength (rating counts, publisher size, age of leaders), price band and unit economics for the likely format (compute from live KDP print-cost pages), production effort (length, figures, expert review), policy risk (medical or financial claims, trademark-dominated terms, AI-flood niches), differentiation potential (visible gaps), and expansion potential (editions, series, puzzles, workbooks). Score 1 to 5 each; show the arithmetic and the evidence rows.
5. **Short-list 5 to 10** and for the top 3 run a mini-CMS: 8 to 10 competitors each, USP lines, one gap, a candidate product format and price band.
6. **Recommend** one niche with its first product format, the reasons, the main risk and what would change the verdict. State that this is evidence-based judgment, not a sales prediction.
7. **Write** `niche-discovery.md` (Research Proof, method, seed list, scoring table, shortlist, mini-CMS summaries, recommendation, limitations) in the workspace root `research/` folder (create it) and stop. Ask the owner to pick a niche; then run `/new-book` with it. Do not start any book until the owner approves.

## Rules
- Autocomplete and rank are signals, not proof of sales or profitability.
- Never recommend a niche whose main appeal depends on trademarks, brand names or public figures.
- Flag niches where Amazon's content rules are strict (health and financial claims, children's content, public-domain duplicates, low-content books) and say what extra checks apply.
