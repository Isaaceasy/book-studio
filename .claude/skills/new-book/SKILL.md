---
name: new-book
description: Stage 0 BRIEF + CONFIG. Starts a new book project. Creates the book folder from templates, chooses the profile (engineering, medical, general), interviews the owner to complete the brief and CONFIG (language, region, reader level, image budget, heading style, author), and records everything in brief.md, book.yaml and status.md. Use when the owner gives a book idea or says start a new book.
---

# /new-book — Stage 0: BRIEF AND CONFIG

## Purpose
Turn one raw idea into a complete, approved brief and a ready project folder. Everything later (market research, title check, architecture, writing, formatting, KDP files) depends on this, so be thorough and make no assumption on items that change the book materially. This is the entry point and a hard gate: no market research, front matter, chapter or manuscript file is written until the CONFIG is confirmed.

## Inputs
The owner's idea (a title, a topic, or a paragraph). Optional: a filled `templates/brief-template.md`.

## Step-by-step procedure

1. **Read context.** Read `CLAUDE.md` and list `books/` so you know which slugs exist. Read the three profile files in `profiles/` only as far as needed to ask the right questions.

2. **Choose the slug.** Lowercase hyphenated slug from the working title or topic (example: `structural-beam-mechanics`), max 40 characters, letters, numbers and hyphens only. If `books/<slug>/` already exists, STOP and ask whether to continue that book or create a differently named one.

3. **Create the folder structure** with the file tools:
   `books/<slug>/` with subfolders `front/`, `chapters/`, `back/`, `images/`, `audits/`, `compliance/`, `previews/`, `final/`.
   Copy `templates/book.yaml` to `books/<slug>/book.yaml`, `templates/brief-template.md` to `brief.md`, `templates/status-template.md` to `status.md` (fill slug, title, date). Create empty `verification-log.md`, `run-log.md` and `PROGRESS.md` with a heading line each.

4. **Detect the CONFIG from the idea** and state it for confirmation:
   - `profile`: engineering, medical or general (infer from the idea; ask if unclear).
   - `language` (en, fr, de, es): infer from the language of the title; if ambiguous ask. Never silently default.
   - `region`: target locale controlling number format, units, standards or guidelines and the Amazon marketplace. Defaults: French to France, German to Germany, Spanish to Spain, English to United States unless stated. Offer the main regional alternatives when relevant.
   - Subject area (engineering SUBFIELD or medical SCOPE_DOMAIN) and `reader level` (engineering: first-year undergraduate, upper-level undergraduate, practising engineer, mixed; medical: general public, health-science student, nursing/allied-health student, medical student, practising clinician, mixed; general: describe).
   - `STANDARDS`: unit system, design codes or classification systems (for example ICD edition), drug-naming convention, regional conventions appropriate to the language and region.
   - Chapter or Part count (12 to 18 for engineering and medical).
   - `publication_date`: date against which time-sensitive facts will be checked (default today).

5. **Interview the owner** with AskUserQuestion (multiple choice, at most 4 questions per round, at most 3 rounds), skipping anything already answered. Priority order:
   1. Profile and output (Word house style for engineering and medical; KDP PDF for general; or override).
   2. Reader level and the reader's core problem.
   3. Marketplace, language, region, spelling variant.
   4. Length: engineering and medical default to the fixed floor of 10,000 to 12,000 words per chapter or Part (excluding tables); general: words or pages.
   5. Heading style for Word books: show the menu if the owner has not chosen: 1 Black Banner, 2 Rule Line, 3 Numbered Block, 4 Centered Classic, 5 Shaded Bar, 6 Underline Accent, 7 Minimal Modern (a short description of each; offer the design sample in `/design-interior`).
   6. Image budget for Word books: 10, 20, 50 or custom total figures, and image mode: ask per chapter (YES / NO / EXTERNAL), YES to all, none, or supply myself.
   7. Author or pen name (never invent), voice, any real personal expertise or real examples that may be used.
   8. Non-negotiables: must include, must never include, required disclaimers; medical: whether dose figures are allowed (default no) and whether paediatric, pregnancy, geriatric or special-population content is in scope; out-of-scope topics.
   If the owner expressly declines to choose the language or heading style, English and Black Banner (style 1) may be used, but state the defaults openly first.

6. **Write the final brief** into `brief.md` in plain words with a 3-line "Brief summary" (reader, promise, format) at the top and a "Defaults I chose" section.

7. **Update `book.yaml`**: title (working), author, language, region, profile, output, heading_style, image_count, image_mode, chapter_word_floor (10000 for engineering and medical; the brief's target for general), publication_date. Keep numbers unquoted so the YAML parses.

8. **Estimate size.** Engineering/medical: chapters x floor gives the total words (about 300 to 350 words per page at 12 pt, 1.15 spacing, US Letter) and a page estimate; warn the owner when the estimate suggests a very large book and what the KDP print cost and page limit implications are (to be confirmed in market research with live KDP pages). General: from the word target.

9. **Check the toolchain once**: `python scripts/docxbuild.py check` for Word profiles, `python scripts/bookbuild.py check` for KDP PDF. If anything is MISSING tell the owner the exact install command from `README.md` and do not continue until it is fixed (previews depend on it).

10. **Update `status.md`** (stage = BRIEF awaiting approval; AI disclosure facts section left blank to fill as work proceeds).

## Approval gate
Reply with at most 6 lines: the folder, the CONFIG (profile, language, region, reader level, chapters, figures, heading style), the defaults chosen, and "Approve this brief, or tell me what to change." STOP. On approval tick "Brief + CONFIG approved", set stage to MARKET RESEARCH and name the next step: `/market-research`.

## Quality checks before replying
- `book.yaml` parses, profile is one of the three, language is one of en/fr/de/es.
- Nothing invented (author, publisher, ISBN, credentials).
- `status.md` reflects reality.
