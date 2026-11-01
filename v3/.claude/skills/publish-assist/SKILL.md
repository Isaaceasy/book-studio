---
name: publish-assist
description: Prepares the release packet for each supported publishing platform (Amazon KDP, and optionally IngramSpark, Draft2Digital, Google Play Books, Kobo Writing Life, ACX or audiobook distributors) with every file, every field value and a step-by-step checklist, and offers an optional co-pilot mode in which the owner is signed in themselves and Claude only reads the screen and suggests field values. Claude never signs in, uploads, submits, publishes or pays; the owner makes every click. Use after /kdp-metadata and /kdp-upload-guide.
---

# /publish-assist: RELEASE PACKETS AND THE GUIDED CHECKLIST

## Purpose
GENIE Max "publishing automation: assists with publishing across supported platforms; the customer retains the final publish click." V3 keeps the owner's standing rule 6 (never publish, upload, log in or pay), so assistance means preparation and guidance, not action.

## The two modes
- **Packet mode (default, always available):** for each platform produce a ready-to-use folder and checklist. The owner does everything in their own browser.
- **Co-pilot mode (opt-in, needs the owner's written decision):** set `publish_copilot: true` in `book.yaml` only if the owner explicitly changes rule 6 for this purpose in writing. In co-pilot mode the OWNER signs in and stays in control; Claude (with Claude in Chrome and the owner's per-action permission) may read what is on screen, compare the visible field values with the packet, and tell the owner which field to correct. Claude still never types credentials, never clicks Publish, Submit, Confirm or Pay, never changes account, tax, bank or payment settings, and never accepts terms. If the owner has not changed rule 6, packet mode only.

## Inputs
`release/` assets (interior PDF or EPUB, covers, A+ content, metadata, AI-disclosure facts), `final/KDP-upload-guide.md`, `status.md`, `docs/kdp-specs.md`, `docs/lessons-learned.md`.

## Procedure
1. **Pick platforms** (ask once): which platforms and formats; whether the owner wants wide distribution or exclusivity programs (verify live what each requires; some programs restrict other distribution, state the trade-off honestly and let the owner decide).
2. **Verify live** each platform's current requirements and record dates: file formats, cover specs, metadata fields and limits, pricing and royalty rules, AI-disclosure questions, content guidelines, tax and payment setup (the owner does these; Claude does not touch them).
3. **Build the packet** `release/<platform>/`:
   - `files/` (exact upload files with checksums in `MANIFEST.md`),
   - `fields.md` (every field with the exact value to enter: title, subtitle, series, edition, author, contributors, description (readable and HTML), keywords, categories, language, publication date, ISBN choice, territories, price per marketplace with the computed royalty, print options (ink, paper, trim, bleed), AI-generated content answers, adult content answer, preview settings),
   - `checklist.md` (ordered, with a tick box and a "verify on screen" note for each step, ending with the proof-copy step and the final click reserved for the owner),
   - `risks.md` (what commonly causes rejection: margin errors, low-resolution images, metadata mismatch with the cover, missing alt text for ebooks, trademark words in keywords).
4. **Pre-flight run** before the owner starts: re-run `scripts/preflight_interior.py` and `scripts/preflight_cover.py`; confirm title strings match across cover, title page and fields; confirm the AI-disclosure facts equal `status.md`.
5. **Walkthrough (optional, co-pilot)**: if enabled, work screen by screen as described above; stop immediately if a page asks for credentials, payment, tax or legal acceptance and hand control to the owner.
6. **After publication** (owner reports): record the live URLs, ASINs and publication dates in `status.md`, check the live listing against the packet, and hand over to `/launch-manager`.

## Rules
- Never sign in, upload, submit, publish, pay, accept terms or change account settings. The owner makes every publish click.
- Never claim a platform accepts something you have not verified live.
