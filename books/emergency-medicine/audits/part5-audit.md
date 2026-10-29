# Part 5 editorial and clinical audit: Medical Emergencies (chapters/ch05.md)

Date 2026-10-29. Auditor: independent editor. ch05.md NOT edited. Verdict: **REVISE** (blocking: changes 1 to 6; UNDER-FLOOR by 450 words).

I did not open external sources in this audit and I do not judge accuracy; items for the fact-checker are in section 7. verification-log.md has zero Part 5 rows (grep "P5-" = 0), so every B, D and S item below is unlogged until the parallel fact-check writes its rows. Figures 19 to 22: I read the SVG text layers (Fig 19, 20, 21, 22 labels) but I could not view the raster images in Fig 20 and 21, so pointer wording that depends on image content is marked "check against image".

## 1. Mechanical results
| Check | Result |
|---|---|
| Words, whole file (wc -w) | 4,550. No table in the Part, so nothing to exclude |
| Words with markup stripped (":::", "{.label}", image paths, "[5.1]{.num}") | 4,485 |
| Target / floor / ceiling | target 5,400, floor 5,000, ceiling 6,000 |
| **UNDER-FLOOR** | **450 words short of the floor by wc (515 by stripped count); 850 short of the 5,400 target** |
| Per-section words vs outline budget | Title + objectives + overview 282 vs 250; 5.1 937 vs 700 (+34%); 5.2 642 vs 1,000 (-36%); 5.3 456 vs 500; 5.4 510 vs 700 (-27%); 5.5 648 vs 600; 5.6 474 vs 450; Illustrative Case 231 vs 250; Care Priorities 108 vs 250 (-57%); Review Questions 262 vs about 700 (-63%) |
| Sentences | 336 (includes review options); average 13.1 words; 17 over 30 words (5.1%); longest 53 (L140 Recognition in 5.4); 38 and 43 in Priorities and naloxone sentences |
| Repeated openers | "The" 23, "A" 17, "Check" 10, "Do" 9, "It" 8, "Call" 8. No run of three identical openers inside a paragraph, but L98, L156, L170, L208 are strings of imperative sentences ("Check ... Call ... Give ... Keep ...") |
| Em dashes / en dashes | 0 / 0 |
| Banned or flagged words | "easy" L14 ("easy to explain away"); "easiest" L38 (same family, banned by style guide); "dose" L64 ("second dose of sugar"; the book gives no doses, and the word invites the question); "vital" L18, 140, 154, 156, 158, 160, 208 are all "vital signs" (legitimate term). No commonest, life-saving, never, always, simply, just (L28 "just before" is time use), crucial, golden hour, ER, delve, moreover, furthermore, additionally |
| URLs, links, citations, footnotes | None. One phone number in running text (1-800-222-1222, L170), which is a fact-check item, not a URL. No brand or organization names; "Poison Help line" is a service name, acceptable if the fact-check confirms it |
| Placeholders | None. Files ch05-fig19..22.svg exist |
| Callout words (20 to 60) | Objectives 86 (list, fine); Safety 5.1 45, 5.3 29, 5.5 46; Red Flags 5.2 43, 5.3 51, 5.4 38, 5.5 38, 5.6 41. All in range |
| Remember callouts | None in Part 5 (limit "at most one per entry" met; no duplication risk). See change 4 for one worth adding (stroke screen) |
| Headings | One H1 ("Medical Emergencies", data-label Part 5); H2 entries 5.1 to 5.6 with exactly the outline titles and order; Illustrative Case, Care Priorities, Review Questions follow |
| Answer key | back/answer-keys-part5.md DOES NOT EXIST (Parts 1 and 2 have one). Letters below are inferred from the text |
| verification-log.md | zero Part 5 rows |
| Repetition vs Parts 1 to 4 | Verbatim-level overlap with ch01 L168 in 5.1 (see consistency list). Duplicate material inside the Part: 5.4 risk list twice; 5.3 prohibitions twice |

## 2. Structure against outline
- Entries 5.1 to 5.6 present, in order, with outline titles. Objectives 1 to 6 match the outline word for word.
- Figures: captions begin "Figure 19." to "Figure 22.", numbers match the outline allocation (19 to 22), each caption is one sentence. Each figure has an in-text pointer BEFORE the figure (Fig 19 L30, 20 L76, 21 L82, 22 L142). **All four pointers are bare one-liners that tell the reader nothing to look for** (recurring fault; change 7).
- Procedure pattern (5.1 is the only Part 5 procedure in the Scope Lock):
  | Procedure | Purpose | Scope | Steps | Safety | Stop line | Why prose |
  |---|---|---|---|---|---|---|
  | 5.1 conscious patient with low glucose | yes | yes | 7 | yes | yes | yes |
  Pattern complete. Weaknesses: Safety callout repeats step 3 (swallowing) and ends with the confusing "and wait"; "fast-acting sugar that your protocol names" never names oral glucose although it is on the closed drug list (the sentence "Giving medicines is outside many roles..." is present, which is correct). No Entry 2.2 bridge for the recovery position (outline: one-sentence bridge).
- Nursing and Responder Priorities and See also present in all six entries.
- Emergency-feature passage: Red Flags present in 5.2, 5.3, 5.4, 5.5, 5.6. **5.1 (altered mental status, a time-critical sign) has none** and rests on a Stop line only (change 6).
- Bridges required by the outline map and Part 1/2 forward pointers:
  | Required | In text? |
  |---|---|
  | 5.1 revisits GCS/AVPU (cues only) | yes, one sentence |
  | 5.1 naloxone/opioid as a reversible cause (one sentence) | **missing** (opioid appears only in 5.5) |
  | 5.1 stroke screen (one-sentence bridge to 5.2) | list mentions "signs of stroke", no Entry 5.2 pointer |
  | 5.1 and 5.3 recovery position (one-sentence bridge to 2.2) | **missing in text**; 5.3 has it only in See also |
  | 5.1 diabetic ketoacidosis named once (outline section 7) | **missing**; no mention of a HIGH glucose reading at all |
  | 5.4 early warning/sepsis screening (from 1.4) | thin: one clause (L140) |
  | 5.4 septic cause of shock (new angle on 3.5) | **missing** (3.5's table says only "severe infection" under widened vessels) |
  | 5.3 febrile seizure (6.1 one sentence) | yes (L120) |
  | 5.5 intentional overdose to 6.5 | yes (L164) |
- Vignette: labelled, past tense, 231 words, no institution. **Uses a surname ("Mr. Alvarez"), against book-bible section 3 (first names only).**
- Care Priorities: 108 words and it **restates entries** (glucose check, last-known-well time, nothing by mouth) in the order of the Part. Violates style guide ("does not restate entries").
- Review Questions: 8 present (7 MCQ + 1 short case). Details in section 6.

## 3. Scores (1 to 5)
| Area | Score | Reason |
|---|---|---|
| Promise and structure | 3 | all entries and figures in order; no Red Flags in 5.1; missing bridges; Care Priorities restates entries |
| Substance at length | 2 | UNDER-FLOOR by 450; 5.2 (Major) at 642 of 1,000; 5.4 at 510 of 700; duplicate lists inside 5.1, 5.3, 5.4 |
| Clarity and readability | 4 | average 13.1 words, plain, clear; six-question chain in 5.1 and 53-word sentence in 5.4 |
| Voice consistency | 4 | calm second person, US spelling; "easy", "easiest", "dose" drift |
| Specificity and examples | 3 | stroke screen never named; "time limits measured in hours" vague; sepsis thresholds absent by design but no screening explanation |
| Teaching quality | 3 | stroke reasoning (clot vs bleed) is half-given; septic shock mechanism missing; DKA/high glucose absent; vignette excludes stroke too quickly |
| Human-sounding prose | 3 | "not X, it is Y" at L22; neat closers at L72, L106, L156; Priorities chains; question chain at L28 |
| Consistency | 3 | 70 mg/dL sentence near-duplicates ch01 L168; "Mr. Alvarez"; See also 6.4/4.1 point at content that is not there; CO beyond outline section 7 |
| Chapter ending | 2 | Care Priorities restates; Review Questions close the Part with implausible distractors, letter B four times, no answer key, Q8 repeats the vignette |

## 4. Audit table (classes A/B/C/D/S/N/T)
| # | Location | Claim / item | Class | Status / note |
|---|---|---|---|---|
| 1 | 5.1 | Altered mental status runs from mild confusion to unresponsiveness; trend matters more than one score | A/B | consistent with 1.3; log row |
| 2 | 5.1 | Brain sensitive to oxygen, glucose and blood contents; infection, poison, head injury, stroke change behavior | B | standard; log row |
| 3 | 5.1 | Do not assume confusion is alcohol or old age until reversible causes excluded | S/B | good safety message; log row |
| 4 | 5.1 | Reversible-cause checklist (airway/oxygen, glucose, stroke, head injury, infection, poisoning, seizure, temperature, low BP) | B | clinician; add DKA/high glucose and opioid (change 6) |
| 5 | 5.1 | Alcohol on breath does not exclude other causes; keep drowsy intoxicated patient on side (vomiting risk) | S/B | recovery-position bridge to 2.2 missing |
| 6 | 5.1 | Hypoglycemia below 70 mg/dL (3.9 mmol/L) for many people with diabetes; level varies | B | duplicate of ch01 L168; fact-check once; units written out here but "mg/dL" appears in Q2 undefined (N/T, change 6) |
| 7 | 5.1 | Hypoglycemia "most often occurs in people who take insulin or certain other diabetes medicines"; follows missed meals, extra exercise, alcohol | B | log row |
| 8 | 5.1 | Early signs shakiness, sweating, hunger, headache, anxiety; later confusion, slurred speech, drowsiness, seizures, loss of consciousness | B | log row |
| 9 | 5.1 procedure | Give a fast-acting sugar your protocol names; recheck after about 15 minutes; repeat if still low as protocol directs | S/D | oral glucose is on the closed list; procedural parameter "about 15 minutes" needs a logged source and clinician clearance |
| 10 | 5.1 procedure | Confirm awake, can sit up and swallow safely before giving by mouth | S | NEEDS-HUMAN; safety-critical, consistent with Safety callout |
| 11 | 5.1 Safety | Nothing by mouth if drowsy, confused to not following commands, seizing, or unable to swallow; unconscious but breathing to recovery position | S | consistent; "and wait" is unsafe wording (implies leave it at that), change 6 |
| 12 | 5.1 why-paragraph | "unnecessary second dose of sugar" | T/S | word "dose" in a book that gives none; change 6 |
| 13 | 5.1 | Mandatory sentence "Giving medicines is outside many roles..." present in Safety | D | present |
| 14 | 5.2 | Stroke = damage from blocked or burst vessel; most are clots; smaller number bleed | B | log row |
| 15 | 5.2 | TIA ("mini-stroke") clears alone; needs urgent assessment; full stroke may follow | B | "ischemic" used before glossed in the same sentence family; "same day" is advice, check wording (L88) |
| 16 | 5.2 | Signs: face droop, arm/leg weakness, speech, vision loss, double vision, severe headache, dizziness, balance loss | B | log row; ties to BE-FAST (not named, see change 4) |
| 17 | 5.2 | Screening: smile, raise both arms, repeat a sentence; ask time | B/S | tool not named; "validated" screen is an objective (Part objective 2). Fact-check the name (FAST / BE-FAST) |
| 18 | 5.2 | Mimics: low glucose, post-seizure weakness, migraine, some infections; treat as stroke until clinician shows otherwise; check glucose while waiting | S | "check glucose" must not delay the call: say so |
| 19 | 5.2 | "available treatments have time limits measured in hours" | B | vague; calibrated enough for scope, but the fact-checker should confirm no figure is implied |
| 20 | 5.2 | Last known well time = time before symptoms began, not time found | B/S | strong, correct in principle; wake-up case missing (change 4) |
| 21 | 5.2 | Keep patient lying with head slightly raised if comfortable, side if drowsy | S/C | head-of-bed position for suspected stroke is debated; clinician must clear or soften to "in the position of greatest comfort" |
| 22 | 5.2 | Give nothing by mouth because swallowing may be impaired | S | standard |
| 23 | 5.2 | Do not give aspirin unless medical direction says so, since some strokes are bleeds; mandatory sentence present | D/S | aspirin is on the closed list; correct pairing with the sentence; check consistency with 3.2 wording |
| 24 | 5.2 | "recognizing a stroke quickly and calling for help is more valuable than anything else a bystander can do" | C | superlative with no support; soften (change 4) |
| 25 | 5.3 | Seizure = abnormal electrical activity; generalized tonic-clonic features; list of causes | B | log row |
| 26 | 5.3 | Ease to floor, move objects, cushion head; do not hold down; do not put anything in mouth; "a person cannot swallow their tongue"; loosen neck clothing; side after jerking stops | S | NEEDS-HUMAN; text repeated in the Safety callout (padding) |
| 27 | 5.3 | Seizure of 5 minutes or more is an emergency; series without recovery too | B/S | procedural threshold, "5 minutes" needs a logged source |
| 28 | 5.3 | Febrile seizure in young children, first one needs assessment | B | log row |
| 29 | 5.3 Red Flags | First seizure, seizure in water, in pregnancy, patient with diabetes, injury, breathing trouble | S | log row; "a patient with diabetes" needs the reason (glucose) |
| 30 | 5.4 | Sepsis = dysregulated response to infection causing organ dysfunction; septic shock = dangerously low BP that does not recover | B | log row (Sepsis-3 / Surviving Sepsis 2026, V-003); "dysregulated" unglossed |
| 31 | 5.4 | "early recognition and treatment improve the outcome" | C | outcome claim; qualify or source |
| 32 | 5.4 | Risk groups: older adults, infants, weakened immune system, long-term illness, recent surgery or wounds, pregnancy, diabetes | B | listed twice (L138 and L152) |
| 33 | 5.4 | Warning signs: high or low temperature, fast HR/RR, new confusion, low BP, cool/mottled skin | B | log row; note low temperature is a feature |
| 34 | 5.4 | Older adults and infants may have confusion or poor feeding with little or no fever | B | log row |
| 35 | 5.4 | Early warning scores combine vital signs; service teaches its own | B | generic, no named tool; fine |
| 36 | 5.4 | First priorities include "Give oxygen as your protocol directs" and "Keep the patient warm" | D/S | oxygen is on the closed list and **the mandatory sentence is missing here**; "keep warm" in a febrile patient needs clinician view |
| 37 | 5.4 | "the medicines that treat infection and the fluids that support circulation" | D | classes named outside the closed list (outline section 1 allows only "given by trained clinicians under medical direction" unless a reader would be unsafe) |
| 38 | 5.4 | "Saying 'I am worried about sepsis' tells the team to treat the patient as time-critical" | B/C | soften to "alerts the team" |
| 39 | 5.5 | Poison definition and routes; poisonings include medicines, household products, plants, alcohol, drugs, carbon monoxide, chemicals | B | CO beyond outline section 7 (one sentence max) |
| 40 | 5.5 | Some poisons cause no signs at first and become dangerous hours later | B/S | good; log row |
| 41 | 5.5 | Poison Help line 1-800-222-1222, staffed by experts | B | **must be opened and logged**; wrong number would be a harm |
| 42 | 5.5 | Do not make the patient vomit; do not give anything to drink unless experts direct | S | standard; log row |
| 43 | 5.5 | CO: gas without smell or color from faulty heaters and engines; headache, dizziness, nausea, confusion; several people unwell at once | B | log row |
| 44 | 5.5 | "a pulse oximeter can read normally in carbon monoxide poisoning and must not be trusted" | B/S | fact-check and soften "must not be trusted" to "cannot be relied on"; ch01 L207 already says something similar (bridge, do not repeat) |
| 45 | 5.5 | Opioid overdose: slow or absent breathing, unresponsiveness, very small pupils | B | log row |
| 46 | 5.5 | Give breaths or compressions if not breathing normally, as 2.3 and 3.4 describe | S | check the order for opioid arrest (breaths matter) against 3.4 |
| 47 | 5.5 | Naloxone reverses opioid effects; use where available, trained and permitted; stay because effects can wear off before the opioid does | D/S | naloxone on closed list; mandatory sentence present; clinician clearance |
| 48 | 5.5 | Alcohol poisoning: drowsiness, vomiting, slow breathing; keep on side | B/S | log row |
| 49 | 5.6 | Causes list: bowel infection, appendicitis, gallstones, obstruction/perforation, ulcer, vessel bleed | B | log row |
| 50 | 5.6 | Upper GI bleed: vomit bright red or coffee-ground; lower: bright red or black, tarry, foul-smelling stool | B | log row |
| 51 | 5.6 | Rigid, board-like abdomen, pain worse with movement, lying still suggests an irritated lining, an emergency | B/S | log row |
| 52 | 5.6 | Appendicitis pattern: vague pain near navel moving to lower right; worse with movement or coughing; low fever | B | log row |
| 53 | 5.6 | Ectopic pregnancy in "women of child-bearing age" with missed period or vaginal bleeding | B/S | rephrase to patients who could be pregnant (inclusive language, reason stated) |
| 54 | 5.6 | Position of comfort, knees drawn up; nothing by mouth; do not give painkillers or stomach medicines unless directed; mandatory sentence present | S/D | consistent |
| 55 | 5.6 | "Record what the patient has vomited or passed and keep a sample if clinicians ask" | S | no gloves/standard-precautions reminder; add (change 10) |
| 56 | Vignette | Glucose low with clammy skin, fast breathing; sugar by protocol; recheck about 15 minutes; clearer | S/B | consistent with 5.1; call for help comes last, against 5.1 and Care Priorities (change 1) |
| 57 | Vignette | Stroke excluded because "face and arms looked symmetrical" and equal grip | S/C | models excluding stroke from two signs; contradicts 5.2 "treat ... as a stroke until a clinician shows otherwise" (change 1) |
| 58 | Review Q1 to Q8 | Answers inferred B, B, B, B, C, A, B, short | A | letter B four times (cap is three); implausible distractors (change 3) |
| 59 | Fig 19 to 22 text layers | Fig 22 reads "Oxygen as protocol directs, keep warm" | D | same oxygen/medicines sentence rule applies near the figure; add to caption area or keep with text sentence |
| 60 | All | Numerals for measurements | N | "5 minutes", "10 minutes", "15 minutes" correct; glucose in words in text and "mg/dL" abbreviation unexplained in Q2 |
| 61 | All | Terminology vs table | T | "hypoglycemia", "low blood glucose" both used as table allows; "epinephrine" absent; "heart attack" absent; "ischemic" unglossed; "drugs of misuse" is UK flavored (use "drug use") |

## 5. Human-sounding prose: findings
- "Not X, it is Y" shapes: L22 "The aim is not to name the cause at once. It is to check the causes that kill quickly and can be reversed, and to call for help." L90 "It is the time before the symptoms began, not the time you found them."
- Neat or moral endings: L72 "...is more valuable than anything else a bystander can do." L106 "the most useful thing a responder can do is also the simplest". L156 "so the main contribution of the first responder is to recognize the problem and bring the team." L194 "The safest rule is to look for features that make the pain dangerous."
- Question chain (L28): seven consecutive questions ("Is the airway open ... Is the blood pressure low?"). Reads like a quiz inside a teaching paragraph.
- Stock opener in the overview (L14 "easy to explain away") is a good human touch; keep the idea, change the word.
- Priorities lines restate the entry's First Priorities almost word for word in 5.2 (L98 vs L100), 5.3 (L110 vs L130) and 5.5 (L170 vs L188).
- Duplicates inside the Part: 5.3 L110 and L115 (no restraint, nothing in mouth, nothing to drink); 5.4 L138 and L152 (risk groups) and L140 vs Red Flags L149 (identical list).
- Triplets are mostly descriptive lists (L38, L108, L166). The one decorative run is L98 and L208, strings of eight short imperatives.
- No em dashes. No detector-style filler. Sentence variety is acceptable; the Part sounds like the voice in style-guide samples A and B.

## 6. Review Questions: letters and quality
| Q | Inferred key | Issue |
|---|---|---|
| 1 | A | options B to D ("Height", "Hair color", "Shoe size") are implausible |
| 2 | B | options 40, 120, 200 fine; "mg/dL" not defined |
| 3 | B | A "It tastes unpleasant" implausible |
| 4 | B | fine |
| 5 | C | "Put a spoon in the mouth" is implausible but tests a real myth; keep "Hold down", change others |
| 6 | A | fine; C "pink, warm, calm" too obviously normal |
| 7 | B | fine |
| 8 | short case | repeats the vignette (older man found confused at home); asks "first four things" but no model answer exists |
Letter count A 2, B 4, C 1, D 0: **B four times, D never** (rule: no letter more than three). No question on poisoning management, abdominal pain or stroke recognition (Q4 tests only the time); Entries 5.5 and 5.6 are barely tested. Questions run about 262 words against 700 planned.

## 7. REQUIRED CHANGES (old text then new text; minimal)
Line numbers refer to the current ch05.md.

1. **Vignette (S/C, blocking).** L219 old: "found Mr. Alvarez, an older man who lived alone" new: "found Walter, an older man who lived alone". L221 old: "so she did not think he was having a stroke. She asked her supervisor by phone, and was told to check his blood glucose, which was low." new: "so she saw no sign of a stroke. She phoned her supervisor, who asked for an ambulance to be sent and told her to check his blood glucose. It was low. She had also asked his daughter whether he took insulin; the daughter said he did and that he had eaten nothing that morning." L223 old: "called for help anyway, because she did not know why his glucose had dropped" new: "left the ambulance call in place, because she did not know why his glucose had dropped". (Net +45 words; the vignette reaches about 276.)
2. **Care Priorities (blocking).** Replace body L231 with (about 200 words, no entry content restated): "In medical emergencies the cause is usually unknown at the bedside, so the priorities have to work before the diagnosis does. First, protect the airway and breathing whatever the cause, because a patient who is drowsy and unexplained can still be kept safe. Second, look for the cause that is quick to check and can be reversed, and do that before the causes that only a hospital can sort out. Third, treat the change over time as more important than any single reading: write each observation with its time, because the trend is the part the receiving team cannot see for themselves. Give weight to what family or carers say is different from usual, since a confused patient cannot report their own baseline. When the story changes, start again from the airway. Any time that arrives with the patient, such as the start of symptoms, the last time anyone saw the patient well or the last meal, belongs on paper before you leave the bedside. Finally, an unexplained patient who has become quiet is not a settled patient, so keep rechecking, keep them where you can see them, and ask for help while the patient can still talk to you."
3. **Review Questions and answer key (blocking).** Replace L237 to L279 with the set below (letters B, D, A, C, B, D, A; B twice, D twice, A twice, C once) and write back/answer-keys-part5.md.
   1. A patient is newly confused, sweaty and cool, and your role allows you to check blood glucose. Why is the glucose checked early? A) The reading decides whether you call for help. B) Low blood glucose is a common cause that can be reversed within minutes. C) Confusion is always caused by a glucose problem. D) The airway cannot be assessed until the glucose is known.
   2. A man with diabetes is shaky and sweating. He is awake, sits up and swallows normally. His reading is low. Which action fits Entry 5.1? A) Lay him flat and give nothing by mouth. B) Wait for the ambulance before doing anything. C) Give plain water and recheck in an hour. D) Give the fast-acting sugar your protocol names, then recheck the reading after about 15 minutes.
   3. A woman wakes with a drooping face and a weak left arm. Which time matters most to the receiving team? A) The last time she was known to be well. B) The time you arrived. C) The time she told someone. D) The time the call was connected.
   4. Why should a responder not give aspirin to a patient with a suspected stroke unless medical direction says so? A) It works too slowly to help. B) It hides the facial droop. C) Some strokes are caused by bleeding, and aspirin could make bleeding worse. D) It is used only for chest pain.
   5. A woman has a generalized seizure on a gym floor. Which action is correct? A) Hold her arms and legs still. B) Cushion her head, move hard objects away and note the time. C) Place a folded cloth between her teeth. D) Pour water on her face.
   6. Which patient should be treated as possible sepsis? A) A patient with a mild cough, normal breathing and normal alertness. B) A patient with a sprained wrist and a fast heart rate from pain. C) A patient with a headache that eased after a drink of water. D) A patient with a skin infection who is newly drowsy, breathing fast, with cool, mottled skin.
   7. An adult is found unresponsive with slow, shallow breathing and very small pupils. Which first step is correct? A) Make the scene safe, call emergency services, support breathing and, if your role allows and a device is available, use naloxone as directed. B) Make the patient vomit. C) Give a drink of water to wake the patient. D) Let the patient sleep and recheck in an hour.
   8. Short case. A 70-year-old woman has had severe belly pain for 3 hours. She lies very still, her abdomen is rigid, and her skin is cool and pale with a fast pulse. List, in order, the first four things you would do.
   Answer key text for back/answer-keys-part5.md: 1 B (low blood glucose is a reversible cause that can be checked in minutes). 2 D (swallowing is the safety check; recheck shows whether treatment worked). 3 A (treatment windows run from the last time the patient was well, not from when the symptoms were found). 4 C (some strokes are bleeds). 5 B (protect the head, do not restrain, note the time). 6 D (infection plus new confusion, fast breathing and poor circulation). 7 A (opioid overdose pattern; naloxone only within role and medical direction). 8 Model answer: (1) make the scene safe and call for help early, saying you suspect a serious abdominal emergency and possible bleeding; (2) check airway, breathing and circulation; (3) let her find the position of comfort, often on her side with knees drawn up, and give nothing by mouth because she may need surgery or vomit; (4) take a full set of vital signs with the times, watch for shock, keep her warm and record what you see. Painkillers or stomach medicines are given only if medical direction directs.
4. **Entry 5.2 expansion (UNDER-FLOOR, about +330 words; clinician items marked).**
   a. L72 old: "so recognizing a stroke quickly and calling for help is more valuable than anything else a bystander can do." new: "so recognizing a stroke quickly and calling for help is the most useful thing a bystander can do."
   b. L80 old: "A short screening tool checks the face, arms and speech and asks the time." new: "A short screening tool checks the face, arms and speech and asks the time. One widely taught version is FAST, for Face, Arm, Speech and Time. Some versions add Balance and Eyes (BE-FAST), because a stroke in the back of the brain can cause sudden dizziness, loss of balance or loss of vision without a drooping face." (fact-check the tool names and the added letters before use.)
   c. After the Recognition paragraph add a Remember callout (35 words): "FAST: Face drooping, Arm weakness, Speech trouble, Time. The T is a reminder to call at once and to record when the symptoms began or when the patient was last known to be well."
   d. After L86 (Conditions That Look Like Stroke) add: "[Two Kinds of Stroke.] A clot and a bleed need opposite treatments, which is why a scan must come first and why you do not give a medicine that affects clotting on your own judgment. You cannot tell the two apart at the bedside. A bleed more often starts with a sudden severe headache, vomiting or a rapid fall in alertness, but a clot can look the same. Both need the same response from you: call, protect the airway and write down the times." (about 90 words; clinician and fact-check.)
   e. Replace L90 sentences "The single most useful fact ... not the time you found them." with: "The most useful fact you can give the receiving team is the last time anyone saw the patient well." and add after it: "[Waking With Symptoms.] A patient who wakes with symptoms was last known well at bedtime, not at waking. The same applies to someone found on the floor: count from the last time anyone saw them well, and ask family, neighbors or carers when that was. Write down how you know, because the receiving team will ask how the time was worked out." (about 70 words.)
   f. L98 old: "Keep the patient lying with the head slightly raised if they are comfortable, or on their side if drowsy." new: "Let the patient rest in the position of greatest comfort, or on their side if drowsy." (head-position advice is for the clinician to restore if verified). Add at the end of the glucose sentence: "but do not let the glucose check delay the call."
   g. L100 old: "Screen quickly, call early, record the last known well time, check glucose, protect the airway, and give nothing by mouth." new: "Screen with a stroke tool, call early, and hand over the last known well time."
5. **Entry 5.4 repair and expansion (about +140 words net).**
   a. L136 old: "and early recognition and treatment improve the outcome." new: "and the earlier it is recognized, the sooner treatment can start."
   b. L138 old: "Sepsis occurs when the response to an infection becomes dysregulated and begins to cause organ dysfunction." new: "Sepsis occurs when the body's response to an infection goes out of control and begins to damage its own organs."
   c. Delete L152 "[Who Is Most at Risk.]" first two sentences (the list repeats L138); keep only: "A patient who has had an infection and then becomes more unwell rather than better should be assessed again."
   d. Replace L154 "[Handover Words.]" with: "[Handover.] Entry 1.5 set out the structured handover. For sepsis, make sure it includes the suspected source of infection, the vital signs with their times, any new confusion, and the word sepsis."
   e. Add after L140: "[Why Screening Uses Several Signs.] No single sign proves sepsis, and a normal temperature does not exclude it. A fast heart rate, a fast breathing rate or a fever each occur in many harmless illnesses, so services screen for a combination and for change, often by adding the signs into an early warning score. A score is a prompt to call for help and is not a diagnosis. Entry 1.4 gave typical resting values; here the question is whether the numbers are moving in the wrong direction between sets." (about 85 words; fact-check against V-003.)
   f. Add after the screening paragraph: "[Septic Shock.] Entry 3.5 explained shock from widened vessels. In sepsis the vessels both widen and leak, so the circulation is short of volume although no blood has been lost, and the blood pressure falls. Early on the skin may be warm and flushed; later it turns cool and mottled. A patient who is cool, mottled and newly confused is deteriorating." (about 60 words; clinician.)
   g. L156 old: "Give oxygen as your protocol directs. Keep the patient warm. Treatment, including the medicines that treat infection and the fluids that support circulation, is given by trained clinicians and should begin as early as possible, so the main contribution of the first responder is to recognize the problem and bring the team." new: "Give oxygen as your protocol directs. Giving medicines is outside many roles; follow your scope and medical direction. Treatment is given by trained clinicians under medical direction, so your part is to recognize the problem, record the times and bring the team."
   h. L154 old (if kept): "Saying 'I am worried about sepsis' tells the team to treat the patient as time-critical." new: "Saying 'I am worried about sepsis' alerts the team."
6. **Entry 5.1 repairs (S, blocking).**
   a. L14 old: "a change that is easy to explain away" new: "a change that is easily explained away".
   b. L22 old: "The aim is not to name the cause at once. It is to check the causes that kill quickly and can be reversed, and to call for help." new: "The aim is to check the causes that kill quickly and can be reversed, and to call for help while you do."
   c. L28: turn the question chain into a statement: "Work through a short list: the airway and oxygen supply, the blood glucose, signs of stroke, head injury, infection, poisoning or a recent seizure, extreme heat or cold, and low blood pressure." Keep the cross-reference sentence.
   d. L38 old: "it is the cause that is quickest to check and easiest to treat" new: "it is the cause that is quickest to check and quickest to reverse". Replace the repeated threshold sentence with a bridge and keep one authoritative home: old "For many people with diabetes, a reading below 70 milligrams per deciliter (3.9 millimoles per liter) is low, though the level that counts as low differs from person to person." new "Entry 1.3 gave the usual low reading, 70 milligrams per deciliter (mg/dL) or 3.9 millimoles per liter, which differs from person to person." (saves a repeat and defines mg/dL for Q2.)
   e. Add after L38: "A high reading can also cause drowsiness. A person with diabetes who is very unwell with deep, fast breathing, thirst and vomiting may have diabetic ketoacidosis, so report any high reading and call for help." (clinician check.) Add: "Slow breathing, very small pupils and unresponsiveness suggest an opioid overdose, which Entry 5.5 covers."
   f. L57 Safety old: "Place a patient who is unconscious but breathing in the recovery position, call for help, and wait." new: "Place a patient who is unconscious but breathing in the recovery position (Entry 2.2), call for help, and stay with the patient."
   g. L64 old: "an unnecessary second dose of sugar" new: "an unnecessary second portion of sugar".
   h. After L64 add a Red Flags callout (42 words): "A patient who is hard to wake or cannot follow commands, new confusion with a very fast or slow pulse, a seizure, signs of stroke, a head injury, slow breathing, or a low glucose reading that does not improve. Call emergency services at once."
   i. L66 old: "Check airway, breathing and glucose early, treat a conscious patient who can swallow as protocol directs, give nothing by mouth to a patient who cannot swallow, and call for help for any patient whose cause is not clear." new: "Check airway, breathing and glucose early, and call for help for any patient whose cause is not clear." See also add "Entry 2.2 (recovery position); Entry 5.2 (stroke screen)".
7. **Figure pointers (recurring fault).** L30 old "Figure 19 sets out the approach as a flow." new "Figure 19 sets out the approach as a flow; notice that airway, breathing and glucose come before the search for other causes." L76 old "Figure 20 shows the main arteries that supply the brain." new "Figure 20 shows the main arteries that supply the brain; notice that the front, middle and rear regions serve different parts, which is why different strokes cause different signs." (check against image). L82 old "Figure 21 shows the signs on a face and on the arms." new "Figure 21 shows the signs on a face and on the arms; notice the droop on one side of the face and the arm that drifts lower." L142 old "Figure 22 shows the pathway from suspicion to action." new "Figure 22 shows the pathway from suspicion to action; notice that any one warning sign is enough to reach the call for help."
8. **Entry 5.3 (about +90 words, duplicates removed).** L110: delete "Do not hold the patient down, and do not put anything in their mouth; a person cannot swallow their tongue." (Safety callout carries it) and add the bridge "Entry 2.2 described the recovery position." after "Turn them onto their side as soon as the jerking stops". Add before L118: "[What to Watch.] Notice what the clinicians cannot: which part of the body moved first, whether the eyes turned to one side, how long it lasted, whether the patient answered during it, and how long the drowsiness lasted. Not every seizure convulses. If a patient stares, makes chewing movements or wanders, stay close, guide them away from hazards, do not restrain them, and speak calmly. Tell the dispatcher what you saw." (about 75 words.) L130 Priorities old: "Note the time, protect the patient, turn them onto their side afterward, check breathing and glucose, and call for help for any red flag." new: "Note the time, protect the patient, and call for help for any red flag."
9. **Entry 5.5.** Trim L172 to two sentences about CO: "Carbon monoxide, a gas without smell or color from faulty heaters and engines, causes headache, dizziness and confusion, and several people in one space may feel unwell at once. Get everyone into fresh air and call for help; Entry 1.4 noted that a pulse oximeter can read normally in this poisoning." (satisfies outline section 7: one sentence of its own plus the bridge). L172 old: "must not be trusted" is deleted by this. Replace "drugs of misuse" (L164, L172) with "drug use". L186 add after Red Flags: nothing. Add (optional, +55 words, fact-check first): "[Skin and Eye Contact.] If a chemical is on the skin or in the eyes, remove contaminated clothing if you can do so safely and flush with plenty of clean water while you call the Poison Help line or emergency services. Wear gloves." L188 Priorities old: "Protect yourself, remove the patient from exposure, call emergency services and the Poison Help line, gather the container, support airway and breathing, and stay with the patient." new: "Protect yourself, call early, gather the container, and support airway and breathing."
10. **Entry 5.6.** L206 old: "In women of child-bearing age, abdominal pain with a missed period or vaginal bleeding may mean an ectopic pregnancy" new: "In any patient who could be pregnant, abdominal pain with a missed period or vaginal bleeding may mean an ectopic pregnancy". L208 old: "Record what the patient has vomited or passed and keep a sample if the clinicians ask." new: "Wear gloves, record what the patient has vomited or passed, and keep a sample if the clinicians ask." L212 See also: keep "Entry 4.1 (abdominal injury)" (4.1 covers hidden abdominal bleeding); keep "Entry 6.4 (older adults)" only if Part 6 change 5 adds the abdominal sentence to 6.4, otherwise delete it.
11. **Cross-reference alignment.** 5.2 See also lists "Entry 6.4 (older adults)", and 6.4 has no stroke text; Part 6 change 5 supplies it. Confirm 5.4 See also to 6.1 once Part 6 change 4h adds a sepsis sentence.
12. **Fact-check gate.** Add rows P5-001 and onward to verification-log.md for every B, D and S item in section 4, especially items 9, 17, 21, 27, 41, 44, 47 and 57. No Part 5 text should ship while those rows are empty.

Expected length after changes (measured on my drafted text where I drafted it): current 4,550 + Care Priorities +92 (108 to about 200) + Review Questions +200 (262 to about 462) + 5.2 about +330 + 5.4 about +140 net + 5.3 about +90 + 5.1 about +20 net + 5.5 about +30 net + vignette +45 = about 5,500 by wc (about 5,430 stripped). That clears the floor (5,000), sits on the 5,400 target and stays under the 6,000 ceiling; if the writer drops the optional skin and eye paragraph (change 9) and the septic shock paragraph (5f), the Part still lands at about 5,380. Where genuine new substance goes: 5.2 (clot vs bleed, wake-up onset, FAST/BE-FAST), 5.4 (several-sign screening, septic shock mechanism), 5.3 (what to watch, non-convulsive seizures), 5.1 (high glucose and opioid causes), Care Priorities and Review Questions. None is padding.

## 8. Items for the fact-checker (not for editing)
Stroke screen names (FAST, BE-FAST) and whether the 5.2 recognition list matches them; head-position advice for suspected stroke; aspirin and stroke wording against 3.2; whether the 5.2 time-window claim stays general; "5 minutes" seizure threshold and the seizure first-aid list (do not restrain, nothing in the mouth, side after jerking); febrile seizure first-seizure advice; sepsis definition and the 2026 screening position (V-003); whether early warm skin then cool skin is an acceptable simplification; "keep the patient warm" in sepsis; oxygen and sepsis; Poison Help number 1-800-222-1222 and its US scope; CO and pulse oximetry; "do not make the patient vomit"; naloxone wearing off before the opioid; order of breaths and compressions for opioid arrest; skin and eye flush advice (if added); abdominal signs (rigid abdomen, coffee-ground vomit, tarry stool); 15 minute glucose recheck and 70 mg/dL (3.9 mmol/L); DKA features (if added).

## 9. Reader test
- First page: concrete and calm, the "easy to explain away" opening works; the roadmap paragraph is mechanical but short.
- Middle (5.2): the Major entry reads thinner than 5.1; a student could not name the stroke screen from the text alone.
- Last page: Care Priorities repeats what the entries already said and the questions are easy to guess; no hook to Part 6.

## 10. Verdict
**REVISE.** Blocking: 1 (name and call order in vignette), 2 (Care Priorities), 3 (questions and missing answer key), 4 and 5 (under-floor entries), 6 (5.1 Red Flags, "and wait", DKA and opioid bridges). Unlogged B, D and S items remain until the fact-check rows exist.
