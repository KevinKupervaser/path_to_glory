import math

def sumseries():

    print("This program sums a series of numbers entered by the user.")
    num = float(input("How many numbers do you want to sum: "))

    x = 0
    s = 0

    while x < num:
        x += 1
        s += float(input("Enter a number: "))
        print("The total value of your", num, "numbers is ", s)

sumseries()





