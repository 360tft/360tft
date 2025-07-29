/* Testimonials Page JavaScript */
/* File: /assets/js/pages/testimonials.js */

// Initialize testimonials page functionality
document.addEventListener('DOMContentLoaded', function() {
    
    // Smooth scrolling for anchor links
    initSmoothScrolling();
    
    // Initialize testimonial card animations
    initTestimonialAnimations();
    
    // Initialize CTA tracking
    initCTATracking();
});

/**
 * Initialize smooth scrolling for anchor links
 */
function initSmoothScrolling() {
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
}

/**
 * Initialize testimonial card hover animations
 */
function initTestimonialAnimations() {
    const observerCallback = (entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    };
    
    const observer = new IntersectionObserver(observerCallback, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    // Observe testimonial cards for animation
    document.querySelectorAll('.testimonial-card').forEach(card => {
        card.style.opacity = '0';
        card.style.transform = 'translateY(30px)';
        card.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
        observer.observe(card);
    });
}

/**
 * Initialize CTA click tracking
 */
function initCTATracking() {
    document.querySelectorAll('.cta-button').forEach(button => {
        button.addEventListener('click', function() {
            // Track CTA clicks for analytics
            const buttonText = this.textContent.trim();
            const destination = this.href;
            
            // Send tracking event (if analytics is available)
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    event_category: 'CTA',
                    event_label: buttonText,
                    custom_parameter_destination: destination
                });
            }
            
            // Facebook Pixel tracking (if available)
            if (typeof fbq !== 'undefined') {
                fbq('track', 'Lead', {
                    content_name: 'Testimonials CTA',
                    content_category: 'Social Proof'
                });
            }
        });
    });
}