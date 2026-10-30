# Second-round compliance review (2026-10-30)

Scope A: final/KDP-metadata.md (descriptions, final description, 7 keywords). Scope B: front/copyright.md (Disclaimer), chapters/ch06.md Entry 6.2, scan of all chapters, front, back.

POLICY PAGES USED (opened live 2026-10-30)
- Description G201189630: 4,000 characters incl. tags; h1-h3 unsupported; no URLs, contact details, reviews/quotes/testimonials, price/ordering, time-sensitive details, "any keywords or book tags phrases".
- Keywords G201298500: up to seven keywords/short phrases; no field limit stated; avoid title/contributor/category words, "book", subjective praise, plural/spacing variants, unrelated author names, unauthorized brands, quotation marks, HTML, program names.
- Title G201097560: title + subtitle fewer than 200 characters; must match the cover.
- Content Guidelines G200672390: no content typically disappointing to customers; no descriptive content that misleads or misrepresents the book. (Page has no medical-specific rules.)
- AI content (search result from kdp.amazon.com, 2026-10-30): AI-generated text/images must be disclosed to KDP at publishing; AI-assisted need not be. Not opened as a full page; treat as summary.

## A. KDP-metadata.md: REVISE

Mechanical recount (script): HTML blocks = 2209, 2423, 2575, 2549 characters incl. tags. All match the stated counts, all under 4,000. Tags used: p, b, h4, h5, ul, li only, all allowed, all closed. No URLs, prices, reviews, brand or author names. Seven keywords, each under 50 characters, no quotation marks.

Recount of claims from the files: 33 entries (5,5,5,6,6,6) PASS; 25 figures (25 numbered SVGs; 15 image-tool + 10 vector, matches copyright) PASS; 68 glossary terms PASS; 179 pages (build-report.md) PASS; eight review questions per Part and 8 answers per answer key PASS; objectives, illustrative case, Care Priorities in all 6 Parts PASS; 14 procedure boxes all carry "Scope:" and a stop line (17 stop lines) PASS; "primary survey" 42 and "tourniquet" 31 in chapters/ PASS (46/33 over the whole corpus, which is what round 1 saw); "first responder" 0 and "rotation" 0 hits, confirming the old keywords were rightly removed.

Round-1 findings status
| Round-1 finding | Status | Evidence |
|---|---|---|
| 45 entries wrong | FIXED | Now 33 everywhere (sections 8, 12, 15, HTML) |
| Stranded "Who it is for" headings | FIXED | Audience paragraph now directly follows its h5 in all four readable and HTML versions |
| Unsupported "most mistakes..." sentence | FIXED | Not present |
| "Every procedure states its scope", "why airway comes first" | FIXED | Replaced by "Scope Note boxes mark the limits"; verified true for all 14 procedures anyway |
| "Dangerous rhythms" vs "reading heart tracings" | PARTLY FIXED | See A3 |
| Counts/pages | PASS | As above |
| Medical statements / no clinician-reviewed wording | PASS | None in metadata or manuscript |
| Keywords #6 "book"/"first responders", #7 "emergency"/"rotation", #1 double "survey" | FIXED | Now #1 "primary and secondary survey", #6 "scene safety and vital signs", #7 "handover and documentation skills". No title/subtitle words, no generic word |
| ABCDE rejection reason wrong | NOT FIXED | See A2 |
| Evidence counts 42/31, phrase count | FIXED | 29 phrases listed and titled 29 |
| Category fit (B11) | OPEN, UNVERIFIED | Categories not chosen, so keyword/category word overlap cannot be checked |
| Cover match (B8) | OPEN, UNVERIFIED | No cover exists |
| Description "Topics covered" tag-phrase risk | FIXED in final | Final description has no topic-noun run. Descriptions Two and Three still have long topic lists (Three: "altered mental status, stroke, seizures, sepsis, poisoning and abdominal pain"); upload only the section 16 text |

New and remaining findings
A1. FIX. Section 2 says title + subtitle = "142 characters". Actual: title 30 + subtitle 129 = 159 (161 with a colon and space as status.md counted). Under 200, so no policy risk, but the stated number is false in an audit document. Fix: change to "159 characters (161 with the ': ' separator)".
A2. FIX (low). Section 17 row 15 (ABCDE) still says the string "appears only once in the text". It appears twice, and Entry 1.3 calls ABCDE "the spine of the whole book". Fix: rewrite the reason as "rejected because it is an abbreviation, not a likely search phrase, and no demand evidence was seen".
A3. FIX (low). Descriptions list "dangerous rhythms" and exclude "detailed heart tracing interpretation"; front/how-to-use.md says "reading heart tracings" (no "detailed") and copyright says "electrocardiogram interpretation", while Entry 3.3 teaches four monitor patterns (Figure 10). A reader could call this inconsistent. Fix: in the final description say "...leaves out such as medicine amounts, intravenous access, full heart tracing interpretation and advanced airway skills", and make how-to-use and copyright use the same words ("full heart tracing (ECG) interpretation; Entry 3.3 teaches only four basic patterns").
A4. FIX (low). Section 21 row "Independent compliance review" says "items 1 to 9 and 13 fixed" and "item 10 categories, 11 cover, 12 clinician". Round 1 had no numbered list, so this numbering cannot be traced. Fix: replace with named items (as in the table above).
A5. UNVERIFIED (owner). Categories and cover. Section 20 states categories are unverified. Before upload: pick up to three categories in KDP, remove any keyword that repeats a category word, check title, subtitle and author "Mark Gerald Simon" against the cover and title page.
A6. NOTE. Keyword evidence is Low/Medium for all seven and no Amazon results page was opened. Honestly disclosed (sections 18, 22); not a violation. Do not describe them as proven.
A7. NOTE. Readable word counts (363, 380, 363, 402) are for headings plus text and differ slightly from a count of the HTML text (358, 380, 363, 402). Immaterial.

Checks (scope A)
| Check | Verdict | Evidence |
|---|---|---|
| B6 Misleading claims | PASS | All counts and scope statements verified |
| B7 Medical statements | PASS | Education-only, no doses, not a substitute for training, no cure or outcome claims, no clinician-review claim |
| B8 Metadata consistency | UNVERIFIED | Title/subtitle match book.yaml; cover missing; A1 count error |
| B9 Description | PASS (final, section 16) | 2549 characters, allowed tags, no prohibited content |
| B10 Keywords | PASS | 7 phrases, no brands, no generic words, no title/subtitle words |
| B11 Categories | UNVERIFIED | Not chosen |
| B12 AI disclosure | PASS | Metadata and copyright disclose text and images as AI-generated; status.md lists figures |
| B14 Reviews/promotion | PASS | None |

VERDICT A: REVISE. Fix A1 to A4 (text only), then owner closes A5. No BLOCK.

## B. Manuscript: REVISE (no BLOCK)

Scan results (all of chapters/, front/, back/)
- Placeholders (TODO, TBD, lorem, insert, ???): none.
- Hyperlinks/URLs/emails/DOIs: none; only local image references.
- Citations, footnotes, reference lists, "according to" sources: none. ("According to Entry 6.2" is a cross-reference, allowed.)
- Brand and trademark names: none in chapters, front or back. "Glasgow" is the Glasgow Coma Scale (an eponym, plain text, acceptable; flag per CLAUDE.md rule 7). Medicines named only generically (epinephrine, naloxone). No program names (no Stop the Bleed, no AHA/AAP names).
- Income, guarantee, bestseller, award, price claims: none.
- "Clinician-reviewed", "medically reviewed", "endorsed", "approved by": none. Copyright page says "not affiliated with, endorsed by or sponsored by" any body, and "This book has not been validated for any individual state protocol." Clinician name does not appear.
- Medicine amounts: none (only mg/dL glucose thresholds, which are measurements, not doses).

Copyright page (Disclaimer paragraph)
| Check | Verdict | Evidence |
|---|---|---|
| B7 Medical/safety statements | PASS | Follow current professional guidance over this book; no clinician-patient relationship; do not delay calling emergency services |
| B6 No false credential/review claim | PASS | No review or clearance claim |
| B15 Rights statements | FIX | See B1 |
| B12 AI disclosure | PASS | Text, questions, captions, glossary, figures disclosed; 15 + 10 figure split matches the figure records |

Entry 6.2
| Check | Verdict | Evidence |
|---|---|---|
| Witnessed-collapse sentence | FIX (low) | CPR step 2 now has three cases and the last sentence ("If you saw the child collapse suddenly, call and fetch an AED first, then begin CPR") reads as if it conflicts with the sentence before it for an alone rescuer with no phone. It also has no "alone" qualifier |
| Adult pads must not touch | FIX (low) | Step 7 says "place the pads so that they do not touch each other" but gives no instruction for when they would (small chest). A hostile reader will ask "then where?" Entry 3.4 and the AED paragraph in 3.4 (child under 8, adult pads) do not repeat the rule |
| Consistency with Q3 and answer key | PASS | Q3 stem says "found" (unwitnessed) and "no phone"; answer D (2 minutes of CPR, then call) still correct |
| Numbers (2 in, 1.5 in, 100-120, 30:2, 15:2, 10 s) | PASS | Consistent with the owner's AHA text recorded in status.md; not re-verified against the PDF in this review |
| Stray sentence | FIX (low) | After the CPR box: "Early breaths and oxygen matter more. Giving medicines is outside many roles; follow your scope and medical direction." The medicine sentence has no link to the sentence around it (boilerplate repeated across the book) |

Findings and exact fixes
B1. FIX (owner decision). front/copyright.md opens "Copyright (c) 2026 Mark Gerald Simon. All rights reserved" yet the same page says the text and all illustrations were generated by AI. A full rights claim over AI-generated material may be inaccurate. status.md open item 7 ("copyright wording for AI-generated text") is still unresolved. Fix: owner decides the wording with a qualified adviser (for example, claiming copyright only in the human selection, arrangement and edits), then update the page. I am not giving legal advice. Also confirm "Mark Gerald Simon" is the owner-approved pen name (book.yaml says pen name; status.md records it as supplied by the owner) and that no ISBN/publisher line is invented (none is).
B2. FIX (low). Entry 6.2 step 2: reword the last sentence to "If you are alone and saw the child collapse suddenly, call emergency services (use a phone if you have one, or go for help) and fetch an AED first, then begin CPR." Check wording against the owner's AHA text before saving. Keep Q3 and its key as they are.
B3. FIX (low). Entry 6.2 step 7: add what to do if the pads would touch, taken from the owner's AHA text or the AED's own prompts (for example, "if they would touch, place one pad on the front of the chest and one on the back, and follow the device prompts"). Do not add it if the supplied PDF does not say it. Add one clause about pad spacing to Entry 3.4's child-under-8 sentence for consistency.
B4. FIX (low). Remove or relocate "Giving medicines is outside many roles; follow your scope and medical direction." in the CPR paragraph after the box in 6.2 (nothing in that paragraph mentions a medicine). The sentence is repeated more than ten times across chapters, glossary and answer keys; a one-star reviewer may call this padding. Keep it where a medicine is actually named.
B5. FIX (low). Align the "heart tracings" wording across how-to-use.md, copyright.md and the descriptions (see A3). Entry 3.3 and Figure 10 do teach basic rhythm patterns.
B6. NOTE (status, not a manuscript claim). The clinician clearance is recorded on the owner's word only. Do not add any "reviewed by" wording to the book, cover, description or A+ content until written sign-off and credentials are on file. Nothing in the manuscript claims it.

Customer-experience risks (likely one-star reasons)
1. Rescuer reads 6.2 step 2 and cannot tell what an alone rescuer with no phone does after a witnessed collapse -> B2.
2. "Do not let pads touch" with no remedy on an infant's chest -> B3.
3. Repeated medicine-scope sentence reads as padding -> B4.
4. Reader expects no rhythm teaching, finds Figure 10, or expects it and finds little -> B5/A3.
5. Review questions: the correct option is the longest in about 80 percent of items (status.md open item 4) -> reviewers of study guides notice this; shorten correct options or lengthen distractors.
6. Figure 7 caption admits eye protection not drawn while the procedure lists it (stated in the caption, acceptable); Figure 25 is a mirrored AI image and clinician confirmation of pose is recorded on the owner's word only.
7. Page 56 is flagged "very little text" and six intentional blank pages (32, 82, 132, 166, 170, 176) are listed in build-report.md; the owner must look at them in KDP's online previewer. Not verified here.

VERDICT B: REVISE (no BLOCK). All policy-type scans clean; the remaining items are one rights-wording decision (B1) and five small text fixes (B2 to B5).

NEXT ACTION
1. Apply A1 to A4 in KDP-metadata.md and regenerate the .docx.
2. Apply B2 to B5; owner decides B1.
3. Owner picks categories, then check keywords against category words (A5); check the cover against title, subtitle and author.
4. Run a third, short review round (maximum three allowed by the checklist).
5. Keep the clinician's written sign-off with the clearance pack; use no review wording.

This is a good-faith review, not legal advice or a guarantee of Amazon's acceptance.
