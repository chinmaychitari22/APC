n = int(input("Enter a number: "))

root = int(n ** 0.5)
count = 0

for i in range(1, root + 1):
    if root % i == 0:
        count += 1

if count == 2:
    print("Square root is prime")
else:
    print("Square root is not prime")