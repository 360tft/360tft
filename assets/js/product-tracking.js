// Product Page Tracking - 360TFT
// Handles analytics and conversion tracking for product pages

(function() {
    'use strict';
    
    // Initialize product tracking when DOM is loaded
    document.addEventListener('DOMContentLoaded', function() {
        initProductTracking();
        trackPageView();
        setupCTATracking();
        setupScrollTracking();
    });
    
    function initProductTracking() {
        console.log('360TFT Product Tracking Initialized');
        
        // Track product page type
        const bodyClass = document.body.className;
        const productType = extractProductType(bodyClass);
        
        if (productType) {
            trackEvent('product_page_view', {
                product_type: productType,
                page_url: window.location.href
            });
        }
    }
    
    function extractProductType(bodyClass) {
        const classes = bodyClass.split(' ');
        for (let cls of classes) {
            if (cls.includes('-page')) {
                return cls.replace('-page', '');
            }
        }
        return null;
    }
    
    function trackPageView() {
        // Track page view with product context
        trackEvent('product_page_loaded', {
            timestamp: new Date().toISOString(),
            referrer: document.referrer,
            user_agent: navigator.userAgent
        });
    }
    
    function setupCTATracking() {
        // Track all CTA button clicks
        const ctaButtons = document.querySelectorAll('.cta-purchase, .hero-cta, .final-cta-button, .upgrade-cta');
        
        ctaButtons.forEach((button, index) => {
            button.addEventListener('click', function(e) {
                const buttonText = this.textContent.trim();
                const buttonLocation = getButtonLocation(this);
                
                trackEvent('cta_clicked', {
                    button_text: buttonText,
                    button_index: index,
                    button_location: buttonLocation,
                    product_page: extractProductType(document.body.className)
                });
                
                // Small delay to ensure tracking fires before navigation
                setTimeout(() => {
                    if (this.href) {
                        window.location.href = this.href;
                    }
                }, 100);
                
                e.preventDefault();
                return false;
            });
        });
    }
    
    function getButtonLocation(button) {
        // Determine button location on page
        const rect = button.getBoundingClientRect();
        const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
        
        if (scrollPercent < 25) return 'hero';
        if (scrollPercent < 50) return 'middle';
        if (scrollPercent < 75) return 'lower';
        return 'footer';
    }
    
    function setupScrollTracking() {
        let scrollMilestones = [25, 50, 75, 90];
        let trackedMilestones = [];
        
        window.addEventListener('scroll', throttle(function() {
            const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
            
            scrollMilestones.forEach(milestone => {
                if (scrollPercent >= milestone && !trackedMilestones.includes(milestone)) {
                    trackedMilestones.push(milestone);
                    trackEvent('scroll_milestone', {
                        milestone: milestone,
                        product_page: extractProductType(document.body.className)
                    });
                }
            });
        }, 1000));
    }
    
    function trackEvent(eventName, properties) {
        // Send to analytics service (placeholder for actual implementation)
        if (typeof gtag !== 'undefined') {
            gtag('event', eventName, properties);
        }
        
        // Console log for development
        console.log('360TFT Track Event:', eventName, properties);
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
    
})();