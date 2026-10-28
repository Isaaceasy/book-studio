# Design references (owner-supplied)

Photos of existing textbooks, kept ONLY as visual style references. Nothing from them (text, figures, layouts copied pixel for pixel, logos) may be reproduced in the book. Source: Google Drive folder "Medical book interior".

## What each image shows
1. ref1-open-book-tabs: open hardcover with coloured thumb tabs on the outer edges, two columns, full-colour anatomical figures, running header with the section name.
2. ref2-physiology-spread: two-column serif body; running header with page number, unit and chapter title; bold blue sans-serif subheadings; "Quick Check" callout (rounded, salmon, icon) with review questions; shaded "Box" for a diagnostic study (icon, bold box title); figure captions with a bold figure number then an italic title; full-colour labelled diagrams; coloured edge tabs.
3. ref3-orange-accent-spread: single orange accent family; tinted heading banners; orange bullet dots; tables with an orange header strip; captions introduced by "Figure N //" above a thin orange rule; clean illustrated figures.
4. ref4-red-title-spread: solid crimson heading block with white title and author line; light tinted edge tabs; light green "Summary" box with bullets; bold dark sans subheadings; serif body in two columns; centred formulas; pink/beige figure palette.
5. ref5-teal-small-spread: photo at top of page; yellow-header comparison table; peach "when to seek care" style callout box with icon; teal edge.

## Common elements (candidate house look)
- Serif body text, bold sans-serif subheadings.
- One accent colour family with tinted boxes.
- Callout boxes with a small icon: review questions, key points/summary, diagnostic or clinical notes, when to seek care.
- Running header (chapter or Part title, page number).
- Full-colour, labelled figures with numbered captions.
- Coloured tabs along the outer page edge marking each Part.
- Two-column text (refs 1, 2, 4).

## Decisions (owner, 2026-10-28)
- Owner chose a FULL CHANGE of the Word interior: two-column text, sans-serif subheadings, new fonts, coloured edge tabs, icon callouts. The standard house style (single column, Times New Roman 12 pt, drop caps) does NOT apply to this book once the new design is approved.
- Owner asked Claude to study all five references and pick the best look.
- Claude's pick (to be shown as a sample in /design-interior for approval): crimson accent (suits emergency medicine) with the ref4 solid heading block and summary box, ref2 callout system (Quick Check review questions, shaded clinical boxes, bold-number italic-title captions, running header), ref3 tinted table headers and thin-rule captions, and one coloured edge tab per Part.
- Fonts, sizes and exact colours are set at Stage 4, using fonts that embed and render in both Word and LibreOffice.
- Implementation is deferred to Stage 4 (/design-interior): it needs a book-specific house-style profile and changes to scripts/docxbuild.py (two sections/columns, edge tabs, callout styles, revised automatic checks). Existing house-style checks stay for any other book.
- Still required by Amazon/standing rules: no hyperlinks, no copied figures or text from the reference books, AI image disclosure.
