---
name: outline-book
description: Stage 3 ARCHITECTURE LOCK. Builds the chapter or Part architecture (objectives, entries, figure allocation, terminology and notation table, standards, verification targets, chapter-boundary and non-repetition map), the style guide and the book bible, addresses the gaps found in market research, then asks the run-mode question (STANDARD or AUTONOMOUS). Use after the title gate passes and before any chapter is written.
---

# /outline-book — Stage 3: ARCHITECTURE, ALLOCATION AND TOC LOCK

## Purpose
Create the structure every chapter will obey. After the owner approves it, nothing is silently renamed, merged, split, reordered, added or removed, and figure allocations never change without approval. This stage produces an outline only, no chapter prose (apart from two short style samples).

## Inputs
`brief.md`, `book.yaml`, `market-research.md` ("must address" and "must avoid" lists, positioning, gaps), `title-check.md`, `CLAUDE.md`, the profile file (`profiles/<profile>.md`), and `profiles/docx-house-style.md` for Word books.

## Step-by-step procedure

1. **Read** the profile file completely and the market-research requirements. Note which confirmed gaps the book must address; every confirmed gap must appear somewhere in the architecture or be explicitly declined with a reason.

2. **Research the subject lightly but for real** (WebSearch / WebFetch): key concepts, standard terminology, current standards or guidelines, common beginner questions and mistakes, what authoritative sources treat as the core topics. Open the pages you rely on. Record sources in `verification-log.md` (internal). Do not copy wording.

3. **Choose the structure framework** that fits the profile and book type and say why:
   - Engineering: chapters with the mandatory template (learning objectives, theory and derivation from fundamentals, 2 to 3 or more worked examples, 5 to 10 practice problems with verified answers, summary of key equations and takeaways).
   - Medical: Parts organised by body system or domain; entries by type and tier (Major, Standard, Brief); Part structure per `profiles/medical.md`.
   - General: how-to, workbook, narrative, children's, activity, as appropriate.

4. **Write `outline.md`.** Contents:
   - Working title, subtitle, one-sentence promise, framework chosen, total target words and page estimate.
   - Ordered chapter (or Part) list, normally 12 to 18 for engineering and medical, with for EVERY chapter or Part: exact title, 3 to 5 learning objectives, key concepts (for medical: the entry list with each entry's type and tier), equations or clinical formulas, prerequisites, key points or beats, one example or exercise idea, word target (engineering and medical: the fixed floor of 10,000 to 12,000 words excluding tables, unless the Scope Lock sets another), and exact figure allocation.
   - Figure allocation table whose totals equal `image_count` (engineering and medical); where a figure is planned give subject, what it must show and why.
   - Front matter plan and back matter plan (glossary, symbol or abbreviation list, appendices, index for medical; never a bibliography or reference list).
   - Explicit out-of-scope topics.
   - "Market gaps addressed" table: each confirmed gap from `market-research.md` and where the outline answers it.
   - Verification targets: every external standard, constant, material property, data table, classification system, reference range, guideline convention, drug fact and statistic the book will rely on (these become the fact-check ledger).
   - Chapter-boundary and non-repetition map: for each major concept its single home chapter or entry; for each concept revisited later, the specific new angle (application, comparison, implication, edge case, advanced treatment) that prevents duplication.
   - The no-citation and no-bibliography rule stated explicitly.

5. **Write the master terminology, notation and unit table** in the book's language (symbols, definitions, units, established native terms, accepted synonyms, abbreviations, classification codes for medical) into `book-bible.md`. For fr/de/es use the real native terms (never calques) and record the number-format convention for the region. This table is locked like notation: new terms are added formally before use.

6. **Write `style-guide.md`** for THIS book: narrator and point of view, tense, 3 to 5 tone words, vocabulary and reading level, sentence-length guidance, humour level, spelling variant, how callouts, takeaways, exercises, vignettes and quotes look, extra words and phrases to avoid on top of CLAUDE.md section 6, and 2 short sample paragraphs written fresh to show the voice.

7. **Write `book-bible.md`** sections: reader profile; terminology and notation table; people, characters, places (fiction); facts register (each fact with its verification-log ID); running examples and recurring metaphors; cross-reference list; required disclaimers; image style (filled during writing); sources are in the verification log, not here.

8. **Run `/amazon-compliance`** with scope `outline` (promise versus planned content, claims, disclaimers, sensitive topics, whether the book will give the reader what the title and gap analysis promise). Fix every FIX.

9. **Update `status.md`**: stage = ARCHITECTURE awaiting approval; add chapter rows (number and title); record the figure allocation.

## Approval gate (interactive, always)
Reply with at most 6 lines: the chapter or Part list (titles only, comma-separated), total length, figure total, framework. Ask the owner to approve or adjust. Apply every change to `outline.md`, show only what changed, repeat until approved. Then tick "Architecture lock approved".

## Run-mode question (ask once, after the lock is approved, before any writing)
Ask with AskUserQuestion exactly this choice:
"Would you like to run this book in AUTONOMOUS mode? YES: I will write the front matter, every chapter, the back matter and the final build without asking anything further (I will first collect any missing settings in a single message). NO: I will work in STANDARD mode, stopping for your approval after every chapter (and asking the image question YES / NO / EXTERNAL where it applies)."
Record `run_mode` in `book.yaml`. Never start AUTONOMOUS on your own and never assume a YES. A NO does not close the door: the owner can type AUTONOMOUS later and the run switches from the next chapter onward.
If AUTONOMOUS: collect in ONE message anything still missing (image mode, dosing scope for medical, author name and dedication/acknowledgements or the decision to omit them, delivery format: master DOCX only or per-chapter DOCX plus master) and apply the autonomous defaults in CLAUDE.md section 9 if the owner replies DEFAULTS. Remind the owner that autonomous mode never replaces fact-checking, Amazon compliance review or the human clearance gate.

Name the next step: `/design-interior`.

## Rules
- Never write chapter prose here. No filler chapters or entries. Every chapter earns its place by the reader's promise and the market gaps.
- No unverified claims or invented statistics in the outline.
- Plain-text cross-references only; no hyperlinks.
