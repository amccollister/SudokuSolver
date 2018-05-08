import random
from datetime import datetime
from board import Board
from square import Square

now = datetime.now()
board = Board()
with open("files/input.txt", "r") as file:
    for i in range(9):
        line = file.readline().split(' ')
        for j in range(9):
            val = int(line[j])
            board.set_square(i, j, int(line[j]))
board.establish_choices()
board.print()

while not board.check_board():
    if not board.fill_single_choice():
        print("Cannot find any single choices. Guessing...")
        if board.make_guess() is None:
            print("There were no guesses to make!")
            break
        else:
            print("I set {0.row} {0.col} to {0.value} and its remaining choices are {0.choice}".format(board.guess[-1]))
    board.establish_choices()
    
    if board.guess and board.check_choice():
        print("There was a problem with one of my previous guesses. Adjusting...")
        board.reset_guess()
    

print("\nBoard is solved." if board.validate_board() else "\nBoard is incomplete.")
board.print()
print("I completed this in {}".format(datetime.now() - now))
