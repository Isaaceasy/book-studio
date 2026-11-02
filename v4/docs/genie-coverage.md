# GENIE coverage map: every capability in the owner's GENIE client guide (2026) and where V3 implements it

Source: `docs/reference-materials/GENIE_GUIDE.pdf` (Starter, Pro, Max tiers). V3 has no tiers: the owner has every capability. Status: DONE (skill and scripts exist and were exercised), SKILL (instructions written; needs a live run to prove), NEEDS OWNER DECISION (conflicts with a standing rule or needs a tool/account).

## V4 additions (the "one idea in, publish-ready book out" connected pipeline)
| GENIE principle | V4 implementation | Status |
|---|---|---|
| Eight connected stages: BRIEF, RESEARCH, WRITE, PREVIEW, DESIGN, PACKAGE, PUBLISH, GROW run as one workflow | `/genie` conductor (AUTOPILOT, resume, queue, status, grow, rollback on change) | SKILL (not yet run end to end on a fresh book) |
| "Does GENIE publish without me? No. It prepares or assists, but you make the final publish click." | CLAUDE.md rule 6 and section 9 hard stops; `release/OWNER-CHECKLIST.md` | DONE (same control line as GENIE) |
| Quality checked at every stage (trademark, readability, structure, AI-style signals, layout, page count, files) | `scripts/manuscript_lint.py`, `scripts/preflight_interior.py`, `scripts/preflight_cover.py`, editor, fact-checker, compliance agents, risk gates | DONE (lint and doctor tested on the emergency book) |
| Final production package incl. ebook | `/ebook-build`, `scripts/ebook_build.py`, `scripts/release_pack.py` | DONE (EPUB built and mechanically checked on the emergency book; EPUBCheck not run) |
| Installed on the customer's computer, Windows and Mac | `scripts/doctor.py`, `requirements.txt`, folder is self-contained | DONE for Windows; Mac untested |
| Unlimited books, no per-book credits | `books/_queue.md`, `/genie queue`, `scripts/catalog.py` | SKILL |

## Starter: write
| GENIE capability | V3 implementation | Status |
|---|---|---|
| Full writing pipeline (plan and write chapter by chapter in the approved niche, structure, audience, language) | `/new-book`, `/outline-book`, `/write-chapter`, profiles, `CLAUDE.md` sections 2 to 9 | DONE (proved on the emergency nursing book) |
| Trademark title gate (screen every title before drafting; develop safer alternatives) | `/title-lab` (generate, test, score), `/title-check`, `scripts/tm_scan.py` reading the owner's saved USPTO pages | DONE |
| Premium color interiors (book-specific palette, readable hierarchy, page composition) | `/design-interior` + the interior library (`interiors/`, `/interior-library`) | DONE (library started with the owner's references) |
| Risk analysis (what could go wrong before publishing; legal, policy, market, safety, rights, technical, account) | `/risk-analysis`, `templates/risk-register.md`, gates R1 R2 R3 (blocks `/kdp-upload-guide` and `/publish-assist`) | SKILL (added 2026-11-02, untested on a full book) |
| Embedded interior images | `/interior-images`, HiggsField, image tiers and Figure Log (`CLAUDE.md` 11b) | DONE |
| Editorial quality audits (readability, tone, structure, human-sounding prose, consistency, AI-style signals) | `/editorial-audit` with the editor agent; added audit for answer-key length bias | DONE |
| Word + print-exact PDF previews per chapter | `/preview-chapter`, `scripts/bookbuild.py`, `scripts/docxbuild.py` | DONE |
| KDP upload guidance (manual step by step) | `/kdp-upload-guide`, `/publish-assist` packet mode | DONE |
| Final production package (assemble, verify margins and pagination, update TOC, preserve sources) | `/assemble-book`, `scripts/assemble_kdp.py`, `scripts/preflight_interior.py` | DONE |

## Pro: write + design + research
| GENIE capability | V3 implementation | Status |
|---|---|---|
| Niche discovery (opportunities from live signals, buyer intent, competition, category fit) | `/niche-discovery` | SKILL |
| Market intelligence (competitor tables, gap analysis, price bands, category options, keyword intelligence, evidence-backed positioning) | `/cms-research` (Copy Market Strategy) with `competitors.csv`, USP table, positioning map, unit economics, model blueprint; `docs/cms-browser-snippets.md` | DONE (method proved; improved) |
| Complete cover production (front, back, spine, measured full wrap for trim, format and page count) | `/cover-design`, `scripts/cover_calc.py`, `scripts/cover_compose.py`, `scripts/preflight_cover.py` | DONE (scripts tested; art step needs HiggsField run) |
| A+ content graphics (coordinated storefront set) | `/aplus-content` | SKILL |
| Store metadata package (description, 7 backend keywords, categories in a separate document) | `/kdp-metadata` (from the owner's EMB KDP Description and Backend Keyword Framework) | DONE |
| Puzzle and coloring studios (real puzzle content with verified answer logic; clean line art) | `/puzzle-studio` + `scripts/puzzle_gen.py` (sudoku with unique solution, word search with exactly-once words, mazes); `/coloring-studio` + `scripts/line_art_clean.py` | DONE (puzzle script verified; coloring needs a live HiggsField run) |
| Hardcover and large-print editions | `/edition-expansion` | SKILL |
| Current interior reference bank | `interiors/` folder, `/interior-library`, `INDEX.md` | DONE |

## Max: publish + grow
| GENIE capability | V3 implementation | Status |
|---|---|---|
| Publishing automation across supported platforms; the customer keeps the final click | `/publish-assist`: packet mode (always) and an opt-in co-pilot mode where the owner is signed in and Claude only reads and suggests | NEEDS OWNER DECISION (standing rule 6 forbids uploading, logging in and submitting; co-pilot mode needs the owner's written change to rule 6) |
| Audiobook studio (multi-language narration, store-compliant files) | `/audiobook-studio` (script adaptation, voice plan, generation with available audio tools, loudness and format checks, platform rules read live) | SKILL (depends on audio tools in the session; AI narration policies are verified live) |
| Ads manager (campaigns, weekly optimization, budget awareness, honest math on real data) | `/ads-manager` + `scripts/ads_analyze.py`, reproducing the owner's Manual Campaign Plan rules (break-even ACOS, harvest, negate, bid down and up) on their real Search Term and Targeting exports | DONE (analyzer tested on the owner's September exports; plan and bulk sheets are generated per book) |
| 30-day launch manager | `/launch-manager` | SKILL |
| Review monitoring and correction pipeline (no fabrication or manipulation) | `/review-monitor` | SKILL |
| Royalty reporting from real sales data | `/royalty-report` + `scripts/royalty_report.py` | DONE (script written; needs a real KDP export to confirm column mapping) |
| Author brand kit (author pages, landing pages, reader magnets) | `/author-brand` (reads and improves the owner's existing `author_landing_page.html`) | SKILL |

## Quality and honesty principles from the guide (kept)
Quality gates at every stage (trademark, readability, structure, AI-style signals, layout, page count, files); no per-book credits; the real book chapter by chapter in Word and print-exact PDF; honest by construction: no fabricated sources, reviews, sales data, credentials or income promises; AI assistance disclosed per platform policy; no guarantee of sales, ranking or bestseller status; the owner approves final actions and makes every publish click; existing files remain the owner's.

## Honest gaps to close next (in order)
1. Run `/cover-design` end to end on a real book with HiggsField art, then view the wrap in KDP's cover previewer.
2. Run `/niche-discovery` and `/cms-research` on a fresh idea to harden the browser snippets.
3. Run `/royalty-report` on a real KDP export and fix the column map.
4. Decide on co-pilot mode for `/publish-assist` (rule 6).
5. Test `/audiobook-studio` with the audio tools available in a session.
