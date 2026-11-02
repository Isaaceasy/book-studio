# AUTOMATION ROADMAP: what can make the owner's work easier (ordered by payoff)

Status: BUILT in V3 / NEXT / IDEA. Everything keeps the rule that Claude never publishes, uploads, logs in or pays.

## Already built in V3
1. **One-message intake** (`/new-book`): every setting is asked in one block, so runs do not stall.
2. **Copy Market Strategy** (`/cms-research`): competitor table, USP table, gap analysis, unit economics, product spec in one pass.
3. **Title lab** (`/title-lab`): 15 or more modeled candidates with technique labels, collision, autocomplete, trademark, KDP rules and a scored table.
4. **Trademark page scanner** (`scripts/tm_scan.py`): reads the pages the owner saves from the USPTO site and lists live marks, classes and owners.
5. **Cover pipeline** (`/cover-design`): spine and wrap calculator, exact-text composer, preflight, thumbnail test, ebook cover at 2,560 x 1,600.
6. **Interior library** (`interiors/`): upload references, get style cards, build colored, unique interiors faster.
7. **Interior preflight** (`scripts/preflight_interior.py`): page size, fonts, links, blank pages, odd page count.
8. **Puzzle generator with verification** (`scripts/puzzle_gen.py`).
9. **Coloring page cleaner** (`scripts/line_art_clean.py`).
10. **Ads analyzer** (`scripts/ads_analyze.py`): the owner's Manual Campaign Plan rules applied to real exports, currencies kept apart.
11. **Royalty report** (`scripts/royalty_report.py`).
12. **Retro stage** (`/lessons`): every book improves the framework.

## Built in V4 (2026-11-02)
`/genie` conductor, `/ebook-build` + `ebook_build.py`, `/risk-analysis` + register, `doctor.py`, `manuscript_lint.py`, `status_keeper.py`, `release_pack.py`, `catalog.py`, `git_helper.py`, queue file. These replace NEXT items 1, 2, 9, 10 and part of 4 below.

## STILL TO BUILD (V4 backlog)
1. `figure_pipeline.py` batch runner (HiggsField is an assistant tool, so the batch loop lives in the skill; a script can only write the Figure Log and contact sheet from the downloaded files).
2. Keyword harvest sheet, ads bulk-sheet generator, scheduled research refresh, gate notifications.
3. Mac test; EPUBCheck integration; translation pipeline; proof-copy checklist generator.

## NEXT (recommended build order, V3 list kept for reference)
1. **Auto-commit and push helper** for each stage; a one-click "push for cloud" instruction, and a small script that finds the Git client when `git` is not on PATH.
2. **Status keeper**: a script that rewrites the top of `status.md` from the checklist and moves superseded decisions to the archive, so the file never contradicts itself.
3. **Figure pipeline script**: batch HiggsField generation with retry on rate limits, Figure Log writing, self-check (size, no text), and a contact sheet for the owner's quick review.
4. **Reference and fact ledger tooling**: a script that tracks claims, sources opened (with saved page snapshots) and open items, and exports the clearance pack automatically.
5. **Keyword harvest sheet**: from the CMS autocomplete runs, produce the seven-keyword evidence table skeleton.
6. **Phone notifications at gates**: Remote Control or the app's notifications when a stage needs approval, so long cloud runs wait for a tap, not a visit to the desk.
7. **Scheduled research refresh**: a monthly task that re-reads rank and price for the owner's titles and their top competitors and writes a one-page change report (only public pages; no sign-in).
8. **Bulk-sheet generator** for Amazon Ads (campaign, ad group, keywords, negatives) from `ads_analyze` output.
9. **Catalog dashboard**: one page listing every book, stage, open items, editions, last royalty month, ads ACOS; built from the files already in each book folder.
10. **Batch queue**: run several books' stages in sequence overnight in the cloud, stopping at each owner gate.
11. **Translation edition pipeline**: terminology table, native-term check, and a separate CMS run for the target marketplace.
12. **Proof-copy checklist generator** that compares the proof copy against the build report.

## IDEAS (need the owner's decision or an external tool)
- A paid keyword tool integration (the owner has none yet; the framework works without).
- Co-pilot mode in `/publish-assist` (needs the owner to relax rule 6 in writing).
- Audiobook generation at scale (depends on the audio tools in the session and the platforms' AI-narration policies).
- A reference-image rights tracker for the interior library (what the owner may reuse).
