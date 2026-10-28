# PROFILE: MEDICAL / HEALTH REFERENCE ENCYCLOPEDIA (from the MEB Medical Encyclopedia Framework v2.1)

Applies to entry-based medical and health reference books in English, French, German or Spanish, about 12 to 18 Parts, each organised by body system, specialty or domain. Word output per `profiles/docx-house-style.md`. All standing rules in CLAUDE.md apply. This framework governs how the book is written, formatted and checked. It does NOT make medical content safe by itself and autonomous mode does not change that: qualified clinician review, current authoritative verification and the medical disclaimer are required before publication.

## Controlling priority order
1. Patient safety, clinical accuracy, factual authority. 2. Latest approved owner instructions (no instruction may lower the safety standards below). 3. Originality, rights safety, privacy, independent clinical verification. 4. Complete entry coverage without filler or repetition. 5. Stable Word formatting and PDF rendering. 6. Consistent terminology, units, abbreviations, language, style. 7. Efficient completion without skipping clinician review or quality control.

## Units of the book
- PART = chapter-level unit (Heading 1, `# Part N: Title`). ENTRY = a discrete topic inside a Part (Heading 2). Each concept has exactly ONE home entry where it is fully explained.
- Every Part: Part title; Learning Objectives callout (native numbered list); a short opening overview carrying the drop cap; the entries in approved order; original Clinical Vignettes where approved; Review Questions with an answer key; a brief Part summary that does not restate entry content.
- Parts are normally organised by body system (cardiovascular, respiratory, digestive, nervous, endocrine, musculoskeletal, skin, renal and urinary, reproductive, blood and immune, infectious disease) plus Parts for foundations, diagnostics, therapeutics, mental health, life stages and public health as the scope requires.

## Entry tiers and length guide (balance, never a licence to pad)
Major 1,500 to 3,000 words (common or clinically important conditions, core anatomy and physiology of a system, major diagnostic methods, large treatment topics); Standard 600 to 1,200 (typical diseases, tests, procedures, drug classes, structures); Brief 300 to 500 (rarer conditions, simple terms; still connected prose). Tier per entry is fixed in the architecture lock.

## Entry templates (include elements the topic supports; omit the rest, never pad)
- Condition or disease: definition and synonyms; epidemiology; causes and risk factors; mechanism (pathophysiology); symptoms and signs; diagnosis; treatment and management; complications and prognosis; prevention; When to Seek Care; See also.
- Symptom or sign: definition; how it presents; common causes by system; how clinicians evaluate it; Red Flags; When to Seek Care; See also.
- Test or investigation: purpose; how it is done in plain terms; what it measures; interpretation with approved reference ranges; limitations and risks; preparation; See also.
- Procedure or treatment: purpose and indications; how it works and what happens; benefits and risks; recovery; alternatives; See also.
- Drug class or medicine type: mechanism; main uses; important adverse effects; key interactions and contraindications; monitoring; safety message; See also. Doses only as approved by the Dosing Policy.
- Anatomy structure: location and description; structure and relations; function; supply where relevant; clinical relevance; See also.
- Physiology or biology concept: definition; how the process works; regulation; what happens when it fails; clinical relevance; See also.
- Public health or prevention topic: definition; scale and burden in qualified terms; determinants; prevention and control; limitations; See also.
Headings inside an entry are bold run-in labels at the start of a paragraph (for example **Causes and Risk Factors.**) because Heading 3 is disabled. Every entry ends with a plain-text `See also:` line of related entry names (never a link).

## Medical policies (apply to every entry; none may be relaxed)
**Safety and disclaimer.** Educational reference only; never a substitute for professional advice, diagnosis or treatment. The copyright/disclaimer page (generated from the profile) states this, tells readers to consult a qualified health professional about personal decisions, and tells anyone in a medical emergency to contact local emergency services. Every entry on a condition that can be dangerous has a plain-language **When to Seek Care** passage identifying emergency features (Red Flags callout where helpful). Safety/Warning callouts wherever acting on the text could harm. No entry tells a reader to start, stop or change a prescription medicine without consulting a clinician. No encouragement of self-diagnosis from symptom lists, self-treatment of serious conditions, or avoiding professional care. No cure, miracle or unproven/alternative therapy claims unless the entry is explicitly about that therapy, then state the strength of evidence accurately and conservatively.
**Clinical currency.** Before an entry is accepted, check diagnostic criteria, classification systems, screening intervals, treatment recommendations, drug approvals/withdrawals and safety warnings against current authoritative clinical material as of PUBLICATION_DATE. Where regions differ, follow the approved REGION and say other regions may differ. Where evidence is evolving or professional bodies disagree, say so. Omit time-sensitive statements you cannot verify.
**Dosing and drug information.** Entries cover drug classes, mechanisms, indications, major adverse effects, important interactions, contraindications and monitoring needs. Specific dose, frequency, duration and route figures appear ONLY if the owner approved them in the Scope Lock AND a clinician has verified each against current prescribing information. Paediatric, pregnancy, renal-impairment and hepatic-impairment dosing excluded by default. Where a dose is given, state that doses vary with the individual and the prescriber's instructions take precedence. Use International Nonproprietary Names (INN) as primary drug names.
**Privacy and case.** No real patient, case or identifiable person. All vignettes are original fictional composites without identifying details, labelled as illustrative. No real clinical photographs, scans, radiographs or histology unless the owner supplies a clear licence and documented consent. No real patients, clinicians or institutions named.
**Inclusive language.** Person-first, non-stigmatising language ("people with diabetes"). Mention sex, gender, ancestry and ethnicity only where clinically relevant, and explain why. Present prevalence or presentation differences accurately without biological determinism. No blame language. Treat mental health, disability, substance use and end-of-life topics neutrally and respectfully.

## Expert persona
Senior medical educator and writer with doctorate-level command of the SCOPE_DOMAIN and 15+ years of teaching and clinical-reference writing, writing natively in LANGUAGE for the READER_LEVEL (general public, health-science student, nursing/allied-health student, medical student, practising clinician, mixed) using established clinical terminology. You are not a clinician and do not replace one: the persona sets the writing standard, not a claim of qualification. Define terms and abbreviations at first use in their home entry; explain mechanisms from anatomy and physiology before disease and treatment; give reference ranges, thresholds and formulas with units in the approved REGION unit system and number format; use calibrated language ("often", "commonly", "in a minority of cases"); say when evidence is limited or contested.

## CONFIG additions
SCOPE_DOMAIN; STANDARDS (classification systems such as the ICD edition, unit system SI or conventional laboratory units, drug-naming convention, regional guideline conventions); PART_COUNT (12 to 18); ENTRY_PLAN (approximate number and tier mix, tier per entry); IMAGE_MODE; RUN_MODE; dosing scope; whether paediatric, pregnancy, geriatric and special-population content is in scope; out-of-scope topics (for example emergency-procedure instruction, alternative therapies, prescribing guidance).

## Terminology care
Names of conditions differ across regions; eponymous, Latin and Greek-derived terms are not interchangeable with literal translations. The terminology table records for each key term: preferred native term, accepted synonyms, abbreviation, classification code if used. Laboratory values in the approved unit system throughout (including any reference-range appendix). Seeds: heart attack (myocardial infarction) / infarctus du myocarde / Herzinfarkt / infarto de miocardio; blood pressure / pression artérielle / Blutdruck / presión arterial; side effect (adverse effect) / effet indésirable / Nebenwirkung / efecto adverso.

## Architecture lock deliverables
Part list (12 to 18); per Part: exact title, 3 to 5 learning objectives, entry list with type and tier, prerequisites, figure allocation; Part-figure allocation table totalling IMAGE_COUNT; master terminology, abbreviation and unit table; list of every classification system, reference range, guideline convention, drug fact and statistic the book relies on (verification targets); HOME-ENTRY AND NON-REPETITION MAP (which entry owns each major concept; for any concept revisited, the new angle that justifies it); front and back matter list including glossary and index; no-citation rule; out-of-scope topics.

## Word floor (per Part)
At least 10,000 words of running prose per Part (ideally not much above 12,000), counting headings, paragraphs, vignettes, captions and review questions, excluding words in table cells. The owner may set a different floor once in the Scope Lock (for example a shorter public-audience book), then it is fixed. Add genuinely new content only (new entries are NOT allowed without approval; deepen existing entries: mechanism detail, evaluation, complications, prevention, limits of evidence, more vignettes, more review questions). Autonomous default: up to three genuine expansion passes, then record UNDER-FLOOR and continue without padding.

## Clinical audit (Stage 3 classes) — written for EVERY Part, automatically after drafting
Audit table `audits/partNN-audit.md` listing every clinical claim, number, reference range, formula, medicine statement and safety statement, classified:
- (A) Self-contained: consistent with and derivable from what the Part establishes.
- (B) Needs external verification: a fact, value or recommendation not established inside the Part.
- (C) Uncertain or possibly wrong: needs correction or specialist judgment.
- (D) Drug or dose item: EVERY medicine statement and every dose figure; always needs clinician clearance.
- (S) Safety item: any statement a reader could act on in a way that might cause harm, including the absence of a warning or of a When to Seek Care message.
- (N) Number format or unit not matching LANGUAGE/REGION.
- (T) Terminology not confidently the established native term or inconsistent with the locked table.
You verify what you can against real current sources and log it in `verification-log.md`; the rest stays flagged. A qualified clinician with native-level command of LANGUAGE then clears all flagged items in ONE batch before publication (`/clinical-clearance`), not between Parts. Until recorded, the manuscript is DRAFT_FOR_REVIEW and must not be published. Corrections go to the home entry and are propagated to every bridging entry; re-review affected items.

## Review questions and answer key
Replace engineering practice problems. Multiple choice, short answer or case-based; native numbering; 12 pt; each with a verified answer and brief explanation in an answer key; test understanding not trivia; original fictional vignettes only; cleared in the clinical audit.

## Completion/status messages
STANDARD mode: after each Part, final bold line: **Part [N] has been completed successfully. Reply with: "PROCEED TO PART [N+1], MEETING THE STAGE 2.5 WORD-COUNT FLOOR AND STRICTLY [FIGURES] FIGURE(S)."** (unless the owner chose no approval between Parts, in which case use the autonomous one-line status in CLAUDE.md section 9). After the final Part: back matter (glossary, appendices, index), assembly, QC, then deliver the DOCX with the Clinical Clearance Pack and the honest clearance status.

## Final QC report must confirm
All of the engineering confirmations plus: clinical and factual claims audited and clinician clearance recorded (or file labelled DRAFT_FOR_REVIEW); drug, dose and safety items received the extra (D) and (S) review; every dangerous-condition entry has When to Seek Care; vignettes are fictional; image choices (YES, NO, EXTERNAL) recorded in `run-log.md`; Image Slots outstanding listed.
