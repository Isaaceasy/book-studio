---
name: interior-images
description: Stage 5b IMAGES. Creates and places the interior figures for one chapter: SVG wherever the figure can be drawn (infographics, diagrams, charts, flowcharts, schematics, labelled figures) and HiggsField only for figures that need it (illustrations, anatomical artwork, scenes, photo-like images). Consistent style, visual inspection, AI-disclosure record. Use for one chapter, normally called from /write-chapter.
---

# /interior-images <chapter> — Stage 5b: FIGURES (SVG FIRST, HIGGSFIELD WHEN NEEDED)

## Purpose
Add the planned figures to one chapter so that they are accurate, rights-safe, legible, consistent in style and honestly recorded for the KDP AI-disclosure. The owner's decision (`image_source: hybrid` in `book.yaml`): use SVG wherever a figure can be drawn as SVG; use HiggsField only for figures that SVG cannot do well.

## Routing rule (decide per figure, record the choice in the figure list)
- **SVG (default, written by Claude):** infographics, diagrams, schematics, flowcharts, process and cycle diagrams, concept maps, timelines, comparison graphics, charts and graphs of computed values, free-body and circuit diagrams, labelled technical figures, simplified anatomy or physiology diagrams with labels, icons, layouts. Anything containing text, numbers, labels, exact geometry or data goes here, because SVG text is exact and the figure can be verified.
- **HiggsField:** figures that need artistic or photographic rendering that cannot reasonably be drawn as clean SVG: realistic or richly shaded illustrations, anatomical artwork, scenes, people, objects, textures, cover-style art, mood images. Prompts contain NO text inside the picture; labels go in the caption, a key or a table.
- If a figure needs both (a rendered illustration plus labels), generate the illustration with HiggsField without text and state in the caption or an in-text key how to identify parts; do not overlay text unless the owner asks.
- When unsure, choose SVG. Tell the owner in one line which route each figure takes.

## Inputs
`outline.md` figure allocation for this chapter, `book.yaml` (`image_count`, `image_mode`, `image_source`, `accent`, `heading_style`), `style-guide.md`, `book-bible.md` (image style section), the chapter file, `profiles/docx-house-style.md` section 4.

## Step-by-step procedure

1. **Read the allocation.** List the figures planned for this chapter with subject, what must be shown and why. If the allocation is zero, record "no figures planned" and stop.

2. **Resolve the mode** from `book.yaml`:
   - `ASK`: in STANDARD mode ask the owner (AskUserQuestion) once for this chapter: YES, NO, or EXTERNAL. In AUTONOMOUS mode ASK is not allowed; use YES.
   - `YES-ALL`: create every planned figure.
   - `NO-ALL`: create none; remove figure mentions from the chapter, renumber, reduce `image_count`, record it.
   - `EXTERNAL-ALL`: write Figure Briefs to `images/figure-briefs.md` and leave clearly marked slots (`[FIGURE N.M — owner supplies: description]` on its own line; the build QC lists outstanding slots). Never a blank or dummy picture.
   - `MIXED`: apply the per-chapter instruction in `book.yaml`.

3. **For each HiggsField figure, check the connector.** Load the HiggsField tools with ToolSearch (query `mcp__HiggsField__` — fetch at least `generate_image`, `show_generation_by_ids`, `jobs_wait`, `models_explore`, `media_import_url` and `balance` as needed). If the tools are not present in this Code session, tell the owner in one sentence: HiggsField is not connected here; connect it in the Claude connector settings, or reply EXTERNAL to leave marked slots for those figures only. SVG figures continue regardless. Never substitute another generator and never fake an image.
   Before the first generation of a book, call `balance` and tell the owner the approximate cost if the tool reports it. Respect any budget the owner states; in STANDARD mode ask before spending beyond the first chapter's figures if the tool shows a cost per image.

4. **Fix the book's visual style once** (first chapter with figures), write it in `book-bible.md` under "Image style", and reuse it in every prompt: medium (for example clean flat vector-style technical illustration, or soft anatomical illustration), palette (the book's accent plus neutrals), background (plain white or very light), line weight, perspective, level of detail, aspect ratio (3:2 or 16:9 landscape so it fits 6.5 in wide), and the fixed negative rules below.

5. **Write each prompt** from the figure's purpose: subject, what it must show, composition, the style block. Always include these rules in the prompt: no text, letters, numbers, labels or watermarks inside the image; no logos, brands, trademarked characters or real people; no extra decorative elements; single clear subject; plain background. Medical: schematic, anatomically correct, not graphic or gory, age-appropriate. Engineering: correct geometry, directions and relationships described explicitly (for example "simply supported beam, load arrow pointing down at midspan, two triangular supports, no dimensions"). Identification of parts is done in the caption, an in-text key or a table, because generators garble lettering.
   **Never use an image generator for** exact data charts, plotted equations, dimensioned drawings or anything where wrong numbers or geometry would mislead; those are always SVG drawn from the computed values.

5b. **SVG figures:** hand-write clean SVG in `books/<slug>/images/chNN-figM.svg`: plain shapes, lines, text and paths only; no embedded raster, external references, scripts, web fonts or links; viewBox with 3:2 or 16:9 proportions; text at least the equivalent of 9 pt on a 6.5 in page; strokes at least 1.5 px; every axis, unit, part and angle labelled in the book's language; colours from the book's accent plus neutrals; meaning never carried by colour alone; values plotted from the actual equations, never by eye; same line weights, arrowheads and label style across the book. The build renders SVG to 300 dpi automatically. Insert as `![Figure N.M: caption](images/chNN-figM.svg)`.

6. **Generate HiggsField figures** with `generate_image` (or `generate_image_batch` for several figures), wait with `jobs_wait`, and retrieve the results. Download each finished image into `books/<slug>/images/chNN-figM.png` (or `.jpg` if that is what is delivered) using the file URL the tool returns; if the tool only displays the image and gives no downloadable URL, tell the owner exactly where in HiggsField to download it and to place it in that folder with that file name, and continue with the other work. Record the HiggsField job or media id of every image in `status.md`.

7. **Inspect every image** (Read the PNG). Reject and regenerate (maximum 3 attempts per figure, then report) if there is: garbled or unwanted text, wrong anatomy or mechanics, wrong number of parts, artifacts, extra limbs or fingers, a recognisable brand/character/person, inappropriate content, low resolution (needs at least 1800 px on the long side for 6.5 in at 300 dpi; use `upscale_image` if available and needed), or a mismatch with the chapter text. Check that the picture agrees with what the chapter says about it.

8. **Insert** (HiggsField figures) at the planned place: `![Figure N.M: caption in the book's language](images/chNN-figM.png)` with a caption that says what to look at and carries any key, plus a sentence in the text before the figure that refers to it. The build sets width to 6.5 in; the file must therefore be landscape or square.

9. **Verify by rendering.** Build the chapter preview (`/preview-chapter NN`), convert pages to images and look at each figure: whole, centered, caption below, legible, not overflowing the page.

10. **Record.** In `status.md` AI-disclosure facts: figure ids, how each was made ("written by Claude as SVG" or "generated with HiggsField" with date and job id). KDP requires disclosure of AI-generated images; the owner makes the declaration in the KDP form (see `/kdp-upload-guide`). Also keep a short rights note: generated by the owner's own tool account, no reference images from third parties used.

## Rules
- No figure without a purpose; no decorative filler.
- No copyrighted material, logos, real people's likenesses, trademarks or reference images the owner does not hold rights to.
- Never change the figure total without owner approval.
- A figure that fails inspection is regenerated or removed, never shipped.
- Never claim an image was generated or checked when it was not.
