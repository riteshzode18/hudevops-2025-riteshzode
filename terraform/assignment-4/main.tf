terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 2.46.0"
    }
  }
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "hu-devops-25-rkishorzode-rg-1"
  location = "East US"
}

# Storage Account
resource "azurerm_storage_account" "storage" {
  name                     = "rkishorzodecdnstoragesg" 
  resource_group_name      = azurerm_resource_group.rg.name
  location                 = azurerm_resource_group.rg.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
  allow_blob_public_access = false
  static_website {
    index_document = "index.html"
  }
}

resource "azurerm_storage_blob" "example" {
  name                   = "index.html"
  storage_account_name   = azurerm_storage_account.storage.name
  storage_container_name = "$web"
  type                   = "Block"
  content_type           = "text/html"
  source                 = "index.html"
}

# Storage Container for blobs
resource "azurerm_storage_container" "static_content" {
  name                  = "static-content"
  storage_account_name  = azurerm_storage_account.storage.name
  container_access_type = "blob"

}

# Upload HTML file to Blob Storage
resource "azurerm_storage_blob" "html_page" {
  name                   = "index.html"
  storage_account_name   = azurerm_storage_account.storage.name
  storage_container_name = azurerm_storage_container.static_content.name
  type                   = "Block"
  source                 = "index.html"  
  content_type           = "text/html"
}

# CDN Profile
resource "azurerm_cdn_profile" "cdn" {
  name                = "rkishorzodecdnprofile"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  sku                 = "Standard_Microsoft"
}

# # CDN Endpoint
# resource "azurerm_cdn_endpoint" "cdn_endpoint" {
#   name                = "rkishorzodecdnendpoint"
#   resource_group_name = azurerm_resource_group.rg.name
#   profile_name        = azurerm_cdn_profile.cdn.name
#   location            = azurerm_resource_group.rg.location
#   origin {
#     name      = azurerm_storage_account.storage.primary_blob_endpoint
#     host_name = azurerm_storage_account.storage.primary_blob_endpoint
#   }
#   is_https_allowed = true
# }

# error related to domain name