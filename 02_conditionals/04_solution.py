fruit_in_str = input("Enter a fruits Name: ")
fruit = str(fruit_in_str)
color_in_srt = input("Enter a furits color: ")
color = str(color_in_srt)
if fruit == '' and color == '':
    print("sorry")

if fruit == "Banana":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
elif fruit == "manago":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
elif fruit == "orange":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
elif fruit == "apple":
    if color == "Green":
        print("Unripe")
    elif color == "Yellow":
        print("Ripe")
    elif color == "Brown":
        print("OverRipe")
else:
    print("Sorry i can't give a information in this fruits")
