---
name: ai-legal-news-weekly
description: Writes the WEEKLY "AI Legal News" articles only — the second of two AI Legal News skills. Use when the user or a Claude Routine asks for the AI Legal News weekly writeup, weekly AI article, hot topics, or top stories of the week. Runs unattended and non-interactively: reads the most recent daily-log snapshot on Google Drive, ranks the week's entries by a hotness rubric, automatically selects the top 2 (different practice areas where possible), and drafts them as .docx articles of 600 words max each (Georgia font, black headings, Word endnotes, blue hyperlinked citations, fixed "AI Legal News · [Date]" byline) saved to the articles folder — never asking which to write. Do NOT use for the daily log capture (use the ai-legal-news-log skill) or for non-US / non-legal AI news.
---

# AI Legal News — Weekly Articles

This is **one of two** AI Legal News skills. It does **only** the weekly article writeup for Greg's
"AI Legal News" series. The daily log capture is a **separate** skill (`ai-legal-news-log`) — do not
search for or write daily log entries here. This skill **reads** the log the other skill produced
and turns the week's top stories into finished `.docx` articles.

> **Unattended — fully non-interactive.** This runs on a schedule with no human watching. NEVER ask
> the user which articles to write, present a menu, or wait for a selection. Rank the week's
> candidates, **auto-select the top 2**, write both, and save them autonomously. Reaching the end of
> a run without having written and saved 2 articles (or fewer only if the week genuinely has fewer
> than 2 rankable stories) is a failure.

---

## Where the log lives (read-only for this skill)

The daily log is stored as **dated snapshots** in the `AI-legal-log` folder, ID
**`1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3`**. To get the current log:

- `search_files` with `parentId = '1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3' and title contains
  'master-log'`, then take the file with the most recent `modifiedTime` (newest-modified is
  canonical, regardless of exact filename). `read_file_content` to get its text.
- This skill never writes to the log folder. It only **reads** the snapshot and **writes articles**
  to the `articles` subfolder, ID **`13sq6qNqdVz144cN576Zq-7NDcYRh8CXw`** (always by folder ID,
  never by path — path writes fall back to My Drive root).

---

## Workflow

**1. Read the week's log.** Resolve the newest `master-log_*` snapshot (above). Pull entries from
Monday of the current ISO week through today (Friday) — typically up to ~25 entries (5 × 5 days),
may be fewer.

**2. Rank by hotness.** Score every candidate with the rubric below (full version in
`references/article-template.md`).

**3. Auto-select the top 2.** Pick the **2 highest-scoring** stories. **Diversity rule:** if the top
2 fall in the same substantive category, swap the lower one for the next-highest-scoring story in a
*different* category, so the two articles cover different practice areas. Do not ask; do not wait.
You may print a short ranked shortlist in the chat reply for the record, then proceed straight to
drafting.

**4. Re-verify primary sources** for the 2 selected stories. Re-read the opinion, rule, order, or
filing — don't rely on the one-line log summary. Pull related primary documents where the analysis
depends on them (underlying complaint, distinguished opinions, agency comment record, latest S-1
amendment). Re-check pin cites and any short quotes.

**5. Draft each article** as a separate `.docx`, following **`references/article-template.md`** — the
authoritative spec for structure, voice, the no-advice rule, citation/endnote format, and the
docx-js generation pattern (including the endnote hyperlink fix). Generate with the docx skill
(`/mnt/skills/public/docx/SKILL.md`); do not hand-write XML and do not improvise typography. Locked
essentials are summarized under "House style" below.

**6. Save** each `.docx` to the `articles` subfolder **by ID** with `create_file`:
`parentId = '13sq6qNqdVz144cN576Zq-7NDcYRh8CXw'`,
`title = 'AILegalNews_YYYY-MM-DD_short-slug.docx'` (date = Friday of the week; slug =
lowercase-hyphen topic). Never write by path and never to My Drive root.

**7. Report in chat** (brief, no questions): the two article titles, word counts, endnote counts,
and the `articles/` filenames.

---

## Ranking rubric (summary)

Score each candidate; total ranks the set (full rubric, 0–16 scale, in
`references/article-template.md`):

1. **Precedential/regulatory weight (0–5)** — SCOTUS > circuit split > circuit > district > final
   rule > proposed rule > guidance > bill > hearing.
2. **Breadth of practice impact (0–4)** — how many in-house counsel are directly affected.
3. **Novelty (0–3)** — first-of-kind vs. incremental.
4. **Doctrinal consequence (0–3)** — opens/closes a theory of liability, jurisdiction, or agency
   authority; deepens a split (descriptive, not advice).
5. **Patent/IP bonus (0–1)** — for COPYRIGHT/PATENT/PTAB/USPTO/TRADEMARK/TRADE-SECRETS/PUBLICITY.
6. **Tie-break: resonance** — how much the bar is actively discussing it this week.

The substantive tag on each log entry (`[SUBSTANTIVE / POSTURE]`) defines its category for the
diversity rule.

---

## House style (at a glance — full spec in `references/article-template.md`)

- **Font:** Georgia throughout. US Letter, 1" margins. **Headings are bold black (`000000`), never blue** — Word's default Heading styles are blue, so set the color explicitly.
- **Heading scale:** Title 14pt bold · section heads (`Background` / `Analysis` / `Takeaways`)
  12pt bold · sub-heads inside Analysis 11pt bold. Body Georgia 12pt. Byline 11pt italic.
  Endnotes 10pt.
- **Byline:** exactly `AI Legal News · [Date]` — **no author, no placeholder**. `[Date]` = Friday of
  the ISO week (e.g., `April 24, 2026`).
- **Notes:** Word **endnotes** (max 3), never footnotes.
- **Citations:** every primary-source citation is a live **blue** hyperlink (`0563C1`, underlined) —
  never plain text. Generation detail: set color/underline directly on the hyperlink's `TextRun`;
  do **not** declare a `Hyperlink` paragraph style (it collides with docx-js and renders links
  black). See `references/article-template.md`.
- **Length/structure:** **600 words maximum** (hard ceiling, aim ~500–600); Title → Lead → `Background` → `Analysis` (sub-heads) →
  `Takeaways` bullets. Takeaways is the only post-Analysis section and stays descriptive — **no
  advice, no predictions, no "what counsel should do."**

---

## Suggested Claude Routine prompt — Weekly, Friday 11:00am CT

> Run the AI Legal News weekly writeup. This is an unattended scheduled run — do not ask me anything
> and do not wait for input. Read this week's entries (Monday through today) from the most recent
> `master-log_*` snapshot in the `AI-legal-log` folder on Google Drive, rank them by hotness, and
> automatically select and draft the top 2 (different practice areas where possible) as .docx files of
> no more than 600 words each, with black headings, no more than 3 endnotes, a closing Takeaways
> bullet list, Bluebook-italic case names, blue hyperlinks to primary sources, and the fixed byline
> `AI Legal News · [Date]`. Save them
> to the `articles` subfolder by folder ID.

---

## Operational notes

- **Always end by saving 2 articles by folder ID** (or 1/0 only if the week genuinely lacks rankable
  stories). Never write by path; never to My Drive root.
- **Never ask which to write** — auto-select by score with the diversity rule.
- **Strict no-advice rule:** articles never tell the reader what to do, think, feel, or expect, and
  never predict outcomes. Forbidden sections include "What it means for counsel," "Action items,"
  "What to watch," "Conclusion." Takeaways bullets are descriptive only. Full rule in
  `references/article-template.md`.
- **Stay in lane:** this skill only writes articles from the existing log. It never performs the
  daily news search or writes log entries.
