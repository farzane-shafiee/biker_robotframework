*** Settings ***
Resource       ../../resources/order_snappfood_page/order_snappfood_page_actions.resource


*** Test Cases ***
Create order
    ${token_dispatch}   Get Token From Api          ${username_dispatch}    ${password_dispatch}
    ${order_id}         Create Order
    ${trip_id}          Order List Dispatch         ${order_id}             ${token_dispatch}
    ${biker_id}         Bikers Free List Dispatch   ${trip_id}              ${token_dispatch}

    IF    ${biker_id} != False
        Assign Trip From Dispatch                   ${trip_id}              ${token_dispatch}       ${biker_id}
    END


