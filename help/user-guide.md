---
layout: default
title: User Guide
description: The complete Milely user guide — first-launch setup, recording trips, classifying, reports, exports, vehicles, businesses, and every setting in plain English.
permalink: /help/user-guide/
---

<main markdown="1">

<p style="margin: 0 0 32px;">
  <img src="/assets/og-image.png" alt="Milely" style="width: 100%; max-width: 760px; height: auto; border-radius: 12px;" />
</p>

# Milely user guide

Milely is a private, on-device mileage tracker for iPhone. You drive for work, Milely keeps the records, and at tax time you hand off a clean log to your CPA or your accounting software.

This guide walks through the app in roughly the order you'll touch it: first launch, recording trips, classifying them, looking at reports, then every setting. Anything technical is defined in the [glossary](#glossary) at the end.

Three things to know before you start:

- **Everything stays on your phone.** Milely has no servers and no Milely account. Your trips, addresses, and receipts never leave the device unless you back them up to your own cloud folder, export a PDF, or email a CSV.
- **The trial starts on your first trip, not at install.** A 7-day free trial begins the first time you record a trip — you can install Milely today and not start the clock until you actually drive.
- **After the trial, exports stay free forever.** If you choose not to subscribe, you can still view, edit, and export every trip you've already recorded. The only thing that locks is recording new trips.

---

## Contents

1. [Welcome and what Milely does](#welcome-and-what-milely-does)
2. [First-time setup](#first-time-setup)
3. [The Dashboard](#the-dashboard)
4. [Recording — Manual mode](#recording--manual-mode)
5. [Recording — Automatic mode](#recording--automatic-mode)
6. [Classifying a trip](#classifying-a-trip)
7. [Logs](#logs)
8. [Reports](#reports)
9. [Settings — Trip Settings](#settings--trip-settings)
10. [Settings — Setup](#settings--setup)
11. [Themes and branding](#themes-and-branding)
12. [Backup and restore](#backup-and-restore)
13. [Importing from another tracker](#importing-from-another-tracker)
14. [Privacy and permissions](#privacy-and-permissions)
15. [Subscription and the 7-day trial](#subscription-and-the-7-day-trial)
16. [Year-end and the audit lock](#year-end-and-the-audit-lock)
17. [Watch app and widget](#watch-app-and-widget)
18. [Troubleshooting](#troubleshooting)
19. [Glossary](#glossary)

---

## Welcome and what Milely does

If you drive for work — as a 1099 contractor, freelancer, real-estate agent, gig driver, small-business owner — you can deduct those miles at the standard mileage rate when you file. To take the deduction you need a record showing **when** you drove, **how far**, **where**, and **why**. Milely is built to keep that record honestly and make it easy to hand off.

You can record trips three ways:

- **Manual** — tap Start, drive, tap End. Full control, zero guesswork.
- **Automatic** — Milely notices you're driving and starts recording on its own.
- **Quick Start** — one-tap launchers on the Dashboard, pre-tagged to a business or saved template.

Once a trip is recorded you classify it (which business, what purpose, which vehicle), and at tax time you export — PDF, CSV for QuickBooks, JSON, or Excel.

The on-device promise is the design constraint everything else is built around. There is no Milely server. There is no Milely account. The only outbound network traffic the app makes is when *you* sign in to Google Drive to back up, and when *you* tap "Back Up Now". Everything else — your routes, businesses, receipts, the pattern-learning classifier — lives in encrypted storage on your iPhone.

---

## First-time setup

The first launch hands you two short screens before you reach the Dashboard. Both write only to your device.

### Legal consent

A welcome screen asks you to confirm two things:

- You're old enough to use the app — 13+ in most regions, 16+ in the EU and UK by GDPR. Milely auto-detects which threshold to show based on your phone's region.
- You agree to the Terms of Service and Privacy Policy. Tap the underlined links to read them in your browser, or tap the "Open Terms" / "Open Privacy" helper buttons.

Tick both boxes and tap **Continue**. The four audit fields (terms accepted at, terms version, age confirmed at, region) are stamped locally. You'll only see this screen again if a future update materially changes the terms.

<!-- SCREENSHOT NEEDED: legal consent screen with both checkboxes ticked and the Continue button enabled -->

### Onboarding (nine steps)

After consent, Milely walks you through a guided setup. The exact steps:

1. **Welcome** — one-line overview.
2. **How it works** — Start, drive, End.
3. **Your business** — type the business you'll track miles for ("Greg's Real Estate", "Smith Plumbing"). You can add more later.
4. **Backup** — pick where snapshots go. The two options are "Choose Cloud Folder" (iCloud Drive, Google Drive, Dropbox, OneDrive, or Box via the iOS Files picker) or "This iPhone Only" (manual export when you want it). See [Backup and restore](#backup-and-restore) for the full picture.
5. **Location** — tap **Allow** when iOS asks. Pick **Allow While Using** for now; the upgrade to Always comes later.
6. **Always Allow** — iOS prompts a second time to upgrade location to Always. Allowing this is what lets Automatic mode wake the app when you start driving with the phone in your pocket.
7. **Notifications** — optional. Powers the weekly review reminder, the classify prompt after auto-detected trips, and trip-recovery alerts.
8. **Vehicle** — type a vehicle name (Truck, Wife's Car, Sprinter Van) and tap Add, or Skip. Per-vehicle records help substantiate your annual mileage; if you skip, the Dashboard shows a small reminder until you add one.
9. **Done** — tap **Get Started**.

<!-- SCREENSHOT NEEDED: onboarding business-name step with text field showing a sample business -->

If you deny location during onboarding, manual recording still works — just tap Start when you begin driving and End when you stop. Automatic mode requires Always-Allow location and won't function without it.

---

## The Dashboard

The Dashboard is your home screen. Top to bottom:

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/hero-1-dashboard.png" alt="Milely Dashboard — May estimated deduction donut, Quick Start row with Contracting and Real Estate, and the blue Start Trip button" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">The Dashboard at idle — Day theme, no trial banner.</figcaption>
</figure>

### Trial countdown banner

While your free trial is running, a slim banner sits below the navigation showing how many days are left and a **Subscribe** button. Tap Subscribe to open the subscription sheet without leaving the Dashboard. The banner disappears the moment you subscribe (or buy lifetime), and reappears as a paywall prompt once the trial ends.

### Audit-lock banner (January and after)

On or after February 1 each year, if you have unlocked business trips from the prior year, a yellow banner offers to lock them with one tap. Locking is irreversible per trip and is what gives the log audit defensibility. See [Year-end and the audit lock](#year-end-and-the-audit-lock).

### Live trip banner (only while recording)

When a trip is recording, the top of the Dashboard shows a live banner with a blinking dot, "Manual" or "Automatic" eyebrow, a CarPlay chip (green when paired vehicle is live), and three live tiles: Distance, Time, Deduction. Below them: the business color dot and "Business — Vehicle" label. There's an **End** pill — tap it to stop the trip. Tapping the banner itself opens an editor where you can change business, purpose, or vehicle without ending recording. If a trip is paused (e.g. CarPlay disconnected), the dot turns yellow.

### Monthly Report card

For the current month: total deduction (large), miles, by-business breakdown donut, and — if you've set a tax bracket in Settings — an estimated tax savings. Excluded trips don't enter this figure.

### Quick Start

Up to three rows for your most-driven businesses this month, each one tap to start a pre-tagged trip. Below them: **Repeat Last** (starts a trip pre-filled from your last one) and **Favorites** (opens your saved trip templates). A no-vehicle callout appears if you skipped the vehicle step in onboarding.

### Start Trip button

The big primary button at the bottom — the unconditional way to begin recording.

---

## Recording — Manual mode

Manual is the default, the simplest, and the one that works in every condition. Three steps:

1. Tap **Start Trip** from the Dashboard or pick a Quick Start row.
2. Drive. Milely records GPS in the background. You can switch apps, lock the phone, or close Milely entirely — recording continues.
3. Tap **End Trip**. The End pill is on the Dashboard banner, on the Trip tab map, and in the Logs header — whichever's closest.

The Classify screen appears. Pick a business, type a purpose, save.

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/dashboard-active.png" alt="Milely Dashboard while recording — Automatic mode pill, Truck vehicle, distance and time and deduction tick up, monthly card and Quick Start below" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Dashboard view while a trip records — live distance, time, and deduction at the top.</figcaption>
</figure>

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/hero-3-classify.png" alt="Milely Trip tab during a live recording — distance, time, and deduction tick up over a real-time map" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Recording a live trip — Trip tab, real-time map.</figcaption>
</figure>

### Pause and resume

Tap the live banner to open the editor; one of the rows is **Pause**. The route stops accumulating but the recording stays live. Tap Resume to keep going. Manual recording also pauses automatically when CarPlay or your car's Bluetooth audio disconnects — useful if you stop for gas mid-trip and don't want the parking-lot wander to count.

### What's intentionally absent

Manual mode doesn't have a stationary auto-end. It records until you tap End. The one backstop is the universal overnight cutoff — if a trip is still recording at 4 a.m. local time, Milely ends it for you (this is to catch the genuinely-forgot case, not as a substitute for tapping End).

### CarPlay disconnect behavior

Whether the trip started by CarPlay or you tapped Start, disconnecting from CarPlay or the car's audio pauses the trip. Reconnecting resumes it. This makes the "stopped for coffee, came back, kept driving" pattern produce one clean trip instead of two short ones.

### Recovery from crash or force-quit

Active and paused trips snapshot every 30 seconds. If iOS kills Milely (low memory, force-quit, crash), the next launch shows a "Recover trip in progress?" alert with the miles and start time. Three choices:

- **Recover** — keep going. Polyline and totals are restored, GPS resumes.
- **Save as Partial** — finalize the in-flight trip as it stood. Lands in Logs as Unclassified.
- **Discard** — wipe it.

Snapshots older than 7 days expire silently.

---

## Recording — Automatic mode

Automatic is for "I forget to tap Start" drivers. Switch to it in **Settings → Trip Settings → Automatic**.

<!-- SCREENSHOT NEEDED: settings detection mode picker with Automatic selected -->

How it works in plain terms — Milely runs a four-state machine:

- **Off** — Automatic is disabled. Manual still works.
- **Idle** — Automatic is enabled, no trip running. iOS's *significant location change* and motion-activity APIs are listening. Battery drain is negligible.
- **Armed** — iOS reports "you're moving like a vehicle." Full GPS turns on so distance can accumulate, but no trip is committed yet. The bar is intentionally low (about 5 seconds at walking-plus speed and ~50 meters) — false positives are cheaper than missed drives because you can always swipe-left to Exclude in Logs.
- **Recording** — thresholds met. The trip is committed and saved.

Paired-vehicle drivers skip Armed entirely. If your phone is connected to a paired vehicle's CarPlay or car-Bluetooth audio route at the moment motion confirms automotive activity, Milely treats that as ground truth and goes straight to Recording.

### Backfill — the lost-miles recovery

When a trip promotes from Armed to Recording, Milely walks back through a five-minute rolling location buffer and rewrites the trip's start time and the leading polyline to reflect when you actually started driving — not when the motion classifier finally confirmed it. This recovers the 1–3 minutes of latency that other trackers lose.

### Stationary auto-end

An Automatic trip ends after a configurable stationary timeout (default 60 minutes, or per-vehicle if you set one) — but only if CarPlay isn't connected. Reconnecting to the same paired vehicle cancels the timer. Connecting to a *different* paired vehicle pops a Stop / Continue alert so you don't accidentally tag a trip to the wrong car.

### Strict CarPlay Start (advanced)

In **Settings → Trip Settings → Automatic → Advanced**, the **Strict CarPlay Start** toggle (default off) locks Automatic recording to your paired vehicles only. When ON, Automatic mode only commits a trip if iOS reports a live audio route that matches one of your paired vehicles. Drives in someone else's car, on transit, or as a passenger are silently ignored.

Use this if Automatic mode is occasionally picking up rides that aren't yours. Use the regular setting if you sometimes drive a vehicle that isn't paired (rentals, work trucks).

### What Automatic needs

- **Always-Allow location.** "While Using" is not enough — iOS only wakes the app for SLC events on Always.
- **Motion & Fitness permission.** Used to distinguish driving from walking, biking, or sitting still.

The Settings → Trip Settings page has a Background Recording status card that tells you whether all three signals (location, motion, background app refresh) are configured correctly.

### iOS limitation worth knowing

If you force-quit Milely from the app switcher, iOS suspends the *significant location change* listener too. Automatic mode can't wake the app until the next time you launch it manually. This is an iOS-wide rule for every app — there's no workaround. Don't force-quit Milely if you want Automatic to keep working in the background.

---

## Classifying a trip

After recording, the Classify sheet asks four questions:

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/classify-trip.png" alt="Milely classify-trip view — Trip-tab live map showing distance, time, deduction at the top during recording" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Trip tab live view — same business / purpose / vehicle fields surface on the Classify sheet at End Trip.</figcaption>
</figure>

1. **Business.** Pick from your existing businesses, or tap "+ New Business". The picker shows the business color dot, name, and recent miles for context.
2. **Purpose.** Type a short note ("Client meeting downtown", "Site visit — 412 Main", "Home Depot run"). Smart suggestions surface phrases you've used recently for similar trips.
3. **Vehicle.** Defaults to your most-used vehicle. Tap to change.
4. **Project / tag.** Optional. Sub-categorizes a trip beneath its business — useful if you bill by project.

Tap Save and the trip lands in Logs as **Classified**.

### Smart suggestions

Milely trains a small on-device classifier on every trip you classify. After a dozen or so trips, the Classify sheet starts pre-filling its best guess at business and purpose based on the start/end addresses and time-of-day patterns. The classifier never leaves your phone — there's no cloud round-trip.

### Auto-Classify rules

Settings → Auto-Classify Rules lets you tell Milely *deterministically*: "any trip starting at 412 Main Street is Acme Consulting, purpose 'Site visit'." Rules run before the smart suggester, so they take precedence. Useful for the addresses you visit weekly. Build them at Settings → Setup → Auto-Classify Rules, or by tapping the "Always classify trips here as…" prompt that surfaces when you classify the same address three times in a row.

<!-- SCREENSHOT NEEDED: auto-classify rules list -->

### Excluding a trip

Not every drive is deductible. To mark a trip as non-deductible — a personal errand, a kid pickup, a ride in someone else's car — swipe left in Logs and tap **Exclude**, or open the trip and toggle Exclude. Excluded trips disappear from Reports and from your monthly deduction figure but remain in Logs (so you have a complete audit trail). To put a trip back, swipe right and tap **Include**.

---

## Logs

Logs is your full trip list with filtering, search, and bulk actions.

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/car-is-business.png" alt="Milely Logs tab — searchable list of business and personal trips with addresses, businesses, miles, and Included tags" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Logs — search, filter pills, swipe actions.</figcaption>
</figure>

The header has:

- **Title and Select pill.** Select toggles bulk-edit mode.
- **Search.** Matches trip purpose, address, business, and project tag.
- **Three filters.** Year, Month, Business.

Below the header, trips group into relative buckets: Today, Yesterday, This Week, This Month, then by month name. Each row shows the date, business color dot, miles, deduction, and a small map thumbnail.

### Swipe actions

- **Swipe right** → Include (un-excludes the trip).
- **Swipe left** → Exclude.
- **Tap** → Trip detail.
- **Long press** (in Select mode) → toggle checkmark.

In bulk-select mode, the floating bottom bar shows "{N} selected" and a **Reassign** button for moving many trips to a different business at once. Locked trips are silently skipped.

### Adding a past trip manually

Tap the **+** floating button (bottom right) or the "Log Past Trip Manually" row at the top of the list. Fields: date, time, start address, end address, miles (auto-calculated if you tap Map It), business, purpose, vehicle. This is the path for trips you forgot to record live. Manual past-trip entries do not consume free-trial days.

### Trip detail

Tapping a row opens the trip detail screen. From here you can:

<!-- SCREENSHOT NEEDED: trip detail screen with map and receipts row -->

- See the route on a full map.
- Edit any field (start, end, business, purpose, vehicle, distance).
- Add receipts — see [Receipts](#receipts) below.
- Mark the trip as Locked (irreversible — no further edits or deletions).
- View the audit log — every edit, every receipt add, with timestamps.
- Delete the trip.

### Receipts

Inside trip detail, tap **Add Receipt**. The VisionKit document scanner opens; aim at a paper receipt and Milely auto-detects edges and corrects perspective. Multiple pages are supported. On Save, Milely encodes the pages as JPEG (quality 0.8) and strips all metadata: GPS coordinates, capture timestamps, device model.

You can also add from your photo library — same EXIF strip applies.

Limits: 10 receipts per trip, 5 MB each. Receipts live in Milely's encrypted storage, not your camera roll. They ride along on iCloud device backups and Milely cloud-folder backups. Deleting a trip deletes its receipts in the same operation.

---

## Reports

The Reports tab gives you the year at a glance plus the export menu.

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/hero-4-reports.png" alt="Milely Reports tab — yearly $4,472.89 deduction with stacked-bar by-business breakdown, year-at-a-glance stats, and monthly summary card" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Reports — year hero, stat tiles, monthly breakdown.</figcaption>
</figure>

Top to bottom:

- **Year picker.** Chips for the current and prior years.
- **Savings hero.** Total deduction for the year, plus tax-bracket-adjusted estimate if you've set one.
- **Year at a Glance.** Total trips, average miles per trip, longest trip, busiest day. If you have both manual and auto-detected trips, you'll also see a manual / automatic split.
- **Monthly Breakdown.** One card per month with a donut chart and miles-by-business breakdown. Percentages always sum to 100.
- **Top Destinations.** Top 5 places you've driven to (by trip count, with normalized address dedupe).
- **By Business.** Per-business totals and deductions.
- **By Project.** Per-project totals if you've used project tags.
- **Export menu.** See [exports](#exports) below.

Excluded trips never enter Reports — this is your deduction-only view.

### Exports

Tap the Export button at the bottom of Reports. Choose a format:

- **PDF report.** Annual mileage log with a cover page (totals, by-business breakdown) and one row per trip with a route thumbnail and up to three receipt thumbnails inline. Subscribers get a branded PDF with your business logo, accent color, and footer text. Free / post-trial users get a plain PDF.
- **CSV — Milely full.** Date, Time, Business, Project, Purpose, Start, End, Miles, Vehicle, Deduction. ISO date format, UTF-8 BOM (Excel-friendly).
- **CSV — QuickBooks Online.** Drop-in for QBO's mileage importer.
- **JSON.** Same shape as the backup snapshot. For your own records or if you want to script something.
- **Excel (.xls).** Office Open SpreadsheetML 2003. Opens natively in Excel, Numbers, Sheets, and LibreOffice with proper date typing.

CSV cells are sanitized — values starting with `=`, `+`, `-`, or `@` get a leading apostrophe to neutralize formula injection. PDFs are generated locally with PDFKit. None of these touch the network.

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/hero-5-export.png" alt="Milely Export menu — PDF (Most Users Pick This), Excel (.xls), CSV — Milely (Full), CSV — QuickBooks Online" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Export menu — PDF, Excel, CSV (Milely full), CSV (QuickBooks Online).</figcaption>
</figure>

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/hero-6-pdf.png" alt="Milely annual mileage log PDF — totals, by-business breakdown, and per-trip details ready to hand to a CPA" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">The generated PDF — audit-ready summary.</figcaption>
</figure>

Filtering for export: the Reports year picker scopes the export. To export a single business or single month, filter Logs first, then tap the share icon there.

---

## Settings — Trip Settings

Settings → Trip Settings is where the recording engine is tuned. Three sub-sections.

### Manual

The default. No options to configure — Manual is intentionally minimal. The only control here is the Manual / Automatic switch at the top.

### Automatic

Turn the toggle on to enable automatic recording. Below the toggle:

- **Background Recording status card.** Live read of whether Always-Allow location, Motion & Fitness, and Background App Refresh are all green. If any are red, tapping the row jumps to iOS Settings to fix it.
- **Detection sensitivity.** Default. Higher = catches more rides but more false positives. Lower = fewer false positives, may miss short trips.
- **Advanced (disclosure).**
  - **Strict CarPlay Start** — see [Recording — Automatic mode](#recording--automatic-mode). Default off. Turn on to lock Automatic recording to your paired vehicles only.
  - Diagnostics for advanced troubleshooting.

### Universal (applies to both modes)

- **End Trip After Sitting Still** — stationary auto-end timeout for Automatic mode. Default 60 minutes. Per-vehicle override available in Vehicles.
- **Save Timestamps** — controls whether trip times are stored alongside dates. Default on. Some users prefer date-only logs for audit minimalism.
- **Minimum Logged Trip Miles** — trips shorter than this drop silently. Default 0.05 miles (filters out driveway shuffles).
- **Overnight Cutoff** — the universal "ends a forgotten trip at 4 a.m." backstop. Always on.

---

## Settings — Setup

The middle of the Settings screen — your data scaffolding.

<!-- SCREENSHOT NEEDED: settings screen showing setup section -->

### Businesses

Add one or more businesses you drive for. Each business has:

- **Name.** What shows in pickers and exports.
- **Color.** Tap to pick — this is the dot color throughout the app.
- **Logo.** Optional. Used on branded PDF reports for subscribers.
- **Accent color.** Optional. The branding color for PDFs.
- **Vehicle is fully business** toggle — if you have a dedicated business vehicle, every trip in that vehicle is automatically tagged to this business unless you override it.

Deleting a business doesn't delete its trips. They become "Unclassified" with the business color stripped — miles preserved, audit log preserved.

### Vehicles

Add one or more vehicles. Each has:

- **Name.** "Truck", "Wife's Car", "Sprinter Van".
- **Year, make, model.** Optional but useful for the per-vehicle records line on tax forms.
- **Beginning- and end-of-year odometer.** Track these for substantiation.
- **Paired routes.** The list of CarPlay / Bluetooth audio fingerprints Milely recognizes as "this vehicle is connected." See [pairing a vehicle](#pairing-a-vehicle) below.
- **Per-vehicle stationary auto-end** — overrides the universal default.

### Pairing a vehicle

Vehicle pairing is what lets Automatic mode skip the Armed state entirely (instant Recording when motion + paired audio coincide) and what enables CarPlay-disconnect pause and Strict CarPlay Start.

To pair: in Vehicles → tap a vehicle → **Add from Recently Connected**. Milely shows you a list of audio routes iOS has reported recently — your car will be one of them. Tap it; Milely stores the route fingerprint (port type, UID, name). You can have multiple routes per vehicle (CarPlay USB + CarPlay wireless + Bluetooth audio all link to the same vehicle).

Pairing is fully user-initiated — Milely never silently captures a UID or assumes a route belongs to you.

### Trip Templates (Favorites)

Saved one-tap trip starters. Each template has a name, a business, a vehicle, optional start and end addresses, an estimated miles figure, and a round-trip toggle. Templates surface in the Quick Start row's Favorites picker on the Dashboard. Useful for trips you repeat (weekly site visits, recurring deliveries).

### Auto-Classify Rules

Address-based rules for deterministic classification. See [Auto-Classify rules](#auto-classify-rules) above.

### Mileage Rate

Edit the cents-per-mile rate Milely uses for deduction calculations. Rates seed automatically for 2024–2026 with the published standard mileage rates. To use a custom rate (e.g. you're tracking actual expenses for one vehicle while standard for another), edit the per-year row.

### Tax Bracket

Set your federal tax bracket as a percentage. Milely uses this only to estimate "tax savings" on the Dashboard and Reports — it's a rough multiplier, not a tax calculation. Default is 0%, which hides the estimate everywhere.

### Data Retention

Defaults to keeping every trip forever. You can set a retention window (e.g. 6 years for typical audit lookback) which auto-deletes excluded trips beyond the window. Locked trips are never auto-deleted regardless of retention.

---

## Themes and branding

Milely ships with eight themes. The default on a fresh install is **Day** — pure-white cards, a soft neutral grey, an Azure blue accent. Quiet, restrained, deliberate.

<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 16px; max-width: 760px; margin: 24px auto;">
  <figure style="margin: 0;"><img src="/assets/screenshots/day.png" alt="Day theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Day (default)</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/night.png" alt="Night theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Night</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/light.png" alt="Light theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Light</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/warm.png" alt="Warm theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Warm</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/slate.png" alt="Storm theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Storm</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/sky.png" alt="Clear theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Clear</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/forest.png" alt="Mint theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Mint</figcaption></figure>
  <figure style="margin: 0;"><img src="/assets/screenshots/mint.png" alt="Minty theme" style="width: 100%; height: auto; border-radius: 14px; box-shadow: 0 4px 12px rgba(0,0,0,0.08);" /><figcaption style="text-align: center; font-size: 12px; color: var(--muted); margin-top: 6px;">Minty</figcaption></figure>
</div>

The other themes:

- **Warm** — the original Milely theme. Free for all users at all times.
- **Light** — high contrast, clean.
- **Night** — dark mode for evening use.
- **Storm** — slate blue-grey.
- **Clear** — minimal, near-monochrome.
- **Mint** — pale green.
- **Minty** — deeper green.

Seven of the eight (everything except Warm) require a subscription, lifetime, or an active trial. During the trial, every theme is unlocked with no badges. After the trial ends without a subscription, your theme snaps back to Warm and the locked themes show a small badge.

### Auto-pair

Above the theme list, the **Auto-Pair** card lets you pick separate themes for your phone's Light and Dark mode — Milely will switch automatically based on iOS appearance. Both halves of the pair are subscriber-gated (except for the Warm-Warm default).

### Branding (per business)

If you have a subscription, each business in Settings → Businesses can carry a logo, accent color, and footer text. These show on:

- Branded PDF reports.
- The Dashboard's monthly card business breakdown.
- The classify sheet's business picker.

Free and post-trial users get plain PDFs with the Milely default styling. Logos and accent colors stay configured even after a lapse — they re-activate the moment you subscribe again.

---

## Backup and restore

Milely runs entirely on the iPhone. Backups exist so you can move to a new phone or recover after a reset.

<!-- SCREENSHOT NEEDED: backup screen with cloud folder option -->

### Two options

**Choose Cloud Folder** (subscription required for automatic). On first setup, Milely opens the iOS Files-app folder picker. Pick anywhere — iCloud Drive, Google Drive, Dropbox, OneDrive, Box, or any folder iOS exposes. Milely remembers the folder via a security-scoped bookmark. From then on, "Back Up Now" writes a `milely-<timestamp>.json` file into a Milely Backups sub-folder. You can schedule daily auto-backups or trigger them manually.

**This iPhone Only.** Milely never writes anywhere automatically. Settings → Manual Export hands you a JSON file via the share sheet — Mail, Messages, AirDrop, save into Files yourself.

What's in the snapshot: every trip with full GPS polyline, every business, every vehicle and paired-route fingerprint, every receipt JPEG, AppSettings, and the seeded mileage rates. The trained smart-suggestions classifier is not in the snapshot — it retrains automatically from your restored trips.

### Restoring

On a new phone (or a fresh install), tap the `milely-*.json` file from anywhere — Files app, iCloud Drive, an email attachment, AirDrop. iOS opens Milely with an import dialog showing when the backup was created, what app version wrote it, and how many trips/businesses/vehicles/receipts the file contains.

Tap **Import**. Milely merges only new records. Existing trips are never overwritten — duplicates skip by unique ID. AppSettings on the restoring device is preserved.

---

## Importing from another tracker

Switching from MileIQ, Everlance, or TripLog? Milely reads their CSV exports directly.

Settings → Import. Pick the file from your Files app or share sheet. Milely auto-detects the format from the header row.

- **MileIQ** — Start Date, Stop, Start, Miles (or Miles (IRS)), Purpose, Notes, Category.
- **Everlance** — Date, Trip Distance, Trip Start, Trip End, Notes, Purpose, Tags, Type.
- **TripLog** — Date, Time, Distance, From Address, To Address, Purpose, Notes.

Maximum import size: 25 MB CSV (about 250,000 MileIQ rows) or 50,000 trip rows. Each imported trip gets an audit-log entry reading "Imported from <Source> CSV". Anything Milely doesn't recognize is rejected rather than silently mis-mapped.

If your old tracker uses a different format, export to JSON or CSV and let us know — `support@milely.io` is the fastest way to get a new importer added.

---

## Privacy and permissions

Milely's design starts with a hard rule: nothing is collected. The PrivacyInfo manifest declares zero data collection and zero tracking. There are no analytics SDKs, no crash reporters, no telemetry. The only outbound network traffic is:

- **Google's OAuth endpoints** when you sign in to back up to Google Drive.
- **Google's Drive upload endpoint** when you tap Back Up Now and the destination is Google Drive.

Both are user-initiated. iCloud Drive backups are handled by iOS — Milely never touches Apple's network APIs directly.

When you switch apps, Milely overlays a brand splash so the iOS multitasking switcher caches the splash instead of your dashboard data.

### Permissions Milely asks for, and what happens if you deny

| Permission | Why | If denied |
|---|---|---|
| Location (When in Use) | Record trip routes | Manual trips with a route map don't work |
| Location (Always) | Wake the app for Automatic mode | Automatic mode doesn't function; Manual still works |
| Motion & Fitness | Distinguish driving from walking/biking | Automatic falls back to GPS-only detection |
| Camera | Scan paper receipts | Photo-library import still works |
| Photo Library | Attach receipts from camera roll | Camera scan still works |
| Calendar (opt-in) | Suggest trips from events | Calendar suggestions feature off |
| Notifications | Weekly review, classify prompt, recovery | Find trips manually in Logs |

Milely never asks for: contacts, microphone, health data, or App Tracking Transparency.

### What's in iCloud, what's only on the phone

- **iCloud device backup** (iOS-managed, encrypted by Apple): your Milely sandbox is included by default — every trip, every receipt, every setting. Restoring a new device from iCloud restores Milely with everything intact, no separate Milely backup needed.
- **iCloud Keychain**: nothing. The Google Drive OAuth refresh token uses `kSecAttrSynchronizable=false` — it stays on this device only.
- **Milely cloud-folder backup**: trips, receipts, businesses, vehicles, AppSettings, mileage rates. The audit log (per-edit timestamps) is intentionally omitted to keep backups small and not leak edit timing to cloud storage.

---

## Subscription and the 7-day trial

Milely's pricing is straightforward.

<figure style="margin: 24px auto; max-width: 320px;">
  <img src="/assets/screenshots/hero-7-subscription.png" alt="Milely Subscription view — monthly and annual plans, the seven-day trial detail, and the lifetime option behind Other options" style="width: 100%; height: auto; border-radius: 24px; box-shadow: 0 8px 24px rgba(0,0,0,0.08);" />
  <figcaption style="text-align: center; font-size: 13px; color: var(--muted); margin-top: 8px;">Subscription — monthly, annual, and the lifetime option.</figcaption>
</figure>

### The trial

The 7-day free trial gives you the entire app — recording, exports, themes, branded PDFs, cloud backup, receipts, everything. The clock starts the **first time you record a trip** — not at install, not at first launch. You can install Milely today and not start the clock until you actually drive.

The Dashboard shows a countdown banner during the trial with days left and a Subscribe button.

### After the trial

If you subscribe, nothing changes — the app keeps working as it did during the trial.

If you don't subscribe, the only thing that locks is **recording new trips**. Everything else stays available forever:

- Viewing every trip you've already recorded.
- Editing trips, adding receipts, attaching purposes.
- Exporting to PDF, CSV, JSON, Excel.
- Backing up. Restoring.
- Locking trips for audit defense.

Recording new trips requires a subscription. The Manual Start button and Automatic detection are gated behind the paywall once the trial ends. Manual past-trip entry (typing in a trip you already drove) is also gated — that's a "creating a new trip record" action.

### Plans

- **Monthly — $3.99/month**, 7-day free trial.
- **Annual — $29.99/year** (about 37% savings), 7-day free trial.

Both are surfaced in Settings → Subscribe. Annual is on top because most users prefer it.

### Lifetime (the quiet option)

Some people refuse subscriptions on principle. For them, Milely offers a **$69.99 lifetime** purchase, surfaced under "Other options" at the bottom of Settings → Subscribe. One-time payment, never expires. We don't promote it — the math favors annual for most users — but it's there.

### Restore Purchases

If you've subscribed before and re-installed Milely (new phone, factory reset), tap **Restore Purchases** at the bottom of Settings → Subscribe. Apple looks up your Apple ID's entitlements and restores your subscription instantly.

### Family Sharing

Milely subscriptions are not Family Shareable. Each member of your family who wants Milely gets their own subscription.

---

## Year-end and the audit lock

The point of a mileage log is that it stands up under audit. The audit lock is what makes that work.

<!-- SCREENSHOT NEEDED: audit lock banner on dashboard -->

### What locking does

A locked trip cannot be edited or deleted. The miles, route, business, purpose, vehicle, receipts, and audit log all freeze. If your CPA or a tax authority later asks to verify the log, the locked records prove that nothing was edited after the year closed. That's the audit-defensibility story.

### The annual prompt

On or after **February 1** each year, the Dashboard shows a yellow banner: "Lock {prior-year} trips?" Tap **Lock {year}** to lock every unlocked business trip from the prior year in one tap. Tap **Not Now** to dismiss the banner for the rest of the calendar year — it'll come back next February if there are still unlocked trips.

You can also lock individual trips manually at any time from trip detail.

### Important caveats

- Locking is **irreversible per trip**. The confirmation alert asks again before applying it. Once locked, that trip cannot be unlocked or deleted.
- Locking a trip happens after you classify it. Lock too early and you can't fix typos.
- Locked excluded trips stay locked. The audit log shows whether the lock was manual or automatic (with timestamps).
- February 1 is the cutover date specifically because it gives you all of January to finalize the prior year — January receipts, last-minute corrections, missing trips imported from CSV — without the lock prompt nagging.

### Year-end odometer

Settings → Vehicles → tap a vehicle → **End-of-year odometer**. Snap a photo of the dashboard. Same field for January 1's beginning-of-year reading. This gives substantiation for the percentage-of-business-use calculation per vehicle.

<!-- SCREENSHOT NEEDED: year-end odometer photo entry -->

---

## Watch app and widget

### Apple Watch (display only)

Milely on the watch is a simple status display. When a trip is recording, the watch shows live miles, formatted duration, and a green "Recording" caption. When idle: "No trip in progress — open Milely on iPhone to start." There are no buttons. There are no complications. Starting and ending trips happens on the phone.

### Home-screen widget

Two sizes — Small and Medium — both showing your month-to-date deduction and miles. Refreshes every 30 minutes. Tapping the widget opens Milely.

### Lock-screen Live Activity

When a trip is recording, iOS shows a Milely Live Activity on the lock screen and the Dynamic Island (iPhone 14 Pro and later) with the live miles, duration, deduction, and business. Glance-only — the controls live in the app.

---

## Troubleshooting

### Automatic mode isn't picking up my drives

Run through these in order:

1. **Confirm Always-Allow location.** Settings → Trip Settings — the Background Recording status card tells you. If it's red, tap to fix.
2. **Confirm Motion & Fitness.** Same status card.
3. **Confirm you didn't force-quit Milely.** iOS suspends background-recording listeners after a force-quit until you launch the app again. Don't swipe Milely out of the app switcher.
4. **Check Strict CarPlay Start.** Settings → Trip Settings → Automatic → Advanced. If this toggle is on but the drive wasn't in a paired vehicle, Automatic correctly ignores it. Either pair the vehicle or turn Strict off.
5. **Wait a few seconds.** The Armed → Recording promotion takes 5–10 seconds at minimum. Very short trips (under a minute) sometimes drop below the minimum-mile threshold and don't save.

### A trip stopped recording mid-drive

Most often this is iOS reclaiming the app under memory pressure. Milely should surface a "Recover trip in progress?" alert the next time you launch — tap Recover to keep the trip alive. If you see "Save as Partial" instead, the recovery was outside the 7-day window.

To reduce this happening: don't force-quit Milely from the app switcher.

### Trip is missing the first few minutes of driving

In Automatic mode, this is what backfill is supposed to fix. If it didn't fully recover, edit the trip's start address in trip detail.

In Manual mode, this means you tapped Start a few minutes after you actually started driving. Edit the start time in trip detail.

### CarPlay disconnect didn't pause the trip

Confirm you're connected via the audio route (CarPlay USB, CarPlay Wireless, or the car's Bluetooth A2DP/HFP audio profile). A USB charging cable that doesn't carry CarPlay data won't trigger the pause behavior.

### The trial ended and now I can't tap Start

That's working as designed. Subscribe in Settings → Subscribe, or buy lifetime under Other options. Your existing trips stay viewable and exportable forever — you don't lose anything by waiting.

### Restore from backup says "0 source app version"

Older backups didn't write a clean app-version stamp. Restore still works — the version line is informational only.

### CSV import says "format not recognized"

Milely auto-detects MileIQ, Everlance, and TripLog formats from the header row. If your export doesn't match, open the CSV in a text editor and check the first line. Email `support@milely.io` with the format and we'll add it.

---

## Glossary

<div class="glossary-cols" markdown="1">

**Manual mode** — recording controlled by you tapping Start and End. The default.

**Automatic mode** — Milely watches motion and GPS to start recording on its own.

**Armed** — Automatic state where GPS is on but no trip is committed yet. Confirms before recording.

**Recording** — a trip is actively being captured.

**Classified** — a recorded trip with a business and purpose attached.

**Locked** — a classified trip frozen for audit defense; no further edits.

**Excluded** — a trip flagged as non-deductible. Stays in Logs but absent from Reports.

**Unclassified** — a recorded trip with no business yet assigned. Surfaces with a Classify CTA.

**Paired vehicle** — a vehicle whose CarPlay or Bluetooth audio route fingerprint Milely recognizes.

**Strict CarPlay Start** — toggle that locks Automatic recording to your paired vehicles only.

**Backfill** — the rolling buffer Milely uses to recover the leading minutes of an Automatic trip.

**SLC** — significant location change. iOS's low-power "phone moved meaningfully" signal.

**Audit lock** — the irreversible-per-trip freeze applied to prior-year trips for audit defense.

**Trial** — the 7-day free run of all features. Starts on your first recorded trip.

**Quick Start** — Dashboard shortcuts that begin a trip pre-tagged to a business or template.

**Trip template** — a saved one-tap trip launcher with pre-filled business, vehicle, and addresses.

**Auto-Classify rule** — a deterministic address-based rule for tagging matching trips.

**Smart suggestion** — the on-device classifier's best guess at business and purpose for a new trip.

**Standard mileage rate** — the cents-per-mile rate published annually for tax-deductible business mileage.

**Snapshot** — the JSON file Milely writes during backup. Contains trips, receipts, businesses, vehicles, settings.

**Audit log** — per-trip record of every edit, receipt add, and lock action with timestamps.

</div>

---

*© 2026 SmileyCreative LLC. All rights reserved.*

</main>
