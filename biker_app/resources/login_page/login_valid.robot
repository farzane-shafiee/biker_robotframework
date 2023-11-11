*** Settings ***
Library        AppiumLibrary
Variables      ../../resources/login_page/locators_variables.py
Library        ../../resources/login_page/login_api.py

*** Keywords ***
Login Valid
    [Arguments]    ${mobile_number_valid}
    Wait Until Page Contains Element        ${phone_number_input}     timeout=10s
        Click Element                       ${phone_number_input}
        Input Text                          ${phone_number_input}     ${mobile_number_valid}
        Click Element                       ${continue_button}

        Wait Until Page Contains Element    ${otp_page_label}

        ${token}    Get Token
        ${otp}    Get Otp From Api          ${token}
        Input Text                          ${otp_input}   ${otp}
        Click Element                       ${submit_login_button}

        Wait Until Page Contains Element    ${location_button}
        Click Element                       ${location_button}
        Sleep    1s
        Click Element                       ${location_button2}
        Sleep    2s
        Click Element                       ${click_fake}
        Click Element                       ${click_fake}
        Click Element                       ${click_fake}

        Wait Until Page Contains Element    ${assert_login_valid}
        Page Should Contain Element         ${assert_login_valid}