"""This module contains utility functions for AWS region selecting"""


class NumberOutOfRangeError(Exception):
    """This exception is raised when a user has provided incorrect choice."""


def get_selected_region(user_input: int) -> str:
    """Converts a numeric choice into an AWS region string.

    Args:
        user_input (int): User's input, expected to be a number from 1 to 4.

    Raises:
        NumberOutOfRangeError: triggered when users input is not one of 4 listed regions

    Returns:
        str: The selected region as a string.
    """

    # Selecting on of 4 regions based on user's input
    match user_input:
        case 1:
            return "us-east-1"
        case 2:
            return "us-east-2"
        case 3:
            return "us-west-1"
        case 4:
            return "us-west-2"
        case _:
            raise NumberOutOfRangeError(
                f"Input '{user_input}' is not one of the listed regions (1–4)."
            )


# taking user's input
def region_selector() -> str:
    """Interactively prompts a user to select an AWS region.

    This function displays a menu of choices and handles user input validation,
    re-prompting on errors until a valid selection is made.

    Side Effects:
        - Prints the region selection menu to the console.
        - Prints error messages to the console for invalid input.

    Returns:
        str: The selected AWS region name (e.g., "us-east-1").

    Raises:
        ValueError: Handled internally if the user provides non-integer input.
        NumberOutOfRangeError: Handled internally if the user's choice is invalid.
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
