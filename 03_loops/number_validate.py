while True:
    number = int(input("Enter a value between 1 and 10 : "))
    if 1 <= number <= 10:
        print("Thanks")
        break
    else:
        print("Invalid number, Try again: ")
