#tictactoe by swmwy
import random
from time import sleep


print("Tic\nTac\nToe")

grid1 = ""
grid2 = ""
grid3 = ""
grid4 = ""
grid5 = ""
grid6 = ""
grid7 = ""
grid8 = ""
grid9 = ""

while True:
    player_input = input("Where:")
    if player_input == 1:
        grid1 = "X"
    elif player_input == 2:
        grid2 = "X"
    elif player_input == 3:
        grid3 = "X"
    elif player_input == 4:
        grid4 = "X"
    elif player_input == 5:
        grid5 = "X"
    elif player_input == 6:
        grid6 = "X"
    elif player_input == 7:
        grid7 = "X"
    elif player_input == 8:
        grid8 = "X"
    else:
        grid9 = "X"