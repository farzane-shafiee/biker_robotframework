*** Settings ***
Library    AppiumLibrary
Library    Collections
Variables  base_variables.py
#Variables  data_device.yaml

*** Variables ***

*** Keywords ***
start suite
    [Documentation]   Remote and connect to device_data.
    Log To Console    ************* Start the Suite **************

start test case
    [Tags]                        start test case
    Open Application    http://localhost:4723/wd/hub
    ...   platformName=${platformName}
    ...   deviceName=${deviceName}
    ...   appPackage=${appPackage}
    ...   appActivity=${appActivity}
    ...   automationName=${android_automation}

end test case
    Log To Console    ************* End the test **************

end suite
    Log To Console    ************* End the suite **************
