---
name: title-check
description: Stage 2 TITLE GATE. Screens the title, subtitle and series name for trademark, brand, KDP-metadata and marketplace-collision risk, applies KDP title and subtitle rules for the marketplace, proposes seven natural-language subtitle options with an honest recommendation, and records the chosen title and subtitle. Use after market research is approved or whenever the title changes.
---

# /title-check — Stage 2: TITLE GATE (trademark + KDP rules + subtitle strategy)

## Purpose
Catch risky titles BEFORE chapters are written and choose a compliant, discoverable subtitle in the book's language and marketplace. A title problem discovered after production wastes the whole book. This is a risk screen, not legal advice; never promise a title is "cleared".

## Inputs
`brief.md`, `book.yaml`, `market-research.md` (verdict, price band, positioning, wording seen in the niche, keyword themes), working title and any subtitle or series name.

## Step-by-step procedure

### A. Screen what will be printed
List: main title, subtitle, series name, distinctive made-up words, any proper nouns or brand-like terms inside them. Screen each with WebSearch (mode "standard" first; "extended" only if results are thin):
1. **Registered trademark risk.** Search the term with "trademark" and open the official registries (USPTO trademark search for the US; UK IPO; EUIPO eSearch; WIPO Global Brand Database; the national register of the book's region). Note whether the term appears as a registered or pending mark in classes relevant to books, publications, education (International Classes 9, 16, 41) or the niche. If a registry cannot be searched, say so and mark the item UNVERIFIED with the exact registry link for the owner; do not mark LOW.
2. **Brand, franchise, character and person names.** None in the title, subtitle or series name, including parody-like variants.
3. **Marketplace collision.** Search Amazon and Google for the exact title: count same or near-same titles in the niche and whether one famous or high-selling book dominates it. Report facts.
4. **Franchise formats and series phrases.** Flag phrases that imitate well-known publishing formats.
5. **Metadata policy risk.** Title and subtitle in metadata must match the cover exactly, with no extra promotional words, pricing, ranking claims ("bestseller", "#1") or other brands or authors; read like real text in the book's language, not a keyword list; describe the actual content; not mislead (misleading metadata risks rejection or account action).

### B. KDP title and subtitle rules (open the live KDP metadata help page and record the date)
Baked-in principles to confirm live: title + subtitle together under the current character limit (the owner's frameworks assume under 200); no keyword stuffing; for nonfiction the subtitle carries ONE primary keyword theme and a clear outcome or benefit, researched in the book's language for the marketplace (amazon.fr / .de / .es / .com.mx for those languages; English keywords do not transfer); no trademarked terms, competitor or other authors' names, URLs or genre-descriptor stuffing; set the KDP language field to the book's language. For health books the subtitle must also avoid cure, treatment or diagnostic claims the content does not support and must not imply the book replaces professional care.

### C. Propose exactly SEVEN subtitles in the book's language
Each distinct, natural, KDP-compliant, within the character limit with the title, aimed at the inferred reader, varied in angle (audience-focused, outcome-focused, scope-focused, keyword-focused, etc.) and informed by the wording seen in `market-research.md` (without copying any competitor). Low-repeat preference: generally avoid reusing significant words already in the title (skip small function words of the language); the single primary keyword theme may repeat once if it reads naturally and strengthens discoverability; flag any deliberate repeat. Silently check each subtitle against the title before listing it.

### D. Recommend the strongest, honestly
Name the subtitle you predict is strongest for discoverability and buyer appeal in the marketplace, and explain why in terms of in-language keyword relevance, clarity of benefit, reader targeting, keyword coverage and compliance. State plainly that this is a reasoned prediction, not a guarantee of sales (performance depends on competition, reviews and testing) and recommend A/B testing the top two before committing.

### E. Risk level and alternatives
Assign the full title a risk level LOW, MEDIUM, HIGH or UNVERIFIED with one line of reasoning. If MEDIUM, HIGH or UNVERIFIED propose 5 safer alternative titles that keep the promise and audience, avoid flagged terms and have had a quick exact-match web check.

### F. Write `books/<slug>/title-check.md`
Title screened; date; searches and registries actually consulted (never claim one that was not); findings per term; KDP rules read (page, date); risk level; the seven subtitles, recommendation, A/B note; alternatives if any; the last line: "This is a good-faith screening, not legal advice or a guarantee of trademark clearance. For a title you will build a brand around, consult a trademark attorney or run a formal clearance search."

### G. Compliance
Run `/amazon-compliance` with scope `title` and fix any FIX before the gate.

## Approval gate
Reply with at most 5 lines: risk level, the biggest concern, the recommended subtitle. Ask the owner to choose title and subtitle (or an alternative). Then update `book.yaml` (title, subtitle), `brief.md`, `status.md`; tick "Title gate passed"; name the next step `/outline-book`.

## Rules
- Never claim certainty. Never invent registry results. Cite only what you opened.
- Never recommend titles that imitate a famous book, brand or author.
- Never proceed to the architecture stage on a HIGH-risk title unless the owner explicitly overrides in writing; record the override in `status.md`.
- If the title changes later, repeat this skill and re-run `/market-research` for the changed element.
