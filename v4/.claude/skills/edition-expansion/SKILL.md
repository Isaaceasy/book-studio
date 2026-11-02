---
name: edition-expansion
description: Builds additional editions of a finished book from the same Markdown sources: hardcover, large print, Kindle ebook (reflowable), black-and-white economy edition, or a translated edition plan. Recomputes trim, margins, fonts, page count, print cost, royalties and cover specs per edition, reuses the verified text, and flags edition-specific compliance. Use after /assemble-book when the owner wants more formats of the same book.
---

# /edition-expansion: HARDCOVER, LARGE PRINT AND OTHER EDITIONS

## Purpose
GENIE Pro "hardcover and large-print editions with access to a current interior reference bank": turn one verified manuscript into several sellable products without rewriting it, each correctly formatted and priced.

## Inputs
`chapters/`, `front/`, `back/`, `images/`, `book.yaml`, `final/` build report, `docs/kdp-specs.md`, `interiors/INDEX.md`, `cms-research.md` (do competitors sell the edition; at what price).

## Procedure
1. **Choose editions** (ask once): hardcover; large print; Kindle ebook (reflowable); black-and-white economy edition (graphics must survive greyscale); other trim; translation (needs a new language plan and CMS run for that marketplace).
2. **Verify live rules per edition** and record dates: KDP hardcover (supported trims, minimum and maximum pages, margins, cover case-wrap specifications, availability by marketplace, royalty rules), what KDP and the marketplace treat as large print (font size and trim expectations; verify live), Kindle format and image requirements, color versus black-and-white print costs. The live pages win over this file.
3. **Create the edition folder** `editions/<edition>/` with its own `book.yaml` overrides (trim, margins, fonts, ink) and a `NOTES.md` listing every difference from the base edition.
4. **Large print:** increase body size to the live-recommended minimum or more (commonly 16 pt or above; confirm), larger leading, wider margins, simpler layout, larger figure captions and labels; rebuild figures only if needed for legibility; expect a much higher page count and recompute cost and price.
5. **Hardcover:** use KDP's hardcover trims; margins and gutter per the page count; cover is a case wrap (use `/cover-design` with the hardcover flag); check minimum page count.
6. **Ebook:** reflowable text with a linked contents (hyperlinks ARE allowed inside an ebook's navigation but NOT in the print edition's static contents; keep the two builds separate), image alt text, no fixed print page numbers, cover per KDP ebook spec; verify the title and metadata match.
7. **Economy black-and-white:** convert the palette to greyscale-safe tokens, check every colored element for printed labels and patterns, rebuild figures in grey tones, recompute print cost.
8. **Rebuild and preflight** with the base scripts and overrides; inspect rendered pages; run `/amazon-compliance` scope `edition`; make sure each edition is distinct enough not to trigger duplicate-content concerns (same book, different format is allowed; do not publish near-identical separate titles).
9. **Economics:** table per edition (page count, print cost, three prices, royalty) with arithmetic and source dates.
10. **Deliver** `editions/<edition>/final/`, the cover brief for each edition, and a note on how the editions will be linked on Amazon (owner action). Update `status.md`.

## Rules
- Do not change the verified text without re-running the affected fact-checks; layout changes only.
- Large print and hardcover pricing must come from computed print costs.
