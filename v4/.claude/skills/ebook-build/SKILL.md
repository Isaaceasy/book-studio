---
name: ebook-build
description: Stage 6b EBOOK. Builds the reflowable Kindle-ready EPUB 3 from the book's Markdown sources with scripts/ebook_build.py (cover, navigation menu, styling from the book's accent color, alt text), checks it mechanically, and lists the ebook-specific compliance and quality points (no print page numbers, no fixed layouts, tables and figures that reflow, accessibility, file size, delivery fee). Use after /assemble-book whenever the ebook is a wanted format, and again whenever the text changes.
---

# /ebook-build: THE KINDLE EDITION

## Purpose
V3 produced an ebook cover but no ebook manuscript. The paperback interior is a print-exact PDF; a Kindle ebook is a different product: reflowable text that adapts to the reader's device. This stage makes it from the same verified Markdown, so the ebook and the paperback never say different things.

## Inputs
`book.yaml`, `front/`, `chapters/`, `back/`, `images/`, `covers/ebook-cover.jpg`, `docs/kdp-specs.md`, `profiles/<profile>.md`, the live KDP help pages for ebook content (open them; record the date).

## Procedure
1. **Open the live KDP ebook rules** (file formats accepted, EPUB guidance, image size and resolution, table of contents, cover rules, 650 MB limit, delivery fee for large files, accessibility and metadata guidance). Update `docs/kdp-specs.md` if anything changed.
2. **Prepare the source for reflow** (edit the Markdown copy only if needed, never the verified text):
   - Contents: the ebook gets a real navigation menu from the headings. Remove the static print contents page and print-only instructions ("turn to page 40"); replace page references with section names (the print edition keeps its own).
   - Tables: keep only tables that stay legible on a phone (three or four short columns). Wide tables become a list of short labelled paragraphs, or an image with a caption and a text description.
   - Figures: every image needs alt text and a caption. Informational figures need a text description in the alt text. Text inside images must also exist as real text nearby.
   - Colour-coded information must also carry a text label (the greyscale rule applies to e-ink Kindles).
   - Remove page breaks, running heads, drop caps and other print layout; the callouts become simple bordered paragraphs (the build CSS handles this).
   - No hyperlinks except what KDP's own rules require; the policy of the book (rule 3) still applies.
3. **Build:** `python scripts/ebook_build.py books/<slug>` (output `final/<title>-ebook.epub`). Read its RESULT line and every PROBLEM.
4. **Validate beyond the script:** the script checks structure, links and alt text. Also (a) run EPUBCheck if available (`java -jar epubcheck.jar file.epub`; free tool) and record the result or "NOT RUN"; (b) open the EPUB's text with `pandoc -t plain` and read the first and last pages and one chapter in the middle for broken characters; (c) render two chapters to images if a viewer is available and look at them. Record exactly what was and was not done.
5. **Ebook compliance review:** `/amazon-compliance` on the ebook file and its metadata: title and author equal the cover and the paperback, no "also available as" promotional text inside the book unless allowed by the live rules, AI-disclosure facts identical to the paperback, price/royalty plan consistent (the 70% royalty option has a price range and delivery fee; read it live).
6. **Output:** `final/<title>-ebook.epub`, `final/ebook-build-report.md` (what was changed for reflow, check results, what was NOT checked). Update `status.md`.
7. **Report** in at most 4 lines.

## Rules
- Never change a fact for the ebook. If a sentence must change for reflow, change it in both editions or log the difference.
- The owner views the EPUB in KDP's online previewer or the Kindle previewer before publishing (owner action; listed in the owner checklist).
