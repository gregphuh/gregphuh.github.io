---
layout: default
title: Support
description: Frequently asked questions about Milely — pricing, privacy, multi-device, MileIQ / Everlance / TripLog import, exports, Audit Lock, refunds, and how to contact a real human at SmileyCreative LLC.
permalink: /support/
---

<main markdown="1">

# Support

Help with Milely. If your question isn't answered below, email **milely@smileycreative.io** and we'll get back within a few business days.

<div class="page-intro">If you're new to the app, start with the <a href="/help/">Help & How-To</a> guide.</div>

---

## Frequently Asked Questions

### How much does Milely cost?

**Try it free for 7 days, fully unlocked. After the trial, a single subscription: $3.99/month or $29.99/year (annual saves ~37%).** One plan, all features.

**The trial timer starts on your first recorded trip — not on app install.** Set Milely up at home, pair your CarPlay, classify your first drive, then start the clock when you're actually driving.

**What stays free forever after the trial ends:** every trip you recorded keeps living on your phone. View, edit, classify, and re-export PDF / CSV / JSON / Excel / QuickBooks Online any time, no subscription needed. Recording *new* trips is what requires a subscription.

**Unlocked during your 7-day trial AND with a subscription** (the trial really is the full app — every feature, no card required to start):
- **Recording new trips** — without limit; gated only after the trial expires
- **Smart Suggestions** — on-device CoreML pattern learning that pre-fills business + purpose based on your past classifications (never leaves your phone)
- **Auto-classify rules** — "Always business at this address" / "Always personal" one-tap rules
- **Favorite trips** — save recurring drives as one-tap shortcuts on the Dashboard
- **Receipts** — VisionKit scanner + camera-roll attach + on the PDF report
- **Branded PDF reports** — your logo, colors, and firm footer
- **Eight color themes** — Warm, Light, Night, Day, Slate, Sky, Forest, Mint (in picker order)
- **Cloud backup** — automatic exports to a Files folder you pick (iCloud Drive, Google Drive, Dropbox, OneDrive)
- **Calendar past-trip recovery** — pulls past calendar events with locations and proposes them as trips
- **Project / client tagging** — sub-classify within a business for billing and reporting
- **Year-end odometer reconciliation** — IRS Form 2106 / Schedule C-aligned beginning-of-year and end-of-year readings
- **Audit Lock and edit history** — last year's records lock automatically January 31; every edit is timestamped for audit defense
- **Sunday review reminder** — gentle nudge when you have trips waiting on Include/Exclude
- **Priority email support**

Cancel any time in Apple's subscription management.

**Don't want a subscription?** A separate **Milely Lifetime** purchase ($69.99 one-time) is available inside the app at **Settings → Subscribe → Other options**. Unlocks everything forever — no recurring charge. We don't promote it, because subscriptions fund ongoing development, but it's there for the minority who refuse subscriptions on principle.

### Does Milely work without internet?

Yes — recording, classifying, viewing, and exporting all work fully offline. The only thing that requires internet is uploading backups to cloud storage.

### Will Milely drain my battery?

Manual mode only consumes battery while a trip is recording. Automatic mode runs a three-stage state machine: **idle** (only iOS's significant-location-changes API, negligible drain) → **armed** (full GPS turns on the moment iOS's motion classifier reports automotive activity, so Milely can confirm you're really driving) → **recording** (the trip is committed). Typical drain: ~3% per hour while recording. Automatic mode and CarPlay-trigger detection both keep working even after iOS has shut Milely down to free memory: when you start your next drive, iOS wakes the app via a significant location change, Milely re-checks your CarPlay or Bluetooth connection, and starts the trip if your paired vehicle is connected. The exception is force-quit: if you swipe up in the app switcher to kill Milely, iOS won't relaunch it — that's a system policy that no app can override.

### What happens if the app crashes or my phone dies during a trip?

Milely snapshots your in-progress trip (route, distance, and time so far) to disk every 30 seconds. If iOS evicts the app to free memory, the app force-quits, or your phone runs out of battery mid-drive, the next time you open Milely within 7 days you'll see a **Recover trip in progress?** prompt. Tap to resume — your route picks up from the last snapshot. Nothing is lost.

### Does Milely keep recording if I closed the app?

Yes for normal backgrounding (you switched to another app or locked your phone) — the trip keeps recording. Yes for iOS-evicted-the-app-to-free-memory: iOS will re-launch Milely on the next significant location change so a new trip can start. The only case where Milely cannot keep recording is force-quit — if you swipe up in the app switcher to kill the app, iOS treats that as the user explicitly disabling background activity and won't relaunch Milely until you open it again.

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

Yes — Milely imports CSV exports from **MileIQ**, **Everlance**, and **TripLog**. Export a CSV from your old app, then in Milely go to **Settings → Backup → Import from MileIQ / Everlance / TripLog**, pick the file, and confirm. Milely auto-detects the source format from the file's header row, shows a preview of detected trips, and applies your chosen default business / vehicle / purpose to every imported trip. Imported trips arrive **Excluded** from your annual report by default — Include and assign a business in bulk via the Logs multi-select.

If you're coming from a different app and have a CSV that isn't one of those three formats, send it to **milely@smileycreative.io** and we'll see if we can help.

### How do I delete a single trip?

Two ways, pick whichever fits the moment:

- **Long-press** a row in the **Logs** tab → tap **Delete trip** in the menu → confirm. This is the quickest delete path.
- Open the trip detail screen → tap **Delete Trip** at the bottom → confirm. Same outcome, just from inside the trip.

(Swipe-left no longer deletes — it now Excludes the trip from your annual report. Locked **business** trips can't be deleted until you unlock them from the trip's detail page; locked Personal trips can be deleted directly without unlocking, since they don't reach IRS reports.)

### How do I exclude a trip from my annual report (so it doesn't count toward my deduction)?

Two paths, depending on whether you know up-front:

- **Marking it Personal at classification.** When you classify a trip, pick **Personal** in the business picker — Personal lives there alongside the businesses you've added. The Classify form for a Personal trip skips business purpose and deduction.
- **Excluding an already-saved trip.** **Swipe left** on a row in the **Logs** tab to Exclude it from your annual report. To put it back, swipe right on the same row to Include it.

Excluded trips (and trips assigned to Personal) stay in your Logs for record-keeping but are kept out of every deduction total — Reports tab, Dashboard savings ticker, and PDF / CSV / Excel exports. Include and Exclude are independent of which business a trip is assigned to: a trip stays on whichever business you picked, you're just choosing whether it's part of this year's report or not.

### How do I delete ALL my data?

Delete the app from your iPhone — that wipes the local SwiftData store, UserDefaults, and the trained Smart Suggestions model. (Reinstalling gets you a clean first-launch.)

### What if I forgot to start a trip?

Two paths depending on the gap:

- **One or two trips?** **Logs → Log Past Trip Manually**. Enter the date, miles, addresses, business, and purpose by hand.
- **A whole stretch (a week, a month)?** **Settings → Integrations → Recover from calendar**. Milely reads your past calendar events with locations (on-device, never transmitted), dedupes against trips you already saved, and lets you bulk-create the rest.

### What is Smart Suggestions, and why is Milely guessing?

After you've classified about ten trips, Milely starts pre-filling business + purpose on the Classify screen based on patterns it has learned from those classifications. The training is a small Apple CoreML model (`LogisticRegressionClassifier` trained on `NLEmbedding` features of your end addresses). It runs entirely on-device — Milely has no server, no analytics pipeline, no shared model. Tap a suggestion chip to accept it whole, or just classify normally and the model keeps learning. Uninstall the app and the model goes with it.

### What is Audit Lock?

On **January 31 each year**, Milely automatically locks the previous year's trips so you can't accidentally edit them mid-audit. A year-end-lock banner appears at the top of the **Reports** tab on and after Jan 31 so you can see at a glance that the year is sealed. If you legitimately need to amend a return, open the trip from the Logs tab → tap **Unlock for editing** → make the change. The unlock and any edits that follow are written to the trip's **Edit history** with timestamps, so even when you reopen a closed year there's a clean paper trail showing exactly what changed and when.

### How does locking work?

**Every trip auto-locks the moment you save it.** The instant you classify a trip and tap Save, it's locked — no extra step, no chance to forget. Locked trips can't be edited or deleted accidentally, so you can't fat-finger a record once it's correct. To make a legitimate change, tap the trip → **Unlock for editing** at the bottom of the detail page → make the change → save. The unlock and every field-level change after it are recorded in the trip's **Edit history** with timestamps, so the full timeline is always there if your CPA asks how a record evolved. Re-saving auto-locks the trip again.

### What happens when I disconnect from CarPlay mid-drive?

Up to you — **Settings → Trip Settings** has a **Pause/Resume Based on CarPlay** toggle inside each mode (Manual and Automatic) that controls disconnect behavior independently:

- **Toggle ON.** When you disconnect from CarPlay or your car's Bluetooth, Milely pauses the trip and drops GPS to a low-power state — your battery doesn't drain at the job site, and the trip resumes automatically when you reconnect. Best for stop-and-go workdays.
- **Toggle OFF.** Milely keeps logging at full GPS resolution after disconnect — useful if you regularly continue a drive in a different vehicle, or the trip's destination is somewhere you'll arrive on foot.

Either way, reconnecting to a *different* paired vehicle mid-trip prompts you to stop the current trip and start a new one for the new vehicle.

### How do the mode and the CarPlay auto-start toggle interact?

They're independent. The mode (Manual or Automatic) controls motion-based auto-detect. The **Auto-Start Trip on CarPlay Connect** toggle — both live inside Settings → Trip Settings — controls whether connecting to a paired vehicle starts a trip on its own. You can mix them however you want:

<table>
  <thead>
    <tr><th>Mode</th><th>CarPlay auto-start</th><th>What you get</th></tr>
  </thead>
  <tbody>
    <tr><td><strong>Automatic</strong></td><td><strong>ON</strong> (default)</td><td>Trip auto-starts the instant you connect to a paired vehicle. For unpaired drives (Ubers, borrowed cars), motion-based detection still catches the trip. CarPlay wins on speed when both apply.</td></tr>
    <tr><td><strong>Automatic</strong></td><td><strong>OFF</strong></td><td>Motion-only. Works without any vehicle pairing.</td></tr>
    <tr><td><strong>Manual</strong></td><td><strong>ON</strong></td><td>CarPlay-trigger still fires for paired vehicles. Motion is ignored. Useful if you want manual control everywhere except your work truck.</td></tr>
    <tr><td><strong>Manual</strong></td><td><strong>OFF</strong></td><td>Pure manual. Nothing auto-starts; you tap Start, drive, tap End.</td></tr>
  </tbody>
</table>

Both auto-start paths check whether a trip is already recording before starting one — they won't double-start. The Vehicle list under **Settings → Vehicles** also acts as the motion-detect arming gate: with at least one paired vehicle, motion-based detection only arms when one of those vehicles is the live audio route, so passenger rides in someone else's car stay silent.

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

We aim to respond within 2 business days. We're a focused team — please be patient if it takes a touch longer during tax season.

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

<!--
  FAQPage schema for /support/ — wraps the 19 Q&As above as a single
  structured-data block so Google can render rich-result FAQ snippets
  in SERPs. Questions match the page H3s exactly; answers are
  condensed to one paragraph each (Google's FAQ-rich-result UI clips
  long answers). Wording avoids IRS-compliance claims per the brand
  spec — "business deductions" / "audit-ready" instead.
-->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "How much does Milely cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Try Milely free for 7 days with every feature unlocked — unlimited trips, all eight themes, receipts, branded PDFs, automatic cloud backup. The trial timer starts on your first recorded trip — not on app install. After the trial, a single subscription: $3.99/month or $29.99/year (annual saves about 37%). All trips you've already recorded stay viewable, editable, and exportable forever — recording new trips is what requires a subscription. A one-time $69.99 Lifetime option is available inside the app at Settings → Subscribe → Other options."
      }
    },
    {
      "@type": "Question",
      "name": "Does Milely work without internet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — recording, classifying, viewing, and exporting all work fully offline. The only thing that requires internet is uploading backups to cloud storage."
      }
    },
    {
      "@type": "Question",
      "name": "Will Milely drain my battery?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manual mode only consumes battery while a trip is recording. Automatic mode uses iOS's significant-location-changes API when idle (negligible drain) and ramps up GPS only when motion suggests driving. Typical drain: about 3% per hour while recording. Automatic mode and CarPlay-trigger detection both keep working even after iOS has shut Milely down to free memory: when you start your next drive, iOS wakes the app via a significant location change and Milely re-checks your CarPlay or Bluetooth connection. The exception is force-quit — if you swipe up in the app switcher to kill Milely, iOS won't relaunch it."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if the app crashes or my phone dies during a trip?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Milely snapshots your in-progress trip (route, distance, and time so far) to disk every 30 seconds. If iOS evicts the app to free memory, the app force-quits, or your phone runs out of battery mid-drive, the next time you open Milely within 7 days you'll see a 'Recover trip in progress?' prompt. Tap to resume — your route picks up from the last snapshot. Nothing is lost."
      }
    },
    {
      "@type": "Question",
      "name": "Does Milely keep recording if I closed the app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes for normal backgrounding (you switched to another app or locked your phone) — the trip keeps recording. Yes for iOS-evicted-the-app-to-free-memory: iOS will re-launch Milely on the next significant location change so a new trip can start. The only case where Milely cannot keep recording is force-quit — if you swipe up in the app switcher to kill the app, iOS treats that as the user explicitly disabling background activity and won't relaunch Milely until you open it again."
      }
    },
    {
      "@type": "Question",
      "name": "What happens to my data if I delete the app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The app's data is wiped when you uninstall. If you set up iCloud Drive or Google Drive backup, your backup files remain in your cloud and you can restore from them on a new install."
      }
    },
    {
      "@type": "Question",
      "name": "How do I restore from a backup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Backups are JSON snapshot files written to whichever cloud folder you picked under Settings → Backup (iCloud Drive, Google Drive, Dropbox, OneDrive). To restore on a new device: reinstall Milely, open the backup milely-*.json file from the Files app, and choose 'Open in Milely' when prompted. Trips, businesses, vehicles, and templates import in place."
      }
    },
    {
      "@type": "Question",
      "name": "Can I use Milely on multiple devices?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The app stores data locally on each device. Today, the cleanest path is the manual backup-and-restore. The next major release (v1.3) is planned around Apple's CloudKit sync — your data syncs through your private iCloud, end-to-end encrypted with Advanced Data Protection, never through a Milely server."
      }
    },
    {
      "@type": "Question",
      "name": "Does Milely support Android?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not currently — and likely staying that way. Milely is iOS-only by design; building Android would mean either a parallel codebase to maintain or a cross-platform framework that compromises the privacy posture and native feel."
      }
    },
    {
      "@type": "Question",
      "name": "Can I import data from MileIQ, Everlance, or another app?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Milely imports CSV exports from MileIQ, Everlance, and TripLog. Export a CSV from your old app, then in Milely go to Settings → Backup → Import, pick the file, and confirm. Milely auto-detects the source format from the file's header row and shows a preview of detected trips before applying. Imported trips arrive Excluded from your annual report by default — Include and assign a business in bulk via the Logs multi-select."
      }
    },
    {
      "@type": "Question",
      "name": "How do I delete a single trip?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two ways: long-press a row in the Logs tab and tap Delete trip in the menu (quickest); or open the trip detail screen and tap Delete Trip at the bottom. Swipe-left no longer deletes — it now Excludes the trip from your annual report. Saved trips auto-lock and can't be deleted until you unlock them from the trip's detail page."
      }
    },
    {
      "@type": "Question",
      "name": "How do I delete all my data?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Delete the app from your iPhone — that wipes the local SwiftData store, UserDefaults, and the trained Smart Suggestions model. Reinstalling gets you a clean first-launch."
      }
    },
    {
      "@type": "Question",
      "name": "What if I forgot to start a trip?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Two paths. For one or two trips: Logs → Log Past Trip Manually, then enter the date, miles, addresses, business, and purpose by hand. For a longer stretch (a week or month): Settings → Integrations → Recover from calendar — Milely reads your past calendar events with locations on-device, dedupes against trips you already saved, and lets you bulk-create the rest."
      }
    },
    {
      "@type": "Question",
      "name": "What is Smart Suggestions, and why is Milely guessing?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "After you've classified about ten trips, Milely starts pre-filling business and purpose on the Classify screen based on patterns it has learned. The training is a small Apple CoreML model that runs entirely on-device — Milely has no server, no analytics pipeline, and no shared model. The training data is yours and stays yours; uninstall the app and the model goes with it."
      }
    },
    {
      "@type": "Question",
      "name": "What is Audit Lock?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On January 31 each year, Milely automatically locks the previous year's trips so you can't accidentally edit them mid-audit. A year-end-lock banner appears at the top of the Reports tab on and after January 31 so you can see at a glance that the year is sealed. If you legitimately need to amend a return, open the trip from the Logs tab, tap Unlock for editing, and make the change. The unlock and any edits that follow are written to the trip's Edit history with timestamps."
      }
    },
    {
      "@type": "Question",
      "name": "How does locking work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every trip auto-locks the moment you save it — no extra step, no chance to forget. Locked trips can't be edited or deleted accidentally. To make a legitimate change, tap the trip and tap Unlock for editing at the bottom of the detail page, then save again to re-lock. Every unlock and every field-level change is recorded in the trip's Edit history with timestamps, so the full timeline is always there if your CPA asks how a record evolved."
      }
    },
    {
      "@type": "Question",
      "name": "What happens when I disconnect from CarPlay mid-drive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Up to you. Settings → Trip Settings has a Pause/Resume Based on CarPlay toggle inside each mode — Manual and Automatic configure it independently. Toggle ON: Milely pauses the trip on disconnect and drops GPS to low-power so your battery doesn't drain at the job site; the trip resumes automatically when you reconnect. Toggle OFF: Milely keeps logging at full GPS resolution after disconnect — useful when a drive continues in a different vehicle or arrives on foot. Either way, reconnecting to a different paired vehicle mid-trip prompts you to stop the current trip and start a new one."
      }
    },
    {
      "@type": "Question",
      "name": "How do the mode and the CarPlay auto-start toggle interact?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "They're independent. The mode (Manual or Automatic) controls motion-based auto-detect; the Auto-Start Trip on CarPlay Connect toggle controls whether connecting to a paired vehicle starts a trip on its own. Both live inside Settings → Trip Settings. Four useful combinations: Automatic + CarPlay auto-start ON (default) — both paths active, CarPlay wins on speed for paired drives, motion-based detection is the fallback for unpaired drives. Automatic + CarPlay auto-start OFF — motion only. Manual + CarPlay auto-start ON — CarPlay only, motion ignored, useful for hands-off recording on a work truck plus manual control everywhere else. Manual + CarPlay auto-start OFF — pure manual. The Vehicle list under Settings → Vehicles also acts as the motion-detect arming gate — with paired vehicles in the list, motion only arms when one of them is the live audio route, so passenger rides in someone else's car stay silent."
      }
    },
    {
      "@type": "Question",
      "name": "How do I export to QuickBooks Online or Excel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reports tab → Export button (top of the page) → menu opens with four formats: PDF (audit-ready trip log), Excel (.xls), CSV — Milely (full), and CSV — QuickBooks Online (drop-in mileage importer with MM/DD/YYYY date format). Pick the format and the iOS share sheet opens — email it, AirDrop it, or save to Files."
      }
    },
    {
      "@type": "Question",
      "name": "Why does Milely ask my age on first launch?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "App Store policy and EU/EEA child-protection law require an age check (13+ globally, 16+ in the EEA). The confirmation is a single tap and is stored locally on your device — never transmitted. You'll only see the welcome screen again if our Terms or Privacy Policy materially change in a future update."
      }
    },
    {
      "@type": "Question",
      "name": "What's the IRS standard mileage rate?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "The IRS publishes the standard mileage rate annually. Milely pre-loads recent years (2022–2026), but you should verify the current year's rate at irs.gov before filing. You can edit any year's rate in Settings → IRS Rate."
      }
    },
    {
      "@type": "Question",
      "name": "Do I need an LLC or business entity to use Milely?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. Milely works for sole proprietors, single-member LLCs, multi-member LLCs, S-corps, or anyone who deducts business mileage on personal vehicle use."
      }
    },
    {
      "@type": "Question",
      "name": "Can I get a refund?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Refunds for App Store purchases are handled by Apple, not Milely. Request a refund at reportaproblem.apple.com."
      }
    }
  ]
}
</script>
