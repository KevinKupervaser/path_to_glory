import math
#Write a program that accepts two points and determines the distance between them.

def distance():
    print("This program calculates the slope of a line through 2 points.")

    # Asking the user for the imputs of x and y

    x1, y1 = eval(input("Input the first x and y point separated by a comma: "))
    x2, y2 = eval(input("Input the first x and y point separated by a comma: "))

    # Distance =  math.sqrt (x2 - x1)**2 + (y2 - y1)**2
    # First step: substrack and then elevate

    x = (x2 - x1)**2
    y = (y2 - y1)**2

    # Second step: add x + y
    result = x + y

    # Third step: square root the previous result
    final_result = math.sqrt(result)

    print("The distance between the two points is:", final_result)
distance()



