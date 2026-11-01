---
name: cms-research
description: Stage 1 CMS RESEARCH (Copy Market Strategy). Runs deep live research on Amazon and Google for any title or idea, samples 15 to 25 real competitors, extracts each one's USP, runs the gap analysis, models the bestsellers (structure, keywords, price, format, interior and cover conventions) without copying them, computes unit economics for 2 to 3 product formats, and ends with an owner-approved PRODUCT SPEC and a GO / CAUTION / NO-GO verdict. Mandatory for every new idea and every title, niche, format or marketplace change, before any writing.
---

# /cms-research: Stage 1, COPY MARKET STRATEGY (live Amazon study)

## Purpose
The owner's rule: for every idea or title, study the niche live on Amazon, learn what the bestsellers do, find what they miss, and build a better, clearly different book from that evidence. This skill is the evidence engine. It never runs from memory and never invents a number.

## MANDATORY RESEARCH GATE (applies to everything below)
1. Live research is compulsory. It may not be skipped, softened or replaced by prior knowledge, and it does not depend on a browser being available.
2. Make at least one real web search or browsing tool call before writing any finding. Baseline: WebSearch / WebFetch. Preferred: a connected browser (the built-in browser pane or Claude in Chrome) so the owner can watch.
3. Put a **Research Proof** block at the top of `cms-research.md`: today's date, the plain-language log of every browser action and page actually visited, every search query run, the delivery location used, and 3 to 8 findings each with a source. Record only what actually happened.
4. If no web search or browsing tool of any kind is available, stop and reply exactly: "I cannot complete this task as specified because no live web-search or browsing tool is enabled in this session. Please run me in a Claude surface with web access."
5. Never claim to have opened a browser, searched, visited Amazon, changed the delivery location, used autocomplete, read a bestseller list, operated Chrome or used an extension unless it was actually done. Never sign in, buy, or change any account setting.
6. Do not write conclusions before the Research Proof block holds real results.

## Inputs
`brief.md`, `book.yaml` (profile, language, region, marketplace), the idea or working title, and (optional) any files the owner supplies: saved Amazon pages, keyword exports, review text they pasted, `interiors/INDEX.md`.

## Procedure

### Step 1. Plan and permission (one question)
1. Choose the marketplace (default amazon.com, Books or Kindle Store; for fr/de/es use amazon.fr, .de, .es or .com.mx and research in that language).
2. Write a 6 to 10 line research plan: seed terms (idea, audience, problem, subtopics, alternative phrasing, format words), pages to open, searches to run.
3. Ask ONE question (AskUserQuestion): approve the whole plan once (recommended) / ask before every browser action / web search only. Follow it exactly. If no browser is connected, say so plainly and state the limitation in the report.
4. Browser ground rules: clean or private session where possible; set the delivery location to a US ZIP (for example 90001) only after permission and confirm what shows (Amazon shows local prices and delivery by location: a non-US location shows foreign currency); select Books or Kindle Store; never sign in. Lessons learned: Amazon pages may fail with errors for fetch tools; the browser pane works better; review pages need a sign-in (ask the owner to paste reviews, or to sign in to their own browser and paste what they see).

### Step 2. Demand and keyword evidence (live)
For each important seed term type it into the real Amazon search box and record the native autocomplete suggestions (tests: before and after the term, singular and plural, audience, problem, application, format variants). Open the most promising result pages; reject phrases that return mostly unrelated products. Cross-check with Google searches and an official or authoritative source for currency. Autocomplete is a signal of common wording, NOT proof of volume, profitability, low competition, sales or buyer intent.
Useful browser technique (see `docs/cms-browser-snippets.md`): run a short script in the page to read result titles, prices, ratings and ASINs, and to fetch product-page details (price, print length, rank, publication date) instead of opening each page by hand.

### Step 3. Competitor sampling (live)
Sample at least 15, target 20 to 25, directly competing listings from the relevant search results and the MOST SPECIFIC bestseller subcategories (not only the general page). Include: top sellers, rising newcomers (under 12 months and ranking well), and weak but visible titles. Save them in `competitors.csv` (columns in `templates/competitors.csv`). Record ONLY what is visible, NOT SEEN otherwise:
title, subtitle, author or publisher type, format, trim, page count, price, publication date and edition, Best Sellers Rank (overall and category), rating and rating count, badges ("bought in past month" if shown), "Look inside" or contents topics, description structure, cover style (palette, imagery, type), interior style if a preview is visible, recurring review themes you can legitimately see (own words, no long quotes).
Names of authors and brands are allowed in this internal file only.

### Step 4. USP extraction (the heart of CMS)
For every sampled competitor write one line: its USP in plain words (who it targets, what it promises, how it is different), its format and price position, and its strongest and weakest point. Then cluster the competitors into 3 to 6 positioning groups (for example "huge textbook", "pocket reference", "exam prep", "illustrated beginner guide") and say which group sells best by rank evidence and which is thin.
Output the **USP table** and the **positioning map**.

### Step 5. Profitability assessment (evidence-based, honest)
1. Demand signals actually observed (ranks, recency, number of distinct books, autocomplete, Google interest).
2. Competition signals (rating counts, publisher size, age of leaders, quality of weak leaders).
3. Observed price bands by format.
4. **Unit economics for 2 to 3 candidate PRODUCT FORMATS** (for example compact 5 x 8 color, standard 6 x 9 black and white, premium large color): open KDP's live printing-cost and royalty pages, record the rules and date, and compute royalty per copy at 3 candidate prices for each format using the page estimate. Show the arithmetic. Print cost = fixed + pages x per-page, by trim class, ink and marketplace. Royalty = rate x list price minus print cost; ebook royalty options come from the live KDP page.
5. Sales volume: Amazon does not publish it. Describe rank bands qualitatively (strong, moderate, weak, unknown). If you quote any rank-to-sales estimate, it must come from a real page you opened (name and date), labelled a third-party rough estimate, as a range.
6. **Verdict**: GO / CAUTION / NO-GO with 5 to 8 lines of reasons; state that it is evidence-based judgment, not a prediction.

### Step 6. Gap analysis (live evidence only)
Content, quality, audience, format, price and localization gaps. Table: gap, evidence (which pages), how this book will address it, risk, status CONFIRMED (seen on at least 3 sampled pages or in repeated review themes) or POSSIBLE.

### Step 7. MODEL BLUEPRINT and DIFFERENTIATORS
Model the winners, never copy them. Write:
- **Title pattern** (head term first? audience in subtitle? number or promise? length) and **subtitle pattern**.
- **Keyword layers**: head terms, audience terms, problem terms, format terms (from autocomplete and titles).
- **Price band, length band, format and trim** that the best rankers use.
- **Interior conventions** of the niche (density, color, callouts, figures, tables) as seen in previews; pointer to candidate styles in `interiors/INDEX.md`.
- **Cover conventions** (palette families, imagery type, type treatment, thumbnail legibility).
- **Description structure** the winners use.
- **DIFFERENTIATORS**: 3 to 5 things this book does that none of the sampled books does, each tied to a confirmed gap.
- **Distance rule**: list what must NOT resemble any single competitor (title wording, cover look, interior layout, table of contents). Later stages check against this.

### Step 8. Policy and risk screen
Red flags for Amazon compliance in this niche (medical claims, income claims, trademark-dominated niches, brand-name keyword dependence, near-duplicate public-domain books, flooding of near-identical new titles). Link each to checks in `profiles/amazon-compliance-checklist.md`.

### Step 9. Write the three files
1. `cms-research.md`: Research Proof; idea and marketplace; seed terms and autocomplete evidence; competitor table (20 rows or as sampled); USP table and positioning map; demand, competition, price; unit-economics tables with arithmetic and sources; verdict; gap table; model blueprint and differentiators; requirements handed to the outline ("must address", "must avoid"); disclosures (what could not be checked, what is an estimate, what would change the verdict). Export a Word copy with pandoc if available.
2. `competitors.csv`: one row per sampled competitor.
3. `product-spec.md`: the PRODUCT SPEC for approval: chosen format, trim, ink, page and word target, parts or chapters target, figure target, price band, positioning statement, differentiators, run-time and cost notes, ebook plan, edition plan (hardcover, large print) if any. Lessons learned: decide trim, ink, length and price band NOW; changing them after the title or outline restarts research and wastes work.

### Step 10. Update `status.md` and stop at the gate
Reply with at most 6 lines: verdict, top 2 reasons, top 2 confirmed gaps, the recommended product spec, and "Approve this research and product spec, or tell me what to change." On NO-GO or CAUTION offer concrete options (change angle, narrow niche, change level, change format, change marketplace, stop). Do not proceed to `/title-lab` until the owner approves. Tick "CMS research done" only after approval.

## Rules
- Repeat Steps 2 to 7 for the changed element whenever the owner changes the idea, title, niche, level, format or marketplace.
- Never fabricate browser actions, ranks, prices, review counts, search suggestions, sales numbers or evidence.
- Competitor names appear only in this internal file, never in the manuscript, subtitle options, description, keywords or cover.
- Do not copy any competitor's text; summarise in your own words.
- If a competitor page cannot be opened, say so and sample another.
- New 2026-era listings with unusually long keyword-heavy subtitles and very high prices are common: record them as a competition signal, do not imitate them.
