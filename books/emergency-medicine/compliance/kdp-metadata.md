# Compliance review: KDP-metadata.md (descriptions and keywords)

SCOPE: /home/user/book-studio/books/emergency-medicine/final/KDP-metadata.md, sections 8 to 19 (Descriptions One, Two, Three, final description in readable and HTML form, seven backend keywords and evidence). Checked against the manuscript in chapters/, front/, back/, images/, final/build-report.md. Date: 2026-10-29.

POLICY PAGES USED (opened live this session via WebFetch, 2026-10-29)
- KDP Description guidelines (G201189630): 4,000 characters including HTML tags; allowed tags br, p, b, em, i, u, h4-h6, ol, ul, li; no URLs, contact details, reviews or testimonials, price, availability, time-sensitive info, ads, or "keywords or book tag phrases".
- KDP Keywords (G201298500): up to seven keywords or short phrases; avoid words already in title, contributors or categories, generic words such as "book", subjective claims, plural or spacing variants, other authors, unauthorized brands, program names; no per-field character count is stated.
- KDP Title and subtitle (G201097560): title plus subtitle under 200 characters; must match the cover; no promotional or ranking words.
- Checklist: /home/user/book-studio/profiles/amazon-compliance-checklist.md (B6-B10, C1-C5).

## Mechanical checks (done by script)
- HTML character counts: 2415, 2397, 2558, 2663. All match the stated counts and are under 4,000.
- Tags used: p, b, h4, h5, ul, li only. All allowed. All tags closed and correctly nested in all four blocks.
- No URLs, emails, phones, prices, review requests, testimonials, competitor, brand, author or program names found in any description or keyword.
- Title plus subtitle: 142 characters (title 28 plus subtitle) per section 2; below 200. (status.md says 161 with a separator count; either is under 200.) Title/subtitle text matches book.yaml.

## Verdicts by check
| Check | Verdict | Evidence | Fix |
|---|---|---|---|
| B6 Misleading claims, "45 entries" | FIX | Manuscript has 33 numbered entries (5+5+5+6+6+6; confirmed by grep of "## [n.n]" headings and by the contents list in final/build-report.md). "45" appears in Description One ("Six Parts and 45 numbered entries"), Description Three (bullet heading and HTML h5 "Six Parts, 45 entries"), the final description ("Six Parts and 45 numbered entries"), and the section 21 checklist ("45 entries ... counted from the files"). | Replace every "45" with "33". Correct the section 21 row and the "counted from the files" claim. |
| C2 Completeness of the description (stranded headings) | FIX | In Descriptions One, Two, Three and the final description, the heading "Who it is for" (or "Who should read it" / "Who it serves") is followed immediately by another heading. The audience paragraph ("Students and new responders...", "Nursing, paramedic, EMT...") sits after the next section, so it reads as part of "Why the order matters" / "Clear limits" / "Written to be read and revisited". Same fault in readable and HTML versions (lines 76-82, 116-124, 157-165, 214-224 and the HTML on lines 91, 133, 174, 233). | In each HTML block, move the audience paragraph so that it directly follows the "Who it is for" h5, before the next h5. Do the same in the readable copies. No length change. |
| B6 Unsupported claim | FIX | "Most mistakes in the first minutes of an emergency come from skipping a step, not from missing a rare fact." (One and final description). No source is logged; it is a factual claim about error causes. | Delete the sentence, or replace it with a non-factual statement such as "Each entry gives the reason behind its steps, so the sequence is easier to remember." Do not cite a source unless it is logged in verification-log.md. |
| B6 Absolute claims vs manuscript | FIX | "Every procedure in this guide says so, tells you when to stop..." (Two) and "Every procedure states its scope, tells you when to stop" (final). The manuscript has Scope Note boxes in 5 of 6 Parts; front/how-to-use.md makes the same claim, but not every procedure was checked to carry all three. Also "why airway comes first" / "airway comes before circulation": Entry 4.2 says a tourniquet may be applied first for massive limb bleeding. | Say "Procedures state the scope of practice and tell you when to call for more help" only if verified for each procedure; otherwise use "Scope Note boxes mark the limits of your role". Change "why airway comes first" to "why the primary survey runs in a fixed order". |
| C1 Promise-delivery, dangerous rhythms | FIX (low) | Entry 3.3 is "Recognizing Dangerous Rhythms", while the descriptions say the book leaves out "reading heart tracings". A reader may expect rhythm-strip teaching or feel misled. | Add a clause: "recognizing dangerous rhythms from the patient's signs and the AED's prompts, not from reading heart tracings", after confirming against Entry 3.3. |
| B6 Counts and page claims | PASS | 25 figures (25 SVG files in images/), 68 glossary terms (68 bold entries), 179 pages (build-report.md), eight review questions in every Part (verified in all six chapters), answers in Appendix A, five acuity levels (Entry 1.2), "about 180 pages" acceptable, no medicine doses (front/how-to-use.md, copyright), 5 x 8 in, color (book.yaml). | Re-count if the book changes. |
| B7 Medical statements | PASS with condition | Descriptions state education-only, no doses, follow local protocol, not a substitute for training. No cure or outcome promises. No claim of clinician review. | The clinician is named but NOT cleared (status.md). Do not add "clinician-reviewed" wording. Re-run this review when clearance is recorded. |
| B8 Title/subtitle/metadata consistency | PASS (cover UNVERIFIED) | Title and subtitle match book.yaml. No cover exists yet, so the match to the cover is UNVERIFIED. | Re-check against the final cover and title page before upload. |
| B9 Description compliance | REVISE (see above) | Length, tags, prohibited content PASS. Defects are the stranded headings, the "45" error and the unsupported sentence. The "Topics covered" paragraph in Description One is a long run of topic nouns and borders on "keywords or book tag phrases". | Fix the items above. Consider shortening "Topics covered" or recasting it as a sentence; the final description already avoids it. |
| B10 Keywords: count and format | PASS | Exactly seven phrases, no quotation marks, no HTML, no names or brands, no price/time words, no program names. Longest is 43 characters. | Check the KDP field counter. |
| B10 Keywords: generic and title words | FIX | #6 "study book for first responders": "book" is the generic word the KDP page names; "first responders" does not occur in the manuscript (0 hits), and the audience is students (EMT/paramedic/nursing). #7 "emergency department clinical rotation": "emergency" is the first word of the title; "rotation" does not occur in the manuscript (it uses "placement"); the book is not about the emergency department as a topic; the evidence row itself says Low confidence and "no evidence". #1 repeats "survey" twice within one field. | Replace #6 and #7 (see Replacement keywords). Change #1 to "primary and secondary survey" (the word "survey" once). |
| B10 Keywords: duplicates across fields | FIX (low) | Words "and" and "survey" recur; the term "children" and "CPR" are only in one field each. Acceptable except #1. #4 "bleeding control and tourniquet use" and #3 are good. Rejection reason for ABCDE ("appears once in the manuscript") is wrong: Entry 1.3 says ABCDE "is the spine of the whole book". | Correct the evidence table. Consider "ABCDE assessment steps" as a better candidate than #7 (verify it is not a protected term; it is a generic mnemonic). |
| B10 Keywords: evidence integrity | FIX (low) | Section 19 counts do not match the files: "primary survey appears 42 times" (46 found), "tourniquet appears 29 times" (33 found). Section 17 is titled "26 phrases" but lists 27. Evidence for #3, #4, #5, #6, #7 is "none seen". | Correct the numbers and the title. State that all keywords are untested hypotheses. The file already says so in sections 18 and 22, which is honest. |
| B11 Category fit | UNVERIFIED | Section 20 says the category names were not checked against KDP's list; categories not chosen. Keywords cannot be checked against category words until the owner picks them. | Owner picks up to three categories in KDP; then remove any keyword that repeats a category word. |
| B12 AI disclosure | PASS (outside scope) | status.md lists text and 25 of 25 figures as AI-generated. The metadata file section 3 says so. Descriptions do not hide it. | None. |
| B14 Reviews and promotion | PASS | No review requests or incentive wording. | None. |
| Research honesty | PASS | Section 1 and 22 state no browser was used for this stage, 503 errors, and the thin evidence. | None. |

## Replacement keywords (suggestions to be tested by the owner in the Amazon search box; not guaranteed)
- Replace #6 with a phrase that uses words the book contains and none of the title words, for example "scene safety and patient assessment" (Entries 1.1 and 1.3) or "ABCDE assessment steps".
- Replace #7 with a phrase that matches how the book describes its reader, for example "clinical skills lab preparation" or "first emergency placement preparation". Avoid "emergency" (title) and "nursing", "EMT", "paramedic", "students", "guide", "illustrated", "compact" (subtitle).
- Keep #2 to #5. Change #1 to "primary and secondary survey".
- Do not use "pocket", "NCLEX", "EMT exam", program or course names (the file already rejects these correctly).

## Customer-experience risks (likely one-star reasons)
1. Listing says 45 entries; the reader finds 33 -> change to 33 everywhere.
2. Blank "Who it is for" heading in the live listing looks careless and hides who the book is for -> reorder the audience paragraph.
3. Reader buys expecting rhythm-strip teaching because of "dangerous rhythms" -> add the clarification above.
4. "Every procedure states its scope" read literally: a reviewer finds one that does not -> use the softer wording.
5. "Compact" and "about 180 pages" with price in the 5 x 8 color format: no promise is made about price; fine. Nothing further.
6. Students who expect exam prep from words like "review questions" -> the description already says it is not a substitute for a course; keep "not an exam-prep title" out of keywords (done).
7. Unsupported statement on where mistakes come from may be challenged by clinicians -> delete.

## OVERALL VERDICT: REVISE
No BLOCK. Nothing risks account action. The descriptions are compliant in length, tags and prohibited content, but the false entry count (33 not 45), the stranded headings, the unsupported claim and two weak keywords (#6 generic "book" and non-manuscript phrase; #7 title word and non-manuscript phrase) must be fixed. The category check is UNVERIFIED and the clinician clearance is still open, so PASS is not allowed yet.

## NEXT ACTION
1. Apply fixes 1 to 7 above to final/KDP-metadata.md (and regenerate final/KDP-metadata.docx).
2. Recount characters of every HTML block after editing (limit 4,000 including tags).
3. Owner tests the seven keywords in the Amazon search box and picks categories; then a second review round.
4. Re-check title, subtitle and author against the cover when it exists, and re-review after clinician clearance.

This is a good-faith review, not legal advice or a guarantee of Amazon's acceptance.

## Re-review note (2026-10-29)
Owner-facing fixes applied after this review: entry count corrected to 33; stranded headings reordered; unsupported and absolute wording removed; keywords 1, 6 and 7 replaced; evidence counts corrected; Topics paragraph recast. Items 10 and 11 remain open. A second review round is still advised after the owner chooses categories.
