---
name: lessons
description: Stage 11 RETRO. After a book (or at any milestone) reviews what went wrong and right, extracts reusable lessons, and updates docs/lessons-learned.md and, when a rule or skill should change, proposes the exact edit for the owner to approve. Keeps the framework improving with every book. Use at the end of every book and after any painful rework.
---

# /lessons: THE FRAMEWORK GETS BETTER EVERY BOOK

## Purpose
Every book teaches something. This stage turns the run into rules so the next book avoids the same rework.

## Inputs
`books/<slug>/status.md`, `status-archive.md`, `run-log.md`, `PROGRESS.md`, `compliance/`, `audits/`, `verification-log.md`, git history of the book folder, the owner's messages that corrected the course, and the previous `docs/lessons-learned.md`.

## Procedure
1. **Collect the facts**: dates and durations per stage, number of review rounds and what they found, decisions the owner changed (what, when, cost in rework), tool failures (what failed, how it was fixed), files that went stale, claims that were corrected, and what the owner liked.
2. **Classify** each finding: PROCESS (stage order, gates), RULE (policy or compliance), TOOL (script, connector, environment), QUALITY (writing, audits, figures), MARKET (research method), OWNER-PREFERENCE (style, communication).
3. **Write lessons** in the format: what happened, why it mattered, the rule or check that prevents it, where it lives (file and section), status (ADDED / PROPOSED). Keep each lesson to a few lines; no blame.
4. **Apply safely**: add lessons to `docs/lessons-learned.md` (append, dated, with the book slug); for any change to `CLAUDE.md`, a skill, a profile or a script, write the exact proposed edit and ask the owner to approve before changing instruction files. Never silently change standing rules.
5. **Metrics line**: stage durations, review rounds, figures regenerated, words per Part, final page count, open items at handover.
6. **Report** in at most 6 lines: top 3 lessons, what was changed, what needs approval.

## Rules
- Honest: record failures as failures. Do not embellish results.
- Never remove an old lesson; mark it SUPERSEDED with the reason.
