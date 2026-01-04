correct_password = "Github@2026"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("✅ Access Granted")
        break
    else:
        attempts -= 1
        print(f"❌ Wrong password. Attempts left: {attempts}")

if attempts == 0:
    print("🔒 Account locked due to multiple failed attempts")
