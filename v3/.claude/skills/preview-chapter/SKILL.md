---
name: preview-chapter
description: Stage 5d PREVIEW. Builds the editable Word file and a PDF test copy for one chapter (Word profiles via docxbuild.py) or the print-exact PDF (general profile via bookbuild.py), inspects the pages visually, fixes layout faults and reports file locations. Use for one chapter, normally called from /write-chapter, or whenever the owner wants to see a chapter.
---

# /preview-chapter <chapter> — Stage 5d: PREVIEW

## Purpose
Show the owner exactly how the chapter will look, and catch layout faults before the whole book is assembled.

## Procedure

1. **Identify the profile and output** from `book.yaml`.

2. **Build.**
   - Word profiles (engineering, medical, or `output: docx`):
     `python scripts/docxbuild.py chapter books/<slug> chapters/chNN.md`
     Output: `previews/chNN.docx` (the editable deliverable) and `previews/chNN.pdf` (a LibreOffice test copy for checking layout only). The script prints word count excluding tables, figure count, equation count, table count and QC warnings.
   - General profile:
     `python scripts/bookbuild.py chapter books/<slug> chapters/chNN.md`
     Output: `previews/chNN.pdf` and `previews/chNN.docx`.
   If the build fails, read the error and fix the cause in the chapter file or the book config (never by weakening the script), then rebuild. Report persistent failures with the exact message.

3. **Inspect visually.** Convert the PDF to page images (`pdftoppm -r 60 -png previews/chNN.pdf previews/chNN-page`) and view them with Read. Check and list the result of each:
   - Chapter heading in the chosen style; drop cap on the first paragraph of the chapter, inside the text block, no overlap.
   - Headings never stranded at the bottom of a page; no blank pages; no broken-looking widows or orphans.
   - Tables: exactly within the margins (6.5 inches wide, zero indent), one blank line after, header row readable, no clipped columns, long tables split sensibly.
   - Figures: centered, whole, caption below with the correct number, text legible.
   - Callouts consistent with the heading style.
   - Equations: counted in the QC printout. LibreOffice without its Math component may not draw Word equations in the PDF test copy (blank space is expected); confirm the equation count equals the number in the Markdown and tell the owner to check equations in Word.
   - Language typography (quotation marks, spacing before punctuation in French, decimal separators).
   - Page numbering: Roman numerals in front matter, Arabic from Chapter 1 (full-book build only).

4. **Fix and rebuild** until clean; record the number of rounds.

5. **Report to the owner** (at most 4 lines): file names and locations (`previews/chNN.docx`, `previews/chNN.pdf`), word count excluding tables, figure and table counts, and any note (equations render in Word; page numbers in the test copy may differ slightly from Word).

## Rules
- The DOCX is the deliverable; for Word profiles the PDF is only a layout check.
- Never edit the DOCX by hand; fix the Markdown or configuration and rebuild.
- Never claim a visual check you did not perform.
