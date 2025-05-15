"""This module contains utility functions for AWS region selecting"""


class NumberOutOfRangeError(Exception):
    """This exception is raised when a user has provided incorrect choice."""


def get_selected_region(user_input: int, selected_region: str | None = None) -> str:
    """Selects an AWS region based on the user's input.

    Args:
        user_input (int): User's input, expected to be a number from 1 to 4.
        selected_region (str | None, optional): The selected region. Defaults to None.

    Raises:
        NumberOutOfRangeError: triggered when users input is not one of 4 listed regions

    Returns:
        str: The selected region as a string.
    """

    # Selecting on of 4 regions based on user's input
    match user_input:
        case 1:
            selected_region = "us-east-1"
            return selected_region
        case 2:
            selected_region = "us-east-2"
            return selected_region
        case 3:
            selected_region = "us-west-1"
            return selected_region
        case 4:
            selected_region = "us-west-2"
            return selected_region
        case _:
            raise NumberOutOfRangeError(
                f"Input '{user_input}' is not one of the listed regions (1–4)."
            )


# taking user's input
def region_selector() -> str:
    """Prompts the user to choose one of four listed AWS regions.

    Returns:
        str: The selected AWS region as a string.
    """
    while True:
        try:
            choice: int = int(
                input(
                    "Which AWS US region would you like to use? "
                    "\nEnter the number next to your choice: (1-4) \n "
                    "(1) = us-east-1 \n "
                    "(2) = us-east-2 \n "
                    "(3) = us-west-1 \n "
                    "(4) = us-west-2 \n"
                )
            )
            region: str = get_selected_region(choice)
            return region
        except ValueError as v:
            print(f"❌ Error, input is not a valid number: {v} \ntry again:")
        except NumberOutOfRangeError as e:
            print(f"❌ Error: number out of range — {e} \ntry again:")
