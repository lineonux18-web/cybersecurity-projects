password = input("Enter your password: ")

has_upper = any(char.isupper() for char in password)
has_digit = any(char.isdigit() for char in password)
has_symbol = any(not char.isalnum() for char in password)

score = 0
feedback = []

if len(password) >= 8:
    score += 1
else:
    feedback.append("Too short")

if has_upper:
    score += 1
else:
    feedback.append("Add uppercase letter")

if has_digit:
    score += 1
else:
    feedback.append("Add a number")

if has_symbol:
    score += 1
else:
    feedback.append("Add a symbol")

if score <= 1:
    print("Weak")
elif score <= 3:
    print("Medium")
else:
    print("Strong")

if feedback:
    print("Suggestions:", ", ".join(feedback))
