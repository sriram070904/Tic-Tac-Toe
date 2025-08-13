def get_player_move(player, board):
    while True:
        move = input(f"Enter your move {player.upper()} (1-9): ").strip()
        if not move.isdigit() or not (1 <= int(move) <= 9):
            print("Invalid input! Please enter a number from 1 to 9.")
            continue

        move = int(move) - 1
        if board[move] in ('x', 'o'):
            print("Cell is already taken.")
            continue

        return move
