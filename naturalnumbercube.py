import math

def naturalnumbercube():
    print("This program find the sum of the cubes of the first n natural numbers")

# Formula for n is = n * (n+1) / 2
# User gives the value of n

    firstn = float(input("Enter the value of n: "))
    n = firstn * (firstn + 1) / 2

# N is powered by 2

    n = n**2

    print("The sum of the cubes of first", firstn, "natural numbers is:", n)

naturalnumbercube()
