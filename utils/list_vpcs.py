"""This module contains utility functions for listing vpc in a specific region"""

import boto3
from botocore.exceptions import ClientError


def vpcs_list(vpc_region: str) -> None:
    """Lists all VPCs in a specified AWS region

    Args:
        vpc_region (str): The AWS region to list VPCs from
    """
    print(f"listing vpcs in ({vpc_region}) ...")
    print()  # empty line for readable output
    # Fetching and printing vpcs
    try:
        client = boto3.client("ec2", region_name=vpc_region)

        response = client.describe_vpcs()
        vpcs = response.get("Vpcs", [])

        # in case on no vpcs found in region
        if not vpcs:
            print(f"No vpcs found: region >> {vpc_region}")
            return

        # printing vpcs details
        print(f"\nVPCs in region {vpc_region}:")
        for vpc in vpcs:
            vpc_id = vpc.get("VpcId")
            vpc_cidr_block = vpc.get("CidrBlock")

            # checking for tags
            name_tag = None
            tags = vpc.get("Tags", [])
            for tag in tags:
                if tag.get("Key") == "Name":
                    name_tag = tag.get("Value")
                    break

            print(f"vpc ID: {vpc_id}")
            print(f"vpc_cidr: {vpc_cidr_block}")
            print(f"vpc name: {name_tag}")
            print("-" * 30)

    # errors
    except ClientError as e:
        print(f"client error: {e}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")


# End-of-file (EOF)
