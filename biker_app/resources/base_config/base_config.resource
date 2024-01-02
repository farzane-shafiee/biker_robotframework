*** Settings ***
Library    AppiumLibrary
Variables  base_variables.py

*** Keywords ***
start biker app
    [Tags]              start test case
    [Arguments]         ${server_name}    ${platform_name}   ${device_name}   ${app_package}   ${app_activity}  ${android_automation}   ${auto_grant_permissions}
    Open Application    http://${server_name}:4723/wd/hub
    ...   platformName=${platform_name}
    ...   deviceName=${device_name}
    ...   appPackage=${app_package}
    ...   appActivity=${app_activity}
    ...   automationName=${android_automation}
    ...   autoGrantPermissions=${auto_grant_permissions}