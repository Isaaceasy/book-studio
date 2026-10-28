---
name: fact-check
description: Fact-checks every claim in a chapter, Part, description or other content against real sources opened live, recomputes every calculation, and records results in the internal verification log. Nothing is complete until the ledger is clear. Use for one chapter at a time (called from /write-chapter) or on any content the owner wants checked.
---

# /fact-check — EVERY CLAIM VERIFIED, NOTHING INVENTED

## Purpose
The owner's rule: every piece of content you generate must be fact checked. This skill builds and clears the claim ledger for a piece of content. The ledger is internal (`books/<slug>/verification-log.md`) and never enters the manuscript (the manuscript carries no citations, footnotes, bibliography, URLs or DOIs).

## Independence
The check is performed by the `fact-checker` subagent (`.claude/agents/fact-checker.md`) so it is independent of the writer. If that agent type is unavailable, use a general-purpose agent and paste its instructions. The writer then fixes what is found. Do not tell the checker your opinion of the content.

## Inputs
Argument: chapter number or file path (also works on `outline.md`, descriptions, subtitle options, or any text). Files: the chapter, `book-bible.md` (facts register and terminology), `book.yaml` (profile, language, region, publication_date), `outline.md` (verification targets), the profile file.

## Step-by-step procedure

1. **Extract the claim ledger.** Read the content line by line and list EVERY checkable statement as a row. Claim types:
   - FACT (historical, scientific, technical, institutional), STAT (any number, percentage, rate, price, quantity), DATE, NAME (person, organisation, product, place), STANDARD (code, regulation, classification, guideline), CONSTANT or PROPERTY (physical constant, material property, reference range), EQUATION (every formula), CALC (every worked example, conversion, numeric answer, practice-problem answer, boxed answer), LEGAL or FINANCIAL, DRUG (every medicine statement), DOSE (every dose, frequency, duration, route), SAFETY (any statement a reader could act on in a harmful way, and the presence or absence of warnings), DEFINITION (technical term and its native-language equivalent), CURRENCY (anything time-sensitive: latest guideline, approval, price, version, event).
   Number the rows with an ID such as `C03-017` (chapter 3, claim 17).

2. **Verify each claim against real sources you actually open** with WebSearch / WebFetch (or the browser). Prefer authoritative and primary material: standards bodies, official guidelines, regulators, peer-reviewed or institutional publications, manufacturer technical documentation (for facts, not promotion), government statistical offices, textbooks of record. Cross-check important claims with at least two independent sources and record both. Confirm time-sensitive items against current material as of `publication_date`. Distinguish established fact from opinion, estimate, assumption and inference, and use calibrated wording in the text accordingly. Do not rely on memory or on a single secondary website. Do not mark a claim verified unless you opened the source and found the claim supported.

3. **Recompute every calculation yourself.** For every EQUATION, CALC, unit conversion, table value and boxed answer: reproduce the result with Python (`python3 -c` or a small script, sympy for symbolic work), check dimensional consistency and unit tracking, check significant figures, and check the number format against the language and region convention. A calculation is VERIFIED only when your independent recomputation matches. Record the code or the formula check in the ledger (short form).

4. **Classify each row** with a status:
   - VERIFIED — source(s) opened, claim supported (or calculation reproduced).
   - QUALIFIED — supported only in part or with conditions; the text was rewritten to say exactly what is supported (calibrated language, region limits, "estimates vary").
   - REMOVED — could not be verified; deleted from the content.
   - CORRECTED — found wrong; text corrected, correction verified.
   - NEEDS-HUMAN — requires a qualified specialist (engineering profile: safety factors, design codes, material specifications; medical profile: every DRUG, DOSE and SAFETY item and any diagnostic criterion, screening interval or emergency advice; legal or financial advice). Never mark these VERIFIED on your own authority.
   For engineering and medical profiles also assign the Stage 3 audit classes: (A) self-contained, (B) needs external verification, (C) uncertain or possibly wrong, (D) drug or dose item, (S) safety item, (N) number format, (T) terminology. Class (D) and (S) rows are always NEEDS-HUMAN for clearance.

5. **Fix the content.** Edit the chapter (back up first to `chapters/_backup/chNN-before-factcheck.md`): remove or qualify unverifiable claims, correct errors, never replace an unverifiable claim with an invented one, never add a citation to the text. Add confirmed facts and their sources to `book-bible.md` (facts register).

6. **Write the ledger** to `books/<slug>/verification-log.md` (append a section per chapter) with columns: ID, claim (short), type, class, source 1 (title, publisher, URL, date accessed), source 2, method (for CALC), status, action taken, human reviewer / date (blank until cleared). Keep this file out of every build.

7. **Write the audit table** for engineering and medical profiles to `audits/chNN-audit.md` (the separate Stage 3 table: every equation, number, answer, constant, property, standard, and for medical every drug, dose and safety item; classes as above). Output only the table in that file.

8. **Re-check** the edited content (repeat steps 1 to 4 on changed text) until the ledger has no unverified row except NEEDS-HUMAN rows. Maximum 3 rounds; if rows remain unresolved, report them to the owner.

## Completion criteria
A chapter may be declared complete only when: every ledger row is VERIFIED, QUALIFIED, CORRECTED or REMOVED (or NEEDS-HUMAN and listed in the audit table for the reviewer); no calculation is unreproduced; no claim of any kind appears in the text that is not in the ledger; the content contains no citation, URL, DOI or invented source.

## Output to the owner (max 4 lines)
Counts per status, the number of NEEDS-HUMAN rows, where the ledger and audit table are, and anything removed that the owner may want to know about.

## Rules
- Never fabricate a source, quotation, statistic, study, standard, trial, case, guideline, price or date. Never "verify" from your own prior knowledge.
- If a page cannot be opened, say so, use another source, or remove the claim.
- The ledger honestly records what you actually opened. A source you did not open does not appear in it.
- Facts about Amazon rules and the market are verified the same way (live pages, date accessed).
