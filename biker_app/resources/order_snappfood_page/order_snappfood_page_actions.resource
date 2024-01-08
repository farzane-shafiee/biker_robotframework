*** Settings ***
Library        ${CURDIR}/order_snappfood_keywords_python_library.py
Library        ../login_page/login_keywords_python_library.py
Variables      data_variables.py
Variables      ../base_config/base_variables

*** Keywords ***
Evaluate Time Stamp
    ${timestamp}=           Evaluate                calendar.timegm(time.gmtime())
    RETURN                  ${timestamp}

#Create Orders In Dispatch
#    [Arguments]             ${string_code}          ${number_code}          ${time_stamp}
#    ${order_id}             Create Order            ${string_code}          ${number_code}      ${time_stamp}
#    Sleep                   5s
#    RETURN                  ${order_id}

#Orders List Dispatch
#    [Arguments]             ${order_id}             ${token}
#    ${trip_id}              Order List Dispatch     ${order_id}             ${token}
#    RETURN                  ${trip_id}

#Bikers Free List Dispatch
#    [Arguments]             ${trip_id}              ${token_dispatch}
#    ${biker_id}             Biker Free List         ${trip_id}              ${biker_mobile}     ${token_dispatch}
#    RETURN                  ${biker_id}

#Assign Trip From Dispatch
#    [Arguments]             ${trip_id}              ${token_dispatch}       ${biker_id}
#    Assign Trip             ${trip_id}              ${token_dispatch}       ${biker_id}