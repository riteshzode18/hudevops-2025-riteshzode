terraform {
  source = "../../modules/s3"
}

inputs = {
  region       = "us-east-1"
  bucket_name  = "hu-devops-25-rkishorzode-dev-bucket"
  name         = "Dev Bucket"
  environment  = "Dev"
}