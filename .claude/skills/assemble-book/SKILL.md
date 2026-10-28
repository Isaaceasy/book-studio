---
name: assemble-book
description: Stage 6 ASSEMBLE. Builds the final manuscript after all chapters are approved. Word profiles produce the master DOCX (title page, copyright page, static contents, chapters, glossary, static index, correct page numbering) plus a PDF test copy and a QC report; the general profile produces the KDP interior PDF with margin and page-count checks. Then runs the compliance review and, for medical and engineering books, prepares the Clearance Pack. Use only when every chapter is approved.
---

# /assemble-book — Stage 6: ASSEMBLE, QC, FINAL COMPLIANCE

## Purpose
Turn the approved chapters into the final production file and prove by inspection and measurement that it is complete, consistent, correctly formatted and compliant. Source files are never deleted.

## Pre-flight (stop if any fails)
1. Every chapter row in `status.md` shows fact-check, compliance, audit and preview as passed (STANDARD: owner-approved; AUTONOMOUS: built, labelled DRAFT_FOR_REVIEW).
2. No open NEEDS-HUMAN item in `verification-log.md` without a recorded owner acceptance.
3. Front matter files exist or are generated: title page, copyright page, (optional) dedication, acknowledgements, about the author (only with real information supplied by the owner; never invented), contents (generated), preface or how-to-use. Back matter: glossary, symbol or abbreviation list (as planned), appendices, index terms file `back/index-terms.txt` (medical profile requires an index; engineering when planned). Ask the owner (STANDARD) for author name, copyright holder, year, edition, ISBN if they have one (leave "ISBN: pending" otherwise) and dedication text. In AUTONOMOUS mode use the values collected earlier or the documented defaults.

## Procedure

### Word profiles (engineering, medical)
1. Write or update `front/*.md` and `back/*.md` using the conventions in `profiles/docx-house-style.md`. The copyright page contains: title, author or pen name, copyright line, rights wording, edition, publisher if given, disclaimers required by the brief (medical: educational use, not a substitute for professional care; engineering: not a substitute for a licensed engineer's judgment where the brief says so). No URLs. No ISBN invented.
2. Check the toolchain: `python scripts/docxbuild.py check`.
3. Build: `python scripts/docxbuild.py book books/<slug>`.
   Outputs: `final/<slug>-manuscript.docx` (the deliverable) and `final/<slug>-manuscript.pdf` (layout test copy).
4. Run QC: `python scripts/docxbuild.py qc books/<slug>`; it writes `final/qc-report.md`. It checks, among other things: page size and margins, fonts, styles in use, one drop cap per chapter, chapter word counts against floor and ceiling (excluding tables), table widths and indents, presence of images versus allocation, equation counts, no hyperlinks or bookmarks or comments or tracked changes or citations or URLs, front matter and body numbering, contents entries versus headings, index entries versus terms.
5. Inspect visually: convert the PDF to images and look at the title page, copyright page, contents, the first page of three chapters (drop cap, heading style), a page with a table, a page with a figure, the glossary and the index. Verify TOC page numbers match the headings' actual pages in the test copy.
6. Fix every QC failure at the source (Markdown, config or script input), rebuild, re-run QC. Repeat until the report has zero failures. Warnings must be explained in the report.
7. Tell the owner plainly that the contents and index page numbers were calculated from the LibreOffice layout and that Word may paginate slightly differently, so they should open the file in Word and compare a few contents and index entries with the real pages (the contents are static text, not a Word field) and tell Claude if any differ so it can adjust.

### General profile (KDP print PDF)
1. Complete front/back matter as above.
2. `python scripts/bookbuild.py check`, then `python scripts/bookbuild.py book books/<slug>`.
3. Verify page count against the planned count, the gutter (inside margin) against the KDP table for the final page count (confirm the live KDP numbers), bleed settings, fonts embedded (pypdf), no text outside the safe area, all images at least 300 dpi at printed size.
4. Look at the pages as images (title, copyright, contents, three chapter openers, an image page, the last page).

### Final compliance and customer-experience pass (both)
Run `/amazon-compliance manuscript` over the whole file (consistency of the promise with content, placeholders, repeated or missing content, formatting faults, AI-disclosure facts compiled in `status.md`, disclaimers present). Fix every FIX; stop on BLOCK.

### Clearance Pack (medical and engineering)
Run `/clinical-clearance` to prepare the review pack for the human clinician or technical reviewer (claims ledger, high-risk items, calculations, tables, corrections log). Explain to the owner that the book must not be published as authoritative until a qualified person has reviewed it; the reviewer's corrections are applied with `APPLY CORRECTIONS`.

## Preserve everything
Do not delete or overwrite sources. Copy the final DOCX (and PDF) with a date-stamped duplicate in `final/archive/` before any rebuild after owner edits.

## Report (at most 6 lines)
Files and where they are, total pages and words, QC result (counts of fail/warn), compliance verdict, clearance status, and the next step: `/kdp-metadata` then `/kdp-upload-guide`.

## Rules
- Never claim a QC item passed that the report did not measure.
- Never publish, upload or log in anywhere.
- If the owner edits the DOCX by hand, treat their file as the new master and tell them which later rebuilds would overwrite it.
