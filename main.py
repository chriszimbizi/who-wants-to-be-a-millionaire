from src.menu import play_again, confirm_quit
from src.game import get_questions, play_game


def main() -> None:
    """
    The main function to run the game.

    Returns:
    - None
    """

    print("\nWelcome to Who Wants to Be a Millionaire!\n")
    while True:
        questions = get_questions()

        play_game(questions)

        if not play_again():
            if confirm_quit():
                print("\nGoodbye!\n")
                break


if __name__ == "__main__":
    main()
