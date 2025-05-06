from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.web import WebSiteManagementClient
import os

# Set your Azure subscription ID
subscription_id = '5bdd4011-32b6-4533-8a15-229a8fe9abd3'

# Set the tag to filter resources
tag_key = "Key1"
tag_value = "Value1"

# Initialize clients
credential = DefaultAzureCredential()
resource_client = ResourceManagementClient(credential, subscription_id)
storage_client = StorageManagementClient(credential, subscription_id)
web_client = WebSiteManagementClient(credential, subscription_id)

# Function to list and delete resources based on tags
def list_and_delete_resources_by_tag():
    # List all resources in the subscription
    resources = resource_client.resources.list()

    # Iterate over resources to find those with the specified tag
    for resource in resources:
        # Check if the resource has the specified tag
        if resource.tags and resource.tags.get(tag_key) == tag_value:
            resource_id = resource.id
            resource_type = resource.type
            resource_name = resource.name
            resource_group = resource.id.split('/')[4]  # Extract resource group from resource ID

            # Print resource details
            print(f"Found resource: {resource_name} of type {resource_type} in resource group {resource_group}")

            # Delete the resource based on its type
            if resource_type.startswith("Microsoft.Storage/storageAccounts"):
                # Delete storage account
                print(f"Deleting storage account: {resource_name}")
                storage_client.storage_accounts.delete(resource_group, resource_name)
            elif resource_type.startswith("Microsoft.Web/sites"):
                # Delete web app
                print(f"Deleting web app: {resource_name}")
                web_client.web_apps.delete(resource_group, resource_name)
            elif resource_type.startswith("Microsoft.Web/serverfarms"):
                # Delete app service plan
                print(f"Deleting app service plan: {resource_name}")
                web_client.app_service_plans.delete(resource_group, resource_name)
            else:
                # Delete other resources
                print(f"Deleting resource: {resource_name}")
                resource_client.resources.begin_delete_by_id(resource_id, api_version="2021-04-01")

# Execute the function
list_and_delete_resources_by_tag()

print("Deletion process completed for resources with specified tags.")
