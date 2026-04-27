# Milely Website (milely.io)

Static website for Milely. Hosted free on **GitHub Pages**, served from `milely.io` via DNS pointed at GitHub.

## What's here

```
website/
├── _config.yml           Jekyll config (built into GitHub Pages)
├── _layouts/default.html Brand-styled layout (browns + burnt orange + warm yellow gradient, Space Grotesk + Inter)
├── CNAME                 Custom domain config (contains "milely.io")
├── index.html            Landing page
├── privacy/index.md      Privacy policy
├── terms/index.md        Terms of service
├── support/index.md      Support / FAQ / contact
├── help/index.md         How-to guide
└── assets/
    ├── icon.png          The Milely M-as-road icon (1024×1024)
    └── og-image.png      Open Graph preview image
```

## Cost

**$0/month** after the milely.io domain you already paid for. GitHub Pages is free for public repos.

## Deploy in 3 steps

### 1. Create the GitHub repo

```bash
# From your machine, with a GitHub account signed in:
gh repo create milely-llc/milely-llc.github.io --public
```

Or via the web: github.com → New repository → name **`milely-llc.github.io`** (or anything else — see Step 2 if you pick a different name) under an org or your own account.

### 2. Push the website

```bash
cd /Users/gregphuh/Claude/Milely/website
git init
git add .
git commit -m "Initial Milely website"
git branch -M main
git remote add origin git@github.com:milely-llc/milely-llc.github.io.git
git push -u origin main
```

If you used a different repo name (not `<user>.github.io` style), enable GitHub Pages in repo Settings → Pages → Source: `main` branch, `/` (root) folder.

### 3. Point milely.io DNS at GitHub Pages (GoDaddy)

In your GoDaddy account → **My Products → Domains → milely.io → DNS**:

**a. Apex domain (`milely.io`)** — add 4 A records pointing to GitHub Pages:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| A | @ | `185.199.108.153` | 1 hour |
| A | @ | `185.199.109.153` | 1 hour |
| A | @ | `185.199.110.153` | 1 hour |
| A | @ | `185.199.111.153` | 1 hour |

**b. www subdomain** — add a CNAME:

| Type | Name | Value | TTL |
|------|------|-------|-----|
| CNAME | www | `milely-llc.github.io` (or whatever your repo URL is, e.g. `<user>.github.io`) | 1 hour |

**c. In GitHub repo Settings → Pages:**
- Custom domain: `milely.io`
- Click **Save**
- Check ✅ **Enforce HTTPS** (may take 24h to provision the SSL cert — wait until you can check it)

**Verification:** GitHub will validate the DNS automatically. Once green checkmarks appear, milely.io serves the site.

DNS changes can take up to 24 hours to propagate worldwide; usually it's 5-30 minutes.

---

## Update the site later

```bash
cd /Users/gregphuh/Claude/Milely/website
# edit any .md or .html file
git add .
git commit -m "Update privacy policy"
git push
```

Live in 30-60 seconds (GitHub Pages rebuilds automatically).

---

## Local preview (optional)

Install Jekyll once:
```bash
gem install bundler jekyll
```

Then preview:
```bash
cd website
bundle init
echo 'gem "jekyll"' >> Gemfile
echo 'gem "jekyll-feed"' >> Gemfile
echo 'gem "jekyll-seo-tag"' >> Gemfile
bundle install
bundle exec jekyll serve
# open http://localhost:4000
```

You don't have to do this — GitHub will build and serve the live site once you push.

---

## After milely.io is live

1. **Update `Milely/Views/Settings/SettingsView.swift`** — replace the placeholder URLs:
   - `https://example.com/milely-privacy` → `https://milely.io/privacy/`
   - `https://example.com/milely-terms` → `https://milely.io/terms/`
2. **Update `appstore/04-LISTING-COPY.md`** — Support URL = `https://milely.io/support/`, Privacy URL = `https://milely.io/privacy/`, Marketing URL = `https://milely.io/`
3. **Update Apple's `privacy-policy.md`** in the repo root — already mostly current, but you can delete it if you want one source of truth at the website
4. **Set up email** at the milely.io domain for `support@`, `privacy@`, `legal@`, `security@`. GoDaddy offers Microsoft 365 mailboxes (~$6/mo each) or you can use Cloudflare Email Routing (free, forwards to your existing inbox) — recommended.
