*** Settings ***
Library        AppiumLibrary
Variables      ../../resources/login_page/locators_variables.py

*** Keywords ***
Login - Invalid Otp
    [Arguments]    ${mobile_number_valid}    ${otp_invalid}
    Wait Until Page Contains Element    ${phone_number_input}    timeout=10s
    Click Element                       ${phone_number_input}
    Input Text                          ${phone_number_input}     ${mobile_number_valid}
    Click Element                       ${continue_button}

    Wait Until Page Contains Element    ${otp_page_label}

    Input Text                          ${otp_input}   ${otp_invalid}
    Click Element                       ${submit_login_button}

    Wait Until Page Contains Element    ${assert_otp_invalid}
    Page Should Contain Element         ${assert_otp_invalid}