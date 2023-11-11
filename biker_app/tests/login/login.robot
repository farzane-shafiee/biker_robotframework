*** Settings ***
Library        AppiumLibrary
Resource       ../../resources/base_config/base_config.robot
Variables      ../../resources/login_page/data_variables.py
Resource       ../../resources/login_page/login_valid.robot
Resource       ../../resources/login_page/login_wrong_mobile_number.robot
Resource       ../../resources/login_page/login_invalid_mobile_number.robot
Resource       ../../resources/login_page/login_null_mobile_number.robot
Resource       ../../resources/login_page/login_invalid_otp.robot
Resource       ../../resources/login_page/login_null_otp.robot

Suite Setup       start suite
Test Setup        start test case
Test Teardown     end test case
Suite Teardown    end suite

*** Variables ***
*** Test Cases ***

test login valid
    [Documentation]  login valid
    [Tags]           regression

    Login Valid    ${mobile_number_valid}

test login - wrong mobile number  # 09190
    [Documentation]  login - wrong mobile number
    [Tags]           regression

    Login - Wrong Mobile Number    ${mobile_number_wrong}

test login - invalid mobile number  # 09150560098
    [Documentation]  login - invalid mobile number
    [Tags]           regression

    Login - Invalid Mobile Number    ${mobile_number_invalid}

test login - Null mobile number
    [Documentation]  login - Null mobile number
    [Tags]           regression

    Login - Null Mobile Number

test login - invalid otp
    [Documentation]  login - invalid OTP
    [Tags]           regression

    Login - Invalid Otp   ${mobile_number_valid}    ${otp_invalid}

test login - Null Otp
    [Documentation]  login - Null OTP
    [Tags]           regression

    Login - Null Otp    ${mobile_number_valid}