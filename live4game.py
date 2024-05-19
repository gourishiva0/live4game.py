def create_board():
    return [[' ' for _ in range(7)] for _ in range(6)]

def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-' * 29)

def is_valid_move(board, column):
    return board[0][column] == ' '

def drop_piece(board, column, player):
    for row in range(5, -1, -1):
        if board[row][column] == ' ':
            board[row][column] = player
            break

def check_winner(board, player):
    # Check rows
    for row in range(6):
        for col in range(4):
            if all(board[row][col + i] == player for i in range(4)):
                return True

    # Check columns
    for col in range(7):
        for row in range(3):
            if all(board[row + i][col] == player for i in range(4)):
                return True

    # Check diagonals
    for row in range(3):
        for col in range(4):
            if all(board[row + i][col + i] == player for i in range(4)):
                return True
            if all(board[row + i][col + 3 - i] == player for i in range(4)):
                return True

    return False

def is_board_full(board):
    return all(cell != ' ' for row in board for cell in row)

def play_connect_four():
    board = create_board()
    players = ['X', 'O']
    current_player = 0

    while True:
        print_board(board)
        column = int(input(f"Player {players[current_player]}, choose a column (0-6): "))

        if 0 <= column <= 6 and is_valid_move(board, column):
            drop_piece(board, column, players[current_player])
            if check_winner(board, players[current_player]):
                print_board(board)
                print(f"Player {players[current_player]} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a draw!")
                break

            current_player = (current_player + 1) % 2
        else:
            print("Invalid move. Please try again.")

if __name__ == "__main__":
    play_connect_four()