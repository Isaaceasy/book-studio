# Fonts used by the book build

`InterTT-*.ttf` are TrueType copies of the Inter sans-serif (SIL Open Font License, from the Inter OpenType files installed on the build machine). They were made because Chromium writes the original CFF-based Inter into the PDF as Type 3 fonts, which KDP's font checker does not describe. The TrueType copies embed as ordinary TrueType subsets.

To build the book on another computer, copy these five files into the user font folder (for example `~/.fonts` on Linux) and run `fc-cache -f`. The family name is `InterTT`. The body font is Caladea (installed with the Carlito/Caladea font package).
