def password_checker():
    password = input("Enter your password: ")

    common_passwords = [
        "123456", "password", "admin", "qwerty",
        "abc123", "password123", "12345678"
    ]

    if password.lower() in common_passwords:
        print("❌ This password is too common.")
        return

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

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("✅ Strong Password")
    elif len(password) >= 6 and has_upper and has_lower and has_digit:
        print("⚠️ Medium Password")
    else:
        print("❌ Weak Password")


def login_simulation():
    correct_password = "Secure@123"
    attempts = 3

    while attempts > 0:
        password = input("Enter login password: ")

        if password == correct_password:
            print("✅ Access Granted")
            return
        else:
            attempts -= 1
            print(f"❌ Wrong password. Attempts left: {attempts}")

    print("🔒 Account locked due to multiple failed attempts")


while True:
    print("\n🔐 Mini Cybersecurity Toolkit")
    print("1. Password Strength Checker")
    print("2. Login Brute-Force Protection")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        password_checker()
    elif choice == "2":
        login_simulation()
    elif choice == "3":
        print("Goodbye 👋")
        break
    else:
        print("❌ Invalid choice. Try again.")
