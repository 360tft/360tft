// Academy Tracking - 360TFT
// Specialized tracking for Football Coaching Academy page

(function() {
    'use strict';
    
    document.addEventListener('DOMContentLoaded', function() {
        initAcademyTracking();
        trackMembershipInterest();
        setupPricingAnalytics();
        monitorEngagement();
    });
    
    function initAcademyTracking() {
        console.log('Academy Tracking Initialized');
        trackPageEntry();
        setupConversionTracking();
    }
    
    function trackPageEntry() {
        // Track how users arrived at academy page
        const referrer = document.referrer;
        const utmParams = getUTMParameters();
        
        trackEvent('academy_page_view', {
            referrer: referrer,
            utm_source: utmParams.source,
            utm_medium: utmParams.medium,
            utm_campaign: utmParams.campaign,
            timestamp: new Date().toISOString()
        });
    }
    
    function getUTMParameters() {
        const urlParams = new URLSearchParams(window.location.search);
        return {
            source: urlParams.get('utm_source'),
            medium: urlParams.get('utm_medium'),
            campaign: urlParams.get('utm_campaign'),
            content: urlParams.get('utm_content'),
            term: urlParams.get('utm_term')
        };
    }
    
    function trackMembershipInterest() {
        // Track pricing plan interactions
        const pricingCards = document.querySelectorAll('.pricing-card');
        
        pricingCards.forEach((card, index) => {
            // Track pricing card views
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        trackEvent('pricing_card_viewed', {
                            plan_type: index === 0 ? 'monthly' : 'annual',
                            card_index: index
                        });
                    }
                });
            }, { threshold: 0.5 });
            
            observer.observe(card);
            
            // Track hover interactions
            card.addEventListener('mouseenter', function() {
                trackEvent('pricing_card_hover', {
                    plan_type: index === 0 ? 'monthly' : 'annual',
                    hover_duration_start: Date.now()
                });
            });
            
            card.addEventListener('mouseleave', function() {
                trackEvent('pricing_card_hover_end', {
                    plan_type: index === 0 ? 'monthly' : 'annual',
                    hover_duration_end: Date.now()
                });
            });
        });
    }
    
    function setupConversionTracking() {
        // Track all CTA interactions
        const ctaButtons = document.querySelectorAll('[href*="academy"], .academy-cta, .join-cta');
        
        ctaButtons.forEach((button, index) => {
            button.addEventListener('click', function(e) {
                const buttonText = this.textContent.trim();
                const buttonLocation = getElementLocation(this);
                const planType = determinePlanType(this);
                
                trackEvent('academy_cta_clicked', {
                    button_text: buttonText,
                    button_index: index,
                    button_location: buttonLocation,
                    plan_type: planType,
                    scroll_percentage: getScrollPercentage()
                });
                
                // Track conversion funnel step
                trackConversionStep('cta_click', {
                    plan_type: planType,
                    button_location: buttonLocation
                });
            });
        });
    }
    
    function determinePlanType(element) {
        const elementText = element.textContent.toLowerCase();
        const closestCard = element.closest('.pricing-card');
        
        if (closestCard) {
            const cardText = closestCard.textContent.toLowerCase();
            if (cardText.includes('annual') || cardText.includes('yearly')) {
                return 'annual';
            }
            if (cardText.includes('monthly')) {
                return 'monthly';
            }
        }
        
        if (elementText.includes('annual') || elementText.includes('yearly')) {
            return 'annual';
        }
        
        return 'monthly'; // default
    }
    
    function setupPricingAnalytics() {
        // Track pricing comparison interactions
        const pricingToggles = document.querySelectorAll('.pricing-toggle, .plan-toggle');
        
        pricingToggles.forEach(toggle => {
            toggle.addEventListener('change', function() {
                trackEvent('pricing_toggle_switched', {
                    toggle_to: this.checked ? 'annual' : 'monthly',
                    timestamp: new Date().toISOString()
                });
            });
        });
        
        // Track value proposition views
        const valueElements = document.querySelectorAll('.value-item, .benefit-item, .feature-item');
        
        valueElements.forEach((element, index) => {
            const observer = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const valueText = element.textContent.trim().substring(0, 50);
                        trackEvent('value_proposition_viewed', {
                            value_index: index,
                            value_text: valueText
                        });
                    }
                });
            }, { threshold: 0.7 });
            
            observer.observe(element);
        });
    }
    
    function monitorEngagement() {
        // Track time spent on page
        const startTime = Date.now();
        let maxScrollDepth = 0;
        
        // Track scroll depth
        window.addEventListener('scroll', throttle(function() {
            const scrollDepth = getScrollPercentage();
            if (scrollDepth > maxScrollDepth) {
                maxScrollDepth = scrollDepth;
            }
        }, 1000));
        
        // Track testimonial interactions
        const testimonials = document.querySelectorAll('.story-card, .testimonial-card');
        testimonials.forEach((testimonial, index) => {
            testimonial.addEventListener('click', function() {
                const authorName = this.querySelector('.story-author, .testimonial-author')?.textContent || 'Unknown';
                trackEvent('testimonial_clicked', {
                    testimonial_index: index,
                    author_name: authorName
                });
            });
        });
        
        // Track engagement before page unload
        window.addEventListener('beforeunload', function() {
            const timeOnPage = Date.now() - startTime;
            trackEvent('academy_page_exit', {
                time_on_page: timeOnPage,
                max_scroll_depth: maxScrollDepth,
                page_url: window.location.href
            });
        });
        
        // Track FAQ interactions
        const faqQuestions = document.querySelectorAll('.faq-question');
        faqQuestions.forEach((question, index) => {
            question.addEventListener('click', function() {
                const questionText = this.textContent.trim().substring(0, 100);
                trackEvent('faq_question_clicked', {
                    question_index: index,
                    question_text: questionText
                });
            });
        });
    }
    
    function trackConversionStep(step, additionalData = {}) {
        trackEvent('academy_conversion_funnel', {
            step: step,
            timestamp: new Date().toISOString(),
            ...additionalData
        });
    }
    
    function getElementLocation(element) {
        const rect = element.getBoundingClientRect();
        const scrollPercent = getScrollPercentage();
        
        if (scrollPercent < 25) return 'hero';
        if (scrollPercent < 50) return 'features';
        if (scrollPercent < 75) return 'testimonials';
        return 'pricing';
    }
    
    function getScrollPercentage() {
        const scrollTop = window.scrollY;
        const scrollHeight = document.body.scrollHeight - window.innerHeight;
        return (scrollTop / scrollHeight) * 100;
    }
    
    function trackEvent(eventName, properties) {
        // Send to analytics service
        if (typeof gtag !== 'undefined') {
            gtag('event', eventName, properties);
        }
        
        // Send to custom analytics if available
        if (typeof window.analytics !== 'undefined') {
            window.analytics.track(eventName, properties);
        }
        
        // Console log for development
        console.log('Academy Track Event:', eventName, properties);
        
        // Store in localStorage for debugging
        try {
            const events = JSON.parse(localStorage.getItem('academy_events') || '[]');
            events.push({
                event: eventName,
                properties: properties,
                timestamp: new Date().toISOString()
            });
            
            // Keep only last 50 events
            if (events.length > 50) {
                events.splice(0, events.length - 50);
            }
            
            localStorage.setItem('academy_events', JSON.stringify(events));
        } catch (e) {
            console.warn('Could not store academy event:', e);
        }
    }
    
    function throttle(func, limit) {
        let inThrottle;
        return function() {
            const args = arguments;
            const context = this;
            if (!inThrottle) {
                func.apply(context, args);
                inThrottle = true;
                setTimeout(() => inThrottle = false, limit);
            }
        }
    }
    
    // Export for debugging
    window.AcademyTracking = {
        trackEvent: trackEvent,
        getScrollPercentage: getScrollPercentage,
        getEngagementData: function() {
            try {
                return JSON.parse(localStorage.getItem('academy_events') || '[]');
            } catch (e) {
                return [];
            }
        }
    };
    
})();