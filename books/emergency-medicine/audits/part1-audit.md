# Part 1 editorial and clinical audit: The Emergency Approach (chapters/ch01.md)

Date 2026-10-29. Auditor: independent editor. ch01.md NOT edited. Verdict: **REVISE** (14 required changes; none needs new facts except where marked S/B).

## 1. Mechanical results
| Check | Result |
|---|---|
| Words, whole file (wc -w) | 5,540 |
| Table cells (2 tables, 149 words) | excluded |
| Words excluding tables | 5,391 vs target 5,400 and ceiling 6,000: ON TARGET, floor (5,000) met by content not padding |
| Per-entry words vs outline budget | 1.1 694 vs 650; 1.2 892 vs 1,100 (-19%); 1.3 1,553 vs 1,100 (+41%); 1.4 738 vs 650; 1.5 416 vs 450. Overview 215 vs 250; Vignette 271 vs 250; Care Priorities 181 vs 250; Review Questions 299 for 8 items (budget about 700 with stems, short) |
| Sentences (prose incl. label paragraphs) | 293; average 15.4 words; 28 over 30 words (9.6%); longest 50 (Red Flags callout in 1.2) |
| Repeated openers | "The" 28, "A" 27, "It" 13, "Entry" 9. Runs of 3: "A" x1, "The" x2 (benign). Style-guide sample sentences reused: Sample A is the 1.2 opening and Sample B the 1.1 opening (intended by the guide) |
| Em dashes | 0 |
| Banned words (CLAUDE.md 6 and style guide) | none found: no delve, unlock, moreover, furthermore, additionally, crucial, simply, easy, just, always, never, "ER", golden hour, "In conclusion" |
| ESI / START / ENA / AHA / SBAR / course names | none (case-sensitive grep). Structure caveat in F4 below |
| URLs, links, citations, footnotes | none |
| Placeholders / TODO | none. Figure files ch01-fig1..4.svg exist |
| Callout word counts (20 to 60) | Safety 44, 57; Remember 29, 16 (too short, see C5); Red Flags 50, 44; Scope Note 50, 42. All in range except Remember 1.3 (16) |
| Remember callouts per entry | 1.2: 1; 1.3: 1; none elsewhere. Rule met |
| Figure caption start | all four begin "Figure N." in order of appearance (1 triage, 2 primary survey, 3 sites, 4 handover). But each caption is TWO sentences; style guide says one sentence |
| Figures referenced in prose | none of the four is mentioned in running text before it appears |

## 2. Structure against outline
- Entries 1.1 to 1.5 present, in order. Heading 1.5 is shortened: outline title is "Communication, consent, scope of practice, handover, reassessment and documentation"; ch01 reads "Communication, Consent, Handover and Reassessment". Scope of practice is never given its own passage in 1.5 (FAIL, change 4).
- Objectives 1 to 5 match outline wording (only "(ABCDE)" dropped from objective 3, acceptable because ABCDE is defined in 1.3). Objective 4 says "name abnormal findings", but 1.4 gives only normal ranges plus one abnormal threshold (RR above about 25). Partially unmet (change 9).
- Procedure pattern: 1.1 passes (purpose, scope line, 6 steps, Safety, Stop line, prose paragraph). 1.3 passes (9 steps, Safety, Stop line, prose paragraph); the order in 1.3 is long prose first, then procedure, which is acceptable. 1.1 and 1.3 Safety callouts both end "Giving medicines is outside many roles" although no medicine is named anywhere in either entry (change 12).
- "Nursing and Responder Priorities." present in all 5 entries. "See also:" present in all 5. Forward bridges required by outline section 1/9 present: 1.3 to 3.5 and 5.1, 1.4 to 5.4, plus 6.1. 
- Vignette present, labelled, past tense, 271 words, no institutions. Care Priorities present but fails the non-repetition rule (change 1). Review Questions 8, answer key present at back/answer-keys-part1.md with explanations of 1 sentence.

## 3. Scores (1 to 5)
| Area | Score | Reason |
|---|---|---|
| Promise and structure | 4 | all entries/order OK; 1.5 title and scope-of-practice gap; 1.3 over budget |
| Substance at length | 4 | at target through content; some in-entry repetition (1.2, 1.3 recheck message x6) |
| Clarity and readability | 4 | avg 15.4 words, clear; 28 long sentences, mostly lists |
| Voice consistency | 4 | calm, second person; "not X but Y" habit weakens it |
| Specificity and examples | 4 | units carried; abnormal values thin in 1.4 |
| Teaching quality | 3 | "neck injury is not possible" wording, bleeding-first not in steps, abnormal findings not named |
| Human-sounding prose | 3 | about 14 "not X, Y" constructions, triplet lists (35 hits), moral endings |
| Consistency | 3 | Care Priorities restates entries; terminology drift (blood sugar, breathing rate, abbreviations undefined) |
| Chapter ending | 4 | Review Questions close the Part, no forward hook; Care Priorities is meant to carry the takeaway |

## 4. Audit table (classes A/B/C/D/S/N/T)
IDs refer to verification-log.md rows already written for Part 1. I opened none of the sources again; "VERIFIED" below only repeats what the log records and needs the clinician batch anyway.
| # | Location | Claim / item | Class | Status / note |
|---|---|---|---|---|
| 1 | 1.1 | Standard precautions list; gloves first, eye protection/mask/gown when splashes likely | B | log P1-0xx (CDC), follow-up with reviewer |
| 2 | 1.1 | Procedure "Make the Scene Safe" steps 1 to 6, Safety, Stop line | S | clinician clearance |
| 3 | 1.1 | Responder wellbeing advice (debrief, peer support) | S | low risk, reviewer to note |
| 4 | 1.1 / 1.3 Safety | "Giving medicines is outside many roles" with no medicine in text | D | no drug or dose in Part 1 (log P1-068 agrees); line unnecessary |
| 5 | 1.2 | Five-level US triage, level 1 most urgent; usually done by nurse (P1-012, P1-015) | B | log VERIFIED |
| 6 | 1.2 | Four ordered questions and 5-row level table | B/S | mirrors the published five-level tool's decision points almost one-to-one although not named; confirm with owner/compliance it is acceptable as generic principle and not a lightly paraphrased copy |
| 7 | 1.2 | Red Flags list (speech, gray/blue lips, confusion, bleeding) | S | clinician clearance |
| 8 | 1.2 | "word comes from the French for sorting" | B | not in log rows I read; add or remove |
| 9 | 1.3 | ABCDE order and rationale (P1-028/029) | B | log VERIFIED (secondary) |
| 10 | 1.3 | Bleeding handled first in many trauma protocols (P1-030) | S | QUALIFIED + NEEDS-HUMAN; procedure steps do not reflect it (change 10) |
| 11 | 1.3 | First look about 30 s; speaking = airway open (P1-031) | B | OK; "has enough blood flow to the brain" is an inference, soften |
| 12 | 1.3 | "if a neck injury is not possible, tap or shake the shoulders" (P1-069) | S | WRONG/ambiguous as written; reads as permission to shake when injury is impossible; contradicts Safety box in spirit (change 2) |
| 13 | 1.3 | CPR if unresponsive and not breathing normally; gasps not normal (P1-032) | S | needs clearance; CPR not defined at first use (T) |
| 14 | 1.3 | Capillary refill: 5 s press, under 2 s normal; caveats (P1-036) | B | log VERIFIED; adult-only caveat could be added |
| 15 | 1.3 | AVPU/ACVPU; GCS 3 to 15 (P1-038/039) | B | VERIFIED. "Highest score" fine |
| 16 | 1.3 | Glucose below 70 mg/dL (3.9 mmol/L) for many people with diabetes (P1-045/046) | B/A | VERIFIED; 70/18.016 = 3.89 checked by log |
| 17 | 1.3 | Lancet single use, sharps container, meter per maker | S | clearance |
| 18 | 1.3 | Safety: cervical spine care; do not move injured patient unless scene unsafe (P1-043) | S | NEEDS-HUMAN; also contains an unrelated reassessment sentence (change 12) |
| 19 | 1.4 | Table: 60 to 100 bpm; 12 to 18 breaths/min; 90/60 to 120/80 mm Hg; 97.7 to 99.1 F (36.5 to 37.3 C) (P1-051) | B/N | VERIFIED to a consumer source; conversions reproduced. Units format OK. SpO2 row absent although SpO2 is a vital sign per bible |
| 20 | 1.4 | RR above about 25 "widely treated" (P1-052) | B | vague authority wording (change 8 item) |
| 21 | 1.4 | Pulse oximeter limits incl. skin pigmentation, CO (P1-055) | B/S | OK; CO named in one sentence, allowed by outline section 7 |
| 22 | 1.4 | BP can stay normal in shock | B | not found in log; add source or qualify |
| 23 | 1.5 | Consent, capacity, implied consent in emergencies; rules differ by state | S | NEEDS-HUMAN, legal statement |
| 24 | 1.5 | Four-part handover format (Situation, Background, Assessment, Recommendation) | B | generic, unnamed; fine |
| 25 | 1.5 | Documentation advice (P1-063) | B | low risk |
| 26 | Vignette | findings consistent with chapter definitions (P1-066) | A | OK; man "in his sixties": age/sex mention not stated as clinically relevant (minor) |
| 27 | RQ 1 to 8 / key | answers (P1-064/065) | A | Q8 key/prompt mismatch (change 13) |
| 28 | All | number format and units | N | measurements spelled out as words ("thirty seconds", "five seconds", "two seconds", "twenty minutes"); style guide wants numerals for measurements (change 7) |
| 29 | All | terminology vs table | T | "low blood sugar" (1.3 Disability) vs locked "low blood glucose"; "breathing rate" without defining as respiratory rate (RR); ED, CPR, EMT used without definition at first use (change 8) |

## 5. Human-sounding prose: findings
- "Not X, but/only Y" and negation-then-correction (about 14): L13-14 overview, L23, L25, L54, L62 (approved sample, keep), L90, L92 (twice), L116, L186, L190 ("a guide, not a rule"), L201 ("not a diagnosis"). Rewrites in required change 5.
- Triplet rhythm (rule of three) examples: L23 "environment, people present, own protection"; L229 "protects the patient, helps the next team, and protects you"; L223 "short, ordered and free of guesses"; L130 "Look, listen and feel"; L54 "Eat, drink and rest". 35 comma lists of three or more; most are functional (hazard lists, signs), the decorative ones are above.
- Moral or neat endings: L25, L54, L201, L205 "the secondary survey is your best chance to find a hidden one", L229, L260 (Care Priorities final line), L90 "the reason you recheck is to catch that change".
- Vague authority: L13 "The people who handle this well are rarely the ones who know the most" (unsupported generalization); L199 "widely treated".
- Repeated message: "recheck after every intervention" appears at L123 (Remember), L151 (step 9), L168 (caption), L170 (Priorities), L227, L256; "Wait a short while ... before judging its effect" appears word-for-word at L157 and L227.
- 1.2 states twice that triage is not about worth (L62 and L92).

## 6. REQUIRED CHANGES (numbered, minimal)
1. **Care Priorities restates entries (blocking).** All five paragraphs repeat the Priorities lines or entry text (e.g. "Look at the scene, protect yourself, and call for help early" = L56; "trust trends over single numbers" = L199/L213). Replace the box body (L252-260) with a tie-breaker passage that adds a new angle:
   "First, when two things compete, your own safety comes before the patient's need, and the patient who cannot wait comes before the patient who complains most. Second, treating a threat comes before measuring it: a pulse oximeter reading can wait, an obstructed airway cannot. Third, calling for help comes before finishing the history, the head-to-toe check or the paperwork. Fourth, a plan is only as good as the next check, so put a time on every observation and decide before you leave the bedside when you will look again. Finally, if a task is outside your scope, say so at once and stay with the patient until someone who can do it arrives."
   (about 120 words; Part stays under 5,400 and above 5,000; the 250-word figure is a target, honest length rule applies.)
2. **Neck-injury wording (S), L126.** Old: "if a neck injury is not possible, tap or shake the shoulders gently as you ask whether they are all right". New: "if a neck injury is unlikely, tap the shoulders gently as you ask whether they are all right; if a neck injury is possible, speak loudly and do not move the head or neck." Send to clinician batch (P1-069).
3. **Remember in 1.3 is not a memory aid and is only 16 words (L123).** Old: "Fix each problem as you find it, then move on. Recheck after every action you take." New: "Find it, fix it, check again. After any treatment, wait a short while before judging its effect, then repeat the survey." (about 20 words; this also lets you delete the duplicate sentence in the 1.3 Safety box, change 12.)
4. **Heading and scope of practice in 1.5 (outline lock).** Old heading: "## [1.5]{.num} Communication, Consent, Handover and Reassessment". New: "## [1.5]{.num} Communication, Consent, Scope of Practice, Handover, Reassessment and Documentation". Add after the consent paragraph: "[Scope of Practice.]{.label} Your scope of practice is the set of tasks your license, certification or student status allows. Do only what it allows, say plainly when a task is beyond it, and ask your supervisor before trying anything you have not been taught and cleared to do." (about 50 words). Also update the opening sentence of 1.5 list ("speaking with the patient, obtaining consent, ...") to include "staying within your scope".
5. **Remove "not X, but Y" tics.** Quote then new:
   - L23 old: "A safe approach is not a delay. A few deliberate seconds at the edge of a scene cost far less than having to treat a second patient." New: "A few deliberate seconds at the edge of a scene cost far less than treating a second patient."
   - L25 old: "...the check must be a routine step that you do every time and not a judgment call that you make only when something looks wrong." New: "...the check must be a routine step you take every time."
   - L54 old: "Seeking that help is part of staying safe to work, not a sign that you are unfit for it." New: "Seeking that help is part of staying safe to work."
   - L90 old: "...must be reassessed at once and moved to a higher level, and the reason you recheck is to catch that change." New: "...must be reassessed at once and moved to a higher level."
   - L92 old: "It is also not a ranking of worth. Two patients with the same level are often seen in the order they arrived, unless one gets worse, and a patient who waits longer is not a lower-priority person, only one whose condition allows waiting." New: "Two patients with the same level are often seen in the order they arrived, unless one gets worse. A patient who waits longer is one whose condition allows waiting."
   - L116 old: "It is not a diagnosis and it is not a full examination." New: "It does not diagnose and it does not replace a full examination."
   - L186 old: "What matters is not the letters but the habit of covering the ground the same way every time, so that nothing important, such as an allergy or a blood-thinning medicine, is forgotten." New: "Use the mnemonic you are taught and cover the same ground in the same order every time, so that nothing important, such as an allergy or a blood-thinning medicine, is forgotten."
   - L13-14 old: "The people who handle this well are rarely the ones who know the most. They are the ones who have a fixed order of thinking and follow it while their pulse is racing." New: "People who handle this well have a fixed order of thinking and follow it while their pulse is racing."
6. **Neat-moral and triplet endings.** L205 delete the sentence "When the patient has no obvious problem, the secondary survey is your best chance to find a hidden one." (unsupported). L229 old: "A clear record protects the patient, helps the next team, and protects you." New: "A clear record lets the next team see what has already been done and when." L223 old: "A good handover is short, ordered and free of guesses presented as facts." New: "A good handover is short, follows a fixed order, and labels a guess as a guess."
7. **Number format (N), measurements as numerals per style guide.** L126 "about thirty seconds" to "about 30 seconds"; L144 same; L132 "for five seconds" to "for 5 seconds" and "under two seconds" to "under 2 seconds"; L199 "over twenty minutes" to "over 20 minutes". Optional: "milligrams per deciliter (3.9 millimoles per liter)" to "mg/dL (3.9 mmol/L)" after spelling out once.
8. **Terminology table (T) and abbreviations.** L134 old: "low blood sugar can cause confusion" New: "low blood glucose can cause confusion". L64 first use: "In a US emergency department (ED), triage..." and use "ED" at L105. L126 first use: "start cardiopulmonary resuscitation (CPR) as set out in Entry 3.4" (and L145 keep CPR). L210 old: "nursing, paramedic and EMT students" New: "nursing, paramedic and emergency medical technician (EMT) students". L130 old: "Count the breathing rate carefully" New: "Count the breathing rate (respiratory rate, RR) carefully"; keep "breathing rate" afterwards as an accepted synonym. L199 old: "breathing rates above about 25 breaths per minute are widely treated as a sign that a patient may be heading for trouble" New: "a breathing rate above about 25 breaths per minute is a marker of illness that calls for urgent attention and a call to your supervisor".
9. **Objective 4 "name abnormal findings" (1.4) and 1.2 "danger range".** After the table (L198) add: "A reading outside its range is an abnormal finding. Report it, and treat a large departure, or any departure in a patient who looks unwell, as urgent." Also in the 1.2 Remember box, old: "Are the vital signs safe for that level?" keep; in L76 old: "if they are in a danger range" New: "if they are in a danger range (Entry 1.4 gives typical resting values)". No new numbers, class A.
10. **Bleeding first is in the prose and Care Priorities but not in the steps (S).** Procedure step 2, old: "Take the first look: speak to the patient and watch the response for about thirty seconds." New: "Take the first look: speak to the patient and watch the response for about 30 seconds; if heavy bleeding is visible, your protocol may direct you to control it first (Entry 4.1)." Clinician to clear (P1-030).
11. **Figure captions are two sentences; guide says one.** New: Fig 1 "A generic five-level triage sequence, in which the first two questions ask about danger, not paperwork." Fig 2 "The primary survey as a loop, with treatment after each check and a repeat of the whole loop after every intervention." Fig 3 "Where to check pulse, breathing and skin perfusion on an adult, in the same places each time." Fig 4 "A four-part handover in which each part answers one question for the receiver." Also add one in-text pointer before each figure (e.g. before L78: "Figure 1 shows the sequence."; before L168 "Figure 2"; before L203 "Figure 3"; before L225 "Figure 4").
12. **Safety callouts.** 1.1 Safety and 1.3 Safety end with "Giving medicines is outside many roles; follow your scope and medical direction." where no medicine appears; delete in both (rule applies on drug mention). In 1.3 Safety also delete "Wait a short while after any treatment before judging its effect, because some treatments take minutes to work." (now in new Remember; 1.5 Reassessment keeps its own sentence; delete the duplicate at L227 "Wait a short while after an intervention before judging its effect.").
13. **Review Questions.** Q5 options "A. A. / B. V. / C. P. / D. U." are hard to read; New: "A. Alert. B. Voice. C. Pain. D. Unresponsive." Q4 option D old: "Exposure only if the patient is conscious." New: "Exposure." Q8 and key: old key "(4) Assess airway and breathing, count and record the breathing rate, then continue through circulation, disability and exposure and treat problems as found." New: "(4) Assess airway and breathing and count the breathing rate. Then continue through circulation, disability and exposure." In the key, justify (3): "Call for help early because fast breathing and a reduced response to voice suggest the patient may worsen." Add one question on history or vital signs (objective 4) by replacing Q2 or Q1 is NOT required; but the set tests no objective-4 item beyond oximeter, so replace Q4 (pure recall) with a vital-signs trend question if the owner agrees (answer key must follow). Answer letters currently B,C,B,C,B,C,C: reorder options so keys are spread.
14. **Fact items for fact-checker (not editing):** "word comes from the French for sorting" (L64); BP may stay normal in shock (L199); "has enough blood flow to the brain" (L126) soften to "is probably getting enough blood to the brain"; the 1.2 four-question Remember and 5-level table closely mirror a published tool: decide with owner/compliance whether to reword the level descriptions further.

## 7. Reader test
- First page: promises a fixed order of thinking; specific and calm. Overview is shorter than planned (215 vs 250) but not thin.
- Middle (1.3): clear, but long; the recheck message is repeated six times.
- Last page: Review Questions end the Part with no hook to Part 2; Care Priorities (once rewritten) should carry the takeaway. Acceptable.

## 8. Verdict
**REVISE.** Blocking: changes 1, 2, 4, 9, 10. Others are quality fixes. After changes, expected Part words about 5,350 to 5,450 excluding tables, inside the ceiling.
