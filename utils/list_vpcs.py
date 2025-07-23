"""This module contains utility functions for listing VPCs in the chosen AWS region"""

import boto3
from botocore.exceptions import ClientError

# from utils.terraform_builder import tf_code_builder, tf_provider


def vpcs_list(vpc_region: str) -> tuple[list[str], list[str], list[str]]:
    """Fetches AWS VPCs, prints their details, and returns their data.

    Connects to AWS to retrieve all VPCs in a specified region. It prints
    a formatted list of each VPC's ID, CIDR block, and Name tag to the
    console. It also collects this data into lists and returns them.

    Args:
        vpc_region (str): The AWS region identifier (e.g., "us-east-1").

    Returns:
        tuple[list[str], list[str], list[str]]: A tuple containing three
        lists: 1. VPC IDs, 2. VPC CIDR blocks, and 3. VPC name tags.

    Side Effects:
        - Prints a formatted list of all discovered VPCs to the console.
        - Prints status or error messages to the console.
    """
    print(f"\n listing vpcs in ({vpc_region}) ...")
    print()  # empty line for readable output

    # creating an empty list, as a container for each VPC paramiter
    vpc_ids = []
    vpc_cidr_blocks = []
    name_tags = []

    # Fetching and printing vpcs
    try:
        client = boto3.client("ec2", region_name=vpc_region)

        response = client.describe_vpcs()
        vpcs = response.get("Vpcs", [])

        # in case on no vpcs found in region
        if not vpcs:
            print(f"No vpcs found: region >> {vpc_region}")
            return [], [], []

        # printing vpcs details and creating the terraform file
        print(f"\nVPCs in region {vpc_region}: \n")
        for vpc in vpcs:
            vpc_ids.append(vpc.get("VpcId"))
            vpc_cidr_blocks.append(vpc.get("CidrBlock"))

            # checking for tags
            name = None
            tags = vpc.get("Tags", [])
            for tag in tags:
                if tag.get("Key") == "Name":
                    name = tag.get("Value")
                    break
            name_tags.append(name)

            print("_" * 30)
            print(f"| vpc ID: {vpc_ids[-1]}")
            print(f"| vpc_cidr: {vpc_cidr_blocks[-1]}")
            print(f"| vpc name: {name_tags[-1]}")

            print("-" * 30)

    # errors
    except ClientError as e:
        print(f"client error: {e}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")

    print("\n")
    print("=" * 30)
    return vpc_ids, vpc_cidr_blocks, name_tags
