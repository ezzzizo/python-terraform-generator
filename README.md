# AWS VPC Terraform Generator


This Python project provides a command-line utility to:
1. Select an AWS region from a predefined list.
2. List all Virtual Private Clouds (VPCs) in the selected region using the AWS EC2 API.
3. Generate a Terraform configuration file (`vpc.tf`) to create a new VPC in the selected region.


## Prerequisites

- **Python**: Version 3.8 or higher.
- **Dependencies**:
  - `boto3`: AWS SDK for Python.
  - Terraform: To apply the generated `vpc.tf` file.

## Technologies Used

| [![AWS](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/supported/aws_vector.svg)](https://aws.amazon.com/) | [![Terraform](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/supported/terraform_vector.svg)](https://www.terraform.io/) | [![Python](https://cdn.jsdelivr.net/npm/@intergrav/devins-badges@3/assets/cozy/supported/python_vector.svg)](https://www.python.org/) | [![Boto3](https://raw.githubusercontent.com/boto/boto3/master/docs/source/_static/images/boto3-logo.png)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) |
|-------|-------|-------|-------|


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

2. **Example Output**:
   ```
<img src="https://github.com/user-attachments/assets/1dbd163a-7b89-434d-9aa3-7e2d32d192fd" alt="output">

3. **Using the Generated Terraform File**:
   - Ensure Terraform is installed (`terraform` command available).
   - Navigate to the project directory containing `vpc.tf`.
   - Run:
     ```bash
     terraform init
     terraform apply
     ```
   - Review and approve the plan to create the VPC in AWS.

## Project Structure

- **`main.py`**: Entry point that orchestrates region selection, VPC listing, and Terraform file generation.
- **`utils/aws_region.py`**: Handles AWS region selection with input validation.
- **`utils/list_vpcs.py`**: Lists all VPCs in a specified region using `boto3`.
- **`utils/terraform_builder.py`**: Generates a Terraform configuration file for a new VPC.
- **`vpc.tf`** (generated): Terraform file created after running the program, containing the VPC configuration.
