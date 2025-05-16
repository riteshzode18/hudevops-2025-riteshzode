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


resource "aws_iam_policy" "aws-s3-ec2-policy-1" {
  name        = "aws-s3-ec2-policy-1"
  description = "My test policy"

  policy = <<EOT
    {
    "Version": "2012-10-17",
    "Statement": [
        {
        "Action": [
            "s3:ListAllMyBuckets",
            "ec2:DescribeInstances"
        ],
        "Effect": "Allow",
        "Resource": "*"
        }
    ]

    }
    EOT
}   

resource "aws_iam_policy" "aws-s3-ec2-policy-2" {
  name = "aws-s3-ec2-policy-2"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action   = ["s3:ListAllMyBuckets", "ec2:DescribeInstances"]
        Effect   = "Allow"
        Resource = "*"
      },
    ]
  })
}

// create a sample role and attach policy
resource "aws_iam_role" "aws-s3-ec2-role" {
  name = "aws-s3-ec2-role"
  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Principal = {
          Service = "ec2.amazonaws.com"
        }
        Action = "sts:AssumeRole"
      },
    ]
  })
    tags = {
        Name = "hu-devops-25-rkishorzode"
    }
}
resource "aws_iam_role_policy_attachment" "role_one_policy_attachment" {
  role       = aws_iam_role.aws-s3-ec2-role.name
  policy_arn = aws_iam_policy.aws-s3-ec2-policy-1.arn
}
# resource "aws_iam_role_policy_attachment" "role_one_policy_attachment-2" {
#   role       = aws_iam_role.aws-s3-ec2-role.name
#   policy_arn = aws_iam_policy.aws-s3-ec2-policy-2.arn
# }