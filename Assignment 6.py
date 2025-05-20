import string
# Andrew Ternopolsky
# Password strength checker

# Get password input
password = input("Enter a password: ")

# Define checks
has_upper = any(char.isupper() for char in password)
has_lower = any(char.islower() for char in password)
has_digit = any(char.isdigit() for char in password)
has_special = any(char in string.punctuation for char in password)
long_enough = len(password) >= 8

# Gather failed checks
missing = []

if not long_enough:
    missing.append("at least 8 characters")
if not has_upper:
    missing.append("an uppercase letter")
if not has_lower:
    missing.append("a lowercase letter")
if not has_digit:
    missing.append("a digit")
if not has_special:
    missing.append("a special character")

# Display results
if not missing:
    print("Your password is strong!")
else:
    print("Your password needs " + " and ".join(missing) + ".")

# Strength Meter
score = 0
if long_enough:
    score += 2
if has_upper:
    score += 2
if has_lower:
    score += 2
if has_digit:
    score += 2
if has_special:
    score += 2

print(f"Password strength score: {score}/10")
