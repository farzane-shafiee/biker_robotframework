*** Settings ***
Resource       ../../resources/order_snappfood_page/order_snappfood_page_actions.resource


*** Test Cases ***
Create order
    ${token_dispatch}   Get Token From Dispatch     ${username_dispatch}    ${password_dispatch}
    ${order_id}         create orders
    ${trip_id}          orders list dispatch        ${order_id}    ${token_dispatch}
    ${biker_id}         bikers free list dispatch   ${trip_id}     ${token_dispatch}

    IF    ${biker_id} != False
        assign trip from dispatch           ${trip_id}      ${token_dispatch}
    END


