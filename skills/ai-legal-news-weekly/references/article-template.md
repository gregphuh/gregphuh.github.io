# Weekly Article Template — AI Law Weekly

This file defines the hotness ranking rubric for picking weekly candidates, the .docx article format (structure, voice, citation style, length), and a worked skeleton.

> **House style is locked.** Font is **Georgia** throughout; heading scale is **14 / 12 / 11**
> (Title 14, section heads 12, subsection heads 11); body is **Georgia 11pt**. The byline is the
> fixed string **`AI Law Weekly · [Date]`** — there is no author name and no placeholder to swap.
> Citations are live **blue** hyperlinks (`0563C1`, underlined). This file is the single source of
> truth for article formatting and generation; the at-a-glance summary in `SKILL.md` defers to it.

---

## Ranking rubric — picking the top 5 from the week's log

Apply these criteria in order. Each contributes a score; total ranks the candidate set.

### 1. Precedential/regulatory weight (0–5)

| Weight | Example |
|---|---|
| 5 | SCOTUS decision or binding circuit opinion resolving a split |
| 4 | Circuit opinion not yet creating a split; major final agency rule |
| 3 | District opinion on motion to dismiss or summary judgment with novel holding; proposed final rule; major enforcement settlement |
| 2 | District ruling on procedural matter with substantive implications; agency guidance document; consent decree |
| 1 | Bill introduced or advanced; enforcement complaint filed; hearing announcement |

### 2. Breadth of practice impact (0–4)

| Weight | Example |
|---|---|
| 4 | Affects every in-house counsel at a company using AI (e.g., training-data fair use ruling; federal AI EO) |
| 3 | Affects a major practice area or industry (e.g., AI in financial services, healthcare AI) |
| 2 | Affects a specific sub-practice or company type (e.g., hiring-AI vendors; AI startups pursuing IPO) |
| 1 | Narrow application (e.g., single-agency guidance in one regulated vertical) |

### 3. Novelty (0–3)

| Weight | Example |
|---|---|
| 3 | First of its kind — no prior precedent, rule, or enforcement action on this theory |
| 2 | First within its circuit/forum, or significant expansion of existing doctrine |
| 1 | Incremental development; confirms prior trend |

### 4. Doctrinal consequence (0–3)

| Weight | Example |
|---|---|
| 3 | Opens or closes a new theory of liability, jurisdiction, or agency authority |
| 2 | Clarifies a disputed doctrinal question; creates or deepens a circuit split |
| 1 | Applies settled doctrine to a new factual pattern |

Note: this criterion is purely descriptive — it measures the legal significance of the development, not what any reader "should" do about it.

### 5. Patent/IP bonus (0–1)

Add 1 point if the story falls within `[COPYRIGHT]`, `[PATENT]`, `[PTAB]`, `[USPTO]`, `[TRADEMARK]`, `[TRADE-SECRETS]`, or `[PUBLICITY]`. Reflects Greg's practice focus.

### 6. Resonance (tie-break only)

If two candidates tie on the numerical score, break the tie based on how much the bar is actively discussing it this week (volume of firm alerts, press coverage, LinkedIn discussion by GCs). Do not otherwise weight by press volume — precedential weight dominates.

### Scoring summary

- Maximum score: 16 (5 + 4 + 3 + 3 + 1)
- A candidate below 6 typically isn't worth ranking — flag it in the proposal as "weak week" if the top 5 are all under 8.

---

## Selecting the two articles (automatic — no user input)

This routine runs **unattended**. Do **not** present a menu, ask which to write, or wait for a pick. Score every candidate with the rubric above, then automatically choose the **2 highest-scoring** stories to write.

**Diversity rule:** if the top 2 fall in the same substantive category, swap the lower of the two for the next-highest-scoring story in a *different* category, so the two articles cover different practice areas.

For the record, the run's chat reply may include a short ranked shortlist — but it then proceeds straight to drafting, never stopping for confirmation:

```
SELECTED (Week of [Mon date]–[Fri date]) — writing these 2:
  #1  [Headline] — COPYRIGHT / LITIGATION — 13/16 (Weight 4 · Breadth 3 · Novelty 3 · Doctrine 2 · IP+1)
  #2  [Headline] — ANTITRUST / DOJ — 12/16
Also ranked: #3 [Headline] (10) · #4 [Headline] (9) · #5 [Headline] (8)
```

**Angle discipline.** Proposed angles must be framed as legal questions or analytical observations, never as advice or calls to action. Good angle: "How the Ninth Circuit distinguishes training-stage copying from distribution under Kadrey." Bad angle: "What in-house counsel should do now in response to Kadrey."

---

## Article format (.docx)

### Overall specs

- **Length:** **600–650 words** in the body — lede + Background + Analysis + Takeaways bullets (title, byline, and endnotes don't count). Aim to land in that range; **650 is a hard ceiling.** Before saving, count the body words; if the total exceeds 650, trim Analysis until it is within 600–650. The section budgets below are set to land in that range.
- **Endnote cap:** no more than 3 endnotes per article. Reserve endnotes for the sources that are directly essential to the article's main points — typically the case or agency action being analyzed, any parallel proceeding central to the analysis, and the controlling statute or regulation. **Do not cite like a law review.** Do not endnote every factual claim. If a point can be stated and attributed inline in the prose (e.g., "the statute defines supply chain risk as an adversary's potential to sabotage a covered system"), state it inline without an endnote.
- **Takeaways:** required closing section of **4–5 self-contained bullets (~20–35 words each)** that give a skimming reader the article's *point* — what the case/development means and why it matters (its holding, the rule it sets, or the key open question). Descriptive significance, never advice or a bare recap. See Structure below.
- **Font:** Body in **Georgia 11pt**. Headings bold Georgia at the locked scale: Title 14pt, section heads (Heading 2) 12pt, subsection heads (Heading 3) 11pt **bold italic**. Single title, no subtitle. **Headings are black (`000000`), never blue** — Word's default Heading styles are blue, so set the color explicitly.
- **Margins:** 1" all sides; US Letter (12240 × 15840 DXA).
- **Endnotes (not footnotes):** Word endnotes, placed at the end of the document. The article uses endnotes rather than footnotes so that prose pages read uninterrupted by citation blocks at the bottom. Full legal citation format (see below). The generator (`references/build_article.py`) produces real Word endnotes automatically from the `endnotes` array — see *Generating the .docx*.
- **Filename:** `AILawWeekly_YYYY-MM-DD_short-slug.docx` (date = Friday of the week)

### Structure

1. **Title** (Heading 1, 14pt bold black) — a **single line** (no subtitle) that names the development and the holding or question at stake, matching the approved exemplar: `FASCSA in the AI Era: The D.C. Circuit's Anthropic Stay Denial and the Merits Questions Reserved for May 19`. Not a call to action, not a question to the reader, not clickbait.
   - Good: "The Ninth Circuit's Training-Data Fair-Use Ruling in Kadrey v. Meta"
   - Bad: "What the Kadrey Ruling Means for Your Training-Data Strategy"
   - Bad: "Five Things In-House Counsel Must Know About the Cerebras S-1"

2. **Byline** (italic, 11pt, one line)
   - Format: **`AI Law Weekly · [Date]`** — no author name. `[Date]` = Friday of the ISO week, formatted `Month D, YYYY` (e.g., `April 24, 2026`).
   - There is no `[AUTHOR]` token and nothing to swap before publishing.

3. **Lede** (70–90 words, no heading)
   - One paragraph.
   - Sentence 1: what happened (the news).
   - Sentence 2: why the development is legally significant — describe the doctrinal or procedural importance, not what it means for any particular reader.
   - Sentence 3 (optional): the analytical thesis — the legal question or doctrinal issue the piece will examine, framed descriptively.

4. **Background** (Heading 2, 12pt bold; body 120–150 words)
   - One paragraph. Procedural posture (for litigation) or regulatory context (for rules/EOs/IPOs). Parties, forum, prior rulings or comment record. Written entirely in your own words from primary sources. No firm-article paraphrasing.

5. **Analysis** (Heading 2, 12pt bold; body 290–340 words, split into 2–3 subsections with Heading 3 subheads)
   - Each subsection has its own descriptive subheading (Heading 3, 11pt **bold italic**, black) — not a question, not a call to action.
   - Walk through what the opinion/rule/order actually says. Identify the novel or disputed element(s). Compare to prior law where helpful. Describe disagreements — dissents, prior contrary authority. Identify the legal questions the development leaves open, framed analytically rather than as things for the reader to monitor.
   - Prefer three tight subsections over four thin ones given the tight word budget.

6. **Takeaways** (Heading 2; bullet list, 4–5 bullets, one self-contained sentence each ~20–35 words)
   - **Give a skimming reader the article's *point*.** Each bullet is a standalone, plain-language statement of what the development means and why it matters — its holding, the rule or principle it establishes, what it changes, or the key open question. Someone who reads only the Takeaways should come away understanding what the case or development stands for.
   - **Self-contained, not fragments.** Do not assume the reader read the body. Avoid bare procedural recaps and context-dependent shorthand; state the bottom-line significance in everyday legal English.
   - Still **descriptive and neutral** — convey significance, never advice: no "should," no instructions, no taking a side.
   - The generator renders the `takeaways` array as a round-bullet list automatically.
   - Good (gives the point): "A federal appeals court will now suspend attorneys — not just fine them — for filing AI-fabricated citations, the toughest judicial response to AI hallucinations so far."
   - Good (the principle): "The decisive factor was dishonesty, not the mistake: the court punished the attorneys' denial of AI use more than the fake citations themselves."
   - Weak (recap with no point — avoid): "The court imposed a six-month suspension and a $2,500 fine."
   - Bad (advice — cut): "Counsel should disclose AI use proactively."

7. **Endnotes** throughout — full legal citations (see below). Cap: 3.

**Do not include a "What it means for counsel" section, an "Action items" section, a "Key takeaways" section that issues recommendations, a "Conclusion" section, a "What to watch" section, an "Implications for practitioners" section, or any other prescriptive section. Takeaways in the required format above is the only post-Analysis section; its bullets must stay descriptive.**

### Endnote budget — what gets an endnote

With a 3-endnote cap, every endnote must earn its place. Endnotes are for the sources directly essential to the article's main points — not for law-review-style support of every proposition. Typical allocation for a court-decision article:

1. The case being analyzed (docket, procedural posture, court, date) — with docket hyperlink
2. Any parallel or related proceeding central to the analysis (if the article's thesis depends on it)
3. The controlling statute, regulation, or precedent the court or agency construes

For an agency-action article: (1) the order or rule; (2) the authorizing statute; (3) any central implementing regulation.

**Do not endnote:** paraphrased arguments from a party's brief (attribute inline: "the government argues that…"), statutory short names already defined in the text, routine procedural details, background context taken from primary sources you're not quoting, or analytical observations that are your own synthesis. If a claim doesn't come from one of the 3 endnoted sources, state it in the text with inline attribution where needed ("the statute defines," "the panel explained," "DOJ contends"), not with an endnote.

If a fourth endnote seems unavoidable, either (a) cut the sentence that requires it, (b) rework the prose to attribute inline, or (c) decide which existing endnote is less essential and replace it.

### Endnote citation format

Use Bluebook-style endnote citations. Two formatting rules apply to every citation:

**Rule 1 — Italicize case names and Bluebook signals.** Every case name is italicized, full form and short form. Standard Bluebook signals and citation words are italicized: *See, See also, See, e.g., Cf., Compare, But see, Contra, Accord, E.g., Id.* So are internal cross-references: *supra, infra, ibid.* Statute names, regulation section numbers, and publication titles are not italicized. In the article JSON, mark an italic run as `{"text": "…", "italic": true}`.

**Rule 2 — Embed source URLs as live blue hyperlinks, not plain text.** Every endnote citing a source with a public URL must render that URL as an active hyperlink in Word blue with an underline. In the article JSON, mark a citation run as `{"text": "…", "url": "https://…"}` — the generator renders it blue and underlined. Never paste a raw URL as plain text.

**Which sources get hyperlinks:**

| Source type | Preferred URL target |
|---|---|
| U.S. Code section | Cornell LII, e.g., `https://www.law.cornell.edu/uscode/text/41/4713` |
| Federal Acquisition Regulation | acquisition.gov, e.g., `https://www.acquisition.gov/far/52.204-30` |
| DFARS | acquisition.gov, e.g., `https://www.acquisition.gov/dfars/subpart-239.73-...` |
| Code of Federal Regulations | eCFR, e.g., `https://www.ecfr.gov/current/title-17/...` |
| Federal Register | federalregister.gov (document-specific URL) |
| Supreme Court opinion | `https://supreme.justia.com/cases/federal/us/<vol>/<page>/` or the Court's opinions page |
| Circuit opinion | CourtListener docket URL; the circuit's opinions page if a precedential opinion |
| District court opinion / docket | CourtListener docket URL |
| Agency press release | the agency's own URL |
| SEC filing | SEC EDGAR document URL |
| Executive order | whitehouse.gov presidential-actions URL or federalregister.gov |
| USPTO notice | uspto.gov URL |

**Which sources skip the hyperlink:** Items without a reliably public URL — e.g., sealed filings, party briefs not posted to PACER/CourtListener, *Id.* citations, social-media posts, and internal agency correspondence.

**URL discipline:** Use the most authoritative and durable URL. Prefer primary sources to secondary. Never link to firm-alert or news articles as the cited source — the citation is to the primary document, with the URL pointing to that document's authoritative host.

Examples in the required format. In the rendered .docx: italic portions are italicized; URL portions are active hyperlinks. In this markdown reference, italics are shown with asterisks.

**Case (first citation, long form):**
> *Kadrey v. Meta Platforms, Inc.*, No. 3:23-cv-03417 (N.D. Cal. Apr. 21, 2026) (order on motion for summary judgment), slip op. at 14, docket available at https://www.courtlistener.com/docket/XXXXXX/kadrey-v-meta-platforms-inc/.

**Case (short form):**
> *Kadrey*, slip op. at 17.

**Case with introductory signal:**
> *See* *Nken v. Holder*, 556 U.S. 418, 434 (2009), https://supreme.justia.com/cases/federal/us/556/418/.

**Id. reference:**
> *Id.* at 420.

**Federal Register / agency rule:**
> Executive Order on Federal AI Procurement, 91 Fed. Reg. 12345 (Apr. 22, 2026), https://www.federalregister.gov/documents/2026/04/22/2026-XXXXX/...

**Agency enforcement:**
> *In re* [Respondent], Advisers Act Release No. 12345 (Apr. 22, 2026), https://www.sec.gov/litigation/admin/2026/ia-XXXXX.pdf.

**USPTO guidance:**
> U.S. Patent & Trademark Office, *Updated Guidance on AI-Assisted Inventions* (Apr. 2026), https://www.uspto.gov/sites/default/files/documents/ai-inventorship-guidance-update-2026.pdf.

**Statute:**
> 35 U.S.C. § 100(f), https://www.law.cornell.edu/uscode/text/35/100.

**Bill:**
> H.R. 1234, 119th Cong. (2026), https://www.congress.gov/bill/119th-congress/house-bill/1234.

**SEC filing:**
> [Company Name], Registration Statement (Form S-1) (Apr. 20, 2026), https://www.sec.gov/Archives/edgar/data/XXXXXXXX/...

**Note:** The *In re* signal in an agency-enforcement citation and the title of a stand-alone publication (like an agency report or USPTO guidance document) are italicized; statute names and regulation section numbers are not. Keep citations tight. Favor links to authoritative primary-source URLs over secondary-source URLs.

### Voice and strict no-advice rule

- **Analytical, descriptive, lawyer-to-lawyer.** Write as if briefing another lawyer on what a court or agency did and what the decision or action means as a legal matter. Do not write as if briefing a client on what to do about it.
- **No advice, no recommendations, no opinions, no predictions directed at the reader.** The article never tells the reader to do anything or feel anything.
- **Neutral and impartial — never take a position for or against any party or the government.** Report what each side argued and what the court or agency did; do not advocate, praise, criticize, or signal which side is right. Attribute contested points ("the government argues," "Anthropic contends," "the panel held") rather than asserting them in the article's own voice.
- **Forbidden words and constructions** (when directed at the reader): *should, must, consider, review, monitor, watch for, prepare, assess, examine, revisit, map, inventory, update, audit, expect (you to), anticipate.* These words are fine when describing what a court or party did ("the court should apply Alice/Mayo next"); they are forbidden when directing the reader.
- **Forbidden sections:** *What it means for in-house counsel, What to do now, Action items, Key takeaways, Next steps, What to watch, Implications for practitioners, Conclusion, Looking ahead, The bottom line.* If content seems to want a section like this, either absorb the legally significant parts into Analysis (framed descriptively), surface them in the required Takeaways bullets (as descriptive statements, never prescriptions), or cut. **Takeaways** is the only permitted post-Analysis section, and its bullets must follow the no-advice rule: describe what the article established, do not tell the reader what to do, feel, or expect.
- **No marketing adjectives** (*groundbreaking, landmark, seismic, watershed, game-changing*).
- **Hedge only where legally necessary.** If the case is on motion to dismiss, say so — don't call it a "final ruling."
- **Avoid first and second person.** No "we," "our," "you," "your." The byline identifies the publication.
- **Declarative subheadings only.** No questions as subheadings ("What does this mean?"). No imperatives ("Watch for…").
- **Passive voice allowed** for procedural sentences ("The motion was denied") but prefer active voice for party conduct.
- **Full case names on first reference, short names thereafter.** Same for statutes and regulations.

### Test for compliance

Before delivering, re-read the draft with two questions. **(1) Does any sentence tell the reader what to do, what to think, or how to feel?** **(2) Does any sentence give legal advice or take a side — for or against a party or the government?** Check **every Takeaways bullet** in particular. If either is true, rewrite the sentence as a neutral, descriptive statement of fact, doctrine, or procedural posture, or cut it. Watch the lede's last sentence, every paragraph's closing sentence, and any sentence containing *should, must, consider, expect, watch, review, prepare, map, or update*. Both checks are hard gates — do not save an article that fails either.

---

## Adversarial review (mandatory before saving)

After drafting, run a **separate, adversarial Reviewer pass** before the article is saved. Adopt a skeptical mindset: assume the draft contains errors and try to find them; do not rubber-stamp. If the runtime supports subagents, run the review as an independent agent; otherwise perform it as a distinct second pass with fresh, critical eyes. The writer then revises to clear every issue, and the loop repeats until the Reviewer signs off with zero open items. Only a draft that passes is saved.

**Reviewer checklist:**

1. **Citations (highest priority).** For every endnote: open/verify the primary-source URL actually resolves, is the authoritative source for the proposition, and genuinely supports the exact sentence it is attached to. Reject and require fixing any citation that is unverifiable, mismatched, to a secondary source where a primary exists, or possibly fabricated. **No hallucinated or unverifiable citation may survive** — a wrong cite is worse than no cite. (Hallucinated citations are themselves a recurring AI-legal story; do not become one.)
2. **Factual accuracy & posture.** Every claim matches the primary sources. Procedural posture is precise (motion to dismiss vs. summary judgment vs. final judgment; stay vs. merits). Dates, courts, dockets, statute sections, and party names are correct.
3. **No advice — but the Takeaways must have a point.** No sentence gives advice, recommendations, action items, or tells the reader what to do, watch, consider, or expect (scan **every Takeaways bullet**). Separately, confirm each Takeaways bullet is self-contained and conveys the development's *significance* — what it means/stands for — not a bare procedural recap or a fragment that only makes sense if you read the body. Reject recap-only or out-of-context bullets.
4. **Neutrality.** No sentence takes a position for or against any party or the government, predicts an outcome, or signals which side is right. Contested points are attributed, not asserted.
5. **Length & structure.** 600–650 body words (650 hard ceiling); exactly Title (single line) → byline → Lead → Background → Analysis (with subheadings) → Takeaways (bullets) → endnotes; no forbidden sections.
6. **Format.** Georgia; Title 14 / section 12 / sub-head 11 / body 11; headings black; citations blue hyperlinks; **endnotes, not footnotes**; byline `AI Law Weekly · [Date]`.
7. **Copyright discipline.** Under 15 verbatim words from any source; at most one direct quote per source; everything else paraphrased.

The Reviewer returns a concise, itemized **critical feedback list** (what is wrong and why). The writer fixes each item and re-submits. Do not save until the list is empty.

---

## Worked article skeleton

The exact format is produced by **`references/build_article.py`** (see *Generating the .docx*). The skeleton below illustrates the structure it emits — single Title line, byline, Lead, Background, Analysis with descriptive subheadings, Takeaways bullets, ≤3 endnotes — targeting 600–650 words:

```
Title: The Ninth Circuit's Training-Data Fair-Use Ruling in Kadrey v. Meta

Byline: AI Law Weekly · April 24, 2026

[Lede — 70–90 words]
The Ninth Circuit on Tuesday reversed the Northern District of California's
summary-judgment grant in Kadrey v. Meta, holding that intermediate copying
during model training is not categorically transformative and requires a
factor-by-factor fair-use analysis.¹ The decision clarifies the framework that
will govern training-data infringement cases in the circuit where most frontier
AI developers are based and sets up a potential split with the Second Circuit's
approach in the pending New York Times litigation.

Background (Heading 2, 120–150 words)
[One paragraph — case history, who sued, prior rulings, posture]

Analysis (Heading 2)

  The panel's transformative-use framework (Heading 3)
  [body paragraph — core holding, how the panel treats §107 factor one]

  Market-substitute analysis under factor four (Heading 3)
  [body paragraph — fourth-factor analysis; divergence from S.D.N.Y. approach]

  Questions the opinion reserves (Heading 3)
  [body paragraph — scope and limits, open doctrinal questions for the next
   round of cases]

Takeaways (Heading 2)
  • The Ninth Circuit held that intermediate training-data copying is not
    categorically transformative and must be evaluated factor-by-factor.
  • The panel's fourth-factor analysis emphasizes market displacement by
    model outputs, departing from the narrower framing adopted in the
    S.D.N.Y.
  • The decision reserves two doctrinal questions: how to treat torrent-based
    data acquisition, and whether contributory liability can reach downstream
    distribution of training corpora.
  • The ruling creates a potential split with the pending New York Times
    litigation on the scope of 17 U.S.C. § 107.

[3 endnotes total:]
¹ *Kadrey v. Meta Platforms, Inc.*, No. 24-XXXXX (9th Cir. Apr. 21, 2026),
   slip op. at 17–24, docket at https://www.courtlistener.com/docket/XXXXXX/
   kadrey-v-meta-platforms-inc/.
² *Kadrey v. Meta Platforms, Inc.*, No. 3:23-cv-03417 (N.D. Cal.)
   (summary-judgment order below).
³ 17 U.S.C. § 107, https://www.law.cornell.edu/uscode/text/17/107.
```

Note the shape: Background and Analysis stay lean so Takeaways crystallizes the key points without repeating them at length. Endnotes sit on the three sources essential to the article — the opinion being analyzed, the order below, and the controlling statute. Everything else (e.g., *Campbell*, *Recentive*, the competing S.D.N.Y. case) is referenced in the prose without an endnote.

---

## Re-verification before drafting

Before writing either of the two chosen articles:

1. **Re-open the primary source** cited in the log entry. Read the whole thing, not just the paragraph that caught your eye for the log.
2. **Pull related primary documents** — for a court opinion, read the underlying complaint and any opinions it distinguishes; for a final rule, skim the proposed rule and comment summary; for an S-1, pull the latest amendment; for an EO, read the text and any implementing guidance released.
3. **Re-check the pin cites** and direct quotes before inserting them into the article.
4. **Quote discipline:** Under 15 words per quote, max one direct quote per source, paraphrase by default. A court opinion where the exact judicial language matters legally is the main place to use a short pin-cite quote — everywhere else, paraphrase.

---

## Generating the .docx (self-contained — NO external skill)

> **Do not use `/mnt/skills/public/docx`, docx-js, python-docx, or any other external skill/library — they are NOT guaranteed to exist in the run environment, and relying on them yields a broken file (no styles.xml, no heading styles, square bullets, fake endnotes). Generate the document only with the bundled, dependency-free script `references/build_article.py` (Python standard library only). It hardcodes the entire house style, so the output is correct every time.**

**Steps:**

1. Compose the article as `article.json` following this schema:

```json
{
  "title": "single-line title",
  "date": "Month D, YYYY",
  "lead": [ run, ... ],
  "background": [ [run, ...], ... ],
  "analysis": [ { "subhead": "string", "paras": [ [run, ...], ... ] }, ... ],
  "takeaways": [ [run, ...], ... ],
  "endnotes": [ [run, ...], ... ]
}
```

A **run** is a plain string, or one of:
- `{"text": "…", "italic": true}` — italic (case names, Bluebook signals like *See*, *Id.*)
- `{"text": "…", "url": "https://…"}` — blue underlined hyperlink (primary-source citations)
- `{"endnote": N}` — superscript marker that points to endnote N

2. Run the generator (it writes the .docx **and** a `.b64` sidecar for upload):

```
python3 references/build_article.py article.json AILawWeekly_YYYY-MM-DD_slug.docx
```

3. Upload to Google Drive with the connector's `create_file`:
   - `parentId = '13sq6qNqdVz144cN576Zq-7NDcYRh8CXw'`  (the `articles` folder)
   - `title = 'AILawWeekly_YYYY-MM-DD_slug.docx'`  (date = Friday of the week)
   - `contentMimeType = 'application/vnd.openxmlformats-officedocument.wordprocessingml.document'`
   - `disableConversionToGoogleType = true`
   - `base64Content =` the full contents of `AILawWeekly_YYYY-MM-DD_slug.docx.b64`

The script guarantees: Georgia; Title 14 bold black; Background/Analysis/Takeaways 12 bold black; Analysis sub-heads 11 bold italic black; round bullets; real Word ENDNOTES (never footnotes); blue (`0563C1`) underlined citation hyperlinks; XML-safe text (escapes `&`, `<`, `>`). Do not hand-build a .docx, do not restyle, do not post-process.

`build_article.py` is the single source of truth for format — if the house style ever changes, edit that script (its `STYLES`, `NUMBERING`, and endnote builders).
