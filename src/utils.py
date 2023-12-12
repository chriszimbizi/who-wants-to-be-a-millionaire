import os


def clear_screen() -> None:
    """
    Clears the console screen.

    Returns:
    - None
    """

    os.system("clear" if os.name == "posix" else "cls")


def user_response(prompt: str) -> bool:
    """
    Ask the user a yes/no question and return the response.

    Args:
    - prompt (str): The question prompt.

    Returns:
    - bool: True if the user answers 'yes', False otherwise.
    """
    return input(prompt + " (yes/no): ").lower().startswith("y")


def confirmation(action: str) -> bool:
    """
    Ask the user for confirmation before {action} and return the response.

    Returns:
    - bool: True if the user wants to {action}, False otherwise.
    """

    prompt = f"Are you sure you want to {action}?"
    return user_response(prompt)
