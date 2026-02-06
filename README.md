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
```

## Repository Structure

```
password-strength-analyzer/
├── index.html              # Main web interface (GitHub Pages)
├── password_checker.py     # Python password strength checker
├── README.md              # This documentation
└── .github/workflows/     # GitHub Actions for testing
    └── python-tests.yml
```

## Password Criteria

The tool checks for:
- Minimum length (8+ characters, 12+ recommended)
- Both uppercase and lowercase letters
- At least one number (0-9)
- At least one special character (!@#$%^&* etc.)
- Not a common password
- No repeated characters (aaa)
- No sequential patterns (abc, 123)

## Security Considerations

⚠️ **Important Security Notes:**
- The web version runs **entirely in your browser** - no passwords are transmitted
- For maximum security, use the tool offline or on trusted networks
- Consider using a password manager for generating and storing strong passwords
- Always use unique passwords for different accounts

## Development

### Local Development
1. Clone the repository:
```bash
git clone https://github.com/yourusername/password-strength-analyzer.git
```

2. Open `index.html` in a browser for frontend testing

3. Test the Python script:
```bash
python password_checker.py
```

### GitHub Pages Setup
1. Go to repository Settings > Pages
2. Select "Deploy from a branch"
3. Choose "main" branch and "/root" folder
4. Save - your site will be published at `https://yourusername.github.io/password-strength-analyzer`

## Contributing

Contributions are welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available for educational and personal use.

## Author

Created by Obidiegwu Onyedikachi Henry a cybersecurity Engineer passionate about improving password security practices.

---

**Disclaimer:** This tool is for educational and security assessment purposes only. Always follow organizational security policies and best practices when creating and managing passwords.


## GitHub Actions Test Workflow
Create `.github/workflows/python-tests.yml`:

```yaml
name: Python Tests

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.9'
    
    - name: Test password checker
      run: |
        python -c "
from password_checker import PasswordStrengthChecker
checker = PasswordStrengthChecker()

# Test weak password
result = checker.check_password_strength('password')
assert result['level'] in ['Weak', 'Very Weak'], 'Weak password test failed'

# Test strong password
result = checker.check_password_strength('StrongPass123!@#')
assert result['level'] == 'Strong', 'Strong password test failed'

print('All tests passed!')
        "
```

## Deployment Instructions

1. **Create a new GitHub repository** named `password-strength-analyzer`

2. **Upload all files** to the repository:
   - `index.html`
   - `password_checker.py`
   - `README.md`
   - `.github/workflows/python-tests.yml`

3. **Enable GitHub Pages**:
   - Go to repository Settings
   - Click on "Pages" in the left sidebar
   - Under "Source", select "Deploy from a branch"
   - Choose "main" branch and "/root" folder
   - Click Save

4. **Your site will be live** at: `https://yourusername.github.io/password-strength-analyzer`

5. **Update the links** in `index.html` and `README.md`:
   - Replace `yourusername` with your actual GitHub username
   - Update the repository URL in the Python script header
