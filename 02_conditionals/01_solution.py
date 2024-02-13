age = input("provide me an age: ")
age_in_int = int(age)

# age = 25
if age_in_int < 13:
    print("Child")
elif age_in_int < 20:
    print("Teenager")
elif age_in_int < 60:
    print("adult")
else:
    print("Senior")
