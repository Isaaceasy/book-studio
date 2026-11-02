---
name: interior-library
description: Reads the owner's uploaded book interiors (PDF pages, mockup images, DOCX) from interiors/_inbox, analyses each one into a structured style card (layout, palette, typography, hierarchy, callouts, tables, figures, density, trim, book type, strengths, and what to avoid copying), files it in the interior library, and updates the index. Used by /design-interior to build beautiful color interiors that match a niche's conventions but are uniquely designed. Run whenever the owner uploads new interiors.
---

# /interior-library: THE INTERIOR REFERENCE BANK

## Purpose
The owner uploads finished or sample book interiors for many kinds of books. This skill turns each upload into a **style card** the framework can read later, so every new book gets a beautiful, colored, category-appropriate interior that is clearly unique, never a copy. This is the "current interior reference bank" feature of the owner's GENIE product guide.

## Where things live (`interiors/`)
- `_inbox/`: the owner drops new files here (PDF, PNG, JPG, WEBP, DOCX, mockup photos, links in a text file).
- `library/<id>/style-card.md`: the analysis (committed to git).
- `library/<id>/reference/`: the original images or PDF (kept on the owner's computer; NOT committed, because they are third-party designs; see `interiors/README.md`).
- `INDEX.md`: one table of all cards (id, book type, niche, trim, palette family, density, color, tags, best use).
- `STYLE-CARD-TEMPLATE.md`: the card layout.

## Procedure

### Step 1. Intake
List `interiors/_inbox/`. For each new item: assign an id (`<booktype>-<NN>-<shortname>`, for example `medical-03-crimson-charcoal`); create `library/<id>/reference/` and move the file there (never delete originals); note the source and what the owner said it is, if anything.

### Step 2. Look at it for real
Render and view the pages. For PDFs, extract the page images (pypdf `page.images`) or render pages with the installed PDF tools, and look at at least: a chapter opener, a typical text page, a table page, a figure page, a callout or box page, the contents page and a back-matter page. For mockup photos, note that perspective hides exact margins; estimate carefully and mark estimates ESTIMATED. Never claim to have seen a page you did not open.

### Step 3. Write the style card (`STYLE-CARD-TEMPLATE.md`)
Record, in plain words and measurable terms where possible:
- Identity: id, source, book type and niche it suits, reader level, trim and page size (measured or ESTIMATED), color or black and white, density (words per page estimate, airy / balanced / dense).
- Palette: primary, secondary, accent and tint colors as hex values (sample from the image where possible), where each is used, contrast notes, greyscale behaviour.
- Typography: serif or sans, weight and style of body, headings (levels 1 to 3), labels, captions, numerals; body size and leading estimate; identify the closest open-licence fonts (the framework uses fonts in `fonts/` or Google/open fonts; never assume a commercial font is available).
- Page furniture: running header and footer, page-number treatment, margins (inside, outside, top, bottom), edge tabs, chapter-opener design, rule lines, ornaments.
- Hierarchy and components: chapter opener, section heads, run-in labels, numbered lists, callout boxes (types, icons, colors, border style), tables (header style, zebra, borders), figures and captions, pull quotes, case or example boxes, summary and review-question blocks.
- Strengths (what makes it work for readers) and weaknesses (what to improve).
- **Do not copy list**: distinctive elements that belong to that designer or publisher (logos, signature ornaments, exact layouts, brand colors) and must not be reproduced.
- **Adaptation notes**: how to carry the idea to other trim sizes (for example two columns on 8.5 x 11 become one column on 5 x 8), to black and white, to ebook reflow.
- Suggested CSS tokens: a short block of variables (colors, font stacks, sizes) usable in `book.css`.
- Tags (for search): niche, mood, palette family, density, features (tabs, icons, sidebars, tables).

### Step 4. Update `interiors/INDEX.md`
Add the row; keep the table sorted by book type. Add a short "good for / not good for" line.

### Step 5. Report
At most 5 lines: how many interiors were added, ids, the three most useful tags, and any file that could not be read (say which and why). Do not move anything outside `interiors/`.

## Using the library (called by `/design-interior`)
1. From the CMS research (`cms-research.md` interior conventions and sampled interiors) and the book profile, shortlist 2 or 3 library cards that match the niche, trim and density.
2. Propose a **unique design** that borrows the niche-appropriate conventions of the shortlisted cards but changes palette, typography pairing, header and tab system, callout icon set and chapter-opener composition enough that the interior is clearly its own. Show a "distance check": a table naming each element and how it differs from every shortlisted card and from the competitor interiors in `competitors.csv`.
3. All interiors are COLORED (owner rule) unless the owner chooses black and white for a given edition; every colored element still keeps a printed label or pattern so a greyscale edition remains readable.
4. Record which cards were used in `status.md` and `book.yaml` (`interior_refs`).

## Rules
- Originals are never committed to git by default (rights). Style cards describe, they do not reproduce.
- If a card's palette or layout is too close to what is proposed (a recognizable copy), change the proposal.
- Credit: store the designer or source name in the card for internal reference only; never print it in a book.
- If the owner uploads a stylesheet or template they own, record it as `source: owner-owned` and it may be reused directly.
