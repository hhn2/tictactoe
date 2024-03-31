import os
import platform

def clear_screen():
    """Clears the console screen."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

def display_board(board):
    clear_screen()
    for row in board:
        print(" | ".join(row))
        print("-" * 9)  # Divider between rows

def check_win(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ": return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ": return board[0][i]
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ": return board[1][1]
    return None

def check_draw(board):
    for row in board:
        if " " in row: return False
    return True

def player_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move as row,col (e.g., 1,2): ")
            row, col = map(int, move.split(','))
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("This cell is already taken. Please choose another one.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers from 0 to 2, separated by a comma.")

def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        display_board(board)
        player_move(board, current_player)
        if check_win(board):
            display_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

play_game()
