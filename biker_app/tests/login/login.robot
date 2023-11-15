*** Settings ***
Resource       ../../resources/login_page/login_page_actions.resource


Suite Setup       start suite
Test Setup        start test case
Test Teardown     end test case
Suite Teardown    end suite

*** Variables ***
*** Test Cases ***

test login valid
    [Documentation]  login valid
    [Tags]           regression

    Insert Phone Number To Input    ${mobile_number_valid}
    Click Continue Button
    Assert Otp Page
    Insert Otp To Input             Get Otp
    Click Confirm Button Login
    Assert Valid Login

test login - wrong mobile number  # 09190
    [Documentation]  login - wrong mobile number
    [Tags]           regression

    Insert Phone Number To Input    ${mobile_number_wrong}
    Click Continue Button
    Assert Wrong Phone Number

test login - invalid mobile number  # 09150560098
    [Documentation]  login - invalid mobile number
    [Tags]           regression

    Insert Phone Number To Input    ${mobile_number_invalid}
    Click Continue Button
    Assert Invalid Phone Number

test login - Null mobile number
    [Documentation]  login - Null mobile number
    [Tags]           regression

    Click Continue Button
    Assert Wrong Phone Number

test login - invalid otp
    [Documentation]  login - invalid OTP
    [Tags]           regression

    Insert Phone Number To Input    ${mobile_number_valid}
    Click Continue Button
    Assert Otp Page
    Insert Otp To Input             ${otp_invalid}
    Click Confirm Button Login
    Assert Invalid Otp

test login - Null Otp
    [Documentation]  login - Null OTP
    [Tags]           regression

    Insert Phone Number To Input    ${mobile_number_valid}
    Click Continue Button
    Assert Otp Page
    Click Confirm Button Login
    Assert Null Otp