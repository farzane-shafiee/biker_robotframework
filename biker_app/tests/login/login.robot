*** Settings ***
Resource       ../../resources/login_page/login_page_actions.resource

Test Setup        start biker app   ${server_name}    ${platform_name}   ${device_name}   ${app_package}   ${app_activity}  ${android_automation}   ${auto_grant_permissions}
Library    ../../resources/login_page/login_keywords_python_library.py

*** Test Cases ***
login by valid mobile number
    [Documentation]    Login by valid mobile number is successfully.
    Wait Until Page Contains Element         ${phone_number_input_login}     timeout=5s
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Wait Until Page Contains Element         ${cross_button_login}
    Click On The Continue Button

    Wait Until Page Contains Element         ${phone_number_label_login}
    ${phone_number}                          Get Phone Number From Text
    ${persian_phone_number}                  Convert Persian Numerals                ${phone_number}
    Should be equal as strings               ${persian_phone_number}                 ${mobile_number_valid}
    ${token}                                 Get Token                               ${username}    ${mobile_number_valid}
    ${otp}                                   Get Otp                                 ${token}       ${biker_id}
    Enter The Otp Into The Input             ${otp}
    Click On The Confirm Button

    Wait Until Page Contains Element         ${today_income_button_login}
    Page Should Contain Element              ${today_income_button_login}

login by wrong mobile number  # 09190
    [Documentation]    Login by wrong mobile number and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_wrong}
    Click On The Continue Button

    Wait Until Page Contains Element         ${notification_invalid_phone_numner}
    Page Should Contain Element              ${notification_invalid_phone_numner}
    Page Should Contain Text                 شماره موبایل صحیح وارد نشده است

login by invalid mobile number  # 09150560098
    [Documentation]    Login by invalid mobile number and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_invalid}
    Click On The Continue Button

    Wait Until Page Contains Element         ${notification_invalid_phone_numner}
    Page Should Contain Element              ${notification_invalid_phone_numner}
    Page Should Contain Text                 شماره معتبر نمیباشد.

login by Null mobile number
    [Documentation]    Login by null mobile number and dees not login.
    Click On The Continue Button
    Wait Until Page Contains Element        ${notification_invalid_phone_numner}
    Page Should Contain Element             ${notification_invalid_phone_numner}
    Page Should Contain Text                شماره موبایل صحیح وارد نشده است

login by invalid otp
    [Documentation]    Login by invalid OTP and dees not login.
    Enter The Phone Number Into The Input   ${mobile_number_valid}
    Click On The Continue Button
    Wait Until Page Contains Element        ${phone_number_label_login}
    ${phone_number}                         Get Phone Number From Text
    ${persian_phone_number}                 Convert Persian Numerals                ${phone_number}
    Should be equal as strings              ${persian_phone_number}                 ${mobile_number_valid}
    Enter The Otp Into The Input            ${otp_invalid}
    Click On The Confirm Button
    Wait Until Page Contains Element        ${notification_invalid_otp}
    Page Should Contain Element             ${notification_invalid_otp}

login by Null Otp
    [Documentation]    Login by null OTP and dees not login.
    Enter The Phone Number Into The Input   ${mobile_number_valid}
    Click On The Continue Button
    Wait Until Page Contains Element        ${phone_number_label_login}
    ${phone_number}                         Get Phone Number From Text
    ${persian_phone_number}                 Convert Persian Numerals                ${phone_number}
    Should be equal as strings              ${persian_phone_number}                 ${mobile_number_valid}
    Click On The Confirm Button
    Wait Until Page Contains Element        ${notification_null_otp}
    Page Should Contain Element             ${notification_null_otp}