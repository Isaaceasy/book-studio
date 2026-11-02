---
name: audiobook-studio
description: Turns a finished book into an audiobook package: an audio-ready script (numbers, abbreviations, figures and tables rewritten for the ear), narration with an approved voice in one or more languages using the available audio tools, chapter-by-chapter files, a retail-sample file, and a compliance checklist for the chosen audiobook platform's live technical and AI-narration rules. Never uploads. Use after /assemble-book when the owner wants audio.
---

# /audiobook-studio: NARRATION, MULTI-LANGUAGE AND STORE-COMPLIANT FILES

## Purpose
GENIE Max "audiobook studio": produce narration in multiple languages and organize store-compliant audio files for distribution workflows. The owner chooses the platform and uploads.

## Inputs
`chapters/`, `front/`, `back/` (final text), `book-bible.md` (terminology, pronunciation notes), `book.yaml` (language, region), `final/KDP-metadata.md`, the owner's platform choice, available audio tools in this session (check: HiggsField `generate_audio`, `create_voice`, `voice_change`, `dubbing` tools, or another text-to-speech tool the owner connected).

## Procedure
1. **Check tools and rules honestly.** List which audio generation tools exist in this session; if none, stop at the script stage and say so. Open and record (with dates) the live technical specifications and content policies of the chosen platform (for example Audible/ACX, KDP's audiobook options, Findaway Voices, Google Play, Spotify for Authors): file format, loudness and noise floor, sample rate and bit rate, chapter file rules, opening and closing credits, retail sample length, cover size, and the platform's current rules on AI or synthetic narration and disclosure. The live pages win. Never assume a platform accepts AI narration.
2. **Audio script** (`audio/script/NN-name.txt`): rewrite for listening: expand abbreviations and symbols, spell out numbers and units the way a narrator would say them, replace "see figure" with a spoken description or a short omission note, turn tables into a spoken summary, move or drop pure-visual material, keep terminology exactly as locked, add pronunciation guides for hard terms (IPA or respelling) in `audio/pronunciation.md`. Safety-critical text (doses, thresholds, procedures) is read exactly as written. Do not add new facts; changes are listening adaptations only.
3. **Voice plan**: choose or design a voice per language (the owner approves a 30-second sample first). No cloning of a real person's voice without documented consent. Record the tool, voice id, language and settings in `audio/audio-log.md`.
4. **Generate** chapter by chapter in chunks the tool can handle; retry on rate limits; concatenate per chapter; normalize loudness to the platform spec using the installed audio tools (for example ffmpeg if available); trim silence; add room-tone padding where required; keep a consistent sample rate.
5. **Quality control**: listen-check systematically if the tool exposes audio you can inspect (durations, silence gaps, clipping, loudness measurements); flag mispronunciations from the pronunciation list; the owner listens to sample chapters and approves before the full run. Be honest that you cannot hear the audio unless a tool returns analysis.
6. **Package** `audio/final/`: opening credits, chapters, closing credits, retail sample, metadata sheet (title, subtitle, author, narrator or voice credit as the platform requires, language, description from `/kdp-metadata`), cover per the platform spec (use `/cover-design`), and the AI-narration disclosure record.
7. **Multi-language**: translated editions require a separate book run (`/edition-expansion` translation plan and CMS for the target marketplace); do not machine-translate silently.
8. **Compliance** `/amazon-compliance` scope `audio`; deliver and update `status.md`.

## Rules
- Never upload or sign in. Never claim a human narrator. Disclose synthetic narration where the platform requires it.
- No voice that imitates a real person without documented consent.
