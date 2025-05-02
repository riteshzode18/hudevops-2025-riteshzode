from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient 
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Access the environment variable
subscription_id = os.getenv('SUBSCRIPTION_ID')
# Initialize the StorageManagementClient with DefaultAzureCredential
credential = DefaultAzureCredential()
storage_client = StorageManagementClient(credential, subscription_id)
# Define the parameters for the storage account
resource_group_name = 'HU-DevOps-25-rkishorzode-rg'
storage_account_name = 'hudevops25rkishorzodesa'
location = 'eastus'
# Create the storage account
async_storage_account_creation = storage_client.storage_accounts.begin_create(
 resource_group_name,
 storage_account_name,
 {
 "location": location,
 "sku": {"name": "Standard_LRS"},
 "kind": "StorageV2",
 "properties": {}
 }
)

# Wait for the storage account creation to complete
storage_account = async_storage_account_creation.result()
print(f'Storage account {storage_account.name} created successfully.')

# in storage account create container
blob_service_client = BlobServiceClient(
    account_url=f"https://{storage_account_name}.blob.core.windows.net",
    credential=credential
)
container_name = 'hu-devops-25-rkishorzode-container-by-cli'
container_client = blob_service_client.create_container(container_name)
print(f'Container {container_name} created successfully in storage account {storage_account_name}.')


