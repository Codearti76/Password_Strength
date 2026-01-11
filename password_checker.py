password = input("Enter your password: ")
common_passwords = [
    "123456", "password", "admin", "qwerty",
    "abc123", "password123", "12345678"]

if password.lower() in common_passwords:
    print("❌ This password is too common. Choose a stronger one.")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_chars = "@#$%!&*"

for char in password:
    if  char.isupper():
        has_upper = True
    elif char.islower():
       has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True
if len(password) >= 8:
    score += 2
else:
    warnings.append("Password is too short")

if has_upper:
    score += 1
else:
    warnings.append("Missing uppercase letter")

if has_lower:
    score += 1
else:
    warnings.append("Missing lowercase letter")

if has_digit:
    score += 1
else:
    warnings.append("Missing number")

if has_special:
    score += 1
else:
    warnings.append("Missing special character")
if password_lower in common_passwords:
    score -= 3
    warnings.append("Password is very common")

if "123" in password or "qwerty" in password_lower:
    score -= 2
    warnings.append("Predictable pattern detected")

print("\n🔍 Password Analysis:")

print("\n📊 PASSWORD STRENGTH RESULT")

if score <= 2:
    print("🔴 WEAK PASSWORD")
elif score <= 4:
    print("🟠 MEDIUM PASSWORD")
else:
    print("🟢 STRONG PASSWORD")

print(f"Score: {score}/7")

if score < 5:
print("\n💡 Suggestions to improve your password:")

if len(password) < 8:
    print("- Increase password length to at least 8 characters")

if not has_upper:
    print("- Add at least one uppercase letter")

if not has_lower:
    print("- Add at least one lowercase letter")

if not has_digit:
    print("- Include at least one number")

if not has_special:
    print("- Add a special character (e.g., @, #, $)")

if password_lower in common_passwords:
    print("- Avoid common passwords")

if "123" in password or "qwerty" in password_lower:
    print("- Avoid predictable patterns")
