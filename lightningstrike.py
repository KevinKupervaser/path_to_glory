import math

def lightning():
    speed_of_sound = .343 #m/s

    time = float(input("Time between flash and thunder: "))

    storm_distance = time * speed_of_sound

    print(storm_distance)
lightning()

