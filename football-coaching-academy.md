---
layout: default
title: "Football Coaching Academy | Join {{ site.site_constants.community_size }} Elite Coaches Worldwide"
description: "Join the exclusive Football Coaching Academy for just {{ site.pricing.academy.current_monthly }}. Monthly masterclasses with Kevin Middleton, elite coaching network, cutting-edge resources, and direct mentorship. Transform your coaching career."
keywords: [football coaching academy, coaching education, football coach training, coaching certification, coaching mentorship, Kevin Middleton academy, 360TFT academy, coaching community]
seo_title: "Football Coaching Academy | Join {{ site.site_constants.community_size }} Elite Coaches | {{ site.pricing.academy.current_monthly }} | 360TFT"

# Open Graph
og_title: "Football Coaching Academy - Join {{ site.site_constants.community_size }} Elite Coaches Worldwide"
og_description: "Exclusive coaching education community for just {{ site.pricing.academy.current_monthly }}. Monthly masterclasses, direct mentorship, and advanced resources for serious coaches."
og_image: "/assets/images/academy-preview.jpg"

# Twitter
twitter_title: "Football Coaching Academy - Join 1200+ Elite Coaches"
twitter_description: "Exclusive coaching education community for just $10/month. Monthly masterclasses, direct mentorship, and advanced resources."
twitter_image: "/assets/images/academy-preview.jpg"

# Page-specific settings
css: ["/assets/css/product-pages.css", "/assets/css/academy-specific.css"]
js: ["/assets/js/product-interactions.js", "/assets/js/academy-tracking.js"]
body_class: "academy-page"
schema_type: "Product"

# Product Information
product_name: "Football Coaching Academy"
product_price: "{{ site.pricing.academy.current_monthly }}"
original_price: "{{ site.pricing.academy.future_monthly }}"
annual_price: "{{ site.pricing.academy.current_yearly }}"
annual_savings: "Save 33%"
purchase_url: "{{ site.purchase_links.academy }}"
guarantee: "Cancel Anytime"
member_count: "{{ site.site_constants.community_size }}"
member_limit: "Limited to 500 new members"
---

<style>
/* Academy Page Styles */
.academy-hero {
    background: linear-gradient(135deg, #1a1a1a 0%, #2d1b4e 50%, #976bdd 100%);
    color: white;
    padding: 120px 0 100px;
    position: relative;
    overflow: hidden;
}

.academy-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><polygon points="50,5 95,95 5,95" fill="rgba(255,255,255,0.05)"/><circle cx="80" cy="20" r="3" fill="rgba(255,255,255,0.1)"/></svg>');
    opacity: 0.3;
}

.hero-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    text-align: center;
    position: relative;
    z-index: 2;
}

.exclusive-badge {
    background: linear-gradient(45deg, #ff5757, #ff8c42);
    color: white;
    padding: 15px 30px;
    border-radius: 25px;
    font-weight: 700;
    margin-bottom: 30px;
    display: inline-block;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 2px;
    box-shadow: 0 10px 30px rgba(255, 87, 87, 0.4);
    animation: glow 2s ease-in-out infinite alternate;
}

@keyframes glow {
    from { box-shadow: 0 10px 30px rgba(255, 87, 87, 0.4); }
    to { box-shadow: 0 15px 40px rgba(255, 87, 87, 0.7); }
}

.hero-content h1 {
    font-size: 3.8rem;
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.1;
    background: linear-gradient(45deg, #ffffff, #e0e0e0);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.hero-tagline {
    font-size: 1.6rem;
    color: #ff5757;
    margin-bottom: 30px;
    font-weight: 600;
    font-style: italic;
}

.hero-description {
    font-size: 1.3rem;
    line-height: 1.6;
    margin-bottom: 40px;
    color: rgba(255,255,255,0.9);
    max-width: 800px;
    margin-left: auto;
    margin-right: auto;
}

.member-stats {
    display: flex;
    justify-content: center;
    gap: 60px;
    margin: 50px 0;
    flex-wrap: wrap;
}

.stat-item {
    text-align: center;
}

.stat-number {
    display: block;
    font-size: 3rem;
    font-weight: 700;
    color: #ff5757;
    margin-bottom: 5px;
}

.stat-text {
    font-size: 1rem;
    color: rgba(255,255,255,0.8);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.pricing-preview {
    background: rgba(255,255,255,0.1);
    padding: 40px;
    border-radius: 20px;
    margin: 50px auto;
    max-width: 500px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
    position: relative;
}

.price-comparison {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 20px;
}

.original-price {
    font-size: 1.2rem;
    text-decoration: line-through;
    opacity: 0.7;
}

.current-price {
    font-size: 2.5rem;
    font-weight: 700;
    color: #ff5757;
}

.price-note {
    font-size: 1rem;
    color: rgba(255,255,255,0.8);
    margin-bottom: 20px;
}

.rising-price-warning {
    background: #ff5757;
    color: white;
    padding: 12px 20px;
    border-radius: 25px;
    font-weight: 600;
    font-size: 0.9rem;
    animation: pulse 2s infinite;
}

.hero-cta {
    margin-top: 40px;
}

.btn-academy {
    background: linear-gradient(45deg, #ff5757, #ff8c42);
    color: white;
    padding: 18px 40px;
    font-size: 1.2rem;
    font-weight: 600;
    border-radius: 30px;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s ease;
    box-shadow: 0 10px 30px rgba(255, 87, 87, 0.4);
    margin: 0 10px 10px 0;
    position: relative;
    overflow: hidden;
}

.btn-academy:before {
    content: '';
    position: absolute;
    top: 0;
    left: -100%;
    width: 100%;
    height: 100%;
    background: linear-gradient(90deg, transparent, rgba(255,255,255,0.3), transparent);
    transition: left 0.5s;
}

.btn-academy:hover:before {
    left: 100%;
}

.btn-academy:hover {
    transform: translateY(-3px);
    box-shadow: 0 15px 40px rgba(255, 87, 87, 0.6);
}

.btn-secondary {
    background: rgba(255,255,255,0.2);
    color: white;
    border: 2px solid rgba(255,255,255,0.3);
}

.btn-secondary:hover {
    background: rgba(255,255,255,0.3);
    border-color: rgba(255,255,255,0.5);
}

/* Exclusivity Section */
.exclusivity {
    padding: 100px 0;
    background: #1a1a1a;
    color: white;
}

.exclusivity-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 80px;
    align-items: center;
}

.exclusivity-text h2 {
    font-size: 2.8rem;
    color: #ff5757;
    margin-bottom: 30px;
    font-weight: 700;
}

.exclusivity-text p {
    font-size: 1.2rem;
    line-height: 1.7;
    color: rgba(255,255,255,0.9);
    margin-bottom: 25px;
}

.elite-features {
    list-style: none;
    padding: 0;
    margin: 30px 0;
}

.elite-features li {
    padding: 12px 0;
    font-size: 1.1rem;
    position: relative;
    padding-left: 30px;
    color: rgba(255,255,255,0.9);
}

.elite-features li:before {
    content: '🏆';
    position: absolute;
    left: 0;
    font-size: 1.2rem;
}

.exclusivity-visual {
    text-align: center;
}

.member-avatars {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 15px;
    margin-bottom: 30px;
}

.avatar {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: linear-gradient(45deg, #976bdd, #ff5757);
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: 700;
    color: white;
    border: 3px solid rgba(255,255,255,0.2);
}

.club-logos {
    display: flex;
    justify-content: center;
    gap: 20px;
    margin: 30px 0;
    flex-wrap: wrap;
}

.club-logo {
    background: rgba(255,255,255,0.1);
    padding: 15px 20px;
    border-radius: 10px;
    font-weight: 600;
    font-size: 0.9rem;
    color: rgba(255,255,255,0.8);
}

.member-limit {
    background: #ff5757;
    color: white;
    padding: 12px 25px;
    border-radius: 25px;
    font-weight: 600;
    display: inline-block;
    margin-top: 20px;
}

/* Benefits Section */
.benefits {
    padding: 100px 0;
    background: #f8f9fa;
}

.section-header {
    text-align: center;
    margin-bottom: 80px;
}

.section-header h2 {
    font-size: 2.8rem;
    color: #976bdd;
    margin-bottom: 20px;
    font-weight: 600;
}

.section-header p {
    font-size: 1.3rem;
    color: #666;
    max-width: 600px;
    margin: 0 auto;
}

.benefits-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 40px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.benefit-card {
    background: white;
    padding: 40px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
    border: 2px solid transparent;
    position: relative;
    overflow: hidden;
}

.benefit-card:before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    height: 5px;
    background: linear-gradient(45deg, #976bdd, #ff5757);
}

.benefit-card:hover {
    transform: translateY(-10px);
    border-color: #976bdd;
    box-shadow: 0 20px 50px rgba(151, 107, 221, 0.3);
}

.benefit-icon {
    font-size: 3rem;
    margin-bottom: 20px;
    background: linear-gradient(45deg, #976bdd, #ff5757);
    width: 80px;
    height: 80px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    color: white;
}

.benefit-card h3 {
    color: #333;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 15px;
}

.benefit-card p {
    color: #666;
    line-height: 1.6;
    margin-bottom: 25px;
}

.benefit-details {
    list-style: none;
    padding: 0;
    margin-bottom: 25px;
}

.benefit-details li {
    color: #555;
    padding: 8px 0;
    border-bottom: 1px solid #eee;
    position: relative;
    padding-left: 25px;
}

.benefit-details li:before {
    content: '✓';
    color: #976bdd;
    font-weight: bold;
    position: absolute;
    left: 0;
}

.benefit-value {
    background: linear-gradient(45deg, #976bdd, #ff5757);
    color: white;
    padding: 12px 25px;
    border-radius: 25px;
    text-align: center;
    font-weight: 600;
    font-size: 0.9rem;
}

/* Success Stories */
.success-stories {
    padding: 100px 0;
    background: white;
}

.stories-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 40px;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

.story-card {
    background: #f8f9fa;
    padding: 40px;
    border-radius: 20px;
    border-left: 5px solid #976bdd;
    position: relative;
    transition: all 0.3s ease;
}

.story-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(151, 107, 221, 0.2);
}

.story-card::before {
    content: '"';
    font-size: 4rem;
    color: #976bdd;
    position: absolute;
    top: 10px;
    left: 20px;
    opacity: 0.3;
}

.story-text {
    font-size: 1.1rem;
    line-height: 1.6;
    color: #444;
    margin-bottom: 25px;
    font-style: italic;
}

.story-author {
    font-weight: 600;
    color: #976bdd;
    margin-bottom: 5px;
}

.story-role {
    color: #666;
    font-size: 0.9rem;
    margin-bottom: 10px;
}

.story-result {
    background: #976bdd;
    color: white;
    padding: 8px 15px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 600;
    display: inline-block;
}

/* Pricing Section */
.pricing {
    padding: 100px 0;
    background: linear-gradient(135deg, #1a1a1a 0%, #2d1b4e 100%);
    color: white;
    text-align: center;
}

.pricing h2 {
    font-size: 2.8rem;
    margin-bottom: 20px;
    font-weight: 600;
}

.pricing-subtitle {
    font-size: 1.3rem;
    color: rgba(255,255,255,0.8);
    margin-bottom: 60px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
}

.pricing-options {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 40px;
    max-width: 800px;
    margin: 0 auto;
    padding: 0 20px;
}

.pricing-card {
    background: rgba(255,255,255,0.1);
    padding: 40px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    border: 2px solid rgba(255,255,255,0.2);
    transition: all 0.3s ease;
    position: relative;
}

.pricing-card.featured {
    border-color: #ff5757;
    transform: scale(1.05);
    background: rgba(255,255,255,0.15);
}

.pricing-card.featured:before {
    content: 'MOST POPULAR';
    position: absolute;
    top: -15px;
    left: 50%;
    transform: translateX(-50%);
    background: #ff5757;
    color: white;
    padding: 8px 20px;
    border-radius: 15px;
    font-size: 0.8rem;
    font-weight: 700;
}

.pricing-card:hover {
    transform: translateY(-10px);
    border-color: #ff5757;
}

.plan-name {
    font-size: 1.3rem;
    font-weight: 600;
    margin-bottom: 15px;
    color: rgba(255,255,255,0.9);
}

.plan-price {
    font-size: 3rem;
    font-weight: 700;
    color: #ff5757;
    margin-bottom: 5px;
}

.plan-period {
    font-size: 1rem;
    color: rgba(255,255,255,0.7);
    margin-bottom: 30px;
}

.plan-features {
    list-style: none;
    padding: 0;
    margin-bottom: 30px;
    text-align: left;
}

.plan-features li {
    padding: 10px 0;
    border-bottom: 1px solid rgba(255,255,255,0.1);
    position: relative;
    padding-left: 25px;
    color: rgba(255,255,255,0.9);
}

.plan-features li:before {
    content: '✓';
    color: #ff5757;
    font-weight: bold;
    position: absolute;
    left: 0;
}

.plan-cta {
    background: linear-gradient(45deg, #ff5757, #ff8c42);
    color: white;
    padding: 15px 30px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
    display: block;
    transition: all 0.3s ease;
    margin-bottom: 20px;
}

.plan-cta:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(255, 87, 87, 0.4);
}

.plan-cta.secondary {
    background: rgba(255,255,255,0.2);
    border: 2px solid rgba(255,255,255,0.3);
}

.membership-guarantee {
    background: rgba(255,255,255,0.1);
    padding: 30px;
    border-radius: 15px;
    margin-top: 60px;
    max-width: 600px;
    margin-left: auto;
    margin-right: auto;
    backdrop-filter: blur(10px);
}

.membership-guarantee h3 {
    color: #ff5757;
    margin-bottom: 15px;
}

/* Mobile Responsive */
@media (max-width: 768px) {
    .hero-content h1 {
        font-size: 2.5rem;
    }
    
    .member-stats {
        gap: 30px;
    }
    
    .exclusivity-content {
        grid-template-columns: 1fr;
        gap: 40px;
    }
    
    .benefits-grid {
        grid-template-columns: 1fr;
    }
    
    .stories-grid {
        grid-template-columns: 1fr;
    }
    
    .pricing-options {
        grid-template-columns: 1fr;
    }
    
    .pricing-card.featured {
        transform: scale(1);
    }
    
    .btn-academy {
        width: 100%;
        margin: 10px 0;
    }
}

/* Sticky CTA */
.sticky-cta {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: linear-gradient(45deg, #ff5757, #ff8c42);
    color: white;
    padding: 15px 25px;
    border-radius: 50px;
    text-decoration: none;
    font-weight: 700;
    box-shadow: 0 10px 30px rgba(255, 87, 87, 0.4);
    z-index: 1000;
    animation: pulse 2s infinite;
    transition: all 0.3s ease;
}

.sticky-cta:hover {
    transform: scale(1.1);
    box-shadow: 0 15px 40px rgba(255, 87, 87, 0.6);
}

@media (max-width: 768px) {
    .sticky-cta {
        bottom: 10px;
        right: 10px;
        padding: 12px 20px;
        font-size: 0.9rem;
    }
}
</style>

<!-- Sticky CTA -->
<a href="{{ page.purchase_url }}" class="sticky-cta" target="_blank">Join Academy 🏆</a>

<!-- Hero Section -->
<section class="academy-hero">
    <div class="hero-content">
        <div class="exclusive-badge">🏆 Exclusive Membership</div>
        <h1>{{ page.product_name }}</h1>
        <p class="hero-tagline">Where Football Coaching Excellence is Forged</p>
        <p class="hero-description">Join {{ page.member_count }} elite coaches from professional academies worldwide. Monthly masterclasses with Kevin Middleton, cutting-edge resources, and the most exclusive coaching network on the planet.</p>
        
        <div class="member-stats">
            <div class="stat-item">
                <span class="stat-number">{{ page.member_count }}</span>
                <span class="stat-text">Elite Members</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">6</span>
                <span class="stat-text">Continents</span>
            </div>
            <div class="stat-item">
                <span class="stat-number">50+</span>
                <span class="stat-text">Pro Clubs</span>
            </div>
        </div>
        
        <div class="pricing-preview">
            <div class="price-comparison">
                <div class="original-price">Usually {{ page.original_price }}</div>
                <div class="current-price">{{ page.product_price }}</div>
            </div>
            <div class="price-note">Or {{ page.annual_price }}/year ({{ page.annual_savings }})</div>
            <div class="rising-price-warning">⏰ Price rising to {{ site.pricing.academy.future_monthly }} on {{ site.pricing.academy.price_increase_date }}</div>
        </div>
        
        <div class="hero-cta">
            <a href="{{ page.purchase_url }}" class="btn-academy" target="_blank">Join Academy - {{ page.product_price }}</a>
            <a href="#learn-more" class="btn-academy btn-secondary">See What's Inside</a>
        </div>
    </div>
</section>

<!-- Exclusivity Section -->
<section class="exclusivity">
    <div class="exclusivity-content">
        <div class="exclusivity-text">
            <h2>This Isn't for Everyone</h2>
            <p>While other coaches settle for basic training videos and generic advice, Academy members demand excellence from themselves and their development.</p>
            <p>This is where the top 1% of coaches come to stay ahead of the curve, master advanced methodologies, and build careers that matter.</p>
            <p><strong>If you're looking for quick fixes or surface-level content, this isn't for you.</strong></p>
            
            <ul class="elite-features">
                <li>Direct monthly access to Kevin Middleton's expertise</li>
                <li>Advanced coaching methodologies not available anywhere else</li>
                <li>Network with coaches from professional academies worldwide</li>
                <li>First access to cutting-edge player development research</li>
                <li>Personalized feedback on your coaching challenges</li>
                <li>Career advancement opportunities and recommendations</li>
            </ul>
        </div>
        
        <div class="exclusivity-visual">
            <h3>🏆 Current Academy Members</h3>
            <div class="member-avatars">
                <div class="avatar">MC</div>
                <div class="avatar">SJ</div>
                <div class="avatar">TR</div>
                <div class="avatar">DW</div>
                <div class="avatar">AL</div>
                <div class="avatar">KR</div>
                <div class="avatar">MH</div>
                <div class="avatar">LB</div>
            </div>
            
            <div class="club-logos">
                <div class="club-logo">Man United</div>
                <div class="club-logo">Arsenal</div>
                <div class="club-logo">Liverpool</div>
                <div class="club-logo">Barcelona</div>
                <div class="club-logo">Real Madrid</div>
                <div class="club-logo">Bayern Munich</div>
            </div>
            
            <p style="color: rgba(255,255,255,0.8); margin: 20px 0;">Coaches from 50+ professional clubs worldwide</p>
            <div class="member-limit">{{ page.member_limit }}</div>
        </div>
    </div>
</section>

<!-- Benefits Section -->
<section class="benefits" id="learn-more">
    <div class="section-header">
        <h2>What Academy Members Get</h2>
        <p>Exclusive resources and opportunities available nowhere else</p>
    </div>
    
    <div class="benefits-grid">
        <div class="benefit-card">
            <div class="benefit-icon">🎓</div>
            <h3>Monthly Live Masterclasses</h3>
            <p>90-minute deep-dive sessions with Kevin exploring advanced coaching concepts, guest experts from elite clubs, and cutting-edge methodologies.</p>
            <ul class="benefit-details">
                <li>Live Q&A with Kevin Middleton</li>
                <li>Guest speakers from professional academies</li>
                <li>Downloadable session recordings</li>
                <li>Detailed implementation guides</li>
                <li>Interactive breakout discussions</li>
            </ul>
            <div class="benefit-value">Value: $150/month</div>
        </div>

        <div class="benefit-card">
            <div class="benefit-icon">🌐</div>
            <h3>Elite Coaching Network</h3>
            <p>Connect, collaborate, and learn from coaches at professional academies and clubs worldwide. Build relationships that advance your career.</p>
            <ul class="benefit-details">
                <li>Private networking events</li>
                <li>Coaching exchange programmes</li>
                <li>Job opportunity sharing</li>
                <li>Mentorship matching</li>
                <li>International coaching visits</li>
            </ul>
            <div class="benefit-value">Value: $200/month</div>
        </div>

        <div class="benefit-card">
            <div class="benefit-icon">🔬</div>
            <h3>Cutting-Edge Research Access</h3>
            <p>Be the first to learn about new player development research, sports science findings, and tactical innovations before they become mainstream.</p>
            <ul class="benefit-details">
                <li>Monthly research summaries</li>
                <li>Access to sports science studies</li>
                <li>Tactical trend analysis</li>
                <li>Technology integration guides</li>
                <li>Performance data insights</li>
            </ul>
            <div class="benefit-value">Value: $120/month</div>
        </div>

        <div class="benefit-card">
            <div class="benefit-icon">🎯</div>
            <h3>Personalized Development Path</h3>
            <p>Custom coaching development journey based on your experience level, goals, and career aspirations. Individual attention you can't get elsewhere.</p>
            <ul class="benefit-details">
                <li>Skills assessment and gap analysis</li>
                <li>Personalized learning curriculum</li>
                <li>Progress tracking and milestones</li>
                <li>Career advancement guidance</li>
                <li>Individual coaching consultations</li>
            </ul>
            <div class="benefit-value">Value: $180/month</div>
        </div>

        <div class="benefit-card">
            <div class="benefit-icon">📚</div>
            <h3>Exclusive Resources Library</h3>
            <p>Access to Kevin's complete coaching vault including unpublished materials, case studies, and advanced methodologies not available in any public course.</p>
            <ul class="benefit-details">
                <li>Unreleased session plans</li>
                <li>Player development case studies</li>
                <li>Advanced tactical analysis</li>
                <li>Psychology and mindset resources</li>
                <li>Business and career development</li>
            </ul>
            <div class="benefit-value">Value: $100/month</div>
        </div>

        <div class="benefit-card">
            <div class="benefit-icon">💬</div>
            <h3>Direct Mentor Access</h3>
            <p>Monthly opportunities for direct coaching advice, career guidance, and problem-solving with Kevin Middleton. Get answers to your specific challenges.</p>
            <ul class="benefit-details">
                <li>Monthly office hours with Kevin</li>
                <li>Direct message access</li>
                <li>Priority response to questions</li>
                <li>Career advancement strategy</li>
                <li>Personal coaching challenges support</li>
            </ul>
            <div class="benefit-value">Value: $300/month</div>
        </div>
    </div>
    
    <div style="text-align: center; margin-top: 60px; padding: 40px; background: white; border-radius: 20px; max-width: 600px; margin-left: auto; margin-right: auto; box-shadow: 0 10px 30px rgba(0,0,0,0.1);">
        <h3 style="color: #976bdd; margin-bottom: 20px;">Total Monthly Value: $1,050+</h3>
        <h2 style="color: #ff5757; font-size: 2.5rem; margin-bottom: 10px;">Your Investment: {{ page.product_price }}</h2>
        <p style="color: #666;">That's 99% savings on individual coaching education</p>
    </div>
</section>

<!-- Success Stories -->
<section class="success-stories">
    <div class="section-header">
        <h2>Academy Transform Careers</h2>
        <p>How membership advanced these coaching careers</p>
    </div>
    
    <div class="stories-grid">
        <div class="story-card">
            <p class="story-text">The Academy didn't just improve my coaching - it transformed my career. Within 6 months, I went from grassroots volunteer to academy coach. The network connections alone were worth the membership.</p>
            <div class="story-author">Sarah Mitchell</div>
            <div class="story-role">Academy Coach, Wolverhampton Wanderers</div>
            <div class="story-result">🚀 Result: Promoted to professional academy role</div>
        </div>
        
        <div class="story-card">
            <p class="story-text">Kevin's monthly masterclasses are like having a personal mentor. The advanced tactics and psychology content has given me a massive edge. My players' decision-making improved dramatically.</p>
            <div class="story-author">David Chen</div>
            <div class="story-role">U18 Head Coach, Manchester City Academy</div>
            <div class="story-result">🧠 Result: Team won regional championship</div>
        </div>
        
        <div class="story-card">
            <p class="story-text">The community aspect is incredible. I've collaborated with coaches from Real Madrid, Bayern Munich, and Ajax. The knowledge sharing and friendships I've built are priceless.</p>
            <div class="story-author">Elena Rodriguez</div>
            <div class="story-role">Youth Development Director</div>
            <div class="story-result">🌐 Result: International coaching exchanges established</div>
        </div>
        
        <div class="story-card">
            <p class="story-text">As a former professional player transitioning to coaching, the Academy fast-tracked my development by years. The personalized guidance and resources are unmatched anywhere.</p>
            <div class="story-author">Jake Morrison</div>
            <div class="story-role">Former Professional Player</div>
            <div class="story-result">🚀 Result: Head Coach at League Two Club</div>
        </div>
        
        <div class="story-card">
            <p class="story-text">The exclusive research and tactical analysis gives me insights I can't get anywhere else. My players' decision-making has improved dramatically since implementing the Academy methodologies.</p>
            <div class="story-author">Emma Thompson</div>
            <div class="story-role">Academy Coach, Leicester City</div>
            <div class="story-result">🧠 Result: 45% improvement in tactical awareness scores</div>
        </div>
        
        <div class="story-card">
            <p class="story-text">The Academy community opened doors I never knew existed. The job opportunities shared within the network led directly to my current role at one of England's top academies.</p>
            <div class="story-author">Michael Roberts</div>
            <div class="story-role">Head of Player Development</div>
            <div class="story-result">💼 Result: Dream job at Premier League academy</div>
        </div>
    </div>
</section>

<!-- Pricing Section -->
<section class="pricing" id="join-now">
    <div>
        <h2>Choose Your Academy Membership</h2>
        <p class="pricing-subtitle">Join the world's most exclusive coaching education community</p>
        
        <div class="pricing-options">
            <div class="pricing-card">
                <div class="plan-name">Monthly Academy</div>
                <div class="plan-price">${{ page.product_price | remove: ' | remove: '/month' }}</div>
                <div class="plan-period">per month</div>
                
                <ul class="plan-features">
                    <li>Monthly live masterclasses with Kevin</li>
                    <li>Access to elite coaching network</li>
                    <li>Exclusive resources library</li>
                    <li>Direct mentor access</li>
                    <li>Cutting-edge research access</li>
                    <li>Personalized development path</li>
                    <li>Cancel anytime</li>
                </ul>
                
                <a href="{{ page.purchase_url }}" class="plan-cta secondary" target="_blank">
                    Join Monthly - $10
                </a>
            </div>

            <div class="pricing-card featured">
                <div class="plan-name">Annual Academy</div>
                <div class="plan-price">$6.67</div>
                <div class="plan-period">per month ({{ page.annual_price }} billed annually)</div>
                
                <ul class="plan-features">
                    <li>Everything in Monthly Academy</li>
                    <li>2 months free ({{ page.annual_savings }})</li>
                    <li>Exclusive annual retreat invite</li>
                    <li>Priority coaching consultation</li>
                    <li>Advanced resources early access</li>
                    <li>Lock in current pricing forever</li>
                </ul>
                
                <a href="{{ page.purchase_url }}" class="plan-cta primary" target="_blank">
                    Join Annual - Save $40
                </a>
            </div>
        </div>
        
        <div class="membership-guarantee">
            <h3>🛡️ Academy Membership Guarantee</h3>
            <p>If you're not completely satisfied with your Academy membership in the first 30 days, we'll refund your subscription and let you keep any resources you've downloaded. {{ page.guarantee }}.</p>
        </div>
    </div>
</section>

<!-- FAQ Section -->
<section class="faq" style="padding: 100px 0; background: #f8f9fa;">
    <div style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
        <div class="section-header">
            <h2>Frequently Asked Questions</h2>
            <p>Everything you need to know about Academy membership</p>
        </div>
        
        <div class="faq-grid">
            <div class="faq-item">
                <div class="faq-question">What exactly do I get with Academy membership?</div>
                <div class="faq-answer">Monthly live masterclasses with Kevin Middleton, access to our private community of {{ page.member_count }} elite coaches, exclusive resources library, direct mentorship opportunities, and networking with coaches from professional academies worldwide. Everything is designed for serious coaches who want systematic improvement.</div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">How is this different from the free community?</div>
                <div class="faq-answer">The free community is open to all coaches and focuses on basic Q&A and general discussions. The Academy is exclusively for committed coaches and includes live masterclasses, advanced resources, direct access to Kevin, career guidance, and connections with professional club coaches.</div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Can I cancel anytime?</div>
                <div class="faq-answer">Absolutely. There are no long-term contracts. You can cancel your membership at any time and retain access until your current billing period ends. We believe in earning your membership every month through value, not contracts.</div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">What if I'm just starting as a coach?</div>
                <div class="faq-answer">While the Academy is designed for serious coaches, we welcome ambitious beginners who are committed to excellence. The personalized development paths help new coaches accelerate their learning curve significantly.</div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Are the masterclasses recorded if I can't attend live?</div>
                <div class="faq-answer">Yes, every masterclass is recorded and available in the members' library within 24 hours. You also get downloadable resources and implementation guides. However, live attendance is recommended for the Q&A sessions.</div>
            </div>
            
            <div class="faq-item">
                <div class="faq-question">Will this help me advance my coaching career?</div>
                <div class="faq-answer">Many members have advanced their careers through Academy connections, improved coaching skills, and the confidence that comes from systematic development. While we can't guarantee career outcomes, the tools and network significantly increase your opportunities.</div>
            </div>
        </div>
    </div>
</section>

<!-- Final CTA -->
<section style="padding: 100px 0; background: linear-gradient(135deg, #1a1a1a 0%, #2d1b4e 100%); color: white; text-align: center;">
    <div style="max-width: 800px; margin: 0 auto; padding: 0 20px;">
        <h2 style="font-size: 2.8rem; margin-bottom: 20px; font-weight: 600;">Ready to Join the Elite?</h2>
        <p style="font-size: 1.3rem; margin-bottom: 40px; color: rgba(255,255,255,0.9);">{{ page.member_count }} coaches from professional academies worldwide are already inside. Your spot is waiting.</p>
        
        <div style="background: #ff5757; color: white; padding: 15px 30px; border-radius: 25px; font-weight: 600; margin-bottom: 40px; display: inline-block; animation: pulse 2s infinite;">
            ⏰ Price rising to $15 on August 1st, 2025 - Lock in $10 now
        </div>
        
        <div>
            <a href="{{ page.purchase_url }}" class="btn-academy" target="_blank" style="margin: 10px;">
                🚀 Join Academy - {{ page.product_price }}
            </a>
            <a href="{{ page.purchase_url }}" class="btn-academy btn-secondary" target="_blank" style="margin: 10px;">
                💰 Annual - {{ page.annual_price }} ({{ page.annual_savings }})
            </a>
        </div>
        
        <div style="margin-top: 30px; font-size: 0.9rem; opacity: 0.8;">
            <p>✅ {{ page.guarantee }} • ✅ Access entire community • ✅ Lock in pricing forever</p>
        </div>
    </div>
</section>

<script>
// FAQ Functionality
document.addEventListener('DOMContentLoaded', function() {
    const faqQuestions = document.querySelectorAll('.faq-question');
    
    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const answer = this.nextElementSibling;
            const isActive = this.classList.contains('active');
            
            // Close all other FAQs
            faqQuestions.forEach(q => {
                q.classList.remove('active');
                q.nextElementSibling.classList.remove('active');
            });
            
            // Toggle current FAQ
            if (!isActive) {
                this.classList.add('active');
                answer.classList.add('active');
            }
        });
    });
    
    // Track Academy CTA clicks for analytics
    document.querySelectorAll('a[href*="coachingacademy"]').forEach(link => {
        link.addEventListener('click', function() {
            console.log('Academy CTA clicked');
            // Analytics tracking would go here
        });
    });
    
    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
});
</script>

<!-- Schema Markup for SEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Product",
    "name": "{{ page.product_name }}",
    "description": "Exclusive football coaching education community. Monthly masterclasses with Kevin Middleton, elite coaching network, cutting-edge resources, and direct mentorship.",
    "image": "{{ site.url }}{{ site.baseurl }}/assets/images/academy-preview.jpg",
    "brand": {
        "@type": "Brand",
        "name": "360TFT"
    },
    "offers": {
        "@type": "Offer",
        "url": "{{ page.purchase_url }}",
        "priceCurrency": "USD",
        "price": "10",
        "availability": "https://schema.org/InStock",
        "seller": {
            "@type": "Person",
            "name": "Kevin Middleton"
        },
        "priceSpecification": {
            "@type": "RecurringPaymentFrequency",
            "frequency": "monthly"
        }
    },
    "aggregateRating": {
        "@type": "AggregateRating",
        "ratingValue": "4.9",
        "reviewCount": "347"
    },
    "audience": {
        "@type": "Audience",
        "audienceType": "Football Coaches"
    }
}
</script>