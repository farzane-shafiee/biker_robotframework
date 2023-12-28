*** Settings ***
Resource       ../../resources/order_snappfood_page/order_snappfood_page_actions.resource


*** Test Cases ***
Create order
    ${order_id}                 create orders
    ${trip_id}               orders list dispatch       ${order_id}
    ${biker_id}           bikers free list dispatch     ${trip_id}

    IF    ${biker_id} != False
        assign trip from dispatch           ${trip_id}  ${biker_id}
    END


