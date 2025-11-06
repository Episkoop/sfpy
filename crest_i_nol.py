def print_board(board):
    for column in board:
        print("|" + "|".join(column) + "|")

def player_move(player):
    while True:
        move =int(input(f"игрок {player}, ходит на (1-9): ")) - 1
        if 0 <= move <= 8 and board[move // 3][move % 3] == " ":
            return move
        else:
            print("ход вне системы")

def check_win(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]
    return None

board = [[" " for _ in range(3)] for _ in range(3)]

current_player = "X"
game_over = False

while not game_over:
    print_board(board)

    move = player_move(current_player)

    board[move // 3][move % 3] = current_player

    winner = check_win(board)
    if winner:
        print_board(board)
        print(f"игрок {winner} выиграл")
        game_over = True
    elif " " not in board[0] + board[1] + board[2]:
        print_board(board)
        print("ничья")
        game_over = True
    else:
        current_player = "O" if current_player == "X" else "X"