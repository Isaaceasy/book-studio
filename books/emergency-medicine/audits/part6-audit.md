# Part 6 editorial and clinical audit: Special Populations, Behavioral Emergencies and Safety (chapters/ch06.md)

Date 2026-10-29. Auditor: independent editor. ch06.md NOT edited. Verdict: **REVISE** (blocking: changes 1 to 4; UNDER-FLOOR by 165 words).

I did not open external sources and I do not judge accuracy; risky claims are listed in section 8 for the fact-checker. verification-log.md has zero Part 6 rows (grep "P6-" = 0), so every B, D and S item below is unlogged until the parallel fact-check writes its rows. I read the text layers of Figures 23, 24 and 25 (labels only: Fig 24 "Child | Adult", Fig 25 "Left side down, supported with a rolled blanket"); I could not view the raster images, so pointer wording that depends on the image is marked "check against image". status.md records that Figure 25 was MIRRORED in the SVG so that the patient lies on her LEFT; a clinician must confirm the side before print.

## 1. Mechanical results
| Check | Result |
|---|---|
| Words, whole file (wc -w) | 4,903 |
| Table cells (1 table, 68 words incl. header) | excluded |
| Words net of table | 4,835 (4,749 with markup stripped) |
| Target / floor / ceiling | target 5,650, floor 5,000, ceiling 6,000 |
| **UNDER-FLOOR** | **165 words short of the floor by wc net (251 by stripped count); 815 short of the 5,650 target** |
| Per-section words vs outline budget | Title + objectives + overview 287 vs 250; 6.1 941 vs 1,100 (-14%; table excluded); 6.2 784 vs 800; 6.3 612 vs 650; 6.4 598 vs 600; 6.5 603 vs 650; 6.6 383 vs 400; Illustrative Case 190 vs 250 (-24%); Care Priorities 90 vs 250 (-64%); Review Questions 325 vs about 700 (-54%) |
| Sentences | 336 (includes review options); average 13.9 words; 21 over 30 words (6.2%); longest 45 (L32, Work of Breathing); six sentences of 40 or more are lists (L80 x2, L131, L217 x2, L32) |
| Repeated openers | "A" 26, "Do" 14, "Entry" 12, "The" 11, "In" 9, "What" 7, "If" 7. **L58 is five consecutive sentences opening "Entry N described/covered/covers ..."** (a run of three or more) |
| Em dashes / en dashes | 0 / 0 |
| Banned or flagged words | "lifesaving" L165 (style guide bans "life-saving" as marketing); "always" L18 ("As always"), L281 (distractor "It always means dementia"; acceptable inside a wrong option, but change anyway); "just" L84 ("just enough to make the chest rise"); "ageing" L157 and L279 (British spelling; US "aging"); "simple" L36, L193 (not banned, but the style guide dislikes "simply/easy"; leave). "vital" L133, L189 are "vital sign(s)" (legitimate). No commonest, never, easy, simply, crucial, golden hour, ER, delve, moreover, furthermore, additionally |
| URLs, links, citations, footnotes | None. "988" and "911" in running text (L195) are fact-check items. No brand, course or organization names |
| Placeholders | None. Files ch06-fig23..25.svg exist |
| Callout words (20 to 60) | Red Flags 6.1 41, 6.3 37, 6.4 45, 6.6 38; Scope Note 6.1 41; Safety 6.2 33, 6.5 38. All in range |
| Remember callouts | None in Part 6 (limit met) |
| Headings | One H1; H2 entries 6.1 to 6.6 with exactly the outline titles and order; Illustrative Case, Care Priorities, Review Questions follow |
| Answer key | back/answer-keys-part6.md DOES NOT EXIST; letters below inferred from the text |
| verification-log.md | zero Part 6 rows |
| Table | 1 table (Typical resting ranges in children), caption begins "Table:" like ch01 to ch03. **No sentence in the text points to it** |
| Repetition vs Parts 1 to 5 | no re-teaching of the adult choking steps (L82 bridges to Entry 2.2 and adds only force); 6.5 L185 reuses the reversible-cause list of Entry 5.1 but only as a pointer. Within the Part: L185 and L187 list the same physical causes twice |

## 2. Structure against outline
- Entries 6.1 to 6.6 present in order with outline titles. Objectives 1 to 6 match the outline.
- Figures: captions begin "Figure 23." to "Figure 25.", numbers match the outline (23 to 25), each caption is one sentence. Each has an in-text pointer before it (L26, L42, L127), **but all three are bare one-liners that do not say what to notice** (recurring fault; change 10). The table has no pointer.
- Procedure pattern against the Scope Lock list (outline section 1: "infant and child choking relief, rescue breathing and CPR differences (6.2)" and "left-lateral positioning (6.3)"):
  | Procedure | Purpose | Scope | Steps | Safety | Stop line | Why prose |
  |---|---|---|---|---|---|---|
  | 6.2 infant choking (L80) | **MISSING** | **MISSING** | **none (prose, 5 sentences)** | shared box mentions abdominal thrusts only | **MISSING** | **MISSING** |
  | 6.2 child choking (L82) | n/a | bridges to 2.2 | n/a | n/a | n/a | n/a (acceptable as a bridge) |
  | 6.2 rescue breathing (L84) | **MISSING** | **MISSING** | **none (prose)** | **MISSING** | **MISSING** | **MISSING** |
  | 6.2 CPR infant or child | yes | yes | 8 | yes (but item 1 belongs to choking) | yes | yes (L111) |
  | 6.3 left-lateral positioning | **MISSING** | **MISSING** | **none (prose, L125)** | **MISSING** | **MISSING** | partial (mechanism stated, no steps) |
  | 6.3 imminent birth (L139) | n/a, not a Scope Lock procedure but it gives actions | | | | | Red Flags present |
  Three of four Scope Lock procedures lack the fixed pattern. This is the same fault Part 2 had for choking and is blocking.
- Nursing and Responder Priorities and See also present in all six entries.
- Emergency-feature passage: Red Flags in 6.1, 6.3, 6.4, 6.6; 6.2 has a Stop line only (acceptable with procedures); **6.5 (suicide, weapons) has a Safety callout and a Stop line but no Red Flags callout** (change 7).
- Safety callout: present in 6.2 and 6.5; **6.6 has none although acting wrongly (confronting, questioning in front of the suspected abuser) could harm the patient**; 6.3 has none and needs one for the positioning procedure and CPR in pregnancy.
- Scope Note: 6.1 only; good use.
- Bridges and outline map items:
  | Required (outline section 9 and inbound See also pointers) | In ch06? |
  |---|---|
  | 6.1 child-specific ABCDE sequence and findings | partial: appearance, breathing, skin, no child Disability or glucose cues |
  | 6.1 pediatric acuity cues (1.2 to 6.1, ch01 L112 points here) | **missing** |
  | 6.1 child values (1.4 to 6.1, ch01 L223) | yes, table |
  | 6.1 child airway differences (2.1 to 6.1) | yes (L40, Fig 24) |
  | 6.1 child BVM sizing and rate cues (ch02 L183 points here) | **missing**; the Scope Note says sizing is outside the book. Either change the ch02 pointer to 6.2 (rate is in 6.2) or add one sentence |
  | 6.1 anaphylaxis in children (ch02 L219) | **missing** |
  | 6.1 asthma in children | yes (L58) |
  | 6.1 hypoglycemia cues | yes (L58) |
  | 6.1 febrile seizure | yes (L58) |
  | 6.1 tourniquet in children (ch04 L109) | present but empty: "the same limits apply" (L58) |
  | 6.1 spinal motion restriction in children (ch04 L151) | **missing** |
  | 6.1 fractures in children (ch04 L200 points here) | **missing** |
  | 6.1 burns in children (ch04 L230) | **missing** |
  | 6.1 abuse (one sentence) | yes |
  | 6.1 sepsis in children (5.4 See also) | **missing** |
  | 6.2 child and infant CPR and AED adaptations only (3.4) | yes; AED child pads in step 7 |
  | 6.3 CPR adaptation in pregnancy (3.4 L168 says "Entry 6.3 describes the adaptation") | **weak**: L137 says the adaptation "is taught in advanced courses", which does not describe it |
  | 6.4 chest pain in older adults and women (ch03 L73 points here, home 3.2) | **one vague sentence** (L155) with no new angle |
  | 6.4 sepsis in older adults | yes, one sentence (L155) |
  | 6.4 heat and cold differences (4.6 home) | thin (L167, 2 sentences) |
  | 6.4 and 5.2 stroke / 5.6 abdominal pain (See also from Part 5) | **missing in 6.4** |
- Vignette: labelled, past tense, 190 words (vs 250), no institution named ("an emergency department triage area" is generic). First names only. Care Priorities present (90 words).
- Review Questions: 8 present (7 MCQ + 1 short case).

## 3. Scores (1 to 5)
| Area | Score | Reason |
|---|---|---|
| Promise and structure | 2 | three of four Scope Lock procedures lack the pattern; no Red Flags in 6.5; no Safety in 6.6 and 6.3 |
| Substance at length | 3 | 165 under the floor; Care Priorities, vignette and questions are all well under budget; 6.1 has five empty pointer sentences |
| Clarity and readability | 4 | average 13.9, plain, short paragraphs |
| Voice consistency | 4 | calm and respectful; "lifesaving", "ageing", "just" drift; "mother" used where "patient" is safer |
| Specificity and examples | 3 | table has no pointer and overlapping bands; "very young infant" undefined; "the same limits apply" says nothing |
| Teaching quality | 3 | pregnancy CPR deferred rather than taught; left-lateral position lacks steps and a CPR exception; step 2 of child CPR contradicts L115 |
| Human-sounding prose | 3 | "not X, it is Y" at L157; stock opener "hidden in plain sight" (L213); five-sentence "Entry N described" run (L58); neat close in Care Priorities |
| Consistency | 2 | six inbound See also pointers to 6.1 and 6.4 not delivered; "ageing"; all seven keys are B; Fig 25 side to confirm |
| Chapter ending | 2 | Care Priorities is generic and 90 words; all answers B; Q8 repeats the vignette; no answer key |

## 4. Audit table (classes A/B/C/D/S/N/T)
| # | Location | Claim / item | Class | Status / note |
|---|---|---|---|---|
| 1 | 6.1 | Children compensate longer and then fail faster | B | log row |
| 2 | 6.1 | Pediatric assessment = appearance, work of breathing, circulation to skin; hands-off; done from the doorway | B | log row (pediatric assessment triangle); tool name not used in text, fine |
| 3 | 6.1 | Appearance cues: alert, consolable, eye contact, strong cry, normal movement; limp, glassy-eyed, hard to wake = seriously unwell | B/S | log row |
| 4 | 6.1 | Work-of-breathing signs: nostril flaring, grunting, retractions, tripod position | B | log row |
| 5 | 6.1 | Skin: pale, mottled, blue suggests poor circulation or oxygen | B | log row |
| 6 | 6.1 | Dehydration signs (dry mouth, no tears, few wet diapers, sunken eyes, sunken soft spot, drowsiness, fast breathing) | B | log row |
| 7 | 6.1 | Drowsy, cool, mottled child with fast breathing is in shock | B/S | log row |
| 8 | 6.1 | Large head: neck bends forward when flat; small pad under shoulders may be needed | B/S | clinician; age cut-off not stated |
| 9 | 6.1 table | Breathing rate: infant 30 to 53, toddler 22 to 37, preschool 20 to 28, school 18 to 25, adolescent 12 to 20 a minute | B | **looks like one source family for rates and a different one for heart rates**; log both; units "a minute" vs bible "breaths per minute" (N) |
| 10 | 6.1 table | Heart rate awake: infant 100 to 160, toddler 90 to 150, preschool 80 to 140, school 70 to 120, adolescent 60 to 100 | B | the same bands are sometimes given with different upper limits; confirm source |
| 11 | 6.1 table | Age bands "Toddler (1 to 3 years)" and "Preschool (3 to 5 years)" overlap at 3; "School age (6 to 11)" leaves age 5 to 6 unassigned | C | fix after the source is chosen (change 5) |
| 12 | 6.1 table | Caption says "(reference copy)" but 6.1 is the HOME of child values; outline says Appendix C is the permitted reference copy | T/consistency | remove the label here (change 5) |
| 13 | 6.1 | Children may keep normal BP until close to collapse; fast HR and slow capillary refill are earlier signs | B/S | log row; "capillary refill" not bridged to 1.3 |
| 14 | 6.1 | Falling heart rate with sleepiness and stopped struggling is late and serious | B/S | log row |
| 15 | 6.1 | Fever is not itself a danger sign; fever with stiff neck, non-fading rash, lethargy or poor feeding needs urgent care | B/S | log row |
| 16 | 6.1 Red Flags | "a fever in a very young infant" | C | undefined age; state the age limit the source gives (for example "under about 3 months") |
| 17 | 6.1 | Low glucose more common in small children who are ill; glucose check for any drowsy child | B | log row; cross-check with 5.1 |
| 18 | 6.1 | Tourniquet: "the same limits apply" | C | empty claim; replace (change 5) |
| 19 | 6.1 Scope Note | Equipment and medicine amounts sized by weight and age are outside the book | S | good; consistent with dosing rule. "medicine amounts" is acceptable here |
| 20 | 6.2 | Infant under 1 year; child from 1 year to puberty | B | log row (AHA age definitions) |
| 21 | 6.2 | Infant choking: no abdominal thrusts; back blows (up to 5) with head lower than chest, then up to 5 chest thrusts with 2 fingers on lower half of breastbone; alternate | S/B | NEEDS-HUMAN; guidance differs between organizations; procedure pattern missing (change 1) |
| 22 | 6.2 | Child choking: abdominal thrusts with force suited to size; unresponsive to ground, call, CPR | S/B | NEEDS-HUMAN |
| 23 | 6.2 | Rescue breathing: 1 breath every 2 to 3 seconds for child and infant | B/S | procedural parameter; needs a logged source and clearance; "about" phrasing fine |
| 24 | 6.2 CPR | Alone: 2 minutes of CPR first, then call and fetch an AED; with phone speaker, call while starting | B/S | **guidance may have changed in 2025**; fact-check against current pediatric BLS. Internal conflict between step 2 and L115 (change 1) |
| 25 | 6.2 CPR | Breathing check for no more than 10 seconds | B | log row |
| 26 | 6.2 CPR | Child: heel of one hand on lower half of breastbone; infant: two fingers or two thumbs | B/S | for the 2-thumb technique the usual form is two rescuers and encircling hands; clinician |
| 27 | 6.2 CPR | Depth about one third of chest depth; 100 to 120 a minute | B/S | procedural parameter; log; numeral/fraction wording (N) |
| 28 | 6.2 CPR | 30:2 single rescuer, 15:2 two rescuers | B/S | log row |
| 29 | 6.2 CPR | AED with child pads or child setting if available | B/S | what to do when only adult pads exist is not stated (S gap); clinician |
| 30 | 6.2 Safety | Do not press on belly or soft part of neck; do not tilt a child's head back as far as an adult's | S | NEEDS-HUMAN |
| 31 | 6.2 | Children most often stop breathing before their hearts stop; early breaths and oxygen matter more | B | log row |
| 32 | 6.2 | Choking prevention: small objects, round foods, balloons | B | log row |
| 33 | 6.3 | Late pregnancy: uterus presses on the large vessel returning blood when flat on back; place on left side or tilt left with pillow/rolled blanket under right hip | B/S | clinician; **no exception for CPR or suspected spine injury** (change 2) |
| 34 | 6.3 | Call for help: vaginal bleeding, severe abdominal pain, severe headache, vision changes, face and hand swelling, seizure, reduced fetal movements, fall or injury, fluid loss | B/S | log row |
| 35 | 6.3 | "a dangerous high blood pressure condition" | B/T | unnamed; name and gloss (change 2) |
| 36 | 6.3 | Blood volume rises, resting heart rate higher, so a pregnant patient can lose much blood before signs of shock | B/S | log row |
| 37 | 6.3 | BP often a little lower in the middle months | B | log row |
| 38 | 6.3 | Any injury needs assessment even if she feels well; seat belt use to be asked | B/S | log row |
| 39 | 6.3 | CPR in advanced pregnancy: same compressions, uterus moved gently to the left by hand if protocol directs | B/S | clinician; described only as "taught in advanced courses" (change 2) |
| 40 | 6.3 | Imminent birth signs: urge to push, crowning, contractions very close; call; do not delay birth; support head as it emerges; do not pull on baby or cord; dry, warm skin to skin, check breathing; do not cut the cord unless trained and protocol directs | S | **"supporting the head gently" borders on a delivery maneuver, which outline section 7 excludes**; clinician decision. Cord prolapse appears only in Red Flags |
| 41 | 6.4 | Older adults: less reserve, atypical heart attack without chest pain, infection with confusion and no fever, fall may bleed in skull with little pain | B | log row |
| 42 | 6.4 | A medicine that slows the heart may hide a fast pulse | B | log row (class mention only; no drug named) |
| 43 | 6.4 | New confusion "is called delirium" | B/T | simplification; fine if worded "often called" (change 6) |
| 44 | 6.4 | Falls: ask about blackout, head strike, blood-thinning medicines | B/S | log row |
| 45 | 6.4 | Do not stop or change any medicine yourself | S | good, matches style guide |
| 46 | 6.4 | Pressure sores, thin skin; long lie leaves patient cold, dehydrated, weak | B | log row |
| 47 | 6.4 | Written wishes about resuscitation; do not delay "lifesaving care" while searching for a document unless protocol directs | S/B | legal and clinical item; wording banned; clinician and state-law note (change 6) |
| 48 | 6.5 | Behavioral emergency definition; physical causes can mimic | B | log row |
| 49 | 6.5 | Panic attack symptoms overlap with heart attack and asthma; do not assume anxiety | S | good safety message; log row |
| 50 | 6.5 | Scene safety: weapons, exits, distance, do not stand between patient and door; leave if threatened | S | log row; consistent with Stop line |
| 51 | 6.5 | Book does not teach restraint; restraint carries serious risks | S | matches outline |
| 52 | 6.5 | De-escalation techniques | B | log row (general good practice) |
| 53 | 6.5 | "Asking does not put the idea into someone's head" | B/S | safe-messaging claim; log row |
| 54 | 6.5 | "died by suicide" wording; avoid blaming or glamorizing | S | matches safe-messaging rule; clinician |
| 55 | 6.5 | Do not leave the person alone; remove means if safe; 988 call or text; 911 for immediate danger | B/S | **988 service details must be opened and logged**; "remove means" needs clinician view |
| 56 | 6.5 Safety | Do not argue with, shame or promise secrecy; do not leave person who may self-harm; leave scene if unsafe | S | consistent |
| 57 | 6.6 | Abuse and neglect definitions; affects every age, sex, background | B | log row |
| 58 | 6.6 | Signs: injuries do not fit story, story changes, delay, injuries at different healing stages, fear; infant bruising when not mobile; bruises in unusual places; burns with clear outlines; poor hygiene or untreated illness in children; pressure sores, dehydration, poor nutrition, carer who answers every question | B/S | log row; phrase "bruises in unusual places" needs a site or source |
| 59 | 6.6 | Treat injuries first; speak to patient privately; record in their own words; do not confront the suspected abuser | S | privately "if you can do so safely" is missing; no Safety callout (change 8) |
| 60 | 6.6 | Mandatory reporting duties for children and vulnerable adults in many places; differ by state and role; you do not need proof | B/S | log row; keep "in general terms" |
| 61 | Vignette | Toddler with fever, not feeding, retractions, slow capillary refill, many hours since last wet diaper, moved forward | S/B | consistent with 6.1; fine |
| 62 | Vignette | Both the vignette and Q8 describe a hot, drowsy, fast-breathing toddler | consistency | Q8 repeats the vignette (change 4) |
| 63 | RQ 1 to 8 | Answers inferred B, B, B, B, B, B, B, short | A | **every MCQ key is B** (cap three); several implausible distractors (change 4) |
| 64 | All | Numerals | N | steps use "2 breaths" and "two rescuers" and "two fingers or two thumbs" in the same lists (L94 to L96); "one third" (fraction, L95); fix to numerals within steps (change 11) |
| 65 | All | Terminology vs table | T | "ageing" (US "aging"); "breathing rate" in the table header is accepted, but units should read "breaths per minute"; AED/CPR first appear in 6.2 after 3.4 (fine, defined there) |

## 5. Human-sounding prose: findings
- "Not X, it is Y": L157 "New confusion is not a normal part of ageing. It is called delirium and is a sign of illness". L22 "A child who is breathing hard and still playful is in a very different place from..." is fine (a contrast, not a tic).
- Stock or moral lines: L213 "Abuse and neglect are hidden in plain sight." and "Recognizing the signs and acting properly can protect a child, an older adult or a partner who cannot ask for help." L123 "two lives in the balance, and the best care for the baby is good care of the mother" repeats the overview's "two lives to protect" (L14). L153 "what changes is how much weight you give to the vague complaint, the quiet patient and the small change." L248 "In every case, record facts, tell the people who need to know, and stay with the patient until help takes over." (generic sign-off, rule of three).
- Run of identical openers: L58 (five sentences "Entry N described/covered/covers") and L58 content: "the same limits apply" is empty.
- Lists of exactly three: L14 "a child ... a pregnant patient ... an older adult" is descriptive and fine; L153, L248 are decorative.
- Priorities lines are chains of 5 to 6 verbs and restate the entry: L72, L117, L147, L177, L207, L227. Shorten as in change 12.
- Clumsy sentence L40: "Their breathing rate is higher, and their heart rate is higher, and both vary by age." and the displaced "Entry 2.2 described the positions for adults." inside the same paragraph.
- Sex/gender wording: 6.3 uses "mother" and "her" throughout (L125 to L139). Use "the patient" where the sentence can bear it and say pregnancy is the reason when sex is mentioned (style guide). Not blocking.
- No em dashes; voice otherwise matches style-guide samples A and B.

## 6. Review Questions: letters and quality
| Q | Inferred key | Issue |
|---|---|---|
| 1 | B | A "Age, weight and height" and D "Hair, skin and eyes" are implausible; C "only" is a giveaway |
| 2 | B | D "It begins with CPR" and C "finger sweeps" are weak; keep as real myth |
| 3 | B | A and D implausible ("comfortable for the responder", "cools the patient") |
| 4 | B | C "Hold the baby upside down" implausible; A "Pull on the cord" is a useful misconception |
| 5 | B | A "normal part of ageing" (spelling); D implausible |
| 6 | B | A, C, D are all clearly wrong; D "Argue the person out of it" is unlikely to tempt a student |
| 7 | B | A and C and D implausible; "A quick visit to the clinic" is not an abuse sign |
| 8 | short case | repeats the vignette (toddler hot, drowsy, breathing fast); no model answer exists |
**Key letters: B seven times, A, C, D never.** No question tests 6.2 CPR numbers, rescue breathing, 6.3 emergencies (only positioning and birth) or 6.4 beyond confusion; no question on the Scope Note or the Red Flags. Questions run 325 words against 700 planned.

## 7. REQUIRED CHANGES (old text then new text; minimal)
Line numbers refer to the current ch06.md.

1. **Entry 6.2 procedures (S, blocking, about +220 words net).**
   a. Replace L80 (Choking in an Infant) with this lead-in and procedure. Lead-in: "A choking infant cannot cry, cough or breathe. Do not use abdominal thrusts on an infant." Then:
   `::: {.procedure}` `[Procedure: Relieve Choking in an Infant]{.callout-title}` "Purpose: to clear a blocked airway in an infant under 1 year who cannot cry, cough or breathe. Scope: follows your training level and local protocol; the exact method your course teaches takes precedence." Steps: "1. Confirm that the infant cannot cry, cough or breathe, and shout for someone to call emergency services. 2. Lay the infant face down along your forearm, resting on your thigh, with the head lower than the chest. 3. Support the head and jaw with your hand, and keep your fingers off the soft part of the throat. 4. Give up to 5 firm back blows between the shoulder blades with the heel of your other hand. 5. If the object has not come out, turn the infant face up along your other forearm, with the head lower than the body, and give up to 5 chest thrusts with 2 fingers on the lower half of the breastbone. 6. Look in the mouth after each round, and remove an object only if you can see it. 7. Repeat steps 2 to 6 until the object comes out or the infant becomes unresponsive. 8. If the infant becomes unresponsive, lay the infant on a firm surface and begin infant CPR (procedure below)." `:::`
   Safety callout (35 words): "Do not use abdominal thrusts on an infant. Do not sweep the mouth blindly, because you may push the object deeper. Keep the head lower than the chest and support it throughout." Stop line: "**Stop and call for help if** the object does not come out after several rounds, the infant turns blue or gray or goes limp, or the infant becomes unresponsive." Why paragraph (about 50 words): "Back blows jolt the object loose, and chest thrusts raise the pressure inside the chest so that air pushes the object toward the mouth. Abdominal thrusts are avoided in infants because their organs sit low and are poorly protected by the ribs. Alternating the two gives each technique a chance to work." (fact-check and clinician.)
   b. Replace L84 (Rescue Breathing) with a procedure: Purpose "to give breaths to an infant or child who has a pulse but is not breathing normally. Scope: follows your training level and local protocol." Steps: "1. Make the scene safe, check for a response, and call for help; send someone for an AED. 2. Open the airway with the head in line with the body or tilted back only slightly (Entry 2.2). 3. Check for breathing, and for a pulse if your role includes it, for no more than 10 seconds. 4. Seal a mask of the right size over the nose and mouth (Entry 2.3 described the seal). 5. Give 1 breath every 2 to 3 seconds, each lasting about 1 second, just enough to make the chest rise. 6. Recheck breathing and pulse about every 2 minutes, and start compressions if there is no pulse or you are not sure." Safety (about 30 words): "Give gentle breaths. Small lungs are easily over-filled, and air forced into the stomach can cause vomiting. Stop if the chest does not rise and recheck the airway." Stop line: "**Stop and call for help if** the chest does not rise after two attempts, there is no pulse, or the child is not improving." Why (about 40 words): "Children usually stop breathing before the heart stops, so breaths alone can restore a failing circulation if they start early. The rate is slower than the adult rate because the lungs are smaller, and the chest rise tells you the breath was enough." (clinician.) Remove "Your protocol sets the rate you follow." only if the scope line covers it (it does).
   c. CPR procedure: L92 old: "If you are alone, give 2 minutes of CPR first, then call for help and fetch an AED; if someone else is with you, send them at once." new: "If someone else is with you, send them to call for help and fetch an AED. If you are alone and have a phone, put it on speaker and call while you begin. If you are alone with no phone, give 2 minutes of CPR first, then call and fetch an AED." Then delete the paragraph "[Calling Early in a Child.]" (L115, about 50 words; now duplicated). L94 old: "place two fingers or two thumbs on the lower half of the breastbone" new: "place 2 fingers (1 rescuer) or 2 thumbs with the hands encircling the chest (2 rescuers) on the lower half of the breastbone" (clinician to confirm). L96 old: "with two rescuers, give 2 breaths after every 15 compressions" new: "with 2 rescuers, give 2 breaths after every 15 compressions". L97 add: "If there are no child pads, use adult pads placed so they do not touch." (fact-check; omit if not verified.) L95 old: "by about one third of the depth of the chest" new: "by about one third of the depth of the chest (about 1.5 inches (4 centimeters) in an infant and 2 inches (5 centimeters) in a child)" (fact-check; omit numbers if not verified).
   d. CPR Safety box (L104) old: "Do not use abdominal thrusts on an infant. Do not press on the belly or the soft part of the neck. Keep the head in line, and do not tilt a child's head back as far as an adult's." new: "Do not press on the belly or the soft part of the neck. Keep the head in line, and do not tilt a child's head back as far as an adult's."
   e. L113 (Preventing Choking) old: "Small objects, round foods and balloons are common causes of choking in young children. Responders often meet the parent afterward, and a short practical word about keeping small items out of reach and cutting food to a safe size is part of care. Do not lecture a frightened parent in the first minutes." new: "Small objects, round foods and balloons are common causes of choking in young children. Once the child is safe, a short practical word to the parent about keeping small items out of reach and cutting food small is part of care; do not lecture a frightened parent in the first minutes."
2. **Entry 6.3 (S, blocking, about +300 words, within the ceiling by dropping optional items elsewhere).**
   a. Replace the Positioning paragraph (L125) with a one-sentence mechanism and a procedure. Lead-in: "In the later months of pregnancy, the enlarged uterus can press on the large vessel that returns blood to the heart when the patient lies flat on her back, causing faintness and a fall in blood pressure." Then Figure 25 pointer (change 10), figure, and:
   `::: {.procedure}` `[Procedure: Position a Pregnant Patient on the Left Side]{.callout-title}` "Purpose: to take the weight of the uterus off the large vessel that returns blood to the heart. Scope: follows your training level and local protocol." Steps: "1. Make the scene safe, explain what you will do, and ask permission. 2. Check airway and breathing, and call for help if she is unwell. 3. If you suspect a neck or back injury, do not turn her; call for help and follow your spinal motion restriction protocol (Entry 4.3). 4. Help her roll onto her left side, supporting her shoulder and hip. 5. Put a pillow under her head and a rolled blanket behind her back to hold the position. 6. Recheck her breathing, color and responsiveness often, and note the time she was placed on her side. 7. If she becomes unresponsive and is not breathing normally, lay her on her back on a firm surface and start CPR (see below)." `:::`
   Safety (about 30 words): "Do not leave her flat on her back in late pregnancy. Do not tilt her for CPR, because compressions need a firm, flat surface." Stop line: "**Stop and call for help if** she bleeds heavily, has severe pain, a seizure, a severe headache with vision changes, faints, or the baby is crowning." Why paragraph (about 45 words): "The enlarged uterus can squeeze the large vein that carries blood back to the heart when she lies flat. Lying on her left side lifts that weight away, so more blood returns to the heart and the blood pressure improves." (fact-check; clinician for the CPR exception and the spinal case.)
   b. L137 old: "In advanced pregnancy, the same compressions apply, with the uterus moved gently to the patient's left by hand if protocol directs, and the adaptation is taught in advanced courses." new: "In advanced pregnancy, the same compressions apply, and the AED is used as usual. If a second rescuer is available, that person moves the uterus gently to the patient's left by hand while compressions continue. Call for help early, because the patient and the baby both depend on fast advanced care." (fact-check.)
   c. L131 old: "A seizure in late pregnancy can be a sign of a dangerous high blood pressure condition." new: "A seizure in late pregnancy can be a sign of eclampsia, a dangerous complication of high blood pressure, and a severe headache with vision changes can be an early warning of it." (fact-check.)
   d. L139 add at the end: "If the cord is visible before the baby, or the baby is not breathing after birth, tell the dispatcher at once and follow the instructions you are given." (clinician decision; also decide whether "supporting the head gently as it comes" stays given outline section 7.)
   e. Optional style: replace "mother" with "the patient" at L133 ("the mother's own signs"), L147 and L139 where possible.
3. **Care Priorities (blocking).** Replace body L248 with (about 190 words): "Patients who do not fit the adult model share one trap: the usual numbers and the usual story mislead. Ask what is normal for this patient before you decide what is abnormal, and ask the person who knows, whether that is a parent, a carer or a relative. Look before you touch, because a frightened child, a person in crisis and a patient with dementia all react to how you approach, and that first reaction is part of your assessment. Give extra weight to the quiet patient, since a child who has stopped crying, a pregnant patient who feels well after a fall and an older adult with no complaint can each be the sickest person present. When the picture does not make sense, such as an injury that does not fit the story, write down what you saw and what you were told in the patient's own words, and pass it to the person who can act. Finally, check your scope before you act: equipment sizes and legal duties differ by age and by state, and when you are unsure the right move is to call early and stay."
4. **Review Questions and answer key (blocking).** Replace L254 to L296 with the set below (letters C, A, D, B, C, A, D; C twice, A twice, D twice, B once) and write back/answer-keys-part6.md.
   1. A 2-year-old is held by her mother in the doorway. She is limp, does not look at you and has stopped crying. Which part of the pediatric assessment does this describe? A) Circulation to the skin. B) Work of breathing. C) Appearance. D) Vital signs.
   2. An infant cannot cry, cough or breathe after choking on a small toy. Which technique is used? A) Up to 5 back blows, then up to 5 chest thrusts with 2 fingers, repeated. B) Abdominal thrusts below the ribs. C) Blind finger sweeps of the mouth. D) Gentle shaking of the infant held face down.
   3. An alone rescuer finds an unresponsive child who is not breathing normally, with no phone to hand. According to Entry 6.2, which is correct? A) Leave at once to call for help and return later. B) Give 5 rescue breaths only and wait. C) Wait until help arrives. D) Give 2 minutes of CPR, then call for help and fetch an AED.
   4. Why is a pregnant patient in late pregnancy who feels faint helped onto her left side? A) It lowers the risk of vomiting. B) It moves the weight of the uterus off the large vessel that returns blood to the heart. C) It slows labor. D) It turns the baby head down.
   5. A baby is born before help arrives. Which action is correct? A) Pull on the cord to deliver the placenta. B) Cut the cord at once with clean scissors. C) Dry the baby, keep the baby warm against the mother's skin and check breathing. D) Hold the baby upside down to clear fluid.
   6. An 82-year-old who usually chats freely is drowsy and confused, and her daughter says this is new. What does this most suggest? A) An illness, such as infection, low glucose or low oxygen, that needs a cause to be sought. B) Normal aging. C) Dementia, so nothing more is needed. D) Tiredness from a poor night's sleep.
   7. A person in crisis says they want to die. Which response matches Entry 6.5? A) Change the subject to avoid upsetting them. B) Promise to keep it secret. C) Tell them how much they have to live for. D) Ask directly and kindly about suicide, stay with them and call for help.
   8. Short case. A 3-month-old is brought in by a parent. The infant has a bruise on the cheek and is unusually quiet and feeding poorly. The parent says the baby rolled off a sofa. List, in order, the first four things you would do.
   Answer key text for back/answer-keys-part6.md: 1 C (appearance reflects how well the brain is working: tone, interaction, cry). 2 A (infant choking uses back blows and chest thrusts; abdominal thrusts and blind sweeps are avoided). 3 D (the alone-rescuer sequence in Entry 6.2; follow local protocol). 4 B (left-side positioning moves the uterus off the large vessel). 5 C (dry, warm, check breathing; no pulling on the cord). 6 A (new confusion is a sign of illness). 7 D (ask directly, stay, call; do not promise secrecy). 8 Model answer: (1) Look from a distance with the three-part assessment (how the infant seems, how the infant breathes, the color of the skin) and call for help early if any part is abnormal. (2) Complete the primary survey in the usual order, check the glucose if your role allows, and treat the injury. (3) Speak calmly to the parent and record the explanation in the parent's own words with the time, without accusing anyone. (4) Report your concern to your supervisor and through the channels your service requires, because a bruise in an infant who cannot yet roll over does not fit a fall from a sofa, and you do not need proof to report.
5. **Entry 6.1 (about +170 words net; replaces vague pointers).**
   a. L26 pointer is changed in change 10. Before the table (L46) add: "The table below gives typical resting ranges by age." Table caption old: "Table: Typical resting ranges in children (reference copy)" new: "Table: Typical resting ranges in children". Header old: "Breathing rate (a minute) | Heart rate awake (a minute)" new: "Breathing rate (breaths per minute) | Heart rate awake (beats per minute)". Age bands old: "Toddler (1 to 3 years)", "Preschool (3 to 5 years)", "School age (6 to 11 years)" new (only after the fact-check source is chosen; bands must not overlap or leave a gap): "Toddler (1 to 2 years)", "Preschool (3 to 5 years)", "School age (6 to 11 years)".
   b. L40 old: "Entry 2.2 described the positions for adults. Their breathing rate is higher, and their heart rate is higher, and both vary by age." new: "Entry 2.2 described the positions for adults. Children also breathe faster and have a faster heart rate than adults, and both change with age."
   c. L56 add "(Entry 1.3)" after "slow capillary refill".
   d. L58 old (all five sentences) new: "Several earlier entries gain one child-specific point. Asthma (Entry 2.4) shows the same signs in a child, who may tire sooner. A child has a small blood volume, so bleeding that would be minor in an adult can be serious, and an adult-sized tourniquet (Entry 4.2) may not fit a small limb; call for help early. Low blood glucose is more common in small children who are ill, so a glucose check belongs in the assessment of any drowsy child (Entry 5.1). A first seizure with fever in a young child needs assessment (Entry 5.3), and any injury that does not fit the story needs attention (Entry 6.6)." (fact-check "tire sooner" and tourniquet fit.)
   e. Add after L58: "[Urgency and Allergy.] Entry 1.2 set out the five levels of acuity. For a child the same levels apply, with one addition: a child who is limp, hard to wake or inconsolable is sorted higher whatever the numbers show, and a parent who says the child is not acting like themselves counts as a finding. Anaphylaxis (Entry 2.5) in a child may begin with hives, vomiting or a cry that turns hoarse rather than with obvious breathing trouble, so treat these after a likely trigger as an emergency. In sepsis (Entry 5.4) an infant may show only poor feeding, floppiness or an unusual cry, with or without fever. Burns (Entry 4.5) in a child need a clinician's assessment even when they look small, and the spinal precautions of Entry 4.3 apply to children with the padding adjustment described above." (about 125 words; fact-check all.)
   f. L63 Red Flags old: "or a fever in a very young infant" new: "or a fever in an infant under about 3 months" (use the age the source gives).
   g. ch02 L183 See also old "Entry 6.1 (child sizing and rate)" new "Entry 6.2 (child breaths and rate)" (change in ch02, flagged for the propagation pass).
6. **Entry 6.4 (about +90 words net).**
   a. L155 old last sentence: "Chest pain in older adults and the other presentations of Entry 3.2 deserve the same urgent response." new: "Entry 3.2 gave the classic chest pain pattern. In older adults, and in women of any age, a heart attack may instead show as breathlessness, nausea, sweating or unusual tiredness, so treat unexplained breathlessness or sudden weakness as possible heart trouble and call early. A stroke may show as sudden confusion or a fall rather than a drooping face (Entry 5.2), and a serious abdominal problem may bring little pain, no fever and a soft belly (Entry 5.6), so the red flags of those entries apply even when the picture looks mild." (fact-check; sex is mentioned because presentation differs.)
   b. L157 old: "New confusion is not a normal part of ageing. It is called delirium and is a sign of illness: infection," new: "New confusion is a sign of illness, often called delirium. Its causes include infection,".
   c. L165 old: "Do not delay lifesaving care while you search for a document unless your protocol directs." new: "Do not delay urgent care while you search for a document; follow your protocol." (clinician and state-law item.)
   d. L167 old: "Older adults are less able to sense and respond to heat and cold, and Entry 4.6 described the signs. Check the temperature of the home." new: "Older adults sense heat and cold less well and may not feel thirsty. Entry 4.6 described the signs; check the temperature of the home and ask how long the patient has been in it."
   e. L177 old: "review medicines, protect from falls" new: "note the medicines, protect from falls".
   f. L279 (Q5 in the old set) is replaced in change 4; ensure "aging" in the final set.
7. **Entry 6.5 (about +80 words net).**
   a. Add a Red Flags callout after L195 (about 42 words): "A person who talks about wanting to die or has a plan or the means, a weapon, threats to others, severe agitation with confusion, chest pain or breathing trouble with panic, or signs of poisoning. Call emergency services at once."
   b. L187 old: "Fear, pain, confusion, intoxication, withdrawal, low glucose, low oxygen, a head injury and an acute psychiatric illness can each cause agitation, and a person may have more than one at once." new: "Fear, pain, intoxication, withdrawal and an acute psychiatric illness can each cause agitation on top of the physical causes above, and a person may have more than one at once." (removes the duplicate list.)
   c. Add after L193: "[When the Person Refuses Help.] A person in crisis may refuse care. Entry 1.5 set out consent. Stay calm, keep talking, do not argue and call for help, because decisions about whether someone may refuse, or be held for their own safety, rest with clinicians and the law of your state." (about 50 words; clinician.) Optional if the count allows: "A frightening call can leave a responder shaken; Entry 1.1 mentioned responder wellbeing, and telling your supervisor is part of the job."
8. **Entry 6.6 (about +90 words net).**
   a. L213 old: "Abuse and neglect are hidden in plain sight. Responders see injuries and illnesses, and some of them are not accidents. Recognizing the signs and acting properly can protect a child, an older adult or a partner who cannot ask for help." new: "Responders see injuries and illnesses, and some of them are not accidents. The patient may be a child, an older adult or a partner who cannot ask for help, and you may be the only professional who sees the signs."
   b. Add a Safety callout (about 35 words) after L219: "Do not question the patient about abuse in front of the person you suspect, promise to keep a secret you cannot keep, or confront the suspected abuser. Your first aim is the patient's safety now."
   c. L219 old: "Speak to the patient privately if you can and listen without judging." new: "Speak to the patient privately if you can do so safely, and listen without judging."
   d. Add after L219: "[Recording What You See.] Write the patient's words in their own words, the time, who was present, and each injury by place and size, for example a round bruise about 1 inch (2.5 centimeters) across on the left upper arm. Describe; do not conclude. A note that says abuse is a conclusion, and a note that describes the bruise lets the next clinician judge." (about 65 words.)
9. **Vignette (about +65 words).** After L236 sentence "Her breathing was fast, and the skin between her ribs pulled in with each breath." add "Her lips were pink, but her hands and feet looked pale and a little mottled." Replace L240 with: "A doctor saw Noor within minutes. Afterward the triage nurse asked Sam what she had noticed first, and Sam answered in the order she had looked: how Noor seemed, how she breathed, and the color of her skin. She also gave the nurse the times the mother had mentioned, because Sam had written them down as she heard them." (the Part 5 vignette ends with a handover too; this ending differs in shape.)
10. **Figure and table pointers (recurring fault).** L26 old "Figure 23 shows the three parts of the assessment." new "Figure 23 shows the three parts of the assessment; notice that the look is made from a distance, before you touch the child." L42 old "Figure 24 compares the airway of a child with that of an adult." new "Figure 24 compares the airway of a child with that of an adult; notice the size of the head and tongue relative to the airway." (check against image.) L127 old "Figure 25 shows left-lateral positioning." new "Figure 25 shows left-lateral positioning; notice the rolled blanket behind her back that holds the position." Clinician must confirm that Figure 25 shows the LEFT side down (mirrored image, status.md).
11. **Numbers, spelling and word choices (N, T).** L18 old "As always, what you may do depends on" new "What you may do still depends on". L84 (if kept) "just enough" new "only enough". Steps L94 to L96 use numerals as in change 1. Q-set uses "aging". L123 old "A pregnant patient has two lives in the balance, and the best care for the baby is good care of the mother." new "In pregnancy the care you give the patient is also care for the baby." (drops the repeat of the overview.)
12. **Priorities lines (shorten, no restating).** L72 new: "Look first from a distance, use the three-part assessment, involve the parent, and call early." L117 new: "Match the technique to the age, and call early for any child who is not breathing normally." L147 new: "Position on the left side, call early, and watch for shock." L177 new: "Take vague symptoms seriously, ask what is usual for the patient, and call early." L207 new: "Check the scene, rule out medical causes, ask directly about suicide, and stay with the person." L227 new: "Treat the injuries, listen privately, record facts, and report as your role requires."
13. **Fact-check gate.** Add rows P6-001 onward to verification-log.md for every B, D and S item in section 4, especially items 9, 10, 16, 21, 23 to 29, 33, 39, 40, 47, 53, 55 and 58. No Part 6 text should ship while those rows are empty.

**Length plan.** The required (A) changes are 1, 2, 3, 4, 7a, 8b and 9: about +220 (6.2 net) + 300 (6.3) + 100 (Care Priorities) + 90 (questions, 325 to about 415) + 42 + 35 + 65 = about +850, landing at about 5,750 by wc (about 5,680 stripped): above the floor and 100 over the 5,650 target. Changes 5, 6, 7b, 7c and 8d add about +300 more and would reach about 6,050, which breaches the ceiling of 6,000, so the writer should apply 5, 6 and 7 first and drop 8d and the optional wellbeing sentence if the count passes 5,950. Where genuine new substance is placed: pediatric procedures in 6.2, positioning procedure and CPR adaptation in 6.3, child urgency and allergy cues in 6.1, atypical presentation in 6.4, refusal and consent in 6.5, documentation wording in 6.6, vignette detail, Care Priorities and questions. None is padding.

## 8. Items for the fact-checker (not for editing)
Child resting breathing and heart rate bands (which source, which bands, overlap at 3 and gap at 5 to 6); "very young infant" age limit; infant choking sequence (back blows, chest thrusts, head position, no abdominal thrusts, no blind sweep); child choking with abdominal thrusts; pediatric CPR numbers (depth one third of chest depth, 100 to 120, 30:2 and 15:2, 10 second check, two-finger and two-thumb techniques); the alone-rescuer rule (2 minutes first versus call first or speaker phone) against current pediatric BLS as of 2026-10-29; rescue breathing rate 1 breath every 2 to 3 seconds; AED pads for children and adult pads when child pads are missing; left-lateral positioning and the exception for CPR and for suspected spine injury; manual uterine displacement in pregnancy CPR; eclampsia wording; cord prolapse; "supporting the head" in imminent birth; "do not cut the cord unless trained"; blood volume and heart rate changes in pregnancy and the "middle months" BP statement; atypical heart attack presentation in older adults and women; stroke and abdominal presentations in older adults; resuscitation-wish documents and state law; 988 (call or text) and 911; "asking does not put the idea into someone's head"; remove-means advice; abuse indicators (bruising in a non-mobile infant, "bruises in unusual places", burns with clear outlines); mandatory reporting in general terms; whether adult-sized tourniquets fit children.

## 9. Reader test
- First page: honest and well framed ("a child is not a small adult"); the objectives list matches what follows.
- Middle (6.2): the infant CPR procedure is strong, but the choking and breathing sections above it are unstructured prose and the alone-rescuer rule is stated twice differently.
- Last page: Care Priorities is generic, every answer is B, and the case question repeats the vignette. A reader would sense the Part running out of steam.

## 10. Verdict
**REVISE.** Blocking: 1 (procedure pattern for infant choking and rescue breathing, contradictory alone-rescuer rule), 2 (positioning procedure, pregnancy CPR exception), 3 (Care Priorities), 4 (questions and missing answer key). Under-floor by 165 words until the A set of changes is applied. Unlogged B, D and S items remain until the fact-check rows exist.
