# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 01: Tic-Tac-Toe
# 3. Assignment Description:
#      Play the game of Tic-Tac-Toe
# 4. What was the hardest part? Be as specific as possible.
#      -I feel that the hardest part of this assignment is getting back into the swing of things.
# I also feel that it was making the game work and display correctly. This is what I felt was the most difficult for me.
# It will be intresting to see what will be the hardest as we move on.-
# 5. How long did it take for you to complete the assignment?
#      -1hr 30min-
import os
import json

# The characters used in the Tic-Tac-Too board.
# These are constants and therefore should never have to change.
X = 'X'
O = 'O'
BLANK = ' '

# A blank Tic-Tac-Toe board. We should not need to change this board;
# it is only used to reset the board to blank. This should be the format
# of the code in the JSON file.
blank_board = {  
            "board": [
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK,
                BLANK, BLANK, BLANK ]
        }

def read_board(filename):
    '''Read the previously existing board from the file if it exists.'''
    # Put file reading code here.
    if os.path.exists(filename):
        with open(filename, 'rt') as filehandle:
            data = json.load(filehandle)
            return data['board']
    else:
        return blank_board['board']

def save_board(filename, board):
    '''Save the current game to a file.'''
    # Put file writing code here.
    with open(filename, 'wt') as game:
        json.dump({'board': board}, game)

def display_board(board):
    '''Display a Tic-Tac-Toe board on the screen in a user-friendly way.'''
    # Put display code here.
    for row in range(3):
        row_diplay = ' ' + ' | '.join(board[row*3:row*3+3])
        print(row_diplay)
        if row < 2:
            print("---+---+---")

def is_x_turn(board):
    '''Determine whose turn it is.'''
    # Put code here determining if it is X's turn.
    x_count = board.count(X)
    o_count = board.count(O)
    return x_count == o_count

def play_game(board):
    '''Play the game of Tic-Tac-Toe.'''
    # Put game play code here. Return False when the user has indicated they are done.
    while not game_done(board, message=True):
        display_board(board)
        turn = X if is_x_turn(board) else O
        print(f"It's {turn}'s turn.")

        move = input("Enter your move (1-9) or type 'q' to quit: ")
        if move.lower() == 'q':
            return False
        
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        position = int(move) - 1
        if board[position] != BLANK:
            print("That space is already taken. Try again.")
            continue
        
        board[position] = turn
        save_board('game.json', board)
    
    display_board(board)
    return False
    


def game_done(board, message=False):
    '''Determine if the game is finished.
       Note that this function is provided as-is.
       You do not need to edit it in any way.
       If message == True, then we display a message to the user.
       Otherwise, no message is displayed. '''

    # Game is finished if someone has completed a row.
    for row in range(3):
        if board[row * 3] != BLANK and board[row * 3] == board[row * 3 + 1] == board[row * 3 + 2]:
            if message:
                print("The game was won by", board[row * 3])
            return True

    # Game is finished if someone has completed a column.
    for col in range(3):
        if board[col] != BLANK and board[col] == board[3 + col] == board[6 + col]:
            if message:
                print("The game was won by", board[col])
            return True

    # Game is finished if someone has a diagonal.
    if board[4] != BLANK and (board[0] == board[4] == board[8] or
                              board[2] == board[4] == board[6]):
        if message:
            print("The game was won by", board[4])
        return True

    # Game is finished if all the squares are filled.
    tie = True
    for square in board:
        if square == BLANK:
            tie = False
    if tie:
        if message:
            print("The game is a tie!")
        return True


    return False

# These user-instructions are provided and do not need to be changed.
print("Enter 'q' to suspend your game. Otherwise, enter a number from 1 to 9")
print("where the following numbers correspond to the locations on the grid:")
print(" 1 | 2 | 3 ")
print("---+---+---")
print(" 4 | 5 | 6 ")
print("---+---+---")
print(" 7 | 8 | 9 \n")
print("The current board is:")

# The file read code, game loop code, and file close code goes here.

filename = 'game.json'
board = read_board(filename)
display_board(board)
if not play_game(board):
    save_board(filename, board)
    print("Game saved. Goodbye!")

board = blank_board['board']
save_board(filename, board)
play_again = input("Play again? (y/n): ").lower()
if play_again != 'y':
    print("Thanks for playing!")