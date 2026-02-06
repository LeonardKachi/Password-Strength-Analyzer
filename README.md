# Password Strength Analyzer

A comprehensive password strength checking tool with a web frontend and Python backend.

![Password Strength Analyzer](https://img.shields.io/badge/Security-Password%20Checker-blue)
![GitHub Pages](https://img.shields.io/badge/Hosted-GitHub%20Pages-green)
![Python](https://img.shields.io/badge/Python-3.6%2B-yellow)

## Features

### Web Frontend (GitHub Pages)
- **Client-side processing** - No passwords sent to servers
- **Real-time feedback** - Instant strength analysis as you type
- **Visual strength meter** - Color-coded password strength indicator
- **Detailed recommendations** - Specific advice to improve passwords
- **Cybersecurity optimized** - Security-focused design and warnings
- **Responsive design** - Works on desktop and mobile devices

### Python Script
- **Enhanced logic** - More comprehensive checks than basic implementations
- **Detailed reporting** - Generate formatted password analysis reports
- **Interactive mode** - Command-line interface with secure input
- **Common password detection** - Checks against known weak passwords
- **Pattern detection** - Identifies sequences and repeated characters

## Quick Start

### Using the Web Interface
1. Visit the GitHub Pages site: `https://yourusername.github.io/password-strength-analyzer`
2. Enter a password in the input field
3. View real-time strength analysis and recommendations

### Running the Python Script
```bash
# Interactive mode
python password_checker.py

# Check a specific password
python password_checker.py "YourPassword123!"

# Import as a module
from password_checker import PasswordStrengthChecker
checker = PasswordStrengthChecker()
result = checker.check_password_strength("YourPassword123!")
