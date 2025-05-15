# AWS VPC Terraform Generator

A Python command-line tool that helps you select AWS regions, list existing VPCs, and generate Terraform configuration files to create new VPCs.

## Features

- Interactive AWS region selection from a set of US regions.
- List all VPCs in the selected region.
- Generate a Terraform `.tf` file with your specified VPC name and CIDR block.
- Handles input errors gracefully with clear messages.

## output

![output](https://github.com/user-attachments/assets/1dbd163a-7b89-434d-9aa3-7e2d32d192fd)
<img src="https://github.com/user-attachments/assets/1dbd163a-7b89-434d-9aa3-7e2d32d192fd" alt="output">

## Getting Started

### Prerequisites

- Python 3.8+
- AWS CLI configured with appropriate credentials
- `boto3` Python package installed

### Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/ezzzizo/python-terraform-generator.git
   cd aws-vpc-terraform-generator
