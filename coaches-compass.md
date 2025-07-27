---
layout: default
title: "The Coach's Compass - Free | 5-Minute Team Diagnostic"
description: "Get the free 5-minute team diagnostic that identifies your team's biggest weakness and the exact training focus that fixes it. Used by 1200+ coaches worldwide."
keywords: [football team diagnostic, free coaching tool, team analysis, coaching problems, youth football development, Kevin Middleton, 360TFT, coaching assessment]
seo_title: "Free Football Team Diagnostic | The Coach's Compass | 360TFT"

# Product-specific meta
product_name: "The Coach's Compass"
product_price: "FREE"
product_tagline: "5-Minute Team Diagnostic"
product_badge: "🆓 Completely Free"

# Open Graph
og_type: product
og_title: "The Coach's Compass - Free 5-Minute Team Diagnostic"
og_description: "Identify your team's biggest weakness and get the exact training focus that fixes it. Completely free."
og_image: "/assets/images/coaches-compass-free.jpg"

# Twitter
twitter_title: "Free Football Team Diagnostic - The Coach's Compass"
twitter_description: "5-minute diagnostic identifies your team's biggest weakness. Completely free from 360TFT."
twitter_image: "/assets/images/coaches-compass-free.jpg"

# Page-specific CSS/JS
css: [
  "/assets/css/product-pages.css", 
  "/assets/css/free-product.css",
  "/assets/css/components/images.css",
  "/assets/css/components/authority-section.css"
]
js: ["/assets/js/free-product-tracking.js"]
body_class: "compass-page free-product"

# Product data
product_type: "free_diagnostic"
gumroad_url: "https://kev1wired.gumroad.com/l/TheCoachCompass?wanted=true"
schema_type: "Product"
---

<!-- Hero Section -->
<section class="hero free-hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-badge">{{ page.product_badge }}</div>
            <h1>Most Football Coaches Guess What's Wrong With Their Team.</h1>
            <h2 class="hero-subtitle">Successful Coaches Know Exactly Where To Start.</h2>
            <p class="hero-description">Get The 5-Minute Team Diagnostic That Identifies Your Team's Biggest Weakness (And The Exact Training Focus That Fixes It)</p>
            
            <div class="value-proposition">
                <h3>Here's what separates coaches who get results from coaches who get frustrated:</h3>
                <p><strong>Results-driven coaches diagnose before they prescribe.</strong></p>
                <p>They don't waste time running random exercises hoping something works. They identify the specific problem, apply the targeted solution, and watch their team transform.</p>
            </div>
            
            <div class="hero-cta-group">
                <a href="{{ page.gumroad_url }}" class="hero-cta-secondary">Get Your Free Team Diagnostic Now</a>
                <p class="hero-guarantee">✅ Completely Free • ✅ Instant Access • ✅ No Email Required</p>
            </div>
        </div>
    </div>
</section>

<!-- Authority Section -->
<section class="authority-section">
    <div class="container">
        <div class="authority-content">
            <div class="kevin-info">
                <img src="{{ '/assets/images/kevin-middleton-coach.jpg' | relative_url }}" 
                     alt="Kevin Middleton - Football Coach with 15+ years experience"
                     loading="lazy">
            </div>
            <div class="kevin-credentials">
                <h3>Meet Your Coach</h3>
                <p><strong>Kevin Middleton</strong> has {{ site.site_constants.years_experience }} years of coaching experience and has helped {{ site.site_constants.coaches_mentored }} coaches in the Football Coaching Academy community develop better players at every level.</p>
                
                <p>Kevin's diagnostic approach has been tested with grassroots teams through to professional academies. His systematic methodology helps coaches identify problems faster and implement solutions that actually work.</p>
                
                <div class="stats-grid">
                    <div class="stat-item">
                        <span class="stat-number">{{ site.site_constants.years_experience }}+</span>
                        <span class="stat-text">Years Experience</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">{{ site.site_constants.coaches_mentored }}+</span>
                        <span class="stat-text">Coaches Helped</span>
                    </div>
                    <div class="stat-item">
                        <span class="stat-number">Professional</span>
                        <span class="stat-text">Level Approved</span>
                    </div>
                </div>
                
                <div class="authority-links">
                    <a href="https://x.com/coach_kevin_m" target="_blank" rel="noopener" class="social-link">
                        Follow on Twitter
                    </a>
                    <a href="https://www.skool.com/coachingacademy" target="_blank" rel="noopener" class="academy-link">
                        Join Academy
                    </a>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- Schema Markup -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{{ page.product_name }}",
    "description": "{{ page.description }}",
    "brand": {
        "@type": "Brand",
        "name": "{{ site.title }}"
    },
    "offers": {
        "@type": "Offer",
        "price": "0",
        "priceCurrency": "GBP",
        "availability": "https://schema.org/InStock",
        "seller": {
            "@type": "Organization",
            "name": "{{ site.title }}"
        }
    },
    "creator": {
        "@type": "Person",
        "name": "{{ site.author.name }}",
        "jobTitle": "Football Coach",
        "description": "Football coach with {{ site.site_constants.years_experience }} years experience"
    },
    "category": "Sports Coaching Tools",
    "keywords": "{{ page.keywords | join: ', ' }}"
}
</script>