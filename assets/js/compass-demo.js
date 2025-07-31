// Coach's Compass Demo Functionality - 360TFT
// Interactive demo for the coaching diagnostic system

(function() {
    'use strict';
    
    document.addEventListener('DOMContentLoaded', function() {
        initCompassDemo();
        setupDiagnosticFlow();
    });
    
    function initCompassDemo() {
        console.log('Coach\'s Compass Demo Initialized');
        createDemoElements();
        setupInteractiveDemo();
    }
    
    function createDemoElements() {
        // Add interactive demo section if it doesn't exist
        const demoContainer = document.querySelector('.compass-demo');
        if (demoContainer) {
            enhanceDemoContainer(demoContainer);
        }
    }
    
    function enhanceDemoContainer(container) {
        const demoHTML = `
            <div class="compass-interactive">
                <h3>Try the Compass System</h3>
                <div class="demo-scenario">
                    <p><strong>Scenario:</strong> Your U12 team is struggling with passing accuracy in matches</p>
                    <button class="demo-button" data-step="1">Start Diagnosis</button>
                </div>
                <div class="demo-results" style="display: none;">
                    <div class="demo-step" id="step-1" style="display: none;">
                        <h4>Step 1: Identify the Problem</h4>
                        <p>The Compass identifies this as a <strong>Technical Issue</strong> under pressure</p>
                        <button class="demo-button" data-step="2">Next: Find Root Cause</button>
                    </div>
                    <div class="demo-step" id="step-2" style="display: none;">
                        <h4>Step 2: Root Cause Analysis</h4>
                        <p>Players can pass in training but struggle in matches = <strong>Pressure Training Gap</strong></p>
                        <button class="demo-button" data-step="3">Next: Get Solution</button>
                    </div>
                    <div class="demo-step" id="step-3" style="display: none;">
                        <h4>Step 3: Targeted Solution</h4>
                        <div class="solution-box">
                            <h5>Recommended Training Focus:</h5>
                            <ul>
                                <li>✅ Passing under pressure drills</li>
                                <li>✅ Small-sided games with time constraints</li>
                                <li>✅ Progressive overload training</li>
                                <li>✅ Match simulation exercises</li>
                            </ul>
                        </div>
                        <button class="demo-button demo-restart" data-step="restart">Try Another Scenario</button>
                    </div>
                </div>
            </div>
        `;
        
        container.insertAdjacentHTML('beforeend', demoHTML);
        addDemoStyles();
    }
    
    function setupInteractiveDemo() {
        document.addEventListener('click', function(e) {
            if (e.target.classList.contains('demo-button')) {
                const step = e.target.getAttribute('data-step');
                handleDemoStep(step);
            }
        });
    }
    
    function handleDemoStep(step) {
        const resultsContainer = document.querySelector('.demo-results');
        const scenarioContainer = document.querySelector('.demo-scenario');
        
        if (step === 'restart') {
            // Reset demo
            resultsContainer.style.display = 'none';
            scenarioContainer.style.display = 'block';
            document.querySelectorAll('.demo-step').forEach(el => el.style.display = 'none');
            return;
        }
        
        if (step === '1') {
            scenarioContainer.style.display = 'none';
            resultsContainer.style.display = 'block';
        }
        
        // Hide all steps
        document.querySelectorAll('.demo-step').forEach(el => el.style.display = 'none');
        
        // Show current step
        const currentStep = document.getElementById(`step-${step}`);
        if (currentStep) {
            currentStep.style.display = 'block';
            
            // Scroll to step with smooth animation
            currentStep.scrollIntoView({ 
                behavior: 'smooth', 
                block: 'center' 
            });
        }
        
        // Track demo interaction
        trackDemoInteraction(step);
    }
    
    function setupDiagnosticFlow() {
        // Enhance diagnostic steps with interactive elements
        const diagnosticSteps = document.querySelectorAll('.diagnostic-step');
        
        diagnosticSteps.forEach((step, index) => {
            step.addEventListener('click', function() {
                this.classList.toggle('active');
                
                // Add visual feedback
                if (this.classList.contains('active')) {
                    this.style.transform = 'scale(1.02)';
                } else {
                    this.style.transform = 'scale(1)';
                }
            });
            
            // Add hover effects
            step.addEventListener('mouseenter', function() {
                if (!this.classList.contains('active')) {
                    this.style.transform = 'translateY(-5px)';
                }
            });
            
            step.addEventListener('mouseleave', function() {
                if (!this.classList.contains('active')) {
                    this.style.transform = 'translateY(0)';
                }
            });
        });
    }
    
    function addDemoStyles() {
        if (document.getElementById('compass-demo-styles')) return;
        
        const styles = `
            <style id="compass-demo-styles">
                .compass-interactive {
                    background: linear-gradient(135deg, #976bdd, #7c5bc4);
                    color: white;
                    padding: 40px;
                    border-radius: 20px;
                    margin: 40px 0;
                    text-align: center;
                }
                
                .demo-scenario,
                .demo-step {
                    background: rgba(255, 255, 255, 0.1);
                    padding: 30px;
                    border-radius: 15px;
                    margin: 20px 0;
                    backdrop-filter: blur(10px);
                }
                
                .demo-button {
                    background: #ff5757;
                    color: white;
                    border: none;
                    padding: 15px 30px;
                    border-radius: 25px;
                    font-weight: bold;
                    cursor: pointer;
                    font-size: 1.1em;
                    transition: all 0.3s ease;
                    margin: 15px 0;
                }
                
                .demo-button:hover {
                    background: #e64545;
                    transform: translateY(-2px);
                    box-shadow: 0 5px 15px rgba(255, 87, 87, 0.4);
                }
                
                .solution-box {
                    background: rgba(255, 255, 255, 0.2);
                    padding: 25px;
                    border-radius: 10px;
                    margin: 20px 0;
                    text-align: left;
                }
                
                .solution-box h5 {
                    color: #ffeb3b;
                    margin-bottom: 15px;
                    font-size: 1.2em;
                }
                
                .solution-box ul {
                    list-style: none;
                    padding: 0;
                }
                
                .solution-box li {
                    padding: 8px 0;
                    font-size: 1.1em;
                }
                
                .demo-step h4 {
                    color: #ffeb3b;
                    margin-bottom: 15px;
                }
                
                @media (max-width: 768px) {
                    .compass-interactive {
                        padding: 25px 20px;
                    }
                    
                    .demo-scenario,
                    .demo-step {
                        padding: 20px;
                    }
                    
                    .demo-button {
                        padding: 12px 25px;
                        font-size: 1em;
                    }
                }
            </style>
        `;
        
        document.head.insertAdjacentHTML('beforeend', styles);
    }
    
    function trackDemoInteraction(step) {
        // Track demo usage for analytics
        if (typeof trackEvent === 'function') {
            trackEvent('compass_demo_interaction', {
                step: step,
                timestamp: new Date().toISOString()
            });
        }
        
        console.log('Compass Demo Step:', step);
    }
    
})();