import json
import random
import time
from typing import List, Dict
from .utils import clear_screen, confirmation


file_name = "who-wants-to-be-a-millionaire/data/questions.json"

money_scale = [
    100,
    200,
    300,
    500,
    1000,
    2000,
    4000,
    8000,
    16000,
    32000,
    64000,
    125000,
    250000,
    500000,
    1000000,
]


def get_player_name() -> str:
    """
    Get the player's name from the user.

    Returns:
    - str: The validated and lowercased player's name.
    """
    while True:
        player_name = input("\nEnter your name: ").strip()

        if player_name.isalpha() and len(player_name) < 15:
            return player_name.lower()
        else:
            print("Invalid name. Please use up to only 15 letters.")


def get_questions() -> List[Dict]:
    """
    Load questions from the JSON file and shuffle them.

    Returns:
    - List[Dict]: Shuffled list of questions.
    """
    with open(file_name, "r") as f:
        data = json.load(f)
        questions = data["questions"]
        random.shuffle(questions)
    return questions


def display_options(question: Dict) -> None:
    """
    Display the question and answer options.

    Args:
    - question (Dict): The current question.

    Returns:
    - None
    """
    print("Question: ", question["question"])
    print("Options:")
    for i, option in enumerate(question["options"], start=1):
        print(f"\t{i}. {option}")
    print()


def get_user_answer(question: Dict) -> int:
    """
    Prompt the user for an answer and return it.

    Args:
    - question (Dict): The current question.

    Returns:
    - int: The user's selected answer.
    """
    while True:
        try:
            user_answer = int(input("Answer: "))
            if 1 <= user_answer <= len(question["options"]):
                return user_answer
            else:
                print(
                    "Invalid input. Please enter a number between 1 and",
                    len(question["options"]),
                )
        except ValueError:
            print("Invalid input. Please enter a number.\n")


def cash_out(total_money: int) -> bool:
    """
    Ask the user if they want to cash out or continue.

    Args:
    - total_money (int): The total money accumulated so far.

    Returns:
    - bool: True if the user wants to cash out, False if they want to continue.
    """
    while True:
        cash_out_input = input(
            f"Do you want to cash out with ${total_money}? (yes/no): "
        ).lower()
        if cash_out_input == "yes":
            return True
        elif cash_out_input == "no":
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def play_game(questions: List[Dict]) -> int:
    """
    Play a single game of Who Wants to Be a Millionaire.

    Args:
    - questions (List[Dict]): List of questions to be used in the game.

    Returns:
    - int: The final amount of money earned in the game.
    """
    money_earned = 0

    for i, question in enumerate(questions):
        question_worth = money_scale[i]

        time.sleep(2)
        clear_screen()
        print(f"In the Bank: ${money_earned} | Current Prize: ${question_worth}\n")
        display_options(question)

        correct_answer = question["correct"] + 1
        user_answer = get_user_answer(question)

        if user_answer != correct_answer:
            if money_earned == 0:
                print("Golden Duck! Better luck next time.\n")
            else:
                print(
                    f"Game Over! You lost ${money_earned}, maybe you should've cashed out.\n"
                )
            return money_earned
        else:
            print("Congratulations", end=" ")
            money_earned = question_worth

        if cash_out(money_earned):
            if confirmation("cash out"):
                print(f"Wise choice! You cashed out with ${money_earned}.\n")
                return money_earned

    if money_earned == money_scale[len(money_scale) - 1]:
        print(
            "Congratulations! You answered all questions correctly and won $1,000,000!"
        )

    return money_earned
