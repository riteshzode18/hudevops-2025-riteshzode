provider "google" {
  project = "us-gcp-ame-con-1878b-sbx-1"
  region  = "us-central1"
}

# Create a Google Container Registry
resource "google_container_registry" "gcr" {
  project = "us-gcp-ame-con-1878b-sbx-1"
}


# create google cloud run service
resource "google_cloud_run_service" "my-service" {
  name     = "my-app"
  location = "us-central1"
  project = "us-gcp-ame-con-1878b-sbx-1"

  template {
    spec {
      containers {
        image = "gcr.io/us-gcp-ame-con-1878b-sbx-1/nginx:latest"
      }
    }
  }
}
 

