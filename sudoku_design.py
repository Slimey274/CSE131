# 1. Name:
#      -Briant Woolley-
# 2. Assignment Name:
#      Lab 06 : Sudoku Program
# 3. Assignment Description:
#      -describe what this program is meant to do-
# 4. What was the hardest part? Be as specific as possible.
#      -a paragraph or two about how the assignment went for you-
# 5. How long did it take for you to complete the assignment?
#      -total time in hours including reading the assignment and submitting the program-

import json
import re

def load_game(filename):
    with open(filename, "r") as file:
        data = json.load(file)
        return data["board"]

def save_game(filename, board):
    with open(filename, "w") as file:
        json.dump({"board": board}, file, indent = 2 )
    print(f"Game saved to {filename}")

def display_board(board):
    print("  A B C D E F G H I")
    for idx, row in enumerate(board):
        print(idx + 1, " ".join(str(cell) if cell != 0 else "." for cell in row))

def parse_input(user_input):
    user_input = user_input.strip().lower()
    if user_input == 'q':
        return 'quit', None, None
    # this match makes it so that you can in put it ether way
    match = re.match(r"([a-i1-9])\s*([1-9a-i])\s+(\d+)", user_input)
    if not match:
        return 'invalid', None, None

    first, second, value_str = match.groups()
    # Determine which is the column letter and which is the row number
    col_letter = first if first.isalpha() else second
    row_number = first if first.isdigit() else second

    row = int(row_number) - 1
    col = ord(col_letter.upper()) - ord('A')
    try:
        value = int(value_str)
    except ValueError:
        return 'invalid', None, None
    return 'move', (row, col), value

def is_valid_move(row, col, value, board):
    if not (0 <= row < 9 and 0 <= col < 9):
        print("Invalid position: row and column must be between 1 and 9 (A-I).")
        return False
    if not (1 <= value <= 9):
        print("Invalid value: must be between 1 and 9.")
        return False
    if board[row][col] != 0:
        print("Cell is already filled.")
        return False
    if value in board[row]:
        print("Invalid move: value already in this row.")
        return False
    if value in [board[r][col] for r in range(9)]:
        print("Invalid move: value already in this column.")
        return False
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == value:
                print("Invalid move: value already in this 3x3 box.")
                return False
    return True

def choose_difficulty():
    print("Choose difficulty level:")
    print("1. Easy")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter 1, 2, or 3: ").strip()
        if choice == '1':
            return "131.05.Easy.json"
        elif choice == '2':
            return "131.05.Medium.json"
        elif choice == '3':
            return "131.05.Hard.json"
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def main():
    filename = choose_difficulty()
    board = load_game(filename)
    print(f"Sudoku Game Started ({filename}):")
    display_board(board)

    while True:
        user_input = input("Enter move (e.g., B2 5 or 2B 5), or 'Q' to quit: ")
        result, coords, value = parse_input(user_input)

        if result == 'quit':
            save_game("saved_game.json", board)
            print("Game saved. Goodbye!")
            break
        elif result == 'invalid':
            print("Invalid input. Please use format like 'B2 5' or '2B 5'.")
            continue

        row, col = coords
        if is_valid_move(row, col, value, board):
            board[row][col] = value
            display_board(board)
main()