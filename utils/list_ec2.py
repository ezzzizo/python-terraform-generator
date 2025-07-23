"""This module contains utility functions for listing EC2s instances in the chosen AWS region"""

import boto3
from botocore.exceptions import ClientError


def ec2_list(ec2_region: str) -> None:
    """Fetches and prints a detailed list of EC2 instances for a given region.

    This function connects to AWS using boto3 to retrieve all EC2 instances.
    It then prints key details for each one, such as its name tag, ID, type,
    state, and public IP address. It handles cases where no instances are found
    and catches potential AWS client errors.

    Args:
        ec2_region (str): The AWS region identifier (e.g., "us-east-1").

    Side Effects:
        - Prints a formatted list of EC2 instances to the console.
        - Prints status or error messages to the console.
    """
    print(f"listing Ec2 instances in ({ec2_region}) ...")
    print()  # empty line for readable output

    # Fetching and printing instances
    try:
        client = boto3.client("ec2", region_name=ec2_region)

        response = client.describe_instances()
        reservations = response.get("Reservations", [])

        # in case on no instances found in region
        if not reservations:
            print(f"No ec2 found in region >> {ec2_region}")
            return

        # printing instances details
        print(f"\nEc2 instances in region {ec2_region}: \n")

        for reservation in reservations:
            instances = reservation.get("Instances", [])
            for instance in instances:
                instance_id = instance.get("InstanceId")
                instance_type = instance.get("InstanceType")
                instance_state = instance.get("State", {}).get("Name")

                # extracting public IP
                public_ip = None
                for interface in instance["NetworkInterfaces"]:
                    # association = interface.get("Association", "no-association")
                    public_ip = interface.get("Association", {}).get("PublicIp")

                # checking for tags, extracting instance name
                name_tag = None
                tags = instance.get("Tags", [])
                for tag in tags:
                    if tag.get("Key") == "Name":
                        name_tag = tag.get("Value")
                        break

                print("_" * 30)
                print(f"| Instance name: {name_tag}")
                print(f"| Instance ID: {instance_id}")
                print(f"| Instance Type: {instance_type}")
                print(f"| Current instance state: {instance_state}")
                if public_ip:
                    print(f"| Public IP: {public_ip}")
                else:
                    print("| this instance not assosiated with a public ip")

                print("-" * 30)

    # errors
    except ClientError as e:
        print(f"client error: {e}")
    except Exception as e:
        print(f"Unexpected error: {str(e)}")
    print("\n")
    print("=" * 30)
