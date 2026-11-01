# LESSONS LEARNED (read at every session start)

Format: what happened, why it mattered, the rule or check that prevents it, where it lives. Newest at the bottom. Mark a lesson SUPERSEDED rather than deleting it.

## Book 1: Emergency Nursing Fundamentals (2026-10-28 to 2026-11-02)

L1. **Decide the product format before the title and outline.** The book started as 12 Parts, US Letter, 50 figures, about $40 to $50. After research and the owner's questions it became 6 Parts, 5 x 8 in, 25 figures, $20 to $25. Each change meant redoing economics, title, outline and design. Rule: `/cms-research` ends with an approved PRODUCT SPEC (trim, ink, length, figures, price band, positioning); changing it restarts research. Lives in: `cms-research` Step 9, CLAUDE.md section 11.

L2. **Amazon pages and fetch tools.** Fetch tools returned HTTP 503 on Amazon, so the first research run had no competitor data. The built-in browser worked after setting the delivery location (it showed Nigeria and foreign currency until set to a US ZIP). Reading result lists and product pages with a small in-page script was fast and reliable. Reviews need a sign-in; never sign in, ask the owner to paste. Lives in: `cms-research` Step 1 and `docs/cms-browser-snippets.md`.

L3. **Autocomplete honesty.** Typing into the real search box and calling the suggestion service from the page both show the same short list; say which was done. Signals only. Lives in: `cms-research` Step 2.

L4. **Trademark risk is in the title word.** "Essentials" collided with a live registered book mark owned by another company; "Emergency Nursing" is closely tied to a professional association's live marks. The USPTO site was not searchable by the assistant; the owner saved result pages and `scripts/tm_scan.py` extracted the live marks. Rule: owner-run registry search is a named step; never mark LOW risk without a registry search; avoid common series words. Lives in: `title-lab` C3.

L5. **Do not call a 5 x 8 book "pocket".** KDP's smallest US paperback trim is 5 x 8 in; real pocket references are smaller. Use "Compact". Lives in: CLAUDE.md section 8.

L6. **Reviewer agents have no write tool.** Compliance reports came back as messages; the main session must save them. Three review rounds were enough; each round found real problems (promise vs content, dosing wording, word budget arithmetic, forward references, claim wording). Rule: cap at 3 rounds; main session saves the report. Lives in: CLAUDE.md rule 16.

L7. **Word budgets and review questions.** Budgets that ignore callouts, captions and the real length of questions come in under the floor. Plan 5 to 10 percent above the floor and budget review questions at realistic length. Lives in: CLAUDE.md rule 14.

L8. **"No dose figures" was ambiguous.** The book needs compression rate and tourniquet timing but no medicine doses. Rule: define "no medicine doses; verified procedural parameters allowed" up front and use the same words everywhere. Lives in: `profiles/medical.md`.

L9. **Forward references.** An early entry needed concepts taught later (shock, low glucose). Handle with one-sentence plain-text bridges listed in the outline. Lives in: `outline-book`.

L10. **Stale status files.** The status file kept withdrawn decisions and contradicted itself (clearance "named, none" above and "cleared" below). Rule: one source of truth; move superseded decisions to `status-archive.md`; update the top line first. Lives in: CLAUDE.md rule 15.

L11. **Clearance needs a paper trail.** The owner reported verbally that the clinician cleared everything; the framework recorded it "on the owner's word". V3 requires a sign-off record file and the reference to the written sign-off. Lives in: CLAUDE.md 11b item 4, `templates/signoff-record.md`.

L12. **Image tools.** HiggsField returned rate-limit errors (retry), refused some prompts with a content filter (change the prompt, do not paste filter-triggering words), drew the wrong side or pose (mirror or regenerate and have the expert confirm), added no text when told, and produced hands and equipment that need review. Keep a Figure Log with job ids. AI image terms were read from the official terms page and recorded. Lives in: `interior-images`, CLAUDE.md 11b item 5.

L13. **Design had to adapt.** The owner's reference interiors were two-column Letter-size layouts; on a 5 x 8 page a two-column body is unreadable. Document the adaptation and ask the owner to confirm. Lives in: `interior-library` adaptation notes.

L14. **Git and cloud.** A cloud session starts from the pushed branch only. The assistant's shell had no GitHub credentials, so the owner pushed with their Git client. The shell had no `git` on PATH (GitHub Desktop's bundled git worked). Cloud sessions are not visible to local session tools; their work arrives as commits on a new branch. Lives in: CLAUDE.md rules 17 and section 9.

L15. **Quality traps in generated review questions.** About 80 percent of correct answers were the longest option. Add a length-bias check to the editorial audit. Lives in: `editorial-audit`.

L16. **Collect decisions in one question block.** The owner answered best in short multiple-choice blocks of up to four questions; long chains of single questions slowed the run. Lives in: CLAUDE.md section 5.

L17. **Cover art resolution.** HiggsField images came out at 688 x 1024 px, far below the 300 dpi a 5 x 8 in wrap needs (about 1575 x 2475 px). Use the upscale tool (4K) on the chosen art before composing, and record the upscale job ids; check the proof copy for softness. Lives in: `cover-design` Step 5.

L18. **Cover scripting traps.** (a) Chromium blocks local file links when a page is built in memory: embed art as data URIs. (b) Variable system fonts become Type 3 in the PDF: embed static TrueType files. (c) Chromium rounds PDF page size up to whole points (0.012 in on this wrap): set the exact media box afterward (cropping into the bleed). (d) Spine text reads top to bottom for US books. (e) Keep the art lower on the front panel so illustrations never run under the title block. Lives in: `scripts/cover_compose.py`.

L19. **Back-cover copy must stand alone.** A sentence lifted from a description section ("Nursing, paramedic, EMT ... students ...") had no verb without its heading and read like a typo on the cover. Check cover copy as free-standing text, and record deliberate differences from the description. Lives in: `cover-design` Step 8 compliance.

L20. **Competitor covers.** Look at the actual covers (a contact sheet is enough): the nursing niche was crowded with red, cartoon nurses, heartbeat lines and badges, which pointed to a calm dark poster concept. Lives in: `cms-research` Step 3 (cover notes).

L21. **Geometric concepts need no AI art.** A cover concept built from simple shapes (discs, bands, blocks) is drawn by script: sharp at any size, no resolution or upscale problem, no AI-image disclosure for the art, no anatomy to check. Ask for the style change before spending image credits. Overlapping shapes hide labels: draw from the back forward and place each label in the visible part. Lives in: scripts/art_discs.py, cover-design Step 4.
