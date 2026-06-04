# Daily Log Entry Template — AI Legal News

This file gives the exact format for daily log entries, plus worked examples showing the right level of detail and tone. Log entries use the same no-advice rule as articles, in a lighter form — the "Read more" bullet describes the development's legal significance, not what any reader should do about it.

---

## Master log file structure

Logs live in the Google Drive **`AI-legal-log`** folder (ID `1YaiLGmORzyQ9XbzaXpISHxRuU8t4HOI3`).

**Storage model — versioned snapshots (important).** The Google Drive connector can create and copy files but **cannot update a file in place or delete one.** So the log is never appended to or overwritten — that only spawns duplicate files. Instead, each daily run writes a **new dated snapshot of the entire running log**:

- Filename: `master-log_YYYY-MM-DD.md` (e.g., `master-log_2026-04-22.md`).
- **Resolve "the current log"** by searching the folder for `title contains 'master-log'` and taking the file with the most recent `modifiedTime` — newest-modified always wins, regardless of exact name. (This also picks up any legacy `master-log.md`.)
- Read that file, insert today's day block at the top (see below), and `create_file` the result as `master-log_<today>.md` with `parentId` = the folder ID above, `contentMimeType = 'text/markdown'`, `disableConversionToGoogleType = true`.
- Older snapshots are immutable history; leave them. A same-day re-run is safe because the latest write becomes canonical.

Each snapshot's internal structure:

```
# AI Legal News — Master Log

Running log of top US AI-related legal developments. Newest at top.

---

## 2026-04-22 (Wed)

[5 entries for today — see entry format below]

---

## 2026-04-21 (Tue)

[5 entries for Tuesday]

---

## 2026-04-20 (Mon)

[5 entries for Monday]

---
```

**Newest day always at top.** When building the new snapshot, insert the new day block directly after the top-of-file header, pushing older days down.

---

## Entry format

Each entry has three parts:

1. **Tagged headline** — one sentence, starts with `**[TAG / POSTURE]**` in bold.
2. **Read more bullet** — 2–3 sentences of factual context in our own words, describing what happened and its legal significance.
3. **Source bullet** — URL to the primary source.

Exact markdown:

```markdown
**[TAG / POSTURE]** One-sentence summary of what happened — subject, action, effect.
- **Read more:** 2–3 sentences of factual context written in your own words. Who the parties are and the procedural posture. The core holding, mechanism, or doctrinal significance. What legal question the development resolves or reframes.
- **Source:** https://primary-source-url
```

Blank line separates entries. Day headers (`## YYYY-MM-DD (Ddd)`) separate days. Trailing `---` separates day blocks.

### No-advice rule (applies to log entries)

The Read more bullet is descriptive, not prescriptive. It states what happened and what it means doctrinally or procedurally. It never tells the reader to do anything or expect anything of themselves.

- Bad: "Counsel should review their training-data indemnities in light of this ruling."
- Good: "The ruling turns on the first and fourth fair-use factors and narrows the scope of transformative-use defenses available to training-data defendants in the circuit."

- Bad: "In-house lawyers advising AI companies should expect heavier SEC review of customer-concentration disclosures."
- Good: "The S-1 discloses a single-customer contract representing a material share of projected revenue and is likely to draw SEC staff comment on customer-concentration disclosure in subsequent amendments."

Describe the legal significance of the development. Do not issue instructions to the reader.

---

## Worked examples

These examples show the right level of detail, tone, and tag usage. They are fictional composites for formatting reference. Each ends with a descriptive observation about the legal or procedural significance of the development — no advice, no "counsel should."

### Example 1 — Copyright litigation

```markdown
**[COPYRIGHT / LITIGATION]** The Northern District of California denied Meta's motion for summary judgment on the direct-infringement claims in *Kadrey v. Meta*, allowing the authors' training-data case to proceed to trial on fair use.
- **Read more:** Judge Chhabria found genuine disputes on the first and fourth fair-use factors as applied to Llama's training corpus, particularly on whether outputs function as market substitutes for the plaintiffs' works. The court rejected Meta's categorical argument that intermediate copying during training is transformative, and the decision keeps the fact-intensive fair-use framework in play for training-data defendants in the Ninth Circuit.
- **Source:** https://www.courtlistener.com/docket/XXXXXX/kadrey-v-meta-platforms-inc/
```

### Example 2 — SEC enforcement (AI washing)

```markdown
**[AI-WASHING / SEC]** The SEC announced a settled enforcement action against [Company] charging the adviser with making materially false claims about its use of AI in portfolio construction, with a civil penalty of $X million.
- **Read more:** The order alleges that the firm marketed an AI-driven strategy despite having no functioning model in production during the relevant period. The settlement bars future Advisers Act antifraud violations and requires retention of an independent compliance consultant, continuing the SEC's pattern of treating AI-capability misrepresentations as disclosure fraud rather than relying on AI-specific rulemaking.
- **Source:** https://www.sec.gov/files/litigation/admin/2026/ia-XXXXX.pdf
```

### Example 3 — USPTO guidance

```markdown
**[USPTO / GUIDANCE]** The USPTO issued an updated guidance memorandum clarifying examiner expectations for applications claiming AI-assisted inventions, expanding on the 2024 inventorship guidance.
- **Read more:** The memo addresses how examiners should treat specification disclosures describing model architecture, training data provenance, and human contribution to claim elements, and tightens the showing required for natural-person inventorship under 35 U.S.C. § 100(f) when an AI system materially contributed to conception. The guidance formalizes a line of examiner practice that had developed ad hoc since *Thaler v. Vidal*.
- **Source:** https://www.uspto.gov/sites/default/files/documents/ai-inventorship-guidance-update-2026.pdf
```

### Example 4 — IPO filing

```markdown
**[IPO / SEC]** [AI Company] filed an S-1 for a proposed $X billion IPO on Nasdaq, with risk factors flagging training-data copyright litigation exposure and BIS export-control compliance costs as material risks.
- **Read more:** The filing discloses ongoing or threatened copyright litigation involving training corpora, describes contingent liability reserves tied to those actions, and identifies dependency on a limited set of chip suppliers. The prospectus is the first full public disclosure by an AI developer at this scale and sets a new reference point for AI risk-factor drafting in the 2026 filing cycle.
- **Source:** https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=XXXXXXXXXX&type=S-1
```

### Example 5 — Executive order

```markdown
**[EXEC-ORDER / FEDERAL]** The White House issued an executive order directing OMB and GSA to accelerate federal procurement of US-developed AI systems and to tighten export licensing for frontier-model weights.
- **Read more:** The order requires OMB implementing guidance within 90 days and directs BIS to publish updated licensing criteria for closed-weight frontier models. It reorients federal AI procurement around domestic-developer preference and narrows the class of models that can be exported under existing license exceptions.
- **Source:** https://www.whitehouse.gov/presidential-actions/2026/04/executive-order-XXXX/
```

### Example 6 — Antitrust

```markdown
**[ANTITRUST / DOJ]** DOJ's Antitrust Division opened a Section 2 civil investigative inquiry into frontier-model licensing practices at [Company], focused on allegedly exclusive compute-partnership terms.
- **Read more:** A CID was reportedly served on [Company] and several cloud partners. The theory centers on whether exclusive or near-exclusive model-access arrangements with hyperscalers foreclose competition in downstream enterprise-AI markets. This is the first publicly reported DOJ Section 2 investigation to treat frontier-model access as the relevant market.
- **Source:** https://www.justice.gov/opa/pr/[release-url]
```

### Example 7 — Flex rule (outside-list)

```markdown
**[BREAKING / OUTSIDE-LIST]** The Commerce Department announced expanded outbound-investment restrictions under Executive Order 14105, adding specified generative-AI dual-use applications to the prohibited-transaction list for US persons investing in Chinese entities.
- **Read more:** The final rule takes effect 60 days from publication in the Federal Register, reaches US-person investments in Chinese entities developing AI systems for specified military, surveillance, or dual-use applications, and imposes notification obligations on a broader set of transactions. The expansion represents the most significant widening of the outbound-investment regime since its 2023 origin.
- **Source:** https://www.federalregister.gov/documents/2026/XX/XX/[document-number]
```

---

## Do's and don'ts

**Do:**

- Lead each one-sentence headline with the substantive actor and action (e.g., "The Ninth Circuit held…," "SEC announced…," "USPTO issued…").
- Keep the one-sentence summary readable without having to consult the "Read more."
- In "Read more," describe the legal significance of the development — what doctrinal or procedural question it resolves, reframes, or leaves open.
- Use pin cites if a specific page or section matters ("at slip op. 14" or "§ IV.B").
- Use the primary URL, not the news article URL — even when the news article led you there.
- **Italicize case names in markdown** using `*Case Name v. Case Name*`. Applies to both the headline and the Read more bullet. Example: `*Kadrey v. Meta*` (correct), `Kadrey v. Meta` (incorrect). Statutory short names are not italicized.

**Don't:**

- Don't give advice. No "counsel should," "in-house teams should," "practitioners should expect," "companies should review." Describe the development; do not instruct the reader.
- Don't copy any substantial phrase from a news article or firm alert. Every word of every bullet must be yours.
- Don't exceed 15 verbatim words from any primary source; one direct quote per source maximum per entry.
- Don't pad. If the legal news is thin, an entry can be shorter.
- Don't use marketing adjectives (*groundbreaking, landmark, seismic*). State what happened.
- Don't predict outcomes. Report what the primary source says; describe what it materially changes as a matter of law.

---

## Tag selection tips

- If a court ruling is about copyright, tag `[COPYRIGHT / LITIGATION]` — not `[IP / LITIGATION]`. Be specific.
- Use `CIRCUIT`, `DISTRICT`, `SCOTUS` in the posture slot for court decisions.
- Use `FTC`, `SEC`, `DOJ`, `USPTO` etc. in the posture slot for agency actions instead of `ENFORCEMENT` or `GUIDANCE` when the agency identity is the important thing.
- Use `RULEMAKING` when the action is a formal rule (proposed or final under APA), `GUIDANCE` for non-binding documents, `LEGISLATION` for bills.
- `BREAKING` tag is for lead stories that dominate the day even if they fit another category. You can stack it: `[COPYRIGHT / LITIGATION / BREAKING]` if needed.
- `OUTSIDE-LIST` is for stories that don't fit any substantive tag (foreign-policy AI, US–China tensions, infrastructure deals with only tangential legal angles).
