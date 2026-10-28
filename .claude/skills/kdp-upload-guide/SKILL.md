---
name: kdp-upload-guide
description: Stage 9 KDP GUIDE. Produces a step-by-step MANUAL guide for uploading the finished book to Amazon KDP, tailored to this book (files to upload, every setting, metadata from /kdp-metadata, AI-disclosure facts, pre-publish checklist). Claude never uploads, logs in or publishes. Use after /assemble-book and /kdp-metadata.
---

# /kdp-upload-guide — Stage 9: MANUAL KDP PUBLISHING GUIDE

## Purpose
Give the owner one clear, accurate checklist for the KDP dashboard so nothing is forgotten and every declaration is truthful. Claude does not sign in to Amazon, upload files, fill forms, set prices or press Publish; the owner does that.

## Inputs
`book.yaml`, `brief.md`, `status.md` (AI-disclosure facts), `title-check.md`, `market-research.md` (price band, category evidence), `final/` files, the output of `/kdp-metadata` (description, seven keywords), `compliance/` reviews, the Clearance Pack status for medical and engineering books.

## Procedure

1. **Open the live KDP help pages** (WebSearch / WebFetch, record the date): paperback and ebook setup, content guidelines, metadata guidelines, AI-generated content disclosure, manuscript and cover formatting, pricing and royalty, categories, ISBN. Use the current wording and numbers. If a page cannot be opened, mark the dependent step "verify on KDP".

2. **Pre-publish gate.** List and tick, with evidence from the project: fact-check ledger has no open NEEDS-HUMAN; compliance verdict PASS on the manuscript; clinical/technical clearance obtained (state who and when, or "NOT DONE — do not publish as authoritative"); metadata passes; copyright and trademark screen done; no placeholders. If any item is not satisfied, the guide opens with a red warning section and the exact actions required.

3. **Write `final/KDP-UPLOAD-GUIDE.md`** (and a Word copy for printing if the owner wants) with these sections:
   - **Files to upload:** the exact manuscript file (Word profiles: the DOCX; general: the interior PDF), and what the owner still has to supply (cover file; the cover is NOT produced in this studio). Trim, paper and ink settings and why.
   - **Step 1 Book details:** language, title, subtitle, series (if any), edition, author (must equal the cover and title page), contributors, description (final text from `/kdp-metadata`), publishing rights (own the copyright), seven keywords from `/kdp-metadata` (one per box), categories (two or three, chosen from the research evidence, with the exact browse path), age/reading range if relevant, "adult content" answer.
   - **Step 2 Content:** ISBN choice, print options, manuscript upload, cover upload, AI-generated content declaration with the facts from `status.md` (what was AI-generated: text, images, translations) in plain words so the owner answers accurately; previewer check list (what to look at in the online previewer: table edges, figures, equations, page numbers, contents, drop caps).
   - **Step 3 Pricing:** marketplaces, price band from `market-research.md`, royalty plan, print cost estimate (to be read from the live KDP calculator), KDP Select decision (ebook only) with the trade-offs stated neutrally.
   - **Order a proof copy** recommendation before publishing; what to check on it.
   - **Pre-publish checklist** (tick boxes) and **after publishing**: page appears in a day or two, check the live listing against the metadata, do not edit the title or author after publishing without consequences, how to update the manuscript.
   - **Policy reminders from the live pages:** content guidelines, no misleading metadata, no review manipulation, no keyword stuffing, no trademark use, quality expectations (the quality-complaint risk).

4. **Honesty block** at the end: what Claude verified (list), what it could not verify and the owner must check on KDP, and "This guide is based on KDP pages read on <date>; KDP changes its rules, so confirm in the dashboard."

5. **Update `status.md`**: stage = READY FOR OWNER TO PUBLISH.

## Rules
- Never claim a KDP rule or number without having opened the page (or mark it "verify on KDP").
- Never advise evading a KDP check or rule.
- Never invent ISBNs, prices, royalty numbers or category paths; take them from the evidence and the live pages.
- Medical and engineering books: never state they are cleared unless the Clearance Pack records a real reviewer.
