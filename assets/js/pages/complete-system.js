// Complete System Page Interactions - 360TFT
// Handles interactive elements and animations for the complete system page

(function() {
    'use strict';
    
    document.addEventListener('DOMContentLoaded', function() {
        initCompleteSystemPage();
        setupTimelineAnimations();
        setupTestimonialRotation();
        setupPricingInteractions();
    });
    
    function initCompleteSystemPage() {
        console.log('Complete System Page Initialized');
        enhanceUserExperience();
        setupScrollAnimations();
    }
    
    function enhanceUserExperience() {
        // Add loading states to CTA buttons
        const ctaButtons = document.querySelectorAll('.cta-purchase, .hero-cta');
        
        ctaButtons.forEach(button => {
            button.addEventListener('click', function(e) {
                if (!this.classList.contains('loading')) {
                    this.classList.add('loading');
                    const originalText = this.textContent;
                    this.textContent = 'Processing...';
                    
                    // Reset after 3 seconds if no navigation occurs
                    setTimeout(() => {
                        this.classList.remove('loading');
                        this.textContent = originalText;
                    }, 3000);
                }
            });
        });
        
        // Add loading styles
        addLoadingStyles();
    }
    
    function setupTimelineAnimations() {
        const timelineItems = document.querySelectorAll('.timeline-item');
        
        if (timelineItems.length === 0) return;
        
        // Create intersection observer for timeline animations
        const timelineObserver = new IntersectionObserver((entries) => {
            entries.forEach((entry, index) => {
                if (entry.isIntersecting) {
                    setTimeout(() => {
                        entry.target.classList.add('animate-in');
                    }, index * 200); // Stagger animation
                }
            });
        }, {
            threshold: 0.3
        });
        
        timelineItems.forEach(item => {
            timelineObserver.observe(item);
        });
    }
    
    function setupTestimonialRotation() {
        const testimonialCards = document.querySelectorAll('.testimonial-card');
        
        if (testimonialCards.length <= 1) return;
        
        let currentTestimonial = 0;
        
        // Add navigation dots
        const testimonialContainer = document.querySelector('.testimonials-grid');
        if (testimonialContainer) {
            const dotsContainer = document.createElement('div');
            dotsContainer.className = 'testimonial-dots';
            
            testimonialCards.forEach((_, index) => {
                const dot = document.createElement('button');
                dot.className = `testimonial-dot ${index === 0 ? 'active' : ''}`;
                dot.addEventListener('click', () => showTestimonial(index));
                dotsContainer.appendChild(dot);
            });
            
            testimonialContainer.appendChild(dotsContainer);
            
            // Auto-rotate testimonials every 8 seconds
            setInterval(() => {
                currentTestimonial = (currentTestimonial + 1) % testimonialCards.length;
                showTestimonial(currentTestimonial);
            }, 8000);
        }
        
        function showTestimonial(index) {
            // Update dots
            document.querySelectorAll('.testimonial-dot').forEach((dot, i) => {
                dot.classList.toggle('active', i === index);
            });
            
            // Highlight testimonial
            testimonialCards.forEach((card, i) => {
                card.classList.toggle('highlighted', i === index);
            });
            
            currentTestimonial = index;
        }
    }
    
    function setupPricingInteractions() {
        // Add value calculator
        const systemComponents = document.querySelectorAll('.component-card');
        
        if (systemComponents.length > 0) {
            createValueCalculator(systemComponents);
        }
        
        // Add comparison tool
        setupComparisonTool();
    }
    
    function createValueCalculator(components) {
        const calculatorHTML = `
            <div class="value-calculator">
                <h3>Calculate Individual Item Value</h3>
                <div class="calculator-items">
                    <div class="calc-item">
                        <label>328 Sessions (individual): <span class="calc-price">$328</span></label>
                    </div>
                    <div class="calc-item">
                        <label>Game Model Guide: <span class="calc-price">$40</span></label>
                    </div>
                    <div class="calc-item">
                        <label>Coaching Compass: <span class="calc-price">$25</span></label>
                    </div>
                    <div class="calc-item">
                        <label>Cheatsheet Vault: <span class="calc-price">$15</span></label>
                    </div>
                </div>
                <div class="calc-total">
                    Total Individual Value: <span class="total-price">$408</span>
                </div>
                <div class="calc-savings">
                    Your Savings: <span class="savings-amount">$281</span>
                </div>
            </div>
        `;
        
        const pricingSection = document.querySelector('.pricing, .value-section');
        if (pricingSection) {
            pricingSection.insertAdjacentHTML('afterbegin', calculatorHTML);
        }
    }
    
    function setupComparisonTool() {
        // Add comparison with other coaching resources
        const comparisonHTML = `
            <div class="comparison-tool">
                <h3>Compare to Alternatives</h3>
                <div class="comparison-grid">
                    <div class="comparison-item">
                        <h4>Other Coaching Courses</h4>
                        <div class="comparison-price">$500-2000</div>
                        <div class="comparison-features">
                            <span class="feature-no">❌ Generic content</span>
                            <span class="feature-no">❌ No ongoing support</span>
                            <span class="feature-no">❌ Theory-focused</span>
                        </div>
                    </div>
                    <div class="comparison-item highlight">
                        <h4>360TFT Complete System</h4>
                        <div class="comparison-price">$127</div>
                        <div class="comparison-features">
                            <span class="feature-yes">✅ Proven methodology</span>
                            <span class="feature-yes">✅ Ready-to-use sessions</span>
                            <span class="feature-yes">✅ Lifetime access</span>
                        </div>
                    </div>
                </div>
            </div>
        `;
        
        const faqSection = document.querySelector('.faq');
        if (faqSection) {
            faqSection.insertAdjacentHTML('beforebegin', comparisonHTML);
        }
    }
    
    function setupScrollAnimations() {
        // Animate elements as they come into view
        const animateElements = document.querySelectorAll('.component-card, .testimonial-card, .timeline-item');
        
        const scrollObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('scroll-animate');
                }
            });
        }, {
            threshold: 0.2
        });
        
        animateElements.forEach(el => {
            scrollObserver.observe(el);
        });
    }
    
    function addLoadingStyles() {
        if (document.getElementById('complete-system-styles')) return;
        
        const styles = `
            <style id="complete-system-styles">
                .loading {
                    opacity: 0.7;
                    cursor: wait;
                    position: relative;
                }
                
                .loading::after {
                    content: '';
                    position: absolute;
                    width: 16px;
                    height: 16px;
                    margin: auto;
                    border: 2px solid transparent;
                    border-top-color: #ffffff;
                    border-radius: 50%;
                    animation: spin 1s linear infinite;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                }
                
                @keyframes spin {
                    0% { transform: translate(-50%, -50%) rotate(0deg); }
                    100% { transform: translate(-50%, -50%) rotate(360deg); }
                }
                
                .timeline-item {
                    opacity: 0;
                    transform: translateY(30px);
                    transition: all 0.6s ease;
                }
                
                .timeline-item.animate-in {
                    opacity: 1;
                    transform: translateY(0);
                }
                
                .testimonial-dots {
                    display: flex;
                    justify-content: center;
                    gap: 10px;
                    margin-top: 30px;
                }
                
                .testimonial-dot {
                    width: 12px;
                    height: 12px;
                    border-radius: 50%;
                    border: 2px solid #976bdd;
                    background: transparent;
                    cursor: pointer;
                    transition: all 0.3s ease;
                }
                
                .testimonial-dot.active,
                .testimonial-dot:hover {
                    background: #976bdd;
                }
                
                .testimonial-card.highlighted {
                    transform: scale(1.05);
                    box-shadow: 0 20px 40px rgba(151, 107, 221, 0.25);
                }
                
                .value-calculator {
                    background: linear-gradient(135deg, #f8f9fa, #e9ecef);
                    padding: 30px;
                    border-radius: 15px;
                    margin: 30px 0;
                    border: 2px solid #976bdd;
                }
                
                .calc-item {
                    display: flex;
                    justify-content: space-between;
                    padding: 10px 0;
                    border-bottom: 1px solid #ddd;
                }
                
                .calc-total {
                    font-size: 1.3em;
                    font-weight: bold;
                    color: #333;
                    padding: 15px 0;
                    border-top: 2px solid #976bdd;
                    margin-top: 15px;
                    display: flex;
                    justify-content: space-between;
                }
                
                .calc-savings {
                    font-size: 1.5em;
                    font-weight: bold;
                    color: #ff5757;
                    text-align: center;
                    padding: 15px;
                    background: rgba(255, 87, 87, 0.1);
                    border-radius: 10px;
                    margin-top: 15px;
                }
                
                .comparison-tool {
                    background: #f8f9fa;
                    padding: 40px;
                    border-radius: 15px;
                    margin: 40px 0;
                }
                
                .comparison-grid {
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 30px;
                    margin-top: 20px;
                }
                
                .comparison-item {
                    background: white;
                    padding: 30px;
                    border-radius: 10px;
                    text-align: center;
                    border: 2px solid #ddd;
                }
                
                .comparison-item.highlight {
                    border-color: #976bdd;
                    background: linear-gradient(135deg, #976bdd, #7c5bc4);
                    color: white;
                }
                
                .comparison-price {
                    font-size: 2em;
                    font-weight: bold;
                    margin: 15px 0;
                    color: #ff5757;
                }
                
                .comparison-item.highlight .comparison-price {
                    color: white;
                }
                
                .comparison-features {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    margin-top: 20px;
                }
                
                .feature-yes {
                    color: #4caf50;
                }
                
                .feature-no {
                    color: #f44336;
                    opacity: 0.7;
                }
                
                .comparison-item.highlight .feature-yes {
                    color: #c8e6c9;
                }
                
                .scroll-animate {
                    animation: slideInUp 0.6s ease forwards;
                }
                
                @keyframes slideInUp {
                    from {
                        opacity: 0;
                        transform: translateY(30px);
                    }
                    to {
                        opacity: 1;
                        transform: translateY(0);
                    }
                }
                
                @media (max-width: 768px) {
                    .comparison-grid {
                        grid-template-columns: 1fr;
                    }
                    
                    .value-calculator,
                    .comparison-tool {
                        padding: 25px 20px;
                    }
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
})();