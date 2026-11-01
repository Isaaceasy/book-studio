---
name: aplus-content
description: Creates the Amazon A+ Content package for a finished book: a coordinated set of storefront graphics (promise, benefits, audience, inside look, trust-safe facts, author) plus the module copy and alt text, sized to Amazon's live A+ module specifications, using the approved cover, interior samples and HiggsField art, with text set by script. Never invents reviews, awards or claims. Use after /cover-design and /kdp-metadata.
---

# /aplus-content: A+ CONTENT GRAPHICS AND COPY

## Purpose
GENIE Pro "A+ content graphics": a coordinated storefront visual set that explains the book's promise, benefits, audience and interior experience. Extends the owner's Non-Fiction Book Design Prompt System (Part 4: eight A+ images).

## Inputs
`covers/` (front cover PNG), `final/KDP-metadata.md` (description, benefits), interior sample pages (render 4 to 6 representative pages from `final/` PDF), `book-bible.md` (reader profile), `cms-research.md` (what competitors' A+ pages emphasize, if visible), `docs/kdp-specs.md`.

## Procedure
1. **Verify live specs.** Open Amazon's current A+ Content guidelines and KDP's A+ help page (the KDP "A+ Content" area for books). Record the date, module types available to the owner, image dimensions and file limits, text limits, and prohibited content. The live pages win over any number in this skill.
2. **Plan the set (8 modules by default).** (1) Promise banner: the book's central benefit in one line. (2) Who it is for: the reader groups. (3) What you will learn: 4 to 6 benefits taken from the manuscript. (4) Inside the book: real interior pages (cropped renders of the actual interior). (5) Format and quality facts: trim, page count, color, figure count (only true facts). (6) How the chapters work: the learning structure. (7) Safety, scope or honesty note when relevant (educational use, not a substitute for professional care; US scope; what is NOT covered). (8) Author or series module (only facts the owner supplies; no invented bio).
3. **Copy.** Short, factual, reader-centred, no guarantees, no prices, no ranking or award claims, no reviews or testimonials, no competitor names, no URLs, no "limited time" language; each benefit must exist in the manuscript. Write alt text for every image.
4. **Art.** Use HiggsField only for backgrounds or scene art (no text, no logos, no real people); use real renders of the cover and interior for modules that show the book. Set ALL text by script over the art (HTML/CSS rendered to PNG at the exact module size) so lettering is never garbled. Keep the same palette and type as the cover and interior so the page looks like one brand.
5. **Compose and preflight.** Render each module to `release/aplus/NN-name.png` at the live-spec size; check text legibility at the size Amazon displays, safe margins, file size, no stretched images, and that every claim matches the manuscript.
6. **Compliance.** `/amazon-compliance` scope `aplus`. Record AI-generated art in the Cover/Image Log and in `status.md` AI-disclosure facts.
7. **Deliver** `release/aplus/` (images, `aplus-copy.md` with module text and alt text, `README.md` with upload instructions: the owner uploads in their own account). Reply in at most 5 lines.

## Rules
- Never upload or sign in. Never invent facts, reviews, awards or endorsements.
- If a module type or size is unavailable to the owner's account, adapt the set and say so.
