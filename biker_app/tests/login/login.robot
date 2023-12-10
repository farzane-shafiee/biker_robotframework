*** Settings ***
Resource       ../../resources/login_page/login_page_actions.resource

Suite Setup       start suite
Test Setup        start biker app
Test Teardown     close biker app
Suite Teardown    end suite

*** Test Cases ***
login by valid mobile number
    [Documentation]    Login by valid mobile number is successfully.
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Click On The Continue Button
    Assert Valid Phone Number
    ${otp}                                   get otp
    Enter The Otp Into The Input             ${otp}
    Click On The Confirm Button
    activate app locations
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
    Assert Valid Phone Number
    Enter The Otp Into The Input             ${otp_invalid}
    Click On The Confirm Button
    Assert Invalid Otp

login by Null Otp
    [Documentation]    Login by null OTP and dees not login.
    Enter The Phone Number Into The Input    ${mobile_number_valid}
    Click On The Continue Button
    Assert Valid Phone Number
    Click On The Confirm Button
    Assert Null Otp