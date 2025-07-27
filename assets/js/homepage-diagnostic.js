// Homepage Problem-Solving Interactions

document.addEventListener('DOMContentLoaded', function() {
    
    // Problem indicator animations
    const problemItems = document.querySelectorAll('.problem-item');
    
    problemItems.forEach((item, index) => {
        item.style.animationDelay = `${index * 0.2}s`;
        item.classList.add('fade-in-up');
    });
    
    // Diagnostic button tracking
    const diagnosticButtons = document.querySelectorAll('[href*="Team-Diagnostic"]');
    
    diagnosticButtons.forEach(button => {
        button.addEventListener('click', function() {
            // Track diagnostic tool clicks
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    event_category: 'Diagnostic Tool',
                    event_label: 'Homepage CTA'
                });
            }
        });
    });
    
    // Emergency session tracking
    const emergencyLinks = document.querySelectorAll('.emergency-link');
    
    emergencyLinks.forEach(link => {
        link.addEventListener('click', function() {
            const problemType = this.closest('.emergency-card').querySelector('h3').textContent;
            
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    event_category: 'Emergency Help',
                    event_label: problemType
                });
            }
        });
    });
    
    // Academy CTA tracking
    const academyButtons = document.querySelectorAll('[href*="skool.com"]');
    
    academyButtons.forEach(button => {
        button.addEventListener('click', function() {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'click', {
                    event_category: 'Academy',
                    event_label: 'Homepage Join'
                });
            }
        });
    });
});

// Intersection Observer for animations
const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
};

const observer = new IntersectionObserver(function(entries) {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('animate-in');
        }
    });
}, observerOptions);

// Observe elements for animation
document.addEventListener('DOMContentLoaded', function() {
    const animateElements = document.querySelectorAll('.problem-card, .step-card, .tool-card, .emergency-card');
    
    animateElements.forEach(element => {
        observer.observe(element);
    });
});