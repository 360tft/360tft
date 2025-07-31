// Product Interactions - 360TFT
// General interactive elements for all product pages

(function() {
    'use strict';
    
    document.addEventListener('DOMContentLoaded', function() {
        initProductInteractions();
        setupFAQToggles();
        setupStickyElements();
        setupFormEnhancements();
    });
    
    function initProductInteractions() {
        console.log('Product Interactions Initialized');
        enhanceUserInterface();
        setupScrollEffects();
    }
    
    function enhanceUserInterface() {
        // Add hover effects to cards
        const cards = document.querySelectorAll('.component-card, .testimonial-card, .story-card, .included-item');
        
        cards.forEach(card => {
            card.addEventListener('mouseenter', function() {
                this.style.transform = 'translateY(-5px)';
            });
            
            card.addEventListener('mouseleave', function() {
                this.style.transform = 'translateY(0)';
            });
        });
        
        // Enhance button interactions
        const buttons = document.querySelectorAll('.cta-purchase, .hero-cta, .upgrade-cta');
        
        buttons.forEach(button => {
            // Add ripple effect
            button.addEventListener('click', function(e) {
                createRippleEffect(e, this);
            });
        });
    }
    
    function createRippleEffect(event, element) {
        const ripple = document.createElement('span');
        const rect = element.getBoundingClientRect();
        const size = Math.max(rect.width, rect.height);
        const x = event.clientX - rect.left - size / 2;
        const y = event.clientY - rect.top - size / 2;
        
        ripple.style.cssText = `
            position: absolute;
            border-radius: 50%;
            background: rgba(255, 255, 255, 0.5);
            transform: scale(0);
            animation: ripple 0.6s linear;
            width: ${size}px;
            height: ${size}px;
            left: ${x}px;
            top: ${y}px;
        `;
        
        element.style.position = 'relative';
        element.style.overflow = 'hidden';
        element.appendChild(ripple);
        
        setTimeout(() => {
            ripple.remove();
        }, 600);
        
        // Add ripple animation if not exists
        if (!document.getElementById('ripple-animation')) {
            const style = document.createElement('style');
            style.id = 'ripple-animation';
            style.textContent = `
                @keyframes ripple {
                    to {
                        transform: scale(4);
                        opacity: 0;
                    }
                }
            `;
            document.head.appendChild(style);
        }
    }
    
    function setupFAQToggles() {
        const faqItems = document.querySelectorAll('.faq-item');
        
        faqItems.forEach(item => {
            const question = item.querySelector('.faq-question');
            const answer = item.querySelector('.faq-answer');
            
            if (question && answer) {
                question.addEventListener('click', function() {
                    const isActive = item.classList.contains('active');
                    
                    // Close all other FAQs
                    faqItems.forEach(otherItem => {
                        otherItem.classList.remove('active');
                        const otherAnswer = otherItem.querySelector('.faq-answer');
                        if (otherAnswer) {
                            otherAnswer.classList.remove('active');
                        }
                    });
                    
                    // Toggle current FAQ
                    if (!isActive) {
                        item.classList.add('active');
                        answer.classList.add('active');
                    }
                });
            }
        });
    }
    
    function setupStickyElements() {
        const stickyElements = document.querySelectorAll('.sticky-cta');
        
        stickyElements.forEach(element => {
            // Show sticky CTA after user scrolls past hero
            const heroSection = document.querySelector('.hero, .product-hero');
            
            if (heroSection) {
                const observer = new IntersectionObserver((entries) => {
                    entries.forEach(entry => {
                        if (entry.isIntersecting) {
                            element.classList.remove('show');
                        } else {
                            element.classList.add('show');
                        }
                    });
                });
                
                observer.observe(heroSection);
            }
        });
        
        // Add sticky CTA styles
        addStickyStyles();
    }
    
    function setupFormEnhancements() {
        // Enhance any forms on the page
        const forms = document.querySelectorAll('form');
        
        forms.forEach(form => {
            const inputs = form.querySelectorAll('input, textarea');
            
            inputs.forEach(input => {
                // Add floating label effect
                input.addEventListener('focus', function() {
                    this.parentElement.classList.add('focused');
                });
                
                input.addEventListener('blur', function() {
                    if (!this.value) {
                        this.parentElement.classList.remove('focused');
                    }
                });
                
                // Check if input has value on load
                if (input.value) {
                    input.parentElement.classList.add('focused');
                }
            });
        });
    }
    
    function setupScrollEffects() {
        // Parallax effect for hero sections
        const heroSections = document.querySelectorAll('.hero, .product-hero');
        
        heroSections.forEach(hero => {
            window.addEventListener('scroll', () => {
                const scrolled = window.pageYOffset;
                const rate = scrolled * -0.5;
                hero.style.transform = `translateY(${rate}px)`;
            });
        });
        
        // Progress indicator
        createScrollProgress();
    }
    
    function createScrollProgress() {
        const progressBar = document.createElement('div');
        progressBar.id = 'scroll-progress';
        progressBar.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 0%;
            height: 4px;
            background: linear-gradient(90deg, #976bdd, #ff5757);
            z-index: 9999;
            transition: width 0.1s ease;
        `;
        
        document.body.appendChild(progressBar);
        
        window.addEventListener('scroll', () => {
            const scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
            progressBar.style.width = scrollPercent + '%';
        });
    }
    
    function addStickyStyles() {
        if (document.getElementById('sticky-styles')) return;
        
        const styles = `
            <style id="sticky-styles">
                .sticky-cta {
                    opacity: 0;
                    transform: translateY(100px);
                    transition: all 0.4s ease;
                }
                
                .sticky-cta.show {
                    opacity: 1;
                    transform: translateY(0);
                }
                
                .form-group {
                    position: relative;
                    margin: 20px 0;
                }
                
                .form-group.focused label {
                    transform: translateY(-20px);
                    font-size: 0.9em;
                    color: #976bdd;
                }
                
                .form-group label {
                    position: absolute;
                    top: 15px;
                    left: 15px;
                    transition: all 0.3s ease;
                    pointer-events: none;
                    color: #666;
                }
                
                .form-group input,
                .form-group textarea {
                    width: 100%;
                    padding: 15px;
                    border: 2px solid #ddd;
                    border-radius: 8px;
                    font-size: 1em;
                    transition: border-color 0.3s ease;
                }
                
                .form-group input:focus,
                .form-group textarea:focus {
                    outline: none;
                    border-color: #976bdd;
                }
                
                @media (max-width: 768px) {
                    .sticky-cta {
                        font-size: 0.9em;
                        padding: 12px 20px;
                    }
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
})();