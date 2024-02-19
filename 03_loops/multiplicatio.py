# number = 3
n = input("enter a number you wnat")
number = int(n)


for i in range(1, 11):
    if i==5:
        continue
    print(number, 'X', i, '=', number * i)