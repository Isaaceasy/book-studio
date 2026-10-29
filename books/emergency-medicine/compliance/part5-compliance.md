# Compliance and customer-experience review: Part 5 (chapters/ch05.md), round 1

Scope: chapters/ch05.md (text, captions, callouts, Review Questions), images/ch05-fig19.svg to ch05-fig22.svg as rendered in previews/ch05.pdf, back/answer-keys-part5.md, verification/part5-ledger.md. ch05.md was NOT edited.

## Research Proof (what was actually done)
Date: 2026-10-29. Reviewer: independent compliance-reviewer pass (new session; I did not open any KDP page in the Part 1 or Part 2 reviews, so I opened them myself). No chapter, figure, answer key or ledger was edited.

Files read in full: CLAUDE.md (system context), profiles/amazon-compliance-checklist.md, outline.md (sections 1, 4, 7, 9, 11, 11b, 12 and the Part 3 to 5 figure rows), style-guide.md, status.md, compliance/part1-compliance.md, compliance/part2-compliance.md, .claude/skills/amazon-compliance/SKILL.md, chapters/ch03.md, ch04.md, ch05.md, back/answer-keys-part3.md, part4.md, part5.md, verification/part3-ledger.md, part4-ledger.md, part5-ledger.md (every CORRECTED, QUALIFIED and non-"None" row compared with the chapter text; NEEDS-HUMAN rows counted, not re-judged), chapters/ch06.md (cross-reference targets only), PROGRESS.md.

Checks run: grep of each chapter for doses, drug names, brand and course names (ESI, START, ENA, AHA, ACLS, BLS, ATLS, TCCC, Red Cross), URLs, "pocket", exam and outcome words, double commas, em dashes and banned filler; SVG inspection (embedded JPEG yes or no, title and desc, font sizes); pdfimages for placed resolution (all raster figures 310 ppi or more); previews/ch03.pdf (24 pages), ch04.pdf (26) and ch05.pdf (23) rendered with pdftoppm: contact sheet of every page, a page-fill measurement per page, and 130 dpi views of the figure pages. The PDFs are newer than the chapter files (ch03 md 13:17:15, pdf 13:18:09; ch04 md 13:17:57, pdf 13:18:14; ch05 md 13:16:18, pdf 13:16:23), so they are not stale.

Live KDP pages opened with WebFetch on 2026-10-29 (content returned):
| Page | Takeaway |
|---|---|
| Content Guidelines (kdp.amazon.com/en_US/help/topic/G200672390) | AI-generated text, images and translations must be disclosed; AI-generated stays AI-generated after substantial edits; AI-assisted (editing, brainstorming, error checks only) need not be disclosed. Misleading descriptions and content that typically disappoints readers are not allowed. No medical or health section. No update date shown. |
| Guide to Kindle Content Quality (G200952510) | Typos, missing content, repeated content, forced formatting, blurry images, illegible text in images and metadata mismatch are listed disappointments; content that is too short or excessively reused is also listed. No medical statement. No update date shown. |
| Format Images in Your Book (G202169030) | Print images: 300 DPI minimum as worded; under 200 DPI is low resolution; insert at 100 percent, do not enlarge; flatten to one layer. |
| Web search for a KDP medical-content page | None found. Closest rule seen only as a search snippet (A+ Content guidelines, G4WB7VPPEAREHAAD, not opened): cure, treat or prevent claims for drugs, devices and health products must be removed and other health claims need substantiation. Medical safety is therefore judged against the book's own outline rules (sections 1 and 11b), not a KDP rule. |

NOT opened by me this session: KDP Terms and Conditions, Metadata Guidelines, margin and trim page, review and promotion rules. B8 to B11 and B15 are not testable at chapter level (no title page, description or keywords yet) and are marked NOT IN SCOPE; B1 rests on the Content Guidelines plus the Part 1 reviewer's summary-level T&C read.

## Ledger application check (every CORRECTED and QUALIFIED row of part5-ledger.md)
Applied and confirmed in ch05.md by quoting the new wording: P5-007, 018 (insulin removed; grep "insulin" none), 028, 029 (scope sentence at the end of 5.4 First Priorities), 043 (caption "two signs of the stroke screen"), 046, 047, 049, 063, 065 (both "longer than 5 minutes"), 067, 069, 072, 076, 084, 088, 098, 099, 100, 108, 113, 116, 119, 122, 127, 130, 135 to 143 (the writer rewrote the questions; chapter key D-first pattern: B, D, A, C, B, D, A; key file matches all seven).
NOT applied or only partly applied:
- P5-078 (Figure 22): "High or low temperature" is still missing from the warning-sign box although 5.4 Recognition lists it first; and the figure's box "Oxygen as protocol directs, keep warm" carries no scope wording. Open: Fix 3.
- P5-012 (Figure 19 last box): the SVG now reads "Call for help early, keep rechecking, do not wait for the cause": applied.
- P5-080 (stray sentence "A patient who has had an infection and then becomes more unwell...", ledger said no change): in the preview it sits alone after the Red Flags box and reads as an orphan line. Open: Fix 1.
- P5-081 (handover wording): superseded, the sentence no longer exists.
- P5-133 (length): chapter is 5,444 words including markup, above the 5,000 floor, nothing to do.
- Ledger defect: P5-131 says a case-sensitive grep for "FAST" found no match, but ch05.md contains "FAST" (5.2 Recognition and the Remember box). Correct the row; FAST is a generic stroke mnemonic and the ledger source is the CDC BE-FAST page.
39 rows are NEEDS-HUMAN (class D drugs and class S safety) and sit with the clinician. The manuscript stays DRAFT_FOR_REVIEW.

## Check table
| Check | Verdict | Evidence | Fix |
|---|---|---|---|
| B1 Illegal/infringing | PASS (T&C not re-read) | No brands, no course names, no quotations. "FAST" is a generic public mnemonic; "Poison Help" is the official service name next to the allowed phone number 1-800-222-1222. Fig 21 faces are AI-generated fictional people, no logo. | none |
| B2 Originality | PASS | Fresh prose. | none |
| B3 Duplicate content | PASS | Bridges used ("Entry 1.3 gave you", "Entry 3.5 explained", "Entry 1.5 set out"). | none |
| B4 Thin content | PASS | 5,444 words including markup, 6 entries, 4 figures, case, 8 questions. | none |
| B5 Harmful/dangerous | FIX | Glucose procedure step 6 "repeat the treatment if it is still low" and the explanation "an unnecessary second portion of sugar" read as a repeat-dose rule (frequency of a closed-list item, oral glucose) although the owner rule is no medicine dose, frequency, duration or route; it is hedged "as your protocol directs" and has no amount. Needs an owner or clinician decision. 5.6 "keep them lying down with the legs raised if they are faint or pale" sits right after "position of greatest comfort" and is unsourced for lay readers (NEEDS-HUMAN). All other safety wording is sound: glucose procedure (swallow check, nothing by mouth if drowsy, stay with patient, recovery position, stop line), seizure (no restraint, nothing in the mouth), poisoning ("Do not make the patient vomit"), aspirin withheld in suspected stroke. | Fix 4, 8 |
| B6 Misleading claims | FIX (minor) | Objective 2 says "validated stroke screen" while the text teaches FAST; ledger P5-002 verified validation only for the Cincinnati scale. No outcome or exam claim; no "clinician-reviewed". | Fix 5 |
| B7 Medical statements | FIX / UNVERIFIED | No medicine dose, frequency, duration, route or oxygen flow rate (grep: only "mg/dL" as a glucose unit). Drug names used: oxygen (5.1 physiology, 5.4 treatment), aspirin (5.2 text, Q4), naloxone (5.5, Q7), and glucose as "fast-acting sugar" (the product is never named; allowed by the closed list). Scope sentence present verbatim after: 5.1 Safety box (glucose and sugar), 5.2 First Priorities (aspirin), 5.4 First Priorities (oxygen), 5.5 Opioid Overdose (naloxone), 5.6 First Priorities (painkillers). Missing: answer-key Q4 (aspirin) has no scope sentence (Q7 key has one in substance); 5.2 "a medicine that affects clotting" is a class mention, acceptable. The 5.5 phone numbers (1-800-222-1222) are allowed; 988 is not used here. 39 NEEDS-HUMAN rows remain. | Fix 7 |
| B8 Metadata consistency | NOT IN SCOPE | | at /kdp-metadata |
| B9 Description | NOT IN SCOPE | Must not list carbon monoxide as excluded: 5.5 now covers it in about four sentences (outline section 7 allowed one sentence); log this as an accepted deviation. Must state: no medicine doses, recognition and first priorities only. | Fix 9 |
| B10 Keywords | NOT IN SCOPE | Do not use "FAST", "Narcan" or "BE-FAST" as keywords. | |
| B11 Category fit | NOT IN SCOPE | | |
| B12 AI disclosure | PASS | status.md line 78 records Figs 20 and 21 (HiggsField gpt_image_2_5, job ids with alternatives) and Figs 19 and 22 as AI-written SVG; SVG check: embedded JPEG in fig20 and fig21 only. Placed resolution 334 and 311 ppi. Clinician review pending (region colors in Fig 20 schematic). | none |
| B13 Images | FIX | Fig 19 and 22 flow text is about 5 to 6 pt printed (12 to 12.5 units in a 420-unit box scaled to fit), legible but small, and Fig 22 lacks the temperature item and the scope wording on its oxygen box. Fig 20 is a plausible side view with three shaded regions and cerebellum and brainstem; the caption says "each supplied mainly by a different main artery" but no artery is named or colored per region. Fig 21: face droop and one arm lower drawn clearly, arrows shown, fictional faces. No graphic content. | Fix 3, 6 |
| B14 Reviews/promotion | PASS | none | none |
| B15 Rights statements | NOT IN SCOPE | | |
| C1 Promise-delivery | FIX (minor) | Objectives 1 to 6 map to 5.1 to 5.6; objective 2 wording (Fix 5). | Fix 5 |
| C2 Completeness | PASS | Answer key with Q8 model answer exists; cross-references resolve (Entries 1.3, 1.4, 1.5, 2.2, 2.3, 3.4, 3.5, 4.3, 4.6, 5.x, 6.1, 6.4, 6.5, 6.6). | none |
| C3 Accuracy | UNVERIFIED (pending clinician) | Ledger applied (above). | Fix 4, 8 |
| C4 Clarity | FIX (minor) | Orphan sentence after the 5.4 Red Flags box. | Fix 1 |
| C5 Writing quality | PASS | No typos, doubled words or banned openers found. | none |
| C6 Repetition | FIX (minor) | FAST is explained twice in 5.2 (Recognition and Remember box); the scope sentence appears seven times (required by rule, so leave); "call emergency services at once" ends every Red Flags box (safety repeat). | Fix 2 |
| C7 Formatting | FIX | Page fill (90 percent = full): p13 41 (Recognition ends the page; the Figure 22 lead-in and figure moved to p14), p15 78, p17 80, p23 59 (last page). p2, p5, p8 and p12 end near full. No stranded procedure title; glucose procedure starts p4 and finishes p5 intact. Tables none. | Fix 6 |
| C8 Images/tables | FIX | See B13. | Fix 3, 6 |
| C9 Safety/trust | FIX | See B5. | Fix 4, 8 |
| C10 Value for price | PASS | Method for the undifferentiated patient, six problem entries, four figures, case and questions beyond free pages. | none |

## Required fixes (REVISE), old text -> new text
1. Orphan sentence (5.4). Old: a stand-alone paragraph "A patient who has had an infection and then becomes more unwell rather than better should be assessed again." between the Red Flags box and "Why Screening Uses Several Signs." New: delete it and append to the end of the Recognition paragraph, after "your service will teach the one it uses.": "A patient who has had an infection and then becomes more unwell rather than better should be assessed again."
2. FAST duplicate (5.2). Old (Recognition): "One widely taught version is FAST, for Face, Arm, Speech and Time." New: "The common version, FAST, is set out in the Remember box." Keep the Remember box as the single definition.
3. Figure 22 (images/ch05-fig22.svg). Add the item "High or low temperature" to the warning-sign box (P5-078); change the box Old "Oxygen as protocol directs, keep warm" New "Oxygen only if scope and protocol allow, keep warm"; raise the flow text to at least 7 pt printed (widen the boxes, shorten labels). Same size rise for Figure 19.
4. Glucose procedure (B5; owner or clinician decision, since the outline says no medicine frequency). Old (step 6): "Recheck the blood glucose after about 15 minutes, and repeat the treatment if it is still low, as your protocol directs." New: "Recheck the blood glucose after about 15 minutes, and if it is still low, follow your protocol and call for help." Old (explanation): "Rechecking the reading tells you whether the treatment worked and avoids both a missed relapse and an unnecessary second portion of sugar." New: "Rechecking the reading tells you whether the treatment worked and whether the problem has returned."
5. Objective 2. Old: "Recognize stroke with a validated stroke screen and state why time matters." New: "Recognize stroke with a standard stroke screen and state why time matters."
6. Layout and Figure 20 caption. (a) Rebuild previews/ch05.pdf so page 13 is not 41 percent full: move the Red Flags box and "Why Screening Uses Several Signs" above Figure 22 or shrink Figure 22 to about 65 percent height, so the figure follows its lead-in; confirm no page ends below about 80 percent except the opener and last page. (b) Caption. Old: "A simplified side view of the brain showing the front, middle and rear regions, each supplied mainly by a different main artery." New: "A simplified side view of the brain with the front, middle and rear regions shaded; each region is supplied mainly by a different main artery."
7. Answer key Q4 scope sentence (back/answer-keys-part5.md). Old: "4. C. Some strokes are bleeds, and aspirin could make bleeding worse." New: "4. C. Some strokes are bleeds, and aspirin could make bleeding worse. Giving medicines is outside many roles; follow your scope and medical direction."
8. Legs raised (5.6; NEEDS-HUMAN). Old: "Let the patient find the position of greatest comfort, and keep them lying down with the legs raised if they are faint or pale." New: "Let the patient find the position of greatest comfort; if they are faint or pale, lay them down and, if your protocol allows, raise the legs." Delete the legs clause if the clinician does not clear it.
9. Records. status.md: (a) log carbon monoxide in 5.5 as an accepted deviation from outline section 7 (one sentence allowed; about four used) and that the description must not list carbon monoxide as an exclusion; (b) correct ledger row P5-131 (FAST is present); (c) note the quiz answer-length tell (correct option longest in Q2, Q4, Q6, Q7: shorten the long correct options or lengthen the distractors, for example Q7 A New "Make the scene safe, call emergency services and support breathing; use naloxone only if your role allows." and B New "Make the patient vomit to clear the drug."); (d) fill Chapters row 5 only after PASS.

## Specific checks you asked for
- Medicine doses or flow rates: none. Oxygen: "as your protocol directs".
- Drug names only from the closed list with the scope sentence: PASS in text (glucose, aspirin, naloxone, oxygen); only the key to Q4 lacks it (Fix 7). Epinephrine and albuterol are not named in Part 5. No insulin, glucagon, painkiller names (class "painkillers" in 5.6 is a "do not give").
- ESI, START, ENA, AHA, CDC, course names, URLs, citations, brands, "pocket", "clinician-reviewed", outcome and exam promises: none. Phone number 1-800-222-1222 present and allowed.
- Illustrative case: labelled; Grace, Walter, daughter unnamed; "agency" and "home-care placement" are generic; no real institution. The case teaches the right order (survey, glucose, call, swallow check, protocol, recheck, handover).
- Safety wording of procedures: glucose help (Fix 4), seizure (PASS), recovery position bridge (PASS), naloxone (PASS: stay with patient because it can wear off).
- Graphic content: none.
- Figure and caption match: Fig 19 PASS, Fig 20 near (Fix 6b), Fig 21 PASS, Fig 22 FIX. Numbering 19 to 22 in order of appearance.
- AI disclosure consistent with status.md: yes.
- Cross-Part repetition: modest; 5.1 recovery-position and 5.2 glucose lines are one-sentence bridges.

## Customer-experience risks (likely one-star reasons)
1. "Half-blank page 13" -> Fix 6.
2. "Stray sentence after a box" -> Fix 1.
3. "Flow chart text too small; sepsis chart misses the temperature the text lists" -> Fix 3.
4. "Quiz: the longest answer is always right" -> Fix 9c.
5. "Repeat-dose instruction for sugar in a book that says no doses" -> Fix 4.
6. "Description says CO is excluded but the book covers it" -> Fix 9a.
7. "Says 'validated' but teaches FAST" -> Fix 5.
8. "FAST explained twice" -> Fix 2.

## OVERALL VERDICT: REVISE
No BLOCK, no plan change. PASS is not possible today: open FIX items 1 to 9, 39 NEEDS-HUMAN ledger rows, and clinician review of four figures. Stays DRAFT_FOR_REVIEW.

This is a good-faith review, not legal advice or a guarantee of Amazon's acceptance.
