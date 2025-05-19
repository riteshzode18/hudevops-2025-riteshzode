remote_state {
  backend = "s3"
  config = {
    bucket         = "hu-devops-25-rkishorzode-remote-state"
    region         = "us-east-1"
    encrypt        = true
  }
}