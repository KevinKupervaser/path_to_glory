import math

def lenghtofladder():

    # User enters the input data
    height = float(input("How high do you need the ladder to reach? "))
    angle = float(input("At what angle will the ladder be leaning against the house? "))

    # To get the lenght of the ladder we need first to convert the angle to radians
    radians = (math.pi / 180) * angle
    lenght = height / math.sin(radians)

    print("The lenght of the ladder is:", lenght)

lenghtofladder()
