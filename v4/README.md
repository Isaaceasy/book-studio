# BOOK STUDIO V4: your GENIE-model AI publishing studio (setup and use)

V4 is the fully automated version of the studio. It follows your GENIE client guide: **"One idea in. A finished, publish-ready book out."** You give one idea; V4 researches the niche, screens the title, writes the book chapter by chapter with fact-checks and compliance reviews, designs the colored interior, generates the figures, builds the print interior, the ebook and both covers, writes the store metadata, runs the risk gates and puts everything in a release folder with an upload guide. It then offers the growth tools (launch, ads, reviews, royalties, audio, author brand).

**Control line (same as GENIE):** V4 prepares and assists. You sign in to your own accounts, control payment and tax details, and press the final Publish click. Nothing before that needs you, except the short list of hard stops below.

## Start (any computer)
1. Copy this folder to the computer. Open **this folder** in Claude Code.
2. First time only: install Python 3.10+, pandoc, Git, LibreOffice (optional), then in this folder:
   `pip install -r requirements.txt` and `python -m playwright install chromium`.
3. Check the setup: `python scripts/doctor.py` (it tells you what is missing and which stage it would block).
4. Connect the tools you use: the browser tool (Amazon research) and HiggsField (images).
5. Type: `/genie <your idea or title>`

## The commands
| You type | What happens |
|---|---|
| `/genie <idea or title>` | The whole pipeline, automatically. |
| `/genie continue` | Resume after a stop or a new session. |
| `/genie status` | Catalog table of all books and what each is waiting for. |
| `/genie queue` | Run the ideas in `books/_queue.md` one after another. |
| `/genie grow <slug>` | Launch, ads, reviews, royalties, brand, editions, audio (after you have published). |
| `/genie --guided <idea>` | Same, but it stops for your approval at every gate. |
| `STOP` / `PAUSE` / `change <thing>` | Save and stop / roll back to the affected stage. |

Any stage skill can still be run alone: `/cms-research`, `/title-lab`, `/risk-analysis`, `/cover-design`, `/ebook-build` and the others in `.claude/skills`.

## What can make the run wait for you (the only hard stops)
1. The one intake question block at the start.
2. A NO-GO market verdict (a CAUTION verdict continues with the most conservative plan).
3. Title registry evidence: Claude cannot search the USPTO site. Give it the saved result pages; otherwise the title stays PROVISIONAL and the release is withheld until you do.
4. Expert sign-off for medical, engineering, legal and other expert books: the book is built and marked DRAFT_FOR_REVIEW; the release is withheld until the written sign-off exists.
5. A tool failure that does not clear after two retries (for example the image tool).
6. Risk gate R3 BLOCKED (a High risk is open).
7. Your own actions at the end: sign in, KDP previewer, proof copy, tax and payment details, press Publish.

## What is new in V4 (on top of V3)
- `/genie`, the conductor that runs all stages with automatic pass conditions and rollback.
- `/ebook-build` and `scripts/ebook_build.py`: a Kindle-ready EPUB from the same verified text (V3 had only the ebook cover).
- `/risk-analysis`: one risk register per book with three gates (R1 concept, R2 build, R3 release).
- `scripts/doctor.py` (environment check), `scripts/manuscript_lint.py` (placeholders, links, banned phrases, word floors, name consistency, answer-key length bias), `scripts/status_keeper.py` (status file that cannot contradict the folder), `scripts/release_pack.py` (release folder, manifest with checksums, owner checklist), `scripts/catalog.py` (dashboard), `scripts/git_helper.py` (finds git, commits per stage).
- Queue mode for several books.

## Everything inherited from V3
Copy Market Strategy research, the title lab, trademark page scanner, cover pipeline (spine and wrap calculator, composer, preflight), interior library (19 style cards, no default template), expert-review layer for medical and engineering books, A+ content, editions, puzzle and coloring studios, audiobook studio, ads, launch, review, royalty and author-brand skills, lessons-learned log.

## Files to read
`CLAUDE.md` (the rules), `docs/genie-coverage.md` (GENIE capability to skill map), `docs/automation-roadmap.md`, `docs/kdp-specs.md`, `docs/lessons-learned.md`, `interiors/INDEX.md`.
