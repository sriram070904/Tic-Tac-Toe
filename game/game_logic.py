from .board import print_board
from .utils import get_player_move

def check_win(board, player):
    winning_combinations = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Columns
        (0, 4, 8), (2, 4, 6)               # Diagonals
    ]
    return any(board[a] == board[b] == board[c] == player
               for a, b, c in winning_combinations)

def draw(board):
    return all(cell in ('x', 'o') for cell in board)

def play_game():
    board = [str(i) for i in range(1, 10)]
    player = 'x'
    print_board(board)

    while True:
        move = get_player_move(player, board)
        board[move] = player
        print_board(board)

        if check_win(board, player):
            print(f"Player {player.upper()} wins!")
            break
        if draw(board):
            print("Match draws!")
            break

        player = 'o' if player == 'x' else 'x'
