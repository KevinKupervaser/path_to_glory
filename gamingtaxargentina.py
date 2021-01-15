import math

def gamingtaxargentina():

    print("This program calculates the value of a videogame + taxes in Argentina (MicrosoftStore).")
    game_value = float(input("Enter the value of the game (ARS): "))
    game_value = (game_value * 164.001) / 100
    print("The price of the game + taxes is: ", game_value)

gamingtaxargentina()
