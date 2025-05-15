terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}


// create a security group
resource "aws_security_group" "my_sg" {
  name        = "hu-devops-25-rkishorzode-sg"
  description = "Allow SSH, HTTP and HTTPS traffic"
  vpc_id      = "vpc-040e583668e43adf1"

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["24.239.142.70/32"]

    description = "Allow SSH access"
  }
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["24.239.142.70/32"]

    description = "Allow HTTP access"
  }
  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["24.239.142.70/32"]

    description = "Allow HTTPS access"
  }
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]

    description = "Allow all outbound traffic"
  }
}


// Create an EC2 Instance with a Security Group
resource "aws_instance" "my_instance" {
  ami                         = "ami-0953476d60561c955"
  instance_type               = "t2.micro"
  subnet_id                   = "subnet-011d5547f67a9e312"
  vpc_security_group_ids      = [aws_security_group.my_sg.id]

  tags = {
    Name = "hu-devops-25-rkishorzode-instance"
  }
}