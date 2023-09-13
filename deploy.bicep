param appName string = 'my-kiosk-app'
param containerRegistryName string = 'mykioskappacr'
param containerImage string = 'mykioskapp:latest'



resource appServicePlan 'Microsoft.Web/serverfarms@2021-02-01' = {
  name: '${appName}-plan'
  location: resourceGroup().location
  sku: {
    name: 'F1'
    tier: 'Free'
  }
}

resource webApp 'Microsoft.Web/sites@2021-02-01' = {
  name: appName
  location: resourceGroup().location
  properties: {
    serverFarmId: appServicePlan.id
  }
  dependsOn: [
    appServicePlan
  ]
}

resource containerRegistry 'Microsoft.ContainerRegistry/registries@2021-06-01-preview' = {
  name: containerRegistryName
  location: resourceGroup().location
  sku: {
    name: 'Standard'
  }
}

resource containerDeployment 'Microsoft.Web/sites/config@2021-02-01' = {
  name: '${webApp.name}/config'
  parent: webApp
  properties: {
    appCommandLine: ''
    linuxFxVersion: 'DOCKER|${containerRegistry.properties.loginServer}/${containerImage}'
    scmType: 'None'
  }
  dependsOn: [
    webApp
  ]
}
