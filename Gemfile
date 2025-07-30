source "https://rubygems.org"

# Jekyll core
gem "jekyll", "~> 4.3.0"

# Essential Jekyll plugins for performance and SEO
group :jekyll_plugins do
  # Core functionality
  gem "jekyll-sitemap"           # XML sitemap generation
  gem "jekyll-seo-tag"          # SEO meta tags
  gem "jekyll-feed"             # RSS/Atom feeds
  
  # Performance optimization plugins
  gem "jekyll-minifier"         # HTML/CSS/JS minification
  gem "jekyll-compress-images"  # Image compression
  gem "jekyll-responsive-image" # Responsive images
  gem "jekyll-gzip"            # Gzip compression
  
  # Content management
  gem "jekyll-paginate-v2"     # Advanced pagination
  gem "jekyll-archives"        # Category/tag archives
  gem "jekyll-redirect-from"   # URL redirects
  gem "jekyll-last-modified-at" # Last modified dates
  
  # Development and analytics
  gem "jekyll-analytics"       # Analytics integration
  gem "jekyll-timeago"        # Time ago filter
  gem "jekyll-toc"           # Table of contents
end

# Platform-specific gems
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo", ">= 1", "< 3"
  gem "tzinfo-data"
end

# Performance monitoring (development)
group :development do
  gem "jekyll-admin"          # Admin interface
  gem "jekyll-livereload"     # Live reload during development
end

# Windows-specific gems
gem "wdm", "~> 0.1.1", :platforms => [:mingw, :x64_mingw, :mswin]

# HTTP parser for better performance
gem "http_parser.rb", "~> 0.6.0", :platforms => [:jruby]