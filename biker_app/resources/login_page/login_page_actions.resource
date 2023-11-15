*** Settings ***
Variables      ../../resources/login_page/locators_variables.py
Variables      ../../resources/login_page/data_variables.py
Resource       ../base_config/base_config.resource
Library        login_keywords_python_library.py

*** Keywords ***

enter the phone number into the input
    [Arguments]    ${phone_number}
    Wait Until Page Contains Element    ${phone_number_input}     timeout=10s
    Input Text                          ${phone_number_input}     ${phone_number}
    Wait Until Page Contains Element    ${cross_button}

click on the continue button
    Click Element                       ${continue_button}

assert valid phone number
    ${text_otp_page}                    Get Text                  ${otp_page_label}
    ${phone_number}                     Get Part Of Text          ${text_otp_page}
    Should be equal as strings          ${phone_number}           ${mobile_number_valid}

enter the otp into the input
    [Arguments]    ${otp}
    Input Text                          ${otp_input}              ${otp}

set the otp from api
    ${token}                            Get Token
    Get Otp From Api                    ${token}

click on the confirm button
    Click Element                       ${confirm_login_button}
    Activate App Locations

assert valid login
    Wait Until Page Contains Element    ${assert_login_valid}
    Page Should Contain Element         ${assert_login_valid}

activate app locations
    Wait Until Page Contains Element    ${location_button}
    Click Element                       ${location_button}
    Sleep    1s
    Click Element                       ${location_button2}
    Sleep    1s
    Click Element                       ${click_fake}
    Click Element                       ${click_fake}
    Click Element                       ${click_fake}

assert wrong phone number
    Wait Until Page Contains Element    ${assert_username_invalid}
    Page Should Contain Element         ${assert_username_invalid}
    Page Should Contain Text            شماره موبایل صحیح وارد نشده است

assert invalid phone number
    Wait Until Page Contains Element    ${assert_username_invalid}
    Page Should Contain Element         ${assert_username_invalid}
    Page Should Contain Text            شماره معتبر نمیباشد.

assert invalid otp
    Wait Until Page Contains Element    ${assert_otp_invalid}
    Page Should Contain Element         ${assert_otp_invalid}

assert null otp
    Wait Until Page Contains Element    ${assert_null_otp}
    Page Should Contain Element         ${assert_null_otp}