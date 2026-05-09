---
layout: default
title: Support
description: Frequently asked questions about Milely — pricing, the 7-day trial, privacy, multi-device, MileIQ / Everlance / TripLog import, exports, Audit Lock, refunds, and how to contact a real human at SmileyCreative LLC.
permalink: /support/
---

<main markdown="1">

# Support

Help with Milely. If your question isn't answered below, email [**milely@smileycreative.io**](mailto:milely@smileycreative.io) and we'll get back to you within a few business days.

<div class="page-intro">If you're new to the app, start with the <a href="/help/user-guide/">User Guide</a>. The <a href="/help/">Help index</a> has section-level deep links if you know what you're looking for.</div>

---

## Frequently asked questions

### How much does Milely cost?

**Try it free for 7 days, fully unlocked. After the trial, a single subscription: $3.99 per month or $29.99 per year (annual saves about 37%).** One plan, all features.

**The trial timer starts on your first recorded trip — not on app install.** Set Milely up at home, pair your CarPlay, classify a couple of past drives by hand, then start the clock when you're actually driving.

**What stays free forever after the trial ends:** every trip you recorded keeps living on your phone. View, edit, classify, lock, unlock, and re-export PDF / CSV / JSON / Excel / QuickBooks Online any time, no subscription needed. Recording *new* trips is what requires a subscription.

**Unlocked during your 7-day trial AND with a subscription** (the trial really is the full app — every feature, no card required to start):

- **Recording new trips** — without limit; gated only after the trial expires
- **Smart Suggestions** — on-device CoreML pattern learning that pre-fills business + purpose based on your past classifications (never leaves your phone)
- **Strict CarPlay Start** — locks auto-record to drives where one of your paired vehicles is the live audio route
- **Lost-miles backfill** — recovers the first half-mile to two miles when iOS motion classification lags
- **Auto-classify rules** — *"always business at this address"* / *"always personal"* one-tap rules
- **Trip templates (favorites)** — save recurring drives as one-tap shortcuts on the Dashboard Quick Start row
- **Receipts** — VisionKit document scanner, on-device, EXIF stripped at attach, up to 10 per trip at 5 MB each
- **Branded PDF reports** — your logo, accent color, and firm footer
- **Eight color themes** — Day (default), Night, Light, Warm, Clear, Storm, Minty, Mint
- **Cloud-folder backup** — automatic JSON snapshots into a folder you pick (iCloud Drive, Google Drive, Dropbox, OneDrive, Box) via the iOS Files picker; or *This iPhone Only* mode with manual JSON exports
- **Calendar past-trip recovery** — pulls past calendar events with locations and proposes them as trips
- **Project / client tagging** — sub-classify within a business for billing and reporting
- **Year-end odometer reconciliation** — per-vehicle beginning-of-year and end-of-year readings, printed on the PDF cover page
- **Audit Lock and edit history** — last year's records lock automatically January 31; every edit is timestamped
- **Live Activity, Dynamic Island, watch app, home-screen widget**
- **Weekly review reminder** — gentle nudge when you have unclassified trips waiting
- **Direct email support**

Cancel any time in *Settings → Apple ID → Subscriptions*. Apple handles all billing.

**Don't want a subscription?** A separate **Milely Lifetime** purchase ($69.99 one-time) is available inside the app at *Settings → Subscribe → Other options*. Unlocks everything forever — no recurring charge. We don't promote it because subscriptions fund ongoing development, but it's there for the minority who'd rather pay once.

### Does Milely work without internet?

Yes — recording, classifying, viewing, locking, exporting, and reports all work fully offline. The only things that need internet are uploading backups to your cloud folder and Apple's StoreKit subscription verification.

### Will Milely drain my battery?

Manual mode only consumes battery while a trip is recording — about 3% per hour. Automatic mode runs a three-stage state machine: **idle** (only iOS's significant-location-changes API, negligible drain) → **armed** (full GPS turns on the moment iOS's motion classifier reports automotive activity, so Milely can confirm you're really driving) → **recording** (the trip is committed). Sub-threshold or zero-waypoint drives drop silently before they hit the classify prompt.

Automatic mode and CarPlay-trigger detection both keep working even after iOS has shut Milely down to free memory: when you start your next drive, iOS wakes the app via a significant location change. The exception is force-quit — if you swipe up in the app switcher to kill Milely, iOS treats that as the user explicitly disabling background activity and won't relaunch the app until you open it again. That's a system-wide iOS rule no app can override.

### What happens if the app crashes or my phone dies during a trip?

Milely snapshots the in-progress trip — route, distance, time so far — to disk every 30 seconds. If iOS evicts the app to free memory, the app force-quits, or your phone runs out of battery mid-drive, the next time you open Milely within seven days you'll see a **Recover trip in progress?** prompt. Tap **Recover** to resume from the last snapshot, **Save as Partial** to materialize what was captured as a finalized Unclassified trip, or **Discard** to drop it.

### What happens to my data if I delete the app?

The app's data is wiped when you uninstall. The encrypted SwiftData store, the receipts directory, and the trained Smart Suggestions model all go with it. If you set up cloud-folder backup, your JSON snapshots remain in the cloud folder you picked and you can restore from them on a new install. If you have iCloud Backup enabled in iOS, the entire app sandbox rides along with that backup as well — restoring a new device gets you every trip back.

### How do I restore from a backup?

Backups are JSON snapshot files written to whichever cloud folder you picked under *Settings → Backup* (iCloud Drive, Google Drive, Dropbox, OneDrive, Box — anything that shows up in the iOS Files app). The same JSON format is also produced by *Settings → Manual Export* for one-off backups.

To restore on a new device:

1. Reinstall Milely on the new device.
2. Open the backup `milely-<timestamp>.json` file from the Files app — choose **Open in Milely** when prompted.
3. Trips, businesses, vehicles, mileage rates, and paired audio routes import in place. The import is dedupe-aware: existing rows are kept; only new rows are added.

(CSV and Excel exports are separate from backups — those are *reports* for your accountant, not import-restore files.)

### Can I use Milely on multiple devices?

The app stores data locally on each device. Today, the cleanest path is the manual backup-and-restore above. The next major release is planned around Apple's CloudKit sync — your data syncs through your private iCloud, end-to-end encrypted, never through a Milely server. Until that ships, treat one device as the primary recorder and use cloud-folder backup to mirror to another.

### Does Milely support Android?

Not currently — and likely staying that way. Milely is iOS-only by design; building Android would mean either a parallel codebase to maintain or a cross-platform framework that compromises the privacy posture and native feel.

### Can I import data from MileIQ, Everlance, or another app?

Yes. Milely imports CSV exports from **MileIQ**, **Everlance**, and **TripLog**. Export a CSV from your old app, then in Milely go to *Settings → Backup → Import from MileIQ / Everlance / TripLog*, pick the file, and confirm. Milely auto-detects the source format from the file's header row, shows a preview of detected trips, and applies your chosen default business / vehicle / purpose to every imported trip. Imported trips arrive Excluded from your annual report by default — Include and assign a business in bulk via the Logs multi-select.

If you're coming from a different app and have a CSV that isn't one of those three formats, send it to [**milely@smileycreative.io**](mailto:milely@smileycreative.io) and we'll see if we can help.

### What's Strict CarPlay Start?

A toggle inside *Settings → Trip Settings → Automatic → Advanced*. With it on, Milely refuses to begin auto-record unless iOS reports a live audio route that matches one of the vehicles you've paired in *Settings → Vehicles*. Passenger rides in someone else's car, Ubers, the train — none of them record.

It's off by default. Most drivers prefer to capture every drive and exclude the rare passenger ride after the fact via a swipe-left in Logs. But if you'd rather start tight and never see a stray trip in Logs, this is the toggle. Either way, the Vehicle list itself is the arming gate — with at least one paired vehicle, motion-based detection only arms when one of them is the live audio route, so passenger rides in someone else's car stay silent.

### Auto-mode didn't catch one of my drives. Why?

Three usual causes:

- **Force-quit.** If you swipe up in the app switcher to kill Milely, iOS won't relaunch it until you open it again. That's a system rule no app can override.
- **Sub-threshold qualifiers.** Auto-record only promotes to Recording once you sustain at least 2 mph + 50 m + 5 s on a paired route, or 5 mph + 0.2 mi + 30 s on an unpaired one. Driveway shuffles and very short drives drop silently before the classify prompt.
- **Trial expiry.** If your 7-day trial has ended and you don't have a subscription, auto-detect is suppressed at the promotion gate and a silent local notification fires instead. Subscribe (or buy the lifetime option) and auto-detect resumes.

If a drive is missing and none of those apply, send the date and approximate route to [**milely@smileycreative.io**](mailto:milely@smileycreative.io) — we read every email.

### How do I delete a single trip?

Two ways, pick whichever fits the moment:

- **Long-press** a row in the Logs tab → tap **Delete trip** in the menu → confirm. Quickest path.
- Open the trip detail screen → tap **Delete Trip** at the bottom → confirm. Same outcome.

(Swipe-left no longer deletes — it now Excludes the trip from your annual report. Locked business trips can't be deleted until you unlock them from the trip's detail page.)

### How do I exclude a trip from my annual report?

Two paths:

- **At classification.** Pick *Personal* in the business picker — Personal lives there alongside the businesses you've added. Personal trips are saved Excluded.
- **After saving.** Swipe left on a row in Logs to Exclude. Swipe right to Include. Excluded trips stay in your Logs for record-keeping but are kept out of every deduction total — Reports, Dashboard savings ticker, and PDF / CSV / Excel exports.

Include and Exclude are independent of which business a trip is assigned to: a trip stays on whichever business you picked, you're just choosing whether it's part of this year's report or not.

### How do I delete ALL my data?

Delete the app from your iPhone — that wipes the local SwiftData store, the receipts directory, and the trained Smart Suggestions model. Reinstalling gets you a clean first-launch.

### What if I forgot to start a trip?

Two paths depending on the gap:

- **One or two trips?** *Logs → Log Past Trip Manually*. Enter the date, miles, addresses, business, and purpose by hand. Manual past-trip entry is intentionally exempt from the trial timer — fixing yesterday doesn't burn a trial day.
- **A whole stretch?** *Settings → Integrations → Recover from Calendar*. Milely reads recent calendar events with locations (on-device, never transmitted), dedupes against trips you already saved, and lets you bulk-create the rest.

### What's Audit Lock?

On **January 31 each year**, Milely automatically locks the previous year's trips so you can't accidentally edit them mid-audit. A year-end-lock banner appears at the top of the Reports tab on and after Jan 31 so you can see at a glance the year is sealed. If you legitimately need to amend a return, open the trip from the Logs tab → tap **Unlock for editing** → make the change. The unlock and any edits that follow are written to the trip's edit history with timestamps, so even when you reopen a closed year there's a clean paper trail showing exactly what changed and when.

### How does locking work?

Every trip auto-locks the moment you save it — no extra step, no chance to forget. Locked trips can't be edited or deleted accidentally, so you can't fat-finger a record once it's correct. To make a legitimate change, tap the trip → **Unlock for editing** at the bottom of the detail page → make the change → save. Re-saving auto-locks the trip again. Every unlock and every field-level change is recorded in the trip's edit history with timestamps, so the full timeline is always there if your CPA asks how a record evolved.

### What happens when I disconnect from CarPlay mid-drive?

Milely pauses the active recording with low-power GPS kept alive — your battery doesn't drain at the job site, and the trip resumes automatically when you reconnect to the same paired vehicle. If you reconnect to a *different* paired vehicle mid-trip, Milely prompts you to stop the current trip and start a new one for the new vehicle.

### How do the mode and the CarPlay trigger interact?

They're independent. The mode (Manual or Automatic) controls motion-based auto-detect. CarPlay-trigger fires whenever your phone connects to a paired vehicle and respects the same trial / paywall gates. Useful combinations:

- **Automatic, no Strict CarPlay Start.** Default. Both paths active — paired-vehicle CarPlay takes you straight to Recording; unpaired drives still arm via motion. Capture everything; exclude the rare passenger ride after the fact.
- **Automatic with Strict CarPlay Start.** Auto-record only fires when a paired vehicle is the live audio route. Passenger rides, Ubers, the train — none record.
- **Manual.** Nothing auto-starts; you tap Start, drive, tap End. CarPlay-trigger is suppressed in Manual mode.

Both auto-start paths check whether a trip is already recording before starting one — they won't double-start.

### How do I export to QuickBooks Online or Excel?

Reports tab → **Export** menu → pick a format:

- **PDF** — annual mileage log; branded for subscribers (your logo + accent color + firm footer), plain for free
- **Excel (.xls)** — opens in Excel, Numbers, Google Sheets, or LibreOffice; proper date typing
- **CSV — Milely (full)** — every column we track: date, time, business, project / client, purpose, vehicle, miles, deduction. UTF-8 BOM for Windows Excel. Sanitized against formula-injection.
- **CSV — QuickBooks Online** — drop-in mileage importer; MM/DD/YYYY date format; no deduction column (QBO computes that itself based on its own rate)
- **JSON** — same shape as the backup snapshot

Pick the format → iOS share sheet opens → email it, AirDrop it, save to Files.

### Why does Milely ask my age on first launch?

App Store policy and EU/EEA child-protection law require an age check (13+ globally, 16+ in the EEA). The confirmation is a single tap and is stored locally on your device — never transmitted. You'll only see the welcome screen again if our Terms or Privacy Policy materially change in a future update.

### Why is the mileage rate adjustable?

The standard mileage rate is updated annually, sometimes mid-year. *Settings → Mileage Rate* lets you confirm or override what Milely uses for any given year. Defaults are pre-loaded; you can edit a rate before you file.

### Do I need an LLC or business entity to use Milely?

No. Milely works for sole proprietors, single-member LLCs, multi-member LLCs, S-corps, or anyone who deducts business mileage on personal vehicle use. Milely doesn't provide tax advice — consult a qualified tax professional for your specific situation.

### Can I get a refund?

Refunds for App Store purchases are handled by Apple, not Milely. Request a refund at [reportaproblem.apple.com](https://reportaproblem.apple.com).

---

## Contact

For everything not in the FAQ — support, privacy, legal, security disclosures:

[**milely@smileycreative.io**](mailto:milely@smileycreative.io)

We aim to respond within two business days. We're a focused team — please be patient if it takes a touch longer during tax season.

---

## Bug reports

Found a bug? Email [**milely@smileycreative.io**](mailto:milely@smileycreative.io) with:

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
  FAQPage schema for /support/ — wraps the Q&As above as a single
  structured-data block so Google can render rich-result FAQ snippets
  in SERPs. Questions match the page H3s exactly; answers are
  condensed to one paragraph each (Google's FAQ-rich-result UI clips
  long answers). Wording avoids tax-authority claims per the brand
  spec — "audit-ready" / "your tax records" rather than tax-authority language.
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
        "text": "Try Milely free for seven days with every feature unlocked — unlimited recording, every theme, receipts, branded PDFs, cloud-folder backup. The trial timer starts on your first recorded trip — not on app install. After the trial, a single subscription: $3.99 per month or $29.99 per year (annual saves about 37%). All trips you've already recorded stay viewable, editable, and exportable forever — recording new trips is what requires a subscription. A one-time $69.99 Lifetime option is available inside the app at Settings → Subscribe → Other options."
      }
    },
    {
      "@type": "Question",
      "name": "Does Milely work without internet?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes — recording, classifying, viewing, locking, and exporting all work fully offline. The only things that need internet are uploading backups to your cloud folder and Apple's StoreKit subscription verification."
      }
    },
    {
      "@type": "Question",
      "name": "Will Milely drain my battery?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Manual mode only consumes battery while a trip is recording — about 3% per hour. Automatic mode uses iOS's significant-location-changes API when idle (negligible drain) and ramps up GPS only when motion suggests driving. Automatic mode and CarPlay-trigger detection both keep working even after iOS has shut Milely down to free memory: the next significant location change wakes the app and Milely re-checks your CarPlay or Bluetooth connection. The exception is force-quit — if you swipe up in the app switcher to kill Milely, iOS won't relaunch it."
      }
    },
    {
      "@type": "Question",
      "name": "What happens if the app crashes or my phone dies during a trip?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Milely snapshots the in-progress trip (route, distance, and time so far) to disk every 30 seconds. If iOS evicts the app to free memory, the app force-quits, or your phone runs out of battery mid-drive, the next time you open Milely within seven days you'll see a 'Recover trip in progress?' prompt. Tap Recover to resume from the last snapshot, Save as Partial to materialize what was captured, or Discard to drop it."
      }
    },
    {
      "@type": "Question",
      "name": "How do I restore from a backup?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Backups are JSON snapshot files written to whichever cloud folder you picked under Settings → Backup (iCloud Drive, Google Drive, Dropbox, OneDrive, Box). To restore on a new device: reinstall Milely, open the backup milely-<timestamp>.json file from the Files app, and choose 'Open in Milely' when prompted. Trips, businesses, vehicles, and mileage rates import in place. The import is dedupe-aware — existing rows are kept; only new rows are added."
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
      "name": "Can I import data from MileIQ, Everlance, or TripLog?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. Milely imports CSV exports from MileIQ, Everlance, and TripLog. Settings → Backup → Import, pick the file, and confirm. Milely auto-detects the source format from the file's header row and shows a preview of detected trips before applying. Imported trips arrive Excluded from your annual report by default — Include and assign a business in bulk via the Logs multi-select."
      }
    },
    {
      "@type": "Question",
      "name": "What's Strict CarPlay Start?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "A toggle inside Settings → Trip Settings → Automatic → Advanced. With it on, Milely refuses to begin auto-record unless iOS reports a live audio route that matches one of the vehicles you've paired in Settings → Vehicles. Passenger rides, Ubers, and other non-driving motion stop recording entirely. Off by default — most drivers prefer to capture every drive and exclude the rare passenger ride after the fact."
      }
    },
    {
      "@type": "Question",
      "name": "Auto-mode didn't catch one of my drives. Why?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Three usual causes. Force-quit — if you swiped up in the app switcher to kill Milely, iOS won't relaunch it until you open it again. Sub-threshold qualifiers — auto-record only promotes once you sustain at least 2 mph + 50 m + 5 s on a paired route, or 5 mph + 0.2 mi + 30 s on an unpaired one. Trial expiry — if your 7-day trial has ended without a subscription, auto-detect is suppressed at the promotion gate."
      }
    },
    {
      "@type": "Question",
      "name": "What is Audit Lock?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "On January 31 each year, Milely automatically locks the previous year's trips so you can't accidentally edit them mid-audit. A year-end-lock banner appears at the top of the Reports tab on and after January 31 so you can see at a glance that the year is sealed. If you need to amend, open the trip from the Logs tab, tap Unlock for editing, and make the change. The unlock and any edits that follow are written to the trip's edit history with timestamps."
      }
    },
    {
      "@type": "Question",
      "name": "How does locking work?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Every trip auto-locks the moment you save it — no extra step, no chance to forget. Locked trips can't be edited or deleted accidentally. To make a legitimate change, tap the trip and tap Unlock for editing at the bottom of the detail page, then save again to re-lock. Every unlock and every field-level change is recorded in the trip's edit history with timestamps."
      }
    },
    {
      "@type": "Question",
      "name": "What happens when I disconnect from CarPlay mid-drive?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Milely pauses the active recording with low-power GPS kept alive — your battery doesn't drain at the job site, and the trip resumes automatically when you reconnect to the same paired vehicle. If you reconnect to a different paired vehicle mid-trip, Milely prompts you to stop the current trip and start a new one for the new vehicle."
      }
    },
    {
      "@type": "Question",
      "name": "How do I export to QuickBooks Online or Excel?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Reports tab → Export menu → pick a format: PDF (audit-ready trip log; branded for subscribers, plain for free), Excel (.xls), CSV — Milely (full), CSV — QuickBooks Online (drop-in mileage importer with MM/DD/YYYY date format), or JSON. Pick the format and the iOS share sheet opens — email it, AirDrop it, or save to Files."
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
