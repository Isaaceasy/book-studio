---
name: write-chapter
description: Stage 5 WRITE. Writes ONE chapter (or medical Part) from the locked architecture at the profile's word floor, then runs fact-check, Amazon compliance, images, editorial audit and preview in order, and stops for owner approval (STANDARD) or moves on (AUTONOMOUS). Use with a chapter number, e.g. /write-chapter 1, or to continue when chapters remain.
---

# /write-chapter <number> — Stage 5: WRITE, VERIFY, ILLUSTRATE, AUDIT, PREVIEW

## Purpose
Produce one finished, verified, compliant, designed chapter. Quality gates run in a fixed order and none may be skipped. Chapter files are the source of truth; nothing is "approved" until every gate below is ticked in `status.md`.

## Inputs
`outline.md` (this chapter's row, boundary map, figure allocation), `style-guide.md`, `book-bible.md` (terminology table, facts register), `brief.md`, `book.yaml`, `status.md`, `verification-log.md`, the profile file, `profiles/docx-house-style.md` for Word books, and the previous chapter's closing section for continuity.

## Pre-flight (stop if any fails)
1. Architecture lock, design and run-mode are recorded as approved in `status.md`. If not, name the missing stage and stop.
2. The chapter number exists in `outline.md` and the previous chapter is approved (STANDARD) or built (AUTONOMOUS). Never skip order.
3. If `run_mode` is AUTONOMOUS, append a start line to `run-log.md` and update `PROGRESS.md` (chapter, step, time).

## Step 1 — Write the chapter
Create `books/<slug>/chapters/chNN.md` (two digits, for example `ch01.md`). Rules:
- First line is the heading exactly as the house style requires: `# Chapter N: Title` (Word profiles) or the book's heading format (general).
- Follow the outline row exactly: every objective, key concept, equation, example, figure slot. Do not add, drop or rename without owner approval.
- **Length.** Engineering and medical: at least 10,000 and at most 12,000 words EXCLUDING tables (`chapter_word_floor` / `chapter_word_ceiling` in `book.yaml`). Reaching the floor must come from real substance (derivations, worked examples, edge cases, applications, common mistakes), never padding, repetition or filler. Write in several passes (append section by section) rather than one giant call; after each pass count words.
- **Engineering template:** learning objectives (Callout), theory built from fundamentals with derivations shown, at least 2 to 3 fully worked examples with units carried through every step, 5 to 10 practice problems with answers verified by recomputation, key equations and takeaways summary.
- **Medical template:** per `profiles/medical.md` (entry types, tiers, mandatory subsections, safety wording, no dose figures unless the brief allows them).
- **General:** the structure from the outline; tone and reading level from the style guide.
- Use only the terminology and notation in `book-bible.md`; add new terms there first.
- Equations as Pandoc math (`$...$`, `$$...$$`) so they become native Word equations. Tables as pipe tables with `Table:` captions. Figures as `![Figure N.M: caption](images/chNN-figM.png)` only after Step 5 creates them.
- No citations, footnotes, URLs, hyperlinks, bibliography entries or references to sources by name in the text (Word profiles). Plain-text cross-references ("see Chapter 4") only.
- Write for a human: varied sentence length, concrete examples, no filler openings, no banned phrases from `CLAUDE.md` section 6 and the style guide, no repeated paragraph patterns, no "In conclusion" tails, no unexplained jargon.
- Respect the non-repetition map: do not re-teach what has its home elsewhere; add the planned new angle instead.
- Localization: write in the book's language and region (units, number format, standards, drug names); never mix.

## Step 2 — Word count check
Use the preview build in Step 7 (it prints words excluding tables) or `python scripts/docxbuild.py qc books/<slug>` for the whole book. If below the floor, extend with substantive content and recount; if above the ceiling, tighten. Record the count in `status.md`.

## Step 3 — Fact-check (mandatory, blocks everything after it)
Run `/fact-check chapter NN`. Every number, standard, constant, material property, classification, reference range, historical or legal claim and every worked-example computation is entered in the claim ledger in `verification-log.md`, verified against sources actually opened (or recomputed), and assigned VERIFIED, QUALIFIED, REMOVED, CORRECTED or NEEDS-HUMAN. Apply every correction to the chapter file. No chapter proceeds with an open NEEDS-HUMAN item unless the owner has accepted the risk in writing, recorded in `status.md`.

## Step 4 — Amazon compliance review
Run `/amazon-compliance chapter NN`. Fix every FIX; stop on BLOCK. This also checks customer-experience risks (unmet promise, errors, padding, formatting faults).

## Step 5 — Images (SVG first, HiggsField when needed)
Run `/interior-images NN`. It follows the image allocation in `outline.md` and the image mode in `book.yaml` (ASK per chapter, YES-ALL, NO-ALL, EXTERNAL-ALL, MIXED). In STANDARD mode with mode ASK, ask the owner once for this chapter: "Chapter N has K planned figures. Reply YES (I create them: SVG where drawable, HiggsField for artwork), NO (skip), or EXTERNAL (I leave clearly marked slots and you supply them)." Never invent a figure the owner did not approve.

## Step 6 — Editorial audit
Run `/editorial-audit NN`. It calls the editor agent for readability, tone, structure, human-sounding prose, consistency with the bible and AI-style signals, fixes issues in the file, and re-checks until it passes. If the audit changed any fact or number, repeat Step 3 for those lines.

## Step 7 — Preview
Run `/preview-chapter NN` to build `previews/chNN.docx` and `.pdf` (Word profiles) or the PDF (general profile). Look at the pages as images. Fix every layout fault (clipped table or figure, stranded heading, drop cap overlap, wrong margin) and rebuild.

## Step 8 — Record and report
Update `status.md`: the chapter row (words, figures, fact-check result, compliance verdict, audit result, preview path, date) and the checklist. Update `book-bible.md` facts register and `verification-log.md`.

## Completion message (STANDARD mode)
Reply with at most 6 lines: chapter title; words (excluding tables); figures; fact-check summary (counts by status); compliance verdict; preview file names; then "Approve, or tell me what to change." STOP. Apply requested changes to the chapter, repeat Steps 3 to 7 for the changed parts, and only then mark the chapter approved. Name the next step: `/write-chapter N+1`, or `/assemble-book` after the last chapter.

## AUTONOMOUS mode
If `run_mode` is AUTONOMOUS, do not stop after Step 8: append the result to `run-log.md`, update `PROGRESS.md`, and continue with the next chapter immediately. Apply the autonomous defaults in `CLAUDE.md` section 9. Stop and report only for: a BLOCK verdict, an unresolved NEEDS-HUMAN item, a failed build, a missing tool, or the owner interrupting. Every chapter produced is labelled DRAFT_FOR_REVIEW in `status.md` until the owner (and, for medical and engineering, the human reviewer) clears it. If the session ends, the owner types RESUME and work continues from `PROGRESS.md`.

## Rules
- Never claim a check was done that was not done. Never invent a source, statistic, quote or example. Prefer removing a claim to guessing.
- Never move on with a failed gate.
- Never write the next chapter before this one has passed (STANDARD).
