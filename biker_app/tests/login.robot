*** Settings ***
Library        AppiumLibrary
Resource       ../resources/base_config.robot
Variables      ../resources/login_page/data_variables.py
Variables      ../resources/landing_page/locators_variables.py
Variables      ../resources/login_page/locators_variables.py

Suite Setup       start suite
Test Setup        start test case
Test Teardown     end test case
Suite Teardown    end suite

*** Variables ***
*** Test Cases ***

test search robot
    [Documentation]  login test
    [Tags]           regression

    Wait Until Page Contains Element    ${phone_number_input}    timeout=10s
    Click Element    ${phone_number_input}
    Input Text       ${phone_number_input}     ${phone_number}
#    Press Keys       ${SearchBox}     ENTER

#test search book
#    [Documentation]  Google test
#    [Tags]           regression
#    Pass Execution    message
#    Input Text       ${SearchBox}     ${search_input.test2}
#    Press Keys       ${SearchBox}     ENTER