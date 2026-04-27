---
layout: default
title: Help & How-To
description: Learn how to track trips, classify them, run reports, and back up your data with Milely.
permalink: /help/
---

<main>

# Help & How-To

Everything you need to know to use Milely. Roughly in the order you'll need it.

<div class="page-intro">If you can't find what you need here, email <a href="mailto:support@milely.io">support@milely.io</a>.</div>

---

## Getting started

### First launch

When you first open Milely, a 7-step onboarding walks you through:

1. **Welcome** — a quick overview.
2. **How it works** — a short explainer.
3. **Your business name** — type the name of the business you'll track miles for. You can add more later in Settings.
4. **Backup choice** — pick **iCloud Drive** (recommended), **Google Drive**, or **This iPhone only**.
5. **Location access** — Milely needs this to record the route and distance of trips. Tap "Allow While Using App."
6. **Notifications** — optional. Lets Milely remind you to classify trips and surface the weekly review.
7. **Done** — straight into the Dashboard.

You can re-run any of these steps later from **Settings**.

---

## Recording trips

### Manual mode (the default)

1. From the **Dashboard** or **Trip** tab, tap **Start Trip**. Milely begins recording.
2. The Dashboard's brand header morphs to show live miles, time, and an **End** button.
3. Switch to the **Trip** tab to see your route drawing on a live map.
4. When you arrive, tap **End Trip**.
5. The **Classify** view opens — review/edit anything (miles, addresses, business, purpose), then tap **Save Trip**.

### Quick Start (faster)

On the Dashboard, the "By Business · Quick Start" section shows your top 3 businesses plus a "Repeat last trip" row. Tap any one and a new trip starts with that business pre-selected and your last-used purpose pre-filled.

Tip: build up your list of common purposes by just using the app. The Classify view shows recent purposes for each business as tappable chips.

### Automatic mode

In **Settings → Detection mode**, switch to **Automatic**. Milely will:

- Use motion + GPS to detect when you start driving
- Record the route in the background
- Notify you after the trip ends so you can classify it

Auto mode requires **Always Allow** location and Motion & Fitness permissions. If you decline, Manual mode still works.

---

## Classifying trips

When a trip ends, the Classify view shows:

- **The route map** with a polyline of your drive
- **Trip facts** — miles, date, from/to addresses (all editable)
- **Business chips** — pick the business this trip belongs to
- **Recent purposes** — tappable chips that fill the purpose field with one of your past entries
- **Purpose field** — type the specific business purpose (required for IRS Pub. 463)
- **Vehicle chips** — pick which car you drove (auto-detected if paired)
- **"Was I driving?" toggle** — turn off if you were a passenger; trip is discarded
- **Round trip toggle** — doubles the miles for the return leg, saves as one record
- **Ready to save summary** — final preview of everything that will be saved
- **Save Trip · $X.XX** — shows the deduction you'll lock in

Before you tap Save, double-check the **purpose** field. The IRS expects a stated business purpose, not just a category — e.g., "Showing 1428 Maple St" rather than just "Real Estate."

---

## Trip Templates

For routes you do over and over (e.g., "McKinney → Killeen Next Storage round trip"), create a template:

1. **Settings → Trip Templates → +**
2. Give it a name, set the business, fill in the purpose, optional addresses and estimated miles
3. Save

To start a templated trip: pull up the templates list in Settings, swipe right on the row, tap **Start**. Or tap the **▶︎** button next to the template name.

---

## Vehicles

### Adding a vehicle

**Settings → Vehicles → +**. Enter a name, optional make/model, and current odometer. Set as default if it's your primary.

### Pairing a vehicle to your car

Milely can auto-pick the right vehicle when you start a trip if you pair it to your car's CarPlay or Bluetooth:

1. Connect your phone to your car (CarPlay or Bluetooth)
2. **Settings → Vehicles → tap the vehicle**
3. In the "Auto-detect this vehicle" section, tap **Pair to currently connected device**
4. Save

From then on, when your phone is connected to that car, Milely defaults the trip to that vehicle.

---

## Reports & exports

### Annual report (Schedule C)

**Reports tab → pick a year → Export PDF**. The PDF has:
- A **cover page** with totals (trips, miles, IRS rate, deduction)
- **By-business breakdown** with each business's miles + dollar amount
- **Per-trip log** — date, business, purpose, miles, deduction

This is the document you (or your CPA) reference when filling out Schedule C.

### CSV export

**Reports tab → Export CSV**. One row per trip with date, time, business, purpose, addresses, miles, vehicle, deduction. Opens in Excel, Numbers, or Google Sheets.

### Sharing

The share sheet appears after both PDF and CSV exports. Send via email, AirDrop, save to Files, or upload anywhere.

---

## Backups & restore

### iCloud Drive backup

**Settings → Backup & Restore → toggle iCloud Drive on**. Then tap **Back up now**. Backups appear in `iCloud Drive → Milely-Backups/`. Free, encrypted by Apple, automatic.

### Google Drive (or any cloud) via Files

**Settings → Backup & Restore → Choose backup folder**. iOS opens the Files picker. Navigate to **Google Drive** (you must have the Google Drive app installed and signed in) or any other Files provider — Dropbox, OneDrive, Box. Pick a folder.

Milely creates a `Milely Backups/` subfolder inside and saves your first backup there. Future backups write to that same folder with one tap.

### Manual export

**Settings → Backup & Restore → Export & share JSON**. Generates a backup file and opens the iOS share sheet. Send it anywhere.

### Tax bracket → real savings

**Settings → Tax Bracket**. Pick your federal marginal tax bracket. The dashboard's deduction card now shows an additional line "≈ $X saved" — your actual estimated tax savings (deduction × bracket).

---

## Privacy & data

Milely never transmits your data to Milely-controlled servers. There are no Milely servers. Backups go to **your** iCloud, **your** Google Drive — Milely just generates the file and hands it off.

The full privacy policy is at [milely.io/privacy](/privacy/).

---

## Milely+

**$0.99/year, optional.** The base app is fully functional forever after your one-time $3.99 purchase. Milely+ is an annual auto-renewing subscription that adds:

- **Priority support** — bumped to the front of the queue at support@milely.io
- **Early access** to new features in beta
- **Premium add-ons** released throughout the year (additional themes, advanced report templates, alternate icons)
- **Helps fund development** — supports continued work on Milely

Subscribe in **Settings → Milely+** when you're ready. Cancel any time in Apple's subscription management — you keep Milely+ features through the end of the period you paid for. Apple manages all billing.

---

## Common questions

### Does Milely work without internet?

Yes. The only thing internet enables is uploading backups to cloud storage. Recording, classifying, viewing, exporting, reports — all work offline.

### Will it drain my battery?

In Manual mode, only while a trip is recording. We use sparse GPS sampling (one waypoint per 0.1 mi or 30 seconds, whichever first) to keep drain low.

In Automatic mode, the app uses iOS's significant-location-changes API when idle (negligible drain), then ramps up only when motion suggests driving.

### Why is the year-over-year IRS rate adjustable?

The IRS publishes a new standard mileage rate annually, sometimes with mid-year adjustments. **Settings → IRS Rate** lets you confirm or update the rate Milely uses. We pre-load defaults but you should verify at [irs.gov](https://www.irs.gov) before filing.

### Can I delete a trip after saving?

Yes — open the trip in the Trips tab, tap **Delete Trip** at the bottom. If you locked the year (auto-locks on January 31 of the following year), unlock the trip first.

### How does year-locking work?

To prevent accidental edits to past tax records, Milely auto-locks any trip dated in a previous tax year on January 31 of the current year. Open the trip and tap **Unlock for editing** if you need to amend.

---

## Still stuck?

Email **support@milely.io** with a brief description of what you're trying to do. We'll get back within a few business days.

</main>
