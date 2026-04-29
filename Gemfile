source "https://rubygems.org"

# GitHub Pages gem — pins Jekyll + every supported plugin to the exact
# versions GitHub Pages runs in production. Run `bundle update github-pages`
# periodically to stay in sync; see https://pages.github.com/versions/ for
# the version matrix.
gem "github-pages", group: :jekyll_plugins

# Plugins explicitly enabled in _config.yml. Listed here so a plain
# `bundle install` pulls everything needed for `bundle exec jekyll serve`.
group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-seo-tag"
  gem "jekyll-sitemap"
  gem "jekyll-redirect-from"
end

# Windows + JRuby compatibility shims. Harmless on macOS, required for
# Windows contributors who try to clone + serve locally.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# Ruby 3.x dropped webrick from stdlib; Jekyll's local server needs it back.
gem "webrick", "~> 1.8"
