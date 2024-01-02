*** Settings ***
Library        String
Variables      locators_variables.py
Variables      data_variables.py
Variables      ../base_config/base_variables
Resource       ../base_config/base_config.resource
Library        ${CURDIR}/login_keywords_python_library.py

*** Keywords ***
enter the phone number into the input
    [Arguments]    ${phone_number}
    Wait Until Page Contains Element    ${phone_number_input_login}     timeout=5s
    Input Text                          ${phone_number_input_login}     ${phone_number}
    Wait Until Page Contains Element    ${cross_button_login}

click on the continue button
    Click Element                       ${continue_button_login}

Convert Persian Numerals
    [Arguments]                         ${persian_text}
    ${converted_text}=    Evaluate      "${persian_text}".replace('۰', '0').replace('۱', '1').replace('۲', '2').replace('۳', '3').replace('۴', '4').replace('۵', '5').replace('۶', '6').replace('۷', '7').replace('۸', '8').replace('۹', '9')
    RETURN                              ${converted_text}

Get Phone Number From Text
    ${text_locator}     Get Text        ${phone_number_label_login}
    ${phone_number}     Get Substring   ${text_locator}     27      38
    RETURN                              ${phone_number}

Get Token From Api
    [Arguments]                         ${username}    ${password}
    ${token}                            Get Token      ${username}    ${password}
    RETURN                              ${token}

get otp
    [Arguments]                         ${token}                        ${biker_id}
    ${otp}                              Get Otp From Api                ${token}      ${biker_id}
    RETURN                              ${otp}

enter the otp into the input
    [Arguments]    ${otp}
    Input Text                          ${otp_input_login}              ${otp}

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