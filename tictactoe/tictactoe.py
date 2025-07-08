def create_board():
    return [["#" for _ in range(3)] for _ in range(3)]

def print_board(board):
    print("---------")
    for row in board:
        print(" | ".join(row))
        print("---------")

def check_winner(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "#":
            return True, board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != "#":
            return True, board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != "#":
        return True, board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != "#":
        return True, board[0][2]
    return False, None

def utility(board):
    flag, winner = check_winner(board)
    if winner == "X":
        return 10
    elif winner == "O":
        return -10
    else:
        return 0

def is_full(board):
    return all(cell != "#" for row in board for cell in row)

def get_valid_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == "#"]

def minimax(board, is_maximizing, depth):
    flag, winner = check_winner(board)
    if flag or is_full(board) or depth == 0:
        return utility(board)

    if is_maximizing:
        best_score = float("-inf")
        for i, j in get_valid_moves(board):
            board[i][j] = "X"
            score = minimax(board, False, depth - 1)
            board[i][j] = "#"
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for i, j in get_valid_moves(board):
            board[i][j] = "O"
            score = minimax(board, True, depth - 1)
            board[i][j] = "#"
            best_score = min(best_score, score)
        return best_score

def best_move(board, player, depth):
    best_score = float("-inf") if player == "X" else float("inf")
    move = None

    for i, j in get_valid_moves(board):
        board[i][j] = player
        score = minimax(board, player == "O", depth - 1)
        board[i][j] = "#"
        if (player == "X" and score > best_score) or (player == "O" and score < best_score):
            best_score = score
            move = (i, j)
    return move

def human_move(board):
    while True:
        try:
            x, y = map(int, input("Enter your move (row and column 1-3): ").split())
            x -= 1
            y -= 1
            if 0 <= x <= 2 and 0 <= y <= 2 and board[x][y] == "#":
                return x, y
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter two numbers between 1 and 3.")

# --- Game Start ---
print("Welcome to Tic Tac Toe!")
depth = int(input("Choose AI difficulty (1-9, higher = smarter): "))

board = create_board()
print_board(board)

# X = AI, O = Human
current_player = "X"

while not check_winner(board)[0] and not is_full(board):
    if current_player == "X":
        i, j = best_move(board, "X", depth)
        print(f"AI plays: ({i + 1}, {j + 1})")
    else:
        i, j = human_move(board)

    board[i][j] = current_player
    print_board(board)
    current_player = "O" if current_player == "X" else "X"

flag, winner = check_winner(board)
if winner:
    print(f"{winner} wins!")
else:
    print("It's a tie!")