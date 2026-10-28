---
name: amazon-compliance
description: Reviews any content (idea, title, outline, chapter, image, description, keywords, cover text, whole manuscript) against Amazon KDP's current policies, terms and conditions and against customer-experience standards, using live policy pages, and returns PASS / REVISE / BLOCK. Required for every piece of content before it counts as complete.
---

# /amazon-compliance — AMAZON POLICIES, TERMS AND CUSTOMER EXPERIENCE

## Purpose
The owner's rules: all content must be evaluated against Amazon's policies, terms and conditions; no rule may be broken; nothing may lead to poor or bad customer experience. This skill performs that evaluation independently using the `compliance-reviewer` subagent (`.claude/agents/compliance-reviewer.md`) and the checklist in `profiles/amazon-compliance-checklist.md`.

## Inputs
Argument: the scope. Examples: `idea`, `title`, `outline`, `chapter 3`, `images chapter 3`, `description`, `keywords`, `manuscript`, `cover text`. Files: the item(s), `brief.md`, `book.yaml`, `market-research.md`, `verification-log.md`, `status.md` (AI disclosure facts), `profiles/amazon-compliance-checklist.md`, the profile file.

## When it is run (the system calls it automatically at these points)
- After `/market-research` approval: scope `idea` (policy risk of the niche and angle).
- After `/title-check`: scope `title` (title, subtitle, series, author name).
- After `/outline-book`: scope `outline` (promise versus planned content, claims, disclaimers).
- After every chapter is written and fact-checked: scope `chapter N` (and `images chapter N`).
- After `/assemble-book`: scope `manuscript` (whole-book customer-experience review).
- After `/kdp-metadata`: scope `description` and `keywords`.
- Any time the owner asks, or when a policy-sensitive element appears (health claims, minors, safety, trademarks, public-domain material, AI-generated images).

## Step-by-step procedure

1. **Open the current policies, live.** Following section A of `profiles/amazon-compliance-checklist.md`, search for and open the current Amazon KDP pages (Content Guidelines, Terms and Conditions, metadata guidelines, AI-generated content policy, public domain / duplicate / low-content rules, review and promotion rules, print requirements, health content rules where relevant). Read them. Record each page's title, the date accessed and one line of what it currently requires. If a page cannot be opened, mark the dependent checks UNVERIFIED and tell the owner. Never rely on memory for a rule.

2. **Launch the `compliance-reviewer` subagent** with the scope, the file paths, and the policy notes from step 1. It must return the review in the format in section E of the checklist: a table of the checks in sections B and C, each PASS / FIX / BLOCK / UNVERIFIED with evidence, plus a customer-experience risk list (likely one-star reasons and the fix for each) and an overall verdict.

3. **Customer-experience simulation** (do this yourself in addition): read the item as a buyer who paid for the book on the strength of its title, subtitle and description, then as a skeptical reviewer. For a chapter ask: does it deliver what the title promised at this point; is anything missing, unclear, repetitive, padded, inaccurate or unsafe; would a reader stop reading, ask for a refund, or complain; are there typos, formatting faults, broken tables, clipped figures, wrong page numbers. For the whole manuscript also check the contents page against the real chapters, consistency of terms and notation, balance of chapter lengths, and whether the book is worth its price compared with the gaps found in market research. Record every plausible disappointment.

4. **Fix.** Apply every FIX to the content (backing up first). Re-run the review on the changed parts until PASS. Maximum 3 rounds; then report the remaining issues to the owner. On BLOCK stop and explain the risk plainly (for example an item that could trigger account action) and offer options.

5. **Record.** Save to `books/<slug>/compliance/<scope>-compliance.md`: scope, date, policy pages opened (title, date accessed, takeaway), the check table, customer-experience risk list with fixes made, final verdict. Update the compliance column in `status.md`. Update the AI-disclosure facts in `status.md` (which text, images and translations were AI-generated or AI-assisted) whenever images or translated text are added.

## Verdict rules
- PASS only if every check B1 to B10 is PASS (UNVERIFIED not allowed) and no customer-experience risk remains open.
- Never soften a verdict. Never mark PASS without reading the item and the live policy text.
- A chapter with an open FIX or UNVERIFIED cannot be declared complete.

## Output to the owner (max 3 lines)
Verdict, number of fixes made, anything the owner must decide, and where the review file is.

## Rules
- This is a good-faith review, not legal advice or a guarantee that Amazon will accept the book. Say so in the review file's last line.
- Do not reproduce Amazon's policy text at length; paraphrase.
- Do not suggest ways to evade policies, detection, or review. If content only works by evading a rule, change the content.
