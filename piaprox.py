import math

print("this program that approximates the value of pi.")

n = int(input("Enter the number of terms of the finite sum: "))
total = 0

for i in range(n):
    total = total + 4 * (-1) ** i / (2 * i + 1)

print("The aproximate value of pi is: ", total, ".", sep="")
print("The error in this aproximation is: ", math.pi - total, ".", sep="")
