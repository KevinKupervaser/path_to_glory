import math

#Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2).
#Write a program that calculates the slope of a line through
#two (non-vertical) points entered by the user.


def slope():
    x1, y1 = eval(input("Input the first x and y point separated by a comma: "))
    x2, y2 = eval(input("Input the first x and y point separated by a comma: "))

    slopey = y2 - y1
    slopex = x2 - x1

    print("The slope is", slopey, '/', slopex)
slope()