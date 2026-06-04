---
name: ai-legal-news
description: Produces the "AI Legal News" daily log and weekly writeup for a general in-house-counsel audience covering US AI-related legal developments. MUST use whenever the user or a Claude Routine mentions AI Legal News, AI legal daily log, weekly AI legal writeup, AI hot topics, or asks for recent US AI legal developments — court decisions, agency rules, executive orders, FTC/SEC/DOJ/state AG enforcement, state AI laws, copyright and training-data litigation, chatbot liability, AV litigation, AI antitrust, USPTO and PTAB AI matters, AI company S-1 filings and IPOs, employment AI rules, or legal-ethics AI guidance. Two modes. LOG mode searches the last 24–36 hours, picks 5 top developments, verifies from primary sources, and writes a new dated snapshot of the master log on Google Drive. ARTICLE mode reads the week's log, proposes top 5 candidates by category, waits for the user to pick up to 2, and drafts 600–700 word .docx articles with Word endnotes. Do NOT use for general AI news unrelated to law or non-US developments.
---

# AI Legal News

A two-mode skill for Greg's "AI Legal News" series. Covers US legal developments at the intersection of AI and commercial practice, for a general in-house-counsel audience with a mild patent/IP lean.

The skill runs in one of two modes, selected from the prompt sent by the calling Claude Routine:

| Mode | Trigger phrases in prompt | Output |
|---|---|---|
| **LOG** | "daily log", "daily AI legal", "today's AI legal news", "daily roundup" | A new dated snapshot `master-log_YYYY-MM-DD.md` (full running log, today's 5 entries on top) in the `AI-legal-log` folder on Google Drive |
| **ARTICLE** | "weekly writeup", "weekly AI article", "hot topics", "top 5 for the week" | Interactive: propose top 5 grouped by category → user picks up to 2 → produce .docx files in the `articles` subfolder |

Detect the mode from the incoming prompt and jump to the matching section.

---

## Google Drive storage model (read this first — it governs both modes)

The Google Drive connector can **create** and **copy** files, but it **cannot update a file in place and cannot delete files**. There is no "append" or "overwrite." Every save is a brand-new file. Two rules follow from this, and they are the difference between consistent and inconsistent output:

1. **Never write to a fixed, undated filename.** Writing `master-log.md` every day does not overwrite — it creates a second `master-log.md`, then a third, and the routines lose track of which is current. Instead, each daily run writes a **new, date-stamped snapshot** of the entire running log: `master-log_YYYY-MM-DD.md`.

2. **Always write into a folder by its hardcoded ID, never by path or name.** If the connector can't resolve a path it silently drops the file in My Drive root. Pass `parentId` explicitly on every create.

### Canonical folder IDs (hardcoded — do not resolve by name)

| Folder | ID |
|---|---|
| `AI-legal-log` (logs) | `1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3` |
| `articles` (writeups) | `13sq6qNqdVz144cN576Zq-7NDcYRh8CXw` |

If a future run shows these IDs no longer exist, re-resolve once with `search_files` and update this table; do not fall back to writing by path.

### Resolving the current log ("newest-modified wins")

Both modes need "the current master log." Resolve it the same way every time:

1. `search_files` with `parentId = '1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3' and title contains 'master-log'`.
2. Pick the file with the most recent `modifiedTime`. That is canonical — regardless of exact filename.
3. Older snapshots are immutable history. They cannot be deleted through the connector; leave them. Sorting by `modifiedTime` means stale copies never break correctness, and a same-day re-run is safe (the latest write simply becomes canonical).

This also migrates the legacy `master-log.md` automatically: on the first run after this change, the newest existing `master-log*` is read as the base, and the dated snapshot continues from it.

---

## Scope — what counts as "AI Legal News"

Full reference: `references/scope.md`

### Core daily watch list (always scan)

1. **IP** — copyright, patent, trademark, trade secrets, right of publicity
2. **Privacy & data protection** — state AI/ADMT laws, BIPA, FTC algorithmic disgorgement
3. **Employment & labor** — EEOC, AEDT audits, hiring AI, workplace surveillance
4. **Consumer protection / AI washing** — FTC Operation AI Comply, SEC enforcement, state AG actions
5. **Securities & financial services** — board oversight, 10-K AI risk, CFPB, FINRA
6. **AI company capital markets events** — S-1 filings, IPO pricing, direct listings, SPAC mergers, major private rounds with governance or disclosure implications
7. **Antitrust & merger review** — DOJ/FTC review of AI M&A and investments, algorithmic price-fixing, monopolization theories on model access
8. **Healthcare** — FDA SaMD/PCCP, prior-auth litigation, clinician AI rules
9. **Product liability & torts** — AVs, chatbot liability, §230 and generative output
10. **Commercial contracting** — vendor terms, indemnities, IP ownership, M&A diligence
11. **Litigation, discovery & evidence** — hallucinated citations, proposed FRE 707, authentication
12. **Legal ethics** — ABA Op. 512, state bar opinions
13. **Government / federal action** — executive orders, OMB memos, BIS export controls, NIST

### Secondary list (include when genuinely breaking)

14. Civil rights & algorithmic discrimination
15. Cybersecurity & AI-enabled fraud
16. Criminal law (deepfakes, NCII, election deepfakes)
17. First Amendment / platform regulation
18. Corporate governance
19. Class actions
20. Tax & R&D

### Flex rule

If the day's news is dominated by a secondary-list topic OR something outside the list entirely (e.g., US–China AI competition, major AI-infrastructure deal with legal implications, foreign-policy AI development, large M&A with AI-asset focus), **include it**. The 5 daily slots reflect the actual news of the day, not a rigid taxonomy. Tag such entries `[BREAKING]` or `[OUTSIDE-LIST]`.

### Geographic scope

US-focused. Include international only when it directly affects US practice (e.g., EU AI Act enforcement against a US-domiciled company, UK Online Safety Act against a US platform).

---

## Source policy

Law firm client alerts, trackers, and legal press are **lead generators only**. Use them to discover what happened; then always read the primary source and write in your own words.

**Primary sources (cite these, in priority order):**

1. Court opinions (CourtListener, Justia, PACER, court websites)
2. Federal Register, agency press releases, final rules, guidance documents
3. Bill text (Congress.gov, state legislature sites)
4. Agency orders, consent decrees, complaints (FTC.gov, SEC.gov EDGAR, DOJ.gov)
5. Executive orders (whitehouse.gov, Federal Register)
6. USPTO notices and PTAB decisions (uspto.gov)
7. SEC EDGAR filings (S-1, 10-K, 8-K) for capital-markets events

**Lead generators (scan for leads; do not quote):** Reuters Legal, Bloomberg Law, Law360, Above the Law, Legaltech News, Wilson Sonsini AI tracker, Gibson Dunn AI alerts, Cooley AI updates, Fenwick, Perkins Coie, Latham AI.

Full source list and research queries: `references/scope.md`

**Copyright discipline (hard rules):**

- Under 15 words verbatim from any single source.
- Maximum one direct quote per source.
- Paraphrase by default.
- Short pin-cite quotes from court opinions are fine where the exact language matters legally.
- Never reproduce article paragraphs or firm-alert copy.

---

## Tag taxonomy

Every log entry gets one **substantive** tag (primary) and optionally one **posture/forum** tag (secondary), separated by ` / ` inside square brackets. The ranker uses these on Friday to group candidates by category.

### Substantive tags (pick one — the primary subject-matter bucket)

`COPYRIGHT` · `PATENT` · `PTAB` · `USPTO` · `TRADEMARK` · `TRADE-SECRETS` · `PUBLICITY` · `PRIVACY` · `EMPLOYMENT` · `AI-WASHING` · `SECURITIES` · `IPO` · `ANTITRUST` · `HEALTHCARE` · `PRODUCT-LIABILITY` · `CONTRACTING` · `EVIDENCE` · `LEGAL-ETHICS` · `EXEC-ORDER` · `CIVIL-RIGHTS` · `CYBER` · `CRIMINAL` · `FIRST-AMENDMENT` · `GOVERNANCE` · `CLASS-ACTION` · `TAX` · `BREAKING` · `OUTSIDE-LIST`

### Posture/forum tags (optional second tag)

`LITIGATION` · `ENFORCEMENT` · `RULEMAKING` · `GUIDANCE` · `LEGISLATION` · `SCOTUS` · `CIRCUIT` · `DISTRICT` · `FTC` · `SEC` · `DOJ` · `FEDERAL` · `STATE`

### Tag examples

- `[COPYRIGHT / LITIGATION]` — a training-data fair-use ruling
- `[ANTITRUST / DOJ]` — DOJ investigation into a frontier-model hyperscaler deal
- `[IPO / SEC]` — an AI company S-1 filing
- `[PATENT / PTAB]` — an IPR decision on an ML claim
- `[EXEC-ORDER / FEDERAL]` — a new White House AI EO
- `[AI-WASHING / FTC]` — an FTC Operation AI Comply action
- `[USPTO / GUIDANCE]` — new USPTO AI inventorship notice
- `[EMPLOYMENT / STATE]` — California FEHA AI regulation update

Use the most specific substantive tag that fits. If two apply roughly equally, pick the one the article would lead with.

---

## Mode 1: LOG mode

### Trigger
Routine prompt contains "daily log," "today's AI legal news," "daily roundup," or similar.

### Workflow

**1. Search.** Cover the core list (1–13). Use web_search with targeted queries covering the last 24–36 hours:

- `AI copyright lawsuit ruling [date]`
- `FTC AI enforcement announcement today`
- `state AI law signed this week`
- `USPTO AI guidance notice`
- `executive order AI [current year]`
- `Federal Circuit AI patent opinion`
- `AI company S-1 SEC filing`
- `DOJ AI antitrust investigation`
- `PTAB IPR machine learning`
- `Section 101 machine learning Federal Circuit`
- `chatbot liability lawsuit`
- `state bar AI ethics opinion`
- Flex: scan top-of-feed headlines at Reuters Legal, Law360, Bloomberg Law for any dominant story.

Spread queries across the 13 core categories; don't burn all your calls on IP.

**2. Select 5 items.** Priority rules:

- Precedential weight (SCOTUS > circuit split > circuit > district)
- Regulatory weight (final rule > proposed rule > guidance > bill > hearing)
- Novel/first-of-kind over incremental
- Client-actionability (compliance deadlines, enforcement risk, contract implications)
- Small bonus for patent/IP developments (Greg's practice)
- Apply the flex rule if a dominant story falls outside the core

**3. Verify from primary source.** For each item, locate and read the actual opinion, rule, order, complaint, bill, filing. If the primary document isn't available (press release only), mark the entry `[source pending]` and cite the most authoritative available URL.

**4. Write entries** using the format in `references/log-entry-template.md`.

**5. Write a new dated snapshot of the master log on Google Drive.** Because the connector cannot append or overwrite (see "Google Drive storage model"), build the full log in memory and save it as one new file:

   a. **Resolve the current log** with the "newest-modified wins" procedure: `search_files` for `parentId = '1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3' and title contains 'master-log'`, take the most recently modified, and `read_file_content` to get its full text.
   b. **Prepend today's block.** Insert today's day block (5 entries, newest at top) directly under the schema header, above the most recent existing day block. Keep every prior day intact — this snapshot is the complete running log, not just today.
   c. **Create the snapshot** with `create_file`: `title = 'master-log_YYYY-MM-DD.md'`, `parentId = '1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3'`, `contentMimeType = 'text/markdown'`, `disableConversionToGoogleType = true`, content = the full assembled log. Each day block is separated from the next by `---`.
   d. If this is the very first run and no `master-log*` file exists, start from the schema header in `references/log-entry-template.md`, then add today's block.

**6. Confirm in chat.** Reply with the date, the 5 tagged headlines, and the snapshot filename. Example: "Logged 2026-04-22: [COPYRIGHT/LITIGATION], [ANTITRUST/DOJ], [IPO/SEC], [USPTO/GUIDANCE], [EXEC-ORDER/FEDERAL]. Wrote AI-legal-log/master-log_2026-04-22.md (now canonical)."

### Daily log entry format

```
## 2026-04-22 (Wed)

**[COPYRIGHT / LITIGATION]** One-sentence summary of what happened — who did what, ruling/action, effect.
- **Read more:** 2–3 sentences of factual context in your own words. Parties and procedural posture. Core holding or mechanism. Why it matters to in-house counsel.
- **Source:** https://primary-source-url

**[ANTITRUST / DOJ]** One-sentence summary…
- **Read more:** Context…
- **Source:** https://…

(three more entries, same format)

---
```

Template details and worked examples: `references/log-entry-template.md`

### Edge cases

- **Slow news day:** If fewer than 5 genuine developments in the window, log what you have (2–4) and add a final line `> Slow news day; N entries rather than 5.` Do not pad with weak stories.
- **Follow-on stories:** If a story from earlier in the week has a new development today (e.g., TRO ruling following Monday's complaint), log it as a separate entry. The weekly ranker will collapse if appropriate.
- **Source pending:** Mark the entry and re-verify on the next daily run.

---

## Mode 2: ARTICLE mode

### Trigger
Routine prompt contains "weekly writeup," "hot topics," "top 5 for the week," or similar.

### Workflow

**1. Read the week's log.** Resolve the current log with the "newest-modified wins" procedure (`search_files` in the `AI-legal-log` folder for `title contains 'master-log'`, take the most recently modified, `read_file_content`). Pull entries from Monday of the current ISO week through the current day (Friday). Typically 25 entries (5 × 5 days), may be fewer.

**2. Rank by hotness.** Scoring rubric in `references/article-template.md`:

1. **Precedential/regulatory weight** — SCOTUS > circuit split > circuit > district > final agency rule > proposed rule > guidance > bill > hearing
2. **Breadth of practice impact** — how many in-house counsel are directly affected
3. **Novelty** — first-of-kind vs. incremental
4. **Client-actionability** — near-term compliance deadlines, enforcement exposure, contract-drafting implications
5. **Patent/IP bonus** — +1 weight
6. **Tie-breaker: resonance** — how much the bar is actually discussing it this week

**3. Propose top 5, grouped by substantive category.** Present in chat like this:

```
TOP 5 CANDIDATES — Week of 2026-04-20 through 2026-04-24

Category: COPYRIGHT / LITIGATION
  #1  [Headline]
      Logged: Mon 2026-04-20
      Why it ranks: [one-line rationale]
      Proposed angle: [what the 600–700 word piece would actually argue]

Category: ANTITRUST / DOJ
  #2  [Headline]
      Logged: Tue 2026-04-21
      Why it ranks: …
      Proposed angle: …

Category: IPO / SEC
  #3  [Headline]
      Logged: Wed 2026-04-22
      Why it ranks: …
      Proposed angle: …

Category: EXEC-ORDER / FEDERAL
  #4  [Headline]
      …

Category: USPTO / GUIDANCE
  #5  [Headline]
      …

Pick up to 2 to write up. You can pick by rank number, category, or mix
(e.g., #1 plus #3 for variety across practice areas).
```

If two or more of the top 5 fall in the same substantive category, note it and offer an alternative from a different category as a swap, so Greg always has diversity available.

**4. Stop and wait for Greg's choice.** Do not proceed to drafting until he responds with his selection.

**5. Re-verify primary sources** for the chosen 1 or 2. Re-read the opinion, rule, order, or filing. Pull related primary documents if helpful (underlying complaint, prior opinions distinguished, agency comment record). Don't rely on the one-line summary in the log — the log was a lead, now you're writing the article.

**6. Draft each article** as a separate .docx file. **Start from the bundled template `references/house-style.docx`** — it already defines every paragraph style (Title, Subtitle, Byline, Heading 1, Heading 2, List Bullet, Endnote Text) in Times New Roman at the locked sizes, and already wires up Word endnotes. Copy it, replace the bracketed placeholders with the article content, and keep the styles as-is. Target 600–700 words with no more than 3 endnotes and a closing Takeaways bullet list. Use the docx skill (`/mnt/skills/public/docx/SKILL.md`) for editing. Apply the **locked house style** below verbatim if you ever build without the template — same fonts, sizes, spacing, and structure every week. This is the single most important rule for week-to-week consistency: do not improvise typography or section order. **Byline is fixed: `AI Legal News · [Date]` — no author name, no placeholder.** `[Date]` = Friday of the current ISO week, formatted like `April 24, 2026`.

**7. Save** each .docx into the `articles` subfolder **by ID** with `create_file`: `parentId = '13sq6qNqdVz144cN576Zq-7NDcYRh8CXw'`, `title = 'AILegalNews_YYYY-MM-DD_short-slug.docx'`. Date = Friday of the week. Slug = lowercase-hyphen topic, e.g., `AILegalNews_2026-04-24_ninth-circuit-training-data.docx`. Never pass a path as the parent and never write to root; always use the folder ID above so the file can't land in My Drive root.

**8. Report in chat** with article titles, word counts, and the `articles/` filenames.

---

## Article document format (LOCKED house style)

Every weekly `.docx` MUST be built to this exact specification so output is identical week to week. Apply these values explicitly through the docx skill; never fall back to defaults or improvise. Full reference with worked example: `references/article-format.md`.

### Page
- US Letter (8.5" × 11"), portrait. Margins **1" on all four sides**.

### Fonts and sizes (font: **Times New Roman** throughout; sizes in points)
| Element | Font | Size | Weight | Notes |
|---|---|---|---|---|
| **Title** (headline) | Times New Roman | 14 | Bold | Left-aligned. Space after 4pt. |
| **Subtitle** (optional, the longer descriptive line) | Times New Roman | 13 | Regular, *italic* | Left-aligned. Space after 8pt. Omit if the title already says it all. |
| **Byline** | Times New Roman | 11 | Regular, *italic* | Exactly `AI Legal News · [Date]`. No author. Space after 12pt. |
| **H1 section heading** (`Background`, `Analysis`, `Takeaways`) | Times New Roman | 12 | Bold | Space before 12pt, after 6pt. |
| **H2 sub-heading** (e.g., "Two statutes, two outcomes") | Times New Roman | 11 | Bold | Space before 8pt, after 4pt. |
| **Body paragraph** | Times New Roman | 12 | Regular | Left-aligned (ragged right), line spacing 1.15, space after 8pt. |
| **Takeaways bullets** | Times New Roman | 12 | Regular | Standard round bullets, space after 4pt per item. |
| **Endnotes** | Times New Roman | 10 | Regular | See below. |

- **No color** on any element. Headings are bold black, not accented.

### Structure (fixed order, every article)
1. **Title** (H-title style above).
2. **Subtitle** (optional).
3. **Byline** — `AI Legal News · [Date]`, date = Friday of the ISO week (e.g., `April 24, 2026`).
4. **Lead paragraph** — no heading; opens the story.
5. **`Background`** (H1) — factual/procedural setup.
6. **`Analysis`** (H1) — the substance, broken into H2 sub-headings as needed.
7. **`Takeaways`** (H1) — a bullet list (typically 3–5 bullets), descriptive only (no advice — see the strict no-advice rule).

### Notes — use ENDNOTES, never footnotes
- Use **Word endnotes** (collected at the very end of the document), **not** footnotes at the bottom of each page. Maximum 3.
- Endnote markers are **superscript** numbers in the body text.
- Endnote text: Times New Roman 10pt. Bluebook style; case names italicized; the citation includes a live **blue hyperlink** (the `Hyperlink` style — color `0563C1`, underlined) to the primary source. Never leave a citation URL as plain black text.
- If the docx skill defaults to footnotes, explicitly convert/author them as endnotes before saving.

### Inline conventions
- **Case names** italicized wherever they appear (body and endnotes).
- **Every primary-source citation is a live hyperlink in blue** — the `Hyperlink` character style (color `0563C1`, underlined). Applies to endnote citations and any inline source mention. No plain-text URLs.
- Em dashes for asides; no double spaces after periods.

### Consistency guarantee
The bundled **`references/house-style.docx`** starter already defines all of these styles and endnote wiring; build every article from it. `references/article-format.md` is the written source of truth for the values. If a future example supersedes this, update the template and the table here in one place — do not let individual runs set their own typography.

---

## Suggested Claude Routine prompts

Paste these into Greg's Claude Routines. These prompts are designed to trigger this skill reliably.

### Daily routine — Mon–Fri, 10:00am CT

> Run today's AI Legal News daily log. Search for the top 5 US AI-related legal developments from the past 24 hours across court decisions, agency rules, executive orders, enforcement actions, AI company IPO/securities filings, antitrust developments, PTAB/USPTO AI matters, and other government initiatives. Apply the flex rule for breaking stories outside the core list. Verify each item from its primary source, tag each with the substantive and posture taxonomy, then write a new dated snapshot `master-log_YYYY-MM-DD.md` of the full running log to the `AI-legal-log` folder on Google Drive (today's 5 entries on top), using the daily log format.

### Weekly routine — Friday, 11:00am CT

> Run the AI Legal News weekly writeup. Read this week's entries (Monday through today) from the most recent `master-log_*` snapshot in the `AI-legal-log` folder on Google Drive. Rank them by hotness and propose the top 5 candidate articles grouped by substantive category, with a one-line ranking rationale and a proposed angle for each. Stop and wait for me to choose up to 2. Then draft the chosen articles as 600–700 word .docx files with no more than 3 endnotes, a closing Takeaways bullet list, Bluebook-italic case names, active hyperlinks to primary sources, and the fixed byline `AI Legal News · [Date]`, and save them to the `articles` subfolder.

---

## Operational notes

- **Google Drive storage model:** Create/copy only — no update, no delete. Logs are written as new dated snapshots (`master-log_YYYY-MM-DD.md`); the newest-modified `master-log*` file is always canonical. See the dedicated section near the top. Always pass `parentId` (the hardcoded folder IDs); never write by path.
- **Folder IDs:** `AI-legal-log` = `1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3`, `articles` = `13sq6qNqdVz144cN576Zq-7NDcYRh8CXw`. If they ever fail to resolve, re-resolve once with `search_files` and update the table; do not fall back to path-based writes.
- **Ordering in master log:** Newest day at the top. Within a day, order entries roughly by hotness (most precedentially significant first) — this makes the Friday ranker's job easier.
- **Near-duplicates across days:** Log follow-on developments separately. The Friday ranker decides whether to treat them as one story.
- **When nothing qualifies:** Never invent. Log fewer entries with a note, rather than filling with low-relevance items.
- **Byline on articles:** Fixed string `AI Legal News · [Date]` with `[Date]` = Friday of the week (e.g., `April 24, 2026`). No author name and no placeholder token — there is nothing to replace by hand.
- **Voice guardrails:** Analytical, descriptive, lawyer-to-lawyer. No marketing. No "in conclusion." No unnecessary hedging.
- **Strict no-advice rule for articles:** Articles never give advice, recommendations, prescriptive guidance, predictions about what readers should do, or the author's opinion. No "should," "must," "consider," "review," "prepare," "watch for" directed at the reader. No action items. No sections that frame the story as something to act on. The article reports and analyzes what happened, what the law says, what the parties argued, and what legal questions remain open — nothing more. If a sentence tells the reader what to do or what to think, rewrite it as a descriptive statement of fact, doctrine, or procedural posture, or cut it. This rule applies to both article modes and, in softer form, to the "Read more" line of daily log entries (see `references/log-entry-template.md`).
