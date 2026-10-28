---
name: clinical-clearance
description: Medical and engineering profiles only. Builds the Clearance Pack (master audit table sorted for the qualified reviewer), tracks clearance status, and applies the reviewer's corrections to the home entry or chapter and every bridging place, then rebuilds the final file without the draft label. Use after assembly and before publication.
---

# /clinical-clearance — BATCH CLEARANCE BY A QUALIFIED HUMAN (clinician or technical reviewer)

## Purpose
These frameworks do not replace qualified review. A qualified human must clear every flagged item before publication. For the medical profile this is a qualified clinician with native-level command of the book's language; for the engineering profile a qualified engineer (with native-level command of the language for non-English books). Clearance is a single batch gate after assembly, not a gate between chapters. Until clearance is recorded, the manuscript is a DRAFT_FOR_REVIEW and must not be published.

## Commands handled by this skill
- `BUILD CLEARANCE PACK` (also run automatically at the end of `/assemble-book`).
- `RUN CLINICAL QC` / `RUN TECHNICAL QC`: re-check the open items for a chapter or the whole book.
- `APPLY CLINICAL CORRECTIONS` / `APPLY TECHNICAL CORRECTIONS`: apply the reviewer's corrections.

## BUILD CLEARANCE PACK
1. Read every `audits/chNN-audit.md` and `verification-log.md`.
2. Compile `final/Clearance-Pack.docx` (and a `.md` source): ONE master table covering every chapter or Part, with columns: Chapter or Part, entry or section, claim or value, class, Cleared by, Date, Correction. Sort so the highest risk comes first: medical profile (D) drug or dose, then (S) safety, then (C) uncertain, then (B) needs external verification, then (N) number format, then (T) terminology; engineering profile (C), (B), (N), (T). Class (A) rows are omitted unless the reviewer asks.
3. Add a cover sheet: book title, language, region, publication date used, scope (including whether dose figures and special populations are in scope), the number of rows per class, and what the reviewer is being asked to do (check each row against current authoritative material for the region and publication date, mark cleared or give the correction).
4. Add a one-page "How to review" note: where the verification log is and what source we opened for each item, so the reviewer can check quickly.
5. Name the delivered manuscript with `DRAFT_FOR_REVIEW` in the file name until clearance is recorded. The label appears in the file name and delivery message only, never inside the manuscript.
6. Update `status.md`: clearance status = PENDING with the date and the row counts.

## APPLY CORRECTIONS (when the reviewer returns the table or a list of corrections)
1. Read each correction. For each row: locate the HOME entry or chapter where the concept is explained, apply the correction there, then find and update every bridging passage, cross-reference, example, table, figure, review question and answer key that depends on it (search the whole book, including `book-bible.md` and the terminology table). Corrections to foundational material can touch many places in later chapters; propagation is mandatory.
2. Re-run `/fact-check` on every changed passage (the reviewer's correction is a claim too: record the reviewer's name or initials, the date and the source they gave in `verification-log.md`; if they gave no source, record that it was a reviewer judgment). Re-run `/amazon-compliance` for the affected chapters (scope `chapter N`).
3. Mark each row Cleared by, Date, Correction in the pack.
4. Rebuild the book (`python scripts/docxbuild.py book books/<slug>`), rerun the QC, rename the final file without `DRAFT_FOR_REVIEW` ONLY if every row is cleared; otherwise keep the label and list the open rows.
5. Update `status.md`: clearance status = CLEARED (date, reviewer) or PARTIAL (open rows).

## Rules
- You never clear an item yourself. You never write a reviewer's name you were not given. You never imply the book is clinically or technically approved without a recorded human clearance.
- Class (D), (S) items (medical) and safety-factor, design-code, material-specification items (engineering) always require the human reviewer.
- If the reviewer disagrees with a claim you verified, the reviewer's correction is applied and the disagreement is logged; if you believe the correction is wrong, tell the owner and cite the source you opened, but do not override the reviewer.
- Never publish. Tell the owner plainly: "This book must not be published until the reviewer's clearance is recorded."
