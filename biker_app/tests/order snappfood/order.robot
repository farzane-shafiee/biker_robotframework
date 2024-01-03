*** Settings ***
Library        String
Resource       ../../resources/order_snappfood_page/order_snappfood_page_actions.resource
Resource       ../../resources/login_page/login_page_actions.resource

*** Test Cases ***
Create order
    ${token_dispatch}   Get Token From Api          ${username_dispatch}    ${password_dispatch}
    ${time_stamp} =     Run Keyword If  1           Evaluate Time Stamp
    ${string_code}      Generate Random String      7                       [LOWER]
    ${number_code}      Generate Random String      8                       [NUMBERS]
    ${order_id}         Create Orders In Dispatch   ${string_code}          ${number_code}          ${time_stamp}
    ${trip_id}          Order List Dispatch         ${order_id}             ${token_dispatch}
    ${biker_id}         Bikers Free List Dispatch   ${trip_id}              ${token_dispatch}

    IF    ${biker_id} != False
        Assign Trip From Dispatch                   ${trip_id}              ${token_dispatch}       ${biker_id}
    END
