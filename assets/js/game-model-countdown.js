// Game Model Countdown Timer - 360TFT
// Creates urgency for launch special pricing

(function() {
    'use strict';
    
    document.addEventListener('DOMContentLoaded', function() {
        initCountdown();
    });
    
    function initCountdown() {
        // Set launch special end date (adjust as needed)
        const launchEndDate = new Date();
        launchEndDate.setDate(launchEndDate.getDate() + 7); // 7 days from now
        
        // Create countdown elements if they don't exist
        createCountdownElements();
        
        // Start countdown timer
        const countdownTimer = setInterval(function() {
            const now = new Date().getTime();
            const distance = launchEndDate.getTime() - now;
            
            if (distance < 0) {
                handleCountdownExpired(countdownTimer);
                return;
            }
            
            updateCountdownDisplay(distance);
        }, 1000);
    }
    
    function createCountdownElements() {
        const countdownContainers = document.querySelectorAll('.launch-special, .pricing-card');
        
        countdownContainers.forEach(container => {
            if (!container.querySelector('.countdown-timer')) {
                const countdownHTML = `
                    <div class="countdown-timer">
                        <div class="countdown-label">Launch Special Ends In:</div>
                        <div class="countdown-display">
                            <div class="countdown-item">
                                <span class="countdown-number" id="days">0</span>
                                <span class="countdown-text">Days</span>
                            </div>
                            <div class="countdown-item">
                                <span class="countdown-number" id="hours">0</span>
                                <span class="countdown-text">Hours</span>
                            </div>
                            <div class="countdown-item">
                                <span class="countdown-number" id="minutes">0</span>
                                <span class="countdown-text">Mins</span>
                            </div>
                            <div class="countdown-item">
                                <span class="countdown-number" id="seconds">0</span>
                                <span class="countdown-text">Secs</span>
                            </div>
                        </div>
                    </div>
                `;
                
                container.insertAdjacentHTML('beforeend', countdownHTML);
            }
        });
        
        // Add countdown styles
        addCountdownStyles();
    }
    
    function updateCountdownDisplay(distance) {
        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);
        
        // Update all countdown displays
        document.querySelectorAll('#days').forEach(el => el.textContent = days);
        document.querySelectorAll('#hours').forEach(el => el.textContent = hours);
        document.querySelectorAll('#minutes').forEach(el => el.textContent = minutes);
        document.querySelectorAll('#seconds').forEach(el => el.textContent = seconds);
    }
    
    function handleCountdownExpired(timer) {
        clearInterval(timer);
        
        // Update pricing to regular price
        document.querySelectorAll('.launch-price, .launch-price-big').forEach(el => {
            el.textContent = '$40';
        });
        
        // Hide launch special elements
        document.querySelectorAll('.launch-special, .savings').forEach(el => {
            el.style.display = 'none';
        });
        
        // Update countdown display
        document.querySelectorAll('.countdown-timer').forEach(el => {
            el.innerHTML = '<div class="countdown-expired">Launch Special Has Ended</div>';
        });
    }
    
    function addCountdownStyles() {
        if (document.getElementById('countdown-styles')) return;
        
        const styles = `
            <style id="countdown-styles">
                .countdown-timer {
                    background: rgba(255, 87, 87, 0.1);
                    border: 2px solid #ff5757;
                    border-radius: 15px;
                    padding: 20px;
                    margin: 20px 0;
                    text-align: center;
                }
                
                .countdown-label {
                    color: #ff5757;
                    font-weight: bold;
                    font-size: 1.1em;
                    margin-bottom: 15px;
                }
                
                .countdown-display {
                    display: flex;
                    justify-content: center;
                    gap: 20px;
                    flex-wrap: wrap;
                }
                
                .countdown-item {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    min-width: 60px;
                }
                
                .countdown-number {
                    background: #ff5757;
                    color: white;
                    font-size: 1.8em;
                    font-weight: bold;
                    padding: 10px 15px;
                    border-radius: 8px;
                    min-width: 50px;
                    margin-bottom: 5px;
                }
                
                .countdown-text {
                    font-size: 0.9em;
                    color: #666;
                    font-weight: bold;
                }
                
                .countdown-expired {
                    color: #ff5757;
                    font-weight: bold;
                    font-size: 1.2em;
                    padding: 20px;
                }
                
                @media (max-width: 768px) {
                    .countdown-display {
                        gap: 10px;
                    }
                    
                    .countdown-number {
                        font-size: 1.4em;
                        padding: 8px 12px;
                    }
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
})();