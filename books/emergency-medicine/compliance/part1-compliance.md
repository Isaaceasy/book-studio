# Compliance and customer-experience review: Part 1 (chapters/ch01.md)

Date: 2026-10-29. Reviewer: independent compliance-reviewer pass. Scope: chapters/ch01.md (text, captions, Review Questions), images/ch01-fig1.svg to ch01-fig4.svg, back/answer-keys-part1.md. ch01.md was NOT edited.

## Research Proof (what was actually done)
Files read in full this session: CLAUDE.md (system context), profiles/amazon-compliance-checklist.md, profiles/medical.md (only the first lines of the tool output were seen; NOT read in full, so profile rules were judged through outline.md and style-guide.md), books/emergency-medicine/outline.md, style-guide.md, status.md, book.yaml, verification-log.md (Part 1 section), compliance/title-v2.md, .claude/skills/amazon-compliance/SKILL.md, chapters/ch01.md, back/answer-keys-part1.md, all four SVG files (fig3 contains an embedded JPEG that I extracted and viewed). compliance/title.md was listed but not read.
Checks run: grep of ch01.md for brand, course, organization, drug, dose, URL, citation, claim and banned-style terms; word counts by script; pdftotext and page images of previews/ch01.pdf (viewed contact sheet and pages 7 and 17).
Live KDP pages opened with WebFetch on 2026-10-29 (real opens, content returned):
| Page | Result |
|---|---|
| Content Guidelines (kdp.amazon.com/en_US/help/topic/G200672390 and G200672410) | Opened. No date shown. Requires AI-generated text, images and translations to be disclosed (AI-generated stays AI-generated after heavy editing; AI-assisted need not be disclosed); bars misleading descriptive content and content "typically disappointing to customers"; copyright, trademark and privacy are the publisher's responsibility. NO medical or health section on this page. |
| Metadata Guidelines for Books (G201097560) | Opened. Title field = title as on cover; title + subtitle under 200 characters; no other titles, authors, trademarks, rank claims or promotions; description may not contain URLs, reviews, review requests, time-sensitive or price text; keywords may not name other authors, rank or promotions. |
| Guide to Kindle Content Quality (G200952510) | Opened. Typos are a top complaint; missing content, missing promised images and content that misrepresents the book are critical; "excessively reused or repeated content within or across books" and content "too short" are listed as disappointing; metadata must match the book. No medical-claims section. |
| Low-Content Books (GGE5T76TWKA85DJM) | Opened. Nonfiction, manuals and textbooks are "generally not low-content"; this book is not low-content. |
NOT opened or not found (dependent checks marked UNVERIFIED): KDP Terms and Conditions (two URL guesses returned 404 or the wrong page); any KDP page dedicated to medical or health content (search found none; the Content Guidelines have no such section, so medical safety is judged against the book's own medical profile, not a KDP rule); KDP print requirements (not re-opened by me; the 2026-10-29 margin and image-resolution numbers in status.md are the owner session's, not verified here); KDP review/promotion rules page.

## Check table (checklist sections B and C)
| Check | Verdict | Evidence | Fix |
|---|---|---|---|
| B1 Illegal/infringing | FIX (T&C UNVERIFIED) | No copied passages, quotes, brands or real people in the text. Fig 1 box wording and the four-question "Remember" box track the published triage tool's decision points almost word for word ("immediate life-saving action", "high-risk situation, new confusion, severe pain or distress", "how many resources"). Ideas are not protected but wording close to a proprietary handbook is avoidable. KDP T&C not opened. Fig 3 raster provenance not recorded (see B13). | Fix 6, Fix 10 |
| B2 Originality | PASS | Text is fresh; 1.1 and 1.2 openers reuse the style guide's sample paragraphs, which is the book's own text. No source language found. | none |
| B3 Duplicate content | PASS | Nothing in the folder duplicates it; one internal overlap noted under C6. | Fix 9 |
| B4 Low/thin content | PASS | About 5,430 words (target 5,400, floor 5,000, ceiling 6,000), 24 preview pages, 4 figures, 5 entries, case, priorities, 8 questions. Review Questions are about 300 words against the 700 planned, offset by the rest; no blank or padded pages in the text. | none |
| B5 Harmful/dangerous | FIX | Safety wording defects: "if a neck injury is not possible, tap or shake" (confusing double negative, can be read as shake when injury IS possible); Safety box "do not move an injured patient unless the scene is unsafe" has no exception for the unresponsive, non-breathing patient who needs CPR on a firm flat surface; first mention of CPR omits "call for help". | Fix 2, 3, 4 |
| B6 Misleading claims | PASS | No outcome, exam, income, rank or credential claim. "Clinician" appears only as "qualified clinician" in scope instructions, never as a review claim. No "clinician-reviewed" wording. Learning objectives 2 and 4 promise more than the text delivers (see C1). | Fix 7, 8 |
| B7 Medical/legal statements | FIX | No medicine doses; no drug names at all (closed list not even used); no ESI, START, ENA, AHA, SBAR, course or organization names (grep clean; the "Glasgow Coma Scale" and "AVPU" are generic scale names allowed by the book bible). Thresholds used (70 mg/dL, vital ranges, 25/min, CRT) are logged as VERIFIED. Items still NEEDS-HUMAN in verification-log (hazard list, 1.1 procedure, lancet steps, spine advice, consent law) cannot be cleared by me and keep the file DRAFT_FOR_REVIEW. Two "Giving medicines is outside many roles" lines appear where no medicine is mentioned. | Fix 2, 3, 4, 13 |
| B8 Metadata consistency | NOT IN SCOPE | Chapter holds no title page. Running title "Emergency Nursing Fundamentals" matches book.yaml. Subtitle promise "Rapid Assessment, Priorities and Procedures" is delivered by Part 1 (assessment, priorities, two procedures); "Illustrated" delivered by 4 of 4 planned Part 1 figures. | review again at /kdp-metadata |
| B9 Description | NOT IN SCOPE | not written yet | |
| B10 Keywords | NOT IN SCOPE | not written yet. "Pocket" must not appear (see Fix 1). | |
| B11 Category fit | NOT IN SCOPE | | |
| B12 AI disclosure | FIX | status.md lines say "HiggsField commercial-use terms: NOT yet recorded" (line 41) and "no HiggsField image has been generated yet" (line 71) while line 72 records the terms and ch01-fig3.svg now embeds an AI raster. No record of tool, date, prompt or job for Fig 3; Chapters table row 1 not updated. Disclosure plan itself (all text AI-generated, 25 of 25 figures AI-generated, no translation) is consistent with the live policy. | Fix 10 |
| B13 Images | FIX | Fig 1 to 4 (SVG vector, original drawings, no logos, no people except Fig 3). Fig 3: embedded JPEG 527 x 440 px shown about 3.75 in wide = about 140 ppi, soft for print; label text about 7 pt at print size; the "Radial pulse" leader line runs through its own label (seen on page 17); faceless adult male figure, no real person; anatomy plausible (carotid, sternal, radial, fingertip dots). Fig 1 to 4 label text is about 8 pt at print size (readable but small). Alt text is not present for any figure. All figures await clinician review. | Fix 10 |
| B14 Reviews/promotion | PASS | No review solicitation or promotion in the chapter. | none |
| B15 Rights statements | NOT IN SCOPE | front matter not written | |
| C1 Promise-delivery | FIX | Objective 2 "apply a five-level acuity idea to short scenarios": no worked scenario and only one triage-related question. Objective 4 "name abnormal findings": only one abnormal threshold (breathing above about 25) is given; no questions test history, vital signs, consent or documentation. | Fix 7, 8 |
| C2 Completeness | PASS | No placeholders, drafting notes or empty headings; every entry has the required labels; forward pointers (Entries 2.2, 3.4, 3.5, 4.1, 5.1, 5.4, 6.1) match the home-entry map and must be re-checked at assembly. Q8 model answer now exists. | none |
| C3 Accuracy | PASS (pending clearance) | Ledger P1-001 to P1-071: fixes recorded in the ledger are present in ch01.md (checked: "quickly" removed, "often not staffed", "two or more kinds", "consider moving", "stridor", GCS wording, glucose, oximeter). Exception: Fig 1 (ch01-fig2.svg) still says "move the patient up" (see Fix 5). | Fix 5 |
| C4 Clarity | FIX | CPR used before it is expanded; "defibrillator box", "cervical spine", "capacity" undefined for a first-year reader. | Fix 4, 14 |
| C5 Writing quality | PASS | No banned filler openers found; no typos found. | none |
| C6 Repetition | FIX | "Recheck after every action" appears in the Remember box, step 9, Fig 2 caption, the Priorities line, the Safety box, 1.5 Reassessment and Care Priorities; "Wait a short while ... before judging its effect" appears twice (1.3 Safety box and 1.5); the four triage questions appear four times (Remember box, paragraph, Figure 1, table); Care Priorities restates entries although outline section 9 says it must not (ledger P1-071 still open). KDP lists excessive repeated content as disappointing. | Fix 9 |
| C7 Formatting | FIX | previews/ch01.pdf is STALE (built 12:13, ch01.md saved 12:22): it still prints "gurgling", "full minute", "pocket kit", old figure numbering (triage labelled Figure 2 before Figure 1). Page 7 in that PDF holds one figure and about 40 percent blank space. Review Questions use typed bold numbers instead of native numbering (style guide asks native). Cannot confirm final layout. | Fix 10 |
| C8 Images/tables | FIX | see B13; tables sit inside margins and are legible. | Fix 10 |
| C9 Safety/trust | FIX | see B5, B7. | Fix 2, 3, 4 |
| C10 Value for price | PASS | Part 1 gives a fixed method, procedures with scope lines, figures and questions beyond free pages; no web-copy sign. | none |

## Specific checks you asked for
- Medicine doses: none. Drug names: none (closed list not needed in Part 1). Procedures carry Scope, Safety and Stop-and-call lines (1.1, 1.3); glucose check carries a scope-and-protocol line.
- ESI, START, ENA, AHA, course names, URLs, DOIs, citations, hyperlinks, brand and author names: none found by grep and by reading.
- Word "Pocket": ONE hit, "pulled on gloves from her pocket kit" (vignette). Fix 1.
- "Clinician-reviewed" or similar: none.
- Outcome or exam promises: none.
- Fictional case: labelled "Illustrative Case: Not a Real Patient"; no real patient, no institution; passes. About 271 words (target about 250).
- AI disclosure consistency: plan consistent with live KDP rule; status.md has stale lines and no Fig 3 record (B12).
- Promises vs subtitle: delivered at Part 1 level, except objectives 2 and 4.

## Required fixes (REVISE)
1. Banned word. Old: "pulled on gloves from her pocket kit" New: "pulled on gloves from her kit bag"
2. First look, neck injury. Old: "speak to them and, if a neck injury is not possible, tap or shake the shoulders gently as you ask whether they are all right." New: "speak to them loudly. If you can rule out a neck injury, tap the shoulders gently as you ask whether they are all right; if a neck injury is possible, do not shake the patient and keep the head and neck still."
3. Safety box movement. Old: "do not move an injured patient unless the scene is unsafe." New: "do not move an injured patient unless the scene is unsafe or you must move them to give life-saving care such as CPR, as your protocol directs."
4. CPR first use. Old: "If the patient is unresponsive and not breathing normally, start CPR as set out in Entry 3.4." New: "If the patient is unresponsive and not breathing normally, call for help and start cardiopulmonary resuscitation (CPR) as set out in Entry 3.4." (Procedure step 3 may then keep "begin CPR (Entry 3.4)".)
5. Figure 1 (images/ch01-fig2.svg) final box contradicts the corrected text. Old: "move the patient up if they are in a danger range" New: "consider moving the patient up if vital signs are in a danger range" (enlarge the green box to three lines so it fits).
6. Wording too close to the published triage tool. Old (Fig 1 and Remember box): "immediate life-saving action", "High-risk situation, new confusion, or severe pain or distress?", "How many different resources will the patient probably need?" New (suggested): "Will this patient die or be harmed within minutes without help?", "Could this patient worsen quickly, seem newly confused or drowsy, or be in severe pain?", "How many separate tests or treatments will this patient probably need?" Keep the same logic; reword the matching sentences in 1.2 and the table so the three places agree. Log in status.md that the text describes a generic principle.
7. Objective 4 over-promises. Old: "Describe how to gather a focused history and a set of vital signs, and name abnormal findings." New: "Describe how to gather a focused history and a set of vital signs, and recognize and report a worsening trend." (Do not add new thresholds unless a source is opened and logged.)
8. Objective 2 over-promises. Old: "Explain how triage assigns priority and apply a five-level acuity idea to short scenarios." New: "Explain how triage assigns priority using a generic five-level idea." Also replace trivial Review Question 4 with a question on vital signs, for example: "A patient's blood pressure reading is normal, but the skin is cool and pale and the breathing is fast. What is the best interpretation? A. The patient is safe because blood pressure is normal. B. Recheck in an hour. C. The patient may still be seriously ill, because blood pressure can stay normal for a time in shock. D. Only the temperature matters." (key: C) and update the key. Lines up with 1.4 text.
9. Repetition. (a) Delete in 1.5: "Wait a short while after an intervention before judging its effect." (b) Care Priorities, third paragraph. Old: "The first look tells you quickly whether the patient is responding normally. Then work through airway, breathing, circulation, disability and exposure, controlling severe bleeding first when it is obvious and your protocol directs it, and check again after every intervention." New: "Work through airway, breathing, circulation, disability and exposure in order, and let the patient's response decide what you do next." (c) Cut one of the four statements of the triage questions (keep figure and table; shorten the paragraph in 1.2 to a one-sentence pointer). (d) Remove "Recheck after every action you take." from the 1.3 Remember box and replace with a new, non-repeated memory aid.
10. Rebuild and inspect. Re-render previews/ch01.pdf from the current ch01.md, then check: Figure 1 on page 7 has no 40 percent gap, Fig 3 label "Radial pulse" is clear of its leader line, no stranded heading. Fig 3: regenerate the image at a size that gives about 300 ppi at 3.75 in (about 1,125 px wide) or confirm the live KDP print image requirement; raise label size to about 8 pt printed; add alt text for all four figures. Update status.md: record tool, date, prompt or job id and plan for Fig 3, fix line 41 ("NOT yet recorded") and line 71 ("no HiggsField image has been generated yet"), fill Chapters row 1 only after this review passes, and keep Fig 3 on the clinician-review list.
11. Review Questions answer pattern. Correct letters are B, C, B, C, B, C, C: A and D are never right. Reorder options so the key spreads across A to D; shorten distractors that are not plausible ("It always reads too high"; "Exposure only if the patient is conscious"); write Q5 options as "Alert / Voice / Pain / Unresponsive" instead of "A. A.". Update back/answer-keys-part1.md to match.
12. Remove the non-sequitur in 1.1. Old (1.1 Safety box): "Giving medicines is outside many roles; follow your scope and medical direction." New: delete the sentence (no medicine is mentioned in 1.1; keep the line in 1.3 only if a medicine or treatment is discussed there, otherwise delete there too).
13. Undefined terms. "bring the defibrillator box" -> "bring the automated external defibrillator"; "cervical spine" -> "neck (cervical spine)"; "patient who has capacity" -> "patient who has capacity, meaning the ability to understand the choice and its results".
14. Convert Review Questions to native numbered lists per style-guide.md (build fault, not a content fault).
15. Open items I cannot clear: ledger rows marked NEEDS-HUMAN (P1-001, P1-007, P1-008, P1-009, P1-026, P1-032, P1-043, P1-044, P1-048, P1-049, P1-056 to P1-063, P1-069, P1-071), clinician credential and clearance, KDP T&C, KDP print-requirement and image-resolution rules. The manuscript stays DRAFT_FOR_REVIEW and unpublishable.

## Customer-experience risks (likely one-star reasons)
1. "Stale proof": the preview PDF does not match the manuscript (old text, wrong figure order) -> rebuild before any approval (Fix 10).
2. "Says it teaches triage scenarios and abnormal findings but doesn't" -> reword objectives or add content (Fix 7, 8).
3. "Repeats itself": the same recheck line, the four triage questions and the Priorities block recur many times -> Fix 9.
4. "Unsafe or confusing instruction" on shaking a possibly neck-injured patient, and on moving a patient who needs CPR -> Fix 2, 3, 4.
5. "Quiz is too easy and predictable" (answers cluster on B and C, silly distractors, no coverage of history, vital signs or consent) -> Fix 8, 11.
6. "Blurry or cramped figure" (Fig 3 at about 140 ppi, small labels, line through a label) -> Fix 10.
7. "Jargon" (CPR, defibrillator, cervical spine, capacity) -> Fix 4, 13.
8. "Stray safety line about medicines in a scene-safety box" -> Fix 12.

## OVERALL VERDICT: REVISE
No BLOCK. Nothing here needs a plan change. Next action: apply Fixes 1 to 14 to ch01.md, the answer key, ch01-fig2.svg and ch01-fig3.svg (the writer, not this reviewer), rebuild the preview, update status.md, then re-run this review (round 2 of a maximum of 3). Even after PASS the file stays DRAFT_FOR_REVIEW until the open items in Fix 15 are cleared.

This is a good-faith review, not legal advice or a guarantee of Amazon's acceptance.

---

# ROUND 2 (2026-10-29)

Reviewer: independent compliance-reviewer pass. ch01.md was NOT edited. Files re-read: chapters/ch01.md (saved 12:27:51), back/answer-keys-part1.md, status.md, images/ch01-fig2.svg (Figure 1), ch01-fig3.svg (embedded JPEG extracted and measured), previews/ch01.pdf (built 12:28:14, after the last ch01.md save, so not stale; 25 pages; rendered with pdftoppm, contact sheet of all pages plus pages 7, 15, 18, 19 viewed).

## KDP pages opened this round (real opens through WebFetch)
| Page | Result |
|---|---|
| KDP Terms and Conditions (kdp.amazon.com/terms-and-conditions redirects to a kdp-eu.amazon.com/agreement page) | OPENED via the redirect. Title "Kindle Direct Publishing Terms and Conditions", last updated October 21, 2026 (as returned by the fetch tool's summary; the full text was not read by me). Points returned: 5.1.2 content must comply with Program Policies and Amazon may modify or remove metadata and cover art; 5.8 publisher warrants it holds the rights and its content infringes no one; 5.1.3/5.1.5 Amazon decides what it accepts and may remove books. The summary says the T&C do not mention AI content (the AI rule lives in the Content Guidelines, opened in round 1). Nothing in the chapter conflicts. B1 T&C check: now VERIFIED at summary level only. |
| Format Images in Your Book (G202169030) | OPENED. Print interior images: recommended minimum 300 DPI; below 200 DPI is classed as low resolution; insert at 100 percent and do not enlarge. |
| Print Options (G201834180) | OPENED. Trim sizes and page-count ranges only; no image or margin rules (those are on "Set Trim Size, Bleed, and Margins", opened by the owner session per status.md, not re-opened by me). |
Still not opened by me: the margin page, any medical-content page (none exists in the pages seen).

## Round 1 fixes: closed or open
| Fix | Status | Evidence |
|---|---|---|
| 1 pocket kit | CLOSED | vignette now "from her kit bag"; no "pocket" in the PDF text |
| 2 neck injury / shaking | CLOSED | "speak to them loudly. If you can rule out a neck injury, tap ... do not shake the patient and keep the head and neck still" |
| 3 movement exception | CLOSED | Safety box in 1.3 now allows moving to give life-saving care "as your protocol directs" |
| 4 CPR first use | CLOSED | "call for help and start cardiopulmonary resuscitation (CPR)"; step 3 "call for help and begin CPR" |
| 5 Figure 1 "move the patient up" | CLOSED | SVG now "consider moving the patient up if in a danger range"; text matches |
| 6 wording near the published triage tool | CLOSED | Figure 1, 1.2 paragraph and table now use the reworded questions consistently. status.md still lacks the one-line note "generic principle" asked for (minor, see R2-3) |
| 7 objective 4 | CLOSED | "recognize and report a worsening trend" |
| 8 objective 2 and Q4 | CLOSED | objective 2 reworded; Q4 now the shock/blood-pressure question; key updated to C |
| 9 repetition | PARTLY OPEN | (a) closed: the 1.5 "wait a short while" sentence is gone; (b) closed: Care Priorities rewritten as one paragraph without re-listing ABCDE; (d) closed: 1.3 Remember box is new wording; (c) OPEN: the 1.2 paragraph "The first question asks ..." still restates the three questions in full, so they appear in Figure 1, the table and the paragraph. "Check again" still appears in about six places (Remember box, step 9, Fig 2 caption, Priorities line, 1.5, Care Priorities); acceptable for a safety loop but trim one |
| 10 rebuild, Fig 3, status | PARTLY OPEN | Rebuilt PDF current. Fig 3 raster is now 880 x 734 px, placed at about 266 ppi (pdfimages): above KDP's 200 ppi low-resolution line, just under the 300 ppi recommendation; label text about 8 pt printed; "Radial pulse" leader no longer crosses its label (page 18 viewed). Figure record now present (see below). Layout blanks still present (R2-1). status.md lines 41 and 71 still stale (R2-3). Alt text: Fig 3 has title and desc; Figs 1, 2, 4 have none; irrelevant to a print PDF, needed only if an ebook is made |
| 11 answer pattern | CLOSED | key now B, D, A, C, D, A, C; Q5 options are Alert / Pain / Unresponsive / Voice; distractors plausible; answer-keys-part1.md matches all eight questions |
| 12 stray medicines line | CLOSED | removed from 1.1 and 1.3 |
| 13 undefined terms | CLOSED | "automated external defibrillator", "neck (cervical spine)", "capacity, meaning ..." all present |
| 14 native numbered lists | CLOSED | PDF shows numbered question list; step discs native |
| 15 open items | OPEN (cannot be cleared by a reviewer) | NEEDS-HUMAN ledger rows, clinician credential and clearance; file stays DRAFT_FOR_REVIEW |

## Figure 3 AI-image record
status.md line 74 (added after my first read of the file in this round) lists: tool HiggsField MCP, model gpt_image_2_5, date 2026-10-29, 3 variants at 0.25 credit, variant 1 chosen, the full prompt, labels added outside the image, disclose to KDP as AI-generated, clinician review pending. This closes the record requirement. One gap: no job or media ID is recorded (the earlier request said "prompt or job id"; the prompt suffices, an ID is advisable). Fig 3 content seen on page 18: faceless adult male, no logo, no text inside the raster, four markers plausible. The "Capillary refill / fingertip" label sits on the fingertip marker (dot touches the word "fingertip"); small, but move the label 6 to 8 px right.

## Layout inspection of previews/ch01.pdf (25 pages)
- Pages 6, 14 and 20 end with the lead-in line ("Figure 1 shows the sequence.", "Figure 2 shows the loop.", "Figure 4 shows the four parts.") and then about 40 percent blank space, because the figure does not fit and moves to the next page. Page 7 (Figure 1 only plus its caption) also ends at about 60 percent. Page 25 ends at 56 percent (acceptable, last page).
- All figure text is readable at print size (about 8 pt); no clipped text; no stranded headings seen; Part opener page has no fault; tables inside margins.
- Margin is cosmetic, but a reviewer would call four half-empty pages in 25 "padding or sloppy layout".

## Customer-experience risks still open
1. Four pages with about 40 percent white space and a lead-in line stranded at the page foot (R2-1).
2. Triage questions stated three times in one entry (R2-2).
3. status.md internal inconsistency could mislead the AI-disclosure answer (R2-3).

## Remaining required fixes
R2-1. Pagination. The figure lead-ins at the foot of pages 6, 14, 20 leave 40 percent blanks. Old: "Figure 1 shows the sequence." (before the figure) New: keep the sentence but build so the lead-in and figure stay together or the figure moves up: either shrink Figures 1, 2 and 4 about 15 percent (Figure 1 to roughly 55 percent of text height) or place each figure before the text paragraph that follows it. Rebuild and confirm no page ends above about 80 percent except the last page, the Part opener and a page before a forced break.
R2-2. Repetition, finishing Fix 9(c). Old (1.2): "The first question asks whether the patient will die or be harmed within minutes without help, for example from an obstructed airway or a stopped heart. If yes, that patient is at the top level and you act at once. The second question asks whether the patient could worsen quickly, seems newly confused or drowsy, or is in severe pain. Such patients are very unwell and should not wait, even though no action needs to happen in the next few seconds. If neither applies, the remaining patients are sorted by how many separate tests or treatments they will probably need, such as laboratory tests, imaging or procedures." New: "Three questions, asked in order, do the sorting. The first finds the patient who needs action at once, for example from an obstructed airway or a stopped heart. The second finds the patient who should not wait even though nothing must happen in the next few seconds. Everyone else is sorted by how many separate tests or treatments, such as laboratory tests, imaging or procedures, they will probably need." Keep the vital-signs sentence that follows.
R2-3. status.md bookkeeping. (a) Line 41, old: "HiggsField commercial-use terms: NOT yet recorded (to read live before any image is accepted)." New: "HiggsField terms read 2026-10-29 (see HIGGSFIELD TERMS OPENED entry); Part 1 Figure 3 is the first generated image (see FIGURE RECORD entry)." (b) Line 71, old: "no HiggsField image has been generated yet." New: "Part 1 Figure 3 has since been generated (see FIGURE RECORD entry)." (c) Add one line: "Triage text and Figure 1 describe a generic principle in original wording; no published tool is reproduced." (d) Add the HiggsField job or media ID for the chosen Fig 3 variant. (e) Fill the Chapters row 1 only after the final PASS.
R2-4. Fig 3 label. Move "Capillary refill / fingertip" right so its text does not touch the fingertip marker. Optional: add title and desc to Figures 1, 2 and 4 if an ebook is ever made.
R2-5. Image resolution. Fig 3 is about 266 ppi placed. KDP recommends 300; either accept (above the 200 ppi low-resolution line) and record that decision in status.md, or regenerate or upscale to about 1,000 px across the 3.3 in placement width... (3.3 in x 300 = about 990 px, so the current 880 px is only 11 percent short; accepting is reasonable).
R2-6. Open and not clearable by me (carry forward): NEEDS-HUMAN ledger rows, clinician credential and clearance (Orville A. Corey named, no credential, no clearance), clinician review of all four figures (placement of carotid and radial markers, fingertip), KDP margin page re-check at final page count. The manuscript stays DRAFT_FOR_REVIEW and unpublishable.

## ROUND 2 OVERALL VERDICT: REVISE (minor)
No BLOCK. Every safety, trademark and promise fix from round 1 is closed. What remains is layout (four half-empty pages), one repetition block, stale bookkeeping in status.md and the unclearable human-review items. PASS cannot be given while checklist items B7 and the clinician-clearance items remain NEEDS-HUMAN; after R2-1 to R2-3 are applied, a round 3 should be a quick check and can return PASS for compliance with the clinician hold noted.

This is a good-faith review, not legal advice or a guarantee of Amazon's acceptance.
