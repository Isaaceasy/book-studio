# WORD HOUSE STYLE (engineering and medical profiles)

Taken from the owner's EMB Unified Book Framework v1.8 and MEB Medical Encyclopedia Framework v2.1. `scripts/docxbuild.py` builds these rules automatically from Markdown. This file tells you (a) what the output must look like and (b) HOW TO WRITE THE MARKDOWN so the build produces it.

## 1. What the final Word file looks like (fixed unless the owner approves a change)

- Page: US Letter 8.5 x 11 in, portrait. Margins exactly 1 in on all four sides (content width 6.5 in, height 9 in). No automatic KDP gutter unless the owner approves a revised print specification.
- Body: Times New Roman 12 pt, fully justified, line spacing 1.15, consistent paragraph spacing. No tabs, repeated spaces or blank paragraphs for alignment or spacing.
- EVERY non-heading element is 12 pt: body, lists, tables, captions, callouts, notes, glossary, appendices, answer keys, index. Exceptions: the drop-cap letter and the title-page elements.
- Headings: Word's built-in Heading 1 (chapter or Part) and Heading 2 (section or entry). Heading 3 is disabled; use bold run-in labels at the start of a paragraph instead. Seven heading styles (the owner picks one number in `book.yaml: heading_style`):
  1 Black Banner · 2 Rule Line · 3 Numbered Block · 4 Centered Classic · 5 Shaded Bar · 6 Underline Accent · 7 Minimal Modern. The style changes headings and callout treatment only.
- Every chapter or Part starts on a new page. Manual page breaks only before chapters/Parts and approved major front or back matter divisions. Never before sections, examples, tables or figures.
- Drop cap: every chapter opens with one Word "Dropped" drop cap (3 lines, Times New Roman), never "In margin", on the first true body paragraph (after a Learning Objectives callout if one comes first). None in front matter, back matter, sections, lists, tables, captions, equations or callouts.
- Tables: real Word tables, exactly 6.5 in wide with zero indent, repeating header row, no row splitting, 12 pt text, caption ABOVE left-aligned 12 pt bold in the form `Table [Chapter].[Number]: [Description]`, and exactly one 12 pt line of space after the table (paragraph spacing, not an empty paragraph).
- Figures: centred, aspect ratio preserved, caption BELOW centred 12 pt italic `Figure [Chapter].[Number]: [Description]`, placed near first discussion, each mentioned in the text.
- Equations: every displayed equation is a native, editable Word equation (never code, LaTeX text, images or caret/underscore notation). All variables and units defined in the text.
- Lists: native Word bullets and numbering, hanging indents inside the margins, complete sentences end with a period, no one-item lists, properly ended before prose resumes.
- Front matter order: half-title (if approved), title page, copyright and disclaimer page, trademark disclaimer (if needed), dedication, acknowledgements, preface, introduction, how to use, static contents page, lists of figures/tables/abbreviations. Then chapters, then back matter (glossary, appendices, index).
- Pagination: title and copyright pages count but show no number; front matter in lowercase Roman numerals; Arabic numbering restarts at 1 on Chapter 1.
- Contents page and index are STATIC (no links, no fields) with page numbers computed from the rendered file.
- No hyperlinks, bookmarks, comments, tracked changes, hidden text, placeholders, `[FIGURE]` markers, URLs, DOIs, citations, bibliography.

## 2. How to write the Markdown so the build produces that

### Chapter file (`chapters/ch01-short-title.md`)
```
# Chapter 1: Title of the Chapter

::: {custom-style="Callout"}
**Learning Objectives**
:::

1. First objective as a complete sentence.
2. Second objective.

First true body paragraph (this receives the drop cap and must begin with a letter)...

## Section Heading

Text...
```
- One `#` heading per chapter file, written as `Chapter N: Title` (or `Part N: Title`, `Kapitel`, `Chapitre`, `Capítulo`). The build recognises these as chapters (drop cap, word count, contents).
- Back matter files start with a plain `# Glossary`, `# Appendix A: ...`: they are NOT chapters (no drop cap, no word floor).
- `##` for sections or entries. Never use `###`.

### Callouts
```
::: {custom-style="Callout"}
**Key Term:** Neutral axis. Definition in one or two sentences.
:::
```
Callout types (always bold label first): Learning Objectives, Key Term, Worked Example, Safety/Warning, Note, and for medical profile also Clinical Vignette and Red Flags. Callouts need a function, never decoration. A Learning Objectives callout is followed by a native numbered list written as normal Markdown (`1.`, `2.`).

### Equations
Inline: `$\sigma = \dfrac{M y}{I}$`. Displayed: a line containing only `$$ ... $$`. Number an equation by adding `\qquad (3.1)` inside the math. Use correct operators, units with `\,\mathrm{m/s^2}`, Greek letters, matrices, summations, integrals.
Never write plain-text equations with `^` and `_`. Never write the final equation as an image or a code block.

### Tables
```
Table: Table 1.1: Sample section properties.

| Section | I (mm4) | Notes |
|---|---|---|
| Rectangle | 1.0e6 | Simple |
```
Put the `Table:` caption line directly above the pipe table. Mention every table in the prose. Keep all content in cells short enough for 12 pt in the width; if too wide, simplify or split the table.

### Figures
```
![Figure 1.1: Short descriptive caption.](images/ch01-fig01.svg)
```
Use a relative path starting with `images/`. SVG files are rendered to 300 dpi automatically (the SVG source stays in `images/`). HiggsField images are saved as PNG or JPG (landscape) and inserted at 6.5 in wide automatically; reference them as `images/ch01-fig02.png`. Never leave a `[FIGURE]` planning marker in a finished chapter.

### Worked examples and answers
Use a Callout labelled `**Worked Example.**` with the full solution in prose and equations; put the final boxed answer in its own `::: {custom-style="Callout"}` block starting `**Answer:**`.

### Front matter files (`front/preface.md`, `front/introduction.md`, `front/how-to-use.md`)
Each starts with one `# Title` line. Title page, copyright page and contents page are generated by the build from `book.yaml`; never write them by hand and never invent publisher details, ISBN, addresses, dedications or acknowledgements. Optional keys in `book.yaml`: `publisher`, `isbn`, `copyright_text`.

### Index (optional, medical encyclopedias especially)
Put one term per line in `back/index-terms.txt`. The build creates a static index with page numbers.

### Typography by language
- English: curly quotes automatically.
- French: write « guillemets » with no-break spaces inside; space before `: ; ! ? %`; decimal comma; thousands separator thin no-break space (1 000,5); value and unit separated by a space (9,81 m/s²).
- German: „low-high“ quotes (or »…«); decimal comma; thousands separator period (1.000,5).
- Spanish: «comillas latinas» or “inglesas”; ¿…? and ¡…! inverted opening marks; Spain: decimal comma and thin-space thousands; Mexico: decimal period and comma thousands (set by `region`).
For fr/de/es write the native punctuation directly in the Markdown (automatic English smart quotes are turned off).

## 3. Build and quality control

- One chapter preview: `python scripts/docxbuild.py chapter books/<slug> chapters/chNN-name.md`
- Whole book: `python scripts/docxbuild.py book books/<slug>`
- Any file: `python scripts/docxbuild.py qc path/to/file.docx`
Automatic checks: page size and margins in every section; hyperlinks; bookmarks; comments; tracked changes; drop cap count and position (Dropped, not margin); fonts and sizes; table width, zero indent and post-table spacing; placeholder, URL, DOI, visible-LaTeX and reference-list text; blank paragraphs; figure count against the approved allocation; per-chapter word counts (excluding tables) against the floor.
Still human: open the file in Microsoft Word, page through it, confirm contents page numbers (computed from a LibreOffice rendering, which can paginate slightly differently), confirm drop caps and tables sit inside the margins. Always inspect rendered pages visually; never rely only on the automatic checks.

## 4. Images in Word profiles (SVG first, HiggsField when needed)

Owner decision: use SVG wherever a figure can be drawn as SVG (infographics, diagrams, schematics, flowcharts, charts of computed values, labelled technical figures, simplified labelled anatomy); use the HiggsField image tool only for figures that need artistic or photographic rendering (illustrations, anatomical artwork, scenes, objects, people). `image_source` in `book.yaml` is `hybrid`. Anything with text, numbers or exact geometry is SVG, because image generators garble lettering and cannot be verified numerically; HiggsField prompts therefore ask for no text inside the picture and identification goes in the caption, an in-text key or a table. All figures are original and rights-safe (no copyrighted characters, brands, logos, real people), in one consistent style for the whole book, 3:2 or 16:9 landscape so they fit 6.5 in wide with aspect ratio preserved, legible at print size, with correct labels in the book language, no scripts, external resources or hyperlinks in SVG. Every figure is inspected visually before insertion. Figure allocation per chapter is fixed at the architecture lock and cannot be changed without approval. Image modes (`image_mode` in `book.yaml`):
- `ASK` (STANDARD runs only): after the chapter is written, word floor met, fact-check and audit table done, ask exactly: "Chapter [N] requires [COUNT] visual(s). Reply YES to have me generate them with HiggsField and insert them, NO to skip figures for this chapter, or EXTERNAL if you will create the images elsewhere and want figure briefs." Wait for the answer.
- `YES-ALL`, `NO-ALL`, `EXTERNAL-ALL`, or a per-chapter `MIXED` list.
- NO: set that chapter's allocation to zero, remove its figure mentions, renumber later figures, reduce `image_count`, log it.
- EXTERNAL: write a Figure Brief per figure in `books/<slug>/images/figure-briefs.md` (number, caption, placement, subject, composition, exact labels, facts that must be correct, size up to 6.5 in wide, aspect ratio, file name `Figure_<chapter>.<n>`, alt text, rights requirement) and insert a reserved empty Image Slot with the caption and in-text reference; list outstanding slots in the QC report.
