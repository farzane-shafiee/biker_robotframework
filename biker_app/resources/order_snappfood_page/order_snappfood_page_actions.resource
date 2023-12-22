*** Settings ***
Library        ${CURDIR}/order_snappfood_keywords_python_library.py
Variables      data_variables.py

*** Keywords ***
create orders
    ${order_id}             Create Order
    Sleep                   5s
    RETURN                  ${order_id}

orders list dispatch
    [Arguments]             ${order_id}
    ${trip_id}              Order List Dispatch     ${order_id}
    RETURN                  ${trip_id}

bikers free list dispatch
    [Arguments]             ${trip_id}
    ${biker_id}             Biker Free List         ${trip_id}      ${biker_mobile}
    RETURN                  ${biker_id}

assign trip from dispatch
    [Arguments]             ${trip_id}
    Assign Trip             ${trip_id}