*** Settings ***
Documentation   Testing if defined k8s objects are in ready state
Resource        resources.robot



*** Test Cases ***
Check Pods
    ${result}=  Get All Pods
    Log to console  len(${result["fail"]})
    Should Be Empty  ${result["fail"]}