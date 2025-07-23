"""Main module:
Generates a Terraform configuration file for AWS VPCs.

This interactive script prompts the user to select an AWS region, lists
existing resources (VPCs and EC2 instances), and then allows the user
to either generate a new VPC configuration or import existing VPCs into
a 'vpc.tf' file.
"""

from utils.aws_region import region_selector
from utils.list_vpcs import vpcs_list
from utils.list_ec2 import ec2_list
from utils.new_vpc_builder import new_vpc_tf_generator
from utils.Provider_and_fetchd_VPC import fetchd_vpc_tf_builder
from utils.Provider_and_fetchd_VPC import tf_provider


class NumberOutOfRangeError(Exception):
    """This exception is raised when a user has provided incorrect choice."""


def main():
    """Drives the main application flow for generating VPC Terraform code.

    This function orchestrates the user interaction, starting with region
    selection and discovery of existing resources (EC2, VPC). It then
    prompts the user to choose an action for Terraform file generation
    and handles the corresponding logic.

    Side Effects:
        - Prints information and prompts to the console.
        - Creates or appends to a file named 'vpc.tf' in the current directory.
          (Note: interacts with the file system)

    Raises:
        ValueError: Handled internally if the user provides non-integer input.
        NumberOutOfRangeError: Handled internally if the user's choice is invalid.
    """
    # selecting region
    print()
    region: str = region_selector()

    # listing Ec2 instances
    ec2_list(region)

    # listing vpcs
    vpcids, cidrs, names = vpcs_list(region)

    # Checking user input
    while True:
        try:
            choice: int = int(
                input(
                    "Fetchd VPCs are ready, Choose wisely: what do you want to do?"
                    "\nEnter the number next to your choice: (1-3) \n "
                    "(1) = Configure new VPC \n "
                    "(2) = Configure the fetchd VPCs \n "
                    "(3) = Nothing, just exit \n "
                )
            )
            file_path = "vpc.tf"
            match choice:
                case 1:
                    tf_provider(region)
                    new_vpc_tf_generator()
                    print("terraform file is ready with your new VPC")
                    break
                case 2:
                    with open(file_path, "a", encoding="utf-8") as f:
                        for names, vpcids, cidrs in zip(names, vpcids, cidrs):
                            print(f"Adding VPC {vpcids} to Terraform file...")
                            block = fetchd_vpc_tf_builder(cidrs, names, vpcids)
                            f.write(block)
                            print(" ... ✓ successfully added.")
                            print("terraform file is ready with your fitchd VPCs")
                    break
                case 3:
                    print("Session has ended")
                    break
                case _:
                    raise NumberOutOfRangeError(
                        f"Input '{choice}' is not one of the listed regions (1–2)."
                    )
        except ValueError as v:
            print(f"❌ Error, input is not a valid number: {v} \ntry again:")
        except NumberOutOfRangeError as e:
            print(f"❌ Error: number out of range — {e} \ntry again:")


if __name__ == "__main__":
    main()
