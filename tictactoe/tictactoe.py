def create_board():
    return [["#" for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("---------")
        print(" | ".join(row))
    print("---------")

def make_move(board, move_num):
    while True:
        try:
            move = input("Enter x y coordinates (1-3): ").split()
            x = int(move[0]) - 1  # convert to 0-based index
            y = int(move[1]) - 1

            if 0 <= x <= 2 and 0 <= y <= 2:
                if board[x][y] == "#":
                    board[x][y] = "X" if move_num % 2 == 0 else "O"
                    return board, move_num + 1
                else:
                    print("That space is already taken. Try again.")
            else:
                print("Coordinates must be between 1 and 3.")
        except (ValueError, IndexError):
            print("Invalid input. Enter two numbers between 1 and 3 separated by space.")

# Game loop
board = create_board()
move_num = 1

print_board(board)
for _ in range(9):  # Max 9 moves in Tic Tac Toe
    board, move_num = make_move(board, move_num)
    print_board(board)

            