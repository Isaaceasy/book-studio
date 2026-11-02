---
name: coloring-studio
description: Produces clean, usable coloring-page line art for coloring and activity books with HiggsField, then cleans each page by script (high-contrast black lines on white, closed shapes, no stray gray, correct size and margins) and lays out the interior. Never ships placeholders or AI images with garbled details. Use for coloring-book profiles or coloring sections.
---

# /coloring-studio: COLORING PAGES THAT ARE REALLY COLORABLE

## Purpose
GENIE Pro "coloring projects receive clean, usable line art rather than placeholders". Page quality decides reviews: closed shapes, consistent line weight, no gray shading, enough white space to color.

## Inputs
`brief.md` (theme, audience age, page count, style), `cms-research.md` (bestseller themes and page counts; gaps), `book.yaml` (trim; coloring books are commonly printed single-sided with a blank or test page behind each picture: verify the competitor convention), `interiors/`, `style-guide.md`.

## Procedure
1. **Plan the set**: a list of subjects (one per page), a style sheet (line weight, level of detail by age: bold simple lines for young children, finer detail for adults), a consistency rule (one art style across the book) and a variety plan (no near-duplicates). Check that subjects are original, not trademarked characters, logos or real people.
2. **Generate with HiggsField** (generate_image or the batch tool): prompt pattern: "Black and white coloring page, clean continuous outline art, no shading, no gray, no filled black areas, white background, centered subject, thick consistent lines, [subject], [style level]". Generate 2 variants per page, record prompt, model, job id and date in `coloring/figure-log.md`.
3. **Reject** pages with garbled anatomy (extra limbs or fingers), broken or open outlines, lettering, signatures, watermarks, clutter, or look-alike characters.
4. **Clean by script**: `python scripts/line_art_clean.py in.png out.png --size 2550x3300` converts to pure black on white (threshold), removes specks, closes tiny gaps, optionally thickens lines, trims to the page safe area, checks the black ratio (not too heavy) and the 300 dpi size. Review the report; fix failures.
5. **Layout**: place pages per the interior design (single-sided with blank backs or printed on one side as the style demands), page numbers, title page, "this book belongs to" page, test-color page if useful. Keep within KDP margins for the trim.
6. **QC**: render and inspect every page; `scripts/preflight_interior.py`; compliance scope `coloring` (no trademarked characters; AI-generated images disclosed).
7. **Deliver** the interior PDF and `coloring/` sources; update `status.md` AI-disclosure facts (all images AI-generated).

## Rules
- A page that cannot be colored cleanly is regenerated or dropped; never padded with placeholders.
- No real people, brands, characters from films or games.
