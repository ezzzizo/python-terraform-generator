# AWS Infrastructure Discovery & Terraform Generator


This command-line tool provides a simple and effective way to interact with your AWS account to discover existing infrastructure and generate Terraform configuration files. This tool helps bridge the gap between manually created resources and managing infrastructure as code (IaC).

# Overview

The script allows you to:

1- Select an AWS region.

2- List existing EC2 instances and VPCs for a quick overview of your resources.

3- Create a new vpc.tf file with a provider block and a resource to create a new VPC.

4- Import the configurations of existing VPCs into a Terraform file, making them easier to manage using an Infrastructure as Code approach.

# Features

- Interactive Region Selection: Choose from a list of major AWS regions to target for discovery and generation.
- Resource Discovery: Displays key details for existing EC2 instances and VPCs, including IDs, names, types, and CIDR blocks.
- New VPC Creation: Interactively prompts you to enter a CIDR block and a name to generate an aws_vpc resource block.
- Existing VPC Importing: Creates Terraform resource blocks for VPCs that already exist in your account.
- Modular and Clean Code: The project is designed with clear and well-documented modules, making it easy to understand and extend.

## Project Structure

<pre>
├── main.py                 # Main entry point for the application.
├── utils/
│   ├── __init__.py         # Makes 'utils' a Python package.
│   ├── aws_region.py       # Handles AWS region selection logic.
│   ├── list_ec2.py         # Contains logic for listing EC2 instances.
│   ├── list_vpcs.py        # Contains logic for listing AWS VPCs.
│   ├── tf_newVPC_builder.py  # Builds Terraform config for a new VPC.
│   └── terraform_builder.py  # Builds Terraform config for existing resources.
└── vpc.tf                    # Output file for the generated Terraform code (auto-created).
</pre>         

## Prerequisites

- **Python**: Version 3.8 or higher.
- **Dependencies**:
  - `boto3`: AWS SDK for Python.
  - Terraform: To apply the generated `vpc.tf` file.

## Technologies Used

| <a href="https://aws.amazon.com/"><img src="https://github.com/user-attachments/assets/144360c4-afd9-42e5-a567-931ac06fdf59" width="55" height="60"></a> 
| <a href="https://www.terraform.io/"><img src="https://github.com/user-attachments/assets/11af6368-ed62-4ccc-8bcc-c7ea4bf4e535" alt="Terraform" width="55" height="60"></a> 
| <a href="https://www.python.org/"><img src="https://github.com/user-attachments/assets/ce74e0f0-5497-44f0-9a82-4c5bb87562c8" alt="Python" width="75" height="51"></a> 
| <a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html"><img src="https://github.com/user-attachments/assets/308794da-0ba1-4e6e-b387-af60aafbe098" alt="Boto3" width="55" height="60"></a> |


## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```


3. **Install Dependencies**:
   ```bash
   pip install boto3
   ```

## Usage

1. **Run the Program**:
   ```bash
   python main.py
   ```
   The script will guide you through the following prompts:
   
1-  Select the AWS region you want to work in.

2- The tool will automatically list the existing EC2 instances and VPCs in that region.

3- Choose whether you want to:

- Configure a new VPC: You will be prompted for a CIDR block and a name.

- Configure the fetched VPCs: The tool will create resource blocks for all discovered VPCs.

- Exit.

The resulting Terraform configuration will be saved in a vpc.tf file in the project's root directory.

2. **Example Output**:
<img src="https://github.com/user-attachments/assets/22705478-b57a-495e-ae59-a79468daf7e1" alt="output">

3. **Using the Generated Terraform File**:
   - Ensure Terraform is installed (`terraform` command available).
   - Navigate to the project directory containing `vpc.tf`.
   - Run:
     ```bash
     terraform init
     terraform apply
     ```
   - Review and approve the plan to create the VPC in AWS.     
