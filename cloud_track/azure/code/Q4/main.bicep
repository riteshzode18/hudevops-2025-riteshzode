// param subscriptionId string = '5bdd4011-32b6-4533-8a15-229a8fe9abd3'
// param resourceGroupName string = 'rkishorzode-resource-group'

param location string = 'EastUS'

var storageAccountName = 'rkishorzodestoragebicep'
var functionAppName = 'rkishorzodefunctionapp'
var containerAName = 'container-a'
var containerBName = 'container-b'

// Create a storage account
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-04-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
  properties: {
    supportsHttpsTrafficOnly: true
  }
}

// Create container A
resource containerA 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/${containerAName}'
  properties: {
    publicAccess: 'None'
  }
}

// Create container B
resource containerB 'Microsoft.Storage/storageAccounts/blobServices/containers@2021-04-01' = {
  name: '${storageAccount.name}/default/${containerBName}'
  properties: {
    publicAccess: 'None'
  }
}

// Create an App Service Plan for the Function App (Y1 = Consumption Plan)
resource functionAppPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: '${functionAppName}-plan'
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
  kind: 'functionapp'
}

// Retrieve the storage account key
var storageAccountKey = listKeys(storageAccount.id, '2021-04-01').keys[0].value

// Deploy the Function App
resource functionApp 'Microsoft.Web/sites@2022-03-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp' // Use 'functionapp' for Windows
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    serverFarmId: functionAppPlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};AccountKey=${storageAccountKey};EndpointSuffix=core.windows.net'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'python'
        }
        {
          name: 'WEBSITE_RUN_FROM_PACKAGE'
          value: '1' // This expects your function code to be uploaded as a ZIP later
        }
      ]
    }
    httpsOnly: true
  }
}
