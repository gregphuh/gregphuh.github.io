---
layout: default
title: Privacy Policy
description: Milely's privacy policy. The app runs no servers, collects no analytics, and stores trip data only on your iPhone. Plain-English summary of GDPR, CCPA, and TDPSA rights.
permalink: /privacy/
redirect_from:
  - /privacy.html
  - /privacy-policy/
  - /privacy-policy
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
    <li><a href="#crash-reports">Crash reports &amp; diagnostics</a></li>
    <li><a href="#website">Website privacy</a></li>
    <li><a href="#email-handling">Inbound email handling</a></li>
    <li><a href="#tracking-signals">Tracking-signal disclosure (DNT / GPC)</a></li>
    <li><a href="#retention">Data retention</a></li>
    <li><a href="#international">International data transfers</a></li>
    <li><a href="#breach">Security &amp; data breaches</a></li>
    <li><a href="#children">Children's privacy</a></li>
    <li><a href="#us-state-rights">U.S. state privacy rights</a></li>
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
- **Third-party crash reports.** No third-party crash SDK is integrated. See § 11 for the limited Apple-side picture.

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

<div class="legal-note" markdown="1">
**Precise geolocation under CPRA / TDPSA.** California's CPRA and the Texas Data Privacy and Security Act treat precise geolocation as a category of "sensitive personal information." The App's local-only processing means **SmileyCreative LLC does not "use," "process," "collect," "sell," or "share" precise geolocation in the meaning of the CPRA or TDPSA — the data never reaches us**. The data is generated and consumed entirely on your device, by software running locally for your benefit.
</div>

---

## 6. Motion data {#motion}

Milely uses Apple's Core Motion APIs solely to detect when you start driving (Automatic mode only). Motion data is processed on your device, in real time, and is **never stored** by Milely or transmitted anywhere. You can revoke the App's motion permission in iOS Settings → Privacy &amp; Security → Motion &amp; Fitness → Milely.

---

## 7. Calendar data {#calendar}

If you enable Calendar Suggestions (off by default — Settings → Integrations → Calendar suggestions), Milely uses iOS EventKit to read your calendar events that have a location and surface them as suggested trips. Calendar data is read only on demand, kept only in app memory while you're using the relevant view, and **never stored in the App's database or transmitted off-device**. You can revoke calendar permission in iOS Settings → Privacy &amp; Security → Calendars → Milely.

---

## 8. Receipt photos {#photos}

If you scan or attach a photo to a trip, the photo is stored as part of the trip record on your iPhone. Photos are processed on-device using Apple's VisionKit (for scan/edge-detection) and Vision (for optional text-recognition of receipt totals). Location and timestamp metadata (EXIF) are stripped from each receipt photo before it's saved into the trip record, so a backup file or a shared trip cannot leak where the photo was taken. **No photo data leaves your device** unless you (a) enable backups, in which case the photos are included with the backup, or (b) manually share a trip via the iOS share sheet.

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

## 11. Crash reports &amp; diagnostics {#crash-reports}

Milely integrates **no third-party crash-reporting SDK**. We do not run our own crash collector. We do not receive crash data through any service we operate.

That said, you should be aware that **Apple's developer-diagnostics program** may surface anonymized crash and energy reports to Apple-Connect dashboards available to the App's developer. This happens only if you have opted in to **Settings → Privacy &amp; Security → Analytics &amp; Improvements → Share with App Developers** at the iOS level. When that toggle is on, Apple may anonymize and aggregate diagnostic data and make it available to the Company through App Store Connect.

The data shown to the Company in App Store Connect:

- Is **aggregated and anonymized** by Apple before we see it (no user identifier);
- Is **opt-in at the iOS level**, controlled solely by Apple and by you;
- Is used by us only to identify and fix crashes and performance regressions;
- Is **not joined**, by us, with any other identifier or data source.

To turn this off entirely, open iOS Settings → Privacy &amp; Security → Analytics &amp; Improvements and toggle **Share with App Developers** off.

---

## 12. Website privacy {#website}

This privacy policy is published at **milely.io**, which is a static website served by **GitHub Pages** (operated by GitHub, Inc., a subsidiary of Microsoft Corporation). When you visit milely.io:

- **Hosting.** GitHub Pages serves the site's HTML, CSS, images, and fonts. As a standard part of operating any web server, **GitHub logs visitor IP addresses, user-agent strings, and request paths** for security, abuse-prevention, and operational purposes. Those logs are governed by [GitHub's Privacy Statement](https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement). The Company does not access or aggregate those logs.
- **Fonts.** The site loads typefaces (Inter, Space Grotesk) from **Google Fonts**. When your browser fetches a font file, Google may receive your IP address and user-agent. See [Google's privacy policy](https://policies.google.com/privacy).
- **No third-party analytics.** The site does not include Google Analytics, Plausible, Fathom, Mixpanel, Segment, or any other web-analytics tag. No A/B-testing or marketing pixel is present. The Company does not run any first-party analytics on the site.
- **No advertising.** No advertising network or ad pixel is loaded.
- **Cookies.** The site sets **no cookies** under the milely.io domain. Embedded fonts and any third-party links you may follow are governed by their own terms and may set cookies on those third-party domains (not on milely.io).
- **Email links.** The site contains `mailto:` links to **milely@smileycreative.io**. Any email you send is handled per § 13.

If we add any analytics or cookies in the future, we will update this Section before doing so and (where practicable) flag the change in-app.

---

## 13. Inbound email handling {#email-handling}

If you email **milely@smileycreative.io**, what we do with your email:

- **Receipt and review.** Inbound mail is read by a human at SmileyCreative LLC — typically the developer who wrote the App. There is no chatbot, no automated triage, and no pipeline that hands your email to a third-party analytics or marketing platform.
- **Retention.** Support and privacy correspondence is retained for up to **24 months** after the conversation closes, unless a longer retention is required to resolve an open issue (for example, a multi-month bug investigation or a legal hold). Threads tied to refunds, security disclosures, or legal complaints may be retained longer as required by applicable law.
- **No marketing or analytics use.** The Company does not add your email address to any marketing list, mailing list, or newsletter, and does not feed your email content into any analytics or AI-training pipeline.
- **Mail provider.** Email is delivered through standard SMTP-based providers; the contents of any email transit and are stored by those providers under their own terms. The Company will not voluntarily share your email content with third parties except as required to operate the mail service or comply with law.
- **Deletion on request.** You may at any time request deletion of email correspondence by replying to the relevant thread or writing **milely@smileycreative.io**. We will confirm deletion within 30 days, subject to any legal-hold obligation.

---

## 14. Tracking-signal disclosure (DNT / GPC) {#tracking-signals}

**Milely does not track users across third-party websites or apps.** The App does not respond to **Do Not Track ("DNT")** or **Global Privacy Control ("GPC")** signals — there is no tracking to disable, and there is no third-party data sale or share for which an opt-out signal would be meaningful. The Company has no advertising business and operates no analytics pipeline.

The website at milely.io similarly performs no cross-site tracking. Any third-party signals received by the static-hosting provider (GitHub) or the font provider (Google) are handled per those providers' own policies.

---

## 15. Data retention {#retention}

Because Milely does not collect or store data on any Milely-controlled server, there is **no Milely-side data retention period** for App data. Your data is retained for as long as it remains on your device or in your chosen backup destination. When you delete the App from your device, all on-device data — trip records, photos, settings — is removed by iOS.

For inbound email, see § 13.

---

## 16. International data transfers {#international}

Milely does not operate any servers and does not transfer your App data to any country. Your data stays on your device unless you choose to back it up.

If you enable a third-party backup destination (e.g., iCloud, Google Drive), that provider may store your backup in data centers in any country. The transfer is between your device and the provider; Milely is not involved. Refer to your chosen provider's privacy policy for cross-border transfer details.

The website at milely.io is hosted on GitHub Pages, whose servers are located primarily in the United States; if you visit the website from outside the U.S., your visit involves a transfer of basic request metadata (IP, user-agent, path) to GitHub in the U.S., handled per GitHub's policies.

---

## 17. Security &amp; data breaches {#breach}

Because Milely does not operate any servers and does not collect data, there is **no central database for an attacker to breach**. The security of your trip data is governed by:

- **Your iPhone's security model.** iOS stores app data in a sandboxed, encrypted container. We strongly recommend enabling Face ID/Touch ID, a strong device passcode, and automatic iOS updates.
- **Your chosen backup provider's security.** If you enable iCloud Drive or a third-party Files provider, that provider's security and breach-notification practices apply to your backup files.

If we ever become aware of a security issue affecting the App that could place your data at risk, we will post a notice at this URL and (where practicable) flag it via an App Store update note. Because we do not maintain user contact information, we cannot send individual breach notifications. Optional security-notification email opt-in may be offered in the future; **no email collection is currently mandatory**, and we have no plans to make it mandatory.

---

## 18. Children's privacy {#children}

Milely is **not directed at, or intended for use by, children under 13** (or under 16 in jurisdictions where 16 is the applicable threshold under the Children's Online Privacy Protection Act, the GDPR, or comparable regulations). The App does not knowingly collect any information from children. If you believe a child has used the App and you'd like the App removed from their device, deleting the App from the device is sufficient — there is no Milely-side data to remove.

For the corresponding eligibility framework in the Terms of Service (including the Texas App Store Accountability Act readiness clause), see [Terms § 4 (Eligibility &amp; Age)](/terms/#eligibility).

---

## 19. U.S. state privacy rights {#us-state-rights}

This Section consolidates your rights under U.S. state privacy laws. The mechanism for invoking any of these rights is the same: email **milely@smileycreative.io** with a clear description of the right you want to exercise.

**Personal information we collect, sell, share, or process.** **None.** Milely does not collect, sell, share, or process personal information from you. The Company has no servers and operates no advertising or analytics business. Inbound email at milely@smileycreative.io is handled per § 13. The website's hosting log (per § 12) is not aggregated or accessed by us.

**19.1 Texas — TDPSA.** The **Texas Data Privacy and Security Act** ("TDPSA"), effective July 1, 2024, applies to SmileyCreative LLC as a Texas-resident business. Texas residents have the right to (a) confirm whether the Company processes their personal data, (b) access and obtain a copy of that personal data, (c) correct inaccuracies, (d) delete personal data, (e) obtain a portable copy of personal data, and (f) opt out of the processing of personal data for the purposes of (i) targeted advertising, (ii) the sale of personal data, or (iii) profiling in furtherance of a decision that produces a legal or similarly significant effect. Because the Company does not collect or process Texas residents' personal data within the meaning of the TDPSA — see § 5 (Location data) and § 13 (Inbound email handling) for the limits of what we touch — most of these rights are non-applicable in practice. **The Company does not engage in targeted advertising, the sale of personal data, or profiling**, so opt-outs in those categories are not applicable.

**19.2 California — CCPA / CPRA / Shine the Light / § 1798.83.** California residents have the rights to know, delete, correct, opt out of sale or sharing, limit use of sensitive personal information, designate an authorized agent, and exercise non-discrimination, under the California Consumer Privacy Act of 2018 as amended by the California Privacy Rights Act. **None of these are applicable in any operative sense, because the Company collects, sells, shares, and uses no personal information.** The Company does not respond to "Do Not Sell or Share My Personal Information" links because there is no sale or share to opt out of (see § 14). The Shine the Light Law (Cal. Civ. Code § 1798.83) does not apply for the same reason. For the California consumer-rights notice required by Cal. Civ. Code § 1789.3 specifically directed to App users, see [Terms § 29](/terms/#california-notice).

**19.3 Other comprehensive state privacy laws.** Comprehensive consumer-privacy laws in **Virginia (VCDPA), Colorado (CPA), Connecticut (CTDPA), Utah (UCPA), Iowa (ICDPA), Indiana (INCDPA), Tennessee (TIPA), Montana (MCDPA), Oregon (OCPA), Florida (FDBR), Delaware (DPDPA), New Hampshire (NHDPA), New Jersey (NJDPA), Kentucky (KCDPA), Maryland (MODPA), Minnesota (MCDPA), Rhode Island (RIDPPA)**, and similar laws each grant residents of those states broadly equivalent rights — **access, deletion, correction, portability, and opt-outs of sale, targeted advertising, and certain profiling**. **Because the Company collects, sells, shares, and processes no personal data from any user**, all such rights resolve to the same outcome as in Texas and California: there is nothing to deliver, delete, correct, port, or opt out of. We will, on request, confirm in writing that the Company maintains no personal data on the requester.

**19.4 How to make a request.** Email **milely@smileycreative.io**. Identify the law and the right you want to invoke, and provide enough information for us to identify the email thread. Because we have no records linked to your identity, identity verification is necessarily based on the email address from which the request is sent — see § 22.4 below. We will respond within the deadline specified by the applicable state law (typically 45 to 60 days, with a permissible extension where the law allows).

**19.5 Authorized agent.** You may designate an authorized agent. We may verify the agent's authority by requesting a signed permission letter or comparable evidence; because we have no personal records, agent-mediated requests resolve to the same outcomes as user-direct requests.

**19.6 Non-discrimination.** The Company does not offer financial incentives in exchange for personal information, and does not discriminate against any user for exercising any privacy right under any state law.

---

## 20. European Economic Area, United Kingdom, and Switzerland (GDPR) {#europe}

If you are in the European Economic Area, the United Kingdom, or Switzerland, the General Data Protection Regulation ("**GDPR**") and corresponding U.K. and Swiss laws grant you rights regarding your personal data.

**Controller.** SmileyCreative LLC, Texas, U.S.A. is the data controller for the limited personal data the App handles. Because we have no servers and collect no personal data, our controller obligations are minimal in practice. We have not designated a Data Protection Officer because we are not required to under Article 37 of the GDPR.

<div class="legal-note" markdown="1">
**EU/UK Representative (Article 27 GDPR / Article 27 UK GDPR).** Because the App processes data exclusively on the user's own device and SmileyCreative LLC does not collect, transmit, or store personal data on its own infrastructure, SmileyCreative LLC has not designated a representative under Article 27 of the GDPR or UK GDPR. SmileyCreative LLC does not direct marketing activities at the European Union or the United Kingdom. EU and UK residents who wish to exercise rights under the GDPR or UK GDPR may contact the Company directly at **milely@smileycreative.io** and the Company will respond within the one-month period contemplated by Article 12(3) of the GDPR. Should SmileyCreative LLC commence regular monitoring of EU or UK residents or active marketing into those jurisdictions, an Article 27 representative will be designated and the representative's name, postal address, and contact email will be inserted here at that time.
</div>

**Lawful basis for processing.** Where the App processes data on your device, the lawful basis differs by category:

- **Performance of a contract (GDPR Art. 6(1)(b)).** The App's *core* trip-tracking function — recording trips, computing miles, generating reports — is essential to delivering the service you've installed the App for. **Location processing is a contractual necessity for trip tracking; if you revoke location permission, the App cannot perform.**
- **Consent (GDPR Art. 6(1)(a) and Art. 9(2)(a) for any sensitive-category processing).** *Optional* features — Calendar Suggestions, photo/camera-based receipt scanning, and any biometric-style processing — operate only with your iOS-level consent (granted via the iOS permission prompts). You may withdraw consent at any time via iOS Settings or by toggling the feature off in-App. Withdrawal does not affect the lawfulness of processing prior to the withdrawal.
- **Legitimate interest (GDPR Art. 6(1)(f)).** The Company relies on legitimate-interest only for narrow, defensive purposes — for example, retaining email correspondence (per § 13) for up to 24 months to resolve a future dispute, or investigating a credible security report. The Company's legitimate interest is balanced against your privacy interests, which are protected by our overall no-collection architecture.

**Your rights.** You have the right to:

- Access the personal data being processed (open the App; everything is visible inside it);
- Have inaccurate data rectified (edit in the App);
- Have data erased (delete the App from your device);
- Restrict processing (revoke iOS permissions);
- Data portability (export via Settings → Manual Export);
- Object to processing (revoke iOS permissions, delete the App);
- Withdraw consent (see § 21);
- Lodge a complaint with your local data-protection authority.

We do not engage in automated decision-making or profiling.

**International transfers.** As described in § 16, Milely itself transfers no App data internationally. If you choose a third-party backup destination (e.g., Google Drive), that provider's lawful-transfer mechanism (such as Standard Contractual Clauses) governs the transfer.

---

## 21. Withdrawing consent {#withdraw}

You can withdraw any consent you've previously given the App, at any time:

- Revoke any iOS permission (Location, Motion, Calendars, Camera, Photos, Notifications) in Settings → Privacy &amp; Security.
- Disable any backup option in Settings → Backup.
- Delete the App from your device, which removes all on-device data and revokes all consents simultaneously.

Withdrawing consent does not affect the lawfulness of processing that occurred before the withdrawal.

---

## 22. Exercising your rights {#rights}

Because Milely stores data only on your device, most rights are exercisable directly inside the App without contacting us:

- **22.1 Access / view.** Open the App — all your data is fully visible.
- **22.2 Correct.** Edit any record inside the App.
- **22.3 Export.** Settings → Manual Export → share the JSON or CSV file via the iOS share sheet.
- **22.4 Delete.** Delete the App from your iPhone or use Settings → Reset to wipe local data.

**Identity verification for rights requests.** If you contact us at **milely@smileycreative.io** to invoke a right under the CCPA, CPRA, TDPSA, GDPR, or any other privacy law, please understand that **the Company holds no server-side records that could verify your identity**. Identity verification is therefore necessarily a *best-efforts* exercise based on (a) the email address from which the request is sent and (b) any descriptive context you can provide about a prior support thread. We will not require you to provide additional sensitive information, such as a government ID, simply to verify a request that — given our no-collection architecture — would resolve to "we hold nothing about you" in any event. Where applicable law permits, we will respond within 30 days (or longer where a permitted extension applies), at no charge unless the request is excessive or repetitive.

---

## 23. Changes to this policy {#changes}

If this policy changes, the updated version will be posted at this URL with a new "Last updated" date. Material changes will be flagged in-app where practicable and (for residents of jurisdictions that require advance notice) at least 30 days before they take effect. Your continued use of the App after the effective date constitutes acceptance of the revised policy.

---

## 24. Contact {#contact}

Questions about this policy, requests under CCPA, GDPR, TDPSA, or similar laws, or any other privacy concern:

**SmileyCreative LLC**  
Attn: Milely Privacy  
**milely@smileycreative.io**

---

*Milely is published by SmileyCreative LLC, a Texas limited liability company. © 2026 SmileyCreative LLC. All rights reserved.*

</main>
