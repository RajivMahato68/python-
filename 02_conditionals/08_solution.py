user_password = input("Enter your password:-")
password = user_password

if len(password) < 6:
    strength = "week"
elif len(password) <= 10:
    strength = "medium"
else:
    strength = "Strong"
print("password strenght: ", strength)