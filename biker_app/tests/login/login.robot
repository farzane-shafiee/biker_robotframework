*** Settings ***
Resource       ../../resources/login_page/login_page_actions.resource
Library        ../../resources/login_page/login_keywords_python_library.py

Test Setup        start biker app   ${server_name}    ${platform_name}   ${device_name}   ${app_package}   ${app_activity}  ${android_automation}   ${auto_grant_permissions}


*** Test Cases ***
login by valid phone number
    [Documentation]    Login by valid mobile number is successfully.
    Wait Until Page Contains Element         ${phone_number_input_login}     timeout=5s
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Click On The Continue Button
    ${phone_number}                          Get Phone Number From Text
    ${persian_phone_number}                  Convert Persian Numerals                ${phone_number}
    Validate Phone Number                    ${persian_phone_number}                 ${mobile_number_valid}
    ${token}                                 Get Token                               ${username}    ${mobile_number_valid}
    ${otp}                                   Get Otp                                 ${token}       ${biker_id}
    Enter The Otp Into The Input             ${otp}
    Click On The Confirm Button
    Validate Login

login by wrong phone number  # 09190
    [Documentation]    Login by wrong mobile number and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_wrong}
    Click On The Continue Button
    Validate Wrong Phone Number

login by invalid phone number  # 09150560098
    [Documentation]    Login by invalid mobile number and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_invalid}
    Click On The Continue Button
    Validate Invalid Phone Number

login by null phone number
    [Documentation]    Login by null mobile number and dees not login.
    Click On The Continue Button
    Validate Null Phone Number

login by invalid otp
    [Documentation]    Login by invalid OTP and dees not login.
    Enter The Phone Number Into The Input   ${mobile_number_valid}
    Click On The Continue Button
    ${phone_number}                         Get Phone Number From Text
    ${persian_phone_number}                 Convert Persian Numerals                ${phone_number}
    Should be equal as strings              ${persian_phone_number}                 ${mobile_number_valid}
    Enter The Otp Into The Input            ${otp_invalid}
    Click On The Confirm Button
    Validate Invalid Otp

login by null otp
    [Documentation]    Login by null OTP and dees not login.
    Enter The Phone Number Into The Input   ${mobile_number_valid}
    Click On The Continue Button
    ${phone_number}                         Get Phone Number From Text
    ${persian_phone_number}                 Convert Persian Numerals                ${phone_number}
    Validate Phone Number                   ${persian_phone_number}                 ${mobile_number_valid}
    Click On The Confirm Button
    Validate Null Otp


*** Keywords ***
Validate Phone Number
    [Arguments]                             ${persian_phone_number}                 ${mobile_number_valid}
    Should be equal as strings              ${persian_phone_number}                 ${mobile_number_valid}

Validate Login
    Wait Until Page Contains Element        ${today_income_button_login}

Validate Wrong Phone Number
    Page Should Contain Text                شماره موبایل صحیح وارد نشده است

Validate Invalid Phone Number
    Page Should Contain Text                شماره معتبر نمیباشد.

Validate Null Phone Number
    Page Should Contain Text                شماره موبایل صحیح وارد نشده است

Validate Invalid Otp
    Wait Until Page Contains Element        ${notification_invalid_otp}

Validate Null Otp
    Wait Until Page Contains Element        ${notification_null_otp}
