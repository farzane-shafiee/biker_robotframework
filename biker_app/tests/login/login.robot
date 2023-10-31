*** Settings ***
Library        AppiumLibrary
Resource       ../../resources/base_config.robot
Variables      ../../resources/login_page/data_variables.py
Variables      ../../resources/login_page/locators_variables.py
Library        ../../resources/login_page/api_otp.py

Suite Setup       start suite
Test Setup        start test case
Test Teardown     end test case
Suite Teardown    end suite

*** Variables ***
*** Test Cases ***

test search robot
    [Documentation]  login test
    [Tags]           regression

    Wait Until Page Contains Element    ${phone_number_input}    timeout=10s
    Click Element    ${phone_number_input}
    Input Text       ${phone_number_input}     ${phone_number}
    Click Element    ${continue_button}

    Wait Until Page Contains Element    ${otp_page_label}

    ${otp}    Get Otp From Api
    Log To Console   ${otp}
    Input Text       ${otp_input}   ${otp}
    Click Element    ${submit_login_button}

    Wait Until Page Contains Element    ${location_button}
    Click Element    ${location_button}
    Sleep    2s
    Click Element    ${click_fake}
    Click Element    ${click_fake}
    Click Element    ${click_fake}
