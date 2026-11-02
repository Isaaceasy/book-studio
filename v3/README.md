# BOOK STUDIO V3: your complete AI publishing studio (setup and use)

V3 is the upgraded, universal framework built from the emergency nursing book run and from your four framework documents (EMB Unified v1.8, EMB Medical v1.0, the EMB KDP Description framework and the GENIE client guide). It takes one idea or title to a publish-ready package (interior, ebook cover, paperback wrap, metadata, upload guide) and, when you ask, to launch, ads, reviews, royalties, audio and author brand. It never publishes, uploads, logs in or pays: you make every final click.

## What is new in V3
1. **Copy Market Strategy (CMS)**: for every title or idea, deep live Amazon research: 15 to 25 competitors, each one's USP, positioning map, gap analysis, unit economics for 2 to 3 formats, a model blueprint, and an approved PRODUCT SPEC.
2. **Title Lab**: bestseller-modeled titles built with several keyword-composition techniques, tested for collision, autocomplete, trademark and KDP rules, scored, and clearly different from the books they model.
3. **Cover stage**: ebook cover and paperback wrap, with exact spine and wrap calculation, text set by script, preflight checks and an AI-disclosure log.
4. **Interior library** (`interiors/`): you upload interiors; the framework reads them and designs beautiful, colored, category-appropriate, unique interiors.
5. **Growth stages** from your GENIE guide: niche discovery, A+ content, editions (hardcover, large print), puzzle and coloring studios, audiobook studio, ads manager, launch manager, review monitor, royalty reports, author brand kit, publishing packets.
6. **Expert-review layer** from your EMB Medical framework: safety-critical items, audit classes, guideline registry, sign-off record, image tiers, color coding with a greyscale fallback, optional numbered references.
7. **Lessons learned** from the first book are built in (`docs/lessons-learned.md`), and every book adds to them.

Read `docs/genie-coverage.md` to see every GENIE capability and where it lives, and `docs/automation-roadmap.md` for what to automate next.

## One-time setup (Windows)
1. Install Claude Code or use the Claude desktop app, signed in.
2. Install Python 3.9 or newer (tick "Add Python to PATH") and Pandoc.
3. In a terminal in this `v3` folder: `pip install -r requirements.txt` then `python -m playwright install chromium`.
4. Optional but recommended: a PDF page-to-image tool (Poppler) so Claude can look at pages, and an image tool connected for figures (HiggsField).
5. Open THIS `v3` folder as the project (so Claude reads `v3/CLAUDE.md` and `v3/.claude/skills`). The older framework in the repository root is version 2.

## How to run a book
1. `/niche-discovery` (optional) to find an idea, then `/new-book` and answer the one question block.
2. `/cms-research`, approve the product spec.
3. `/title-lab`, choose a title; save your USPTO result pages and Claude reads them with `scripts/tm_scan.py`; `/title-check`.
4. `/outline-book`, approve the lock, answer the run-mode question.
5. `/design-interior`, approve the sample. Upload new interiors to `interiors/_inbox/` and run `/interior-library` any time.
6. `/write-chapter` (or the autonomous run), then `/assemble-book`.
7. Expert review and the sign-off record (medical, engineering and other expert profiles).
8. `/cover-design`, `/kdp-metadata`, `/kdp-upload-guide` (and `/publish-assist`).
9. Growth when you want it: `/aplus-content`, `/edition-expansion`, `/launch-manager`, `/ads-manager`, `/review-monitor`, `/royalty-report`, `/author-brand`, `/audiobook-studio`, `/puzzle-studio`, `/coloring-studio`.
10. `/risk-analysis` at three gates (after titles, after assembly and covers, before the upload guide); it keeps `risk-register.md` and blocks the upload guide while any High risk is open.
11. `/lessons` at the end of every book.
Say "continue" any time; Claude reads the status file and proposes the next step.

## Where your files go
Every book lives in `books/<slug>/` (see `CLAUDE.md` section 3). Markdown files are the source of truth; PDFs and Word files are generated.

## Good to know
- Reference documents you gave me (`docs/reference-materials/`) and the interior reference images (`interiors/_inbox`, `interiors/library/*/reference`) are kept on your computer and are not committed to git (rights and privacy). Style cards and instructions are committed so cloud sessions can use them.
- Cloud runs only see what is pushed. Push from your Git client, then start the cloud session.
- Amazon asks you to disclose AI-generated content. The status file records the exact facts.
- Claude does not invent sources, reviews, sales numbers, credentials or income promises. Check anything important yourself before publishing.
