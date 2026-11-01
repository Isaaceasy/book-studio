---
name: puzzle-studio
description: Generates real puzzle content for puzzle and activity books (word search, sudoku, crosswords, mazes, cryptograms, word scrambles, number puzzles, kids' activities) with a script that guarantees valid, solvable puzzles and verified answer keys, then lays them out in the book interior. Never ships placeholder or unsolved puzzles. Use for puzzle-book profiles or puzzle sections inside other books.
---

# /puzzle-studio: PUZZLES WITH VERIFIED ANSWER LOGIC

## Purpose
GENIE Pro "puzzle studio: generates real puzzle content and verifies answer logic". Every puzzle must be solvable, unique where required, and match its answer key. Amazon's low-content and quality rules apply: a puzzle book needs substantial, original, varied content, not filler.

## Inputs
`brief.md` (puzzle types, audience, difficulty ladder, theme, count), `cms-research.md` (what the best sellers include: puzzle counts, difficulty, large print, themes), `book.yaml`, `style-guide.md`, `interiors/` (puzzle-friendly styles).

## Procedure
1. **Plan the content set**: puzzle types and counts per section, difficulty progression (easy, medium, hard), themes, word lists or numeric constraints, and page layout per puzzle (one per page or several; large print for senior audiences). Check KDP's live low-content guidance and make sure the book is not generic filler.
2. **Generate with the script** `python scripts/puzzle_gen.py <type> --count N --seed S --out puzzles/<type>/` (types supported out of the box: `wordsearch`, `sudoku`, `maze`; extend the script for crosswords and others). The script produces the grid, the solution and a self-check, and writes JSON plus SVG. Seeds make runs reproducible.
3. **Verify** every puzzle with the script's `verify` step: word search words all present exactly once in the allowed directions and none overlapping illegally; sudoku has a valid solution and exactly one solution (the generator uses a solver to confirm uniqueness); mazes have a path from start to end; crosswords have valid intersections and a clue for each answer. Record pass or fail counts in `puzzles/verify-report.md`. Any failure is regenerated, never shipped.
4. **Word lists and clues**: original, age-appropriate, no trademarks or real people; remove offensive strings by running every generated filler string against a blocklist; for themed lists verify facts (use `/fact-check`).
5. **Answer keys**: generated from the verified solutions, printed at the back, one answer per puzzle number; spot-check ten by hand and record them.
6. **Layout**: build puzzle pages from the generated SVG using the interior design (large clear grids, enough line weight for print, numbering, consistent difficulty icons). Check legibility at print size.
7. **Compliance and QC**: `/amazon-compliance` scope `puzzle`; `scripts/preflight_interior.py`; render and inspect pages.
8. **Deliver** `puzzles/`, the assembled interior, the verify report, the AI-disclosure facts (generated programmatically versus AI-written word lists), and update `status.md`.

## Rules
- Never publish an unverified puzzle or an answer key not generated from the verified solution.
- Never present randomly generated letter noise as content; every puzzle must be solvable.
