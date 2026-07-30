import math

x = float(input("Enter x in radians: "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(n):
    power = 2 * i
    term = (x ** power) / math.factorial(power)

    if i % 2 == 0:
        sum = sum + term
    else:
        sum = sum - term

print("Cos(x) =", sum)