import re
import sys
import getpass
from typing import Dict, List, Tuple

class PasswordStrengthChecker:
    """Enhanced password strength checker with detailed feedback"""
    
    def __init__(self):
        self.common_passwords = [
            "password", "123456", "12345678", "1234", "qwerty", 
            "admin", "welcome", "password123", "12345", "letmein"
        ]
        
        self.special_characters = r'[!@#$%^&*(),.?":{}|<>]'
    
    def check_password_strength(self, password: str) -> Dict:
        """
        Check the strength of a password and provide detailed feedback.
        
        Args:
            password (str): The password to check
            
        Returns:
            Dict: Contains strength score, level, and detailed feedback
        """
        if not password:
            return {
                "score": 0,
                "level": "Empty",
                "feedback": ["Password cannot be empty."],
                "details": {}
            }
        
        strength_score = 0
        feedback = []
        details = {}
        
        # Check 1: Length
        details["length"] = len(password)
        if len(password) >= 12:
            strength_score += 2
            details["length_met"] = "Excellent (>12 chars)"
        elif len(password) >= 8:
            strength_score += 1
            details["length_met"] = "Good (8-11 chars)"
            feedback.append("Consider using 12 or more characters for better security.")
        else:
            details["length_met"] = "Poor (<8 chars)"
            feedback.append("Password must be at least 8 characters long.")
        
        # Check 2: Lowercase letters
        has_lowercase = bool(re.search(r'[a-z]', password))
        details["has_lowercase"] = has_lowercase
        if has_lowercase:
            strength_score += 1
        
        # Check 3: Uppercase letters
        has_uppercase = bool(re.search(r'[A-Z]', password))
        details["has_uppercase"] = has_uppercase
        if has_uppercase:
            strength_score += 1
        
        if not (has_lowercase and has_uppercase):
            if not has_lowercase:
                feedback.append("Add lowercase letters to your password.")
            if not has_uppercase:
                feedback.append("Add uppercase letters to your password.")
        
        # Check 4: Numbers
        has_numbers = bool(re.search(r'\d', password))
        details["has_numbers"] = has_numbers
        if has_numbers:
            strength_score += 1
        else:
            feedback.append("Add at least one number (0-9) to your password.")
        
        # Check 5: Special characters
        has_special = bool(re.search(self.special_characters, password))
        details["has_special"] = has_special
        if has_special:
            strength_score += 1
        else:
            feedback.append("Add at least one special character (!@#$%^&* etc.) to your password.")
        
        # Check 6: Common password
        is_common = password.lower() in self.common_passwords
        details["is_common"] = is_common
        if is_common:
            strength_score = max(0, strength_score - 2)
            feedback.append("This is a very common password. Choose something more unique.")
        
        # Check 7: Repeated characters
        has_repeats = bool(re.search(r'(.)\1{2,}', password))
        details["has_repeats"] = has_repeats
        if has_repeats:
            feedback.append("Avoid repeating the same character multiple times in a row.")
        
        # Check 8: Sequential characters
        sequential_patterns = [
            'abc', 'bcd', 'cde', 'def', 'efg', 'fgh', 'ghi', 'hij', 'ijk', 'jkl', 
            'klm', 'lmn', 'mno', 'nop', 'opq', 'pqr', 'qrs', 'rst', 'stu', 'tuv', 
            'uvw', 'vwx', 'wxy', 'xyz', '012', '123', '234', '345', '456', '567', 
            '678', '789'
        ]
        
        has_sequence = any(seq in password.lower() for seq in sequential_patterns)
        details["has_sequence"] = has_sequence
        if has_sequence:
            feedback.append("Avoid simple sequences like 'abc' or '123'.")
        
        # Determine strength level
        if strength_score >= 6:
            level = "Strong"
            if not feedback:
                feedback.append("Excellent password! It meets all basic security criteria.")
        elif strength_score >= 4:
            level = "Moderate"
            feedback.append("Your password is okay, but could be stronger.")
        elif strength_score >= 2:
            level = "Weak"
            feedback.append("Your password needs significant improvement.")
        else:
            level = "Very Weak"
            feedback.append("This password is highly insecure.")
        
        # Additional recommendations for strong passwords
        if strength_score >= 6 and len(password) >= 12:
            feedback.append("Consider using a password manager to store this password securely.")
            feedback.append("Use two-factor authentication where available for added security.")
        
        return {
            "score": strength_score,
            "level": level,
            "feedback": feedback,
            "details": details
        }
    
    def generate_password_report(self, password: str) -> str:
        """
        Generate a formatted report for a password.
        
        Args:
            password (str): The password to analyze
            
        Returns:
            str: Formatted report
        """
        result = self.check_password_strength(password)
        
        # Hide password for security
        hidden_password = password[0] + "*" * (len(password) - 2) + password[-1] if len(password) > 2 else "***"
        
        report = []
        report.append("=" * 60)
        report.append("PASSWORD STRENGTH ANALYSIS REPORT")
        report.append("=" * 60)
        report.append(f"Password: {hidden_password}")
        report.append(f"Length: {len(password)} characters")
        report.append(f"Strength Score: {result['score']}/7")
        report.append(f"Strength Level: {result['level']}")
        report.append("-" * 60)
        
        report.append("DETAILED ANALYSIS:")
        for key, value in result['details'].items():
            report.append(f"  - {key.replace('_', ' ').title()}: {value}")
        
        report.append("-" * 60)
        report.append("RECOMMENDATIONS:")
        for i, rec in enumerate(result['feedback'], 1):
            report.append(f"  {i}. {rec}")
        
        report.append("=" * 60)
        
        return "\n".join(report)


def interactive_mode():
    """Run the password checker in interactive mode"""
    checker = PasswordStrengthChecker()
    
    print("\n" + "="*60)
    print("PASSWORD STRENGTH CHECKER - Interactive Mode")
    print("="*60)
    print("Note: For security, your password will not be displayed as you type.")
    print("="*60 + "\n")
    
    while True:
        try:
            # Use getpass for secure input
            password = getpass.getpass("Enter a password to check (or press Enter to exit): ")
            
            if not password:
                print("\nExiting. Stay secure!")
                break
            
            result = checker.check_password_strength(password)
            
            print("\n" + "-"*40)
            print(f"STRENGTH: {result['level']} ({result['score']}/7)")
            print("-"*40)
            
            print("\nFeedback:")
            for i, feedback in enumerate(result['feedback'], 1):
                print(f"  {i}. {feedback}")
            
            print("\n" + "-"*40)
            
            # Ask if user wants a full report
            choice = input("\nGenerate full report? (y/n): ").lower()
            if choice == 'y':
                print("\n" + checker.generate_password_report(password))
            
            print("\n" + "="*60 + "\n")
            
        except KeyboardInterrupt:
            print("\n\nExiting. Stay secure!")
            break
        except Exception as e:
            print(f"\nError: {e}")
            continue


def check_single_password(password: str):
    """Check a single password and print results"""
    checker = PasswordStrengthChecker()
    print(checker.generate_password_report(password))


if __name__ == "__main__":
    # Command line interface
    if len(sys.argv) > 1:
        # Check password provided as argument
        check_single_password(sys.argv[1])
    else:
        # Run in interactive mode
        interactive_mode()
