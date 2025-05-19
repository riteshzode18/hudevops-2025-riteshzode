terraform {
  source = "../../modules/s3"
}

inputs = {
  region       = "us-east-1"
  bucket_name  = "hu-devops-25-rkishorzode-prod-bucket"
  name         = "Prod Bucket"
  environment  = "Prod"
}