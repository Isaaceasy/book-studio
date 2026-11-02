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

## OWNER KIT (from `AI-PROMPT-2`, the A+ "Step-by-Step Amazon Marketing Design System"): how it is implemented here
The owner's kit has 8 images and a 14-layout menu. Keep its structure; replace its weak points with checks and scripts.

**The 8 images (sizes from the kit; VERIFY against Amazon's live A+ page before building, the live page wins):**
1. Hero banner with the book cover mockup, 970 x 600 px.
2. Open book showing interior pages, 970 x 600 px.
3. Benefit banner, 970 x 300 px.
4. Call-to-action banner with a small cover mockup, 970 x 300 px.
5 to 8. Four square outcome tiles, 300 x 300 px each, one per top reader outcome.

**Step 1 analysis first** (no design yet): genre, ideal buyer, top 4 things a reader will achieve (these become the 4 tiles), main cover colors with hex codes, emotional tone. Ask the owner to confirm before designing.

**Layout menu (pick a DIFFERENT letter for images 1 to 4; vary the four tiles):** A split panel (color half and photo half); B curved white cutout over a full photo; C diagonal color slash across a photo; D circular spotlight with text wrapping; E torn paper reveal; F full-bleed photo with one floating text card; G grid or magazine block panels; H bold ribbon banner with whitespace; I framed border composition; J book as centerpiece with radial callouts; K before and after two-panel story; L vertical color stripe holding the headline; M angled overlapping parallelograms; N circular badge cluster with the book in the center. Tell the owner which layout each image uses and why; wait for "next".

**Rules kept from the kit:** headline states what the reader will ACHIEVE, not what the book contains; a small eyebrow tag above the headline; one short supporting sentence; palette from the cover; no invented statistics, review counts, bestseller claims or trust badges, only true provable claims; word limits (image 1: 20 words of body copy; image 2: headline plus 3 short outcome callouts, 20 words; images 3 and 4: 15 words; tiles: 10 words each); "stop anywhere": after step 3 a usable A+ page exists.

**Where V3 differs from the kit (on purpose):**
- The kit asks an image tool to draw the cover mockup "exactly as provided". Image generators redraw covers and garble text. V3 composites the REAL cover pixels with `python scripts/mockup_cover.py covers/front-cover.png out.png --size 970x600 --bg "#hex" --side left` (stylized mockup with spine strip, perspective and shadow). For richer scenes generate a scene WITHOUT any book (HiggsField) and pass it as `--bg-image`.
- Interior page images for image 2 come from real renders of the final PDF pages; composite them onto an open-book scene by script, never redrawn.
- All headline and callout text is set by script (HTML to PNG) over the art, never generated inside the image. If any generated image shows lettering, treat it as decoration or regenerate without text and add clean text (the kit's own "Canva" tip, automated).
- Photorealism is only claimed for real renders; label stylized mockups honestly.

**Step 8 final check and export (kit):** correct dimensions per image type, file format and size limits (read live), what to do if text is garbled, tips for mobile sharpness (large type, high contrast, thumbnail test at 300 px wide).
