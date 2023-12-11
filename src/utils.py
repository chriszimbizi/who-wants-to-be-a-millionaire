import os


def clear_screen() -> None:
    """
    Clears the console screen.

    Returns:
    - None
    """

    os.system("clear" if os.name == "posix" else "cls")
