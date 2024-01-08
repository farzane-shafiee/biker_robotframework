*** Settings ***
Library        String
Variables      locators_variables.py
Variables      data_variables.py
Variables      ../base_config/base_variables
Resource       ../base_config/base_config.resource
Library        ${CURDIR}/login_keywords_python_library.py

*** Keywords ***
Enter The Phone Number Into The Input
    [Arguments]                         ${phone_number}
    Input Text                          ${phone_number_input_login}     ${phone_number}

Click On The Continue Button
    Click Element                       ${continue_button_login}

Get Phone Number From Text
    ${text_locator}     Get Text        ${phone_number_label_login}
    ${phone_number}     Get Substring   ${text_locator}     27      38
    RETURN                              ${phone_number}

Convert Persian Numerals
    [Arguments]                         ${persian_text}
    ${converted_text}=    Evaluate      "${persian_text}".replace('۰', '0').replace('۱', '1').replace('۲', '2').replace('۳', '3').replace('۴', '4').replace('۵', '5').replace('۶', '6').replace('۷', '7').replace('۸', '8').replace('۹', '9')
    RETURN                              ${converted_text}

#Get Token From Api
#    [Arguments]                         ${username}    ${password}
#    ${token}                            Get Token      ${username}    ${password}
#    RETURN                              ${token}

#Get Otp From Api
#    [Arguments]                         ${token}       ${biker_id}
#    ${otp}                              Get Otp        ${token}      ${biker_id}
#    RETURN                              ${otp}

Enter The Otp Into The Input
    [Arguments]    ${otp}
    Input Text                          ${otp_input_login}           ${otp}

Click On The Confirm Button
    Click Element                       ${confirm_button_login}