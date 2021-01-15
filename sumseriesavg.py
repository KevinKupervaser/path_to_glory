import math

def sumseriesavg():

    n = eval(input("How many numbers you want to enter: "))
    x = 0
    sum = 0

    for i in range(n):
        num = eval(input("Please enter a number: "))
        sum += num

        print("The sum of the amount of numbers is: ", sum)
    print("The average of this series of numbers is:",  sum / n)

sumseriesavg()
