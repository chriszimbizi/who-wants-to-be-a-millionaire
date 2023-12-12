import json

leaderboard_file = "who-wants-to-be-a-millionaire/data/leaderboard.json"


# Load leaderboard data from the file
def load_leaderboard() -> dict:
    """
    Load the leaderboard data from the JSON file.

    Returns:
    - dict: The leaderboard data.
    """

    try:
        with open(leaderboard_file, "r") as file:
            return json.load(file)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}


def display_leaderboard(leaderboard: dict) -> None:
    """
    Display the current leaderboard.

    Args:
    - leaderboard (dict): The current leaderboard data.

    Returns:
    - None
    """
    if not leaderboard:
        print("\nLeaderboard is empty.\n")
    else:
        print("\nLeaderboard:\n")
        print(f"{'Rank':<5} | {'Player':<10} | {'Score':<10}")
        print("-" * 28)

        for rank, (player, score) in enumerate(
            sorted(leaderboard.items(), key=lambda x: x[1], reverse=True), start=1
        ):
            print(f"{rank:<5} | {player:<10} | {score:<10}")
        print()


def update_leaderboard(leaderboard: dict, player_name: str, score: int) -> None:
    """
    Save the player's score in the leaderboard.

    Args:
    - leaderboard (dict): The current leaderboard data.
    - player_name (str): The name of the player.
    - score (int): The player's score.

    Returns:
    - None
    """

    if player_name not in leaderboard or score > leaderboard[player_name]:
        # Update the score only if the player is new or has a higher score
        leaderboard[player_name] = score

    with open(leaderboard_file, "w") as f:
        json.dump(leaderboard, f)
