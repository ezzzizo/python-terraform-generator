"""Module providing a function generating a terraform file to create new vpc"""

import os


def tf_vpc_builder() -> str:
    """Generates Terraform configuration code for an AWS VPC.

    Prompts the user to input a CIDR block and a VPC name, then returns
    a formatted Terraform configuration string.

    Returns:
        str: A string containing the Terraform configuration for the VPC.
    """
    print()  # empty line for readable output
    print("Configure VPC Settings ... \n")
    cidr: str = input("Enter CIDR block: (e.g., 10.0.0.0/16)")
    print("-" * 10)
    name: str = input("Enter VPC Name: (e.g., my_vpc)")

    # Terraform VPC code block
    terraform_code: str = f"""\

resource "aws_vpc" "{name}" {{
  cidr_block = "{cidr}"

  tags = {{
    Name = "{name}"
  }}
}}
"""
    return terraform_code


# Get the path to the parent directory
parent_dir = os.path.dirname(os.path.dirname(__file__))

# Full path to the Terraform file
file_path = os.path.join(parent_dir, "vpc.tf")


def new_vpc_tf_generator() -> None:
    """Generates and appends a new VPC configuration to the Terraform file.

    This function orchestrates the creation of a new VPC block by calling
    the interactive `tf_vpc_builder` function. It then appends the returned
    Terraform code to the 'vpc.tf' file located in the project's root directory.

    Side Effects:
        - Prompts the user for input via the console (by calling tf_vpc_builder).
        - Appends configuration data to the 'vpc.tf' file.
          (Note: interacts with the file system)
        - Prints a success message to the console upon completion.
    """
    with open(file_path, "a+", encoding="utf-8") as f:
        f.write(tf_vpc_builder())
        print()
        print(" ... ✓ Terraform file generated successfully")
        print()
