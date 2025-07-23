provider "aws" {
  region = "us-east-1"
}




# VPC ID used to import and link the existing AWS resource to this Terraform resource block: vpc-07340bbc5325a6ddf
resource "aws_vpc" "test" {
  cidr_block = "10.0.6.0/24"

  tags = {
    Name = "test"
  }
}





resource "aws_vpc" "main-vpc" {
  cidr_block = "10.0.3.0/16"

  tags = {
    Name = "main-vpc"
  }
}

resource "aws_vpc" "0" {
  cidr_block = "10"

  tags = {
    Name = "0"
  }
}

resource "aws_vpc" "main-server-vpc" {
  cidr_block = "10.0.0.2/24"

  tags = {
    Name = "main-server-vpc"
  }
}

# VPC ID used to import and link the existing AWS resource to this Terraform resource block: vpc-0880598be906c4cb8
resource "aws_vpc" "UnnamedVPC" {
  cidr_block = "172.31.0.0/16"

  tags = {
    Name = "UnnamedVPC"
  }
} 
 

