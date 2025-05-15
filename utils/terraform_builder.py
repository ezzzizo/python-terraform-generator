"""Module providing a function generating a terraform file to create new vpc"""

import os


def tf_code_builder(provider_region: str) -> str:
    """
    Generates Terraform configuration code for creating an AWS VPC.

    Prompts the user to input a CIDR block and a VPC name, then returns
    a formatted Terraform configuration string using the provided AWS region.

    Args:
        provider_region (str): The AWS region to specify in the Terraform provider block.

    Returns:
        str: A string containing the Terraform configuration code for the VPC.
    """
    print()  # empty line for readable output
    print("Configure VPC Settings ... \n")
    cidr: str = input("Enter CIDR block: (ex: 10.0.0.0/16)")
    print("-" * 10)
    name: str = input("Enter VPC Name: (ex: my_vpc)")

    terraform_code: str = f"""\
provider "aws" {{
  region = "{provider_region}"
}}
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


def vpc_tf_generator(provider_region: str) -> None:
    """Function generating a terraform file to create VPC"""
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(tf_code_builder(provider_region))
        print()
        print(" ... ✓ Terraform file generated successfully")
        print()
