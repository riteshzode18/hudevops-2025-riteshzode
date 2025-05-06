# Define variables
$subscriptionId = "5bdd4011-32b6-4533-8a15-229a8fe9abd3"
$resourceGroupName = "rkishorzode-resource-group"
$storageAccountName = "rkishorzodestorageacct"
$containerName = "rkishorzodecontainer"
$csvFileName = "rkishorzode_sub_Vnet.csv"

# # Login to Azure
# az login

# # Set the subscription context
# az account set --subscription $subscriptionId

# Get all virtual networks and their subnets
$vnetList = az network vnet list --subscription $subscriptionId --query "[].{Name:name, Subnets:subnets}" --output json | ConvertFrom-Json

# Prepare data for CSV
$csvData = @()
foreach ($vnet in $vnetList) {
    foreach ($subnet in $vnet.Subnets) {
        $csvData += [PSCustomObject]@{
            VnetName = $vnet.Name
            SubnetName = $subnet.name
            SubnetAddressPrefix = $subnet.addressPrefix
        }
    }
}

# Export data to CSV
$csvData | Export-Csv -Path $csvFileName -NoTypeInformation

# Upload the CSV file to the Azure Blob Storage container
az storage blob upload --account-name $storageAccountName --container-name $containerName --name $csvFileName --file $csvFileName

Write-Host "CSV file '$csvFileName' has been uploaded to container '$containerName' in storage account '$storageAccountName'."
