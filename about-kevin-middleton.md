---
layout: default
title: "About Kevin Middleton | Football Coach with 15+ Years Experience"
description: "Meet Kevin Middleton, the football coach behind 360TFT. 15+ years developing players, 1000+ coaches mentored, creator of the proven 360TFT Game Model that transforms average players into match-winners."
keywords: [Kevin Middleton football coach, 360TFT founder, football coaching expert, player development specialist, coaching philosophy, football coach biography]
seo_title: "About Kevin Middleton | Football Coach with 15+ Years Experience | 360TFT"

# Open Graph
og_type: profile
og_title: "About Kevin Middleton - Football Coach & Player Development Expert"
og_description: "The man behind 360TFT. 15+ years coaching experience, creator of proven methodologies, mentor to 1000+ coaches worldwide."
og_image: "/assets/images/kevin-middleton-coach.jpg"

# Twitter
twitter_title: "About Kevin Middleton - Football Coach & Player Development Expert"
twitter_description: "The man behind 360TFT. 15+ years coaching experience, creator of proven methodologies, mentor to 1000+ coaches worldwide."
twitter_image: "/assets/images/kevin-middleton-coach.jpg"

# Page-specific settings
css: ["/assets/css/about-kevin.css"]
js: ["/assets/js/story-navigation.js"]
body_class: "about-page"
schema_type: "Person"

# Personal details for schema
job_title: "Football Coach & Player Development Expert"
years_experience: "15+"
coaches_mentored: "1000+"
players_developed: "5000+"
---

<style>
/* About Kevin Page Styles */
.about-hero {
    background: linear-gradient(135deg, #976bdd 0%, #7c5acc 100%);
    color: white;
    padding: 100px 0 80px;
    position: relative;
    overflow: hidden;
}

.about-hero::before {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: url('data:image/svg+xml,<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100"><circle cx="20" cy="20" r="2" fill="rgba(255,255,255,0.1)"/><circle cx="80" cy="40" r="1.5" fill="rgba(255,255,255,0.1)"/><circle cx="40" cy="80" r="1" fill="rgba(255,255,255,0.1)"/></svg>');
    opacity: 0.3;
}

.hero-content {
    display: grid;
    grid-template-columns: 2fr 1fr;
    gap: 60px;
    align-items: center;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    position: relative;
    z-index: 2;
}

.hero-text h1 {
    font-size: 3.5rem;
    font-weight: 700;
    margin-bottom: 20px;
    line-height: 1.1;
}

.hero-subtitle {
    font-size: 1.5rem;
    color: rgba(255,255,255,0.9);
    margin-bottom: 30px;
    font-weight: 300;
}

.hero-description {
    font-size: 1.2rem;
    line-height: 1.6;
    margin-bottom: 40px;
    color: rgba(255,255,255,0.95);
}

.hero-stats {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin-top: 40px;
}

.stat-item {
    text-align: center;
    padding: 20px;
    background: rgba(255,255,255,0.1);
    border-radius: 15px;
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255,255,255,0.2);
}

.stat-number {
    display: block;
    font-size: 2.5rem;
    font-weight: 700;
    color: #fff;
    margin-bottom: 5px;
}

.stat-text {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.8);
    text-transform: uppercase;
    letter-spacing: 1px;
}

.hero-image {
    position: relative;
    text-align: center;
}

.hero-badge {
    background: #ff5757;
    color: white;
    padding: 10px 20px;
    border-radius: 25px;
    font-weight: 600;
    margin-bottom: 20px;
    display: inline-block;
    font-size: 0.9rem;
    text-transform: uppercase;
    letter-spacing: 1px;
}

.kevin-photo {
    width: 280px;
    height: 280px;
    border-radius: 50%;
    object-fit: cover;
    border: 8px solid rgba(255,255,255,0.2);
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
}

/* Story Section */
.story {
    padding: 100px 0;
    background: #f8f9fa;
}

.story-content {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 60px;
}

.story-nav {
    background: white;
    border-radius: 20px;
    padding: 30px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    position: sticky;
    top: 120px;
    height: fit-content;
}

.story-nav h3 {
    color: #976bdd;
    font-size: 1.4rem;
    margin-bottom: 25px;
    font-weight: 600;
}

.story-nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
}

.story-nav li {
    margin-bottom: 15px;
}

.story-nav a {
    color: #666;
    text-decoration: none;
    padding: 12px 15px;
    display: block;
    border-radius: 10px;
    transition: all 0.3s ease;
    font-weight: 500;
}

.story-nav a:hover,
.story-nav a.active {
    background: #976bdd;
    color: white;
    transform: translateX(5px);
}

.story-section {
    background: white;
    padding: 40px;
    border-radius: 20px;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.story-section h2 {
    color: #976bdd;
    font-size: 2.2rem;
    margin-bottom: 25px;
    font-weight: 600;
}

.story-section p {
    font-size: 1.1rem;
    line-height: 1.7;
    color: #444;
    margin-bottom: 20px;
}

.story-section blockquote {
    background: #f8f9fa;
    border-left: 5px solid #976bdd;
    padding: 25px 30px;
    margin: 30px 0;
    font-style: italic;
    font-size: 1.2rem;
    color: #555;
    border-radius: 0 15px 15px 0;
}

/* Philosophy Cards */
.philosophy-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 30px;
    margin: 40px 0;
}

.philosophy-card {
    background: white;
    padding: 30px;
    border-radius: 20px;
    border: 2px solid #f0f0f0;
    transition: all 0.3s ease;
    text-align: center;
}

.philosophy-card:hover {
    border-color: #976bdd;
    transform: translateY(-5px);
    box-shadow: 0 15px 35px rgba(151, 107, 221, 0.2);
}

.philosophy-icon {
    font-size: 3rem;
    margin-bottom: 20px;
}

.philosophy-card h3 {
    color: #976bdd;
    font-size: 1.4rem;
    margin-bottom: 15px;
    font-weight: 600;
}

.philosophy-card p {
    color: #666;
    line-height: 1.6;
    margin: 0;
}

/* Timeline */
.timeline {
    padding: 80px 0;
    background: white;
}

.timeline-item {
    display: grid;
    grid-template-columns: 150px 1fr;
    gap: 40px;
    margin-bottom: 50px;
    align-items: start;
}

.timeline-year {
    background: #976bdd;
    color: white;
    padding: 15px 20px;
    border-radius: 25px;
    text-align: center;
    font-weight: 600;
    position: sticky;
    top: 120px;
}

.timeline-content {
    background: #f8f9fa;
    padding: 30px;
    border-radius: 20px;
    border-left: 5px solid #976bdd;
}

.timeline-content h3 {
    color: #976bdd;
    font-size: 1.4rem;
    margin-bottom: 15px;
    font-weight: 600;
}

/* CTA Section */
.about-cta {
    background: linear-gradient(135deg, #976bdd 0%, #7c5acc 100%);
    color: white;
    padding: 80px 0;
    text-align: center;
}

.cta-content {
    max-width: 800px;
    margin: 0 auto;
    padding: 0 20px;
}

.cta-content h2 {
    font-size: 2.5rem;
    margin-bottom: 20px;
    font-weight: 600;
}

.cta-content p {
    font-size: 1.2rem;
    margin-bottom: 40px;
    color: rgba(255,255,255,0.9);
}

.cta-buttons {
    display: flex;
    gap: 20px;
    justify-content: center;
    flex-wrap: wrap;
}

.btn-cta {
    background: #ff5757;
    color: white;
    padding: 15px 30px;
    border-radius: 25px;
    text-decoration: none;
    font-weight: 600;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    gap: 10px;
}

.btn-cta:hover {
    background: #e54545;
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(255, 87, 87, 0.4);
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

/* Mobile Responsive */
@media (max-width: 768px) {
    .hero-content {
        grid-template-columns: 1fr;
        text-align: center;
        gap: 40px;
    }
    
    .hero-text h1 {
        font-size: 2.5rem;
    }
    
    .hero-stats {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .story-content {
        grid-template-columns: 1fr;
        gap: 40px;
    }
    
    .story-nav {
        position: static;
        margin-bottom: 30px;
    }
    
    .timeline-item {
        grid-template-columns: 1fr;
        gap: 20px;
    }
    
    .timeline-year {
        position: static;
        width: fit-content;
        margin: 0 auto;
    }
    
    .cta-buttons {
        flex-direction: column;
        align-items: center;
    }
}
</style>

<!-- Hero Section -->
<section class="about-hero">
    <div class="hero-content">
        <div class="hero-text">
            <h1>Meet Kevin Middleton</h1>
            <p class="hero-subtitle">The Football Coach Behind 360TFT</p>
            <p class="hero-description">For over {{ page.years_experience }} years, I've been obsessed with one question: "How do we develop better footballers faster?" The answer became a methodology that's transformed {{ page.coaches_mentored }} coaches and {{ page.players_developed }} players worldwide.</p>
            
            <div class="hero-stats">
                <div class="stat-item">
                    <span class="stat-number">{{ page.years_experience }}</span>
                    <span class="stat-text">Years Coaching</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{{ page.coaches_mentored }}</span>
                    <span class="stat-text">Coaches Mentored</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{{ page.players_developed }}</span>
                    <span class="stat-text">Players Developed</span>
                </div>
            </div>
        </div>
        
        <div class="hero-image">
            <div class="hero-badge">Creator of 360TFT</div>
            <img class="kevin-photo" src="/assets/images/kevin-middleton-coach.jpg" alt="Kevin Middleton - Football Coach">
        </div>
    </div>
</section>

<!-- Story Section -->
<section class="story" id="story">
    <div class="story-content">
        <div class="story-nav">
            <h3>My Journey</h3>
            <ul>
                <li><a href="#early-days" class="nav-link">Early Days</a></li>
                <li><a href="#coaching-evolution" class="nav-link">Coaching Evolution</a></li>
                <li><a href="#360tft-birth" class="nav-link">Birth of 360TFT</a></li>
                <li><a href="#philosophy" class="nav-link">Coaching Philosophy</a></li>
                <li><a href="#today" class="nav-link">Today & Beyond</a></li>
            </ul>
        </div>
        
        <div class="story-main">
            <div class="story-section" id="early-days">
                <h2>The Early Days</h2>
                <p>My coaching journey began like many others - with passion, but little direction. Fresh-faced and eager, I thought coaching was about knowing more drills than the next person. I was wrong.</p>
                
                <p>My first season coaching an U12 team was humbling. Despite having endless energy and what I thought were great sessions, the players weren't improving. Parents were polite but concerned. I was failing the kids who trusted me to help them get better.</p>
                
                <blockquote>
                    That's when I realised coaching isn't about what you know - it's about how effectively you can transfer that knowledge into improved player performance.
                </blockquote>
                
                <p>I spent that summer studying everything I could find about player development, sports psychology, and motor learning. But more importantly, I started watching my players more carefully - not just what they were doing wrong, but why they were doing it wrong.</p>
            </div>

            <div class="story-section" id="coaching-evolution">
                <h2>The Coaching Evolution</h2>
                <p>Over the next few years, I coached at every level - grassroots clubs, local academies, school teams. Each environment taught me something different about how players learn and develop.</p>
                
                <p>At grassroots level, I learned that fun and development aren't opposites - they're partners. The best sessions felt like play, but every game and exercise was carefully designed to improve specific aspects of player performance.</p>
                
                <p>Working with academy players taught me that talented kids need more than just technical work. They needed to understand the game, make better decisions under pressure, and develop the mental resilience to handle setbacks.</p>
                
                <p>School football showed me the power of systematic development. When you only see players twice a week, every session must build on the last one. No time for random drills or hoping for the best.</p>
            </div>

            <div class="story-section" id="360tft-birth">
                <h2>The Birth of 360TFT</h2>
                <p>The "360" represents the complete player - technical, tactical, physical, and mental development all working together. "TFT" stands for "Think Fast, Think Football" - the ability to make good decisions under pressure.</p>
                
                <p>But 360TFT became more than a methodology. It became a community of coaches who believe that every player deserves systematic, purposeful development. Not just the talented ones. Not just the ones whose parents can afford private coaching. Every player.</p>
                
                <blockquote>
                    The moment I realised 360TFT was working was when a parent coach told me: "My son doesn't just play better now - he thinks about the game differently." That's when I knew we were onto something special.
                </blockquote>
                
                <p>Word spread through coaching networks. Other coaches started asking for my session plans, my development frameworks, my "secrets." But I realised that giving someone a drill isn't the same as teaching them how to coach. That's when I decided to build something bigger.</p>
            </div>

            <div class="story-section" id="philosophy">
                <h2>My Coaching Philosophy</h2>
                <p>After 15+ years of coaching, certain principles have become non-negotiable for me. These aren't just theories - they're battle-tested truths that separate coaches who develop players from coaches who just run training sessions.</p>
                
                <div class="philosophy-grid">
                    <div class="philosophy-card">
                        <div class="philosophy-icon">❤️</div>
                        <h3>Emotional Connection</h3>
                        <p>Players don't remember what you taught them - they remember how you made them feel while they were learning it. This changed everything about how I approach coaching interactions.</p>
                    </div>
                    
                    <div class="philosophy-card">
                        <div class="philosophy-icon">🧠</div>
                        <h3>Decision Making First</h3>
                        <p>Technique without decision-making is just juggling. Technical ability means nothing if players can't apply it under pressure, in the right moment, with teammates and opponents around them.</p>
                    </div>
                    
                    <div class="philosophy-card">
                        <div class="philosophy-icon">📈</div>
                        <h3>Systematic Development</h3>
                        <p>Every session must build on the last one. Random training sessions create random players. Systematic development creates consistent improvement and confident decision-makers.</p>
                    </div>
                    
                    <div class="philosophy-card">
                        <div class="philosophy-icon">🎯</div>
                        <h3>Independent Thinkers</h3>
                        <p>The best coaches make themselves obsolete. My job isn't to create players who depend on me for answers - it's to create players who can solve problems independently on the pitch.</p>
                    </div>
                </div>
            </div>

            <div class="story-section" id="today">
                <h2>Today & What's Next</h2>
                <p>Today, 360TFT has grown beyond what I ever imagined. We have coaches using our methodologies in professional academies, grassroots clubs, and school programmes across six continents. The community includes parent coaches taking their first steps and experienced professionals refining their craft.</p>
                
                <p>But I'm not done. The Football Coaching Academy represents the next evolution - a place where serious coaches can access cutting-edge research, learn from each other, and stay ahead of the curve in player development.</p>
                
                <p>My mission remains the same: to help coaches develop better players, faster. Because when coaches improve, players improve. And when players improve, the beautiful game gets even more beautiful.</p>
            </div>
        </div>
    </div>
</section>

<!-- Timeline Section -->
<section class="timeline">
    <div class="container">
        <div class="section-header text-center">
            <h2>The 360TFT Journey</h2>
            <p>Key milestones in developing the methodology that's transforming football coaching</p>
        </div>
        
        <div class="timeline-container">
            <div class="timeline-item">
                <div class="timeline-year">2010-2012</div>
                <div class="timeline-content">
                    <h3>Grassroots Foundation</h3>
                    <p>Learned that fun and development aren't opposites - they're partners. Discovered the power of small-sided games and player-centred coaching.</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-year">2013-2015</div>
                <div class="timeline-content">
                    <h3>Academy Experience</h3>
                    <p>Worked with talented players who needed more than just technical work. Developed understanding of tactical periodisation and psychological development.</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-year">2016-2018</div>
                <div class="timeline-content">
                    <h3>Methodology Development</h3>
                    <p>Started connecting the dots between different aspects of player development. The 360TFT framework began taking shape.</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-year">2019-2021</div>
                <div class="timeline-content">
                    <h3>System Refinement</h3>
                    <p>Tested and refined the 360TFT Game Model with hundreds of players. Started sharing knowledge with other coaches.</p>
                </div>
            </div>
            
            <div class="timeline-item">
                <div class="timeline-year">2022-Present</div>
                <div class="timeline-content">
                    <h3>Global Impact</h3>
                    <p>360TFT community grows to 1000+ coaches worldwide. Launching the Football Coaching Academy for elite development.</p>
                </div>
            </div>
        </div>
    </div>
</section>

<!-- CTA Section -->
<section class="about-cta">
    <div class="cta-content">
        <h2>Ready to Transform Your Coaching?</h2>
        <p>Join the community of coaches who are developing better players faster with proven 360TFT methodologies.</p>
        
        <div class="cta-buttons">
            <a href="/football-coaching-academy" class="btn-cta">
                Join the Academy
                <span>→</span>
            </a>
            <a href="/complete-coaching-mastery-system" class="btn-cta btn-secondary">
                Get the Complete System
                <span>→</span>
            </a>
        </div>
    </div>
</section>

<script>
// Story Navigation
document.addEventListener('DOMContentLoaded', function() {
    const navLinks = document.querySelectorAll('.nav-link');
    const sections = document.querySelectorAll('.story-section');
    
    // Smooth scrolling for navigation links
    navLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            e.preventDefault();
            const targetId = this.getAttribute('href').substring(1);
            const targetSection = document.getElementById(targetId);
            
            if (targetSection) {
                targetSection.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Update active navigation based on scroll position
    const observerOptions = {
        threshold: 0.3,
        rootMargin: '-100px 0px -200px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                // Remove active class from all links
                navLinks.forEach(link => link.classList.remove('active'));
                
                // Add active class to corresponding link
                const activeLink = document.querySelector(`a[href="#${entry.target.id}"]`);
                if (activeLink) {
                    activeLink.classList.add('active');
                }
            }
        });
    }, observerOptions);
    
    sections.forEach(section => {
        observer.observe(section);
    });
});
</script>

<!-- Schema Markup for SEO -->
<script type="application/ld+json">
{
    "@context": "https://schema.org",
    "@type": "Person",
    "name": "Kevin Middleton",
    "jobTitle": "{{ page.job_title }}",
    "description": "Football coach with {{ page.years_experience }} years experience, creator of the 360TFT Game Model, mentor to {{ page.coaches_mentored }} coaches worldwide",
    "url": "{{ site.url }}{{ site.baseurl }}{{ page.url }}",
    "image": "{{ site.url }}{{ site.baseurl }}/assets/images/kevin-middleton-coach.jpg",
    "sameAs": [
        "https://x.com/coach_kevin_m",
        "https://www.linkedin.com/in/kevinmiddleton360",
        "https://www.youtube.com/@360TFT",
        "https://www.skool.com/coachingacademy"
    ],
    "worksFor": {
        "@type": "Organization",
        "name": "360TFT",
        "description": "Football coaching education and player development",
        "url": "{{ site.url }}{{ site.baseurl }}"
    },
    "alumniOf": {
        "@type": "EducationalOrganization",
        "name": "Football Coaching Experience - Grassroots to Academy Level"
    },
    "knowsAbout": [
        "Football Coaching",
        "Player Development", 
        "Youth Football",
        "Coaching Education",
        "Sports Psychology",
        "Technical Training",
        "Tactical Development",
        "Small-Sided Games",
        "Decision Making Training"
    ],
    "award": [
        "{{ page.coaches_mentored }} Coaches Mentored",
        "{{ page.players_developed }} Players Developed",
        "Creator of 360TFT Game Model",
        "328 Training Sessions Designed"
    ]
}
</script>