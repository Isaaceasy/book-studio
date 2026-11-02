---
name: genie
description: THE CONDUCTOR. One command runs the whole studio in AUTOPILOT, modeled on the owner's GENIE guide ("One idea in. A finished, publish-ready book out."). `/genie <idea or title>` creates the book and runs intake, CMS research, title lab and title check, risk gate R1, architecture lock, interior design, every chapter (fact-check, compliance, figures, audit, preview), assembly, expert clearance pack, covers, ebook build, metadata, risk gates R2 and R3, upload guide and the release folder, stopping only at the hard stops in CLAUDE.md section 9. Also `/genie continue`, `/genie status`, `/genie grow <slug>`, `/genie queue`, `/genie --guided`. Use whenever the owner gives a book idea, says start, continue, run the whole thing, or asks for the status of the catalog.
---

# /genie: ONE IDEA IN, A PUBLISH-READY PACKAGE OUT

## What this skill is
The conductor of the V4 studio. It does not do the work of a stage itself; it calls the stage skills in order, checks their results, writes the state files, commits, and moves on without waiting for approval. The owner's GENIE guide defines the connected pipeline: BRIEF, RESEARCH, WRITE, PREVIEW, DESIGN, PACKAGE, PUBLISH, GROW. V4 runs all of it. GENIE keeps the customer in control of accounts and the final publish click; so does V4 (CLAUDE.md rule 6).

## Commands
| Command | Does |
|---|---|
| `/genie <idea or title>` | New book, full AUTOPILOT run (stages 0 to 10). |
| `/genie continue [slug]` | Resume from `PROGRESS.md` of the active book. |
| `/genie status` | Run `python scripts/catalog.py books` and show the catalog table plus each book's next step. |
| `/genie grow <slug>` | Growth sequence for a finished book (section "Growth run"). |
| `/genie queue` | Run the ideas listed in `books/_queue.md` one after another. |
| `/genie --guided <idea>` | Same pipeline but stop for approval at every gate (V3 behaviour). |
| `STOP` / `PAUSE` | Save state and stop at the next safe point. `change <thing>` rolls back to the affected stage. |

## Step 0: preflight (every run, every session, 1 minute)
1. Read `CLAUDE.md` (all), `docs/lessons-learned.md`, `docs/kdp-specs.md`, the profile for the book, and `profiles/amazon-compliance-checklist.md`.
2. Run `python scripts/doctor.py`. Record the result. If a REQUIRED item is missing, fix it if possible (pip install, playwright install) or tell the owner exactly what is missing and which stages it blocks. Confirm the tools that a script cannot see: browser tool for Amazon research (set the delivery location to the marketplace, honestly record it), HiggsField connection and credits (`balance`), and write permission for the book folder. Say in one line which stages this environment cannot do, and ask nothing else.
3. List `books/`. Open the active book's `status.md`, `PROGRESS.md`, `book.yaml`. If resuming, jump to the first stage not marked done; never redo a finished stage unless the owner said "change".

## Step 1: the one intake block (the only planned question)
Ask ONE question block (AskUserQuestion, up to 4 questions) containing only what cannot be defaulted:
1. Idea or title and marketplace/language (if not already given).
2. Formats wanted: paperback, ebook, hardcover, large print, audiobook (default paperback + ebook).
3. Folder of saved USPTO result pages for the title (or "I will provide later; proceed provisionally").
4. For expert profiles: the name of the human reviewer who will sign off (or "not yet").
Everything else gets a recorded default (CLAUDE.md section 9 defaults). Write the answers to `brief.md`, `book.yaml`, `status.md` ("Defaults I chose"). Never ask the owner again for something already given.

## Step 2: the autopilot sequence
Run these in order. After each stage: save outputs, run the stage's own checks, update `status.md` (top block via `python scripts/status_keeper.py books/<slug> --write`), append `run-log.md`, update `PROGRESS.md`, commit with `python scripts/git_helper.py commit "Stage N: name"`, print the one status line, start the next stage.

| # | Stage | Call | Automatic pass condition | If it fails |
|---|---|---|---|---|
| 0 | Intake | `/new-book` (answers from Step 1, no re-asking) | brief, book.yaml, status.md exist | fix and retry |
| 1 | CMS research | `/cms-research` | cms-research.md, competitors.csv (15+ rows), product-spec.md; verdict GO or CAUTION | NO-GO: HARD STOP 2 |
| 2 | Title lab and check | `/title-lab` then `/title-check` (run `scripts/tm_scan.py` on supplied pages) | one recommended title and subtitle, rating recorded, KDP length rules pass | live mark conflict: rerun title lab; no registry pages: title PROVISIONAL (HARD STOP 3 rule) |
| 2b | **Risk gate R1** | `/risk-analysis` checkpoint R1 | no unmitigated High risk | fix what Claude can; otherwise stop with the list |
| 3 | Architecture lock | `/outline-book` (auto-approve its own run-mode question: AUTOPILOT) | outline, style guide, book bible; every CMS gap addressed; figure allocation | retry once with a stricter prompt |
| 4 | Interior design | `/design-interior` (picks style cards from `interiors/INDEX.md`, builds `book.css`, sample PDF, checks distance from the referenced interiors) | sample PDF renders, 5x8-or-trim legible, greyscale legible where the profile requires | adjust and retry twice |
| 5 | Write all chapters | `/write-chapter N` for N = 1..last, in order (CLAUDE.md section 9 AUTOPILOT rules) | per chapter: word floor, ledger clear, compliance PASS, audit written, figures done, lint 0 errors, render inspected | chapter under floor after 3 genuine expansions: record UNDER-FLOOR, continue; tool failure after 2 retries: HARD STOP 6 |
| 6 | Assemble | `/assemble-book` then `python scripts/manuscript_lint.py books/<slug>` on the whole book, then `python scripts/preflight_interior.py` on the interior PDF | lint 0 errors, preflight PASS, page count meets KDP minimums | fix source and rebuild |
| 6b | **Ebook build** | `/ebook-build` (`scripts/ebook_build.py`) when ebook is a wanted format | EPUB PASS (mechanical) | fix source, rebuild |
| 7 | Expert clearance pack | `/clinical-clearance` (build the pack only; sign-off is the human's) | pack produced; manuscript marked DRAFT_FOR_REVIEW if the profile requires sign-off | continue (HARD STOP 5 rule) |
| 8 | Covers | `/cover-design` (concepts chosen automatically by the CMS cover notes and distance check; script-drawn art when the concept is geometric, HiggsField otherwise) | preflight PASS, thumbnail legible, compliance PASS | retry with a different concept once |
| 8b | A+ content (if Pro-level output is wanted; default yes for Amazon) | `/aplus-content` | 8 images at the live sizes, alt text, no invented claims | skip with a note if the tool fails |
| 9 | KDP metadata | `/kdp-metadata` | description within limit, 7 keywords with evidence, categories | retry |
| 10a | **Risk gate R2** | `/risk-analysis` checkpoint R2 | PASS or PASS WITH OWNER ACTIONS | fix what Claude can |
| 10b | Upload guide and release | `/risk-analysis` R3, then `/kdp-upload-guide`, then `python scripts/release_pack.py books/<slug>` | R3 not BLOCKED; manifest written; owner checklist written | R3 BLOCKED: release_pack withholds the packet (HARD STOP 8) |
| 11 | Final report and retro | print the Final Report (below); run `/lessons` | report saved to `final/FINAL-REPORT.md` | |

## Rules for the whole run
- **Never relax** the standing rules (CLAUDE.md section 0). Autopilot changes WHEN the owner reviews, never WHAT is checked.
- **Independent reviewers** (compliance-reviewer, editor, fact-checker agents) run at their stages. They cannot write files: the main session saves their reports under `compliance/` and `audits/`. At most 3 rounds each.
- **Honesty:** every research stage opens with a Research Proof block; never claim an action that did not happen; mark anything unverified TO VERIFY and remove or qualify it.
- **Provisional marks:** anything depending on an owner-only step (registry search, sign-off) is labelled PROVISIONAL in the files and in the report, never presented as cleared.
- **Roll back, do not patch silently:** if the owner changes the idea, title, niche, trim or price, restart from the earliest affected stage and log the change in `status.md` and `status-archive.md`.
- **Commit** after each stage; if the branch is ahead of origin and a cloud session or backup is wanted, tell the owner to push (the assistant has no credentials).
- **Cost control:** before any batch of image generations, check the HiggsField balance and say what the run will use; if credits are short, finish the stages that need none and stop at HARD STOP 6 with the figure list left as Image Slots.
- **Phone/remote:** if Remote Control is on, the stage status lines are the notifications; after a HARD STOP, state the one thing needed.

## Growth run (`/genie grow <slug>`, only after the owner has published and says so)
1. `/launch-manager` (30-day plan, timed).
2. `/ads-manager` (campaign plan and bulk sheets; weekly optimization needs the owner's exports).
3. `/review-monitor` (monthly, from reviews the owner pastes or exports).
4. `/royalty-report` (monthly, from KDP exports).
5. `/author-brand` (author page copy, landing page, reader magnet).
6. `/edition-expansion` (hardcover, large print) and `/audiobook-studio` if wanted.
7. Offer `/niche-discovery` for the next book and add accepted ideas to `books/_queue.md`.

## Queue run (`/genie queue`)
`books/_queue.md` has one idea per line: `slug | idea or title | profile | formats | notes`. Run each book through the autopilot. When a book reaches a HARD STOP that waits for the owner, record it in `PROGRESS.md`, move to the next queued book, and return to the waiting book when the owner answers. Keep a combined list of everything waiting on the owner in `books/CATALOG.md` (`python scripts/catalog.py books`).

## Final Report (print and save to `final/FINAL-REPORT.md`)
1. What was built: title, subtitle, profile, trim, pages, word count, figures, formats, files (folder and file names in plain words).
2. Gate results: R1, R2, R3; count of High / Medium / Low open risks.
3. What is PROVISIONAL and why (registry search, sign-off, proof copy).
4. AI-disclosure facts to use at upload (text, images, covers).
5. OWNER CHECKLIST: exactly the actions only the owner can do, in order, ending with the publish click.
6. Money: price chosen, royalty per format (from the live calculator), break-even for ads if relevant.
7. Top three lessons for `docs/lessons-learned.md`.
Keep the chat message to at most 6 lines and point to the file.

## What this skill never does
Sign in anywhere, enter passwords or payment details, change account or tax settings, accept terms for the owner, solve CAPTCHAs, upload, submit or press Publish. Those are the owner's. Everything else is automatic.
