password = input("Enter your password: ")
score =0
if len(password) >= 8:
    score += 1
if any(char.isupper() for char in password):
    score += 1
if any(char.islower() for char in password):
    score += 1
if any(char.isdigit() for char in password):
    score += 1
if any(char in "!@#$%^&*()" for char in password):
    score += 1
if score <= 2:
    print("Weak password")
elif score == 3 or score == 4:
    print("Medium password")
else:
    print("Strong password")
password = input("Enter your password: ")

score = 0

if len(password) >= 8:
    score += 1

if any(char.isupper() for char in password):
    score += 1

if any(char.islower() for char in password):
    score += 1

if any(char.isdigit() for char in password):
    score += 1

if any(char in "!@#$%^&*()" for char in password):
    score += 1

if score <= 2:
    print("Weak password")
elif score == 3 or score == 4:
    print("Medium password")
else:
    print("Strong password")

