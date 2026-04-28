---
layout: default
title: Privacy Policy
description: Milely's privacy policy — how (and why) we don't collect your data.
permalink: /privacy/
---

<main markdown="1">

# Privacy Policy

<div class="legal-meta">
  <strong>Effective:</strong> April 26, 2026 &nbsp;·&nbsp; <strong>Last updated:</strong> April 28, 2026
</div>

<div class="legal-summary">
  <h3>Plain-English Summary</h3>
  <p><strong>Milely doesn't collect your data.</strong> The app does not operate any servers. Every trip, photo, address, vehicle, and business name you enter lives on your iPhone. Backups, when you enable them, go directly from your device to your iCloud Drive or chosen Files-app provider — never through us.</p>
  <p>This page explains the technical details, the limited data the app handles locally, and your rights under U.S. and international privacy law.</p>
</div>

Milely is an iOS application published by **SmileyCreative LLC** (a Texas limited liability company) that helps you track business mileage for tax-record-keeping purposes. Privacy is foundational to how Milely is designed: **the app does not operate any servers, and your data never reaches us.** This Privacy Policy describes the limited data the app handles locally on your device, third parties involved when you enable optional features, and the privacy rights available to you under applicable law.

<div class="legal-toc">
  <h3>Contents</h3>
  <ol>
    <li><a href="#what-we-collect">What we don't collect</a></li>
    <li><a href="#what-app-handles">What the app handles locally</a></li>
    <li><a href="#where-data-lives">Where your data lives</a></li>
    <li><a href="#backups">Backups (your choice)</a></li>
    <li><a href="#location">Location data</a></li>
    <li><a href="#motion">Motion data</a></li>
    <li><a href="#calendar">Calendar data</a></li>
    <li><a href="#photos">Receipt photos</a></li>
    <li><a href="#carplay">Vehicle connectivity</a></li>
    <li><a href="#third-parties">Third-party services</a></li>
    <li><a href="#retention">Data retention</a></li>
    <li><a href="#international">International data transfers</a></li>
    <li><a href="#breach">Security &amp; data breaches</a></li>
    <li><a href="#children">Children's privacy</a></li>
    <li><a href="#california">California residents (CCPA / CPRA)</a></li>
    <li><a href="#europe">European Economic Area, U.K., Switzerland (GDPR)</a></li>
    <li><a href="#withdraw">Withdrawing consent</a></li>
    <li><a href="#rights">Exercising your rights</a></li>
    <li><a href="#changes">Changes to this policy</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</div>

---

## 1. What we don't collect {#what-we-collect}

Milely **does not collect** any of the following from you:

- **Personally identifiable information.** No name, email address, phone number, postal address, date of birth, social security number, taxpayer ID, government ID, or biometric identifier.
- **Account credentials.** Milely has no user accounts. There is no sign-up, no login, no password.
- **Payment information.** Apple handles all subscription and one-time purchase billing on its own servers. Milely never sees your card, billing address, or financial details.
- **Contacts, messages, browsing history, photos library**, or any other system-level data not directly used by a feature you've enabled.
- **Advertising identifiers (IDFA / IDFV).**
- **Device fingerprints, IP addresses, or telemetry.** The App makes no analytics or telemetry calls. We do not know whether or how often you use the App.
- **Crash reports.** We rely solely on Apple's optional, opt-in crash reporting; no third-party crash SDK is integrated.

There are no third-party analytics, advertising, attribution, A/B testing, marketing, or tracking SDKs in the App.

---

## 2. What the app handles locally {#what-app-handles}

The App stores the following on your device — and only on your device — when you create or record it:

- **Trip records** — start and end coordinates, route polyline (a sparse list of GPS points), distance, duration, date, vehicle, business category, and the free-text purpose you enter.
- **Vehicle records** — the names, makes, models, and odometer values you enter.
- **Business records** — the business names, colors, and (optional) logos you create (e.g. "Real Estate," "Next Storage").
- **App settings** — your preferred mileage rate, tax bracket (optional), backup configuration, theme choice, and similar preferences.
- **Receipt photos** — only if you choose to scan or attach photos to a trip.

This data lives in Apple's SwiftData on-device store. It is included in backups only if you enable backups, as described below.

---

## 3. Where your data lives {#where-data-lives}

**On your device.** Period. Milely does not operate any servers. There is no Milely-controlled database, no Milely cloud, and no Milely employee with access to your records.

---

## 4. Backups (your choice) {#backups}

Milely lets you choose whether and where to back up your data. When enabled, backups are written **directly from your device** to the destination you select. Milely does not see, intercept, or store backups; they go device-to-cloud or device-to-file using Apple-provided system APIs.

Available options:

- **iCloud Drive.** Backups are encrypted by Apple and governed by [Apple's Privacy Policy](https://www.apple.com/legal/privacy/).
- **Google Drive, Dropbox, OneDrive, Box, or any iOS Files-app provider.** Only if you authorize it via the iOS Files picker. Data sent to these providers is governed by their respective privacy policies — see [Google](https://policies.google.com/privacy), [Dropbox](https://www.dropbox.com/privacy), [Microsoft](https://privacy.microsoft.com/), [Box](https://www.box.com/legal/privacy).
- **Manual export.** You can export a CSV or JSON file of your trips at any time using the iOS share sheet — email, AirDrop, save to Files, or upload anywhere.

You can disable any backup option in Settings → Backup at any time. Disabling a backup does not delete previous backup files at the destination; you must delete those yourself from the storage provider's app or website.

---

## 5. Location data {#location}

Milely uses Apple's Core Location APIs to record the route and distance of each trip. Location is used **only** while a trip is being recorded:

- In **Manual mode**, location is captured only between when you tap "Start Trip" and "End Trip."
- In **Automatic mode**, location is captured only when Milely's motion-detection determines you are driving. The App uses iOS background-location APIs only to detect trip start/end events; it does not record your location continuously.

Location data is stored locally on your device. It is included in backups only if you enable backups (see § 4). You can revoke the App's location permission at any time in iOS Settings → Privacy &amp; Security → Location Services → Milely. Doing so disables trip recording.

---

## 6. Motion data {#motion}

Milely uses Apple's Core Motion APIs solely to detect when you start driving (Automatic mode only). Motion data is processed on your device, in real time, and is **never stored** by Milely or transmitted anywhere. You can revoke the App's motion permission in iOS Settings → Privacy &amp; Security → Motion &amp; Fitness → Milely.

---

## 7. Calendar data {#calendar}

If you enable Calendar Suggestions (off by default — Settings → Integrations → Calendar suggestions), Milely uses iOS EventKit to read your calendar events that have a location and surface them as suggested trips. Calendar data is read only on demand, kept only in app memory while you're using the relevant view, and **never stored in the App's database or transmitted off-device**. You can revoke calendar permission in iOS Settings → Privacy &amp; Security → Calendars → Milely.

---

## 8. Receipt photos {#photos}

If you scan or attach a photo to a trip, the photo is stored as part of the trip record on your iPhone. Photos are processed on-device using Apple's VisionKit (for scan/edge-detection) and Vision (for optional text-recognition of receipt totals). **No photo data leaves your device** unless you (a) enable backups, in which case the photos are included with the backup, or (b) manually share a trip via the iOS share sheet.

You can revoke camera or photo-library permissions in iOS Settings → Privacy &amp; Security → Camera / Photos → Milely.

---

## 9. Vehicle connectivity (CarPlay / Bluetooth) {#carplay}

If you pair a vehicle to a connected device (CarPlay or Bluetooth audio), Milely stores the device's port name (e.g., "Greg's Truck") on the vehicle record so the App can auto-select the right vehicle when you connect to it. Milely uses Apple's `AVAudioSession` API to detect the currently connected device — this does not require any special entitlements and **does not transmit data off-device**.

---

## 10. Third-party services {#third-parties}

Milely contains **no** third-party analytics, advertising, attribution, or tracking SDKs. The only third parties touched by the App, and only when you take an action that triggers them:

- **Apple Maps.** Only when you tap "Open in Apple Maps" from a saved trip. Apple Maps receives the destination URL via the iOS open-URL API; the App does not transmit additional data.
- **Google Drive / Dropbox / OneDrive / Box (etc.).** Only if you enable backups to those services and authorize file writes via the iOS Files app. The Files framework handles the file save; Milely does not call those services' APIs directly. Your data with those providers is governed by their own privacy policies.
- **Apple iCloud Drive.** If you enable iCloud Drive backup, the file is written via Apple's framework. Apple's privacy policy applies.
- **Apple App Store.** All purchases (subscription, lifetime, refunds) are handled by Apple. Milely never sees your payment information; we receive only an anonymized "this user has an active subscription" signal that StoreKit hands the App locally on each launch.
- **Apple's Notification system.** If you enable notifications, the iOS notification system handles delivery on-device. Milely does not use a server-side push provider.

---

## 11. Data retention {#retention}

Because Milely does not collect or store data on any Milely-controlled server, there is **no Milely-side data retention period**. Your data is retained for as long as it remains on your device or in your chosen backup destination.

When you delete the App from your device, all on-device data — trip records, photos, settings — is removed by iOS.

---

## 12. International data transfers {#international}

Milely does not operate any servers and does not transfer your data to any country. Your data stays on your device unless you choose to back it up.

If you enable a third-party backup destination (e.g., iCloud, Google Drive), that provider may store your backup in data centers in any country. The transfer is between your device and the provider; Milely is not involved. Refer to your chosen provider's privacy policy for cross-border transfer details.

---

## 13. Security &amp; data breaches {#breach}

Because Milely does not operate any servers and does not collect data, there is **no central database for an attacker to breach**. The security of your trip data is governed by:

- **Your iPhone's security model.** iOS stores app data in a sandboxed, encrypted container. We strongly recommend enabling Face ID/Touch ID, a strong device passcode, and automatic iOS updates.
- **Your chosen backup provider's security.** If you enable iCloud Drive or a third-party Files provider, that provider's security and breach-notification practices apply to your backup files.

If we ever become aware of a security issue affecting the App that could place your data at risk, we will post a notice at this URL and (where practicable) flag it via an App Store update note. Because we do not maintain user contact information, we cannot send individual breach notifications.

---

## 14. Children's privacy {#children}

Milely is **not directed at, or intended for use by, children under 13** (or under 16 in jurisdictions where 16 is the applicable threshold under the Children's Online Privacy Protection Act, the GDPR, or comparable regulations). The App does not knowingly collect any information from children. If you believe a child has used the App and you'd like the App removed from their device, deleting the App from the device is sufficient — there is no Milely-side data to remove.

---

## 15. California residents (CCPA / CPRA) {#california}

If you are a California resident, the California Consumer Privacy Act of 2018 ("**CCPA**"), as amended by the California Privacy Rights Act ("**CPRA**"), grants you specific rights regarding your personal information.

**Personal information we collect, sell, or share.** **None.** Milely does not collect, sell, share, or disclose personal information for any commercial purpose. We have no servers and operate no advertising or analytics business.

Your rights under California law:

- **Right to know.** You may request a description of personal information collected, used, disclosed, or sold. Our answer is: we collect none.
- **Right to delete.** You may request deletion of personal information. There is nothing on a Milely server to delete; deleting the App from your device removes all on-device data.
- **Right to correct.** You may correct inaccurate personal information. Edit your trip records directly in the App.
- **Right to opt out of sale or sharing.** Not applicable — we do not sell or share personal information. There is no "Do Not Sell My Personal Information" link to publish because there is nothing to opt out of.
- **Right to limit use of sensitive personal information.** Not applicable — we do not use sensitive personal information.
- **Non-discrimination.** Milely does not offer financial incentives in exchange for personal information.
- **Authorized agents.** You may designate an authorized agent. Because we maintain no records of you, there is nothing for an agent to retrieve.
- **Shine the Light Law (Cal. Civ. Code §1798.83).** Not applicable; we do not share personal information with third parties for direct marketing.

To exercise any of these rights, contact us at **milely@smileycreative.io**. We will respond within 45 days as required by law (or longer where law permits an extension).

---

## 16. European Economic Area, United Kingdom, and Switzerland (GDPR) {#europe}

If you are in the European Economic Area, the United Kingdom, or Switzerland, the General Data Protection Regulation ("**GDPR**") and corresponding U.K. and Swiss laws grant you rights regarding your personal data.

**Controller.** SmileyCreative LLC, Texas, U.S.A. is the data controller for the limited personal data the App handles. Because we have no servers and collect no personal data, our controller obligations are minimal in practice. We have not designated a Data Protection Officer because we are not required to under Article 37 of the GDPR.

**Lawful basis for processing.** Where the App processes data on your device (locally), the lawful basis is your **consent** (e.g., granting location, motion, calendar, photos permissions in iOS) and **performance of a contract** (delivering the App's core function). You can revoke consent at any time by revoking the relevant iOS permission or deleting the App.

**Your rights.** You have the right to:

- Access the personal data being processed (open the App; everything is visible inside it);
- Have inaccurate data rectified (edit in the App);
- Have data erased (delete the App from your device);
- Restrict processing (revoke iOS permissions);
- Data portability (export via Settings → Manual Export);
- Object to processing (revoke iOS permissions, delete the App);
- Withdraw consent (see § 17);
- Lodge a complaint with your local data-protection authority.

We do not engage in automated decision-making or profiling.

**International transfers.** As described in § 12, Milely itself transfers no data internationally. If you choose a third-party backup destination (e.g., Google Drive), that provider's lawful-transfer mechanism (such as Standard Contractual Clauses) governs the transfer.

---

## 17. Withdrawing consent {#withdraw}

You can withdraw any consent you've previously given the App, at any time:

- Revoke any iOS permission (Location, Motion, Calendars, Camera, Photos, Notifications) in Settings → Privacy &amp; Security.
- Disable any backup option in Settings → Backup.
- Delete the App from your device, which removes all on-device data and revokes all consents simultaneously.

Withdrawing consent does not affect the lawfulness of processing that occurred before the withdrawal.

---

## 18. Exercising your rights {#rights}

Because Milely stores data only on your device, most rights are exercisable directly inside the App without contacting us:

- **Access / view.** Open the App — all your data is fully visible.
- **Correct.** Edit any record inside the App.
- **Export.** Settings → Manual Export → share the JSON or CSV file via the iOS share sheet.
- **Delete.** Delete the App from your iPhone or use Settings → Reset to wipe local data.

For requests that for any reason you cannot fulfill in-app — for example, a complaint or a question about your rights — contact us at **milely@smileycreative.io**. We will respond within 30 days (or longer where law permits an extension), and at no charge unless the request is excessive or repetitive.

---

## 19. Changes to this policy {#changes}

If this policy changes, the updated version will be posted at this URL with a new "Last updated" date. Material changes will be flagged in-app where practicable and (for residents of jurisdictions that require advance notice) at least 30 days before they take effect. Your continued use of the App after the effective date constitutes acceptance of the revised policy.

---

## 20. Contact {#contact}

Questions about this policy, requests under CCPA, GDPR, or similar laws, or any other privacy concern:

**SmileyCreative LLC**  
Attn: Milely Privacy  
**milely@smileycreative.io**

---

*Milely is published by SmileyCreative LLC, a Texas limited liability company. © 2026 SmileyCreative LLC. All rights reserved.*

</main>
