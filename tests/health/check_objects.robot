*** Settings ***
Documentation   Testing if defined k8s objects are in ready state
Resource        resources.robot


*** Test Cases ***
Check Pods
    [Tags]  k8s 
    ${result}=  Get All Pods
    Log Statuses  ${result} 
    Save Statuses    ${result}    failed_pods.json
    Should Be Empty  ${result["fail"]}

Check HelmRelease
    [Tags]  flux
    ${result}=  Get Crs   helm.toolkit.fluxcd.io  v2  helmreleases  flux-system
    Log Statuses  ${result} 
    Save Statuses    ${result}    failed_helmrelease.json
    Should Be Empty  ${result["fail"]}

Check Kustomizations 
    [Tags]  flux
    ${result}=  Get Crs   kustomize.toolkit.fluxcd.io  v1  kustomizations  flux-system
    Log Statuses  ${result} 
    Save Statuses    ${result}    failed_kustomization.json
    Should Be Empty  ${result["fail"]}

Check HelmChart 
    [Tags]  flux
    ${result}=  Get Crs   source.toolkit.fluxcd.io  v1  helmcharts  flux-system
    Log Statuses  ${result} 
    Save Statuses    ${result}    failed_helmchart.json
    Should Be Empty  ${result["fail"]}
    
Check GitRepos 
    [Tags]  flux
    ${result}=  Get Crs   source.toolkit.fluxcd.io  v1  gitrepositories  flux-system
    Log Statuses  ${result} 
    Save Statuses    ${result}    failed_gitrepo.json
    Should Be Empty  ${result["fail"]}
    
Check OciRepos 
    [Tags]  flux
    ${result}=  Get Crs   source.toolkit.fluxcd.io  v1beta2  ocirepositories  flux-system
    Log Statuses  ${result} 
    Save Statuses    ${result}    failed_ocirepo.json
    Should Be Empty  ${result["fail"]}