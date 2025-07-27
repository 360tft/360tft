---
layout: default
title: "Transform Average Players Into Match-Winners"
description: "Join 1000+ coaches using the 360TFT Game Model. Access 328 ready-to-use training sessions, expert coaching guidance, and proven player development systems from Kevin Middleton."
keywords: [football coaching, soccer training sessions, youth football coaching, coaching courses, player development, Kevin Middleton, 360TFT, football coaching academy]
seo_title: "360TFT - Transform Average Players Into Match-Winners | Football Coaching Academy"
og_title: "360TFT - Transform Average Players Into Match-Winners"
og_description: "Join 1000+ coaches using proven player development systems. 15+ years of coaching expertise in one place."
og_image: "/assets/images/360tft-social-share.jpg"
body_class: "homepage"
css:
  - "/assets/css/homepage-animations.css"
js:
  - "/assets/js/homepage-interactions.js"
---

<!-- Hero Section -->
<section class="hero">
    <div class="container">
        <div class="hero-content">
            <div class="hero-badge">🏆 Trusted by {{ site.site_constants.coaches_mentored }} Coaches Worldwide</div>
            <h1>{{ page.title }}</h1>
            <p class="hero-subtitle">With The Proven 360TFT Game Model</p>
            <p class="hero-description">Join the coaching revolution that's helping youth players develop faster, perform better, and love the game more. {{ site.site_constants.sessions_created }} ready-to-use sessions, expert guidance, and a thriving community of coaches who get results.</p>
            
            <div class="hero-cta-group">
                <a href="#free-resources" class="hero-cta">Get Free Sessions Now</a>
                <a href="https://www.skool.com/coachingacademy" class="hero-cta-secondary">Join The Academy</a>
            </div>
            
            <div class="social-proof">
                <strong>{{ site.site_constants.years_experience }} Years Experience</strong> • 
                <strong>{{ site.site_constants.players_developed }} Players Coached</strong> • 
                <strong>{{ site.site_constants.coaches_mentored }} Coaches Helped</strong>
            </div>
        </div>
    </div>
</section>

<!-- Authority Section -->
<section class="authority" id="about">
    <div class="container">
        <div class="authority-content">
            <div>
                <img class="kevin-photo" src="{{ '/assets/images/kevin-middleton-coach.jpg' | relative_url }}" alt="Kevin Middleton - Football Coach">
            </div>
            <div class="authority-text">
                <h2>Meet {{ site.author.name }}</h2>
                <p>After {{ site.site_constants.years_experience }} years of coaching at every level, I've cracked the code on what actually develops players. Not just drills that look good, but systems that create confident, capable footballers who perform when it matters.</p>
                
                <p>My journey began with failure. Fresh-faced and eager, I thought coaching was about knowing more drills than the next person. I was wrong. My first season coaching an U12 team was humbling - despite endless energy and what I thought were great sessions, the players weren't improving.</p>
                
                <p>That failure became my foundation. The result? The 360TFT Game Model - a systematic approach to developing complete players.</p>
            </div>
        </div>
    </div>
</section>

<!-- Testimonials Section -->
<section class="testimonials" id="testimonials">
    <div class="container">
        <h2>What Real Players & Coaches Say</h2>
        
        <div class="testimonials-grid">
            {% for testimonial in site.data.testimonials_real.professional_players %}
            <div class="testimonial-card">
                <div class="testimonial-header">
                    <h4>{{ testimonial.name }}</h4>
                    <p>{{ testimonial.club }}</p>
                    <span class="pro-badge">{{ testimonial.badge }}</span>
                </div>
                <blockquote>{{ testimonial.quote }}</blockquote>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Products Section -->
<section class="products" id="products">
    <div class="container">
        <h2>From Individual Sessions to Complete Systems</h2>
        <p>Choose what fits your needs</p>
        
        <div class="products-grid">
            {% for product in site.data.products.main_products %}
            <div class="product-card">
                <div class="product-icon">{{ product.icon }}</div>
                <h3>{{ product.name }}</h3>
                <p class="product-price">{{ product.price }}</p>
                <p>{{ product.description }}</p>
                <a href="#" class="product-cta">Learn More</a>
            </div>
            {% endfor %}
        </div>
    </div>
</section>

<!-- Free Resources Section -->
<section class="free-resources" id="free-resources">
    <div class="container">
        <h2>Start Your Coaching Transformation Today</h2>
        
        <div class="resources-grid">
            <div class="resource-card">
                <h3>The 5-Minute Team Diagnostic</h3>
                <p>Identify your team's exact weaknesses and get targeted solutions.</p>
                <a href="https://360tft.github.io/The-5-Minute-Team-Diagnostic/" class="resource-cta">Take The Diagnostic</a>
            </div>
            
            <div class="resource-card">
                <h3>Emergency Session Plans</h3>
                <p>Quick fixes for immediate coaching challenges.</p>
                <a href="https://360tft.github.io/Emergency-Session-Plans/" class="resource-cta">Get Emergency Sessions</a>
            </div>
        </div>
    </div>
</section>