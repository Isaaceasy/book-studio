# Book Studio — Setup and Use (version 2)

This folder is your own AI publishing studio, run by Claude Code in the Claude desktop app (the Code tab). You give it one idea. It researches Amazon live, checks the title, designs the book, writes every chapter with fact-checking and Amazon-policy review, builds the final manuscript and prepares the KDP metadata and upload guide. It stops for your approval at the gates. It never publishes, logs in to Amazon or buys anything. You make the final publish click.

## What it supports

Three book profiles, chosen in `/new-book`:

- **Engineering**: 12 to 18 chapters of 10,000 to 12,000 words each (excluding tables), Word manuscript in your house style, worked examples, practice problems, native Word equations, SVG and HiggsField figures, technical reviewer clearance. Based on your EMB Unified Book Framework.
- **Medical**: Parts and entries, 10,000 to 12,000 words per Part, Word manuscript, glossary and index, safety wording, clinician clearance. Based on your MEB Medical Encyclopedia Framework.
- **General** (everything else): KDP print PDF (6 x 9 by default) with a designed color interior.

Output formats: Word house style for engineering and medical (US Letter, 1 inch margins, Times New Roman 12 pt, justified, 1.15 spacing, drop caps, seven heading styles to choose from); designed PDF for general books.

## One-time setup (Windows)

1. Open the Claude desktop app, choose the **Code** tab and select this folder.
2. Install **Python 3.9 or newer** from python.org (tick "Add Python to PATH").
3. Install **Pandoc** from pandoc.org/installing.html.
4. Install **LibreOffice** from libreoffice.org (needed to make the PDF test copy and the contents page numbers for Word books). Include the Math component if the installer asks, so equations also show in the test PDF.
5. In a terminal (PowerShell) in this folder run:
   ```
   pip install -r requirements.txt
   python -m playwright install chromium
   python scripts/docxbuild.py check
   python scripts/bookbuild.py check
   ```
   Every line should say OK. Anything that says MISSING needs installing before that profile works.
6. (Recommended) Install Poppler for page images: github.com/oschwartz10612/poppler-windows/releases (add its `bin` folder to PATH). Claude uses it to look at the pages.
7. Connect **HiggsField** in the Claude connector settings. Claude draws infographics, diagrams and charts itself as SVG and uses HiggsField only for illustrations and artwork. If HiggsField is not connected Claude tells you and leaves marked slots for those figures only.

## Install the skills (one time)

Claude's tools cannot write into the hidden `.claude` folder, so skills and agents were saved in `claude-config`. Double-click `install-skills.bat`. It copies them into `.claude`. Run it again whenever new versions are delivered. After that you may keep `claude-config` as a backup.

## How to run a book

1. In the Code tab, type `/new-book` and describe your idea in a sentence or two.
2. Follow the stages. Say `approved` at each gate or tell Claude what to change.
3. If you stop, say `continue` or `RESUME` and Claude reads `status.md` / `PROGRESS.md` and picks up.

## The stages (slash commands)

| Stage | Command | What it does |
|-------|---------|--------------|
| 0 | `/new-book` | Folder, profile, language, region, reader, image budget, heading style, brief |
| 1 | `/market-research` | Live Amazon research: demand, competitors, profitability, gap analysis, GO / CAUTION / NO-GO |
| 2 | `/title-check` | Trademark and KDP-rule screen, seven subtitle options with a recommendation |
| 3 | `/outline-book` | Architecture lock, terminology table, style guide, book bible, then the AUTONOMOUS or STANDARD question |
| 4 | `/design-interior` | Heading style 1 to 7 and accent (Word) or full color interior (general) with a sample |
| 5 | `/write-chapter 1` | Writes the chapter, then fact-check, Amazon review, images, editorial audit and preview |
| 6 | `/assemble-book` | Final manuscript, QC report, final compliance pass, clearance pack |
| 7 | `/clinical-clearance` | Review pack for your clinician or engineer, and `APPLY CORRECTIONS` afterwards |
| 8 | `/kdp-metadata` | Live research, three descriptions, final description, seven backend keywords |
| 9 | `/kdp-upload-guide` | Manual step-by-step KDP checklist with the AI-disclosure facts |

Separate gates you can also call on their own: `/fact-check`, `/amazon-compliance`, `/editorial-audit`, `/preview-chapter`, `/interior-images`.

## Rules the studio follows

- Every idea and every title is checked live on Amazon for profitability and gaps before you invest in writing.
- Every fact, number and calculation is verified or removed. Nothing is invented.
- Every chapter, the outline, the metadata and the final manuscript are reviewed against Amazon's live policies and for customer experience.
- Permission questions come before any browser action. Claude never signs in to Amazon.
- Engineering and medical books are NOT cleared by Claude. A qualified human reviewer must clear them before you publish them as authoritative.

## Where your files are

Every book lives in `books/<book-name>/`:

- `chapters/` Markdown source (the master text)
- `previews/` per-chapter Word and PDF
- `final/` the manuscript (Word and PDF test copy), `qc-report.md`, metadata Word file, `KDP-UPLOAD-GUIDE.md`
- `verification-log.md` the fact ledger, `compliance/` the Amazon reviews, `audits/` editorial audits
- `status.md`, `PROGRESS.md`, `run-log.md` where the book stands

## Honest limits

- Contents and index page numbers in the Word manuscript are calculated from a LibreOffice layout. Word may paginate slightly differently, so check a few entries in Word.
- Equations are native Word equations. They may not draw in the PDF test copy unless LibreOffice Math is installed; check them in Word.
- Live research depends on the web and browser access in your session. If it is not available Claude says so and stops; it does not guess.
- Claude does not design the cover or upload to KDP. Amazon asks you to disclose AI-generated content; the guide gives you the facts to answer accurately.
- Check anything important yourself before publishing, especially health, legal, safety and money topics.
