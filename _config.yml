// Homepage Specific Interactions and Animations
// Integrates with main.js global utilities

document.addEventListener('DOMContentLoaded', function() {
    initializeHomepageFeatures();
});

function initializeHomepageFeatures() {
    initializeProductCards();
    initializeNewsletterForm();
    initializeStatCounters();
    initializeScrollAnimations();
    initializeHeroAnimations();
}

// Enhanced Product Card Interactions
function initializeProductCards() {
    const cards = document.querySelectorAll('.product-card');
    
    cards.forEach(card => {
        // Enhanced hover effects
        card.addEventListener('mouseenter', function() {
            this.style.transform = 'translateY(-8px) scale(1.02)';
            
            // Animate the icon
            const icon = this.querySelector('.product-icon');
            if (icon) {
                icon.style.transform = 'scale(1.15) rotate(10deg)';
            }
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'translateY(0) scale(1)';
            
            // Reset icon
            const icon = this.querySelector('.product-icon');
            if (icon) {
                icon.style.transform = 'scale(1) rotate(0deg)';
            }
        });

        // Track card interactions
        card.addEventListener('click', function(e) {
            const productName = this.querySelector('h3')?.textContent || 'Unknown Product';
            
            // Track with global analytics if available
            if (typeof TFTUtilities !== 'undefined') {
                TFTUtilities.trackEvent('Product Card', 'Click', productName);
            }
        });
    });
}

// Newsletter Form Enhancement
function initializeNewsletterForm() {
    const form = document.querySelector('.newsletter-form');
    const input = form?.querySelector('.newsletter-input');
    const button = form?.querySelector('.newsletter-submit');
    
    if (!form) return;

    // Enhanced form validation
    input?.addEventListener('input', function() {
        const email = this.value;
        const isValid = validateEmail(email);
        
        // Visual feedback
        this.style.borderColor = email ? (isValid ? '#4CAF50' : '#f44336') : '';
        
        // Update button state
        if (button) {
            button.disabled = !isValid;
            button.style.opacity = isValid ? '1' : '0.6';
        }
    });
    
    form.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const email = input?.value;
        if (!validateEmail(email)) {
            showNotification('Please enter a valid email address', 'error');
            return;
        }

        // Show loading state
        const originalText = button?.textContent;
        if (button) {
            button.textContent = 'Subscribing...';
            button.classList.add('loading');
        }

        // Simulate API call (replace with actual newsletter service)
        setTimeout(() => {
            // Track newsletter signup
            if (typeof TFTUtilities !== 'undefined') {
                TFTUtilities.trackEvent('Newsletter', 'Homepage Signup', email);
            }
            
            // Show success message
            showNotification('Thanks for subscribing! Welcome to the 360TFT coaching community.', 'success');
            form.reset();
            
            // Reset button
            if (button) {
                button.textContent = originalText;
                button.classList.remove('loading');
                button.disabled = true;
                button.style.opacity = '0.6';
            }
        }, 1500);
    });
}

// Animated Stat Counters
function initializeStatCounters() {
    const stats = document.querySelectorAll('.credential-number');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting && !entry.target.dataset.animated) {
                animateCounter(entry.target);
            }
        });
    }, {
        threshold: 0.5,
        rootMargin: '0px 0px -50px 0px'
    });
    
    stats.forEach(stat => observer.observe(stat));
}

function animateCounter(element) {
    const finalText = element.textContent;
    const numberMatch = finalText.match(/(\d+)/);
    
    if (!numberMatch) return;
    
    const number = parseInt(numberMatch[1]);
    const suffix = finalText.replace(/\d+/, '');
    
    let current = 0;
    const increment = Math.ceil(number / 50);
    const duration = 2000; // 2 seconds
    const stepTime = duration / (number / increment);
    
    const timer = setInterval(() => {
        current += increment;
        if (current >= number) {
            element.textContent = finalText;
            clearInterval(timer);
            element.dataset.animated = 'true';
            
            // Add completion animation
            element.style.transform = 'scale(1.1)';
            setTimeout(() => {
                element.style.transform = 'scale(1)';
            }, 200);
        } else {
            element.textContent = current + suffix;
        }
    }, stepTime);
}

// Scroll-based Animations
function initializeScrollAnimations() {
    const animatedElements = document.querySelectorAll('.product-card, .credential-item, .resource-card');
    
    // Add animation classes
    animatedElements.forEach(el => {
        el.classList.add('animate-on-scroll');
    });
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    });
    
    animatedElements.forEach(el => observer.observe(el));
}

// Hero Section Enhancements
function initializeHeroAnimations() {
    const heroContent = document.querySelector('.hero-content');
    const heroElements = heroContent?.querySelectorAll('.hero-badge, h1, .hero-subtitle, .hero-description, .hero-cta-group, .social-proof');
    
    if (!heroElements) return;
    
    // Staggered entrance animation
    heroElements.forEach((element, index) => {
        element.style.opacity = '0';
        element.style.transform = 'translateY(30px)';
        element.style.transition = 'all 0.8s ease';
        
        setTimeout(() => {
            element.style.opacity = '1';
            element.style.transform = 'translateY(0)';
        }, index * 200);
    });
    
    // Parallax effect for hero background
    let ticking = false;
    
    function updateParallax() {
        const scrolled = window.pageYOffset;
        const parallax = document.querySelector('.hero::before');
        const hero = document.querySelector('.hero');
        
        if (hero && scrolled < hero.offsetHeight) {
            const speed = scrolled * -0.5;
            hero.style.transform = `translateY(${speed}px)`;
        }
        
        ticking = false;
    }
    
    function requestTick() {
        if (!ticking) {
            requestAnimationFrame(updateParallax);
            ticking = true;
        }
    }
    
    window.addEventListener('scroll', requestTick, { passive: true });
}

// Utility Functions
function validateEmail(email) {
    const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return re.test(email);
}

function showNotification(message, type = 'info') {
    // Create notification element
    const notification = document.createElement('div');
    notification.className = `notification notification--${type}`;
    notification.textContent = message;
    
    // Style the notification
    Object.assign(notification.style, {
        position: 'fixed',
        top: '20px',
        right: '20px',
        padding: '15px 20px',
        borderRadius: '8px',
        color: 'white',
        fontWeight: 'bold',
        zIndex: '10000',
        transform: 'translateX(400px)',
        transition: 'transform 0.3s ease',
        backgroundColor: type === 'success' ? '#4CAF50' : type === 'error' ? '#f44336' : '#2196F3'
    });
    
    document.body.appendChild(notification);
    
    // Animate in
    setTimeout(() => {
        notification.style.transform = 'translateX(0)';
    }, 100);
    
    // Auto remove
    setTimeout(() => {
        notification.style.transform = 'translateX(400px)';
        setTimeout(() => {
            if (notification.parentNode) {
                notification.parentNode.removeChild(notification);
            }
        }, 300);
    }, 4000);
}

// Kevin Photo Easter Egg
function initializeKevinPhotoEasterEgg() {
    const kevinPhoto = document.querySelector('.kevin-photo');
    let clickCount = 0;
    
    if (kevinPhoto) {
        kevinPhoto.addEventListener('click', function() {
            clickCount++;
            
            if (clickCount === 1) {
                this.style.transform = 'rotate(5deg) scale(1.05)';
                setTimeout(() => {
                    this.style.transform = 'rotate(0deg) scale(1)';
                }, 300);
            } else if (clickCount === 3) {
                // Easter egg: Show motivational quote
                showNotification("\"The best coaches make themselves obsolete\" - Kevin", 'info');
                clickCount = 0;
            }
        });
    }
}

// Initialize easter egg
document.addEventListener('DOMContentLoaded', function() {
    setTimeout(initializeKevinPhotoEasterEgg, 1000);
});

// Export functions for potential use by other scripts
if (typeof window.HomepageInteractions === 'undefined') {
    window.HomepageInteractions = {
        initializeProductCards,
        initializeNewsletterForm,
        initializeStatCounters,
        validateEmail,
        showNotification
    };
}