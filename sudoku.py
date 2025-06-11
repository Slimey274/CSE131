# 1. Name:
#      -Briant-
# 2. Assignment Name:
#      Lab 05 : Sudoku Draft
# 3. Assignment Description:
#      -The program is a draft of a sudoku game-
# 4. What was the hardest part? Be as specific as possible.
#      -The assignment was good it didnt take top long and was pretty easy to figure out. The hardest part was making sure the json file was correct. IT was also figuring out how to run it and make it work.-
# 5. How long did it take for you to complete the assignment?
#      -3 hr-

import json

def load_board(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
        return data['board']

def save_board(filename, board):
    with open(filename, 'w') as file:
        json.dump({"board": board}, file, indent=2)
    print(f"Game saved to {filename}")

def display_board(board):
    for row in board:
        print(" ".join(str(cell) if cell != 0 else "." for cell in row))

def valid_move(row, col, value, board):
    if not (0 <= row < 9 and 0 <= col < 9):
        print("Invalid position: row and column must be between 0 and 8.")
        return False
    if not (1 <= value <= 9):
        print("Invalid value: must be between 1 and 9.")
        return False
    if board[row][col] != 0:
        print("Cell is already filled.")
        return False
    return True

def main():
    board = load_board("131.05.Easy.json")
    print("Loaded board:")
    display_board(board)

    while True:
        move = input("Enter move (row col value), or 'save' to save and quit: ")
        if move.strip().lower() == "save":
            save_board("saved_game.json", board)
            break
        try:
            row, col, value = map(int, move.strip().split())
            if valid_move(row, col, value, board):
                board[row][col] = value
                display_board(board)
        except ValueError:
            print("Invalid input format. Please enter: row col value (e.g., 0 3 4)")

if __name__ == "__main__":
    main()
