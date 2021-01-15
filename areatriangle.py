import math

def areatriangle():
    print("This program calculates the area of a triangle.")
    # The user enters the input for each side
    side_a = eval(input("Input the lenght of side A: "))
    side_b = eval(input("Input the lenght of side B: "))
    side_c = eval(input("Input the lenght of side C: "))

    # formula for s: s = a+b+c / 2
    s = side_a + side_b + side_c
    s = s / 2

    # formula for area: math.sqrt (s * (s - side_a) * (s - side_b) * (s - side_c))
    firstarea = s * (s - side_a) * (s - side_b) * (s - side_c)
    area = math.sqrt(firstarea)

    print("The area of the triangle is:", area)

areatriangle()
