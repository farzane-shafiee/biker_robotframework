*** Settings ***
Library        ${CURDIR}/order_snappfood_keywords_python_library.py
Variables      data_variables.py

*** Keywords ***
Get Token From Dispatch
    [Arguments]             ${username_dispatch}    ${password_dispatch}
    ${token_dispatch}       Get Token Dispatch      ${username_dispatch}    ${password_dispatch}
    RETURN                  ${token_dispatch}

create orders
    ${order_id}             Create Order
    Sleep                   5s
    RETURN                  ${order_id}

orders list dispatch
    [Arguments]             ${order_id}             ${token}
    ${trip_id}              Order List Dispatch     ${order_id}     ${token}
    RETURN                  ${trip_id}

bikers free list dispatch
    [Arguments]             ${trip_id}              ${token_dispatch}
    ${biker_id}             Biker Free List         ${trip_id}      ${biker_mobile}     ${token_dispatch}
    RETURN                  ${biker_id}

assign trip from dispatch
    [Arguments]             ${trip_id}              ${token_dispatch}
    Assign Trip             ${trip_id}              ${token_dispatch}