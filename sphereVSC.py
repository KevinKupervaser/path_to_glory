import math


print("This calculates the volume, surface and circunference of",
      "a sphere given its radius")

#the user inputs the radius of the sphere
radius = float(input("radius of the sphere (metres): "))

#function to get the volume of the sphere
def volume():
    radius1 = radius
    #formula to get the volume of the sphere
    volume = (4 / 3 * math.pi * radius1**3)
    print("The volume of the sphere is", volume, "m3")
volume()


#function to get the surface of the sphere
def surface():
    radius2 = radius
    #formula to get the surface of the sphere
    surface = 4 * (math.pi) * (radius2**2)
    print("The surface of the sphere is", surface, "m2")
surface()


#function to get the circunference of the sphere
def circunference():
    radius3 = radius
    #formula to get the surface of the sphere
    circunference = 2 * (math.pi) * (radius3)
    print("The circunference of the sphere is", circunference)
circunference()

