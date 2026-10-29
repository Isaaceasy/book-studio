# OUTLINE (Architecture Lock proposal): Emergency Nursing Fundamentals

Date: 2026-10-29. Status: AWAITING OWNER APPROVAL. Nothing below is chapter prose.

## 1. Book identity
- **Title:** Emergency Nursing Fundamentals
- **Subtitle:** A Compact Illustrated Guide to Rapid Assessment, Priorities and Procedures for Nursing, Paramedic, EMT and Allied Health Students (161 characters with the title)
- **Promise:** after reading, a nursing, paramedic/EMT or allied-health student can recognize a deteriorating or time-critical patient, state the first priorities in the right order, and describe the basic emergency skills in their own words, while knowing where their own scope of practice and local protocol begin.
- **Framework:** MEDICAL profile, Parts by phase of emergency care and by problem type (not by body system, because a compact guide must follow the order in which a responder thinks: safe, sort, ABCDE, then problem). Each Part contains ENTRIES with a tier. Scope Lock: compact book (owner, 2026-10-29).
- **Format:** KDP print PDF, 5 x 8 in, standard color, US English, amazon.com. Output overridden from Word to PDF (owner). Page estimate: see Pages below.
- **Length (revised after compliance round 2):** Part targets (words, callouts, step lists, captions and review questions all INCLUDED): Part 1 5,400; Part 2 5,500; Part 3 5,250; Part 4 5,500; Part 5 5,400; Part 6 5,650 = about 32,700 words in Parts (floor 5,000, ceiling 6,000, table cells excluded). Front and back matter about 5,000 words (answer-key explanations about 2,000, glossary about 1,500, abbreviations, Appendix C, front matter). Total about 37,700 words.
- **Pages (single estimate):** about 150 to 180 pages at 5 x 8 in (about 280 words per page of text plus 25 figures); the royalty table in market-research.md section 9b (120, 150, 180 pages) covers this range and is recalculated at the real page count at assembly.
- **Figures:** 25 (owner). All anatomical images and illustrations generated with HiggsField (owner); SVG only for non-anatomical flowcharts, algorithms and schematics. Because AI models err on hands, equipment position and proportions, every one of the 25 figures goes to clinician review, labels and numbers are added outside the AI image, and a figure that fails review is redrawn as SVG (fallback for owner approval at that time).
- **Dosing scope (owner rule, clarified):** NO MEDICINE dose, frequency, duration or route is given anywhere. Verified PROCEDURAL parameters are allowed because a CPR or bleeding-control entry is useless without them: compression rate, depth and ratio, ventilation rate, tourniquet and cooling timings, glucose thresholds, reference values. Each such figure needs a logged current source and clinician clearance. Oxygen: device types and when they are used only, no flow-rate figures. Public wording everywhere (cover, description, front matter) is "no medicine doses", never "no dose figures". Recorded in status.md as a default for the owner to confirm.
- **Drugs outside the closed list below:** not named and not described (glucagon, fever reducers, activated charcoal, antibiotics, fluids, anticonvulsants and others); the text says "the medicines used here are given by trained clinicians under medical direction" at most, and mentions a class only where a reader would otherwise be unsafe.
- **Closed list of drug and agent names that may appear (names only, never doses):** epinephrine (adrenaline), naloxone, albuterol (salbutamol), aspirin, oral glucose, oxygen. Nitrates and other drugs are named only as a class if essential. Every mention carries: "Giving medicines is outside many roles; follow your scope and medical direction."
- **Special populations:** children, pregnancy and older adults are in scope at the level of recognition, assessment differences and priorities, with no medicine dosing (Part 6).
- **Procedures (Scope Lock, owner choice):** basic, non-invasive, step-by-step skills are in scope although the medical profile lists emergency-procedure instruction as an example exclusion: blood glucose check step (1.3), positioning and recovery position (2.2), suction (2.2), adult choking relief (2.2), bag-valve-mask ventilation and oxygen delivery concepts (2.3), assisting with a patient's own pre-measured epinephrine auto-injector per device instructions (2.5), AED use and compressions (3.4), direct pressure, wound packing and tourniquet (4.2), spinal motion restriction principles (4.3), splinting (4.4), oral glucose for a conscious patient able to swallow, per protocol and with no amount stated (5.1), infant and child choking relief, rescue breathing and CPR differences (6.2), left-lateral positioning (6.3). Each procedure carries a Safety callout, a scope-of-practice and local-protocol line, a stop-and-call line, and clinician verification before publication; all are class (S) audit items. The book has not been validated for any individual state protocol. No invasive or advanced skills.
- **Behavioral emergencies (6.5):** safe-messaging language for suicide risk; no restraint technique is taught.

## 2. Structure of every Part (fixed)
1. Part title (Heading 1, `# Part N: Title`).
2. Learning Objectives callout (3 to 5, numbered).
3. Opening overview (about 250 words, drop-cap style per design).
4. Entries in the approved order, each with run-in bold labels (no Heading 3), a **Nursing and Responder Priorities.** passage in EVERY entry (two to three sentences in Brief entries; fuller in Major and Standard), a **When to Seek Care / Call for Help.** or **Red Flags.** passage where an emergency feature exists, and a closing plain-text `See also:` line.
5. One original Clinical Vignette (about 250 words), fictional composite labelled illustrative.
6. **Care Priorities.** (about 250 words, the Part summary written as the ordered priorities a nursing student would carry onto the floor; it does not restate entries).
7. Review Questions: 8 per Part (multiple choice and short case-based, about 700 words including stems), answer keys in Appendix A.

Per-Part budget (words): overview 250 + entries (3,800 to 4,200, see tables) + vignette 250 + Care Priorities 250 + review questions about 700 = the Part targets in section 1. Learning objectives, callouts, step lists and figure captions are counted inside entry budgets; entry budgets for procedure entries were raised in round 2 so the full procedure pattern fits. A Part that lands under 5,000 after genuine expansion passes is recorded UNDER-FLOOR, never padded. No chapter is drafted until the matching rows exist in `verification-log.md`. Entry tiers are scaled to the compact book (Scope Lock): Major about 1,000 to 1,200; Standard about 450 to 800 (procedure entries sit at the top of the band by design); Brief about 350 to 500. These replace the 1,500 to 3,000 / 600 to 1,200 / 300 to 500 profile guide for this book only.

## 3. Parts, entries, tiers, learning objectives and figures

### Part 1: The Emergency Approach: Safety, Triage and Assessment (4 figures)
Prerequisites: none.
Objectives: (1) Describe scene and personal safety steps before patient contact. (2) Explain how triage assigns priority and apply a five-level acuity idea to short scenarios. (3) Describe the order of the primary survey (ABCDE) and the check made at each step, including level of consciousness and a blood glucose check. (4) Describe how to gather a focused history and a set of vital signs and name abnormal findings. (5) Describe a structured handover and the reassessment and documentation that go with it, within scope of practice.
| Entry | Type | Tier | Words |
|---|---|---|---|
| 1.1 Scene safety, personal protection and responder wellbeing | Procedure or concept | Standard | 650 |
| 1.2 Triage and acuity (generic five-level principle; no named proprietary system in the text) | Concept | Major | 1,100 |
| 1.3 The primary survey (ABCDE), including GCS and AVPU, perfusion signs and a glucose check | Procedure | Major | 1,100 |
| 1.4 History, vital signs and the secondary survey | Test or investigation | Standard | 650 |
| 1.5 Communication, consent, scope of practice, handover, reassessment and documentation | Concept | Brief | 450 |
Forward pointers (plain text only, one-sentence bridges with no new teaching): 1.3 to Entry 3.5 (shock) and Entry 5.1 (low blood glucose); 1.4 to Entry 5.4 (early warning and sepsis screening); 2.2 to Entry 3.4 (when an obstructed patient becomes unresponsive); 2.4 to Entry 5.1 (confusion in respiratory failure); 2.5 to Entry 3.5 (shock).
Figures: F1 primary survey sequence (SVG flow). F2 triage decision flow, generic five-level principle drawn fresh, not copied from any published figure (SVG flow). F3 assessment sites for pulse, breathing and perfusion on an adult figure (HiggsField illustration). F4 structured handover sequence (SVG schematic).
Vignette idea: a nursing student at a school sports event finds an unresponsive spectator and works through scene safety and the primary survey.

### Part 2: Airway and Breathing Emergencies (4 figures)
Prerequisites: Part 1 (primary survey).
Objectives: (1) Identify the structures of the upper airway and what narrows or blocks them. (2) Recognize partial and complete airway obstruction and state the response. (3) Describe basic airway positioning, suction and bag-valve-mask ventilation steps and their safety limits. (4) Recognize respiratory distress and failure and state first priorities for asthma, COPD and pneumonia. (5) Recognize anaphylaxis and state the first priorities.
| Entry | Type | Tier | Words |
|---|---|---|---|
| 2.1 Airway anatomy and assessment | Anatomy + assessment | Standard | 650 |
| 2.2 Airway obstruction and basic airway management (positioning, jaw thrust, suction, recovery position, adult choking relief) | Condition + procedure | Major | 1,100 |
| 2.3 Ventilation support: bag-valve-mask and oxygen delivery concepts (device types and when, no flow-rate figures) | Procedure | Standard | 800 |
| 2.4 Respiratory distress: asthma, COPD and pneumonia | Condition | Major | 1,000 |
| 2.5 Anaphylaxis (including assisting with a patient's own pre-measured auto-injector, per device instructions) | Condition + procedure | Brief | 500 |
Figures: F5 upper airway anatomy and landmarks (HiggsField, anatomical). F6 head-tilt chin-lift and jaw thrust positions (HiggsField illustration). F7 bag-valve-mask two-hand seal technique (HiggsField illustration). F8 respiratory distress recognition and first-priority flow (SVG).
Vignette idea: a fictional teenager with wheeze at a youth camp; a camp nurse and a first-year paramedic student sort priorities.

### Part 3: Cardiac Emergencies and Resuscitation (4 figures)
Prerequisites: Parts 1 and 2.
Objectives: (1) Describe the heart's pump and electrical functions in plain terms. (2) Recognize acute chest pain patterns and acute coronary syndrome and state first priorities. (3) Recognize a short list of dangerous rhythm patterns and what they mean for the patient. (4) Describe high-quality adult CPR and AED use, step by step. (5) Recognize shock and state the common first priorities.
| Entry | Type | Tier | Words |
|---|---|---|---|
| 3.1 The heart in brief: pump, vessels and electrical system | Anatomy | Brief | 350 |
| 3.2 Acute chest pain and acute coronary syndrome | Condition | Major | 1,100 |
| 3.3 Recognizing dangerous rhythms | Test or investigation | Standard | 650 |
| 3.4 Cardiac arrest, high-quality CPR and the AED | Condition + procedure | Major | 1,200 |
| 3.5 Shock: recognition and first priorities | Concept | Standard | 500 |
Figures: F9 heart and coronary arteries (HiggsField, anatomical). F10 rhythm pattern schematics, original drawings not copied from any source (SVG). F11 compression hand position and body position (HiggsField illustration). F12 adult cardiac arrest response sequence, original simplified flow (SVG).
Vignette idea: a fictional gym member with chest pressure then collapse; the chain from recognition to AED.

### Part 4: Trauma, Burns and Environmental Emergencies (6 figures)
Prerequisites: Parts 1 to 3.
Objectives: (1) Use mechanism of injury to raise suspicion of serious injury. (2) Describe the order of external bleeding control (pressure, packing, tourniquet) and the steps of each. (3) Recognize head, spine and chest injuries and state first priorities, including motion restriction principles. (4) Describe basic splinting and the checks that go with it. (5) Estimate burn size and state first priorities. (6) Recognize heat and cold emergencies.
| Entry | Type | Tier | Words |
|---|---|---|---|
| 4.1 Trauma assessment and mechanism of injury | Concept | Standard | 600 |
| 4.2 Bleeding and hemorrhage control | Condition + procedure | Major | 1,100 |
| 4.3 Head, spine and chest injuries (with spinal motion restriction principles) | Condition + procedure | Standard | 800 |
| 4.4 Fractures, dislocations and splinting | Condition + procedure | Standard | 750 |
| 4.5 Burns | Condition | Standard | 450 |
| 4.6 Heat and cold emergencies | Condition | Brief | 350 |
Figures: F13 tourniquet application on a limb (HiggsField illustration). F14 direct pressure and wound packing (HiggsField illustration). F15 chest wall and lung anatomy with common injury sites (HiggsField, anatomical; recognition only, no decompression). F16 limb splinting with joint above and below (HiggsField illustration). F17 burn body-surface estimation diagram (HiggsField illustration). F18 heat and cold illness continuum (SVG).
Vignette idea: a fictional cyclist with a leg laceration on a trail; staged bleeding control.

### Part 5: Medical Emergencies (4 figures)
Prerequisites: Parts 1 to 3.
Objectives: (1) Describe an approach to a patient with altered mental status and the reversible causes to check, such as low blood glucose. (2) Recognize stroke with a validated stroke screen and state why time matters. (3) Describe the response to a seizure. (4) Recognize sepsis and state first priorities. (5) Describe first priorities in poisoning and overdose. (6) Recognize acute abdominal emergencies and gastrointestinal bleeding.
| Entry | Type | Tier | Words |
|---|---|---|---|
| 5.1 Altered mental status and hypoglycemia | Symptom + condition | Standard | 700 |
| 5.2 Stroke | Condition | Major | 1,000 |
| 5.3 Seizures | Condition | Brief | 500 |
| 5.4 Sepsis | Condition | Standard | 700 |
| 5.5 Poisoning and overdose | Condition | Standard | 600 |
| 5.6 Acute abdominal pain and gastrointestinal bleeding | Symptom + condition | Brief | 450 |
Figures: F19 altered mental status approach flow (SVG). F20 brain arterial territories (HiggsField, anatomical). F21 stroke screening signs on a face and arms (HiggsField illustration). F22 sepsis recognition pathway (SVG).
Vignette idea: a fictional older adult found confused at home; step through reversible causes.

### Part 6: Special Populations, Behavioral Emergencies and Safety (3 figures)
Prerequisites: Parts 1 to 5.
Objectives: (1) Describe the structured pediatric assessment and how children differ from adults. (2) Describe how choking relief, breathing support and CPR differ in infants and children. (3) Recognize pregnancy-related emergencies, describe safe positioning and state when to call for help for an imminent birth. (4) Describe how assessment changes in older adults. (5) Describe a safe response to behavioral and mental health emergencies using safe-messaging language. (6) Recognize signs of abuse or neglect and state reporting duties in general terms.
| Entry | Type | Tier | Words |
|---|---|---|---|
| 6.1 Children: assessment and how they differ | Concept + condition | Major | 1,100 |
| 6.2 Children: choking, breathing support and resuscitation differences | Condition + procedure | Standard | 800 |
| 6.3 Pregnancy emergencies and imminent birth: recognition and calling for help | Condition | Standard | 650 |
| 6.4 Older adults | Concept | Standard | 600 |
| 6.5 Behavioral and mental health emergencies | Condition | Standard | 650 |
| 6.6 Abuse, neglect and interpersonal violence | Concept | Brief | 400 |
Responder wellbeing moves to a paragraph inside 1.1 (no separate entry).
Figures: F23 pediatric assessment triangle (SVG schematic). F24 child versus adult airway differences (HiggsField, anatomical). F25 left-lateral positioning of a pregnant patient (HiggsField illustration).
Vignette idea: a fictional toddler with fever and poor feeding seen at triage; priorities differ by age.

## 4. Figure allocation table (total = image_count = 25)
| Part | SVG | HiggsField | Total |
|---|---|---|---|
| 1 | 3 (F1, F2, F4) | 1 (F3) | 4 |
| 2 | 1 (F8) | 3 (F5, F6, F7) | 4 |
| 3 | 2 (F10, F12) | 2 (F9, F11) | 4 |
| 4 | 1 (F18) | 5 (F13 to F17) | 6 |
| 5 | 2 (F19, F22) | 2 (F20, F21) | 4 |
| 6 | 1 (F23) | 2 (F24, F25) | 3 |
| Total | 10 | 15 | 25 |
Figure rules: all HiggsField figures are anatomical or illustrative, never realistic clinical photographs; text labels are added outside the AI image; every figure is to be reviewed by a qualified clinician before use (planned, not yet arranged); every figure must read at 5 x 8 in; algorithm-like figures are drawn fresh and never copy a guideline's published figure; AI use is recorded in `status.md`. Allocations do not change without owner approval. If the final delivered count is under about 12, "Illustrated" leaves the subtitle.

## 5. Front matter plan
Title page; copyright and disclaimer page (education only, not a substitute for training, local protocol or medical direction; in an emergency contact local emergency services; US scope; no medicine doses (verified emergency-procedure figures such as compression rate are given); basic, non-invasive skills only; not validated for any individual state protocol; not affiliated with or endorsed by any professional association or certifying body; AI-generated content statement matching the KDP answers); a one-page "How to use this book and scope of practice" note; static contents page. No dedication or acknowledgements unless the owner supplies them.

## 6. Back matter plan
Appendix A: answer keys to all Review Questions with brief explanations. Appendix B: abbreviations. Appendix C: adult and pediatric reference values used in the book (vital signs, Glasgow Coma Scale layout, burn percentages) with units, one table each, all verified. Glossary (about 60 terms). Static index. No bibliography, reference list, further reading, footnotes, URLs or hyperlinks.

## 7. Out of scope (explicit)
Drowning, carbon monoxide and smoke inhalation, pulmonary embolism, diabetic ketoacidosis, syncope, hypertensive emergencies, bites and stings, and electrical or lightning injury do not get entries of their own (each may be named in one sentence inside the entry where it presents, for example diabetic ketoacidosis as a cause in 5.1); the description lists these exclusions. Drug doses and drug-by-drug protocols; IV or IO access, medication administration, cardiac monitoring and 12-lead ECG acquisition as nursing tasks (the book teaches recognition and priorities, not those skills); intubation and advanced airways; chest decompression and other invasive skills; 12-lead ECG interpretation; ACLS drug algorithms; obstetric delivery maneuvers; prescribing; alternative therapies; disaster and mass-casualty command beyond the triage basics in 1.2; certification exam preparation (no pass-rate or exam promises); local or state protocols (the book says protocols differ and the reader must follow their own); neonatal resuscitation beyond recognition.

## 8. Market gaps addressed (from market-research.md sections 7 and 9b)
| Gap (status) | Where answered |
|---|---|
| Compact illustrated reference in the $19.99 to $29.99 band between pocket cards and huge textbooks (CONFIRMED structure and price) | whole book: 6 Parts, 5 x 8 in, 25 figures |
| Many leaders are older editions (CONFIRMED) | every Part WILL be checked against current guidelines as of 2026-10-29 at its fact-check; nothing is verified yet (section 10) |
| Visual support in the band (POSSIBLE) | 25 figures, 4 per Part on average; clinician review planned for every figure (no "clinician-reviewed" wording anywhere until clearance is recorded) |
| Procedures in prose with safety callouts, no medicine doses (POSSIBLE) | procedures in 1.3, 2.2, 2.3, 2.5, 3.4, 4.2, 4.3, 4.4, 5.1, 6.2, 6.3 |
| One book for nursing, paramedic/EMT, allied health (POSSIBLE) | "Nursing and Responder Priorities." label in every entry; scope-of-practice line in every procedure; reassessment and documentation in 1.5 |
| Reader complaints about leaders (UNVERIFIED, reviews not seen) | none claimed; to re-check when reviews can be seen |
Must-avoid list from the research: brand, author and series names; dose figures; padding; copying competitor structures; claims of outcomes, exam results or rank; any use of the word "Pocket" (owner and compliance review).

## 9. Home-entry and non-repetition map
| Concept | Home entry | Revisited in | New angle only |
|---|---|---|---|
| ABCDE primary survey | 1.3 | 4.1 | mechanism-driven catastrophic bleeding first |
| | | 6.1 | child-specific sequence and findings |
| Triage and acuity | 1.2 | 6.1 | pediatric acuity cues |
| Vital signs and reference values | 1.4 | 5.4 | early warning screening in suspected sepsis |
| | | 6.1, 6.3 | child and older adult differences only |
| Handover | 1.5 | none | one structured method only |
| Airway positioning, suction | 2.2 | 4.3 | spine-aware jaw thrust |
| | | 6.1 | child anatomy differences |
| Bag-valve-mask | 2.3 | 6.1 | child sizing and rate cues only |
| Shock | 3.5 | 4.2 | hemorrhagic cause and control |
| | | 5.4 | septic cause |
| CPR and AED | 3.4 | 6.1, 6.2 | child and pregnancy adaptations only |
| Anaphylaxis | 2.5 | none | |
| Hypoglycemia | 5.1 | 6.1 | child-specific cues |
| Stroke screen | 5.2 | 5.1 | as one cause in altered mental status (one sentence bridge) |
Additional rows (round 2): recovery position: home 2.2, 5.1 and 5.3 give one-sentence bridges only. CPR adaptation in pregnancy: 3.4 home, 6.3 adaptation only. Intentional overdose and self-harm: 5.5 covers poisoning management priorities, 6.5 owns the mental health side. Child abuse: home 6.6, 4.1 and 6.1 one sentence each. Heat and cold in older adults: 4.6 home, 6.4 differences only. Burns in children: 4.5 home, 6.1 one sentence. Asthma in children: 2.4 home, 6.1 one sentence. Spinal motion restriction in children: 4.3 home, 6.1 one sentence. Appendix C reference tables are the ONLY permitted deliberate repeat of the home values in 1.4 (adult values) and 6.1 (child values), labelled as a reference copy. Care Priorities passages never restate entry content.
Additional rows (compliance round 1): GCS and AVPU: home 1.3, revisited in 5.1 (altered mental status cues only). Perfusion signs: home 1.3, full shock explanation 3.5. Blood glucose check step: 1.3 (step only), home for low blood glucose 5.1. Choking relief: adult home 2.2, infant and child home 6.2. Recovery position: home 2.2. Oxygen delivery: home 2.3, revisited in 2.4 (COPD caution, new angle only) and 2.5 (none). SpO2 and hypoxia: home 1.4, revisited 2.3 (treatment side only). Naloxone and opioid overdose: home 5.5, revisited 5.1 (as a reversible cause, one sentence). Anaphylaxis in children: 2.5 home, 6.1 one sentence. Sepsis in children and older adults: 5.4 home, 6.1 and 6.4 differences only. Chest pain in older adults and women: 3.2 home, 6.4 new angle only. Febrile and first seizure in children: 5.3 home, 6.1 one sentence. Tourniquet in children: 4.2 home, 6.1 one sentence. Pediatric content is spread: 6.1 owns assessment, 6.2 owns choking, ventilation and CPR differences, so no single entry carries all child revisits.
Rule: a later entry uses a short plain-text bridge ("Entry 1.3 set out the primary survey.") then adds only the new angle. No reuse of sentences, examples, tables, figures or vignettes.

## 10. Verification targets (become the fact-check ledger; nothing below has been verified yet)
Outline-stage scan only (search results, pages not opened; recorded in `verification-log.md`): American Heart Association 2025 CPR and emergency cardiovascular care guidelines (adult and pediatric basic life support, chain of survival, compression rate and depth, ratios, choking response, infant technique, AED use, pregnancy modifications); triage principles and five-level acuity concept (used generically in the text: the manuscript does not name the Emergency Severity Index, START, ENA, AHA or any course; the Emergency Severity Index handbook, published by the Emergency Nurses Association in 2023, and field triage criteria are consulted only to check the general principles); adult and pediatric normal vital sign ranges and early warning scores; Glasgow Coma Scale and AVPU; blood glucose thresholds for hypoglycemia (US conventional units with SI); stroke screening tools and time windows; Surviving Sepsis Campaign 2026 adult guideline (published March 2026) and screening tools; current hemorrhage-control guidance (tourniquet placement and wound packing); burn size estimation methods and first-aid cooling; heat stroke and hypothermia criteria; pediatric assessment triangle; left-lateral positioning in pregnancy; anaphylaxis first-line treatment name; naloxone use in opioid overdose; seizure first aid; choking relief sequence; asthma and COPD severity signs; chest pain red flags; common rhythm recognition basics; abuse and neglect reporting duties in general terms; every unit and conversion used. All claims time-sensitive to 2026-10-29. No claim enters the manuscript until opened and logged.

## 11. Standards and conventions
US English and US guidelines (amazon.com). Units: US conventional first with SI in parentheses where clinically used (blood glucose in mg/dL (mmol/L), temperature in degrees Fahrenheit (degrees Celsius), weight in pounds (kilograms) when needed); the terminology table fixes each. Drug names: US generic names with the international name in parentheses where different at first use (for example epinephrine (adrenaline), albuterol (salbutamol)); no brand names. ICD-10-CM codes are not used in the prose. Person-first language. No real patients; vignettes fictional and labelled illustrative.

## 11b. Claims rule and clearance
No "clinician-reviewed", "clinician-checked", "expert-verified" or similar wording on the cover, in metadata, in the description, in front matter or in A+ content until clearance by a named qualified clinician is recorded in `status.md`. No clinician has been engaged yet (open item for the owner); until recorded, the manuscript is DRAFT_FOR_REVIEW and must not be published. The description must say: basic non-invasive skills only; no medicine doses; no IV, medication administration, ECG or advanced airway content; US scope; educational use only; not exam preparation; 5 x 8 in print.

## 12. Rules restated
No citations, footnotes, bibliography, reference list, further-reading list, URLs, DOIs or hyperlinks in the manuscript. Plain-text cross-references only. Sources live only in `verification-log.md`. Medical profile safety and clinical-currency policies apply to every entry; the manuscript stays DRAFT_FOR_REVIEW until a qualified clinician clears the flagged items.
