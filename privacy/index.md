---
layout: default
title: Privacy Policy
description: Milely's privacy policy — how (and why) we don't collect your data.
permalink: /privacy/
---

<main>

# Privacy Policy

**Effective:** April 26, 2026
**Last updated:** April 26, 2026

Milely is an iOS application that helps you track business mileage for tax purposes. Privacy is fundamental to how Milely is designed: **the app does not operate any servers, and your data never reaches us.**

---

## What data Milely collects

Milely collects only the data you generate while using the app:

- **Trip data** — start and end coordinates, route polyline (a sparse list of GPS points along your trip), distance, duration, date, vehicle, business category, and the free-text purpose you enter.
- **Vehicle records** — name, make, model, and odometer readings you provide.
- **Business records** — names of the businesses you create (e.g., "Real Estate", "Next Storage").
- **App settings** — your preferred IRS mileage rate, tax bracket (optional), backup configuration, notification preferences.

Milely does **not** collect: your name, email, phone number, contacts, photos, payment information, advertising identifiers, or any analytics about how you use the app.

---

## Where your data lives

**On your device.** All trip data is stored locally on your iPhone using Apple's SwiftData framework. Milely does not operate any servers and does not maintain any database of user data.

---

## Backups (your choice)

Milely lets you choose where to back up your data. You can enable any combination of:

- **iCloud Drive** — backups are encrypted by Apple and governed by [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).
- **Google Drive (or any iOS Files provider)** — only if you authorize it via the iOS Files picker. Data sent to Google Drive is governed by [Google's Privacy Policy](https://policies.google.com/privacy). Files providers like Dropbox and OneDrive work the same way.
- **Manual export** — you can share a CSV or PDF of your trips at any time using the iOS share sheet, sending it wherever you choose (email, Files, AirDrop, etc.).

In all cases, backup data is written **directly from your device** to the destination you choose. Milely never receives, transmits, or has access to your backups.

---

## Location data

Milely uses Apple's Core Location APIs to record the route and distance of each trip:

- In **Manual mode**, location is recorded only between when you tap "Start Trip" and "End Trip."
- In **Automatic mode**, location is recorded only when Milely's motion-detection determines you are driving. The app uses iOS background-location APIs only to detect trip start/end events; it does not record your location continuously.

Location data is stored locally on your device. It is included in backups only if you enable backups (see above).

---

## Motion data

Milely uses Apple's Core Motion APIs solely to detect when you start driving (Automatic mode only). Motion data is processed on your device, in real time, and is **not stored** by Milely or transmitted anywhere.

---

## Calendar data

If you enable Calendar Suggestions (off by default — Settings → Integrations → Calendar suggestions), Milely uses iOS EventKit to read your calendar events with locations and surface them as suggested trips. Calendar data is read only on demand, kept only in app memory while you're using the Trip tab, and **never stored or transmitted**.

---

## Photo Library / Camera

If you attach a receipt photo to a trip, the photo is stored as part of the trip record on your iPhone. Photos are included in backups (see above) only if you enable backups.

---

## Vehicle connectivity (CarPlay / Bluetooth)

If you pair a vehicle to a connected device (CarPlay or Bluetooth audio), Milely stores the device's port name (e.g., "Greg's Truck") on the vehicle record on your iPhone. Milely uses Apple's `AVAudioSession` API to detect the currently connected device — this does **not** require any special entitlements and does **not** transmit data off-device.

---

## Third-party services

Milely contains **no** third-party analytics, advertising, attribution, or tracking SDKs. The only third-party services touched by the app are:

- **Apple Maps / Google Maps / Waze** — only when you tap an "Open in Maps" link to navigate. The destination URL is opened in those apps via the iOS share/open API; Milely does not transmit data to them beyond the destination coordinates that the URL contains.
- **Google Drive / Dropbox / OneDrive (etc.)** — only if you choose to back up to one of them via the iOS Files app. Apple's Files framework handles the file save; Milely does not call those services' APIs directly.
- **Apple iCloud** — if you enable iCloud Drive backup, files are written to your iCloud Drive via Apple's framework.

---

## Children's privacy

Milely is not directed at, or intended for use by, children under 13.

---

## Your rights

Because Milely stores data only on your device:

- **Access:** open the app — your data is fully visible inside it.
- **Export:** use the share-sheet export to download a copy in CSV or PDF.
- **Delete:** delete the app from your iPhone, or use Settings → Reset to wipe all data.

Milely cannot access, modify, or delete data on your behalf because Milely does not have a copy.

---

## Changes to this policy

If this policy changes, the updated version will be posted at this URL with a new "Last updated" date. Material changes will also be flagged in-app.

---

## Contact

Questions about this policy:
**privacy@smileycreative.io**

---

*Milely is published by SmileyCreative LLC, a Texas limited liability company. © 2026 SmileyCreative LLC. All rights reserved.*

</main>
