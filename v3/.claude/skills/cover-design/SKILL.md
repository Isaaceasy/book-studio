---
name: cover-design
description: Stage 8 COVERS. Creates the ebook cover and the full paperback wrap (front, spine, back, bleed, barcode area) for any book, from the CMS cover conventions, the approved title and the final page count. Art is generated with HiggsField, all text and measurements are set by script so they are exact, and every file is preflighted against KDP's live cover specifications. Produces upload-ready files plus a cover brief and an AI-disclosure record. Never uploads.
---

# /cover-design: Stage 8, EBOOK COVER AND PAPERBACK WRAP

## Purpose
Produce covers that can be uploaded to Amazon KDP without rework: a **Kindle ebook cover** (front only) and a **paperback wrap** (back + spine + front in one print-ready PDF), for any book type, designed to look professional in the niche, clearly different from every competitor, and legible as a thumbnail. Based on the owner's Non-Fiction Book Design Prompt System (front cover, back cover, wrap, A+ images), upgraded with CMS evidence, exact measurements and automated checks.

## Inputs
`title-lab.md` (final title and subtitle strings), `cms-research.md` (cover conventions and the "must not resemble" list), `competitors.csv` (cover style notes), `book.yaml` (trim, ink, paper, page count after assembly), `final/KDP-metadata.md` (description for the back cover), `brief.md` (audience, mood), `book-bible.md` (author name; never invent a bio or photo), `docs/kdp-specs.md`, `docs/reference-materials/Non-Fiction-Book-Design-Prompt-System.docx`.

## Golden rules (from the owner's guide, kept)
1. The owner decides; propose, do not impose. One step at a time. Never invent reviews, awards, statistics, endorsements or bestseller claims on a cover.
2. **Use AI for artwork, not for print specifications or small text.** Image tools garble lettering and miss exact sizes. Generate art WITHOUT text and set every word of text by script (HTML/CSS rendered to PDF or PNG). If a generated image shows any lettering, treat it as decoration and regenerate or crop.
3. Thumbnail test: shrink the front cover to about 150 px wide; the title must still read. Increase size or contrast if not.
4. No barcode, ISBN, QR code, publisher logo, social handles or photos you do not have rights to. Leave a clean barcode zone on the back cover; KDP adds the barcode.
5. AI-generated cover art must be disclosed to KDP; record the tool, model, prompt and date for every generated image in the Cover Log (`covers/cover-log.md`). Confirm the image tool's commercial-use terms (read the live terms; HiggsField terms were read on 2026-10-29: outputs may be used commercially; re-check at each use).
6. Distance rule: the cover must not copy any competitor's artwork, trade dress, layout or distinctive color-and-type combination. Match category conventions (palette family, imagery type, type weight), not a specific book.
7. Fiction and children's covers follow genre conventions (see profile notes), not the nonfiction concepts below.

## Procedure

### Step 1. Cover brief (`covers/cover-brief.yaml`, from `templates/cover-brief.yaml`)
Collect or infer: exact title and subtitle (character for character as in KDP metadata), author name exactly as on the title page, category, audience, mood words, trim size, interior ink and paper (white or cream), final page count (from `final/` build report), ebook only or ebook plus paperback, hardcover or large-print edition if planned, text allowed on the front cover (title, subtitle, author only, unless the owner approves a short tagline that is true), back-cover copy (from the approved description: a headline and two short paragraphs, factual), whether an author photo or bio is wanted (owner supplies; never invented), and the cover conventions from `cms-research.md`.
Lesson learned: the page count must be the FINAL count from the assembled interior, because the spine width depends on it; any page change later means recalculating the wrap.

### Step 2. Verify the live specifications (record the date)
Open the live KDP pages and record: paperback cover requirements (bleed, spine formulas, barcode area, minimum page count for spine text, file type and resolution), ebook cover requirements (ideal 2,560 x 1,600 px height by width, ratio 1.6:1, minimum 1,000 x 625, maximum 10,000 px per side, JPEG or TIFF, RGB, under 50 MB), and hardcover specifications if applicable. Defaults and dates are in `docs/kdp-specs.md`; if a live page differs, the live page wins and you update `docs/kdp-specs.md`. For the exact paperback template, KDP's own cover template or calculator for this trim, paper and ink is authoritative; the owner's `KDP_Print_File_Setup_Calculator` workbook may also be used to cross-check.

### Step 3. Calculate the wrap
Run `python scripts/cover_calc.py --trim 5x8 --pages 160 --paper white --ink color` (add `--hardcover` when relevant). It prints: spine width, full wrap width and height in inches and pixels at 300 dpi, bleed, safe margins, the back, spine and front panel rectangles, and the barcode zone. Cross-check against KDP's template. Spine text is allowed only above KDP's minimum page count (about 79 to 80 pages at last check; verify live); below it leave the spine blank.

### Step 4. Concepts (nonfiction): five genuinely different, then one chosen
Using the CMS cover conventions, write five concepts, each with: color scheme (2 or 3 colors, solid, gradient or texture), image (what it shows and where it sits), typography direction (font style for title, subtitle, author), layout (text position, white space), mood, and a complete HiggsField image prompt (no text, no icons or borders unless the concept needs them). At least one concept must be a deliberate departure from the niche convention that still reads as the right category. Present the five in a table with a one-line distance check against the closest competitor cover. Ask the owner to choose one (or ask for another round). For fiction use genre-specific concepts (imagery, lettering style, series consistency).

### Step 5. Generate the art
Use HiggsField (generate_image) for the cover image(s): portrait front art at the trim proportion plus bleed, and a matching back-cover background (calm, low contrast, a clean text area, a clean barcode zone). Generate 2 or 3 variants, record every prompt, model, job id and date in `covers/cover-log.md`, choose the best, and reject any with lettering, distorted hands or faces, watermarks, logos, or look-alike artwork. Upscale if needed so the final front image is at least 300 dpi at its printed size (use the upscaling tool or regenerate larger; check pixel dimensions with the calc output). Never enlarge a low-resolution image to hide a defect.

### Step 6. Compose with exact text (script)
Run `python scripts/cover_compose.py covers/cover-brief.yaml` (HTML/CSS template to PDF and PNG via Chromium). It places: front (title, subtitle, author), spine (title and author rotated, only if allowed), back (headline, two paragraphs, barcode zone kept clear), all inside the safe margins, at the exact wrap size, with bleed, fonts from `fonts/` or the font named in the brief. Output files:
- `covers/paperback-wrap.pdf` (print-ready, flattened text, RGB or as KDP requires; embed fonts)
- `covers/ebook-cover.jpg` (2,560 x 1,600 px preferred, RGB)
- `covers/front-cover.png` (high resolution, for A+ content and listings)
- `covers/thumbnail-test.png` (the 150 px test)
- `covers/cover-brief.yaml`, `covers/cover-log.md`
For a hardcover edition produce the case-wrap per KDP's hardcover template (separate calc flag) and a dust-jacket note if the owner wants one.

### Step 7. Preflight (`python scripts/preflight_cover.py covers/`)
Checks: wrap size equals the calculation within tolerance; spine text within its panel with margins; no text outside safe margins; ebook ratio, pixel dimensions, file type and size within limits; front image resolution (dpi at printed size); barcode zone clear; fonts embedded in the PDF; no transparency problems; title strings equal the metadata strings exactly (reads `book.yaml`). Inspect the PNG and PDF visually page by page (render to images and look at them). Fix every failure.

### Step 8. Compliance review
Run `/amazon-compliance` with scope `cover`: no misleading claims, no ranking or award words, no competitor or brand names, no prices, title and subtitle matching metadata, cover not resembling a protected design, AI disclosure recorded. Fix every FIX.

### Step 9. Deliver and stop
Reply with at most 5 lines: where the files are, the wrap size and spine width, the checks passed, the AI-disclosure facts, and what approval is needed. Remind the owner to view the cover in KDP's cover previewer and to order a proof copy; the owner uploads. Update `status.md`.

## Rules
- Never upload or sign in. Never invent an author bio, photo, quote, award or review.
- Spine width and wrap size always come from `cover_calc.py` with the final page count and are cross-checked with KDP's template.
- If the interior page count changes after the cover is made, recompute and rebuild before upload.
- Covers for ebooks and paperbacks must show the same title and subtitle as the metadata.
- Keep the Cover Log; it supports the AI-content disclosure.

## OWNER KIT (from `AI-PROMPT-2` and the Non-Fiction Book Design Prompt System): modes and prompts
**No-reference template (use when the owner has no reference cover):** the intake block is: kind of book, title, what it is about (1 to 2 sentences), genre or category, audience, where it will be sold, trim size. Then Step 2: do the research (CMS cover conventions), give different concepts (color combos of 2 or 3 colors, solid, gradient or texture; image position central or sideways; typography; design concept; mood) with a complete image prompt each; generate from each prompt; if not satisfied ask for 5 new variations from different concepts, "creative and unique, no lines, no icons"; the owner may speak or type exactly what to change; or start again; or download the sample and edit. "You are the sailor of this ship": the owner decides, read every reply.

**Back-cover prompt (universal premium, for professional non-fiction):** match the front in color, mood and type; one background image related to the subject (blend naturally, secondary to text, dark or light overlay for legibility; no collages, floating objects, icons, lines, blueprints, abstract tech patterns, glows); reserve about two thirds as a clean reading area with generous margins; text never touches trim, bleed or safe margins; one bold headline; no more than two short benefit-driven paragraphs (fully justified in the kit; V3 uses left-aligned to avoid rivers on narrow panels unless the owner prefers justified); modern editorial typography with a clear hierarchy; a clean blank white area for the barcode; no barcode, QR code, ISBN, publisher logo, social media, author biography or author photograph; minimal, elegant, professional, premium.

**Paperback wrap prompt (assembly mode):** use the supplied front cover, back cover and the KDP template; DO NOT redesign the supplied artwork; match the template dimensions exactly (bleed, trim, safe margins, 300 dpi); left panel = supplied back cover unchanged (typography, spacing, margins, colors, image placement, empty barcode area); center spine = exact spine width, PLAIN or WITH TITLE; if plain, the background continues seamlessly across the spine with no title, author, logo, icon, border or line; right panel = supplied front cover unchanged; extend the background naturally across back, spine and front; keep important content inside safe areas; add no ISBN, barcode, QR code, logo, website, social media, borders, frames, extra illustrations, shadows or watermarks; output one flattened print-ready wrap.
V3 implements this as `mode: assemble` in `cover-brief.yaml`: `python scripts/cover_compose.py covers/cover-brief.yaml` places the supplied `art.front` and `art.back` images unchanged and adds no text; spine plain by default. Use `spine_style: plain` (without assemble mode) for composed covers with a plain spine, and `spine_text: true` for a title spine. Universal variables: template (KDP), trim, overall wrap size and spine width (from `cover_calc.py`, cross-checked with KDP's template), resolution 300 dpi, spine style plain or with title.

**Image-tool honesty:** the kit assumes ChatGPT or Gemini; V3 uses HiggsField for art. Image tools garble small text and miss exact sizes: art without text, text and sizes by script (kit Part 3 tip). Disclose AI-generated images and confirm the tool's commercial-use terms.
