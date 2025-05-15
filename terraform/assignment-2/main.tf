terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = local.region
}


// create a security group
resource "aws_security_group" "my_sg" {
  name        = "hu-devops-25-rkishorzode-sg"
  description = "Allow SSH and HTTP traffic"
  vpc_id      = local.vpc_id

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

    description = "Allow HTTPs access"
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
  ami                         = local.ami
  instance_type               = local.instance_type
  subnet_id                   = local.subnet_id
  vpc_security_group_ids      = [aws_security_group.my_sg.id]

  tags = {
    Name = "hu-devops-25-rkishorzode-instance"
  }
}