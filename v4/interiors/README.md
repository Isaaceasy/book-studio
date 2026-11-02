# THE INTERIOR LIBRARY

A dedicated folder of book interiors the framework can read to design beautiful, COLORED, category-appropriate interiors that are clearly unique. You upload; Claude analyses; every new book draws on it.

## How to add interiors
1. Drop files into `_inbox/` (PDF pages, mockup photos PNG/JPG/WEBP, DOCX, or a text file of links). Group by book type if you like (a sub-folder per source is fine, like `_inbox/pinterest-design-layout/`).
2. Tell Claude: `/interior-library`. It looks at every page, writes a style card for each, files the card and the original in `library/<id>/`, and updates `INDEX.md`.
3. When you start a book, `/design-interior` shortlists 2 or 3 cards that match the niche (from the CMS research), then designs a unique interior that borrows the conventions, not the layout.

## What is in each place
- `INDEX.md`: one table of all cards (book type, niche, trim, palette, density, tags).
- `STYLE-CARD-TEMPLATE.md`: the layout of a card.
- `library/<id>/style-card.md`: the analysis (kept in git).
- `library/<id>/reference/`: the original files (kept on your computer, NOT in git).
- `_inbox/`: new uploads waiting for analysis (not in git).

## Rules
- All interiors in this framework are COLORED, with printed labels and patterns so a black-and-white edition still reads.
- The references are other people's designs. They teach conventions (density, hierarchy, palette families, callout types); they are never copied. Every card has a "do not copy" list and each new design gets a distance check against the cards it used.
- Originals are not committed to git by default, because of rights. If you own a reference (your own template), mark it `source: owner-owned` in its card and it may be reused directly and committed.
- Cloud sessions only see what is pushed, so the style cards (descriptions and design tokens) carry the knowledge; the images stay local. If a cloud run needs to look at an image, copy it into the book's `design-references/` folder deliberately.
- Add many kinds: medical, engineering, business, self-help, cookbook, travel, children's, puzzle, coloring, fiction, workbook, large print, hardcover. More variety makes better matches.

## First contents (2026-11-02)
- 5 interior references from the owner's `Downloads\medicine book interior` and pocket-neurology photo, plus a children's picture book PDF: analysed into 5 cards.
- 24 pins saved from the owner's Pinterest board "design layout" (only the pins visible without signing in; the board has 140): 14 book-interior images, 1 cover wrap, 1 coloring reference, 8 not book designs. Raw files are in `_inbox/pinterest-design-layout/`; run `/interior-library` to analyse them.
