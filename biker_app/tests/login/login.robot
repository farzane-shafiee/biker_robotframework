*** Settings ***
Resource       ../../resources/login_page/login_page_actions.resource

Suite Setup       start suite
Test Setup        start biker app
Test Teardown     close biker app
Suite Teardown    end suite

*** Test Cases ***

login by valid mobile number
    Insert Phone Number To Input    ${mobile_number_valid}
    Click Continue Button
    Assert Otp Page
    Insert Otp To Input             Set Otp From Api
    Click Confirm Button Login
    Assert Valid Login

login by wrong mobile number  # 09190
    Insert Phone Number To Input    ${mobile_number_wrong}
    Click Continue Button
    Assert Wrong Phone Number

login by invalid mobile number  # 09150560098
    Insert Phone Number To Input    ${mobile_number_invalid}
    Click Continue Button
    Assert Invalid Phone Number

login by Null mobile number
    Click Continue Button
    Assert Wrong Phone Number

login by invalid otp
    Insert Phone Number To Input    ${mobile_number_valid}
    Click Continue Button
    Assert Otp Page
    Insert Otp To Input             ${otp_invalid}
    Click Confirm Button Login
    Assert Invalid Otp

login by Null Otp
    Insert Phone Number To Input    ${mobile_number_valid}
    Click Continue Button
    Assert Otp Page
    Click Confirm Button Login
    Assert Null Otp