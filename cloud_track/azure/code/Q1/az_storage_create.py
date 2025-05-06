from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.storage.blob import BlobServiceClient
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your Azure subscription ID and other parameters
# subscription_id = os.getenv('SUBSCRIPTION_ID')  # Loaded from environment variable
subscription_id = '5bdd4011-32b6-4533-8a15-229a8fe9abd3'
resource_group = 'rkishorzode-resource-group'
location = 'EastUS'
storage_account_name = 'rkishorzodestorageacct'
container_name = 'rkishorzodecontainer'

# Set up your Azure credentials
credential = DefaultAzureCredential()

# Initialize the Storage Management Client
storage_client = StorageManagementClient(credential, subscription_id)

# Create a storage account
async_storage_account_creation = storage_client.storage_accounts.begin_create(
    resource_group,
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
print(f"Storage account '{storage_account_name}' created successfully.")

# Initialize the Blob Service Client using DefaultAzureCredential
blob_service_client = BlobServiceClient(
    account_url=f"https://{storage_account_name}.blob.core.windows.net",
    credential=credential
)

# Create a container
container_client = blob_service_client.create_container(container_name)
print(f"Container '{container_name}' created successfully in storage account '{storage_account_name}'.")
