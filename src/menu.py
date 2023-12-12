from .utils import clear_screen


def display_menu() -> int:
    """
    Display the menu and prompt the user for a choice.

    Returns:
    - int: The user's menu choice.
    """

    clear_screen()

    welcome = "Welcome to Who Wants to Be a Millionaire!"
    print(welcome)
    print("-" * len(welcome))

    print("\nMenu:")
    print("\t1. Start Game")
    print("\t2. Leaderboard")
    print("\t3. Quit")

    while True:
        try:
            choice = int(input("\nEnter your choice (1, 2, or 3): "))
            if 1 <= choice <= 3:
                return choice
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a number.")
