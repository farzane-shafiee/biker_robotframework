*** Settings ***
Resource       ../../resources/order_snappfood_page/order_snappfood_page_actions.resource


*** Test Cases ***
Create order
    ${code}                     create order snappfood
    ${data}                     order list snappfood    ${code}
    confirm order snappfood     ${data}
    call biker from dakhl       ${data}



