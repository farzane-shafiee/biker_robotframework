*** Settings ***
Library        ${CURDIR}/order_snappfood_keywords_python_library.py
Library        ../login_page/login_keywords_python_library.py
Variables      data_variables.py
Variables      ../base_config/base_variables

*** Keywords ***
Evaluate Time Stamp
    ${timestamp}=           Evaluate                calendar.timegm(time.gmtime())
    RETURN                  ${timestamp}