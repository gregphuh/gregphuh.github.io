---
layout: default
title: Help & How-To
description: Walk through Milely the way you'll actually use it — track your first trip, run a tax-time report, back up your data.
permalink: /help/
---

<main>

# How to Milely

Quick, friendly walkthroughs for the things you'll actually do. If you get stuck, hit **Contact Support** below — that's a real human (a small Texas LLC running this app), not a ticket queue.

<div class="page-intro">New to Milely? The fastest path: skim the <a href="#track-trip">first section</a>, log a trip, and you'll have everything you need by lunch.</div>

---

<h2 id="track-trip">1. Record a trip</h2>

<div class="how-row">
<div class="how-text">
<p>This is the whole app, in three taps:</p>

<ol>
<li>Open the <strong>Dashboard</strong> or <strong>Trip</strong> tab and hit <strong>Start Trip</strong>.</li>
<li>Drive. Milely records the route, miles, and time in the background — switch apps, lock your phone, doesn't matter.</li>
<li>When you arrive, hit <strong>End Trip</strong>. The Classify screen pops up so you can pick a business, type a purpose, and save.</li>
</ol>

<p><strong>Faster way:</strong> on the Dashboard, the <em>Quick Start</em> rows show your top businesses + a "Repeat last trip" shortcut. One tap and the trip starts pre-filled with that business and your last-used purpose.</p>
</div>
<div class="how-img"><img src="/assets/screenshots/dashboard.png" alt="Dashboard with Quick Start chips and Start Trip button" /></div>
</div>

---

<h2 id="classify">2. Classify trips for the IRS</h2>

<div class="how-row">
<div class="how-text">
<p>The IRS wants a <em>contemporaneous record</em> with a stated business purpose for each trip. The Classify screen makes that happen in 5 seconds.</p>

<p>Tap a business chip, hit a recent purpose chip (or type a new one — "Showing 1428 Maple St" beats "Real Estate"), confirm the miles, and Save. That's the audit-ready entry done.</p>

<p><strong>Round trip?</strong> Flip the Round Trip toggle — Milely doubles the miles and saves it as one record.<br>
<strong>Wasn't actually driving?</strong> The "Was I driving?" toggle discards the trip cleanly.</p>
</div>
<div class="how-img"><img src="/assets/screenshots/trip-idle.png" alt="Trip tab idle view with Start Trip prompt" /></div>
</div>

---

<h2 id="logs">3. Browse and edit your logs</h2>

<div class="how-row">
<div class="how-text">
<p>The <strong>Logs</strong> tab shows every trip, grouped by date with a search bar across purposes, addresses, and businesses. Tap any trip to see its full route on a map and edit anything (miles, purpose, business, vehicle).</p>

<p>Forgot to start a trip? Hit <strong>Log Past Trip Manually</strong> and enter the date, miles, addresses, and purpose by hand — same audit-ready record.</p>

<p><strong>Year-locking:</strong> on January 31, Milely automatically locks the previous year's trips so you can't accidentally edit them mid-audit. Tap a trip and hit <strong>Unlock for editing</strong> if you need to amend a return.</p>
</div>
<div class="how-img"><img src="/assets/screenshots/logs.png" alt="Logs tab with searchable list of trips" /></div>
</div>

---

<h2 id="report">4. Run your annual tax report</h2>

<div class="how-row">
<div class="how-text">
<p>Come tax time, the <strong>Reports</strong> tab is the only place you need.</p>

<ol>
<li>Pick the year.</li>
<li>Tap <strong>Export PDF</strong> — cover page with totals, by-business breakdown, every trip on its own line.</li>
<li>Hit Share. Email it to your CPA or save it to Files.</li>
</ol>

<p>Need raw data for QuickBooks or a spreadsheet? <strong>Export CSV</strong> instead — one row per trip with full details.</p>

<p><strong>Real tax savings:</strong> set your federal bracket in <em>Settings → Tax Bracket</em> and the Dashboard's deduction card adds a "≈ $X saved" line — actual estimated tax savings, not just the deduction.</p>
</div>
<div class="how-img"><img src="/assets/screenshots/reports.png" alt="Reports tab with year-over-year deduction summary and Export PDF button" /></div>
</div>

---

<h2 id="backup">5. Back up your data</h2>

<div class="how-row">
<div class="how-text">
<p>Milely stores everything on your phone — no servers, no us. So <strong>your backups are your responsibility</strong> (we make it easy).</p>

<p><strong>Manual export</strong> ships with the base app: <em>Settings → Manual Export</em> gives you a JSON backup file via the iOS share sheet — email it, AirDrop it, drop it in Files. Free, any time.</p>

<p>Want backups to be automatic? That's a <strong>Milely+</strong> add-on (see section 6).</p>

<p><strong>Restoring on a new iPhone:</strong> reinstall Milely → open the backup file from Files → tap "Open in Milely". Done. (One-tap restore is on the roadmap.)</p>
</div>
<div class="how-img"><img src="/assets/screenshots/settings.png" alt="Settings screen with Cloud Backup and Manual Export options" /></div>
</div>

---

<h2 id="customize">6. Milely+ — the optional $0.99/yr add-on</h2>

The base app at **$4.99** has everything you need to track miles and run an annual report. **Milely+** is a separate, optional **$0.99/year** subscription that adds the following — *only* if you want them:

- **Receipts.** Scan receipts with VisionKit's document camera (edge detection, perspective correction, multi-page) or attach existing photos from your camera roll. Receipts surface alongside each trip and on the PDF report.
- **Branded PDFs.** Your business logo on every cover, accent colors auto-matched to your brand, your firm name + contact info in the footer of every page.
- **Five extra themes + Brand mode.** Adds Light, Forest, Mint, Sky, and Slate. Brand mode paints the whole app in colors derived from a business logo.
- **Automatic cloud backup.** iCloud Drive or any Files-app cloud (Google Drive, Dropbox, OneDrive). Hands-off after setup. *(Base app does manual JSON export.)*
- **Branded map route.** Trip route renders in Milely's signature gradient instead of Apple's default blue.
- **Priority support.** Front of the queue at [milely@smileycreative.io](mailto:milely@smileycreative.io).
- **Every update as soon as it ships** — no extra purchases.

Subscribe in **Settings → Milely+**. Cancel any time in Apple's subscription management — your subscription stays active through the end of the period you paid for.

---

## Quick answers

<details>
<summary><strong>Does Milely work without internet?</strong></summary>
Yes — recording, classifying, browsing, exporting, and reports all work fully offline. The only thing internet enables is uploading backups to your cloud.
</details>

<details>
<summary><strong>Will it drain my battery?</strong></summary>
Manual mode only consumes battery while a trip is recording (~3% per hour). Automatic mode uses iOS's significant-location-changes API when idle (negligible drain) and only ramps up GPS when motion suggests driving.
</details>

<details>
<summary><strong>How does Automatic mode work?</strong></summary>
Settings → Detection mode → switch to <strong>Automatic</strong>. Milely uses motion + GPS to detect when you start driving, records the route in the background, and notifies you to classify after the trip ends. Requires "Always Allow" location and Motion & Fitness permissions.
</details>

<details>
<summary><strong>Why is the IRS rate adjustable?</strong></summary>
The IRS publishes a new standard mileage rate annually, sometimes mid-year. <strong>Settings → IRS Rate</strong> lets you confirm or update what Milely uses. We pre-load defaults but you should verify at <a href="https://www.irs.gov">irs.gov</a> before filing.
</details>

<details>
<summary><strong>Can I use Milely on multiple devices?</strong></summary>
Today: back up on Device A, restore manually on Device B. Real multi-device sync is on the roadmap.
</details>

<details>
<summary><strong>What about Android?</strong></summary>
Milely is iOS-only and likely staying that way. We're a tiny team and iOS is what we know.
</details>

---

## Still stuck?

Email [**milely@smileycreative.io**](mailto:milely@smileycreative.io) with what you were trying to do, what you expected, and what happened. Screenshots help. We answer within a couple business days (and we read every email).

</main>
