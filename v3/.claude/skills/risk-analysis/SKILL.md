---
name: risk-analysis
description: Cross-cutting RISK GATE. Builds and maintains one Risk Register per book (legal and trademark, Amazon policy, market, content safety, rights and images, quality, technical, account and operational risks), scores every risk by likelihood and impact, assigns a mitigation, an owner and a status, and blocks the upload guide while any High risk is open. Runs at three checkpoints (after CMS research and title lab, after assembly and clearance, before the upload guide) and on demand. Use whenever the owner asks "what could go wrong", "is this safe to publish" or "risk analysis", and automatically at the three checkpoints.
---

# /risk-analysis: ONE REGISTER OF EVERYTHING THAT COULD GO WRONG

## Purpose
V3 already has many separate checks (trademark rating, GO / CAUTION / NO-GO, compliance PASS / REVISE / BLOCK, Critical items, image tiers). This skill gathers them in ONE file so the owner can see, in one place, what could still hurt the book, how bad it would be, what has been done about it and what is still open. It does not replace those checks; it reads their results and adds the risks nobody else covers.

It is analysis only. It never publishes, uploads, logs in or pays (standing rule 6). It never claims a risk is low without evidence recorded in the register (standing rule 5).

## Inputs
`books/<slug>/` : `book.yaml`, `status.md`, `product-spec.md`, `cms-research.md`, `competitors.csv`, `title-lab.md`, `title-check.md`, `compliance/*.md`, `audits/*`, `verification-log.md`, `verification/guideline-registry.md`, `verification/figure-log*`, sign-off records, `covers/cover-log.md`, `final/` build and preflight reports, `final/KDP-metadata*`. Also `profiles/<profile>.md`, `profiles/amazon-compliance-checklist.md`, `docs/kdp-specs.md`, `docs/lessons-learned.md` and the template `templates/risk-register.md`.
Read only what exists at the checkpoint. A missing input is itself recorded as a risk ("not yet done") rather than assumed fine.

## Checkpoints (when it runs)
| Checkpoint | When | What it decides |
|---|---|---|
| R1 CONCEPT | After `/cms-research` and `/title-lab` / `/title-check`, before `/outline-book` | Is the idea, title and format safe and worth building? Market, trademark, policy and similarity risks. A High risk open here stops the outline. |
| R2 BUILD | After `/assemble-book` and `/clinical-clearance` (and covers), before `/kdp-metadata` | Is the finished package safe? Content safety, rights, images, quality, technical and clearance risks. |
| R3 RELEASE | Immediately before `/kdp-upload-guide` and the release folder | Final gate. Nothing High may be open. Every Medium has an owner decision recorded. |
| ON DEMAND | Any time the owner asks, or after any change to title, subtitle, niche, trim, price, profile, images or clearance | Re-score only the affected risks and log the change. |

## Risk categories (check every one at every checkpoint)
1. **LEGAL-TM** Trademark and name conflicts: title, subtitle, series name, author name, keywords, cover text, manuscript mentions of organizations. Evidence: `title-check.md`, owner-run registry search status. Never LOW without a registry search.
2. **POLICY** Amazon KDP rules: content guidelines, metadata rules, title length, AI disclosure, review and ads rules, "disappointing content", duplicate or low-content flags, misleading claims, public-domain or reused content. Evidence: latest `compliance/*.md`, live KDP pages with dates.
3. **MARKET** Demand and profit: competition strength, saturation, price pressure, royalty at the planned price and format, dependence on one keyword, seasonality, bestseller-dominated niche. Evidence: `cms-research.md`, `product-spec.md`, unit economics.
4. **SIMILARITY** Closeness to modeled bestsellers (title wording, cover look, interior layout, table of contents). Evidence: title-lab, cover-design and design-interior distance checks.
5. **SAFETY-CONTENT** Anything that could change what a reader does and cause harm: doses, thresholds, procedures, legal or financial actions, structural or electrical values. Evidence: Critical items in `audits/`, guideline registry currency, sign-off records. Applies to every profile, scaled to the topic.
6. **CREDENTIALS** Missing or unrecorded expert sign-off, unverified reviewer credential or licence, wording such as "clinician-reviewed" before a written sign-off exists, invented authority or affiliations.
7. **RIGHTS-IMAGES** Copyright and licensing of images, fonts, templates and any source text; AI-image terms of the tool (re-read date); figures that resemble real scans or photos; likeness of real people; third-party reference interiors accidentally reused.
8. **QUALITY** Chance of one-star reviews: promise versus content gaps, padding, repetition, typos, placeholders, weak figures, wrong spelling variant, formatting faults, multiple-choice length bias, readability for the audience.
9. **TECHNICAL** Print and file risks: page count against minimums, margins and bleed, spine fit and spine text rule, barcode zone, color vs black ink cost, font embedding, image resolution, greyscale legibility, ebook file validity, PDF page size. Evidence: preflight reports and the proof copy.
10. **ACCOUNT-OPS** Risks to the owner's KDP account and operations: wrong author spelling across files, wrong category, wrong price or royalty option, missed AI disclosure, rights holder statement, tax or ISBN choices left to the owner, publishing too many similar titles, previewer and proof copy not yet done.
11. **PRIVACY-ETHICS** Real persons or patients, identifiable case studies, sensitive topics, inclusive and age-appropriate content, children's safety (profile `childrens-picture`), religious or political sensitivity.
12. **DEPENDENCY** Tool and environment risks: image tool rate limits and terms changes, browser access to Amazon, cloud session limits, unpushed commits, files that exist only locally.
Profiles may add categories (see the profile file); record any added category in the register.

## Scoring
- **Likelihood (L):** 1 Rare, 2 Possible, 3 Likely, 4 Almost certain.
- **Impact (I):** 1 Minor (cosmetic, fixable after launch), 2 Moderate (a bad review pattern, a lost week), 3 Major (listing blocked or removed, refund wave, legal letter, large rework), 4 Severe (reader harm, account suspension, legal action, a book that cannot be sold).
- **Score = L x I.** 1 to 4 LOW, 5 to 8 MEDIUM, 9 to 16 HIGH.
- **Override:** any risk of reader harm (SAFETY-CONTENT with Impact 4) or of account termination is HIGH regardless of likelihood until evidence shows it is closed.
- **Residual score:** after mitigation, re-score and keep both the inherent and the residual score so the owner sees the effect.
- **Confidence:** HIGH (evidence opened and recorded), MEDIUM (partial evidence), LOW (assumption). A LOW-confidence rating on LOW risk is treated as MEDIUM until evidenced.

## Procedure
1. **Open the register** `books/<slug>/risk-register.md` (create from `templates/risk-register.md` at R1). Never delete a risk; close it with the date and the evidence, or mark it ACCEPTED with the owner's decision.
2. **Gather evidence** for each of the 12 categories from the input files. For anything that depends on current rules (KDP policy, trademark, tool terms), open the live source and record the date; do not rely on memory.
3. **List risks** one per row: id (R-001...), category, short description (what could go wrong, in plain words), trigger (what would make it happen), inherent L, I, score and level, evidence (file and section, or "none yet"), mitigation (the specific action and who does it: CLAUDE, OWNER, CLINICIAN, THIRD PARTY), due checkpoint, status (OPEN, MITIGATED, ACCEPTED BY OWNER, CLOSED), residual L, I, score, confidence.
4. **Run the checkpoint tests** (below) and write the gate result at the top of the register.
5. **Fix what Claude can fix** (for example a placeholder, a wrong spelling, a missing log entry) and re-score. Items that need the owner (registry search, previewer, proof copy, sign-off, price decision) stay OPEN with a clear instruction.
6. **Report** in at most 6 lines: gate result, count of High / Medium / Low open, the top 3 risks, what you need from the owner. Save and commit the register (rule 17).

## Checkpoint tests (gate rules)
**R1 CONCEPT: PASS only if**
- the CMS verdict is GO, or CAUTION with the owner's written decision to proceed and a compact plan recorded;
- title and subtitle have a trademark rating, and an owner-run registry search is recorded or the risk is marked OPEN High;
- distance from modeled books is documented and acceptable;
- royalty at the planned price and format is positive with a stated margin;
- no High risk is OPEN without a named mitigation.

**R2 BUILD: PASS only if**
- every chapter has fact-check clear and compliance PASS recorded;
- every Critical item is cleared or removed; for profiles that require expert clearance, the written sign-off record exists (a verbal report is recorded as VERBAL and keeps the risk OPEN High);
- Figure Log complete; every AI image has tier, attempts and reviewer decision where required; the AI-image terms re-check date is recorded;
- interior and cover preflights PASS; greyscale check done where the profile requires it;
- author name, title, subtitle and spelling are identical across `book.yaml`, title page, copyright page, cover files and metadata (run a search and record the result);
- no placeholder, "TODO", "lorem" or bracketed instruction text remains in manuscript files.

**R3 RELEASE: PASS only if**
- zero HIGH risks are OPEN;
- every MEDIUM risk is MITIGATED, or ACCEPTED BY OWNER with date and reason;
- KDP previewer review and a proof copy order are listed as owner actions with status;
- AI-disclosure facts in `status.md` match what the upload guide will say;
- the live KDP policy pages were re-read on a recorded date within the last 30 days;
- all work is committed and, for cloud use, pushed.

Gate result values: **PASS**, **PASS WITH OWNER ACTIONS** (only owner-side items remain, all listed), **BLOCKED** (a High risk or failed test; list exactly what to fix). `/kdp-upload-guide` and `/publish-assist` must refuse to start while the R3 result is BLOCKED and must copy the owner-action list into their checklists.

## Honesty and limits
- This is a structured review, not legal, medical or financial advice and not a guarantee of KDP acceptance. Say so in the register header.
- Amazon publishes no sales data; never invent probabilities of sales. Likelihood scores are judgments backed by recorded evidence.
- Do not mark a risk CLOSED on the strength of your own opinion when the mitigation depends on a human (registry search, clinician, proof copy). Mark MITIGATED PENDING OWNER.
- If an independent opinion is useful, use the `compliance-reviewer` agent for POLICY and the `fact-checker` for SAFETY-CONTENT; they return reports in their messages and the main session saves them (rule 16). At most 3 rounds.

## Output
`books/<slug>/risk-register.md` (living file) and, at each checkpoint, a dated section "Checkpoint R1 / R2 / R3" inside it with the gate result. Update the one-line "Risk gate" field at the top of `status.md`.
