provider "aws" {
  region = "us-east-1"
}
resource "aws_vpc" "gen_vpc" {
  cidr_block = "10.0.0.0/28"

  tags = {
    Name = "gen_vpc"
  }
}
