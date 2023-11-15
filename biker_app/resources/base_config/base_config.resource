*** Settings ***
Library    AppiumLibrary
Variables  base_variables.py

*** Keywords ***
start suite
    [Documentation]   Remote and connect to device_data.
    Log To Console    ************* Start the Suite **************

start biker app
    [Tags]                        start test case
    Open Application    http://localhost:4723/wd/hub
    ...   platformName=${platformName}
    ...   deviceName=${deviceName}
    ...   appPackage=${appPackage}
    ...   appActivity=${appActivity}
    ...   automationName=${android_automation}

close biker app
    Log To Console    ************* End the test **************
    
end suite
    Log To Console    ************* End the suite **************
