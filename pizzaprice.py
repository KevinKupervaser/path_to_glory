import math

# radius = diameter / 2
# diameter = radius * 2
# area = math.pi * radius**2

def pizzaprice():
    # Input data from the user
    diameter = float(input("The diameter of the pizza is(inches): "))
    price = float(input("The price of the pizza is($): "))

    # Radius to get the area of the circle
    radius = (diameter / 2)

    # formula to get the area
    area = math.pi * (radius**2)

    # price/area= cost of the pizza per square inch
    costpersqr = price / area
    print("The cost of the pizza per square inch is:", costpersqr)
pizzaprice()