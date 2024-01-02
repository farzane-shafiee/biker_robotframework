*** Settings ***
Resource       ../../resources/login_page/login_page_actions.resource

Test Setup        start biker app   ${server_name}    ${platform_name}   ${device_name}   ${app_package}   ${app_activity}  ${android_automation}   ${auto_grant_permissions}

*** Test Cases ***
login by valid mobile number
    [Documentation]    Login by valid mobile number is successfully.
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Click On The Continue Button

    Wait Until Page Contains Element         ${phone_number_label_login}
    ${phone_number}                          Get Phone Number From Text
    ${persian_phone_number}                  Convert Persian Numerals                ${phone_number}
    Should be equal as strings               ${persian_phone_number}                 ${mobile_number_valid}
    ${token}                                 Get Token From Api       ${username}    ${mobile_number_valid}
    ${otp}                                   get otp                  ${token}       ${biker_id}
    Enter The Otp Into The Input             ${otp}
    Click On The Confirm Button
    Assert Valid Login

login by wrong mobile number  # 09190
    [Documentation]    Login by wrong mobile number and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_wrong}
    Click On The Continue Button
    Assert Wrong Phone Number

login by invalid mobile number  # 09150560098
    [Documentation]    Login by invalid mobile number and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_invalid}
    Click On The Continue Button
    Assert Invalid Phone Number

login by Null mobile number
    [Documentation]    Login by null mobile number and dees not login.
    Click On The Continue Button
    Assert Wrong Phone Number

login by invalid otp
    [Documentation]    Login by invalid OTP and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Click On The Continue Button
    Wait Until Page Contains Element         ${phone_number_label_login}
    ${phone_number}                          Get Phone Number From Text
    ${persian_phone_number}                  Convert Persian Numerals                ${phone_number}
    Should be equal as strings               ${persian_phone_number}                 ${mobile_number_valid}
    Enter The Otp Into The Input             ${otp_invalid}
    Click On The Confirm Button
    Assert Invalid Otp

login by Null Otp
    [Documentation]    Login by null OTP and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Click On The Continue Button
    Wait Until Page Contains Element         ${phone_number_label_login}
    ${phone_number}                          Get Phone Number From Text
    ${persian_phone_number}                  Convert Persian Numerals                ${phone_number}
    Should be equal as strings               ${persian_phone_number}                 ${mobile_number_valid}
    Click On The Confirm Button
    Assert Null Otp