distance_in_int = input("Enter your Distance: ")
if distance_in_int == '':
    print("please enter a number")
    exit()
elif any(char.isalpha() for char in distance_in_int):
    print("not use albhbet")
    exit()

distance = int(distance_in_int)

if distance < 3:
    print("It's a short distance you can go for walk")
elif distance < 15:
    print("use bike")
else:
    print("car")