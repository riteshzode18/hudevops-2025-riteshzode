from azure.identity import DefaultAzureCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.web import WebSiteManagementClient
from azure.core.exceptions import HttpResponseError

# Define your variables
subscription_id = '5bdd4011-32b6-4533-8a15-229a8fe9abd3'  # Replace with your Azure subscription ID
resource_group_name = 'rkishorzode-resource-group'
location = 'EastUS'
app_service_plan_name = 'rkishorzode-app-service-plan'
web_app_name = 'rkishorzode-web-app'  # Must be globally unique
git_repo_url = 'https://github.com/riteshzode18/python-docs-hello-world'

# Authenticate using DefaultAzureCredential
credential = DefaultAzureCredential()

# Initialize clients
resource_client = ResourceManagementClient(credential, subscription_id)
web_client = WebSiteManagementClient(credential, subscription_id)

try:
    # Create a resource group
    print(f"Creating resource group '{resource_group_name}' in '{location}'...")
    resource_client.resource_groups.create_or_update(
        resource_group_name,
        {'location': location}
    )

    # Create an App Service plan
    print(f"Creating App Service plan '{app_service_plan_name}'...")
    web_client.app_service_plans.begin_create_or_update(
        resource_group_name,
        app_service_plan_name,
        {
            'location': location,
            'sku': {'name': 'F1', 'tier': 'Free'},
            'reserved': True  # Indicates Linux
        }
    ).result()

    # Create a web app
    print(f"Creating web app '{web_app_name}'...")
    web_client.web_apps.begin_create_or_update(
        resource_group_name,
        web_app_name,
        {
            'location': location,
            'server_farm_id': app_service_plan_name,
            'site_config': {
                'linux_fx_version': 'PYTHON|3.10'
            }
        }
    ).result()

    # Configure deployment from GitHub
    print(f"Configuring deployment from GitHub repository '{git_repo_url}'...")
    web_client.web_apps.begin_create_or_update_source_control(
        resource_group_name,
        web_app_name,
        {
            'repo_url': git_repo_url,
            'branch': 'main',
            'is_manual_integration': True
        }
    ).result()

    print(f"Web app URL: http://{web_app_name}.azurewebsites.net")

except HttpResponseError as e:
    print(f"An error occurred: {e.message}")
