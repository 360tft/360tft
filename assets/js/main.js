/**
 * 360TFT Main JavaScript File
 * Contains all shared functionality across the site
 */

(function() {
    'use strict';

    // Global variables
    let mobileMenuOpen = false;
    let scrollPosition = 0;

    // Initialize when DOM is loaded
    document.addEventListener('DOMContentLoaded', function() {
        initializeNavigation();
        initializeScrollEffects();
        initializeSmoothScrolling();
        initializeAnimations();
        initializeBackToTop();
        initializeAnalytics();
        initializeMobileMenu();
    });

    /**
     * Navigation functionality
     */
    function initializeNavigation() {
        const nav = document.querySelector('.header-nav');
        
        // Scroll effect for navigation
        window.addEventListener('scroll', function() {
            if (window.scrollY > 100) {
                nav.style.backgroundColor = 'rgba(255, 255, 255, 0.95)';
                nav.style.backdropFilter = 'blur(10px)';
            } else {
                nav.style.backgroundColor = '#ffffff';
                nav.style.backdropFilter = 'none';
            }
        });

        // Highlight active navigation item
        highlightActiveNavItem();
    }

    /**
     * Highlight active navigation item based on current page
     */
    function highlightActiveNavItem() {
        const currentPath = window.location.pathname;
        const navLinks = document.querySelectorAll('.nav-link');
        
        navLinks.forEach(link => {
            const linkPath = new URL(link.href).pathname;
            if (currentPath === linkPath || currentPath.startsWith(linkPath + '/')) {
                link.classList.add('active');
            }
        });
    }

    /**
     * Mobile menu functionality
     */
    function initializeMobileMenu() {
        const mobileMenuBtn = document.getElementById('mobile-menu-btn');
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileMenuClose = document.getElementById('mobile-menu-close');
        const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');

        if (!mobileMenuBtn || !mobileMenuOverlay) return;

        // Open mobile menu
        mobileMenuBtn.addEventListener('click', function() {
            openMobileMenu();
        });

        // Close mobile menu
        if (mobileMenuClose) {
            mobileMenuClose.addEventListener('click', function() {
                closeMobileMenu();
            });
        }

        // Close menu when clicking overlay
        mobileMenuOverlay.addEventListener('click', function(e) {
            if (e.target === mobileMenuOverlay) {
                closeMobileMenu();
            }
        });

        // Close menu when clicking nav links
        mobileNavLinks.forEach(link => {
            link.addEventListener('click', function() {
                closeMobileMenu();
            });
        });

        // Close menu on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape' && mobileMenuOpen) {
                closeMobileMenu();
            }
        });
    }

    function openMobileMenu() {
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const hamburgerLines = document.querySelectorAll('.hamburger-line');
        
        mobileMenuOverlay.style.display = 'block';
        document.body.style.overflow = 'hidden';
        mobileMenuOpen = true;

        // Animate hamburger to X
        hamburgerLines[0].style.transform = 'rotate(45deg) translate(5px, 5px)';
        hamburgerLines[1].style.opacity = '0';
        hamburgerLines[2].style.transform = 'rotate(-45deg) translate(7px, -6px)';

        // Animate menu in
        setTimeout(() => {
            mobileMenuOverlay.style.opacity = '1';
        }, 10);
    }

    function closeMobileMenu() {
        const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
        const hamburgerLines = document.querySelectorAll('.hamburger-line');
        
        mobileMenuOverlay.style.opacity = '0';
        document.body.style.overflow = '';
        mobileMenuOpen = false;

        // Reset hamburger
        hamburgerLines.forEach(line => {
            line.style.transform = '';
            line.style.opacity = '';
        });

        // Hide menu after animation
        setTimeout(() => {
            mobileMenuOverlay.style.display = 'none';
        }, 300);
    }

    /**
     * Smooth scrolling for anchor links
     */
    function initializeSmoothScrolling() {
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function(e) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute('href'));
                if (target) {
                    const offsetTop = target.offsetTop - 80; // Account for fixed header
                    window.scrollTo({
                        top: offsetTop,
                        behavior: 'smooth'
                    });
                }
            });
        });
    }

    /**
     * Scroll effects and parallax
     */
    function initializeScrollEffects() {
        // Throttle scroll events for performance
        let ticking = false;

        function updateScrollEffects() {
            scrollPosition = window.scrollY;
            
            // Add scroll-based effects here
            updateProgressBar();
            
            ticking = false;
        }

        window.addEventListener('scroll', function() {
            if (!ticking) {
                requestAnimationFrame(updateScrollEffects);
                ticking = true;
            }
        });
    }

    /**
     * Update reading progress bar (if exists)
     */
    function updateProgressBar() {
        const progressBar = document.querySelector('.reading-progress');
        if (progressBar) {
            const docHeight = document.documentElement.scrollHeight - window.innerHeight;
            const progress = (scrollPosition / docHeight) * 100;
            progressBar.style.width = `${Math.min(progress, 100)}%`;
        }
    }

    /**
     * Initialize animations and intersection observer
     */
    function initializeAnimations() {
        // Intersection Observer for fade-in animations
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                }
            });
        }, observerOptions);

        // Observe elements with fade-in class
        document.querySelectorAll('.fade-in').forEach(el => {
            observer.observe(el);
        });

        // Auto-add fade-in class to common elements
        const autoFadeElements = document.querySelectorAll('.card, .testimonial, .stats .stat-item');
        autoFadeElements.forEach(el => {
            el.classList.add('fade-in');
            observer.observe(el);
        });
    }

    /**
     * Back to top button functionality
     */
    function initializeBackToTop() {
        const backToTopBtn = document.getElementById('back-to-top');
        
        if (!backToTopBtn) return;

        // Show/hide button based on scroll position
        window.addEventListener('scroll', function() {
            if (window.scrollY > 300) {
                backToTopBtn.style.display = 'block';
                setTimeout(() => {
                    backToTopBtn.style.opacity = '1';
                }, 10);
            } else {
                backToTopBtn.style.opacity = '0';
                setTimeout(() => {
                    if (window.scrollY <= 300) {
                        backToTopBtn.style.display = 'none';
                    }
                }, 300);
            }
        });

        // Scroll to top when clicked
        backToTopBtn.addEventListener('click', function() {
            window.scrollTo({
                top: 0,
                behavior: 'smooth'
            });
        });
    }

    /**
     * Analytics and tracking
     */
    function initializeAnalytics() {
        // Track CTA clicks
        document.querySelectorAll('.hero-cta, .btn-primary, .btn-accent, .nav-cta').forEach(button => {
            button.addEventListener('click', function() {
                trackEvent('CTA', 'Click', this.textContent.trim());
            });
        });

        // Track scroll depth
        trackScrollDepth();

        // Track time on page
        trackTimeOnPage();
    }

    /**
     * Track scroll depth milestones
     */
    function trackScrollDepth() {
        let maxScroll = 0;
        const milestones = [25, 50, 75, 100];
        const tracked = [];

        window.addEventListener('scroll', function() {
            const scrollPercent = Math.round((window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100);
            
            if (scrollPercent > maxScroll) {
                maxScroll = scrollPercent;
                
                milestones.forEach(milestone => {
                    if (scrollPercent >= milestone && !tracked.includes(milestone)) {
                        tracked.push(milestone);
                        trackEvent('Time on Page', 'Milestone', `${milestone}s`);
                }
            });
        }, 5000); // Check every 5 seconds
    }

    /**
     * Generic event tracking function
     */
    function trackEvent(category, action, label) {
        // Google Analytics 4
        if (typeof gtag !== 'undefined') {
            gtag('event', action, {
                event_category: category,
                event_label: label
            });
        }

        // Facebook Pixel
        if (typeof fbq !== 'undefined') {
            fbq('track', 'CustomEvent', {
                category: category,
                action: action,
                label: label
            });
        }

        // Console log for development
        if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
            console.log('Event tracked:', { category, action, label });
        }
    }

    /**
     * Form handling utilities
     */
    function initializeFormHandling() {
        // Newsletter forms
        const newsletterForms = document.querySelectorAll('.newsletter-form');
        newsletterForms.forEach(form => {
            form.addEventListener('submit', handleNewsletterSubmit);
        });

        // Contact forms
        const contactForms = document.querySelectorAll('.contact-form');
        contactForms.forEach(form => {
            form.addEventListener('submit', handleContactSubmit);
        });
    }

    /**
     * Handle newsletter form submission
     */
    function handleNewsletterSubmit(e) {
        e.preventDefault();
        const form = e.target;
        const email = form.querySelector('input[type="email"]').value;
        
        // Basic email validation
        if (!isValidEmail(email)) {
            showFormMessage(form, 'Please enter a valid email address.', 'error');
            return;
        }

        // Show loading state
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Subscribing...';
        submitBtn.disabled = true;

        // Track subscription attempt
        trackEvent('Newsletter', 'Subscribe Attempt', email);

        // Simulate form submission (replace with actual endpoint)
        setTimeout(() => {
            showFormMessage(form, 'Thanks for subscribing! Welcome to the 360TFT community.', 'success');
            form.reset();
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            
            // Track successful subscription
            trackEvent('Newsletter', 'Subscribe Success', email);
        }, 2000);
    }

    /**
     * Handle contact form submission
     */
    function handleContactSubmit(e) {
        e.preventDefault();
        const form = e.target;
        
        // Show loading state
        const submitBtn = form.querySelector('button[type="submit"]');
        const originalText = submitBtn.textContent;
        submitBtn.textContent = 'Sending...';
        submitBtn.disabled = true;

        // Track contact attempt
        trackEvent('Contact', 'Form Submit', 'Contact Form');

        // Simulate form submission (replace with actual endpoint)
        setTimeout(() => {
            showFormMessage(form, 'Message sent successfully! We\'ll get back to you soon.', 'success');
            form.reset();
            submitBtn.textContent = originalText;
            submitBtn.disabled = false;
            
            // Track successful contact
            trackEvent('Contact', 'Form Success', 'Contact Form');
        }, 2000);
    }

    /**
     * Show form success/error messages
     */
    function showFormMessage(form, message, type) {
        // Remove existing messages
        const existingMessage = form.querySelector('.form-message');
        if (existingMessage) {
            existingMessage.remove();
        }

        // Create new message
        const messageElement = document.createElement('div');
        messageElement.className = `form-message form-message-${type}`;
        messageElement.textContent = message;
        
        // Style the message
        messageElement.style.cssText = `
            padding: 15px;
            margin-top: 15px;
            border-radius: 8px;
            font-weight: 500;
            ${type === 'success' 
                ? 'background: #e8f5e8; color: #2e7d32; border: 1px solid #4caf50;' 
                : 'background: #ffebee; color: #c62828; border: 1px solid #f44336;'
            }
        `;

        form.appendChild(messageElement);

        // Remove message after 5 seconds
        setTimeout(() => {
            messageElement.remove();
        }, 5000);
    }

    /**
     * Email validation utility
     */
    function isValidEmail(email) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return emailRegex.test(email);
    }

    /**
     * Initialize FAQ functionality
     */
    function initializeFAQ() {
        const faqQuestions = document.querySelectorAll('.faq-question');
        
        faqQuestions.forEach(question => {
            question.addEventListener('click', function() {
                const answer = this.nextElementSibling;
                const isActive = answer.classList.contains('active');
                
                // Close all FAQ answers
                document.querySelectorAll('.faq-answer').forEach(item => {
                    item.classList.remove('active');
                    item.style.maxHeight = '0';
                });

                // Open clicked FAQ if it wasn't active
                if (!isActive) {
                    answer.classList.add('active');
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                }

                // Track FAQ interaction
                trackEvent('FAQ', 'Question Click', this.textContent.trim());
            });
        });
    }

    /**
     * Initialize modal functionality
     */
    function initializeModals() {
        // Modal triggers
        const modalTriggers = document.querySelectorAll('[data-modal]');
        modalTriggers.forEach(trigger => {
            trigger.addEventListener('click', function(e) {
                e.preventDefault();
                const modalId = this.getAttribute('data-modal');
                openModal(modalId);
            });
        });

        // Modal close buttons
        const modalCloses = document.querySelectorAll('.modal-close');
        modalCloses.forEach(close => {
            close.addEventListener('click', function() {
                const modal = this.closest('.modal');
                closeModal(modal.id);
            });
        });

        // Close modal on overlay click
        const modalOverlays = document.querySelectorAll('.modal-overlay');
        modalOverlays.forEach(overlay => {
            overlay.addEventListener('click', function(e) {
                if (e.target === overlay) {
                    const modal = overlay.closest('.modal');
                    closeModal(modal.id);
                }
            });
        });

        // Close modal on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const openModal = document.querySelector('.modal.active');
                if (openModal) {
                    closeModal(openModal.id);
                }
            }
        });
    }

    /**
     * Open modal by ID
     */
    function openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;

        modal.classList.add('active');
        document.body.style.overflow = 'hidden';
        
        // Track modal open
        trackEvent('Modal', 'Open', modalId);
    }

    /**
     * Close modal by ID
     */
    function closeModal(modalId) {
        const modal = document.getElementById(modalId);
        if (!modal) return;

        modal.classList.remove('active');
        document.body.style.overflow = '';
        
        // Track modal close
        trackEvent('Modal', 'Close', modalId);
    }

    /**
     * Initialize price calculator (if exists)
     */
    function initializePriceCalculator() {
        const calculator = document.querySelector('.price-calculator');
        if (!calculator) return;

        const inputs = calculator.querySelectorAll('input, select');
        const totalElement = calculator.querySelector('.total-price');

        inputs.forEach(input => {
            input.addEventListener('change', updatePriceCalculation);
        });

        function updatePriceCalculation() {
            // This would contain your specific pricing logic
            // Example implementation:
            let total = 0;
            
            inputs.forEach(input => {
                const value = parseFloat(input.value) || 0;
                const price = parseFloat(input.dataset.price) || 0;
                total += value * price;
            });

            if (totalElement) {
                totalElement.textContent = `£${total.toFixed(2)}`;
            }
        }
    }

    /**
     * Initialize countdown timers
     */
    function initializeCountdowns() {
        const countdowns = document.querySelectorAll('.countdown');
        
        countdowns.forEach(countdown => {
            const endDate = new Date(countdown.dataset.endDate).getTime();
            
            const timer = setInterval(() => {
                const now = new Date().getTime();
                const distance = endDate - now;

                if (distance < 0) {
                    clearInterval(timer);
                    countdown.innerHTML = "EXPIRED";
                    return;
                }

                const days = Math.floor(distance / (1000 * 60 * 60 * 24));
                const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                const seconds = Math.floor((distance % (1000 * 60)) / 1000);

                countdown.innerHTML = `
                    <span class="countdown-item">
                        <span class="countdown-number">${days}</span>
                        <span class="countdown-label">Days</span>
                    </span>
                    <span class="countdown-item">
                        <span class="countdown-number">${hours}</span>
                        <span class="countdown-label">Hours</span>
                    </span>
                    <span class="countdown-item">
                        <span class="countdown-number">${minutes}</span>
                        <span class="countdown-label">Minutes</span>
                    </span>
                    <span class="countdown-item">
                        <span class="countdown-number">${seconds}</span>
                        <span class="countdown-label">Seconds</span>
                    </span>
                `;
            }, 1000);
        });
    }

    /**
     * Initialize lazy loading for images
     */
    function initializeLazyLoading() {
        const images = document.querySelectorAll('img[data-src]');
        
        const imageObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const img = entry.target;
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    imageObserver.unobserve(img);
                }
            });
        });

        images.forEach(img => imageObserver.observe(img));
    }

    /**
     * Utility function to debounce function calls
     */
    function debounce(func, wait) {
        let timeout;
        return function executedFunction(...args) {
            const later = () => {
                clearTimeout(timeout);
                func(...args);
            };
            clearTimeout(timeout);
            timeout = setTimeout(later, wait);
        };
    }

    /**
     * Utility function to throttle function calls
     */
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
        };
    }

    // Initialize additional components when DOM is ready
    document.addEventListener('DOMContentLoaded', function() {
        initializeFormHandling();
        initializeFAQ();
        initializeModals();
        initializePriceCalculator();
        initializeCountdowns();
        initializeLazyLoading();
    });

    // Expose utility functions globally if needed
    window.TFTUtilities = {
        trackEvent,
        openModal,
        closeModal,
        debounce,
        throttle,
        isValidEmail
    };

})();('Scroll Depth', 'Milestone', `${milestone}%`);
                    }
                });
            }
        });
    }

    /**
     * Track time on page
     */
    function trackTimeOnPage() {
        const startTime = Date.now();
        const milestones = [30, 60, 120, 300]; // seconds
        const tracked = [];

        setInterval(() => {
            const timeOnPage = Math.floor((Date.now() - startTime) / 1000);
            
            milestones.forEach(milestone => {
                if (timeOnPage >= milestone && !tracked.includes(milestone)) {
                    tracked.push(milestone);
                    trackEvent