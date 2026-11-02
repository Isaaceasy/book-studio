---
name: author-brand
description: Creates the author brand kit for the owner's catalog: author page copy for the marketplaces, a single-page author landing page (HTML), reader-magnet materials (a useful bonus PDF or checklist drawn from the owner's own books), email welcome copy and consistent brand tokens (colors, fonts, bio rules). Uses only facts and credentials the owner supplies; never invents a bio, photo, endorsement or credential. Use after the first book is ready or when the owner wants catalog branding.
---

# /author-brand: AUTHOR PAGES, LANDING PAGE AND READER MAGNET

## Purpose
GENIE Max "author brand kit: coordinated author-page assets, landing pages and reader-magnet materials for a more consistent long-term catalog presence."

## Inputs
The owner's supplied facts: author or pen name, short true bio, credentials they confirm, photo they own (or none), website or newsletter provider (if any), social handles they want listed, catalog (`books/*/book.yaml`), existing assets (for example `author_landing_page.html` the owner may already have; read it first and keep what works), brand colors and fonts, `docs/lessons-learned.md`.

## Procedure
1. **Read what exists** (existing landing page, current author bio, existing brand colors) and ask one question block for anything missing: author name as printed, bio facts, credentials to state (only those the owner confirms), photo yes or no, newsletter or contact method, tone (warm expert, straight-talking, teacher), and what free bonus fits the catalog.
2. **Brand tokens** `brand/brand-tokens.md`: palette, fonts, logo-free wordmark text treatment, voice rules, claims rules (no income promises, no unverified credentials, no health outcome promises), bio templates (50, 100 and 200 words) built only from supplied facts.
3. **Author page copy** `brand/author-page.md` for each marketplace the owner publishes on (US plus others, in the matching language), with the live Amazon Author Central rules recorded (verify live: photo, bio length, links).
4. **Landing page** `brand/landing/index.html` (+ CSS): one responsive page with an author intro, the catalog (covers and links the owner inserts after publication), a reader-magnet signup block (a placeholder form action the owner replaces with their provider; do not collect data yourself), privacy and disclaimer lines, no tracking scripts by default, accessible markup. Validate that it renders at phone and desktop width.
5. **Reader magnet** `brand/reader-magnet/`: a short, genuinely useful PDF (checklist, quick-reference sheet, sample chapter, printable) generated from the owner's own verified content, with no claims beyond the books, consistent design, and a plain disclaimer; check it with `/fact-check` if it carries factual content.
6. **Email welcome sequence** (3 emails) drafted for the owner's provider: who they are, the free bonus delivered, what to expect, an unsubscribe reminder; no fake urgency, no pressure.
7. **Compliance**: `/amazon-compliance` scope `brand` (no review solicitation tricks, no misleading claims, no competitor names).
8. **Deliver** `brand/` and update `status.md`. The owner publishes the page and sends emails themselves.

## Rules
- Facts and credentials come only from the owner. Never invent an author photo, bio, award or testimonial.
- No data collection by Claude; no tracking without the owner's explicit choice and consent notice.
