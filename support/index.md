---
layout: default
title: Support
description: Get help with Milely — FAQ and contact info.
permalink: /support/
---

<main markdown="1">

# Support

Help with Milely. If your question isn't answered below, email **milely@smileycreative.io** and we'll get back within a few business days.

<div class="page-intro">If you're new to the app, start with the <a href="/help/">Help & How-To</a> guide.</div>

---

## Frequently Asked Questions

### How much does Milely cost?

**Try it free for 7 days, then a single subscription: $3.99/month or $29.99/year (annual saves ~37%).** That's it — one plan, all features.

What the subscription unlocks:
- **Unlimited trips** — free tier records up to 25 trips/month
- **Smart Suggestions** — on-device CoreML pattern learning that pre-fills business + purpose based on your past classifications (never leaves your phone)
- **Auto-classify rules** — "Always business at this address" / "Always personal" one-tap rules
- **Favorite trips** — save recurring drives as one-tap shortcuts on the Dashboard
- **Receipts** — VisionKit scanner + camera-roll attach + on the PDF report
- **Branded PDF reports** — your logo, colors, and firm footer
- **Eight color themes** — Warm, Light, Night, Day, Slate, Sky, Forest, Mint (in picker order)
- **Cloud backup** — automatic exports to a Files folder you pick (iCloud Drive, Google Drive, Dropbox, OneDrive)
- **Excel and QuickBooks Online exports** — drop-in mileage import alongside the PDF / Milely CSV options
- **Calendar past-trip recovery** — pulls past calendar events with locations and proposes them as trips
- **Project / client tagging** — sub-classify within a business for billing and reporting
- **Year-end odometer reconciliation** — IRS Form 2106 / Schedule C-aligned beginning-of-year and end-of-year readings
- **Audit Lock and edit history** — last year's records lock automatically January 31; every edit is timestamped for audit defense
- **Sunday review reminder** — gentle nudge when you have unclassified trips waiting
- **Priority email support**

Cancel any time in Apple's subscription management.

**Don't want a subscription?** A separate **Milely Lifetime** purchase ($69.99 one-time) is available inside the app at **Settings → Subscribe → Other options**. Unlocks everything forever — no recurring charge. We don't promote it, because subscriptions fund ongoing development, but it's there for the minority who refuse subscriptions on principle.

### Does Milely work without internet?

Yes — recording, classifying, viewing, and exporting all work fully offline. The only thing that requires internet is uploading backups to cloud storage.

### Will Milely drain my battery?

Manual mode only consumes battery while a trip is recording. Automatic mode uses iOS's significant-location-changes API when idle (negligible drain) and ramps up GPS only when motion suggests driving. Typical drain: ~3% per hour while recording.

### What happens to my data if I delete the app?

The app's data is wiped when you uninstall. If you set up iCloud Drive or Google Drive backup, your backup files remain in your cloud and you can restore from them on a new install.

### How do I restore from a backup?

Backups are **JSON snapshot files** written to whichever cloud folder you picked under **Settings → Backup** (iCloud Drive, Google Drive, Dropbox, OneDrive — anything that shows up in the iOS Files app). The same JSON format is also produced by **Settings → Manual Export** when you want a one-off backup.

To restore on a new device:
1. Reinstall Milely on the new device.
2. Open the backup `milely-*.json` file from the Files app → choose **Open in Milely** when prompted.
3. Trips, businesses, vehicles, and templates import in place.

(CSV and Excel exports are separate from backups — those are *reports* for accountants, not import-restore files.)

A true multi-device sync (no manual export/import) is planned for v1.3 via Apple's CloudKit — see the next answer.

### Can I use Milely on multiple devices?

The app stores data locally on each device. Today, the cleanest path is the manual backup-and-restore above. The next major release (v1.3) is planned around Apple's CloudKit sync — your data syncs through your private iCloud, end-to-end encrypted with Advanced Data Protection, never through a Milely server. Until that ships, we recommend treating one device as the primary recorder.

### Does Milely support Android?

Not currently — and likely staying that way. Milely is iOS-only by design; building Android would mean either a parallel codebase to maintain or a cross-platform framework that compromises the privacy posture and native feel.

### Can I import data from MileIQ / Everlance / [other app]?

Not directly in v1.0. If you have a CSV export from another app, send it to **milely@smileycreative.io** and we'll see if we can help — and consider building an importer for a future update.

### How do I delete a single trip?

Three ways, pick whichever fits the moment:

- **Swipe left** on a row in the **Logs** tab → tap the red **Delete** button. Quick and quiet.
- **Long-press** a row in **Logs** → confirm-style alert. Use this when you want an "are you sure?" check.
- Open the trip detail screen → tap **Delete Trip** at the bottom → confirm.

### How do I delete ALL my data?

Delete the app from your iPhone — that wipes the local SwiftData store, UserDefaults, and the trained Smart Suggestions model. (Reinstalling gets you a clean first-launch.)

### What if I forgot to start a trip?

Two paths depending on the gap:

- **One or two trips?** **Logs → Log Past Trip Manually**. Enter the date, miles, addresses, business, and purpose by hand.
- **A whole stretch (a week, a month)?** **Settings → Setup → Recover from calendar**. Milely reads your past calendar events with locations (on-device, never transmitted), dedupes against trips you already saved, and lets you bulk-create the rest.

### What is Smart Suggestions, and why is Milely guessing?

After you've classified about ten trips, Milely starts pre-filling business + purpose on the Classify screen based on patterns it has learned from those classifications. The training is a small Apple CoreML model (`LogisticRegressionClassifier` trained on `NLEmbedding` features of your end addresses). It runs entirely on-device — Milely has no server, no analytics pipeline, no shared model. Tap a suggestion chip to accept it whole, or just classify normally and the model keeps learning. Uninstall the app and the model goes with it.

### What is Audit Lock?

On **January 31 each year**, Milely automatically locks the previous year's trips so you can't accidentally edit them mid-audit. A small lock icon shows on locked trips. If you legitimately need to amend a return, open the trip from the Logs tab → tap **Unlock for editing** → make the change. The unlock and any edits that follow are written to the trip's **Edit history** with timestamps, so even when you reopen a closed year there's a clean paper trail showing exactly what changed and when.

### How do I export to QuickBooks Online or Excel?

Reports tab → **Export** button (top of the page) → menu opens with four formats:

- **PDF** — IRS Pub. 463-formatted trip log
- **Excel (.xls)** — opens in Excel, Numbers, Google Sheets, or LibreOffice
- **CSV — Milely (full)** — every column we track (date, time, business, project, purpose, vehicle, miles, deduction)
- **CSV — QuickBooks Online** — drop-in mileage importer; MM/DD/YYYY date format, no deduction column (QBO computes that itself based on its own rate)

Pick the format → iOS share sheet opens → email it, AirDrop it, or save to Files.

### Why does Milely ask my age on first launch?

App Store policy and EU/EEA child-protection law require an age check (13+ globally, 16+ in the EEA). The confirmation is a single tap and is stored locally on your device — never transmitted. You'll only see the welcome screen again if our Terms or Privacy Policy materially change in a future update.

### What's the IRS standard mileage rate?

The IRS publishes it annually. Milely pre-loads recent years (2022–2026) but you should verify the current year's rate at [irs.gov](https://www.irs.gov) before filing. Edit any year's rate in **Settings → IRS Rate**.

### Do I need an LLC or business entity to use Milely?

No. Milely works for sole proprietors, single-member LLCs, multi-member LLCs, S-corps, or anyone who deducts business mileage on personal vehicle use.

### Can I get a refund?

Refunds for App Store purchases are handled by Apple, not Milely. Request a refund at [reportaproblem.apple.com](https://reportaproblem.apple.com).

---

## Contact

For everything not in the FAQ — support, privacy, legal, security disclosures:

[**milely@smileycreative.io**](mailto:milely@smileycreative.io)

We aim to respond within 2 business days. SmileyCreative LLC is a small operation — please be patient if it takes a touch longer during tax season.

---

## Bug reports

Found a bug? Send us an email with:
- iOS version (Settings → General → About → Software Version)
- iPhone model
- Milely version (Settings → About → Version)
- A description of what you did, what you expected, and what happened

If the bug involves a specific trip, screenshots help.

---

## Feature requests

We read every email. We don't promise to build everything (we're keeping the app simple on purpose), but we want to hear from real users about what's missing.

</main>
