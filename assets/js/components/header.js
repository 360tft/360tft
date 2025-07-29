// Header Navigation JavaScript
document.addEventListener('DOMContentLoaded', function() {
    // Mobile menu elements
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenuOverlay = document.getElementById('mobile-menu-overlay');
    const mobileMenuClose = document.getElementById('mobile-menu-close');
    const headerNav = document.getElementById('header-nav');
    
    // Mobile menu toggle functionality
    if (mobileMenuBtn && mobileMenuOverlay) {
        mobileMenuBtn.addEventListener('click', function() {
            mobileMenuOverlay.classList.add('active');
            document.body.style.overflow = 'hidden'; // Prevent background scrolling
        });
    }
    
    if (mobileMenuClose && mobileMenuOverlay) {
        mobileMenuClose.addEventListener('click', function() {
            mobileMenuOverlay.classList.remove('active');
            document.body.style.overflow = ''; // Restore scrolling
        });
    }
    
    // Close mobile menu when clicking overlay
    if (mobileMenuOverlay) {
        mobileMenuOverlay.addEventListener('click', function(e) {
            if (e.target === mobileMenuOverlay) {
                mobileMenuOverlay.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    }
    
    // Close mobile menu when clicking navigation links
    const mobileNavLinks = document.querySelectorAll('.mobile-nav-link');
    mobileNavLinks.forEach(function(link) {
        link.addEventListener('click', function() {
            if (mobileMenuOverlay) {
                mobileMenuOverlay.classList.remove('active');
                document.body.style.overflow = '';
            }
        });
    });
    
    // Header scroll effect
    if (headerNav) {
        window.addEventListener('scroll', function() {
            if (window.scrollY > 10) {
                headerNav.classList.add('scrolled');
            } else {
                headerNav.classList.remove('scrolled');
            }
        });
    }
    
    // Hamburger menu animation
    if (mobileMenuBtn) {
        const hamburgerLines = mobileMenuBtn.querySelectorAll('.hamburger-line');
        
        mobileMenuBtn.addEventListener('click', function() {
            hamburgerLines.forEach(function(line, index) {
                line.style.transform = index === 0 ? 'rotate(45deg) translate(6px, 6px)' :
                                     index === 1 ? 'opacity(0)' :
                                     'rotate(-45deg) translate(6px, -6px)';
            });
        });
        
        if (mobileMenuClose) {
            mobileMenuClose.addEventListener('click', function() {
                hamburgerLines.forEach(function(line) {
                    line.style.transform = '';
                    line.style.opacity = '';
                });
            });
        }
    }
    
    // Game Model badge pulse effect (enhanced)
    const navBadge = document.querySelector('.nav-badge');
    if (navBadge) {
        // Add extra attention after page load
        setTimeout(function() {
            navBadge.style.animation = 'pulse-badge 1s ease-in-out 3';
        }, 1000);
    }
    
    // Smooth scroll for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(function(anchor) {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const headerHeight = headerNav ? headerNav.offsetHeight : 80;
                const targetPosition = target.offsetTop - headerHeight - 20;
                
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });
    
    // Track Game Model clicks for analytics (if needed)
    const gameModelLink = document.querySelector('a[href*="game-model"]');
    if (gameModelLink) {
        gameModelLink.addEventListener('click', function() {
            // Add your analytics tracking here if needed
            console.log('Game Model navigation clicked');
        });
    }
    
    // Handle escape key to close mobile menu
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && mobileMenuOverlay && mobileMenuOverlay.classList.contains('active')) {
            mobileMenuOverlay.classList.remove('active');
            document.body.style.overflow = '';
            
            // Reset hamburger animation
            const hamburgerLines = document.querySelectorAll('.hamburger-line');
            hamburgerLines.forEach(function(line) {
                line.style.transform = '';
                line.style.opacity = '';
            });
        }
    });
    
    // Accessibility improvements
    const navLinks = document.querySelectorAll('.nav-link, .mobile-nav-link');
    navLinks.forEach(function(link) {
        link.addEventListener('focus', function() {
            this.style.outline = '2px solid #976bdd';
        });
        
        link.addEventListener('blur', function() {
            this.style.outline = '';
        });
    });
});