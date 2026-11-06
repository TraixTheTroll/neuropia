source 'https://rubygems.org'

gem 'jekyll', '~> 4.4'

# Plugins used by Neuropia's custom pages and bibliography.
group :jekyll_plugins do
  gem 'jekyll-link-attributes'
  gem 'jekyll-minifier'
  gem 'jekyll-scholar'
  gem 'jekyll-sitemap'
  gem 'jekyll-terser', git: 'https://github.com/RobertoJBeltran/jekyll-terser.git'
end

# Explicit because observer is no longer bundled with recent Ruby releases.
gem 'observer'
# jekyll-link-attributes requires Nokogiri without declaring it as a dependency.
gem 'nokogiri'

group :al_folio_plugins do
  gem 'al_folio_core', '= 1.0.15'
  gem 'al_folio_upgrade', '= 1.0.3'
end
