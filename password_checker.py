import re

common_passwords = [
    "123456",
    "password",
    "admin",
    "qwerty"
]

password = input("Enter Password: ")

score = 0


if len(password) >= 12:
    score += 2

elif len(password) >= 8:
    score += 1


if re.search(r"[A-Z]", password):
    score += 1


if re.search(r"[a-z]", password):
    score += 1


if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*]", password):
    score += 1


if password.lower() in common_passwords:
    print("Common password detected!")
    score = 0


if score <= 2:
    strength = "Weak"

elif score <= 5:
    strength = "Medium"

else:
    strength = "Strong"

print("Password Strength:", strength)

if strength == "Weak":
    suggestion = password.capitalize() + "@2026#"
    print("Suggested Password:", suggestion)