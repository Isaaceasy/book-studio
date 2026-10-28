---
name: design-interior
description: Stage 4 DESIGN SYSTEM. Sets the heading style (1 to 7) and accent for Word-format books and builds a sample chapter for approval; for KDP PDF books creates the book-specific color interior (palette, fonts, hierarchy, callouts, margins) as book.css with a sample PDF. Use after the architecture is locked and before writing chapters.
---

# /design-interior — Stage 4: DESIGN SYSTEM

## Purpose
Give the book a polished, consistent look BEFORE chapters are written, so every chapter preview is the real designed page. Two paths depending on `output` in `book.yaml`.

## PATH A — Word house style (engineering and medical, or `output: docx`)

The page layout, fonts and sizes are FIXED by the owner's frameworks (US Letter, 1-inch margins, Times New Roman 12 pt for every non-heading element, justified, 1.15 line spacing, one Dropped drop cap per chapter). Only the heading style and accent can vary.

1. **Present the heading-style menu** if `heading_style` is not yet confirmed. Use AskUserQuestion with short descriptions:
   1 Black Banner (white on solid black, centered chapter titles; grey-bordered callouts) ·
   2 Rule Line (centered caps with 2 pt rule; left accent bar callouts) ·
   3 Numbered Block (oversized chapter number above a left title; thin boxed callouts) ·
   4 Centered Classic (22 pt centered; hairline callouts) ·
   5 Shaded Bar (dark grey on light-grey band; shaded callouts) ·
   6 Underline Accent (left title with accent underline; bottom-border callouts) ·
   7 Minimal Modern (generous white space; indented callouts).
   Offer to build a sample of two styles so the owner can compare, then set `heading_style` and `accent` (a hex color without `#`) in `book.yaml`.
2. **Build a design sample chapter** `books/<slug>/previews/design-sample.md` with a chapter heading (`# Chapter 1: Sample Chapter`), a Learning Objectives callout and numbered list, two paragraphs in the style guide's voice (the first is the drop-cap paragraph), a `##` section, a native list, a Key Term callout, one inline equation and one displayed equation, a pipe table with a `Table:` caption, and (if SVG allocation exists) one simple figure (a HiggsField image if the connector is available, otherwise an SVG you draw for the sample only). Build it:
   `python scripts/docxbuild.py chapter books/<slug> previews/design-sample.md`
3. **Inspect visually.** Convert the preview PDF pages to images (`pdftoppm -r 60 -png`) and LOOK at them. Check: drop cap sits inside the text area; heading style correct; callout treatment correct; table exactly within the margins with one line of space after; figure centered with caption below; equation visible (note: LibreOffice without its Math component cannot draw Word equations in the PDF test copy; confirm the equation count in the QC printout and tell the owner to check equations in Word). Fix and rebuild until clean.
4. **Update `status.md`** (stage = DESIGN awaiting approval).

## PATH B — KDP print PDF (general profile)

1. **Decide the visual direction** from genre, audience and tone; write 3 lines in `status.md` (mood words, who it is for, what to avoid).
2. **Pick the palette**: one accent, one soft tint, near-black text. Check contrast (body text dark on white; white on accent at least 4.5:1). If `color_interior: false` use one dark gray accent and no tints.
3. **Pick fonts** that render in the owner's Chromium: Georgia + Arial; Palatino Linotype + Segoe UI; Times New Roman + Arial. Body 10.5 to 12 pt (larger for seniors and children), line height 1.4 to 1.6.
4. **Confirm trim and margins** in `book.yaml` (inside margin at least the KDP minimum for the estimated page count; see `CLAUDE.md` section 8; verify current numbers live).
5. **Write `books/<slug>/book.css`** overriding the variables in `templates/interior.css` (`--accent`, `--accent-soft`, `--body-font`, `--heading-font`, `--body-size`, `--line-height`), optional chapter-opener styling, callout variants (`.callout.tip`, `.warning`, `.exercise`), writing-space styling for workbooks. Comment every block in plain language.
6. **Update `book.yaml`** palette and fonts.
7. **Build a design sample** `previews/design-sample.md` (chapter heading, two sample paragraphs, section heading, list, blockquote, callout, table, optional image) and build it with `python scripts/bookbuild.py chapter books/<slug> previews/design-sample.md`. Render to images and inspect: margins, contrast, widows, callout breaks, spacing. Fix until clean.
8. **Update `status.md`** (stage = DESIGN awaiting approval).

## Approval gate (both paths)
Reply with at most 4 lines: the style or palette and fonts, and where the sample is (`previews/design-sample.docx` and `.pdf`, or `.pdf`). Ask the owner to approve or adjust. Apply changes, rebuild, repeat. On approval tick "Design system approved" and name the next step: `/write-chapter 1`.

## Rules
- Never change the approved design later without approval; a design change must be re-previewed on a full chapter.
- Word profiles: never change page size, margins, font or non-heading size; the framework fixes them.
- Keep the interior accessible: sufficient contrast, readable sizes, no text over busy images.
- Run `/amazon-compliance` scope `manuscript formatting` if anything about layout could create a poor reading experience (very small text, clipped elements).
