*** Settings ***
*** Keywords ***
# get pass and fail statuses and log it in string
Log Statuses
    [Arguments]  ${status}
    ${fail}=  Get From Dictionary  ${status}  fail 
    ${stings}=   String Status  ${fail}
    Log  ${stings}   console=False

    ${pass}=  Get From Dictionary  ${status}  pass
    ${stings}=   String Status  ${pass}
    Log  ${stings}   console=False

# save statuses as json so can view them later
Save Statuses
    [Arguments]  ${status}  ${file_name}
    ${fail}=  Get From Dictionary  ${status}  fail 
    ${json_statuses}=  Json Status  ${fail}  
    Create File    ${file_name}    ${json_statuses} 