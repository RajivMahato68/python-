user_input = input("Enter a year :- ")
year = int(user_input)

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print(year, " is a leap year")
else:
    print(year, "Is not a leap year")