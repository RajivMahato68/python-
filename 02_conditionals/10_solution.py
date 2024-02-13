user_input = input("Enter your Domestic Animal:-")
animal = str(user_input)
animal_age = input("Enter your Animal age:-")
age = int(animal_age)

if (animal== "dog" and age<2):
    print("Puppy food")
elif (animal == "dog" and age>5):
    print("senor food")