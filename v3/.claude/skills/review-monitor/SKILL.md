---
name: review-monitor
description: Tracks the real review signals for a published book from reviews the owner exports or pastes (or signs in to view themselves), classifies the themes, separates actionable defects from opinion, routes each defect into a correction workflow (fix in the Markdown source, rebuild, re-check, republish by the owner), and never fabricates, solicits, buys, edits or manipulates reviews. Use after launch, monthly, or whenever the owner pastes new reviews.
---

# /review-monitor: REVIEW SIGNALS AND THE CORRECTION WORKFLOW

## Purpose
GENIE Max "review monitoring: tracks review signals and routes actionable issues into a correction workflow without fabricating or manipulating customer feedback." Reviews are reader feedback; this skill makes them useful.

## Inputs
Reviews the OWNER supplies (pasted text, screenshots, exports from their own signed-in view), the rating and count the owner reads from the listing, the book's source files, `audits/`, `status.md`. Claude never signs in to Amazon; Amazon's review pages need sign-in for many views.

## Procedure
1. **Intake**: record each review: date, star rating, verified purchase if shown, theme tags. Keep quotes short (in the owner's private file only) and paraphrase otherwise. Do not edit or rewrite reviews.
2. **Classify** each review as: praise (what works), defect (factual error, typo, broken layout, missing content, safety concern, unclear step), mismatch (title or description promised something the book does not deliver), format (print quality, size, color), shipping or seller issue (not a book defect), or opinion (no action). Count themes; a theme with 3 or more reviews is a CONFIRMED issue, fewer is a WATCH item.
3. **Route defects**: for each confirmed defect create a ticket in `reviews/tickets.md`: description, evidence (review dates and wording summary), affected file and location (Part, entry, page), severity (safety-critical items go first and are reported to the owner at once), proposed fix, status. Fixes happen in the Markdown source, then the affected audits and fact-checks re-run, the interior rebuilds, `scripts/preflight_interior.py` runs, and the owner uploads the revised file in KDP (the owner decides whether to republish).
4. **Mismatch fixes**: adjust the description, subtitle expectations or A+ content (new metadata proposals through `/kdp-metadata`), never by hiding a defect.
5. **Reply drafts**: Amazon does not let authors reply to reviews on product pages; do not draft public replies. For customer questions or emails the owner receives, draft a polite factual reply the owner sends.
6. **Monthly summary** `reviews/summary-YYYY-MM.md`: rating trend as reported by the owner, theme counts, tickets opened and closed, and lessons for `docs/lessons-learned.md`.
7. **Safety rule**: if a review reports possible harm from the book's content, stop and tell the owner immediately with the affected text and a recommended hold or correction.

## Rules
- Never write, buy, trade, solicit or suggest fake or incentivized reviews, review gating or review manipulation of any kind. Never ask for positive-only feedback.
- Never fabricate review text, counts or ratings. If you have no data, say so.
