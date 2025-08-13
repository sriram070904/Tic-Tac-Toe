from game.game_logic import play_game

if __name__ == "__main__":
    while True:
        play_game()
        again = input("Do you want to play again? (yes/no): ").strip().lower()
        if again != 'yes':
            print("Thanks for playing!")
            break
