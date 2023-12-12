from src.utils import user_response, confirmation
from src.menu import display_menu
from src.leaderboard import (
    load_leaderboard,
    display_leaderboard,
    update_leaderboard,
)
from src.game import get_questions, play_game


def main() -> None:
    """
    The main function to run the game.

    Returns:
    - None
    """

    leaderboard = load_leaderboard()

    while True:
        menu_choice = display_menu()

        if menu_choice == 1:
            # Start the game
            player_name = input("\nEnter your name: ").lower()
            questions = get_questions()
            score = play_game(questions)
            update_leaderboard(leaderboard, player_name, score)

            if not user_response("Do you want to play again?"):
                if not user_response("Return to main menu?"):
                    if confirmation("quit"):
                        print("\nGoodbye!\n")
                        break
        elif menu_choice == 2:
            # Display the leaderboard
            display_leaderboard(leaderboard)
            if not user_response("Return to main menu?"):
                if confirmation("quit"):
                    print("\nGoodbye!\n")
                    break
        elif menu_choice == 3:
            if confirmation("quit"):
                print("\nGoodbye!\n")
                break


if __name__ == "__main__":
    main()
