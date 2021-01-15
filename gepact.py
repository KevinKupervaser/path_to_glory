import math

def gregorian():
    print("This program calculates the value of epact.")

    # Make the user enter a 4 digit year
    year = int(input("Please enter a 4 digit year: "))

    # c = 4digityear // 100
    c = year // 100

    # Formula to calculate the epact: (8 + (c //4) - c + ((8 * c + 13) //25) + 11 * (year % 19)) % 30

    epact = (8 + (c //4) - c
             + ((8 * c + 13) //25)
             + 11 * (year % 19)) % 30
    print("The gregorian epact is:", epact)

gregorian()