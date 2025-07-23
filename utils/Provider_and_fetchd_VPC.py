"""Module providing a function generating a terraform file with the fetchd vpcs"""

import os


def tf_provider(provider_region: str) -> None:
    """Ensures a Terraform provider block exists in the output file.

    This function checks for 'vpc.tf' in the parent directory. If the file
    does not exist, it creates it. It then writes the AWS provider block
    to the file, but only if the file is empty.

    Args:
        provider_region (str): The AWS region identifier (e.g., "us-east-1").

    Side Effects:
        - Creates 'vpc.tf' if it does not exist.
        - Writes AWS provider block to 'vpc.tf' if it is empty.
    """
    terraform_provider: str = f"""\
provider "aws" {{
  region = "{provider_region}"
}}
\n \n
"""
    # Get the path to the parent directory
    parent_dir = os.path.dirname(os.path.dirname(__file__))

    # Full path to the Terraform file
    file_path = os.path.join(parent_dir, "vpc.tf")

    if not os.path.exists(file_path):
        # Create empty file if it doesn't exist
        with open(file_path, "w", encoding="utf-8") as _:
            pass

    if os.stat(file_path).st_size == 0:
        with open(file_path, "w", encoding="utf-8") as file_obj:
            file_obj.write(terraform_provider)
    else:
        return


def fetchd_vpc_tf_builder(cidr: str, name: str | None, vpcid: str) -> str:
    """Builds a Terraform resource block for an existing VPC.

    This function takes the details of a fetched VPC and formats them
    into an 'aws_vpc' resource string. This string is intended to be
    written to a .tf file to manage the existing resource with Terraform.
    Handles cases where the VPC has no Name tag.

    Args:
        cidr (str): The CIDR block of the existing VPC.
        name (str | None): The Name tag of the VPC. Can be None.
        vpcid (str): The ID of the existing VPC (e.g., "vpc-12345").

    Returns:
        str: A formatted string for the Terraform 'aws_vpc' resource.
    """
    print()  # empty line for readable output
    print("Configuring terraform file ...")

    terraform_code: str = f"""\

# VPC ID used to import and link the existing AWS resource to this Terraform resource block: {vpcid}
resource "aws_vpc" "{name or 'UnnamedVPC'}" {{
  cidr_block = "{cidr}"

  tags = {{
    Name = "{name or 'UnnamedVPC'}"
  }}
}} \n \n
"""

    return terraform_code
