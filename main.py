"""Main module"""

from utils.list_vpcs import vpcs_list
from utils.aws_region import region_selector
from utils.terraform_builder import vpc_tf_generator


def main():
    """Main function to:
    1. Prompt user to select an AWS region.
    2. List existing VPCs in that region.
    3. Generate a Terraform file to create a new VPC in the selected region.
    """
    # selecting region
    print()
    region: str = region_selector()

    # listing vpcs
    vpcs_list(region)

    # generating a terraform file to create a new vpc
    vpc_tf_generator(region)


if __name__ == "__main__":
    main()
