# milely.io — Security configuration

This document describes the security posture of milely.io and the operator-side steps to maintain it. The site itself is a static Jekyll build deployed to GitHub Pages; the source-side hardening (CSP, self-hosted fonts, no third-party scripts) is committed in this repo. The HTTP-header layer below has to be configured in Cloudflare.

## Current source-side posture (committed)

| Surface | State |
|---|---|
| External JS | None loaded. Zero `<script src="https://…">` tags. |
| Inline JS | Only `<script type="application/ld+json">` blocks (data, not executable). |
| Iframes | None. |
| Forms | None. No user input surface. |
| External fonts | None. Inter / Space Grotesk / Fraunces self-hosted under `/assets/fonts/`. |
| Mixed content | None. Only `http://` reference is the W3C SVG namespace identifier (`http://www.w3.org/2000/svg`), which is required and never fetched. |
| External link safety | Every `<a href="https://…">` to a third-party host has `rel="noopener noreferrer"`. |
| TLS | Let's Encrypt R12, valid through 2026-07-26 (auto-renewed by GitHub Pages). |
| CSP (meta tag) | `default-src 'self'; style-src 'self' 'unsafe-inline'; font-src 'self' data:; img-src 'self' data:; script-src 'self'; connect-src 'self'; frame-src 'none'; child-src 'none'; base-uri 'self'; form-action 'none'; object-src 'none'` |
| Secrets | None in source or git history (verified by `grep` against common secret patterns + `git log` audit). |

## Cloudflare configuration (operator action — dashboard)

milely.io's DNS A/AAAA record currently resolves directly to GitHub Pages (`185.199.108-111.153`), which means Cloudflare is in **DNS only** mode (gray cloud). To enable Cloudflare's WAF / DDoS / cache / and HTTP-header injection, switch to **Proxied** (orange cloud).

### Step 1 — flip to proxied

1. Cloudflare dashboard → milely.io → DNS → Records
2. Find the A records pointing at `185.199.108-111.153`
3. Click the gray cloud icon on each row to switch to orange (proxied)
4. Save

Verify with:
```bash
curl -sI https://milely.io/ | grep -i 'cf-ray\|server'
```
Should show `cf-ray:` header and `server: cloudflare`. Until that's true, none of the steps below take effect.

### Step 2 — SSL/TLS settings

1. SSL/TLS → Overview
2. Encryption mode = **Full (strict)** — verifies the GitHub Pages origin certificate
3. SSL/TLS → Edge Certificates
4. Always Use HTTPS = **On**
5. Minimum TLS Version = **TLS 1.2** (1.3 if available)
6. Opportunistic Encryption = **On**
7. TLS 1.3 = **On**
8. Automatic HTTPS Rewrites = **On**

### Step 3 — Add HTTP security headers via Transform Rules

Cloudflare dashboard → Rules → Transform Rules → Modify Response Header → Create rule.

**Rule name**: `Add baseline security headers`
**When incoming requests match**: `(http.host eq "milely.io")` (or just leave empty to match all)
**Then…** Set static response headers:

| Header name | Value |
|---|---|
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains; preload` |
| `X-Frame-Options` | `DENY` |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), interest-cohort=(), payment=(), usb=(), accelerometer=(), gyroscope=(), magnetometer=()` |

Save and deploy. Verify with:
```bash
curl -sI https://milely.io/ | grep -iE 'strict-transport|x-frame|x-content-type|referrer-policy|permissions-policy'
```

#### Roll out HSTS carefully

Initial deployment: **start with `max-age=300`** (5 min) for the first day. Watch traffic. If HTTPS works for everyone, bump to `max-age=86400` (1 day) for a week, then `max-age=63072000; includeSubDomains; preload` (2 years) once you're confident no subdomain needs HTTP.

`includeSubDomains` is irreversible from the user's browser cache for the max-age duration — make sure no `*.milely.io` subdomain ever needs to serve plain HTTP before adding it. Currently milely.io has no subdomains, so this is safe.

After 6+ months at the long max-age, submit https://milely.io to https://hstspreload.org for browser-vendor-baked HSTS.

### Step 4 — Bot protection + WAF

1. Security → Bots → Bot Fight Mode = **On** (free tier)
2. Security → WAF → Managed Rules
   - Cloudflare Managed Ruleset = **On**
   - Cloudflare OWASP Core Ruleset = **On** (paranoia level Low for a static site)
3. Security → DDoS → leave at default (auto-mitigated)

### Step 5 — Rate limiting (optional, free tier)

If anyone starts hammering the site:
1. Security → WAF → Rate limiting rules → Create rule
2. **Rule**: more than `100` requests per `10` seconds from a single IP → block for `10 minutes`
3. Apply to all paths

Marketing site traffic should never hit this. If it does, you have either a bot problem or a viral moment — either way you'll want the data.

### Step 6 — Email obfuscation

Security → Settings → Scrape Shield → Email Address Obfuscation = **On**. This rewrites every `mailto:` link in the HTML on-the-fly so spam harvesters see scrambled JS instead of `milely@smileycreative.io`.

### Step 7 — Caching

Caching → Configuration:
- Caching Level = **Standard**
- Browser Cache TTL = **4 hours** (or **Respect Existing Headers** if you'd rather GH Pages's `cache-control: max-age=600` win)
- Always Online = **On** (serves a cached copy if GH Pages is unreachable)

For images specifically, consider a Page Rule: `milely.io/assets/screenshots/*` → Edge Cache TTL = 1 month. Saves on the bandwidth back to GH Pages.

## Verification checklist (post-flip)

```bash
# 1. Cloudflare is in the path
curl -sI https://milely.io/ | grep -i 'cf-ray\|server: cloudflare'

# 2. HSTS present
curl -sI https://milely.io/ | grep -i 'strict-transport-security'

# 3. Other security headers present
curl -sI https://milely.io/ | grep -iE 'x-frame|x-content-type|referrer-policy|permissions-policy'

# 4. CSP meta tag is the source-side fallback (still in HTML)
curl -s https://milely.io/ | grep -i 'content-security-policy'

# 5. No Google Fonts requests
curl -s https://milely.io/ | grep -i 'fonts.googleapis\|fonts.gstatic'
# (should return nothing)

# 6. Local fonts load
curl -sI https://milely.io/assets/fonts/fonts.css

# 7. JSON-LD references the right screenshot
curl -s https://milely.io/ | grep -o 'hero-[0-9]-pdf.png'
# (should print "hero-6-pdf.png")
```

## On rotation

- **TLS cert auto-renewal**: GitHub Pages handles Let's Encrypt renewal. If `notAfter` ever shows < 30 days remaining, that's a regression worth chasing.
- **`github-pages` gem**: run `bundle update github-pages` quarterly to pick up Jekyll + plugin security patches.
- **Cloudflare dashboard audit**: every 6 months, review WAF rule firings + check for any new third-party scripts that snuck in.
- **HSTS preload**: once stable for 6+ months, submit to https://hstspreload.org.

## Items NOT addressed yet (low-priority residue)

- **App Store ID placeholder** — every "Try free for 7 days" CTA still goes to `id__APPSTORE_ID_PENDING__`. Not security; launch-blocker.
- **CSP report-uri** — no violation reporting endpoint. Once Cloudflare is proxying you can use the free `report-uri.com` tier; meanwhile silent.
