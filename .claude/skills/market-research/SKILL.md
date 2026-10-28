---
name: market-research
description: Stage 1 MARKET RESEARCH. Runs live research on Amazon (and Google) to verify the profitability of an idea or title and to perform a gap analysis of the niche, with a Research Proof block and a GO / CAUTION / NO-GO verdict. Mandatory for every new idea and every title, subtitle or niche change, before any writing.
---

# /market-research — Stage 1: LIVE AMAZON PROFITABILITY CHECK + GAP ANALYSIS

## Purpose
The owner's rule: for every idea given or title picked, a part of the system must do live research on Amazon to verify profitability and do a gap analysis of the niche or title. This skill is that part. It must never run from memory. It produces evidence the owner can inspect.

## MANDATORY RESEARCH GATE (read first, applies to everything below)
1. Live research is compulsory and unconditional. It may not be skipped, softened, deferred, or replaced by prior knowledge, and it does not depend on a browser being available.
2. Make at least one genuine web search or browsing tool call before writing any finding. Baseline tool: WebSearch / WebFetch. Preferred tool: a connected browser (Claude in Chrome or the built-in browser) so the owner can watch.
3. Put a "Research Proof" block at the very top of `market-research.md`: today's date, the plain-language log of every browser action the owner approved and every page actually visited, every search query run, and 3 to 8 specific findings each with its source (for example autocomplete phrases observed, competing-title wording, category names, bestseller subcategories, BSR values seen). Record only what actually happened.
4. If NO web search or browsing tool of any kind is available, stop and reply exactly: "I cannot complete this task as specified because no live web-search or browsing tool is enabled in this session. Please run me in a Claude surface with web access." Do not continue from prior knowledge.
5. Never claim to have opened a browser, searched Google, visited Amazon, changed the delivery location, used autocomplete, examined bestseller lists, operated Chrome, or used an extension unless that action was actually completed. Never sign in to the owner's account, buy anything, or change any account setting.
6. Do not write conclusions before the Research Proof block is filled with real results.

## Inputs
`brief.md`, `book.yaml` (profile, language, region, marketplace), the idea or working title. Nothing else is required.

## Step-by-step procedure

### Step 1 — Plan and permission
1. Read the brief. Decide the marketplace: the one in the brief (default Amazon.com United States, Books or Kindle Store department; for fr/de/es books use amazon.fr / amazon.de / amazon.es or .com.mx and research in that language, because English keywords do not transfer).
2. Write the research plan in 6 to 10 lines: seed terms (from the idea, audience, problem, subtopics, alternative phrasing), the Amazon pages you will open (search results, bestseller subcategories, 10 to 20 competing book pages), and the Google searches you will run.
3. Ask the owner ONE question with AskUserQuestion about browser permission:
   - "Approve the whole research plan once (recommended). I will announce each step as I do it." 
   - "Ask me before every single browser action."
   - "Do not use my browser; use web search only."
   Follow the answer exactly. If the owner chose step-by-step approval, before every browser action (open browser, go to a site, change delivery location, run a search, open a page) say in plain words what you are about to do and wait for a clear yes. After each action say briefly what you did and found. If no browser is connected, say so plainly, ask the owner to connect Claude in Chrome (or continue with web search only if they cannot), and clearly state the limitation in the report.
4. Ground rules for the browser: use a clean or private session where possible; set the delivery location to a general ZIP code for the US marketplace (for example 90001) only after permission and confirm what is showing; select the Books or Kindle Store department; never sign in.

### Step 2 — Demand and keyword evidence (live)
For each important seed term:
1. Type it into the Amazon search bar and record the native autocomplete suggestions that are relevant to the idea. Test words before and after the term, singular and plural, audience variants, problem variants, application variants, beginner/advanced/professional/handbook/workbook variants only where they fit.
2. Open the most promising search-result pages. Confirm the results match the idea and the intended reader. Reject phrases that return mostly unrelated products.
3. Run relevant Google searches to see how readers and practitioners phrase the problem and whether the subject is current. Cross-check important findings with an official or authoritative source.
Remember: autocomplete suggestions are a signal of common wording. They do NOT prove search volume, profitability, low competition, sales or buyer intent. Never claim they do.

### Step 3 — Competitor sampling (live)
Open at least 10 (target 15 to 20) directly competing book pages from the relevant search results and nonfiction bestseller subcategory pages (not only the general bestseller page). For each record ONLY what you can see on the page:
- Title and subtitle wording (names of authors and brands are allowed in this internal research file only, never in the manuscript, description or keywords).
- Format and price; page count; publication date and edition; publisher type if visible.
- Best Sellers Rank values shown (overall and category), rating and number of ratings, any "bought in past month" style badge if displayed.
- Table of contents or "Look inside" topics if visible; description structure; cover and interior quality impression only if a preview is visible.
- Recurring themes in the visible customer reviews (praise and complaints), summarised in your own words; no long quotations.
If a field is not visible, write NOT SEEN. Never guess a value.

### Step 4 — Profitability assessment (evidence-based, honest)
1. **Demand signals** actually observed: how many of the sampled titles show strong rank values, how many are recent (under 12 months) and ranking well (a sign that newcomers can succeed), how many different books fill the first results, whether autocomplete shows the term strongly, whether Google shows sustained interest.
2. **Competition signals**: how many sampled titles have large review counts, how many are by large publishers, how old the leaders are, how many of the top titles are low quality or outdated.
3. **Price band**: observed list prices for similar books and page counts.
4. **Unit economics** (compute, do not guess): open KDP's current royalty and printing-cost pages, record the royalty rate rules and the printing-cost formula for the planned trim, page count and ink type (Word-format books: US Letter, black-and-white or color as in the brief), and calculate royalty per paperback at 3 candidate prices using the observed price band. Show the arithmetic and the source page and date. State that print cost varies by marketplace and options.
5. **Sales volume**: Amazon does not publish sales. Do NOT invent sales numbers. You may describe rank bands qualitatively (strong, moderate, weak, unknown) from observed ranks. If you quote any rank-to-sales conversion, it must come from a real page you opened (name and date), be labelled as a third-party rough estimate with its limits, and be shown as a range, never as a promise.
6. **Verdict**: GO (clear demand evidence, beatable competition, positive unit economics at a realistic price), CAUTION (mixed or thin evidence; state exactly what is uncertain and what would settle it), or NO-GO (weak demand, dominated niche, negative economics, or policy risk). Give the reasons in 5 to 8 lines. State plainly that this is evidence-based judgment, not a prediction or guarantee of sales.

### Step 5 — Gap analysis (live evidence only)
Compare the sampled books and reviews with the idea and report real gaps:
- **Content gaps**: subtopics, chapters, levels or use-cases that readers ask for in reviews or that competing tables of contents miss.
- **Quality gaps**: outdated editions, weak structure, errors readers complain about, poor formatting, thin content.
- **Audience gaps**: reader levels or professions poorly served (for example only beginner books, no professional handbook).
- **Format gaps**: no workbook, no large-print, no hardcover, no worked-example edition, no localized edition.
- **Language / region gaps**: strong niche on one marketplace but little in another language (verify on that marketplace before claiming).
- **Positioning options**: 2 to 3 specific positioning statements that exploit the verified gaps, each tied to evidence.
Output a table: gap, evidence (which pages), how the book will address it, risk. Mark each gap CONFIRMED (seen on at least 3 sampled pages or in repeated review themes) or POSSIBLE.

### Step 6 — Policy and risk screen
Note any red flags for Amazon compliance in this niche (medical claims, sensitive topics, trademarks dominating the niche, brand-name keyword dependence, many near-duplicate public-domain books). Link each to `profiles/amazon-compliance-checklist.md` checks. This is only a first screen; full review happens in `/amazon-compliance`.

### Step 7 — Write `books/<slug>/market-research.md`
Structure:
1. **Research Proof** (see gate item 3).
2. Idea / title researched, marketplace, date, tools used, limitations.
3. Seed terms and autocomplete evidence.
4. Competitor table (10 to 20 rows; NOT SEEN where applicable).
5. Demand signals; competition signals; price band; unit-economics table with arithmetic and sources.
6. Verdict (GO / CAUTION / NO-GO) with reasons.
7. Gap analysis table and positioning options.
8. Requirements handed to the outline: "must address" list (confirmed gaps), "must avoid" list (risk and policy flags), reader level and price band guidance.
9. Disclosures: what could not be checked, what is estimate, what would change the verdict.
Also export a Word copy: `pandoc market-research.md -o market-research.docx` (simple formatting is fine).

### Step 8 — Update `status.md` and stop at the gate
Reply with at most 6 lines: verdict, the top 2 reasons, the top 2 confirmed gaps, the recommended positioning, and "Approve this research and verdict, or tell me what to change." On NO-GO or CAUTION, offer concrete options (change angle, narrow the niche, change level, change marketplace, stop). Do not proceed to `/title-check` until the owner approves. Tick "Market research done" only after approval.

## Rules
- Research must be repeated (at least Steps 2 to 5 for the changed element) whenever the owner changes the idea, title, subtitle, niche, level or marketplace.
- Never fabricate browser actions, ranks, prices, review counts, search suggestions, sales numbers or evidence.
- Competitor names appear only in this internal file, never in the manuscript, subtitle options, description or keywords.
- Do not copy any competitor's text; summarise in your own words.
- If a competitor page cannot be opened, say so and sample another.
