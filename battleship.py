import random
import os

board = [
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0"],
]

ship_row = random.randint(0, 4)
ship_column = random.randint(0, 4)
turn = 1
guess_left = 4
end_game = False

print("Battle Ship")
print("Guess a row and column for the ship in the range of 1 to 5")
print("you have 5 guesses to finish the game")
input()
os.system("cls")


def print_board(my_board):
    for y in my_board:
        print(" ".join(y))


while not end_game:
    print(f"turn {turn}\n")
    print_board(board)
    guess_row = int(input("guess the row: "))
    guess_column = int(input("guess the column: "))
    if guess_row == ship_row and guess_column == ship_column:
        print(f"great job! you won with {guess_left} guesses left")
        end_game = True
        input()
    elif guess_left == 0:
        print("game over! out of turns!")
        end_game = True
        input()
    elif guess_row != ship_row or guess_column != ship_column:
        if guess_row < 1 or guess_row > 5:
            print("yikes! that positions is outside of the range! try again")
            input()
            os.system("cls")
        elif board[guess_row][guess_column] == "X":
            print("you guessed that one already! try again")
            input()
            os.system("cls")
        else:
            turn += 1
            guess_left -= 1
            print("you missed! try again")
            board[guess_row][guess_column] = "X"
            input()
            os.system("cls")
