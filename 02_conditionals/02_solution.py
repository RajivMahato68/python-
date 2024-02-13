age_in_int = input("Enter your age: ")
age = int(age_in_int)
day_in_int = input("Enter Today Day: ")
day = str(day_in_int)

# age = 26
# day = "wednesday"

price = 12 if age >= 18 else 8

if day == "wednesday":
    # price = price - 2
    price -= 2

print("Titcket price for you is $", price)