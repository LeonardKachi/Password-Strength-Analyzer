<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cybersecurity Password Strength Analyzer</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        :root {
            --primary-dark: #0a192f;
            --primary-blue: #1e3a8a;
            --cyber-green: #10b981;
            --cyber-red: #ef4444;
            --cyber-yellow: #f59e0b;
            --neutral-light: #f8fafc;
            --neutral-gray: #94a3b8;
            --card-bg: rgba(30, 41, 59, 0.8);
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: var(--primary-dark);
            color: var(--neutral-light);
            line-height: 1.6;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            background-image: 
                radial-gradient(circle at 10% 20%, rgba(28, 58, 173, 0.1) 0%, transparent 20%),
                radial-gradient(circle at 90% 80%, rgba(16, 185, 129, 0.05) 0%, transparent 20%);
        }
        
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
            width: 100%;
        }
        
        /* Header Styles */
        header {
            padding: 2rem 0;
            text-align: center;
            border-bottom: 1px solid rgba(148, 163, 184, 0.2);
            background-color: rgba(10, 25, 47, 0.9);
            backdrop-filter: blur(10px);
        }
        
        .logo {
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 15px;
            margin-bottom: 10px;
        }
        
        .logo-icon {
            color: var(--cyber-green);
            font-size: 2.5rem;
        }
        
        h1 {
            font-size: 2.8rem;
            background: linear-gradient(90deg, var(--cyber-green), #3b82f6);
            -webkit-background-clip: text;
            background-clip: text;
            color: transparent;
            margin-bottom: 10px;
        }
        
        .subtitle {
            color: var(--neutral-gray);
            font-size: 1.1rem;
            max-width: 800px;
            margin: 0 auto;
        }
        
        /* Main Content */
        .main-content {
            display: flex;
            flex-wrap: wrap;
            gap: 40px;
            padding: 40px 0;
            flex: 1;
        }
        
        .input-section, .results-section {
            flex: 1;
            min-width: 300px;
            background-color: var(--card-bg);
            border-radius: 16px;
            padding: 30px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.3);
            border: 1px solid rgba(148, 163, 184, 0.1);
        }
        
        .section-title {
            font-size: 1.8rem;
            margin-bottom: 25px;
            color: var(--cyber-green);
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .section-title i {
            font-size: 1.5rem;
        }
        
        /* Password Input Area */
        .password-container {
            position: relative;
            margin-bottom: 30px;
        }
        
        #passwordInput {
            width: 100%;
            padding: 18px 20px;
            padding-right: 60px;
            font-size: 1.2rem;
            background-color: rgba(15, 23, 42, 0.8);
            border: 2px solid var(--neutral-gray);
            border-radius: 12px;
            color: var(--neutral-light);
            transition: all 0.3s;
        }
        
        #passwordInput:focus {
            outline: none;
            border-color: var(--cyber-green);
            box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2);
        }
        
        .toggle-password {
            position: absolute;
            right: 15px;
            top: 50%;
            transform: translateY(-50%);
            background: none;
            border: none;
            color: var(--neutral-gray);
            cursor: pointer;
            font-size: 1.3rem;
        }
        
        .btn {
            background: linear-gradient(135deg, var(--primary-blue), var(--cyber-green));
            color: white;
            border: none;
            padding: 16px 30px;
            font-size: 1.1rem;
            border-radius: 12px;
            cursor: pointer;
            font-weight: 600;
            width: 100%;
            transition: all 0.3s;
            margin-top: 10px;
        }
        
        .btn:hover {
            transform: translateY(-3px);
            box-shadow: 0 10px 20px rgba(16, 185, 129, 0.2);
        }
        
        .btn:active {
            transform: translateY(0);
        }
        
        /* Python Script Info */
        .python-info {
            margin-top: 30px;
            padding: 20px;
            background-color: rgba(59, 130, 246, 0.1);
            border-radius: 12px;
            border-left: 4px solid #3b82f6;
        }
        
        .python-info h3 {
            color: #3b82f6;
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        .code-link {
            display: inline-flex;
            align-items: center;
            gap: 8px;
            background-color: rgba(59, 130, 246, 0.2);
            color: #3b82f6;
            padding: 10px 15px;
            border-radius: 8px;
            text-decoration: none;
            font-weight: 600;
            margin-top: 10px;
            transition: all 0.3s;
        }
        
        .code-link:hover {
            background-color: rgba(59, 130, 246, 0.3);
            transform: translateY(-2px);
        }
        
        /* Password Strength Indicator */
        .strength-meter {
            height: 10px;
            background-color: rgba(148, 163, 184, 0.2);
            border-radius: 10px;
            margin: 25px 0;
            overflow: hidden;
        }
        
        .strength-fill {
            height: 100%;
            width: 0%;
            border-radius: 10px;
            transition: all 0.5s ease;
        }
        
        .strength-text {
            font-size: 1.5rem;
            text-align: center;
            font-weight: bold;
            margin-bottom: 20px;
            min-height: 36px;
        }
        
        /* Criteria List */
        .criteria-list {
            list-style: none;
            margin-top: 20px;
        }
        
        .criteria-list li {
            padding: 12px 0;
            border-bottom: 1px solid rgba(148, 163, 184, 0.1);
            display: flex;
            align-items: center;
            gap: 15px;
        }
        
        .criteria-list li:last-child {
            border-bottom: none;
        }
        
        .criteria-icon {
            font-size: 1.2rem;
            width: 24px;
        }
        
        .criteria-met {
            color: var(--cyber-green);
        }
        
        .criteria-not-met {
            color: var(--cyber-red);
        }
        
        /* Recommendations */
        .recommendations {
            margin-top: 30px;
            padding: 20px;
            background-color: rgba(15, 23, 42, 0.6);
            border-radius: 12px;
            border-left: 4px solid var(--cyber-green);
        }
        
        .recommendations h3 {
            margin-bottom: 15px;
            color: var(--cyber-yellow);
        }
        
        .recommendations ul {
            list-style-position: inside;
            padding-left: 10px;
        }
        
        .recommendations li {
            margin-bottom: 10px;
            color: var(--neutral-gray);
        }
        
        /* Security Tips */
        .security-tips {
            margin-top: 40px;
            padding: 25px;
            background-color: rgba(239, 68, 68, 0.1);
            border-radius: 12px;
            border: 1px solid rgba(239, 68, 68, 0.3);
        }
        
        .security-tips h3 {
            color: var(--cyber-red);
            margin-bottom: 15px;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        
        /* Footer */
        footer {
            margin-top: auto;
            background-color: rgba(10, 25, 47, 0.95);
            padding: 40px 0 20px;
            border-top: 1px solid rgba(148, 163, 184, 0.2);
        }
        
        .footer-content {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
            gap: 30px;
            margin-bottom: 30px;
        }
        
        .footer-section {
            flex: 1;
            min-width: 250px;
        }
        
        .footer-section h3 {
            color: var(--cyber-green);
            margin-bottom: 20px;
            font-size: 1.3rem;
        }
        
        .footer-links {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 12px;
        }
        
        .footer-links a {
            color: var(--neutral-gray);
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: var(--cyber-green);
        }
        
        .creator-info {
            color: var(--neutral-gray);
            font-size: 0.9rem;
            line-height: 1.8;
        }
        
        .creator-info strong {
            color: var(--cyber-green);
        }
        
        .copyright {
            text-align: center;
            padding-top: 20px;
            border-top: 1px solid rgba(148, 163, 184, 0.1);
            color: var(--neutral-gray);
            font-size: 0.9rem;
        }
        
        /* Responsive Design */
        @media (max-width: 768px) {
            .main-content {
                flex-direction: column;
            }
            
            h1 {
                font-size: 2.2rem;
            }
            
            .input-section, .results-section {
                padding: 20px;
            }
        }
        
        /* Animation for strength change */
        @keyframes pulse {
            0% { transform: scale(1); }
            50% { transform: scale(1.05); }
            100% { transform: scale(1); }
        }
        
        .pulse {
            animation: pulse 0.5s ease-in-out;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <div class="logo">
                <i class="fas fa-shield-alt logo-icon"></i>
                <h1>Cybersecurity Password Analyzer</h1>
            </div>
            <p class="subtitle">A secure frontend for analyzing password strength with cybersecurity recommendations. All processing happens locally in your browser - no passwords are transmitted over the network.</p>
        </div>
    </header>
    
    <div class="container">
        <div class="main-content">
            <!-- Input Section -->
            <section class="input-section">
                <h2 class="section-title"><i class="fas fa-key"></i> Password Input</h2>
                
                <div class="password-container">
                    <input type="password" id="passwordInput" placeholder="Enter password to check strength..." autocomplete="off">
                    <button class="toggle-password" id="togglePassword">
                        <i class="fas fa-eye"></i>
                    </button>
                </div>
                
                <button class="btn" id="checkPassword">
                    <i class="fas fa-search"></i> Analyze Password Strength
                </button>
                
                <div class="python-info">
                    <h3><i class="fab fa-python"></i> Python Script Included</h3>
                    <p>This frontend is based on a Python password strength checker. You can find and run the original Python script in the repository.</p>
                    <a href="https://github.com/yourusername/password-strength-analyzer/blob/main/password_checker.py" class="code-link" target="_blank">
                        <i class="fas fa-code"></i> View Python Script
                    </a>
                </div>
                
                <div class="security-tips">
                    <h3><i class="fas fa-exclamation-triangle"></i> Security Notice</h3>
                    <p>This tool runs entirely in your browser. Your password is never sent to any server, ensuring maximum security. For optimal protection, use this tool offline or on a trusted network.</p>
                </div>
            </section>
            
            <!-- Results Section -->
            <section class="results-section">
                <h2 class="section-title"><i class="fas fa-chart-bar"></i> Analysis Results</h2>
                
                <div class="strength-text" id="strengthText">Enter a password to begin analysis</div>
                
                <div class="strength-meter">
                    <div class="strength-fill" id="strengthFill"></div>
                </div>
                
                <ul class="criteria-list" id="criteriaList">
                    <li>
                        <span class="criteria-icon"><i class="fas fa-ruler"></i></span>
                        <span>At least 8 characters long</span>
                    </li>
                    <li>
                        <span class="criteria-icon"><i class="fas fa-text-height"></i></span>
                        <span>Contains both uppercase and lowercase letters</span>
                    </li>
                    <li>
                        <span class="criteria-icon"><i class="fas fa-hashtag"></i></span>
                        <span>Includes at least one number</span>
                    </li>
                    <li>
                        <span class="criteria-icon"><i class="fas fa-asterisk"></i></span>
                        <span>Includes at least one special character</span>
                    </li>
                </ul>
                
                <div class="recommendations" id="recommendations">
                    <h3><i class="fas fa-lightbulb"></i> Recommendations</h3>
                    <ul>
                        <li>Enter a password above to get personalized recommendations</li>
                        <li>Consider using a passphrase instead of a password</li>
                        <li>Use a unique password for each online account</li>
                    </ul>
                </div>
            </section>
        </div>
    </div>
    
    <footer>
        <div class="container">
            <div class="footer-content">
                <div class="footer-section">
                    <h3>About This Tool</h3>
                    <p class="creator-info">
                        This Password Strength Analyzer was created by <strong>a cybersecurity enthusiast</strong> who understands the critical importance of strong passwords in protecting digital identities.
                    </p>
                    <p class="creator-info">
                        The tool implements password analysis logic based on industry best practices for password security, with a focus on client-side processing to ensure no password data is transmitted over networks.
                    </p>
                    <p class="creator-info">
                        <strong>Repository Includes:</strong> Frontend (HTML/CSS/JS) and the original Python script for password strength checking.
                    </p>
                </div>
                
                <div class="footer-section">
                    <h3>GitHub Repository</h3>
                    <ul class="footer-links">
                        <li><a href="https://github.com/yourusername/password-strength-analyzer" target="_blank">View Full Repository</a></li>
                        <li><a href="https://github.com/yourusername/password-strength-analyzer/blob/main/password_checker.py" target="_blank">Python Script (password_checker.py)</a></li>
                        <li><a href="https://github.com/yourusername/password-strength-analyzer/blob/main/README.md" target="_blank">Documentation</a></li>
                        <li><a href="https://github.com/yourusername/password-strength-analyzer/issues" target="_blank">Report Issues</a></li>
                    </ul>
                </div>
                
                <div class="footer-section">
                    <h3>Password Best Practices</h3>
                    <ul class="footer-links">
                        <li><a href="https://pages.nist.gov/800-63-3/sp800-63b.html" target="_blank">NIST Digital Identity Guidelines</a></li>
                        <li><a href="https://www.ftc.gov/business-guidance/resources/how-secure-your-computer" target="_blank">FTC Computer Security Tips</a></li>
                        <li><a href="https://www.consumer.ftc.gov/articles/secure-your-computer" target="_blank">FTC: Secure Your Computer</a></li>
                        <li><a href="https://www.lastpass.com/password-generator" target="_blank">Secure Password Generator</a></li>
                    </ul>
                </div>
            </div>
            
            <div class="copyright">
                <p>© 2023 Cybersecurity Password Analyzer. This tool runs entirely client-side. No passwords are stored or transmitted. For educational and security assessment purposes only.</p>
                <p style="margin-top: 10px; font-size: 0.8rem;">Note: This frontend demonstrates the Python password checker logic implemented in JavaScript. The original Python script is available in the repository.</p>
            </div>
        </div>
    </footer>
    
    <script>
        // DOM Elements
        const passwordInput = document.getElementById('passwordInput');
        const togglePassword = document.getElementById('togglePassword');
        const checkPasswordBtn = document.getElementById('checkPassword');
        const strengthText = document.getElementById('strengthText');
        const strengthFill = document.getElementById('strengthFill');
        const criteriaList = document.getElementById('criteriaList');
        const recommendationsDiv = document.getElementById('recommendations');
        
        // Toggle password visibility
        togglePassword.addEventListener('click', function() {
            const type = passwordInput.getAttribute('type') === 'password' ? 'text' : 'password';
            passwordInput.setAttribute('type', type);
            this.innerHTML = type === 'password' ? '<i class="fas fa-eye"></i>' : '<i class="fas fa-eye-slash"></i>';
        });
        
        // Check password strength
        checkPasswordBtn.addEventListener('click', function() {
            const password = passwordInput.value;
            const result = checkPasswordStrength(password);
            updateUI(result);
        });
        
        // Also check on input change for real-time feedback
        passwordInput.addEventListener('input', function() {
            const password = passwordInput.value;
            if (password.length > 0) {
                const result = checkPasswordStrength(password);
                updateUI(result);
            } else {
                // Reset UI if input is empty
                strengthText.textContent = "Enter a password to begin analysis";
                strengthFill.style.width = "0%";
                strengthFill.style.backgroundColor = "";
                
                // Reset criteria icons
                const criteriaIcons = criteriaList.querySelectorAll('.criteria-icon i');
                criteriaIcons.forEach(icon => {
                    icon.className = 'fas fa-question';
                    icon.parentElement.className = 'criteria-icon';
                });
                
                // Reset recommendations
                recommendationsDiv.innerHTML = `
                    <h3><i class="fas fa-lightbulb"></i> Recommendations</h3>
                    <ul>
                        <li>Enter a password above to get personalized recommendations</li>
                        <li>Consider using a passphrase instead of a password</li>
                        <li>Use a unique password for each online account</li>
                    </ul>
                `;
            }
        });
        
        // Password strength checking logic (mimics Python script)
        function checkPasswordStrength(password) {
            let strength = 0;
            const recommendations = [];
            
            // Check length
            const lengthCheck = password.length >= 8;
            if (lengthCheck) {
                strength += 1;
            } else {
                recommendations.push("Password must be at least 8 characters long.");
            }
            
            // Check for lowercase and uppercase letters
            const hasLowercase = /[a-z]/.test(password);
            const hasUppercase = /[A-Z]/.test(password);
            const caseCheck = hasLowercase && hasUppercase;
            
            if (caseCheck) {
                strength += 1;
            } else {
                if (!hasLowercase) recommendations.push("Add lowercase letters to your password.");
                if (!hasUppercase) recommendations.push("Add uppercase letters to your password.");
            }
            
            // Check for numbers
            const hasNumber = /\d/.test(password);
            if (hasNumber) {
                strength += 1;
            } else {
                recommendations.push("Add at least one number (0-9) to your password.");
            }
            
            // Check for special characters
            const hasSpecial = /[!@#$%^&*(),.?":{}|<>]/.test(password);
            if (hasSpecial) {
                strength += 1;
            } else {
                recommendations.push("Add at least one special character (!@#$%^&* etc.) to your password.");
            }
            
            // Additional cybersecurity checks (beyond the Python script)
            // Check for common passwords
            const commonPasswords = ["password", "123456", "qwerty", "admin", "welcome"];
            if (commonPasswords.includes(password.toLowerCase())) {
                recommendations.push("This is a very common password. Choose something more unique.");
                strength = Math.max(0, strength - 1); // Penalize for common password
            }
            
            // Check for repeated characters
            if (/(.)\1{2,}/.test(password)) {
                recommendations.push("Avoid repeating the same character multiple times in a row.");
            }
            
            // Check for sequences
            if (/(abc|def|ghi|jkl|mno|pqr|stu|vwx|yz|012|123|234|345|456|567|678|789)/i.test(password)) {
                recommendations.push("Avoid simple sequences like 'abc' or '123'.");
            }
            
            // Evaluate strength
            let strengthLevel, strengthColor;
            if (strength === 4) {
                strengthLevel = "Strong Password!";
                strengthColor = "#10b981"; // Cyber green
            } else if (strength === 3) {
                strengthLevel = "Moderate Password";
                strengthColor = "#f59e0b"; // Cyber yellow
            } else {
                strengthLevel = "Weak Password";
                strengthColor = "#ef4444"; // Cyber red
            }
            
            // Generate personalized recommendations
            let personalizedRecommendations = recommendations;
            if (personalizedRecommendations.length === 0) {
                personalizedRecommendations = [
                    "Your password meets basic strength requirements.",
                    "Consider using a passphrase (e.g., 'CorrectHorseBatteryStaple') for better memorability and security.",
                    "Ensure you use a unique password for each online account.",
                    "Consider using a password manager to generate and store strong passwords."
                ];
            } else {
                // Add general recommendations if password is weak
                if (strength <= 2) {
                    personalizedRecommendations.push("Consider using a password manager to generate a strong password.");
                    personalizedRecommendations.push("Aim for at least 12 characters for better security.");
                }
            }
            
            return {
                strength,
                strengthLevel,
                strengthColor,
                checks: { lengthCheck, caseCheck, hasNumber, hasSpecial },
                recommendations: personalizedRecommendations
            };
        }
        
        // Update UI based on password analysis
        function updateUI(result) {
            // Update strength text and meter
            strengthText.textContent = result.strengthLevel;
            strengthText.classList.add('pulse');
            
            // Calculate percentage for meter
            const percentage = (result.strength / 4) * 100;
            strengthFill.style.width = `${percentage}%`;
            strengthFill.style.backgroundColor = result.strengthColor;
            
            // Update criteria icons
            const criteriaIcons = criteriaList.querySelectorAll('.criteria-icon i');
            
            // Length check
            criteriaIcons[0].className = result.checks.lengthCheck ? 'fas fa-check' : 'fas fa-times';
            criteriaIcons[0].parentElement.className = result.checks.lengthCheck ? 'criteria-icon criteria-met' : 'criteria-icon criteria-not-met';
            
            // Case check
            criteriaIcons[1].className = result.checks.caseCheck ? 'fas fa-check' : 'fas fa-times';
            criteriaIcons[1].parentElement.className = result.checks.caseCheck ? 'criteria-icon criteria-met' : 'criteria-icon criteria-not-met';
            
            // Number check
            criteriaIcons[2].className = result.checks.hasNumber ? 'fas fa-check' : 'fas fa-times';
            criteriaIcons[2].parentElement.className = result.checks.hasNumber ? 'criteria-icon criteria-met' : 'criteria-icon criteria-not-met';
            
            // Special character check
            criteriaIcons[3].className = result.checks.hasSpecial ? 'fas fa-check' : 'fas fa-times';
            criteriaIcons[3].parentElement.className = result.checks.hasSpecial ? 'criteria-icon criteria-met' : 'criteria-icon criteria-not-met';
            
            // Update recommendations
            let recommendationsHTML = `<h3><i class="fas fa-lightbulb"></i> Recommendations</h3><ul>`;
            result.recommendations.forEach(rec => {
                recommendationsHTML += `<li>${rec}</li>`;
            });
            recommendationsHTML += `</ul>`;
            recommendationsDiv.innerHTML = recommendationsHTML;
            
            // Remove animation class after animation completes
            setTimeout(() => {
                strengthText.classList.remove('pulse');
            }, 500);
        }
        
        // Initialize with a sample password for demonstration
        window.addEventListener('DOMContentLoaded', () => {
            // Uncomment the line below to pre-fill with a sample password for demo purposes
            // passwordInput.value = "CyberSec123!";
            // checkPasswordBtn.click();
        });
    </script>
</body>
</html>
