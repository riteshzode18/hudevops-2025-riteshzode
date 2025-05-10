from azure.identity import DefaultAzureCredential
from azure.mgmt.containerinstance import ContainerInstanceManagementClient
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import ResourceGroup

# Set your Azure subscription ID and other parameters
subscription_id = '5bdd4011-32b6-4533-8a15-229a8fe9abd3'
resource_group = 'rkishorzode-resource-group'
location = 'EastUS'
container_app_env = 'HU-DevOps-25-CAE'
container_app_name = 'rkishorzode-container-app'

# Set up your Azure credentials
credential = DefaultAzureCredential()

# Initialize the Resource Management Client
resource_client = ResourceManagementClient(credential, subscription_id)

# Create a resource group
resource_group_params = {'location': location}
resource_client.resource_groups.create_or_update(resource_group, resource_group_params)

# Initialize the Container Instance Management Client
container_client = ContainerInstanceManagementClient(credential, subscription_id)

# Define the container group with public IP
container_group = {
    'location': location,
    'containers': [
        {
            'name': container_app_name,
            'image': 'mcr.microsoft.com/azuredocs/aci-helloworld',
            'resources': {
                'requests': {
                    'cpu': 1,
                    'memory_in_gb': 1.5
                }
            },
            'ports': [
                {
                    'port': 80
                }
            ]
        }
    ],
    'os_type': 'Linux',
    'ip_address': {
        'type': 'Public',
        'ports': [
            {
                'protocol': 'tcp',
                'port': 80
            }
        ],
        'dns_name_label': container_app_name.lower()  # Ensure the DNS name label is unique
    }
}

# Create the container group
container_client.container_groups.begin_create_or_update(resource_group, container_app_name, container_group)

print(f"Container group '{container_app_name}' created successfully in resource group '{resource_group}' with a public IP.")
