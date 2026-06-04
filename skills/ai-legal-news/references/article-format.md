# AI Legal News — Article document format (LOCKED house style)

This is the single source of truth for the weekly `.docx` look. The goal is **byte-for-byte
consistent formatting week to week**: same fonts, sizes, spacing, structure, and note style on
every article. Apply these values explicitly when generating with the docx skill
(`/mnt/skills/public/docx/SKILL.md`). Do not rely on defaults and do not improvise.

## Quick spec

- **Font:** Times New Roman everywhere (body, headings, byline, endnotes).
- **Page:** US Letter, portrait, 1" margins all sides.
- **Color:** none. Everything is black; headings are bold, not colored.
- **Alignment:** left-aligned (ragged right) throughout. Do not justify.
- **Notes:** **ENDNOTES** (end of document), never footnotes. Max 3. Superscript markers.
- **Byline:** exactly `AI Legal News · [Date]` — no author name, ever. `[Date]` = Friday of the
  ISO week, formatted `Month D, YYYY` (e.g., `April 24, 2026`).
- **Length:** 600–700 words.

## Exact values

`w:sz` in OOXML is **half-points**, so 12pt = `24`. Spacing below is given in points (pt) and
twips (1pt = 20 twips) for direct use in the docx layer.

| Element | Font | Size (pt / half-pt) | Weight / style | Alignment | Spacing before / after |
|---|---|---|---|---|---|
| Title | Times New Roman | 16 / 32 | Bold | Left | 0 / 4pt (80 twips) |
| Subtitle (optional) | Times New Roman | 13 / 26 | Italic, regular weight | Left | 0 / 8pt (160 twips) |
| Byline | Times New Roman | 11 / 22 | Italic, regular weight | Left | 0 / 12pt (240 twips) |
| H1 (Background / Analysis / Takeaways) | Times New Roman | 14 / 28 | Bold | Left | 12pt (240) / 6pt (120) |
| H2 sub-heading | Times New Roman | 12 / 24 | Bold | Left | 8pt (160) / 4pt (80) |
| Body paragraph | Times New Roman | 12 / 24 | Regular | Left | 0 / 8pt (160), line 1.15 |
| Takeaways bullet | Times New Roman | 12 / 24 | Regular | Left | 0 / 4pt (80) per item |
| Endnote text | Times New Roman | 10 / 20 | Regular | Left | 0 / 0 |

Body line spacing 1.15 = `<w:spacing w:line="276" w:lineRule="auto"/>`.

## Fixed structure (same order every article)

```
[Title]                              ← 16pt bold
[Subtitle]                           ← 13pt italic (optional; omit if redundant)
AI Legal News · April 24, 2026       ← 11pt italic byline, no author

[Lead paragraph — no heading]        ← 12pt body; states what happened

Background                           ← 14pt bold H1
[1–2 body paragraphs]

Analysis                             ← 14pt bold H1
[Optional H2 sub-heading]            ← 12pt bold
[body paragraphs]
[Optional H2 sub-heading]
[body paragraphs]

Takeaways                            ← 14pt bold H1
• [descriptive bullet]               ← 12pt body bullets, 3–5 items
• [descriptive bullet]
• [descriptive bullet]

[ENDNOTES — auto-collected at end of document, 10pt]
```

## Notes: endnotes, not footnotes

- Insert **endnotes** (Word "endnotes", rendered together at the end of the document). Never use
  page-bottom footnotes.
- Body markers are superscript numbers.
- Endnote content is Bluebook-style: case names italicized, full citation, and a **live hyperlink**
  to the primary source (court opinion, Federal Register, agency release, SEC filing, etc.).
- If the generation path produces footnotes by default, explicitly author them as endnotes (or move
  them) before saving. Verify the final file has an endnotes part and no footnotes part.

## Inline conventions

- **Case names** italicized everywhere they appear.
- **Primary-source citations** hyperlinked (standard blue underline).
- Em dashes for asides; single space after periods.
- No advice/recommendations anywhere (see the strict no-advice rule in `SKILL.md`). Takeaways are
  descriptive statements of fact, doctrine, posture, or open questions — not action items.

## Filename and location

- Folder: `articles` subfolder, written **by folder ID** `13sq6qNqdVz144cN576Zq-7NDcYRh8CXw`
  (never by path, never to My Drive root).
- Filename: `AILegalNews_YYYY-MM-DD_short-slug.docx`, date = Friday of the ISO week, slug =
  lowercase-hyphen topic (e.g., `AILegalNews_2026-04-24_fascsa-dc-circuit-anthropic-stay.docx`).

## Optional: starter template

For maximum fidelity, keep a `references/house-style.docx` in the skill bundle whose paragraph
styles ("Title", "Heading 1", "Heading 2", "Normal", "Endnote Text") are already defined to the
values above. Start each article by copying that template and filling content, so the style
definitions are identical every week rather than re-applied by hand.
