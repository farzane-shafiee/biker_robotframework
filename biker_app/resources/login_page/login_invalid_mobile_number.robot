*** Settings ***
Library        AppiumLibrary
Variables      ../../resources/login_page/locators_variables.py

*** Keywords ***
Login - Invalid Mobile Number
    [Arguments]    ${mobile_number_invalid}
    Wait Until Page Contains Element    ${phone_number_input}    timeout=10s
    Click Element                       ${phone_number_input}
    Input Text                          ${phone_number_input}     ${mobile_number_invalid}
    Click Element                       ${continue_button}

    Wait Until Page Contains Element    ${assert_username_invalid}
    Page Should Contain Element         ${assert_username_invalid}
    Page Should Contain Text            شماره معتبر نمیباشد.
