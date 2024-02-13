weathe_in_str = input("Enter a today Weather Condition:")
weather2 = str(weathe_in_str)
weather = weather2.capitalize()

if weather == '':
    print("please enter a weather name ")
    exit()
elif weather.isdigit():
    print("Please enter a proper weather name, not a number.")
    exit()

if weather == "Sunny":
    print("Go for a walk")
    # activity = "Go for a walk" 
elif weather == "Rainy":
    print("Read a book")
elif weather == "Snowy":
    print("Build a snowman")
else:
    print("Sorry I have a not any information in this condition")