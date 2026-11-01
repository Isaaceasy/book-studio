# Cover Log: Emergency Nursing Fundamentals (cover-design test run, 2026-11-02)

## Decisions
- Competitor cover scan (16 Amazon results for "emergency nursing", viewed in the built-in browser 2026-11-02): crowded red, white and black covers with cartoon nurses, stethoscopes, heartbeat lines, badges ("NCLEX", "Complete", "10 Units"); one bold yellow bestseller with organ illustrations; publisher titles in calm blue and orange geometric blocks. Differentiation chosen: clean dark poster with one anatomical illustration, no people, no badges.
- Owner chose concept B (dark anatomy poster) from four concepts (A five priority discs, B dark anatomy poster, C teal field guide, D crimson color-block split).

## Specifications used (KDP help G201953020 read 2026-11-02)
- Trim 5 x 8 in, standard color, white paper, 179 interior pages (KDP prints 180), spine = 180 x 0.002252 = 0.4054 in, wrap 10.6554 x 8.25 in, bleed 0.125 in, safe margins 0.25 in (stricter than KDP's 0.125 in), barcode zone 2 x 1.2 in reserved bottom right of the back cover.
- Ebook cover: 1600 x 2560 px JPEG RGB (ratio 1.6, KDP ideal 2,560 high).

## Generated images (all AI-generated: disclose to KDP)
| Item | Tool and model | Job id | Date | Notes |
|---|---|---|---|---|
| Front art (chosen) | HiggsField gpt_image_2_5, 2:3, 2 variants | ec350de9-6c48-42b7-8d5a-eda068073ef7 (other: cca3ed5c-c69a-49f8-8aaa-d2a6d9bfc63a, unused) | 2026-11-02 | 688 x 1024 px; no lettering in the art; lung, airway and heart anatomy must be looked at by the clinician |
| Back background | HiggsField gpt_image_2_5, 2:3 | 4a3a3dad-a51f-4074-80d5-f14cf4ca00c1 | 2026-11-02 | faint contour lines and heart outline; no lettering |
| Front art upscale 4K | HiggsField bytedance_image_upscale | eb2a3430-6e11-4703-a5e8-0efb936dce6c | 2026-11-02 | 2764 x 4096 px (about 440 dpi at 6.3 in wide); used for print |
| Back upscale 2K | HiggsField bytedance_image_upscale | e66e0f69-7583-4caf-8bb9-21fe6ae684b5 | 2026-11-02 | 2160 x 3200 px |

Prompt (front): "Premium editorial book cover artwork for a medical education guide. Deep navy-charcoal background (#101826). One large, elegant, simplified anatomical illustration of the human airway, lungs and heart, drawn as refined crimson (#A31C2C) line art with thin precise contours and a very soft red glow, centered ... Large empty dark space above and below ... Flat vector style ... No text, no letters, no numbers, no labels, no logos, no watermarks, no people, no faces, no hands."
Prompt (back): "Subtle abstract back-cover background for a medical book. Deep navy-charcoal (#101826) with very faint, low-contrast crimson (#A31C2C) fine contour lines and a barely visible line-art outline of a heart in the lower area, lots of calm empty space for paragraphs of text ... No text ... no people."
Image tool terms: HiggsField official terms page read 2026-10-29 (cloud session): outputs may be used commercially; provenance metadata may be embedded; re-check before publication.

## Composition
Text set by `v3/scripts/cover_compose.py` from `cover-brief.yaml` (title, subtitle, author exactly as in `book.yaml`; back copy taken from the approved description in `final/KDP-metadata.md`). Fonts: Inter static TrueType embedded. Spine text reads top to bottom (US convention).

## Files
`paperback-wrap.pdf` (print), `ebook-cover.jpg`, `front-cover.png`, `thumbnail-test.png`, `wrap-preview.png` (visual check only), `cover-brief.yaml`, `art/`.

## Preflight (scripts/preflight_cover.py): all mechanical checks PASS on 2026-11-02.
Still to do by the owner: view the wrap in KDP's cover previewer or upload preview, order a proof copy, confirm the spine position on the printed proof, and ask the clinician to look at the lung and heart illustration.

## Compliance review (2026-11-02, independent agent) and fixes
Result: REVISE, no Amazon-rule blocker (title, subtitle, author, dimensions 10.6554 x 8.25 in, spine 0.4054 in, safe margins, no invented barcode or ISBN, ebook spec all PASS).
Fixes applied: (1) back-cover paragraph 2 had no verb; the cover now begins "Written for ..." (deliberate cover variant of the description text; keep it recorded here, or change the description to match). (2) Fonts now embedded as TrueType (Inter static files; SIL Open Font License 1.1, confirm the licence file ships with the fonts). (3) PDF page size set exactly (Chromium had rounded the width up by 0.012 in). (4) Spine text direction set to top to bottom (US convention). (5) Art placement lowered so no illustration runs under the title block (wrap, front cover PNG and ebook).
Still open: clinician check of the lung, airway and heart illustration; confirm the PDF color space and print a proof copy (dark navy and thin crimson lines may print differently from the screen; check line sharpness since the art was AI-upscaled from 688 x 1024); view the wrap and ebook in KDP's previewer; answer YES to AI-generated images at upload; confirm the author spelling matches title page, copyright page and KDP author field; record the HiggsField terms re-check before publishing.

## STYLE CHANGE (2026-11-02): owner replaced the dark anatomy poster with concept A, priority discs`n- Active cover now: off-white ground, five discs lettered A B C D E (the primary survey order) in a crimson to blush gradient bleeding off the right edge, dark title block on the left, crimson spine, same approved back-cover copy. All text strings unchanged (they must equal book.yaml and KDP metadata). Art is drawn by 3/scripts/art_discs.py: NO AI image is used in this style, so the cover-art AI-disclosure item no longer applies to the cover (the interior figures are still AI-generated). No anatomy on the cover, so the clinician art check no longer applies to the cover.
- The first style is kept in covers/style-B-anatomy-poster/ (files, brief, HiggsField art).
- Preflight PASS (mechanical). A new independent compliance review of this style has NOT been run yet. Still to do: KDP previewer, proof copy (check the pale pink discs print visibly against the off-white), author spelling match.
