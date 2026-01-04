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
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

if (len(password) >= 8 and has_upper and has_lower and has_digit and has_special):
    print("✅ Strong Password")
elif (len(password) >= 6 and has_upper and has_lower and has_digit):
    print("⚠️ Medium Password")
else:
    print("❌ Weak Password")
