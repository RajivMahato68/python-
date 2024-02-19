# n = 10
# sum_even = 0
# for i in range(1, n+1):
#     if i %2 == 0:
#         sum_even += 1
# print("sum of even number is :", sum_even)

n = int(input("Enter a value for n: "))
sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += i               

print("Sum of even numbers up to", n, "is:", sum_even)
