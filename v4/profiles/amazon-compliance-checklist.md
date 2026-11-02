# AMAZON KDP COMPLIANCE AND CUSTOMER-EXPERIENCE CHECKLIST

Used by `/amazon-compliance` and by the `compliance-reviewer` agent on EVERY piece of content: idea, title, subtitle, outline, chapter, image, caption, description, keyword, cover text, author bio, and the whole manuscript.

IMPORTANT: This checklist names the TOPICS Amazon governs. It is not a copy of Amazon's rules and must not be treated as current. Before every review session, search for and open the current Amazon KDP pages listed in section A, read what they actually say today, and record the date and what you read in the review file. If a page cannot be opened, say so and mark the affected checks UNVERIFIED (never PASS).

## A. Pages to open and read (live) at the start of each review session

Find the current pages with WebSearch / the browser; do not rely on remembered URLs.
1. KDP Content Guidelines (what content is allowed, prohibited, and "disappointing customer experience" rules).
2. KDP Terms and Conditions (rights, content, termination, prohibited conduct).
3. KDP metadata guidelines (title, subtitle, series, author name, description, keywords, categories, edition).
4. KDP policy on AI-generated content (definitions of AI-generated vs AI-assisted, disclosure requirement for text, images and translations).
5. KDP rules on public domain content, duplicate or very similar content, and low-content / no-content books.
6. KDP rules on reviews, review manipulation, and promotions in metadata.
7. KDP print requirements (trim, margins by page count, minimum page count, bleed, fonts, images, cover).
8. For health and medical books: Amazon's policies on medical and health content, misinformation, and claims.
9. For the book's marketplace: any marketplace-specific differences (language, regional legal requirements).

## B. Content compliance checks (every piece)

For each check give PASS / FIX / BLOCK / UNVERIFIED and one line of evidence.

1. **Illegal or infringing content.** No copyright infringement, no copied passages, no unlicensed images, no trademark misuse, no defamation, no privacy violations, no personal data.
2. **Originality and "web-scraped" content.** Text is fresh, not copied or lightly paraphrased from other sources; not a collection of public-domain or freely available material without meaningful value added.
3. **Duplicate or very similar content.** Not substantially similar to another book by the same publisher or anyone else; not a re-skin of earlier files.
4. **Low-content / thin content.** The book has genuine substantive content; no padding, filler, repetition, blank or near-blank pages, or content that exists only to hit a length.
5. **Offensive, hateful, harmful or dangerous content.** None; sensitive topics (health, safety, self-harm, substance use, minors) handled with care and accurate safety messaging.
6. **Misleading content and claims.** Promise matches content; no guaranteed results, income claims, miracle or cure claims, fake credentials, fake awards, fake endorsements; no unverified superlatives ("best", "number one", "bestseller") in metadata.
7. **Medical, legal, financial and safety statements.** Accurate, qualified, current, with disclaimers where appropriate; no advice to start, stop or change prescribed treatment; no self-diagnosis encouragement.
8. **Metadata compliance.** Title, subtitle, series, contributors match the cover and title page exactly; no extra promotional words, prices, ranking claims, other authors' or brands' names, URLs, or misleading descriptors; natural language, no keyword stuffing; title + subtitle within the current limit.
9. **Description compliance.** Within the current character limit; only allowed HTML; no prices, discounts, links, contact details, review requests, testimonials, time-sensitive promotion, competitor names.
10. **Keyword compliance.** Exactly the allowed fields; relevant; no competitor, author or brand names; no trademarks; no prohibited terms ("bestseller", "free", "new", "number one", "guaranteed"); no misleading terms.
11. **Category fit.** Categories reflect the actual content.
12. **AI disclosure facts.** The log lists which parts are AI-generated or AI-assisted (text, images, translations) so the owner can answer Amazon's question accurately.
13. **Images.** Original or licensed; no real people or patient images without documented licence and consent; no third-party characters or logos; text in images legible and correct; alt text where useful; resolution suitable for print.
14. **Reviews and promotion.** Nothing in the book or metadata solicits reviews in prohibited ways, offers incentives for reviews, or manipulates ratings.
15. **Rights statements.** Copyright page contains only supplied or approved details; no invented publisher details, ISBNs, addresses or credentials.

## C. Customer-experience checks (every chapter and the whole book)

Read as a paying reader and as a hostile one-star reviewer. List the reasons a reader could be disappointed, then fix them.

1. **Promise-delivery match.** Everything promised by the title, subtitle, description and cover text is actually delivered, at the stated level and depth.
2. **Completeness.** No missing sections, unfinished examples, empty headings, placeholders, broken cross-references, drafting notes.
3. **Accuracy.** All facts verified (verification-log clear); calculations correct; no outdated information presented as current.
4. **Clarity and usefulness.** Understandable at the target reader level; logical order; defined terms; examples that help; no jargon without explanation.
5. **Writing quality.** No typos, grammar errors, inconsistent terminology, unnatural phrasing, repeated sentences, filler openers, robotic rhythm.
6. **Repetition.** No repeated explanations or examples across chapters.
7. **Formatting.** Consistent styles, readable fonts, correct margins, no text clipped or overlapping, tables and figures inside margins and readable, correct page numbers, accurate contents page, no stray blank pages, no stranded headings.
8. **Images and tables.** Sharp, relevant, correctly captioned, legible at print size, consistent style.
9. **Safety and trust.** Warnings where needed; disclaimers present; no content that could harm a reader who follows it.
10. **Value for price.** The book offers more than free web content on the same topic (confirmed by the market-research gap analysis).

## D. Verdicts

- **PASS**: every check PASS (UNVERIFIED not allowed for B1-B10).
- **REVISE**: at least one FIX; list exact fixes; re-review after fixing (maximum 3 rounds, then report to the owner).
- **BLOCK**: a check that cannot be fixed without changing the book's plan or that risks account action; stop and tell the owner.

Never soften a verdict. Never mark a check PASS without reading the item and the live policy text.

## E. Review file format

Save to `books/<slug>/compliance/<scope>-compliance.md`:
- Scope reviewed (file names), date, policy pages opened (title + date accessed + one-line takeaway each).
- Table: check, verdict, evidence, fix.
- Customer-experience risk list (likely one-star reasons and the fix for each).
- Overall verdict and next action.
