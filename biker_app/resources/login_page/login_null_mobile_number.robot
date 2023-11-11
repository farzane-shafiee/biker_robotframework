*** Settings ***
Library        AppiumLibrary
Variables      ../../resources/login_page/locators_variables.py

*** Keywords ***
Login - Null Mobile Number
    Wait Until Page Contains Element    ${phone_number_input}    timeout=10s
    Click Element                       ${continue_button}

    Wait Until Page Contains Element    ${assert_username_invalid}
    Page Should Contain Element         ${assert_username_invalid}
    Page Should Contain Text            شماره موبایل صحیح وارد نشده است