---
layout: default
title: User Guide
description: The complete Milely user guide — first-launch setup, recording trips, classifying, reports, exports, vehicles, businesses, and every setting in plain English.
permalink: /help/user-guide/
---

<main markdown="1">

# Milely user guide

This is the long-form user guide. It walks through everything Milely does, in roughly the order you'll do it. If you just want quick how-to recipes, the shorter [Help & How-To page](/help/) covers the most common tasks.

Milely is a private, on-device mileage tracker for iPhone. It records the trips you drive for business and gives you the records you need for tax deductions. Nothing leaves your phone unless you choose to back it up to your own cloud folder. There's no Milely server, no Milely account, no shared data.

This guide assumes you're not technical. There's no jargon you can't skip past. If a term sounds unfamiliar, it's defined in the [glossary](#glossary) at the bottom.

---

## Contents

1. [What Milely does](#what-milely-does)
2. [First-time setup](#first-time-setup)
3. [The Dashboard at a glance](#the-dashboard-at-a-glance)
4. [Recording a trip](#recording-a-trip)
5. [Classifying a trip](#classifying-a-trip)
6. [Personal trips](#personal-trips)
7. [Receipts](#receipts)
8. [The Trip detail screen](#the-trip-detail-screen)
9. [Logs (your trip list)](#logs-your-trip-list)
10. [Reports](#reports)
11. [Exports](#exports)
12. [Vehicles](#vehicles)
13. [Businesses](#businesses)
14. [Settings reference](#settings-reference)
15. [CarPlay and background recording](#carplay-and-background-recording)
16. [Trip recovery](#trip-recovery)
17. [Subscription and free tier](#subscription-and-free-tier)
18. [Privacy and data](#privacy-and-data)
19. [Troubleshooting and FAQ](#troubleshooting-and-faq)
20. [Glossary](#glossary)

---

## What Milely does

You drive for work. The IRS lets you deduct those miles at a standard rate. To take the deduction, you need a record showing when you drove, how far, where, and why.

Milely keeps that record for you.

You can record trips manually (tap Start, drive, tap End), automatically (the phone notices you're driving and starts recording on its own), or by triggering recording when CarPlay or your car's Bluetooth connects. Once a trip is recorded, you classify it — pick which business it was for, type a brief purpose, save. At tax time you export a PDF or CSV that lays it all out.

Everything runs on your iPhone. Milely doesn't have servers; your trips, addresses, receipts, and routes never leave the device unless you put them somewhere yourself (a backup file, an emailed PDF, a cloud folder you choose).

---

## First-time setup

The first time you open Milely you'll go through three short screens before you can use the app.

### Welcome and consent

A welcome screen asks you to confirm two things:

- You're old enough to use the app (13+ in most regions, 16+ in the EU/UK by GDPR rule). Milely auto-detects which threshold applies based on your phone's region.
- You agree to the Terms of Service and Privacy Policy. Both link out to the public copies on milely.io.

Tap both checkboxes, then **Continue**. Both confirmations are stored locally on your phone — nothing is transmitted. You'll only see this screen again if Milely's terms or privacy policy materially change in a future update.

<!-- SCREENSHOT NEEDED: legal consent screen with both checkboxes filled and the Continue button enabled -->

### Onboarding walkthrough

After you continue, Milely walks you through 8 quick steps:

1. **Welcome to Milely.** A one-line overview.
2. **How it works.** Tap Start, drive, tap End.
3. **What's your business?** Type the business name you'll track miles for. You can add more later. (For example: "Greg's Real Estate", "Smith Plumbing", "Acme Consulting".) The seed business "Real Estate" is replaced with whatever you type here.
4. **Backup choice.** If you have a Milely subscription, you'll pick where to back up: iCloud Drive (recommended), Google Drive (uses iOS's Files picker — Google Drive must be installed), or "This iPhone only" (no automatic backup). Without a subscription, you'll see an info screen explaining that your data lives on this phone, with the option to export manually any time.
5. **Location access.** Tap **Allow Location**. iOS will ask "Allow Milely to use your location" with three choices: Allow Once, Allow While Using, Don't Allow. Pick **Allow While Using** for now — Milely will ask for the upgraded "Always" permission later (when you pair a vehicle for background recording). Without location access Milely can't measure trip distances.
6. **Notifications.** Optional. Lets Milely send you the weekly review reminder if you want one. You can turn this on or off later.
7. **Add a vehicle?** You can type a vehicle name (Truck, Wife's Car, etc.) and tap **Add Vehicle**, or **Skip**. The IRS asks for per-vehicle records on Schedule C / Form 2106, so adding at least one vehicle now saves you headaches at tax time. If you skip, the Dashboard shows a small "Add a vehicle for IRS Form 2106 records" reminder until you add one.
8. **You're all set.** Tap **Get Started** to land on the Dashboard.

<!-- SCREENSHOT NEEDED: onboarding business-name step with text field showing "Greg's Real Estate" -->
<!-- SCREENSHOT NEEDED: onboarding vehicle step with the Skip and Add Vehicle buttons -->

### What permissions Milely actually uses

- **Location.** Required to record trips. Milely uses location only during a trip. Pairing a vehicle later prompts you to upgrade to Always-Allow, which is what enables Milely to start recording in the background when you start driving.
- **Motion & Fitness.** Optional. Used by Automatic detection mode to recognize you're driving (vs walking, biking, or sitting still). If you stay in Manual mode, this isn't needed.
- **Notifications.** Optional. Used for the weekly review reminder, the "trip stopped — classify it?" prompt after auto-detected trips, and the "Recover trip in progress?" prompt after a force-quit.
- **Calendar.** Optional. Used by two features: the calendar suggestions on the Trip tab (turns upcoming events into one-tap trip starters) and the "Recover from calendar" tool that surfaces past events with locations as proposed trips. Calendar data is read on-device only.
- **Photo Library.** Optional. Used only when you tap "Add from photos" on a trip's receipts row.
- **Camera.** Optional. Used only when you scan a receipt with the document scanner.

Milely never asks for: your contacts, your microphone, your health data, or anything else.

---

## The Dashboard at a glance

The Dashboard is the home screen. Here's what every tile does, top to bottom.

<!-- SCREENSHOT NEEDED: full Dashboard with monthly card, Quick Start row including business + Personal + Repeat Last + Favorites, and the Start Trip button -->

### Audit Lock reminder banner (January 31 each year)

Once a year, on or after February 1, you'll see a yellow banner at the top of the Dashboard asking whether to lock last year's trips. Tapping **Lock [year]** locks every unlocked business trip from the prior year so it can't be edited or deleted later — that's the audit-defense guarantee. Tapping **Not now** dismisses the banner for the rest of the calendar year. The banner reappears the following January if there are still unlocked prior-year trips.

Locking is irreversible per trip. The confirmation alert will ask you again before applying it.

<!-- SCREENSHOT NEEDED: the yellow audit-lock banner on the Dashboard with Lock and Not now buttons -->

### Live trip banner (only while recording)

When a trip is recording, the very top of the Dashboard shows a live banner with a red blinking dot, "Recording trip", the live distance, time elapsed, and dollar deduction tallying up in real time. There's an **End** pill on the right of the banner — tap it to stop the trip. Tapping the banner itself opens a small editor where you can change the trip's business, purpose, or vehicle without ending it.

If a trip is paused (because the CarPlay you started in just disconnected), the dot turns yellow and shows a pause glyph, and the eyebrow text reads "Paused" instead of "Recording trip".

<!-- SCREENSHOT NEEDED: live trip banner showing distance, time, deduction, with the End pill on the right -->

### First-launch empty state

If you haven't recorded any trips yet, you'll see a small "No trips yet" card explaining what Start Trip will do. This card disappears the moment you save your first trip.

### Monthly Report Card

Once you have trips, the Dashboard shows a card for the current month with:

- **Hero deduction figure.** The dollar value of this month's business mileage, large.
- **Bracket savings.** If you've set your federal tax bracket in Settings → Tax Bracket, you'll see "≈ $X saved" — a rough estimate of how much that deduction reduces your tax bill.
- **Mileage rate.** Shows the cents-per-mile rate Milely is using for the calculation (the IRS standard, e.g. 70 cents/mi).
- **Donut chart.** Visual breakdown of miles by business this month. Tap the legend to see each business's miles and trip count.

Personal trips are excluded from every figure on this card.

### Quick Start row

Below the monthly card, "Quick Start" surfaces shortcuts for the most-used actions:

- **Top businesses (up to 3).** One row per business, sorted by miles this month. Each shows the business's color initials, the trip count, and total miles. Tap to start a trip pre-tagged for that business.
- **Personal.** Green "P" tile, shows this month's Personal trip count and miles, with "Non-deductible" caption. Tap to start a Personal trip directly. (Only appears if "Keep personal trips" is on in Settings — it is by default.)
- **Repeat Last.** Yellow refresh tile. Starts a new trip pre-filled with the same business and purpose as your most recent trip.
- **Favorites.** Yellow star tile. Opens a picker of your saved trip templates. Tap any template to start a trip from it.

<!-- SCREENSHOT NEEDED: Quick Start row with one or two business rows, the green P Personal row, Repeat Last, and Favorites -->

### Start Trip button

Below the Quick Start row, the big burnt-orange **Start Trip** button is the unconditional way to begin recording. Tap it, drive, then end the trip from any tab.

### No-vehicle callout

If you skipped the vehicle step in onboarding (or never added one in Settings), a small yellow callout appears reading "Add a vehicle for IRS Form 2106 records." Tapping it opens the Vehicles editor in a sheet so you can fix the gap without leaving the Dashboard. The callout disappears once you've saved one vehicle.

---

## Recording a trip

There are three ways to record a trip. You can mix and match — they're not mutually exclusive.

### Manual: tap Start, drive, tap End

This is the simplest path and works in every detection mode.

1. From the **Dashboard** or the **Trip** tab, tap **Start Trip** (or pick a Quick Start row to pre-tag the business).
2. Drive. Milely captures GPS waypoints in the background. You can switch apps, lock your phone, leave Milely entirely — recording continues. The route line draws on the map in real time on the Trip tab.
3. When you arrive, tap **End Trip**. The button is on the live banner at the top of the Dashboard, on the live map on the Trip tab, and as a pill in the Logs tab header — pick whichever is closest.
4. The Classify screen appears. Pick a business, type a purpose, save.

If you tap End by accident, the Classify screen has a small **Resume trip** button at the top. Tap it within a few seconds to roll back into recording — the time you spent on the Classify screen is folded into "paused time" and excluded from the trip's duration.

<!-- SCREENSHOT NEEDED: live map with route polyline drawn, stats card overlay, and the End trip button at the bottom -->

### Automatic mode (motion + significant location changes)

In Automatic mode, Milely watches for driving even when you haven't tapped Start. Switch to it in Settings → Detection mode → **Automatic**.

How it works (in plain terms):

- iOS occasionally tells Milely "the phone has moved a meaningful distance from where it last reported." That's the *significant location change* signal. It uses very little battery because the phone is doing it for other system reasons anyway.
- When that signal lands, Milely briefly checks: are we moving fast enough to be in a vehicle? If yes, recording starts.
- Recording continues until you've been stopped long enough (the **stationary auto-end timeout** in Settings) and CarPlay isn't connected. Then the trip ends automatically.
- iOS sends you a notification: "Trip ended — tap to classify." If you tap, the Classify screen opens. If you don't, the trip lands in Logs marked **Unclassified** and you can classify it later.

Automatic mode requires:

- **Always-Allow location.** "While Using" isn't enough — iOS won't wake the app for SLC events on While-Using. Settings → Detection mode shows a "Background recording" status card that tells you whether you're set up correctly.
- **Motion & Fitness permission.** Used to filter out walking/biking from real driving.

Automatic mode does NOT keep GPS running constantly. It uses the SLC signal as a wakeup, then turns on full GPS only when it's actually recording a trip. Battery impact is small unless you drive a lot.

<!-- SCREENSHOT NEEDED: Settings → Detection mode → Automatic card selected, with the Background recording status card showing "Active" -->

### CarPlay-trigger (the most accurate option)

If you've paired a vehicle in Milely (Settings → Vehicles → see the [Vehicles section](#vehicles)), connecting your phone to that vehicle's CarPlay or car-Bluetooth audio route triggers a trip start automatically.

How it works in plain terms:

- iOS notices an audio route connected (CarPlay or your car's hands-free Bluetooth).
- Milely matches the connected device's identifier to a paired vehicle in your records.
- The first time this happens for a new vehicle, Milely shows a one-time prompt asking "Auto-start trips when you connect to [vehicle]?" Tap **Yes, do that** to confirm. From then on, connecting to that vehicle silently starts a trip.
- When you disconnect (engine off + phone leaves the car), the trip pauses or ends depending on the vehicle's settings.

This is the most accurate detection signal Milely has — UID-matching CarPlay or Bluetooth is essentially never wrong, where motion-detected can occasionally fire on a passenger ride or miss a slow start. If you have CarPlay or Bluetooth in your vehicle, this is the recommended setup.

<!-- SCREENSHOT NEEDED: first-time CarPlay consent prompt with Yes do that and Not yet buttons -->

### What happens during recording

While a trip is recording, regardless of how it started:

- The **Trip tab** shows a live map with your route drawing as a polyline. Pinch-zoom and pan like Apple Maps.
- A stats card on the map shows live **Distance**, **Time**, and **Deduction** updating every second.
- The **Dashboard** shows the live banner described earlier.
- The **Logs** tab adds an "End trip" pill to its header so you can stop without changing tabs.
- iOS keeps Milely running cleanly even with the screen locked or another app in the foreground.
- Every 30 seconds, Milely snapshots your in-progress trip to disk, in case the app is force-quit, runs out of memory, or your phone dies. See [Trip recovery](#trip-recovery).

### Logging a past trip manually

Forgot to start a trip? Open the **Logs** tab and tap **Log Past Trip Manually** at the top. A form lets you type the date, addresses, miles, business, purpose, and (optional) odometer readings. Tap **Save Trip** to add it to your records. Manual past entries count against your free-tier monthly limit just like recorded trips.

<!-- SCREENSHOT NEEDED: Log Past Trip Manually form with date picker, From/To address fields, miles, business chips, and purpose field -->

---

## Classifying a trip

Right after a trip ends, the Classify screen appears as a sheet titled "Review & save."

It's organized top to bottom:

- **Trip just ended** eyebrow with a small **Resume trip** undo button on the right (in case you tapped End by accident).
- **Review & save** title.
- **Route map** showing the trip's path with start and end markers.
- **Trip facts.** Three numbers — distance, duration, end time — that you can sanity-check at a glance.
- **Editable fields.** Miles, date/time, From address, To address. Pre-filled but editable. The addresses come from a reverse-geocode of the trip's start and end coordinates, and may take a moment to populate after the screen appears.
- **Smart Suggestions** (when applicable). On-device pattern matches from your past classifications surface as one-tap chips above the business row. Tap to apply.
- **Business chips.** One per business you've created. Tap to select.
- **Personal chip.** Below the business row (when "Keep personal trips" is on). Selecting Personal clears any business and skips the purpose field — Personal trips don't need one.
- **Calendar suggestions.** If the trip overlapped any calendar events with locations, those titles surface as one-tap chips you can use as the purpose.
- **Recent purpose chips.** Up to 6 most-recent purposes for the chosen business. Tap one to fill the purpose field instantly.
- **Purpose field.** Free-text. Required for business trips. Specific is better than generic — "Showing 1428 Maple St" reads better in an audit than "Real Estate."
- **Vehicle chips.** Pick which vehicle you drove. Auto-fills from your CarPlay/Bluetooth pairing if matched, otherwise from your default vehicle.
- **I was driving toggle.** Default ON. Turn off if you were a passenger (Uber, ride-along, carpool). Off marks the trip Personal so it doesn't count toward your deduction.
- **Round trip toggle.** Default OFF. Turn on if you'll drive the same route back — Milely doubles the miles and saves it as one record.
- **Receipts row.** Subscriber feature. See [Receipts](#receipts).
- **Ready to save** summary. The final values that will be saved if you hit Save Trip.
- **Save Trip** button. Shows the deduction amount when you tap it (e.g. "Save Trip · $12.40"), unless the trip is Personal — Personal saves just say "Save Trip."
- **Skip for now** button. The trip lands in Logs as **Unclassified**. You can classify it later by opening it in Logs and editing.

<!-- SCREENSHOT NEEDED: Classify Trip screen scrolled to show route map, business chips, purpose field, and the Save Trip button -->

### What "Skip for now" actually does

This used to be called "Cancel" and people read it as "throw the trip away." It does NOT throw the trip away. The trip is already saved to Logs the moment recording ends — Skip for now just leaves it Unclassified. Open it from Logs anytime, fill in the business and purpose, and save.

This means: even if you crash, kill the app, or never tap Save, your recorded miles are not lost. They're sitting in Logs waiting for you.

### Smart Suggestions (on-device pattern matching)

If you've classified a few trips already, the Classify screen may show "SMART SUGGESTIONS" with chips like "Real Estate · 92%" or "Personal · 88%." Tap a chip to apply that business and purpose to the current trip.

How it learns: from your saved classifications, on your phone. After each save, Milely re-trains a small machine-learning model in the background using Apple's CoreML framework. The model never leaves your device. There's no Milely server, no shared model, no analytics pipeline. Uninstall the app and the model goes with it.

If you have an auto-classify rule that already matched the trip, the Smart Suggestions chips render dimmed and informational — they show what the model thought, but tapping them does nothing because the rule has already chosen for you.

---

## Personal trips

Personal trips are drives that aren't business. Driving to the grocery store, picking up the kids, weekend errands. Milely has a first-class concept of Personal so you can record them and exclude them from your deduction without losing the record.

Three things define a Personal trip:

- **No business attached.** It's not "Real Estate" or "Smith Plumbing" or anything.
- **No purpose required.** The IRS doesn't ask why you went to the grocery store. The Classify screen hides the purpose field for Personal trips.
- **Zero deduction.** Personal miles don't contribute to your business mileage total in any report or export. Ever.

You'll see Personal trips marked with a small green pill in lists and on the live banner.

### How to mark a trip Personal

- **At the moment you classify it.** Tap the **Personal** chip below the business row on the Classify screen.
- **From the Logs tab.** Swipe left on a trip row. The trip is marked Personal AND locked in one motion (Personal trips usually mean "this isn't deductible — set it aside").
- **From the trip detail screen.** Tap the trip in Logs, scroll to the bottom, tap **Mark as personal**.
- **Mid-trip.** Tap the live banner on the Dashboard and pick **Personal** from the business dropdown.
- **From the Dashboard.** Tap the green Personal Quick Start row to start a new trip pre-tagged Personal.

### The Personal Quick Start row

When "Keep personal trips" is on (Settings → Personal Trips), the Dashboard's Quick Start shows a green Personal row with this month's personal trip count and miles. It reads "X trips · non-deductible" so the meaning is clear.

### The Personal filter chip in Logs

The Logs tab's filter row has a green **Personal** chip. Tap it to filter the list to only Personal trips. Personal and the business filter are mutually exclusive — picking one clears the other.

### What happens if you turn "Keep personal trips" off

If you set Settings → Personal Trips → Keep personal trips to OFF:

- The Personal chip disappears from the Classify screen and the live trip editor.
- The Dashboard's Personal Quick Start row hides.
- Existing Personal trips stay in Logs (they're never silently deleted).
- When you next open the Reports tab on a year that has unlocked Personal trips, Milely asks: "Delete N Personal trips from [year]?" Tap Delete to remove them, or Keep to leave them. Either way, you're prompted only once per year.
- Locked Personal trips are NEVER deleted, regardless of your answer.

This gives you two clean modes: Personal as a first-class category, or Personal as a passing label that gets cleaned up at year-end.

---

## Receipts

Snapping receipts to your trips makes audit responses trivial. Milely supports receipts as a subscriber feature.

### Adding a receipt

Open any trip in Logs (or scroll down on the Classify screen during a trip-end review). The **Receipts** row has two buttons:

- **Scan receipt.** Opens iOS's document scanner (the same one Apple Notes uses). Edge detection, perspective correction, multi-page support. Point your camera at the receipt; tap the auto-captured page; repeat for more pages; tap Save when done.
- **Add from photos.** Opens the iOS photo picker so you can attach existing photos from your camera roll.

After you scan or pick, Milely processes each image:

- Strips EXIF metadata (location, timestamp, device info) so the image you save is the picture and nothing else.
- Re-encodes as JPEG for size.
- If the image is over 5 MB, Milely tries to recompress further. If it's still too big after that, it's rejected with a warning — try a smaller scan or fewer pages.
- Up to 10 receipts per trip.
- Receipts live in a per-trip folder under the app's local storage. They never leave your device unless you back up.

### OCR amount detection

When you scan a new receipt, Milely runs Apple's on-device VisionKit OCR to look for a likely receipt total. If it finds one, the total amount surfaces below the Receipts row as a quick-fill chip. The number isn't required for anything — Milely doesn't compute deductions from receipts — but it lets you see at a glance that the scan worked and capture the amount somewhere.

### What's on the PDF report

Subscriber PDF reports include a thumbnail of each receipt next to the trip it's attached to. Free-tier reports do not (receipts themselves are subscriber-only).

### Removing a receipt

Open the trip, tap the small × on a receipt thumbnail, confirm. The image is deleted from the device immediately. The action is logged in the trip's edit history.

You can't add or remove receipts on a locked trip — unlock it first via Trip detail → Unlock for editing.

<!-- SCREENSHOT NEEDED: Trip detail with the Receipts row showing two attached receipt thumbnails and the Scan / Add from photos buttons -->

---

## The Trip detail screen

Tap any trip in Logs to open Trip detail. Top to bottom:

- **Route map.** Full route with start (yellow marker) and end (orange marker). The "Open in" menu in the top-right deep-links into Apple Maps so you can see it in a full map app or get directions back.
- **Stats row.** Distance, duration, time of day.
- **Date.** Editable.
- **Purpose.** Editable.
- **Project / Client.** Free-text tag. Type "1428 Maple listing", "Acme matter", "Smith remodel" — whatever your industry uses. The tag surfaces as its own column in CSV exports and as a "By project" breakdown in Reports.
- **Addresses.** From and To, editable.
- **Business.** Picker. Reassign by tapping.
- **Vehicle.** Picker.
- **Odometer.** Optional start and end odometer for this trip. Filling these in produces an audit-defensible record beyond just GPS miles.
- **Receipts.** See above.
- **Auto badge.** If the trip was auto-detected, a small "Auto-detected" badge appears here.
- **Auto-classify future trips here.** Two buttons — **Always business: [name]** and **Always personal**. Tap one to create an [auto-classify rule](#auto-classify-rules) that fires on every future trip ending at this same address.
- **Edit history.** Every field-level change to the trip, with old value, new value, and timestamp. Includes locking, unlocking, Personal toggling, receipt adds and removes. Always on, always captured. Can't be wiped from inside the app (deleting the trip removes the history with it).
- **Lock / Unlock button.** Tap to lock the trip (immutable for audit) or unlock (to edit again). Locked trips show a lock icon in the row.
- **Mark as business / Mark as personal button.** Only on unlocked trips. Flips the Personal flag.
- **Delete Trip button.** At the bottom, in destructive red. Asks for confirmation. Locked business trips can't be deleted — unlock first. Locked Personal trips can be deleted (they don't reach IRS reports anyway).

### The star button

In the top-right toolbar of any trip detail screen there's a **star** icon. Tap it to save this trip as a Favorite (a Trip Template). The favorite shows up on the Dashboard's Favorites Quick Start row for one-tap re-launching of similar drives.

<!-- SCREENSHOT NEEDED: Trip detail screen with route map, all sections visible, star button in the top-right -->

### Audit Lock

Lock means "frozen for audit." On a locked trip:

- Every editable field is read-only.
- Receipts can't be added or removed.
- The trip can't be deleted (unless it's Personal).
- The Personal flag can't be flipped.

To unlock, tap **Unlock for editing** on the detail screen. The unlock action and any subsequent edits are written to the edit history, so even if you do reopen a closed year there's a clean paper trail showing exactly what changed and when.

Trips lock automatically once a year on January 31 if you accept the Audit Lock reminder banner on the Dashboard. You can also lock individual trips manually via the Lock button or by swiping right on a row in Logs.

### Edit history

Every change writes a row to the edit history. Field, old value, new value, timestamp. You don't have to do anything to turn it on — it just runs. The history is there for the IRS, your CPA, or you-six-months-from-now wondering what changed.

---

## Logs (your trip list)

The Logs tab is your full trip history.

### The header

A frozen header pinned at the top has:

- **Logs** title and the **Select** button (toggles bulk-select mode).
- An **End trip** pill (only when a trip is recording — quick stop without changing tabs).
- A search field that filters across purpose, From address, To address, and business name.
- A row of four filter pills: **Year**, **Month**, **Business**, **Personal**. Year and Month default to the current year + month. Personal and Business are mutually exclusive — picking one clears the other.

<!-- SCREENSHOT NEEDED: Logs tab header showing the search field, Year/Month/Business/Personal filter pills, and a list of trips below -->

### The trip list

Trips are grouped by date with smart labels — **Today**, **Yesterday**, **This week**, **This month**, then "April 2026" / "March 2026" / etc. Each trip row shows the purpose, business pill, miles, time, and any flags (locked, Personal, has-receipts, unclassified).

Tap a row to open Trip detail.

Long-press a row to open a context menu with **Lock trip / Unlock trip**, **Mark as personal / Mark as business**, and **Delete trip** (when allowed).

### Swipe actions

- **Swipe right** on a trip row → **Lock as Business** (burnt orange pill, lock icon).
- **Swipe left** on a trip row → **Lock as Personal** (blue pill, person icon). Sets the trip to Personal AND locks it in one motion.

Both swipes only fire on "active" trips (not already Personal, not already locked). Already-Personal or already-locked rows don't budge when swiped — to undo either, tap into the trip detail and use the Unlock and Mark as business buttons at the bottom of the page.

### Bulk select

Tap **Select** in the top-right to enter bulk-select mode. The rows grow checkboxes; tap to add to your selection. With at least one trip selected, a bottom action bar shows **N selected** and a **Reassign** button. Reassign opens a sheet that bulk-changes the business on every selected trip in one shot. Locked trips are skipped (and you'll see a count of skipped trips in the result alert).

Tap **Done** in the top-right to leave selection mode.

### Logging a past trip manually

The **Log Past Trip Manually** button at the top opens [the manual entry form described earlier](#logging-a-past-trip-manually).

### Floating Add button

The bottom-right has a circular **+** button that also opens the manual entry form. Same form, easier to reach.

### Recovering trips from your calendar

If you forgot to use the app for a stretch and have calendar events with locations during that time, Settings → Setup → **Recover from calendar** can rescue you. Pick a lookback window (14 / 30 / 60 / 90 days), Milely reads your past calendar events with locations, dedupes against trips you've already saved, and shows the rest as proposed trips. Check the ones you actually drove, tap **Create N trips**, and they become normal records. (Calendar reads happen entirely on-device.)

<!-- SCREENSHOT NEEDED: Recover from calendar screen with the lookback picker and a checked list of proposed trips -->

---

## Reports

The Reports tab is the tax-time view.

### Year selector

A horizontal row of year chips at the top. Tap any year to switch the view. Years auto-populate from your saved trips, plus the current year is always visible (so a fresh install has a year to pick).

### Yearly hero

Shows the year's total business miles, the IRS-rate-based deduction, and your bracket savings if Tax Bracket is set. Personal trips are excluded.

### Year stats

A 2×2 grid of summary tiles — **Total trips**, **Avg / trip**, **Longest trip**, **Busiest day** (most-frequent day of the week). When you have a mix of manual and auto-detected trips, a third row shows the count of each.

### Top destinations

The 5 addresses you drove to most often this year, ranked by visit count, with total miles per destination. Useful for noticing which clients or sites accounted for most of your driving.

### By business

One row per active business, showing miles and dollar deduction. Sorted by miles descending.

### By project

If any trip has a Project / Client tag, you'll see a "By project" section with the top 5 projects by miles.

### Monthly breakdown

Below the headline aggregates, every month with at least one trip gets its own MonthlyReportCard. Same layout as the Dashboard's monthly card but for the historical month.

<!-- SCREENSHOT NEEDED: Reports tab scrolled to show year hero, year stats grid, By business breakdown, and the start of monthly cards -->

### Export

The **Export** button at the bottom opens a menu with four formats:

- **PDF.** IRS Pub. 463-formatted trip log. Cover page with totals and per-vehicle odometer reconciliation, by-business breakdown, every trip on its own line. The recommended option for most users — and the only format that includes route-map thumbnails.
- **Excel (.xls).** Opens in Excel, Numbers, Google Sheets, or LibreOffice with formatting intact. Use this when your bookkeeper says "send me a spreadsheet."
- **CSV — Milely (full).** Every column Milely tracks: date, time, business, project / client, purpose, vehicle, miles, deduction. The most complete export.
- **CSV — QuickBooks Online.** Drop-in mileage importer. MM/DD/YYYY date format, no deduction column (QBO computes that itself based on its own mileage rate). Use this when you're importing straight into QBO.

Pick one, Milely builds the file, and the iOS share sheet opens so you can email it, AirDrop it, or save it to Files.

If a build fails (rare — usually a disk-space or temporary issue), you'll see a "Couldn't build the report" alert with a **Retry** button that re-runs the same format, plus an **Email support** button.

---

## Exports

Same four formats listed in [Reports](#reports). A few extras you should know:

- **Free tier** can export PDF and the standard Milely CSV. Excel and the QuickBooks Online CSV are subscriber-only.
- **PDF cover page** includes your business logo and brand color (subscriber feature — Settings → Branding) and per-vehicle odometer reconciliation (Jan 1 and Dec 31 readings if you've filled them in on each vehicle).
- **CSV files** are UTF-8 with a header row. They open in any spreadsheet app.
- **Excel files** are .xls (legacy format) for maximum compatibility. They open in Numbers, modern Excel, Google Sheets, and LibreOffice.

Greg's CPA notes ([from the website](/help/#exports)): the QuickBooks Online CSV intentionally omits the deduction column because QBO computes mileage deductions itself. If you import the Milely-full CSV into QBO, the deduction column will be ignored. Use the QBO preset to avoid the redundant column.

---

## Vehicles

Settings → **Vehicles** lists every vehicle you've added.

<!-- SCREENSHOT NEEDED: Settings → Vehicles list with two vehicles and the "Add from recently seen" section -->

### Adding a vehicle

Two paths.

**Direct add.** Tap the **+** in the top-right of the Vehicles list. The new-vehicle sheet opens with empty Name, Make, Model, and Odometer fields. Name is the only required field — make/model/odometer can be filled in later.

**Add from recently seen.** When Milely observes a CarPlay or car-Bluetooth audio route it doesn't recognize, it remembers the route's UID and friendly name in a list called "recently seen." Routes you haven't paired to a vehicle show up under **Add from recently seen** in the Vehicles list. Tap one and Milely opens a sheet that pre-fills the device name and pairing UID. You can either attach the route to an existing vehicle or create a new vehicle from it.

This second path is useful because iOS doesn't let apps enumerate paired Bluetooth devices directly. Milely can only see the routes that are *currently active* — but it can remember everything it's ever seen, which lets you pair a vehicle later when you're not actually in the car.

### Vehicle edit fields

Tap any vehicle to edit. Fields:

- **Name.** Free-text. "Truck", "Wife's Car", whatever you call it.
- **Make / Model.** Free-text.
- **Current odometer.** Optional.
- **Year-end odometer.** Three rows: current year, last year, year before. Enter the reading from December 31 of each year (which is the same as January 1 of the following year). Used by the PDF report's cover page for the IRS-required odometer reconciliation.
- **Set as default vehicle.** Toggle. The default vehicle is auto-selected on the Classify screen and on the manual entry form when no other match is found.
- **Auto-detect this vehicle.** Pairing controls — see below.
- **Auto-detect only with this CarPlay.** Restricts automatic detection to fire only when this vehicle's audio route is the connected one. Prevents Milely from firing on Uber rides or borrowed cars. Disabled until a CarPlay device is paired.
- **Pause recording when CarPlay disconnects.** When recording a manual trip in this vehicle, pause GPS when CarPlay disconnects (do work between drives, the trip resumes when you reconnect). Connecting to a *different* paired vehicle prompts you to stop or continue.
- **Stationary auto-end timeout.** Per-vehicle override of the global stationary auto-end timeout (Settings → Detection mode). Inherit, Never, or 15/30/60/120 minutes.
- **Delete.** Swipe left on the vehicle row in the list. Blocked if the vehicle is currently attached to a recording trip — end the trip first, then delete.

### Pairing a CarPlay or Bluetooth device

When you connect to a vehicle's audio route for the first time and Milely is in the foreground (or the app launches mid-drive via the CarPlay-trigger path), it offers to pair the route to a vehicle. You can also do this manually:

1. Open the vehicle's edit sheet.
2. Scroll to **Auto-detect this vehicle**.
3. If you're currently connected to the device, the live route's name shows up — tap to pair. Otherwise, use **Add from recently seen** at the Vehicles list level.

The pairing stores the device's UID (a stable internal identifier) and friendly name. Future connects on either match the vehicle silently. If iOS reports a different UID for the same vehicle (wireless vs wired CarPlay sometimes do this), the second pairing flow stamps the second UID onto the same vehicle so both wake the right vehicle without re-prompting.

### "Auto-detect armed" status

The vehicle edit sheet shows whether auto-detect is currently armed for this vehicle. Reads "Active" when iOS has the right permissions and the vehicle is listed in the auto-detect pool, "Limited" if you only have While-Using location, and "Off" otherwise.

### Custom display name for generic-named pairings

Some CarPlay devices report only the generic name "CarPlay" instead of the vehicle's real name. The vehicle edit sheet has a **Custom pairing display name** field where you can type "GMC", "F-150", or whatever you want to see in Milely. Purely cosmetic — pairing matching is still UID-first, so the custom name never affects detection.

### Personal pseudo-vehicle

There's no Personal vehicle option in the picker. Personal trips don't need vehicle attribution because they don't reach IRS reports — but you can still attach any vehicle to a Personal trip if you want the record.

---

## Businesses

Settings → **Businesses** lists every business you've created.

<!-- SCREENSHOT NEEDED: Settings → Businesses list with three businesses and the color picker visible on one -->

### Creating a business

Tap **+** in the top-right. The edit sheet has:

- **Name.** Required.
- **Color.** Tap a swatch from the palette. The color shows up as the avatar tile and chip color throughout the app — Dashboard rows, Logs pills, Reports rows.
- **Working days.** Optional. Tick the days of the week this business is active. Used by Smart Suggestions: a trip on a Sunday probably isn't your weekday-only consulting business.
- **Working hours.** Optional. Used by auto-classify rules to decide whether to apply the rule on a trip outside hours (e.g., a real-estate showing rule won't auto-fire if the trip lands at 11 PM on a Sunday).
- **Associated vehicles.** Optional. Tick the vehicles this business is usually driven in. If you drive Real Estate clients in your sedan and only haul Plumbing tools in the truck, ticking those associations gives Smart Suggestions much better defaults.

### Editing or archiving

Tap a business to edit. The bottom of the edit sheet has an **Archive** button — archived businesses don't show up in chips, dropdowns, or filters but their existing trips remain visible in Logs and Reports. Use this when a client engagement ends and you don't want it cluttering the picker, but you still need the records.

### Reordering

Drag the handles in the Businesses list to reorder. The order applies to chip rows and dropdowns throughout the app (and the Dashboard's Quick Start row, but Quick Start re-sorts by miles this month, so manual order only matters for businesses with the same miles).

---

## Settings reference

Top to bottom in the Settings tab.

### Subscription

The Subscribe row at the top opens [Subscription view](#subscription-and-free-tier). Shows ACTIVE / LIFETIME badge if you're subscribed.

### Trip Detection

#### Detection mode

Three sub-screens:

- **Manual / Automatic mode card.** Pick which one is the default for new trips.
- **CarPlay auto-start card.** Per-app explanation of how CarPlay-trigger works and the consent prompt flow.
- **Background recording status card.** Status (Active / Idle / Limited / Off), what it implies, and a "Request Always Allow" button if you're on While-Using. Always-Allow is required for the SLC wakeup that powers Automatic and CarPlay-trigger detection in the background.
- **Stationary auto-end card.** How long Milely will wait after you stop moving before auto-ending a recording trip. Slider: Never, 15 min, 30 min, 60 min, 120 min. Per-vehicle override available in vehicle settings.
- **Minimum logged trip distance.** Trips that end below this length are dropped silently. Default 0.5 mi. Stops driveway shuffles from cluttering Logs.
- **Quiet hours.** Time-of-day window during which auto-end notifications won't ping (so a trip ending at 2 AM doesn't wake you). The trip itself still ends — just no buzz.
- **Ignored routes.** A list of CarPlay/Bluetooth devices you've explicitly told Milely to ignore (e.g., a friend's car you ride in occasionally). Swipe to remove.
- **Connectivity diagnostic.** Live readout of the connectivity service's current state. Useful when troubleshooting "why didn't auto-start fire?"

#### Notifications

A single Picker for the **Weekly review reminder**:

- **Never.** No reminders.
- **Sunday 6 PM** (default), or any other weekday at 6 PM.

When the chosen day rolls around at 6 PM, if you have any unclassified trips waiting, Milely sends a notification. If the queue is empty, no buzz.

#### Personal Trips

A single toggle: **Keep personal trips**. Default ON. See [Personal trips](#personal-trips) for what changes when you turn it off.

### Setup

- **Businesses.** [See Businesses section.](#businesses)
- **Vehicles.** [See Vehicles section.](#vehicles)
- **Trip Templates.** Manage your saved Favorite trips. Templates appear on the Dashboard's Favorites Quick Start row. Add, rename, edit business attribution, attach addresses, mark as round-trip.
- **Recover from calendar.** [See above.](#recovering-trips-from-your-calendar)
- **Import from MileIQ / Everlance / TripLog.** Auto-detects the CSV format from the header row and maps each format's columns onto Milely's Trip model. Gives you a preview of what'll be imported before you commit.
- **Auto-classify rules.** A list of every rule you've created (typically from the "Always business" / "Always personal" buttons on a trip's detail screen). Swipe to delete a rule. The empty state explains how to create one.
- **Mileage Rate.** The IRS standard mileage rate, year by year. Milely seeds defaults for the current and recent years; you can edit any value if the IRS publishes a mid-year update.
- **Tax Bracket.** Your federal marginal tax bracket. Optional. When set, the Dashboard's monthly card and Reports' yearly hero show "≈ $X saved" — a rough estimate of the tax savings from your deduction. Off by default.
- **Data Retention.** Forever (default) or 3 years. With 3 years selected, trips older than 3 years are deleted on the next launch — but only after a confirmation alert tells you the count and oldest date. Locked trips and trips on the in-progress current year are never auto-deleted.

### Personalize

#### Theme

Pick from 8 color themes:

- **Warm** (free, default). Dark warm-brown with burnt-orange accents.
- **Light**. Daytime sibling of Warm. Toasted cream with burnt-orange accents.
- **Night.** Strict monochrome dark palette with crisp Azure-blue accent.
- **Day.** Pure-white cards on soft neutral grey, same Azure accent.
- **Slate.** Cool blue-gray with platinum highlights.
- **Sky.** Pale sky-blue throughout, navy text, amber pop on the savings figure.
- **Forest.** Deep forest greens with sage and wheat-gold accents.
- **Mint.** Soft mint as the brand voice with warm orange accents on white.

Warm is free for everyone. The other seven require an active subscription. The picker also has a "Match iOS Dark Mode" option — pick a dark theme and a light sibling, and Milely auto-switches based on your phone's system mode.

<!-- SCREENSHOT NEEDED: Settings → Theme picker showing all eight color theme swatches -->

#### Branding (subscriber)

Customize the look of exported PDFs:

- **Logo image.** Upload your business logo. Shows on the cover page of every PDF export.
- **Accent color.** Auto-detected from your logo by default (samples the most prominent color), or you can pick manually.
- **Footer text.** Free-text. Shows on every PDF page footer ("Smith Plumbing LLC · 555-1212 · smith@plumbing.com").

### Backup

#### Cloud Backup (subscriber)

Pick where to write automatic backups:

- **iCloud Drive.** Free with any Apple ID. Most users.
- **Google Drive / Dropbox / OneDrive.** Uses iOS's Files picker. The cloud app must be installed and authenticated; Milely just writes to a folder you choose.

Backups run on a schedule (typically once per day after a trip ends). Each backup is a JSON file containing all your trips, businesses, vehicles, settings, and receipts. Files are named with a timestamp so you can keep multiple versions.

To restore on a new iPhone: install Milely → open the backup file from Files → "Open in Milely". Milely shows a preview (count of trips, businesses, vehicles) and asks you to confirm before applying.

<!-- SCREENSHOT NEEDED: Backup screen showing Cloud Backup row with iCloud selected and last backup timestamp -->

#### Manual Export

Always free. Tap **Export Backup** to generate a JSON file and present the iOS share sheet. Email it to yourself, AirDrop it to another device, drop it in Files, etc.

### Trip Recording

Single toggle: **Save timestamps with trips**. Default ON. When OFF, trips save as date-only with no clock time or duration. Useful if you log all your trips manually after the fact and don't want time precision.

### Integrations

Single toggle: **Calendar suggestions**. Off by default. When ON, Milely reads upcoming events with locations from your calendar and surfaces them as one-tap trip starters on the Trip tab. Calendar data is processed only on your device.

### About

- **Version.** App version + build number.
- **What's New.** A short scrolling release-note view for the latest update.
- **Share Milely.** Sends a short message + the Milely.io link via iOS share sheet.
- **Privacy Policy.** Opens milely.io/privacy in Safari.
- **Terms of Service.** Opens milely.io/terms in Safari.
- **Help & FAQ.** Opens milely.io/help in Safari.
- **Contact Support.** Opens Mail with a pre-filled support template that includes your app version and iOS version.
- **Legal Disclaimer.** Inline read-only disclaimer about Milely not being tax advice.

---

## CarPlay and background recording

This section is for users who want fully hands-off recording — phone in your pocket, drive somewhere, classify later.

### What you need

- **Always-Allow location.** Settings → Detection mode shows whether you have it. The card has a "Request Always Allow" button; pairing a vehicle also prompts for the upgrade.
- **At least one paired vehicle** (for CarPlay-trigger), OR **Automatic detection mode** (for motion-detected start).
- **Don't force-quit Milely.** This one's important. See below.

### What "Auto-detect armed" means

The Vehicle edit sheet and the Detection mode screen both show whether background detection is currently armed. "Armed" means Milely has registered with iOS to receive the wake-up signal when significant location changes happen. It auto-arms whenever you grant Always-Allow location or open the app.

### The force-quit caveat

iOS has a rule: when a user manually force-quits an app from the iOS app switcher (swipe up to kill), the app no longer receives Significant Location Change updates until the user opens it again. This is iOS's design, not Milely's choice — it's documented in Apple's CoreLocation reference.

What this means: if you swipe Milely up to kill it, background recording stops working until you next open the app. Other ways the app might end (a crash, iOS evicting it for memory, your phone shutting down) do NOT trigger this rule — Milely will still wake on the next SLC event.

If you suspect background recording isn't working, the easiest test is: open Milely, go to Settings → Detection mode, and check the Background recording status card. If it says "Active", you're set. If it says "Off" or "Limited", follow the on-card instructions.

### CarPlay-trigger consent prompt

The first time you connect to a vehicle Milely has paired, you'll see a one-time prompt: "Auto-start trips when you connect to [vehicle]?" Tap **Yes, do that** to confirm. From then on, connections silently start trips. Tap **Not yet** if you'd rather not — Milely will ask again next connect.

This prompt exists because some users connect to CarPlay for non-driving reasons (sitting in a parked car listening to music). The consent step makes sure auto-start only fires when you've explicitly opted in.

### Cross-vehicle alert

If you start a trip in Vehicle A's CarPlay, then disconnect, then connect to Vehicle B's CarPlay while the original trip is still recording, Milely shows an alert asking whether to **Stop** the original trip (so you can start a new one in B) or **Continue** recording.

### Pause-on-disconnect

If a vehicle has the **Pause recording when CarPlay disconnects** flag set, manual trips in that vehicle pause GPS the moment CarPlay disconnects and resume when you reconnect. This is the "do work between drives" pattern: drive to job site A, disconnect to do paperwork, drive to job site B — Milely captures one trip with two segments, the paperwork time excluded from the duration.

If you're still actively driving when CarPlay disconnects (cable came loose, Bluetooth dropped), Milely waits 2 minutes before pausing. If you're still moving at that point, it abandons the pause and keeps recording. Real-world scenario: you don't lose the next 0.5 miles to a flaky cable.

---

## Trip recovery

If your phone crashes, runs out of battery, or you force-quit Milely while a trip is recording, you might worry that the trip is lost. It's not.

Every 30 seconds during recording, Milely snapshots the in-progress trip's route, distance, and time so far to a small file in App Group storage (UserDefaults, technically — but think of it as a recovery file). If something interrupts the app, the snapshot is still there.

The next time you open Milely within 7 days, you'll see a **Recover trip in progress?** prompt with three options:

- **Recover.** The trip resumes from the last snapshot. Recording re-starts where the kill happened, and the trip continues normally. Tap End when you arrive.
- **Discard.** The snapshot is deleted. The trip is gone for good.
- **Cancel** (or close the alert by tapping outside it). The prompt re-fires next time you open Milely.

After 7 days, the snapshot is dropped silently — too stale to be useful.

This recovery flow works for any path that left a trip mid-recording: app force-quit, iOS evicted the app for memory pressure, phone died mid-drive, OS update reboot, etc.

If recording was paused at the time of the kill (e.g., CarPlay disconnect pause), the trip resumes paused — tap End to finalize, or wait until the next CarPlay reconnect.

<!-- SCREENSHOT NEEDED: "Recover trip in progress?" alert with Recover / Discard / Cancel buttons -->

---

## Subscription and free tier

Milely is free to install and try. There's a 7-day free trial, then a single subscription with two billing options, plus a one-time lifetime purchase for users who'd rather not subscribe.

### What's free

- Unlimited installs and onboarding.
- Up to **25 trips per calendar month**, recorded any way you like.
- Full Dashboard, Logs, Reports, Trip detail, edit history, audit lock — none of these are gated.
- Manual export (JSON backup) any time.
- PDF export.
- CSV — Milely (full) export.
- One color theme: **Warm** (the original Milely look).
- All trip detection modes (Manual, Automatic, CarPlay-trigger).

When you hit the 25-trip cap, the next Start Trip tap shows: "You've used your 25 free trips this month. Subscribe for unlimited trips." Existing trips stay visible and editable — only NEW trips are blocked.

### What unlocks with a subscription

- **Unlimited trips.** No monthly cap.
- **Receipts.** Scan, attach, on-PDF inclusion. See [Receipts](#receipts).
- **7 additional color themes.** Light, Night, Day, Slate, Sky, Forest, Mint.
- **Branded PDFs.** Logo, accent color, footer text on every PDF page.
- **Excel exports.** .xls format that opens cleanly in Excel, Numbers, Sheets, LibreOffice.
- **QuickBooks Online CSV.** The drop-in QBO importer.
- **Automatic cloud backup.** iCloud Drive, Google Drive, Dropbox, OneDrive — Milely writes a backup on a schedule to a folder you control.
- **Priority support.** Front of the queue at milely@smileycreative.io.

### Pricing

- **Monthly:** $3.99/month, with a 7-day free trial.
- **Annual:** $29.99/year (saves about 37% vs monthly), with a 7-day free trial.
- **Lifetime:** $69.99 one-time. Unlocks everything forever, no recurring charge. Available behind Settings → Subscribe → Other options. Greg doesn't promote this option much because subscriptions fund ongoing development, but it's there for anyone who refuses subscriptions on principle.

### How to subscribe

Settings → **Subscribe**. Pick monthly, annual, or lifetime. iOS handles the actual purchase via StoreKit — Milely never sees your payment info. The 7-day trial activates immediately and converts to a paid sub on day 7 unless you cancel.

### How to cancel

Cancel any time in iOS's subscription management (Settings app → Apple ID → Subscriptions → Milely). Your subscription stays active through the end of the period you paid for.

If you bought lifetime, there's nothing to cancel — it's a one-time purchase. The Subscribe row in Milely shows "LIFETIME" and "You own Milely Lifetime."

### Restore Purchases

If you reinstall on a new device, tap Settings → Subscribe → **Restore Purchases** to re-attach your subscription via your Apple ID.

---

## Privacy and data

Milely is designed for users who don't want their movement, addresses, and tax records on someone else's server.

- **No backend, no account, no login.** Milely doesn't have servers. There's no Milely user account to create. There's nothing to log into.
- **All data is stored on your iPhone** in SwiftData (Apple's local database). Trips, addresses, receipts, businesses, vehicles, settings, edit history — all of it lives in app-private storage that other apps can't read.
- **Receipts strip EXIF metadata** before they're saved (no embedded location, timestamp, or device info from the photo). Receipts live in a per-trip folder that's deleted when you delete the trip.
- **Backups go where you choose.** When you set up cloud backup, Milely writes to a folder in *your* iCloud / Google Drive / Dropbox / OneDrive. Milely doesn't proxy it, doesn't index it, doesn't see what's in it. The cloud provider is between you and your data, not Milely.
- **Manual exports** (JSON backups, PDFs, CSVs) go through the iOS share sheet — they leave the device only when you actively send them somewhere.
- **Smart Suggestions** train a small CoreML model on your past classifications, on your phone, in the background. The model never leaves the device. There's no shared model.
- **Calendar reads** use iOS's EventKit API. Calendar data is processed in-memory on your phone and never transmitted.
- **Reverse geocoding** (turning GPS coordinates into addresses on the Classify screen) uses Apple's CLGeocoder, which is Apple-side. Apple's Location Services privacy policy applies to that lookup; Milely doesn't see Apple's request log.
- **No analytics, no telemetry, no crash reporting** beyond what Apple's standard TestFlight / App Store crash collection captures (which is anonymized by Apple). Milely doesn't ship a third-party analytics SDK.
- **No ads, ever.**
- **Subscription verification** uses StoreKit 2. Apple verifies your purchase; Milely just gets a yes/no entitlement.

For the full legal version of this, see [the Privacy Policy](/privacy/).

---

## Troubleshooting and FAQ

### CarPlay isn't auto-starting trips

Walk through these in order:

1. Settings → Detection mode → Background recording status card. Does it say "Active"? If not, follow the card's instructions (usually grant Always-Allow location).
2. Settings → Vehicles. Is the vehicle paired? If yes, tap into it and verify the "Auto-detect this vehicle" rows show a paired device.
3. Did you tap **Yes, do that** on the first-time consent prompt? If you tapped Not yet, the next CarPlay connect re-prompts. Connect again and tap Yes.
4. Did you force-quit Milely from the iOS app switcher? Background recording is disabled until you next open the app. Reopen Milely.
5. Some CarPlay devices report a generic "CarPlay" name and an unstable UID. Settings → Vehicles → vehicle edit → set a custom display name and re-pair via the "Add from recently seen" path so the latest UID is captured.

### A trip didn't auto-start

If you have Automatic mode on but a trip wasn't captured:

1. Was Always-Allow location granted? Settings → Detection mode → Background recording.
2. Was the app force-quit before the drive? Reopen and the next drive will trigger.
3. Was the drive very short (< 0.5 mi by default)? Sub-threshold trips are silently discarded by design. The threshold is in Settings → Detection mode → Minimum logged trip distance.
4. Was your phone in airplane mode or out of cell range? GPS still works without cell, but iOS's significant-location-change wake-up needs at least one location source — try granting precise location, not just approximate.

### The app didn't relaunch after force-quit

Force-quitting Milely from the iOS app switcher disables background recording until you next open the app. This is an iOS rule for any app that uses background location, not a Milely-specific behavior. Just open Milely; background recording re-arms automatically.

### My CarPlay is named "CarPlay" — that doesn't help

Some vehicles (older models, certain wireless adapters) report only the generic name "CarPlay" instead of the vehicle's actual name. Milely matches by UID first, so detection still works — but the friendly name in the app is unhelpful. Open Settings → Vehicles → tap the vehicle → set a **Custom pairing display name** ("F-150", "GMC", whatever). The custom name shows in chips, banners, and Logs.

### Milely uses too much battery

Manual mode only uses battery while a trip is recording (around 3% per hour, depending on phone and conditions). Automatic mode uses iOS's significant-location-changes API when idle (very low power), then ramps up GPS only when motion suggests driving.

If battery use is high without trips being recorded, check Settings → Detection mode → Background recording status — "Active" is correct; "Limited" or anything stuck-on may indicate stale state. Restart the app.

### A trip's miles look wrong

GPS captures sample points along the way, and Milely connects them into a route. Tunnels, parking garages, and dense urban canyons can make GPS jump or skip — sometimes the recorded distance is shorter than reality. To fix:

- Open the trip in Logs. The miles field is editable on unlocked trips.
- Use your odometer reading instead. Trip detail has a Start odometer / End odometer field — the difference is your authoritative miles.

### Smart Suggestions are wrong

The model trains on YOUR past classifications. If it's wrong, classify a few more trips correctly and the next prediction improves. Smart Suggestions never auto-apply — they're always one-tap chips you can ignore. If you don't see them at all, you probably don't have enough classified trips yet (the model needs a few examples per category).

### Restore a backup

iOS Files app → tap the milely-*.json backup file → Open in Milely. Milely shows a preview (count of trips, businesses, vehicles) and asks to confirm before applying. Restore is destructive — it overwrites the current data. Make a manual export first if you're unsure.

### Multi-device sync

Today, sync is manual: back up on Device A, restore on Device B. Real multi-device sync is on the roadmap but not shipped.

### Android version

iOS-only, and likely staying that way. Milely is a small project and iOS is what Greg knows.

### Mileage rate updates

The IRS sometimes updates the standard mileage rate mid-year. Settings → Mileage Rate lets you confirm or update what Milely uses for any year. Milely seeds defaults but you can always override.

---

## Glossary

**Audit Lock.** The state of a trip where every field is read-only, the trip can't be deleted (unless Personal), and the Personal flag can't be flipped. Triggered by the January 31 reminder banner, by manually tapping Lock on a trip, or by swiping right or left on a row in Logs. To make changes, tap Unlock for editing on the trip detail screen — every unlock and subsequent edit is captured in the trip's edit history.

**Auto-classify rule.** A user-defined rule that pre-fills the business and purpose for any future trip ending at a specific address. Created via the "Always business" or "Always personal" buttons on a trip's detail screen. Managed via Settings → Auto-classify rules. Working hours filter applies — a rule for a "Showings" business won't auto-fire at 11 PM on a Sunday.

**CarPlay-trigger.** Auto-starting a trip when your phone connects to a paired vehicle's CarPlay or car-Bluetooth audio route. The most accurate detection signal Milely has — UID-matched and almost never wrong.

**Detection mode.** Manual (you tap Start) or Automatic (motion + significant location changes start a trip on their own). Set in Settings → Detection mode.

**Edit history.** The append-only record of every field-level change on a trip — old value, new value, timestamp. Always on. Captures locks, unlocks, Personal toggles, receipt adds and removes. Can't be wiped from inside the app (deleting the trip removes the history with it).

**Generic-name pairing.** A CarPlay or Bluetooth route that reports only "CarPlay" as its friendly name. Milely matches by UID instead, so detection still works — set a custom display name in vehicle settings to make the in-app label useful.

**Manual recording continues across disconnects.** A per-vehicle setting. When OFF (default), GPS keeps running on a manual trip even if CarPlay disconnects. When ON, manual trips pause on disconnect and resume on reconnect.

**Pending classify.** The state where a trip has just ended but you haven't tapped Save on the Classify screen yet. The trip is already saved to Logs as Unclassified — Save just adds the business + purpose. Skip for now leaves the trip Unclassified for later.

**Personal trip.** A drive with no business attached, no required purpose, and zero deduction contribution. Marked with a green pill in lists. Excluded from every Reports figure. Optional first-class concept (Settings → Personal Trips → Keep personal trips).

**Project / Client tag.** A free-text tag on each trip — type a listing address, matter name, job number, or whatever your industry uses. Surfaces as a column in CSV exports and as a "By project" breakdown in Reports.

**SeenAudioRoute.** Internal — a CarPlay or Bluetooth audio route Milely has observed at any point but you haven't yet paired to a vehicle. Shown in Settings → Vehicles under "Add from recently seen" so you can pair without being currently in the car.

**SLC (Significant Location Change).** An iOS API that wakes the app when the phone has moved a meaningful distance. Powers Automatic detection mode and CarPlay-trigger background wakeups. Requires Always-Allow location. Does NOT work after a user-initiated force-quit (iOS rule).

**Smart Suggestions.** On-device CoreML predictions of the right business and purpose for a just-ended trip, based on your past classifications. Show as one-tap chips above the business row on the Classify screen.

**Stationary auto-end.** The timeout after which a recording trip ends automatically if you've been stopped and CarPlay is disconnected. Configured globally in Settings → Detection mode → Stationary auto-end and per-vehicle in vehicle settings.

**Trip Template (Favorite).** A saved trip you can re-launch with one tap. Created via the star button on any trip detail screen. Surfaces on the Dashboard's Favorites Quick Start row. Managed in Settings → Trip Templates.

**UID (Unique Identifier).** An iOS-internal opaque string that identifies a specific CarPlay or Bluetooth device. Stable across connections (mostly). Milely uses UIDs as the primary match for vehicle pairing because they're more reliable than friendly names.

**Unclassified.** A trip that's been recorded and saved but doesn't have a business attached yet. Lands here when you tap Skip for now on the Classify screen, or when an auto-detected trip ends and you don't open the notification. Show in Logs with a tap-to-classify chip on the row. The weekly review reminder counts these.

**Working days mask / Working hours.** Optional per-business settings that tell Smart Suggestions and auto-classify rules when this business is active. A weekday-only consulting business won't auto-classify a Saturday trip; an after-hours rule won't apply to a Sunday morning drive.

---

## Need more help?

- **Quick how-to guides** for the most common tasks: [/help/](/help/)
- **Email support**: milely@smileycreative.io
- **Privacy details**: [/privacy/](/privacy/)
- **Terms of service**: [/terms/](/terms/)

---

## Screenshot manifest

The following screenshots are referenced in this guide as `<!-- SCREENSHOT NEEDED -->` placeholders. Use this list to direct a screenshot session.

1. **Legal consent screen** — first-launch welcome with both checkboxes filled and the Continue button enabled.
2. **Onboarding business-name step** — text field showing example "Greg's Real Estate".
3. **Onboarding vehicle step** — vehicle name field with both Skip and Add Vehicle buttons visible.
4. **Full Dashboard** — monthly card on top, Quick Start row including a business row + Personal + Repeat Last + Favorites, Start Trip button at bottom.
5. **Audit-lock banner** — yellow banner on the Dashboard with Lock [year] and Not now buttons.
6. **Live trip banner** — recording state showing distance, time, deduction, with the End pill on the right.
7. **Quick Start row** — business row, green P Personal row, Repeat Last, Favorites stacked.
8. **Live map (Trip tab)** — route polyline drawn, stats card overlay, End Trip button at the bottom.
9. **Settings → Detection mode** — Automatic card selected, Background recording status card showing "Active".
10. **First-time CarPlay consent prompt** — "Auto-start trips when you connect to [vehicle]?" with Yes do that and Not yet buttons.
11. **Log Past Trip Manually form** — date picker, From/To address fields, miles field, business chips, purpose field.
12. **Classify Trip screen (full)** — route map at top, business chips, purpose field, Save Trip button at bottom.
13. **Trip detail with receipts** — Receipts row showing two attached thumbnails plus Scan / Add from photos buttons.
14. **Trip detail (full)** — route map, all sections visible, star button in the top-right corner.
15. **Logs tab header** — search field, Year/Month/Business/Personal filter pills, list of trips below.
16. **Recover from calendar** — lookback window picker and a checked list of proposed trips.
17. **Reports tab** — scrolled to show year hero, year stats grid, By business breakdown, start of monthly cards.
18. **Settings → Vehicles** — list with two vehicles and the "Add from recently seen" section visible.
19. **Settings → Businesses** — list with three businesses, color picker open on one.
20. **Settings → Theme picker** — all eight color theme swatches visible.
21. **Backup screen** — Cloud Backup row with iCloud selected and last backup timestamp.
22. **Recover trip in progress alert** — "Recover trip in progress?" with Recover / Discard / Cancel buttons.

</main>