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
17. [Subscription and trial](#subscription-and-trial)
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

<!-- SCREENSHOT NEEDED: full Dashboard with monthly card, Quick Start rows (Personal sits inline as a sibling business row when enabled) + Repeat Last + Favorites, and the Start Trip button -->

### Audit Lock reminder banner (January 31 each year)

Once a year, on or after January 31, you'll see a yellow banner at the top of the Dashboard asking whether to lock last year's trips. Tapping **Lock [year]** locks every unlocked business trip from the prior year so it can't be edited or deleted later — that's the audit-defense guarantee. Tapping **Not now** dismisses the banner for the rest of the calendar year. The banner reappears the following January if there are still unlocked prior-year trips.

Locking is irreversible per trip. The confirmation alert will ask you again before applying it.

<!-- SCREENSHOT NEEDED: the yellow audit-lock banner on the Dashboard with Lock and Not now buttons -->

### Live trip banner (only while recording)

When a trip is recording, the very top of the Dashboard shows a live banner with a red blinking dot, "Recording trip", the live distance, time elapsed, and dollar deduction tallying up in real time. There's an **End** pill on the right of the banner — tap it to stop the trip. Tapping the banner itself opens a small editor where you can change the trip's business, purpose, or vehicle without ending it.

If a trip is paused (because the CarPlay you started in just disconnected), the dot turns yellow and shows a pause glyph, and the eyebrow text reads "Paused" instead of "Recording trip".

<!-- SCREENSHOT NEEDED: live trip banner showing distance, time, deduction, with the End pill on the right -->

### First-launch empty state

If you haven't recorded any trips yet, you'll see a small "No trips yet" card explaining what Start Trip will do. This card disappears the moment you save your first trip.

**Quick Start always renders** as long as you have at least one Business set up — even on day one before you've logged a trip. Tap any Quick Start row to start a pre-tagged trip immediately.

### Monthly Report Card

Once you have trips, the Dashboard shows a card for the current month with:

- **Hero deduction figure.** The dollar value of this month's business mileage, large.
- **Bracket savings.** If you've set your federal tax bracket in Settings → Tax Bracket, you'll see "≈ $X saved" — a rough estimate of how much that deduction reduces your tax bill.
- **Mileage rate.** Shows the cents-per-mile rate Milely is using for the calculation (the IRS standard, e.g. 70 cents/mi).
- **Donut chart.** Visual breakdown of miles by business this month. Tap the legend to see each business's miles and trip count.

Personal trips are excluded from every figure on this card.

### Quick Start row

Below the monthly card, "Quick Start" surfaces shortcuts for the most-used actions:

- **Top businesses (up to 3).** One row per business, sorted by miles this month. Each shows the business's color initials, the trip count, and total miles. Tap to start a trip pre-tagged for that business. Personal is treated as a built-in business in this list — it surfaces with the same Quick Start row layout as any other business. Tap it to start a Personal trip. The Personal row only appears if "Keep personal trips" is on in Settings (default ON). Personal trips are still excluded from your deduction; the row just lives alongside your real businesses instead of in its own slot.
- **Repeat Last.** Yellow refresh tile. Starts a new trip pre-filled with the same business and purpose as your most recent trip.
- **Favorites.** Yellow star tile. Opens a picker of your saved trip templates. Tap any template to start a trip from it.

<!-- SCREENSHOT NEEDED: Quick Start row with one or two business rows (including Personal as a sibling row), Repeat Last, and Favorites -->

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

### Automatic mode (motion + GPS state machine)

In Automatic mode, Milely watches for driving even when you haven't tapped Start. Switch to it in Settings → Trip Settings → **Automatic**.

How it works (in plain terms): Milely runs a three-stage state machine.

1. **IDLE.** No trip recording. Only iOS's *significant location change* API is listening — that's a low-power signal iOS sends apps when the phone has moved a meaningful distance, typically a few hundred meters. Negligible battery drain.
2. **ARMED.** The moment iOS's motion classifier reports automotive activity AND you're *not* connected to a paired vehicle's CarPlay, Milely flips to ARMED. Full GPS turns on so distance can accumulate, but no trip is recorded yet. The state machine confirms on a low bar — about 5 seconds of sustained motion at walking-plus speed (~2 mph) and ~50 meters traveled. Aggressive on purpose: a missed real drive costs more in lost deductions than an occasional false positive, and you can swipe-left in Logs to Exclude any rides that weren't yours.
3. **RECORDING.** Once thresholds are met, the trip starts. **Paired-vehicle fast-path:** if your phone is connected to a paired vehicle's CarPlay or car-Bluetooth audio route at the moment motion confirms automotive activity, Milely skips ARMED entirely and goes straight to RECORDING — UID match is ground truth, no need to gate on motion thresholds.

Recording continues until you've been stopped long enough (the **End Trip After Sitting Still** timeout in Settings → Trip Settings → Universal) and CarPlay isn't connected. Then the trip ends automatically and iOS sends you a notification — "Trip ended, tap to classify." Whether you tap or not, the trip is saved (it lands in Logs marked **Unclassified** until you classify it).

**Lost-miles recovery:** when a trip promotes to RECORDING, Milely walks back through a 10-minute rolling location buffer to find when you actually started driving and rewrites the trip's start time and route to match. This recovers the typical 1–3 minutes of latency between "you started driving" and "the motion classifier confirmed it" — miles that other trackers simply lose.

Automatic mode requires:

- **Always-Allow location.** "While Using" isn't enough — iOS won't wake the app for SLC events on While-Using. Settings → Trip Settings shows a Background Recording status card that tells you whether you're set up correctly.
- **Motion & Fitness permission.** Used to filter out walking/biking from real driving.

<!-- SCREENSHOT NEEDED: Settings → Trip Settings → Automatic card selected, with the Background recording status card showing "Active" -->

### CarPlay-trigger (the most accurate option)

If you've paired a vehicle in Milely (Settings → Vehicles → see the [Vehicles section](#vehicles)) and the **Auto-Start Trip on CarPlay Connect** toggle is on under **Settings → Trip Settings**, connecting your phone to that vehicle's CarPlay or car-Bluetooth audio route triggers a trip start automatically.

How it works in plain terms:

- iOS notices an audio route connected (CarPlay or your car's hands-free Bluetooth).
- Milely matches the connected device's identifier to a paired vehicle in your records.
- A trip starts immediately — no waiting on the motion classifier. Pairing a vehicle counts as consent: when you save a vehicle with a paired CarPlay route, the auto-start toggle defaults to ON, so future connects silently start trips.
- When you disconnect (engine off + phone leaves the car), the trip pauses or ends depending on your **Pause/Resume Based on CarPlay** toggle.

This is the most accurate detection signal Milely has — UID-matching CarPlay or Bluetooth is essentially never wrong, where motion-detected can occasionally fire on a passenger ride or miss a slow start. If you have CarPlay or Bluetooth in your vehicle, this is the recommended setup.

### How the modes interact

The mode (Manual or Automatic) and the **Auto-Start Trip on CarPlay Connect** toggle are independent — both live inside Settings → Trip Settings, but neither is a sub-setting of the other. Either can be on or off without affecting the other. That gives you four useful combinations:

| Mode | CarPlay auto-start | What you get |
|---|---|---|
| **Automatic** | **ON** (default) | Trip auto-starts the instant you connect to a paired vehicle (no motion check — CarPlay alone is enough). If you're driving something Milely doesn't recognize (Uber, borrowed car), motion-based detection still catches the drive — every drive auto-records by default. Swipe-left in Logs to Exclude rides that weren't yours. |
| **Automatic** | **OFF** | Motion-only. Trips auto-start once motion confirms automotive activity (~5 seconds). Works without any vehicle pairing. |
| **Manual** | **ON** | CarPlay-trigger still fires for paired vehicles. Motion is ignored. Useful if you want manual control everywhere except your work truck — connect to the truck and a trip starts automatically; everywhere else you tap Start. |
| **Manual** | **OFF** | Pure manual. Nothing auto-starts; you tap Start, drive, tap End. |

Both auto-start paths check whether a trip is already recording before starting one — they won't double-start. If both paths could fire (you connect to CarPlay AND the motion classifier sees driving), CarPlay almost always wins because it's instant; motion takes longer to confirm automotive activity.

**Require Paired Vehicle (opt-in restrictive mode).** If your business driving is in one specific paired vehicle and you'd rather not record anything else, flip the **Require Paired Vehicle** toggle in Settings → Trip Settings → Automatic. With it on, Milely only auto-records when motion confirms automotive activity AND a paired vehicle is the live audio route — both conditions, not either. The CarPlay-trigger path is suppressed in this mode (the motion path handles the AND combination via its arming gate). Default is OFF (aggressive) because most users net out ahead by capturing every business mile and excluding the rare passenger ride after the fact.

**Mid-trip CarPlay attribution.** If a motion-only trip is already recording and your phone later connects to a paired vehicle — say, you walked to the corner, then got into your truck — Milely picks up the CarPlay attribution mid-trip. Disconnecting later (engine off, phone leaves the car) still triggers pause-on-disconnect, the same as a trip that started on CarPlay.

<!-- SCREENSHOT NEEDED: Settings → Trip Settings showing the mode tiles and the CarPlay auto-start toggle in their cards -->

### What happens during recording

While a trip is recording, regardless of how it started:

- The **Trip tab** shows a live map with your route drawing as a polyline. Pinch-zoom and pan like Apple Maps.
- A stats card on the map shows live **Distance**, **Time**, and **Deduction** updating every second.
- The **Dashboard** shows the live banner described earlier.
- The **Logs** tab adds an "End trip" pill to its header so you can stop without changing tabs.
- iOS keeps Milely running cleanly even with the screen locked or another app in the foreground.
- Every 30 seconds, Milely snapshots your in-progress trip to disk, in case the app is force-quit, runs out of memory, or your phone dies. See [Trip recovery](#trip-recovery).
- **Background notifications fire even with your phone in your pocket.** Milely keeps a quiet audio session alive so the OS doesn't suspend the app while a trip is recording — the "Trip ended — tap to classify" notification reliably reaches you whether the screen is on, off, or buried under another app.

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
- **Business chips.** One per business you've created. Tap to select. When "Keep personal trips" is on, a **Personal** chip sits in the same row as your real businesses — tapping it clears any business attached and hides the purpose field, since Personal trips don't need one. Personal lives in the same chip row rather than a separate slot.
- **Calendar suggestions.** If the trip overlapped any calendar events with locations, those titles surface as one-tap chips you can use as the purpose.
- **Recent purpose chips.** Up to 6 most-recent purposes for the chosen business. Tap one to fill the purpose field instantly.
- **Purpose field.** Free-text. Required for business trips. Specific is better than generic — "Showing 1428 Maple St" reads better in an audit than "Real Estate."
- **Vehicle chips.** Pick which vehicle you drove. Auto-fills from your CarPlay/Bluetooth pairing if matched, otherwise from your default vehicle.
- **I was driving toggle.** Default ON. Turn off if you were a passenger (Uber, ride-along, carpool). Off marks the trip Personal so it doesn't count toward your deduction.
- **Round trip toggle.** Default OFF. Turn on if you'll drive the same route back — Milely doubles the miles and saves it as one record.
- **Receipts row.** Subscriber feature. See [Receipts](#receipts).
- **Ready to save** summary. The final values that will be saved if you hit Save Trip.
- **Save Trip** button. Shows the deduction amount when you tap it (e.g. "Save Trip · $12.40"), unless the trip is Personal — Personal saves just say "Save Trip." Saving auto-locks the trip — there's no separate manual lock action anymore. To edit a saved trip, open it from Logs and tap **Unlock for editing** in the trip detail view.
- **Skip for now** button. The trip lands in Logs auto-locked and Included in the annual report, with no business attached. You can assign a business later by opening it in Logs, tapping **Unlock for editing**, and picking a business.

<!-- SCREENSHOT NEEDED: Classify Trip screen scrolled to show route map, business chips, purpose field, and the Save Trip button -->

### What "Skip for now" actually does

This used to be called "Cancel" and people read it as "throw the trip away." It does NOT throw the trip away. The trip is already saved to Logs the moment recording ends — auto-locked and Included in your annual report by default, just with no business attached. Open it from Logs, tap **Unlock for editing**, fill in the business, save.

This means: even if you crash, kill the app, or never tap Save, your recorded miles are not lost. They're sitting in Logs waiting for you.

### Smart Suggestions (on-device pattern matching)

If you've classified a few trips already, the Classify screen may show "SMART SUGGESTIONS" with chips like "Real Estate · 92%" or "Personal · 88%." Tap a chip to apply that business and purpose to the current trip.

How it learns: from your saved classifications, on your phone. After each save, Milely re-trains a small machine-learning model in the background using Apple's CoreML framework. The model never leaves your device. There's no Milely server, no shared model, no analytics pipeline. Uninstall the app and the model goes with it.

If you have an auto-classify rule that already matched the trip, the Smart Suggestions chips render dimmed and informational — they show what the model thought, but tapping them does nothing because the rule has already chosen for you.

---

## Personal trips (excluded from annual report)

Personal trips are drives you don't want in your annual deduction report — grocery runs, weekend errands, kid pickup. Milely treats Personal as a built-in Business in the picker (rather than a separate category) and as an Exclude flag on each trip.

Two effects:

- **Built-in Personal business in the chip picker.** When "Keep personal trips" is on (default), a Personal entry appears alongside your real businesses on the Classify screen, in the live trip editor, and in the Logs Business filter dropdown. Picking it classifies the trip as Personal AND sets it Excluded.
- **Excluded flag on each trip.** Every trip in Logs is either Included (orange checkmark pill) or Excluded (gray minus pill). Excluded trips don't show up in Reports, exports, or the Dashboard's deduction tallies.

### How to mark a trip Personal / Excluded

- **At Save time.** Pick the **Personal** chip in the business chip row on the Classify screen.
- **From Logs (any saved trip).** Swipe LEFT on the row to Exclude — Include/Exclude works on locked or unlocked trips alike.
- **From the trip detail view.** Open the trip from Logs, scroll to the bottom, and tap **Mark as personal**. (If the trip is locked, tap **Unlock for editing** first.)
- **Mid-trip.** Tap the live banner on the Dashboard and pick **Personal** from the business dropdown.
- **From the Dashboard.** Tap the Personal Quick Start row to start a new trip pre-tagged Personal.

### How to undo / re-include

Swipe RIGHT on the row in Logs (Include action), or open the trip detail view and tap **Mark as business**.

### What happens if you turn "Keep personal trips" off

If you set Settings → Personal Trips → Keep personal trips to OFF:

- The Personal chip disappears from the Classify screen and the live trip editor.
- The Personal entry disappears from the Dashboard's Quick Start row and the Logs Business filter dropdown.
- Existing Personal (Excluded) trips stay in Logs (they're never silently deleted).
- When you next open the Reports tab on a year that has unlocked Personal trips, Milely asks: "Delete N Personal trips from [year]?" Tap Delete to remove them, or Keep to leave them. Either way, you're prompted only once per year.
- Locked Personal trips are NEVER deleted, regardless of your answer.

This gives you two clean modes: Personal as a first-class option in the picker, or Personal as a passing label that gets cleaned up at year-end.

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
- **Unlock for editing button.** Trips lock automatically on Save — to edit a saved trip, tap **Unlock for editing** here. Re-locking happens automatically the next time you save changes.
- **Mark as business / Mark as personal button.** Only on unlocked trips. Flips the Personal flag, which also flips the trip's Included/Excluded state.
- **Delete Trip button.** At the bottom, in destructive red. Asks for confirmation. Locked business trips can't be deleted — unlock first. Locked Personal trips can be deleted (they don't reach IRS reports anyway).

### The star button

In the top-right toolbar of any trip detail screen there's a **star** icon. Tap it to save this trip as a Favorite (a Trip Template). The favorite shows up on the Dashboard's Favorites Quick Start row for one-tap re-launching of similar drives.

<!-- SCREENSHOT NEEDED: Trip detail screen with route map, all sections visible, star button in the top-right -->

### Audit Lock and auto-lock-on-save

Every trip auto-locks the moment you tap Save (or Skip for now) on the Classify screen. There is no separate manual Lock action — saving locks. The trip's content is now frozen for audit; every editable field is read-only.

On a locked trip:

- Every editable field is read-only.
- Receipts can't be added or removed.
- The trip can't be deleted (unless it's Personal).
- The Personal flag can't be flipped.

**To edit a locked trip:** open Trip detail and tap **Unlock for editing** at the bottom. Every unlock and subsequent change is captured in the trip's edit history.

**Re-locking** happens automatically the next time you Save changes. Save and Unlock are the only two actions.

Once a year, on or after January 31, a yellow audit-lock banner appears on the Dashboard asking whether to lock every prior-year trip in one shot. The yearly banner is for catching trips that slipped through (auto-lock disabled, user unlocked something and forgot to re-save). Locking the prior year is irreversible per trip.

### Edit history (the audit-defense backbone)

Every saved trip has an always-on edit history — open Trip detail and scroll to the **Edit history** section at the bottom. Every field-level change is recorded with timestamp and before/after values: locks, unlocks, Personal toggling, business reassignment, miles edits, address edits, receipt adds and removes.

This is what tells an auditor (or a CPA, or future-you) what really happened. Combined with auto-lock-on-save, it gives the audit-defense guarantee the old per-row lock icon hinted at, with less visual clutter on every Logs row. Edit history can't be wiped from inside the app (deleting the trip removes the history with it).

---

## Logs (your trip list)

The Logs tab is your full trip history.

### The header

A frozen header pinned at the top has:

- **Logs** title and the **Select** button (toggles bulk-select mode).
- An **End trip** pill (only when a trip is recording — quick stop without changing tabs).
- A search field that filters across purpose, From address, To address, and business name.
- A row of three filter pills: **Year**, **Month**, **Business**. Year and Month default to the current year + month. The Business pill opens a dropdown that includes "All", each of your active businesses, and a "Personal" entry (when "Keep personal trips" is on).

<!-- SCREENSHOT NEEDED: Logs tab header showing the search field, Year/Month/Business filter pills, and a list of trips below -->

### The trip list

Trips are grouped by date with smart labels — **Today**, **Yesterday**, **This week**, **This month**, then "April 2026" / "March 2026" / etc. Each trip row shows the route (or purpose), distance, business chip if assigned, time, and the trip's annual-report state — either an orange **Included** check or a gray **Excluded** minus on the trailing edge.

Tap a row to open Trip detail.

### Included vs Excluded — the two-state model

Every trip in Logs has one of two annual-report states:

- **Included** (orange checkmark pill) — counts toward your annual deduction. Default for every new trip.
- **Excluded** (gray minus pill) — set aside. Still in Logs (searchable, filterable), but filtered out of every Reports figure, every export, and the Dashboard's deduction tallies.

Included/Excluded is **independent** of which business is attached. A trip can be Excluded with the "Real Estate" business attached, or Included with no business attached.

Swipe right to Include; swipe left to Exclude. Locked or unlocked, the swipes work either way — categorization (Include/Exclude) is separate from edit-locking (frozen for audit).

### Swipe actions

Every trip in Logs is either **Included** in your annual report (orange checkmark pill, default) or **Excluded** (gray minus pill).

- **Swipe right** on a row → **Include**. Flips the trip back to Included if it was Excluded; preserves whatever business is attached.
- **Swipe left** on a row → **Exclude**. Marks the trip as Personal/Excluded; preserves whatever business is attached.

Both swipes work on locked trips — Include/Exclude is a categorization choice, separate from edit-locking. The two are independent: a trip can be Included with no business assigned, or Excluded with a business attached.

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

- **Every export format** — PDF, CSV (Milely + QuickBooks Online), Excel, JSON — works during the trial and stays available forever for trips you've already recorded. The only subscription-gated action is recording **new** trips.
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
- **Set as Default Vehicle.** Toggle. The default vehicle is auto-selected on the Classify screen and on the manual entry form when no other match is found.
- **Vehicle Pairing.** A status card showing whether this vehicle's CarPlay/Bluetooth route is currently live. See below.
- **End Trip After Stationary** *(per-vehicle override).* Inherits the value from Trip Settings → Universal by default ("Use default"), or pick a custom timeout for this vehicle (Never, or 15 / 30 / 60 / 120 minutes). Useful for splitting behavior between, say, a work truck that sits all day at a job site and a sedan that gives up faster.
- **Stats & Patterns.** Read-only stats: trips logged, total miles, average trip, most common start time, recent driveway-shuffle starts (false-start count for the dampening signal).
- **Delete.** Swipe left on the vehicle row in the list. Blocked if the vehicle is currently attached to a recording trip — end the trip first, then delete.

### Vehicle Pairing card

The vehicle edit sheet has a **Vehicle Pairing** section that shows the current connection state:

- **Paired and connected** *(green checkmark).* Your phone is currently on this vehicle's audio route. The subtitle reads "CarPlay" or "Bluetooth" + your vehicle's Name (e.g., **CarPlayTruck**, **BluetoothSedan**) — concatenated with no separator.
- **Saved pairing.** Below the live state, a row showing what's stored. Tap **Unpair** to forget the pairing.
- **Tap to pair this vehicle.** Appears when you're connected to a route Milely doesn't recognize yet — one tap pairs it.
- **Different vehicle connected.** Appears when you're on a paired route that belongs to a different vehicle in your list. Lets you switch the trip vehicle if needed.
- **Pairing broken.** Appears when the saved pairing's UID can't match the live route — usually means iOS swapped UIDs (wireless ↔ wired). Re-pair to refresh.

In the default (aggressive) configuration, motion-based detection arms on any drive — paired vehicle or not — so passenger rides in someone else's car *do* record by default. The expectation is you swipe-left in Logs to Exclude any rides that weren't yours. To restrict motion-based detection to only fire when one of your paired vehicles is the live audio route, flip the **Require Paired Vehicle** toggle in Settings → Trip Settings → Automatic.

### Pairing a CarPlay or Bluetooth device

When you connect to a vehicle's audio route for the first time and Milely is in the foreground (or the app launches mid-drive via the auto-start path), it offers to pair the route to a vehicle. You can also do this manually:

1. Open the vehicle's edit sheet.
2. Scroll to **Vehicle Pairing**.
3. If you're currently connected to the device, the live route's name shows up — tap **Tap to pair this vehicle**. Otherwise, use **Add from Recently Seen** at the Vehicles list level.

The pairing stores the device's UID (a stable internal identifier) and friendly name. Future connects match the vehicle silently. If iOS reports a different UID for the same vehicle (wireless vs wired CarPlay sometimes do this), the next pairing flow stamps the second UID onto the same vehicle so both wake the right vehicle without re-prompting.

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

### The built-in Personal business

Milely auto-creates a single **Personal** business sentinel that surfaces alongside your real businesses in chips, dropdowns, and filters. You can hide it via **Settings → Personal Trips → Keep personal trips**, but you can't delete or rename it.

### Reordering

Drag the handles in the Businesses list to reorder. The order applies to chip rows and dropdowns throughout the app (and the Dashboard's Quick Start row, but Quick Start re-sorts by miles this month, so manual order only matters for businesses with the same miles).

---

## Settings reference

Top to bottom in the Settings tab.

### Subscription

The Subscribe row at the top opens [Subscription view](#subscription-and-trial). Shows ACTIVE / LIFETIME badge if you're subscribed, or your trial countdown if you're in the 7-day window.

### Trip Settings

A single row that opens the Trip Settings page. Inside, the page is split into mode tiles plus a Universal section.

#### Mode tiles (top of the page)

Two tiles side by side: **Manual** and **Automatic**. The active one shows a checkmark + "Active" label; the other shows "Inactive". Tap either to switch.

#### Manual Detection (sub-section, only when Manual is active)

- **Pause/Resume Based on CarPlay.** A single toggle with dynamic copy describing both states. ON: when you disconnect CarPlay mid-trip the recording pauses; reconnecting resumes it. OFF: the recording keeps running at full GPS until you tap End. Independently configurable from the Automatic mode's version of this toggle.

#### Automatic Detection (sub-section, only when Automatic is active)

- **Auto-Start Trip on CarPlay Connect.** ON: connecting to a paired vehicle starts a trip immediately, no waiting on the motion classifier. New paired vehicles enable this automatically (pairing IS consent). OFF: motion-only auto-detect.
- **Pause/Resume Based on CarPlay.** Same toggle as in Manual mode but tracked separately, so you can have one mode pause and the other not.
- **Background Recording.** A status card showing Active / Idle / Limited / Off, with a "Request Always Allow" button if you don't have the location permission auto-detect needs. Always-Allow is required for iOS to wake Milely on a significant location change.
- **Minimum Trip Distance.** Trips that auto-end below this length are dropped silently — keeps the log free of driveway shuffles and GPS jitter. Pick from Log Every Trip / 0.05 / 0.1 / 0.25 / 0.5 / 1.0 mi. Default 0.05 mi. Manual trips ignore this — pure user control, no silent drops.

#### Universal (sub-section, applies to both modes)

- **Save Trip Timestamps.** Default ON. When OFF, trips save as date-only with no clock time or duration. Useful if you log all your trips manually after the fact and don't want time precision.
- **Keep Personal Trips.** Default ON. See [Personal trips](#personal-trips) for what changes when you turn it off.
- **End Trip After Sitting Still.** Slider 0–8 hours in 15-minute steps, plus an "Or End at This Hour if Still Stationary" toggle (default 3 AM) that ends a forgotten parked trip overnight. Per-vehicle override available in vehicle settings ("Use default" inherits this value).
- **Ignored Routes.** A list of CarPlay/Bluetooth devices you've explicitly told Milely to ignore (e.g., a friend's car you ride in occasionally). Swipe to remove.
- **Connectivity Diagnostic.** Live readout of the connectivity service's current state. Useful when troubleshooting "why didn't auto-start fire?"

### Notifications

- **Weekly Review Reminder.** Single Picker: **Never** / **Sunday 6 PM** (default) / **Monday 6 PM** / etc. When the chosen day rolls around at 6 PM, if you have any unclassified trips waiting, Milely sends a notification. Empty queue, no buzz.
- **Quiet Hours.** Start and end hour pickers. Auto-end notifications won't ping during this window — the trip itself still ends, you just don't get woken at 2 AM.

### Setup

- **Businesses.** [See Businesses section.](#businesses)
- **Vehicles.** [See Vehicles section.](#vehicles)
- **Trip Templates.** Manage your saved Favorite trips. Templates appear on the Dashboard's Favorites Quick Start row. Add, rename, edit business attribution, attach addresses, mark as round-trip.
- **Auto-Classify Rules.** A list of every rule you've created (typically from the "Always business" / "Always personal" buttons on a trip's detail screen). Swipe to delete a rule. The empty state explains how to create one.
- **Mileage Rate.** The IRS standard mileage rate, year by year. Milely seeds defaults for the current and recent years; you can edit any value if the IRS publishes a mid-year update.
- **Tax Bracket.** Your federal marginal tax bracket. Optional. When set, the Dashboard's monthly card and Reports' yearly hero show "≈ $X saved" — a rough estimate of the tax savings from your deduction. Off by default.
- **Data Retention.** Forever (default) or 3 years. With 3 years selected, trips older than 3 years are deleted on the next launch — but only after a confirmation alert tells you the count and oldest date. Locked trips and trips on the in-progress current year are never auto-deleted.

### Personalize

#### Theme

Pick from 8 color themes:

- **Warm** (default). Dark warm-brown with burnt-orange accents.
- **Light**. Daytime sibling of Warm. Toasted cream with burnt-orange accents.
- **Night.** Strict monochrome dark palette with crisp Azure-blue accent.
- **Day.** Pure-white cards on soft neutral grey, same Azure accent.
- **Slate.** Cool blue-gray with platinum highlights.
- **Sky.** Pale sky-blue throughout, navy text, amber pop on the savings figure.
- **Forest.** Deep forest greens with sage and wheat-gold accents.
- **Mint.** Soft mint as the brand voice with warm orange accents on white.

Warm is the default for everyone. The other seven require an active subscription. The picker also has a "Match iOS Dark Mode" option — pick a dark theme and a light sibling, and Milely auto-switches based on your phone's system mode.

<!-- SCREENSHOT NEEDED: Settings → Theme picker showing all eight color theme swatches -->

#### Branding (subscriber)

Customize the look of exported PDFs:

- **Logo image.** Upload your business logo. Shows on the cover page of every PDF export.
- **Accent color.** Auto-detected from your logo by default (samples the most prominent color), or you can pick manually.
- **Footer text.** Free-text. Shows on every PDF page footer ("Smith Plumbing LLC · 555-1212 · smith@plumbing.com").

### Backup

- **Cloud Backup.** *(subscriber)* Pick where to write automatic backups: iCloud Drive (free with any Apple ID, most users), or Google Drive / Dropbox / OneDrive via the iOS Files picker. Backups run on a schedule (typically once per day after a trip ends). Each backup is a JSON file with all your trips, businesses, vehicles, settings, and receipts. Files are timestamped so you can keep multiple versions.
- **Manual Export.** Always available. Tap **Export Backup** to generate a JSON file and present the iOS share sheet.
- **Restore from Backup.** Pick a backup file to restore from. Milely shows a preview (count of trips, businesses, vehicles) and asks you to confirm before applying.
- **Import from MileIQ / Everlance / TripLog.** Auto-detects the CSV format from the header row and maps each format's columns onto Milely's Trip model. Shows a preview before committing.

<!-- SCREENSHOT NEEDED: Backup screen showing Cloud Backup row with iCloud selected and last backup timestamp -->

### Integrations

- **Recover from Calendar.** Reads past calendar events with locations (on-device, never transmitted), dedupes against trips you already saved, and lets you bulk-create the rest. See [Recovering trips from your calendar](#recovering-trips-from-your-calendar).
- **Calendar Suggestions.** Off by default. When ON, Milely reads *upcoming* events with locations from your calendar and surfaces them as one-tap trip starters on the Trip tab.

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

- **Always-Allow location.** Settings → Trip Settings shows whether you have it. The card has a "Request Always Allow" button; pairing a vehicle also prompts for the upgrade.
- **At least one paired vehicle** (for CarPlay-trigger), OR **Automatic detection mode** (for motion-detected start).
- **Don't force-quit Milely.** This one's important. See below.

### What "Auto-detect armed" means

The Vehicle edit sheet and the Detection mode screen both show whether background detection is currently armed. "Armed" means Milely has registered with iOS to receive the wake-up signal when significant location changes happen. It auto-arms whenever you grant Always-Allow location or open the app.

### The force-quit caveat

iOS has a rule: when a user manually force-quits an app from the iOS app switcher (swipe up to kill), the app no longer receives Significant Location Change updates until the user opens it again. This is iOS's design, not Milely's choice — it's documented in Apple's CoreLocation reference.

What this means: if you swipe Milely up to kill it, background recording stops working until you next open the app. Other ways the app might end (a crash, iOS evicting it for memory, your phone shutting down) do NOT trigger this rule — Milely will still wake on the next SLC event.

If you suspect background recording isn't working, the easiest test is: open Milely, go to Settings → Trip Settings, and check the Background recording status card. If it says "Active", you're set. If it says "Off" or "Limited", follow the on-card instructions.

### How CarPlay-trigger consent works

There's no separate consent prompt anymore — **pairing is consent**. When you save a vehicle with a CarPlay or Bluetooth route attached, the **Auto-Start Trip on CarPlay Connect** toggle (Settings → Trip Settings → Automatic Detection) defaults to ON. Future connects to that vehicle silently start trips.

If you prefer not to have CarPlay auto-start, just turn that toggle off. Motion-based detection still catches drives in your paired vehicles after the usual arming window.

### Cross-vehicle alert

If you start a trip in Vehicle A's CarPlay, then disconnect, then connect to Vehicle B's CarPlay while the original trip is still recording, Milely shows an alert asking whether to **Stop** the original trip (so you can start a new one in B) or **Continue** recording.

### Pause-on-disconnect

The **Pause/Resume Based on CarPlay** toggle in **Settings → Trip Settings** controls disconnect behavior. It's configured separately for each mode (Manual and Automatic) so you can have one mode pause and the other not.

- **Toggle ON.** When CarPlay disconnects mid-trip, Milely pauses the recording and drops to low-power GPS so the app stays alive. When you reconnect, the trip resumes cleanly. The "do work between drives" pattern: drive to job site A, disconnect to do paperwork, drive to job site B — Milely captures one trip with two segments, the paperwork time excluded from the duration.
- **Toggle OFF.** Milely keeps recording at full GPS until you tap End or the stationary auto-end fires. Use this when a drive continues in a different vehicle, or arrives somewhere you continue on foot.

Either way, reconnecting to a *different* paired vehicle mid-trip prompts you to stop the current trip and start a new one for the new vehicle (cross-vehicle alert above).

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

## Subscription and trial

Milely is free to install and try. There's a 7-day free trial that gives you every feature unlocked. After the trial, a single subscription with two billing options, plus a one-time lifetime purchase for users who'd rather not subscribe.

### How the trial works

**The 7-day timer starts on your first recorded trip — not on app install.** Set everything up at home, pair your CarPlay, classify a sample trip, then start the clock when you're actually driving. This way you don't burn trial days while configuring.

During the trial, every feature is unlocked: unlimited recording, all themes, all export formats, Smart Suggestions, receipts, branded PDFs, cloud backup — the works.

### What stays free forever after the trial

Every trip you recorded during the trial keeps living on your phone. After the trial ends, even without subscribing you can still:

- View, edit, and re-classify any trip you already recorded.
- Re-export PDF, CSV, JSON, Excel, and QuickBooks Online any time. No format is permanently locked.
- See your full Dashboard, Logs, Reports, Trip detail, edit history, and audit lock.
- Use the Warm theme.

What you can't do without a subscription: record **new** trips. The next Start Trip tap shows the subscription prompt.

### What a subscription unlocks

- **Recording new trips.** Without a subscription, the next Start tap (or auto-detect promotion) is blocked. With one, drive as much as you want.
- **Receipts.** Scan, attach, on-PDF inclusion. See [Receipts](#receipts).
- **7 additional color themes.** Light, Night, Day, Slate, Sky, Forest, Mint.
- **Branded PDFs.** Logo, accent color, footer text on every PDF page.
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

1. Settings → Trip Settings → Background recording status card. Does it say "Active"? If not, follow the card's instructions (usually grant Always-Allow location).
2. Settings → Vehicles. Is the vehicle paired? If yes, tap into it and verify the "Auto-detect this vehicle" rows show a paired device.
3. Is **Auto-Start Trip on CarPlay Connect** turned on under Settings → Trip Settings → Automatic Detection? It defaults to ON when you pair a vehicle, but you may have turned it off.
4. Did you force-quit Milely from the iOS app switcher? Background recording is disabled until you next open the app. Reopen Milely.
5. Some CarPlay devices report a generic "CarPlay" name and an unstable UID. Settings → Vehicles → vehicle edit → set a custom display name and re-pair via the "Add from recently seen" path so the latest UID is captured.
6. If a trip "disappears" after CarPlay disconnects mid-drive, check **Settings → Trip Settings → Pause/Resume Based on CarPlay** for the active mode — turn it OFF if you'd rather Milely keep recording at full GPS through the disconnect.

### A trip didn't auto-start

If you have Automatic mode on but a trip wasn't captured:

1. Was Always-Allow location granted? Settings → Trip Settings → Background recording.
2. Was the app force-quit before the drive? Reopen and the next drive will trigger.
3. Was the drive very short (< 0.05 mi by default)? Sub-threshold trips are silently discarded by design. The threshold is in Settings → Trip Settings → Minimum logged trip distance.
4. Was your phone in airplane mode or out of cell range? GPS still works without cell, but iOS's significant-location-change wake-up needs at least one location source — try granting precise location, not just approximate.

### The app didn't relaunch after force-quit

Force-quitting Milely from the iOS app switcher disables background recording until you next open the app. This is an iOS rule for any app that uses background location, not a Milely-specific behavior. Just open Milely; background recording re-arms automatically.

### My CarPlay is named "CarPlay" — that doesn't help

Some vehicles (older models, certain wireless adapters) report only the generic name "CarPlay" instead of the vehicle's actual name. Milely handles this automatically: the in-app display concatenates the connection type with your Vehicle's name (e.g., **CarPlayTruck**, **BluetoothSedan**). Just set the Vehicle's `Name` to whatever you want shown — "Truck", "F-150", "GMC" — and the app composes the friendly label everywhere it appears (Dashboard chip, Vehicle Pairing card, Logs).

### Milely uses too much battery

Manual mode only uses battery while a trip is recording (around 3% per hour, depending on phone and conditions). Automatic mode uses iOS's significant-location-changes API when idle (very low power), then ramps up GPS only when motion suggests driving.

If battery use is high without trips being recorded, check Settings → Trip Settings → Background recording status — "Active" is correct; "Limited" or anything stuck-on may indicate stale state. Restart the app.

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

**Audit Lock.** The state of a trip where every field is read-only. Trips lock automatically the moment you Save them. A yearly January 31 banner sweeps any prior-year unlocked trips. To make changes to a locked trip, tap **Unlock for editing** on the trip detail screen — every unlock and subsequent edit is captured in the trip's edit history.

**Auto-classify rule.** A user-defined rule that pre-fills the business and purpose for any future trip ending at a specific address. Created via the "Always business" or "Always personal" buttons on a trip's detail screen. Managed via Settings → Auto-classify rules. Working hours filter applies — a rule for a "Showings" business won't auto-fire at 11 PM on a Sunday.

**CarPlay-trigger.** Auto-starting a trip when your phone connects to a paired vehicle's CarPlay or car-Bluetooth audio route. The most accurate detection signal Milely has — UID-matched and almost never wrong.

**Detection mode.** Manual (you tap Start) or Automatic (motion + significant location changes start a trip on their own). Set in Settings → Trip Settings.

**Edit history.** The append-only record of every field-level change on a trip — old value, new value, timestamp. Always on. Captures locks, unlocks, Personal toggles, receipt adds and removes. Can't be wiped from inside the app (deleting the trip removes the history with it).

**Generic-name pairing.** A CarPlay or Bluetooth route that reports only "CarPlay" as its friendly name. Milely matches by UID instead, so detection still works — set a custom display name in vehicle settings to make the in-app label useful.

**Pause/Resume Based on CarPlay.** A toggle in Settings → Trip Settings, configured separately for Manual and Automatic modes. ON: when CarPlay disconnects mid-trip, the recording pauses and GPS drops to low power; reconnecting resumes the trip. OFF: the recording keeps running at full GPS until you tap End or the stationary auto-end fires.

**Pending classify.** The state where a trip has just ended but you haven't tapped Save on the Classify screen yet. The trip is already saved to Logs as a recorded record without a business attached — Save just adds the business + purpose and locks the trip. Skip for now leaves the trip without a business assigned for later.

**Personal trip.** A drive marked Excluded from the annual report. May or may not have the built-in Personal sentinel business attached — what makes a trip "Personal" is the Excluded flag, not the absence of a business. Marked with a gray Excluded pill on the row. Excluded from every Reports figure. The built-in Personal business is optional (Settings → Personal Trips → Keep personal trips).

**Project / Client tag.** A free-text tag on each trip — type a listing address, matter name, job number, or whatever your industry uses. Surfaces as a column in CSV exports and as a "By project" breakdown in Reports.

**SeenAudioRoute.** Internal — a CarPlay or Bluetooth audio route Milely has observed at any point but you haven't yet paired to a vehicle. Shown in Settings → Vehicles under "Add from recently seen" so you can pair without being currently in the car.

**SLC (Significant Location Change).** An iOS API that wakes the app when the phone has moved a meaningful distance. Powers Automatic detection mode and CarPlay-trigger background wakeups. Requires Always-Allow location. Does NOT work after a user-initiated force-quit (iOS rule).

**Smart Suggestions.** On-device CoreML predictions of the right business and purpose for a just-ended trip, based on your past classifications. Show as one-tap chips above the business row on the Classify screen.

**Stationary auto-end.** The timeout after which a recording trip ends automatically if you've been stopped and CarPlay is disconnected. Configured globally in Settings → Trip Settings → Stationary auto-end and per-vehicle in vehicle settings.

**Trip Template (Favorite).** A saved trip you can re-launch with one tap. Created via the star button on any trip detail screen. Surfaces on the Dashboard's Favorites Quick Start row. Managed in Settings → Trip Templates.

**UID (Unique Identifier).** An iOS-internal opaque string that identifies a specific CarPlay or Bluetooth device. Stable across connections (mostly). Milely uses UIDs as the primary match for vehicle pairing because they're more reliable than friendly names.

**Excluded.** A trip's annual-report state when it's been set aside — won't count toward your deduction, won't show up in Reports, exports, or Dashboard tallies. Marked with a gray minus pill on the row in Logs. Set via swipe-LEFT on a Logs row, the Personal chip on the Classify screen, or the **Mark as personal** button in trip detail. The opposite state is **Included** (orange checkmark pill, the default for every new trip).

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
4. **Full Dashboard** — monthly card on top, Quick Start row including business rows (Personal sits in this same row when enabled) + Repeat Last + Favorites, Start Trip button at bottom.
5. **Audit-lock banner** — yellow banner on the Dashboard with Lock [year] and Not now buttons.
6. **Live trip banner** — recording state showing distance, time, deduction, with the End pill on the right.
7. **Quick Start row** — top business rows (Personal appears as a sibling row when enabled), Repeat Last, Favorites stacked.
8. **Live map (Trip tab)** — route polyline drawn, stats card overlay, End Trip button at the bottom.
9. **Settings → Trip Settings** — Automatic mode tile showing "Active" with the sub-section expanded (Auto-Start Trip on CarPlay Connect, Pause/Resume Based on CarPlay, Background Recording, Minimum Trip Distance) and Universal section visible below.
10. **Settings → Vehicles → Edit Vehicle** — Vehicle Pairing card showing "Paired and connected" with subtitle reading "CarPlayTruck" or similar concatenated label.
11. **Log Past Trip Manually form** — date picker, From/To address fields, miles field, business chips, purpose field.
12. **Classify Trip screen (full)** — route map at top, business chips (Personal sits in the same row as the user's businesses), purpose field, Save Trip button at bottom.
13. **Trip detail with receipts** — Receipts row showing two attached thumbnails plus Scan / Add from photos buttons.
14. **Trip detail (full)** — route map, all sections visible, star button in the top-right corner.
15. **Logs tab header** — search field, Year/Month/Business filter pills, list of trips below (each row shows an orange Included or gray Excluded pill).
16. **Recover from calendar** — lookback window picker and a checked list of proposed trips.
17. **Reports tab** — scrolled to show year hero, year stats grid, By business breakdown, start of monthly cards.
18. **Settings → Vehicles** — list with two vehicles and the "Add from recently seen" section visible.
19. **Settings → Businesses** — list with three businesses, color picker open on one.
20. **Settings → Theme picker** — all eight color theme swatches visible.
21. **Backup screen** — Cloud Backup row with iCloud selected and last backup timestamp.
22. **Recover trip in progress alert** — "Recover trip in progress?" with Recover / Discard / Cancel buttons.

</main>