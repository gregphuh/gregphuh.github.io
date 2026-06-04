---
name: ai-legal-news-log
description: Captures the DAILY "AI Legal News" log only — the first of two AI Legal News skills. Use when the user or a Claude Routine asks for the AI legal daily log, daily roundup, or today's US AI-related legal developments (court decisions, agency rules, executive orders, FTC/SEC/DOJ/state-AG enforcement, state AI laws, copyright/training-data litigation, chatbot liability, AI antitrust, USPTO/PTAB matters, AI company S-1s and IPOs, employment AI rules, legal-ethics guidance). Runs unattended and non-interactively: searches the last 24–36 hours, picks the 5 top developments, verifies each from a primary source, tags them, and writes a new dated snapshot of the master log to Google Drive — never asking for input. Do NOT use for the weekly article writeup (use the ai-legal-news-weekly skill) or for non-US / non-legal AI news.
---

# AI Legal News — Daily Log

This is **one of two** AI Legal News skills. It does **only** the daily log capture for Greg's
"AI Legal News" series (US legal developments at the intersection of AI and commercial practice,
for an in-house-counsel audience with a mild patent/IP lean). The weekly article writeup is a
**separate** skill (`ai-legal-news-weekly`) — do not do article drafting here.

> **Unattended — fully non-interactive.** This runs on a schedule with no human watching. NEVER
> ask the user a question, present options (A/B/C/D), or wait for input. Always finish by writing
> the dated snapshot. If you find duplicate or legacy log files, do **not** ask about them — apply
> "newest-modified wins" and proceed. If there are no new items, still write the snapshot (carry
> the prior entries forward and add a one-line `> Run [time] — no new items` note). Reaching the
> end of a run without having written a file is a failure. Do **not** rank stories for articles,
> draft articles, or propose a weekly writeup — that is the other skill's job.

---

## Google Drive storage model (read first — it governs every run)

The Google Drive connector can **create** and **copy** files, but it **cannot update a file in
place and cannot delete files.** There is no "append" or "overwrite." Every save is a new file.
So the log is stored as **dated snapshots**, and each run writes a fresh one:

- **Folder:** `AI-legal-log`, ID **`1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3`** (always write by this ID,
  never by path — path-based writes silently fall back to My Drive root).
- **Snapshot filename:** `master-log_YYYY-MM-DD.md`.
- **Resolve "the current log"** by `search_files` with
  `parentId = '1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3' and title contains 'master-log'`, then take the
  file with the most recent `modifiedTime`. Newest-modified is canonical, regardless of exact
  filename (this also picks up the legacy `master-log.md`).
- Older snapshots are immutable history; leave them. A same-day re-run is safe — the latest write
  simply becomes canonical.

---

## Scope — what counts as "AI Legal News"

Full reference with category examples, key dockets, and research queries: `references/scope.md`.

### Core daily watch list (always scan)

1. **IP** — copyright, patent, trademark, trade secrets, right of publicity
2. **Privacy & data protection** — state AI/ADMT laws, BIPA, FTC algorithmic disgorgement
3. **Employment & labor** — EEOC, AEDT audits, hiring AI, workplace surveillance
4. **Consumer protection / AI washing** — FTC Operation AI Comply, SEC enforcement, state AG actions
5. **Securities & financial services** — board oversight, 10-K AI risk, CFPB, FINRA
6. **AI company capital markets events** — S-1 filings, IPO pricing, direct listings, SPAC mergers
7. **Antitrust & merger review** — DOJ/FTC review of AI M&A, algorithmic price-fixing, model-access theories
8. **Healthcare** — FDA SaMD/PCCP, prior-auth litigation, clinician AI rules
9. **Product liability & torts** — AVs, chatbot liability, §230 and generative output
10. **Commercial contracting** — vendor terms, indemnities, IP ownership, M&A diligence
11. **Litigation, discovery & evidence** — hallucinated citations, proposed FRE 707, authentication
12. **Legal ethics** — ABA Op. 512, state bar opinions
13. **Government / federal action** — executive orders, OMB memos, BIS export controls, NIST

### Secondary list (include when genuinely breaking)

Civil rights & algorithmic discrimination · cybersecurity & AI-enabled fraud · criminal law
(deepfakes, NCII, election deepfakes) · First Amendment / platform regulation · corporate
governance · class actions · tax & R&D.

### Flex rule

If the day's news is dominated by a secondary-list topic OR something outside the lists (e.g.,
US–China AI competition, a major AI-infrastructure deal with legal implications, foreign AI
regulation affecting US companies), **include it**. The 5 daily slots reflect the actual news of
the day, not a rigid taxonomy. Tag such entries `[BREAKING]` or `[OUTSIDE-LIST]`.

### Geographic scope

US-focused. Include international only when it directly affects US practice (e.g., EU AI Act
enforcement against a US-domiciled company; UK Online Safety Act against a US platform).

---

## Source policy

Law firm client alerts, trackers, and legal press are **lead generators only**. Use them to
discover what happened; then always read the primary source and write in your own words.

**Primary sources (cite these, in priority order):** court opinions (CourtListener, Justia, PACER,
court sites) · Federal Register, agency press releases, final rules, guidance · bill text
(Congress.gov, state legislatures) · agency orders, consent decrees, complaints (FTC.gov, SEC.gov
EDGAR, DOJ.gov) · executive orders (whitehouse.gov, Federal Register) · USPTO notices and PTAB
decisions (uspto.gov) · SEC EDGAR filings (S-1, 10-K, 8-K).

**Lead generators (scan; do not quote):** Reuters Legal, Bloomberg Law, Law360, Above the Law,
Legaltech News, and major firm AI trackers (Wilson Sonsini, Gibson Dunn, Cooley, Fenwick, Perkins
Coie, Latham). Full list in `references/scope.md`.

**Copyright discipline (hard rules):** under 15 words verbatim from any single source; max one
direct quote per source; paraphrase by default; short pin-cite quotes from court opinions are fine
where the exact language matters legally; never reproduce article paragraphs or firm-alert copy.

---

## Tag taxonomy

Every entry gets one **substantive** tag (primary) and optionally one **posture/forum** tag
(secondary), separated by ` / ` inside square brackets. The weekly skill uses these to group and
rank candidates, so tag accurately.

**Substantive (pick one):** `COPYRIGHT` · `PATENT` · `PTAB` · `USPTO` · `TRADEMARK` ·
`TRADE-SECRETS` · `PUBLICITY` · `PRIVACY` · `EMPLOYMENT` · `AI-WASHING` · `SECURITIES` · `IPO` ·
`ANTITRUST` · `HEALTHCARE` · `PRODUCT-LIABILITY` · `CONTRACTING` · `EVIDENCE` · `LEGAL-ETHICS` ·
`EXEC-ORDER` · `CIVIL-RIGHTS` · `CYBER` · `CRIMINAL` · `FIRST-AMENDMENT` · `GOVERNANCE` ·
`CLASS-ACTION` · `TAX` · `BREAKING` · `OUTSIDE-LIST`

**Posture/forum (optional second tag):** `LITIGATION` · `ENFORCEMENT` · `RULEMAKING` · `GUIDANCE` ·
`LEGISLATION` · `SCOTUS` · `CIRCUIT` · `DISTRICT` · `FTC` · `SEC` · `DOJ` · `FEDERAL` · `STATE`

Examples: `[COPYRIGHT / LITIGATION]` (a training-data fair-use ruling) · `[ANTITRUST / DOJ]` (a
frontier-model investigation) · `[IPO / SEC]` (an AI company S-1) · `[EXEC-ORDER / FEDERAL]` (a new
White House AI EO). Use the most specific substantive tag; if two apply equally, pick the one the
story would lead with. Tag-selection tips are in `references/log-entry-template.md`.

---

## Workflow

**1. Search** the core list (1–13) with targeted queries for the last 24–36 hours, e.g.:
`AI copyright lawsuit ruling [date]` · `FTC AI enforcement announcement today` · `state AI law
signed this week` · `USPTO AI guidance notice` · `executive order AI [year]` · `Federal Circuit AI
patent opinion` · `AI company S-1 SEC filing` · `DOJ AI antitrust investigation` · `PTAB IPR
machine learning` · `chatbot liability lawsuit` · `state bar AI ethics opinion`. Spread queries
across categories — don't burn them all on IP. (More queries in `references/scope.md`.)

**2. Select 5 items** by: precedential weight (SCOTUS > circuit split > circuit > district);
regulatory weight (final rule > proposed rule > guidance > bill > hearing); novelty; doctrinal
consequence; small bonus for patent/IP (Greg's practice). Apply the flex rule if a dominant story
falls outside the core. If fewer than 5 genuine developments exist, log what you have — do not pad.

**3. Verify from primary source.** For each item, locate and read the actual opinion, rule, order,
complaint, bill, or filing. If only a press release is available, mark the entry `[source pending]`
and cite the most authoritative available URL.

**4. Write entries** in the format below (details + worked examples in
`references/log-entry-template.md`).

**5. Write the dated snapshot** (this is the required output of every run):
   a. Resolve the current log via "newest-modified wins" (see storage model) and `read_file_content`
      to get its full text.
   b. Insert today's day block at the **top**, directly under the file header, pushing older days
      down. Keep every prior day intact — the snapshot is the complete running log.
   c. `create_file` with `title = 'master-log_<today>.md'`,
      `parentId = '1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3'`, `contentMimeType = 'text/markdown'`,
      `disableConversionToGoogleType = true`, content = the full assembled log.
   d. If no `master-log*` file exists yet, start from the header in `references/log-entry-template.md`
      and add today's block.

**6. Report in chat** (brief, no questions): the date, the 5 tagged headlines, and the snapshot
filename. Example: "Logged 2026-04-22: [COPYRIGHT/LITIGATION], [ANTITRUST/DOJ], [IPO/SEC],
[USPTO/GUIDANCE], [EXEC-ORDER/FEDERAL]. Wrote AI-legal-log/master-log_2026-04-22.md (now canonical)."

### Daily log entry format

```
## 2026-04-22 (Wed)

**[COPYRIGHT / LITIGATION]** One-sentence summary — who did what, ruling/action, effect.
- **Read more:** 2–3 sentences of factual context in your own words. Parties and procedural posture. Core holding or mechanism. The legal significance — what the development resolves or reframes.
- **Source:** https://primary-source-url

(four more entries, same format)

---
```

Newest day at the top; each day block separated from the next by `---`. Within a day, order
entries roughly by hotness (most precedentially significant first).

### No-advice rule (lighter form)

The "Read more" bullet is **descriptive, not prescriptive** — it states what happened and its legal
significance, never what a reader should do. Bad: "Counsel should review their training-data
indemnities." Good: "The ruling narrows the transformative-use defense for training-data defendants
in the circuit." Full do's/don'ts in `references/log-entry-template.md`.

### Edge cases

- **Slow news day:** log 2–4 entries and add `> Slow news day; N entries rather than 5.` Never pad.
- **Follow-on stories:** log a new development on an earlier story as its own entry.
- **Source pending:** mark the entry and re-verify on the next run.

---

## Suggested Claude Routine prompt — Daily, Mon–Fri 10:00am CT

> Run today's AI Legal News daily log. This is an unattended scheduled run — do not ask me anything
> and do not wait for input; always finish by saving the snapshot. Search for the top 5 US
> AI-related legal developments from the past 24 hours across court decisions, agency rules,
> executive orders, enforcement actions, AI company IPO/securities filings, antitrust, PTAB/USPTO
> matters, and other government initiatives. Apply the flex rule for breaking stories. Verify each
> from its primary source, tag each with the substantive and posture taxonomy, then write a new
> dated snapshot `master-log_YYYY-MM-DD.md` of the full running log to the `AI-legal-log` folder on
> Google Drive (today's 5 entries on top), using the daily log format.

---

## Operational notes

- **Always end by writing the snapshot by folder ID.** Never write by path; never write to root.
- **Newest-modified wins** for resolving the current log; never ask about duplicate/legacy files.
- **Never invent.** Log fewer entries with a note rather than filling with low-relevance items.
- **Voice:** analytical, descriptive, lawyer-to-lawyer. No marketing adjectives, no advice.
- **Stay in lane:** this skill only logs. It never ranks for articles or drafts articles.
