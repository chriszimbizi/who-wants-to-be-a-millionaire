def play_again() -> bool:
    """
    Ask the user if they want to play again and return the response.

    Returns:
    - bool: True if the user wants to play again, False otherwise.
    """

    return input("\nDo you want to play again? (yes/no): ").lower().startswith("y")


def confirm_quit() -> bool:
    """
    Ask the user for confirmation before quitting and return the response.

    Returns:
    - bool: True if the user wants to quit, False otherwise.
    """

    return input("Are you sure you want to quit? (yes/no): ").lower().startswith("y")
