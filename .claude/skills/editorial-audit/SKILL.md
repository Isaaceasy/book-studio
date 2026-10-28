---
name: editorial-audit
description: Stage 5c AUDIT. Runs an independent editorial audit on one chapter (readability, tone, structure, human-sounding prose, consistency with the bible, formatting conventions, AI-style signals, repetition) using the editor agent, applies fixes, and re-checks until it passes. Fact accuracy and Amazon compliance are separate gates. Use for one chapter or on any chapter the owner asks to check.
---

# /editorial-audit <chapter> — Stage 5c: EDITORIAL AUDIT

## Purpose
Catch quality problems a paying reader would notice, using a second pair of eyes (the `editor` agent) so the writing pass does not grade its own homework. Facts are checked by `/fact-check` and rules by `/amazon-compliance`; this audit makes sure those fixes did not damage the prose and that the chapter reads as a finished book.

## Inputs
The chapter file, `style-guide.md`, `book-bible.md`, `outline.md`, `book.yaml`, the profile file, `verification-log.md` (to see what fact-check changed), and the previous chapter's end.

## Procedure

1. **Run the mechanical checks yourself first** (Bash/Grep; report numbers):
   - Word count excluding tables against the floor and ceiling.
   - Heading structure: one `#` heading, sensible `##` and `###` hierarchy, no skipped levels, no empty section.
   - Forbidden items for Word profiles: URLs, hyperlinks (`](http`), footnotes, citation patterns such as "(Smith, 2019)" or "[1]", bibliography headings.
   - Banned phrases from `CLAUDE.md` section 6 and the style guide (list each hit with line).
   - Repetition: three or more repeated sentence openers in a row, repeated paragraph shapes, unusually overused words, repeated explanations of a concept whose home is another chapter.
   - Notation and terminology against the bible table (flag inconsistent symbols or terms).
   - Figure and table references: every figure and table mentioned exists and is numbered in order; every figure file exists.
   - Placeholders: no TODO, XXX, lorem, or `[FIGURE` slot unless image mode is EXTERNAL.

2. **Call the `editor` agent** with the chapter path and the list above. It returns a scored review (readability, tone fit, structure, flow and transitions, specificity, human-sounding quality, consistency, reader value) and a numbered list of defects with exact locations and suggested fixes.

3. **Fix the defects** in the chapter file with targeted edits (do not regenerate the whole chapter). Keep meaning stable: if a fix would change a fact or a computed value, send it back through `/fact-check` instead of editing silently.

4. **Re-check.** Repeat steps 1 to 3 until the editor reports no major defect and the mechanical checks are clean. Maximum 3 rounds; if still failing, report exactly what remains and why.

5. **Write `audits/chNN-audit.md`**: date, mechanical results (numbers), the editor's first-round and final-round scores, defects found and fixed, anything left (with reason), and PASS or FAIL.

## Reader test (always)
Read the first page, the middle and the last page as a paying reader would. Does the opening promise something specific? Is every section earning its place? Could a beginner follow it? Would the reader feel the money was well spent? Record one sentence on each.

## Rules
- Do not weaken accuracy for style.
- Do not add content just to raise a score.
- Never mark PASS with an open major defect.
- Report numbers, not impressions, wherever a number is possible.
