*** Settings ***
Library        AppiumLibrary
Variables      ../../resources/login_page/locators_variables.py

*** Keywords ***
Login - Null Otp
    [Arguments]    ${mobile_number_valid}
    Wait Until Page Contains Element    ${phone_number_input}    timeout=10s
    Click Element                       ${phone_number_input}
    Input Text                          ${phone_number_input}     ${mobile_number_valid}
    Click Element                       ${continue_button}

    Wait Until Page Contains Element    ${otp_page_label}

    Click Element                       ${submit_login_button}

    Wait Until Page Contains Element    ${assert_null_otp}
    Page Should Contain Element         ${assert_null_otp}