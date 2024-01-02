*** Settings ***
Variables      locators_variables.py
Variables      data_variables.py
Resource       ../base_config/base_config.resource
Library        ${CURDIR}/login_keywords_python_library.py

*** Keywords ***
enter the phone number into the input
    [Arguments]    ${phone_number}
    Wait Until Page Contains Element    ${phone_number_input_login}     timeout=10s
    Input Text                          ${phone_number_input_login}     ${phone_number}
    Wait Until Page Contains Element    ${cross_button_login}

click on the continue button
    Click Element                       ${continue_button_login}

assert valid phone number
    Wait Until Page Contains Element    ${phone_number_label_login}
    ${text_locator}                    Get Text                   ${phone_number_label_login}
    ${phone_number}                     Get Part Of Text          ${text_locator}
    Should be equal as strings          ${phone_number}           ${mobile_number_valid}

get token
    ${token}                            Get Token From Api
    RETURN                              ${token}

get otp
    [Arguments]                         ${token}
    ${otp}                              Get Otp From Api          ${token}
    RETURN                              ${otp}

enter the otp into the input
    [Arguments]    ${otp}
    Input Text                          ${otp_input_login}        ${otp}

click on the confirm button
    Click Element                       ${confirm_button_login}

assert valid login
    Wait Until Page Contains Element    ${today_income_button_login}
    Page Should Contain Element         ${today_income_button_login}

assert wrong phone number
    Wait Until Page Contains Element    ${notification_invalid_phone_numner}
    Page Should Contain Element         ${notification_invalid_phone_numner}
    Page Should Contain Text            شماره موبایل صحیح وارد نشده است

assert invalid phone number
    Wait Until Page Contains Element    ${notification_invalid_phone_numner}
    Page Should Contain Element         ${notification_invalid_phone_numner}
    Page Should Contain Text            شماره معتبر نمیباشد.

assert invalid otp
    Wait Until Page Contains Element    ${notification_invalid_otp}
    Page Should Contain Element         ${notification_invalid_otp}

assert null otp
    Wait Until Page Contains Element    ${notification_null_otp}
    Page Should Contain Element         ${notification_null_otp}