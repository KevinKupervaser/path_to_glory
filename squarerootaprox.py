import math

def squarerootaprox ():
    print("This program calculates an aproximation to a square root of a number using newton method")

    num = int(input("Enter the number whos square root you'd like to calculate: "))
    n = int(input("Enter the number of times Newton's method should iterate: "))
    guess= float(input("Enter your initial guess of what the square root should be: "))

    for i in range(n):
        guess = (guess + num / guess) / 2

        print("The aproximate square root of", num, "is", guess)
        print("The error in this aproximation is", math.sqrt(num) - guess)

squarerootaprox()

