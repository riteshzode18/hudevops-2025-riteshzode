#!/bin/bash

location="EastUS"
resourceGroup="hu-devops-25-rkishorzode-rg-$(date +%s)"
tag="deploy-github.sh"
gitrepo=https://github.com/riteshzode18/python-docs-hello-world
appServicePlan="rkishorzode-app-service-plan"
webapp="rkishorzode-web-app"

echo "Creating $resourceGroup in $location..."
az group create --name $resourceGroup --location "$location" --tag $tag

echo "Creating $appServicePlan"
az appservice plan create --name $appServicePlan --resource-group $resourceGroup --sku FREE --is-linux

echo "Creating $webapp"
az webapp create --name $webapp --resource-group $resourceGroup --plan $appServicePlan --runtime "PYTHON:3.10"

az webapp deployment source config --name $webapp --resource-group $resourceGroup --repo-url $gitrepo --branch main --manual-integration

site="http://$webapp.azurewebsites.net"
echo $site
curl "$site"


# az group delete --name hu-devops-25-rkishorzode-rg -y

