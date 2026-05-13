Password Strength Checker
=========================
A beginner cybersecurity Python project that checks password strength and calculates entropy.

---------------------------
FEATURES
---------------------------
- Checks for uppercase letters
- Checks for lowercase letters
- Checks for digits
- Checks for special symbols
- Checks minimum length (8 characters)
- Calculates password entropy (bits)

---------------------------
REQUIREMENTS
---------------------------
- Python 3.x
- No external libraries needed (uses built-in: math, time, string)

---------------------------
HOW TO RUN
---------------------------
1. Open a terminal
2. Navigate to the project folder
3. Run the script:

   python password_checker.py

4. Type your password when prompted

---------------------------
HOW IT WORKS
---------------------------
1. Takes password input from the user
2. Checks each character against the required criteria
3. Calculates entropy using the formula:
   Entropy = password_length x log2(charset_size)
4. Tells the user which criteria are missing

---------------------------
EXAMPLE OUTPUT
---------------------------
Strong password (e.g., Hello@123):
   password has been created

Weak password (e.g., hello):
   Capital letter is not included
   The digit is not included
   Symbols are not included
   The password length is short

---------------------------
ENTROPY REFERENCE
---------------------------
Below 28 bits  → Very Weak
28 - 35 bits   → Weak
36 - 59 bits   → Reasonable
60 - 127 bits  → Strong
128+ bits      → Very Strong

---------------------------
AUTHOR
---------------------------
Hari

---------------------------
NOTE
---------------------------
This is a beginner-level cybersecurity project.
Future improvements can include later :
- HIBP (Have I Been Pwned) API integration
- Password suggestions
- GUI interface
