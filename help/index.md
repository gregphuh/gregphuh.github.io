---
layout: default
title: Help
description: How to use Milely — record your first trip, configure Strict CarPlay Start, run a year-end report, and back up your trips to a folder you pick. Plus FAQs and direct support.
permalink: /help/
---

<main markdown="1">

# Help

The whole app, in plain English. The full step-by-step lives in the [User Guide](/help/user-guide/) — this page is the table of contents and a place to land if you came in looking for one specific thing.

<div class="page-intro">New to Milely? The fastest path is to skim the <a href="/help/user-guide/#first-time-setup">First-time setup</a> section of the user guide, record one trip, and you'll have everything you need by lunch. Power features are documented inline in the same guide as you grow into them.</div>

---

## The user guide

The [Milely User Guide](/help/user-guide/) is one long page that walks the app in roughly the order you'll touch it. Use the section links below to jump straight to the part you need:

- **[Welcome and what Milely does](/help/user-guide/#welcome-and-what-milely-does)** — the one-paragraph version of the app
- **[First-time setup](/help/user-guide/#first-time-setup)** — age confirmation, terms, mode pick, first vehicle, first business
- **[The Dashboard](/help/user-guide/#the-dashboard)** — month-to-date deduction, Quick Start row, live trip banner, audit-lock banner
- **[Recording — Manual mode](/help/user-guide/#recording--manual-mode)** — Start, Pause, End; what's recorded; battery behavior
- **[Recording — Automatic mode](/help/user-guide/#recording--automatic-mode)** — the four-state machine, arming gate, paired-vehicle skip-to-recording
- **[Strict CarPlay Start](/help/user-guide/#strict-carplay-start)** — the Advanced toggle that locks auto-record to your paired vehicles only
- **[Classifying a trip](/help/user-guide/#classifying-a-trip)** — Review &amp; save, Smart Suggestions, round trip, project tag
- **[Logs — browse, search, edit, lock](/help/user-guide/#logs)** — filters, swipes, bulk-select, locked vs unlocked, edit history
- **[Reports and exports](/help/user-guide/#reports-and-exports)** — yearly hero card, monthly breakdown, the four export formats
- **[Receipts](/help/user-guide/#receipts)** — VisionKit scanner, 10-per-trip cap, EXIF-stripped at attach
- **[Vehicles and odometer](/help/user-guide/#vehicles)** — pairing routes, year-end odometer reconciliation
- **[Backup &amp; restore](/help/user-guide/#backup-and-restore)** — Choose Cloud Folder vs This iPhone Only
- **[Subscription &amp; trial](/help/user-guide/#subscription)** — how the 7-day trial works, what stays free, the lifetime option
- **[Themes](/help/user-guide/#themes)** — Office Day default plus seven subscriber themes
- **[Privacy and permissions](/help/user-guide/#privacy)** — what Milely asks for and why; what it doesn't ask for at all
- **[Troubleshooting](/help/user-guide/#troubleshooting)** — auto-mode didn't catch a drive; CarPlay didn't trigger; recovery prompt
- **[Glossary](/help/user-guide/#glossary)** — terms used in the app and in this guide

---

## Common questions

<details>
<summary><strong>How does the 7-day free trial work?</strong></summary>
<p>The trial timer doesn't start at install — it starts the first time you successfully record a trip. Install Milely today and the clock doesn't move until you actually drive. During the trial, every feature is unlocked: unlimited recording, every theme, receipts, branded PDFs, cloud-folder backup. After seven days, recording new trips needs a subscription, but every trip you already recorded stays viewable, editable, and exportable forever.</p>
</details>

<details>
<summary><strong>What's Strict CarPlay Start?</strong></summary>
<p>An Advanced toggle inside <em>Settings → Trip Settings → Automatic</em>. With it on, Milely refuses to begin auto-record unless iOS reports a live audio route that matches one of the vehicles you've paired in Settings → Vehicles. Passenger rides, Ubers, and other non-driving motion stop recording entirely. Off by default — most drivers prefer to capture every drive and exclude the rare passenger ride after the fact.</p>
</details>

<details>
<summary><strong>Auto-mode didn't catch one of my drives. Why?</strong></summary>
<p>Three usual causes. First, force-quit — if you swipe up in the app switcher to kill Milely, iOS won't relaunch it until you open it again. Second, the qualifiers — auto-record only promotes once you sustain at least 2 mph + 50 m + 5 s on a paired route, or 5 mph + 0.2 mi + 30 s on an unpaired one. Sub-threshold drives drop silently. Third, the lost-miles backfill recovers the first chunk of a missed drive once it does promote — check the trip's start time and route before assuming the drive wasn't captured.</p>
</details>

<details>
<summary><strong>Where does my data live?</strong></summary>
<p>On your iPhone. Trips, GPS routes, addresses, business names, vehicle pairings, and receipts all live in an encrypted SwiftData store inside the app sandbox. Receipts are JPEGs in a per-trip folder, EXIF stripped at attach. The pattern-learning Smart Suggestions model trains on-device and never leaves the phone. The only outbound network calls are Google's OAuth and Drive upload endpoints, both user-initiated. There is no Milely server.</p>
</details>

<details>
<summary><strong>How do I get my trips onto a new phone?</strong></summary>
<p>Two paths. If you turned on <em>Choose Cloud Folder</em> backup, Milely has been writing JSON snapshots into the Milely Backups folder you picked — install Milely on the new phone, open the latest <code>milely-&lt;timestamp&gt;.json</code> from Files, tap Open in Milely, and the trips merge in. If you used <em>This iPhone Only</em> backup, Settings → Manual Export hands you the JSON via the share sheet — AirDrop or email it to yourself, then open it on the new phone. iCloud Backup also includes the entire app sandbox if you have it enabled.</p>
</details>

<details>
<summary><strong>I'm switching from MileIQ / Everlance / TripLog. Can I bring my history?</strong></summary>
<p>Yes. Settings → Backup → Import from MileIQ / Everlance / TripLog. Pick the CSV; Milely auto-detects the source format from the file's header row, previews the trips, and brings every one with you. Imported trips arrive Excluded from the annual report by default — Include and assign a business in bulk via the Logs multi-select. Maximum import is 25 MB or 50,000 rows.</p>
</details>

<details>
<summary><strong>What permissions does Milely ask for?</strong></summary>
<p>Location (When in Use + Always — for recording routes and detecting when you start driving), Motion (to know when you're driving without keeping GPS on), Camera and Photo Library (for receipt scanning), Calendar (opt-in, for past-trip recovery from calendar events), and Notifications (for the weekly review reminder). Milely never asks for contacts, microphone, health data, or App Tracking Transparency.</p>
</details>

<details>
<summary><strong>Will it drain my battery?</strong></summary>
<p>Manual mode only consumes battery while a trip is recording — about 3% per hour. Automatic mode runs three stages: idle (only iOS's significant-location-changes API, negligible drain), armed (full GPS the moment iOS's motion classifier reports automotive activity), recording (committed trip). The armed window is bounded — if motion doesn't sustain, it drops back to idle.</p>
</details>

---

## Still stuck?

The [Support page](/support/) covers a wider list of FAQs — pricing details, refunds, multi-device, deleting all your data, what happens at trial end, how disconnect-from-CarPlay behaves, and more.

For anything not answered there, email [**milely@smileycreative.io**](mailto:milely@smileycreative.io) with what you were trying to do, what you expected, and what happened. Screenshots help. We answer within a couple of business days, and we read every email.

</main>
