---
name: title-lab
description: Stage 2 TITLE LAB. Generates bestseller-modeled titles and subtitles from the CMS research using several keyword-composition techniques, checks every candidate for exact-match collision, autocomplete support, trademark and KDP-rule risk and distance from the modeled books, scores them in a table, and recommends one. Use after /cms-research is approved and before /title-check. Re-run whenever the idea, niche or product spec changes.
---

# /title-lab: Stage 2, BESTSELLER-MODELED TITLES

## Purpose
Create titles that follow what wins in the niche (structure and keyword composition) while being clearly different from any single bestseller, compliant with KDP and low in trademark risk. The owner gives an idea, niche or proposed title; this skill produces and tests candidates and recommends one. It never promises sales.

## Inputs
`cms-research.md` (model blueprint, autocomplete evidence, competitor titles), `competitors.csv`, `product-spec.md`, `book.yaml` (language, region), the owner's proposed title if any, `docs/kdp-specs.md` (title rules), `docs/lessons-learned.md`.

## Procedure

### A. Learn the winning title anatomy (from evidence)
From `competitors.csv` take the top 10 ranked titles and tabulate: head term position, role word (Guide, Manual, Handbook, Reference, Workbook), audience words, promise words, number words, length in characters, subtitle structure, and whether the subtitle repeats title words. State the dominant patterns and the open slots (patterns nobody uses). Lesson learned: short head term first plus a plain role word, audience in the subtitle, was the pattern of the best-ranking indie title in the niche we studied; generic head terms were crowded, so the subtitle carried the audience.

### B. Generate candidates with several keyword-composition techniques
Produce at least 15 title candidates (and 3 to 7 subtitles each for the finalists) using different techniques, labelled per candidate:
1. **Head-term first**: strongest autocomplete phrase leads (for example the exact two-word phrase readers type), role word second.
2. **Audience-first**: the reader group opens the title.
3. **Problem or outcome**: the reader's problem or benefit phrased naturally, no guarantees.
4. **Format-led**: format and depth in the title (Compact, Illustrated, Workbook, Field Guide), only if true.
5. **Question or situation** (nonfiction only, sparingly).
6. **Two-layer composition**: title carries the head term, subtitle carries 1 primary keyword theme plus audience (the owner's subtitle strategy: one primary keyword theme, a clear outcome or benefit).
7. **Long-tail composition**: subtitle assembled from the long-tail phrases found in autocomplete, read aloud for naturalness.
8. **Contrast technique**: for crowded head terms, a less crowded but still searched synonym.
For fiction and children's books the techniques are genre-appropriate (character, setting, promise, series pattern) and keywords go in the subtitle or metadata, not the title.

Rules for every candidate:
- Title plus subtitle under the live KDP limit (200 characters at last check); natural language, no keyword stuffing, no promotional words, no ranking claims, no prices.
- No brand, author, trademark, series-style phrase or competitor name; avoid formats that imitate established series ("Made Easy", "For Dummies" style patterns, "Pocket", "Secrets", "At a Glance", "Case Files" and the like) and avoid words that are registered marks for books in the niche (for example a common word such as "Essentials" is used in registered book marks).
- Low-repeat preference: the subtitle should not reuse significant title words, except ONE deliberate primary-keyword repeat flagged as intentional.
- Must match the product spec truthfully (never say Pocket for a 5 x 8 book; never "Illustrated" unless the figure plan supports it; never "Step-by-Step" unless delivered).
- Must be DISTINCT from every modeled book: no title shares its distinctive words in the same order.

### C. Test every finalist (live)
1. **Exact-match collision**: search Amazon (Books) for the title; count listings that start with the same words; note any famous title it resembles. The first result pages for a head term tell you who owns it.
2. **Autocomplete support**: type the head term into the real search box; record suggestions (signal only).
3. **Trademark pre-screen**: web search plus an owner step. The owner searches the USPTO trademark site (and the equivalent registry for other marketplaces) themselves and saves the result pages; run `python scripts/tm_scan.py <files>` to list live marks containing the title words in classes 9, 16 and 41, with owners and goods. Mark UNVERIFIED until a registry was actually searched; never mark LOW without it. Not legal advice.
4. **KDP rule check**: open the live metadata guidelines page, record the date.
5. **Distance check**: compare against the three closest competitor titles.

### D. Score and recommend
Table: candidate, technique, characters, collision count, autocomplete evidence, trademark status, distance, KDP rules, fit with product spec, and a 1 to 5 score for discoverability, clarity of promise, distinctiveness, and risk (lower is better). Recommend ONE with honest reasoning and name a runner-up for comparison. State it is a reasoned prediction, not a sales guarantee. A print subtitle must match the cover, so choose before the cover is made.

### E. Write `title-lab.md` and stop
Contents: Research Proof for the title tests; the anatomy table; all candidates with techniques; test results; scoring; recommendation; the exact title and subtitle strings (with character counts); open items (trademark search owner step, cover match). Reply in at most 6 lines and ask the owner to choose a title and subtitle (or ask for another round). Then run `/title-check` on the chosen string. After approval update `book.yaml` (title, subtitle), `brief.md`, `status.md` and tick the title gate; next step `/outline-book`.

## Rules
- Never recommend a title that imitates a famous book, brand or author.
- Never proceed on a HIGH-risk title unless the owner overrides in writing; record the override in `status.md`.
- If the title changes later, re-run this skill and the affected CMS checks.
