# PROFILE: GENERAL NONFICTION / GUIDES / WORKBOOKS

For books outside the engineering and medical profiles (how-to guides, business, personal development, hobbies, workbooks, journals, narrative nonfiction, activity books). Output: KDP print PDF (6x9 default; `scripts/bookbuild.py`) plus Word previews. All standing rules in CLAUDE.md apply, including live market research, fact-checking and Amazon compliance. The owner may switch a general book to the Word house style with `output: docx` in `book.yaml`.

## What this profile inherits from the owner's frameworks
- The staged, approval-gated workflow, one chapter at a time.
- No citations, no bibliography, no URLs in the manuscript; sources live in `verification-log.md`.
- No hyperlinks; static contents page.
- Paragraph-based explanation; strict non-repetition across chapters; originality and trademark rules.
- A locked plan (outline, terminology, figure allocation) before writing.
- A separate audit table per chapter (classes A, B, C, N, T; add S for any safety-relevant statement).

## Differences from the Word-format profiles
- Length: set in the brief (words or pages). No fixed 10,000-word floor, but never padded; the outline gives each chapter a word target within plus or minus 10 percent.
- Chapter template: chosen by book type in the outline (how-to: problem, principles, method, mistakes, action plan; workbook: short teaching page, exercises, reflection; narrative: story arc with a lesson per chapter; children's: short text per spread with an illustration plan).
- Images: raster images from the connected image tool are allowed (PNG, 300 dpi at print size); every AI-generated image is recorded for the Amazon AI-disclosure question. Keep images consistent in style across the book.
- Formatting: the KDP PDF design system in `templates/interior.css` and `book.css`, margins checked against the page-count gutter table by the build script.
- Review gate: the owner approves each chapter; no external clinician or technical reviewer is required unless the content touches health, legal, financial or safety topics. If it does, flag those chapters to the owner and add the appropriate disclaimer; if the book is really medical or engineering, switch the profile.

## Health, legal, financial and safety content in a general book
Keep to widely accepted, clearly general information; add disclaimers; never promise outcomes; no advice to start, stop or change treatment; no income or investment guarantees. Flag every such passage in the audit table as class (S) so the owner can decide whether specialist review is wanted.
