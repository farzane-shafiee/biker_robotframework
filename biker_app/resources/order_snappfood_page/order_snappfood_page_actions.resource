*** Settings ***
Library        ${CURDIR}/order_snappfood_keywords_python_library.py

*** Keywords ***
create order snappfood
    ${code}             Create Order
    Sleep                  5s
    RETURN              ${code}

order list snappfood
    [Arguments]         ${code}
    ${data}             Orders List            ${code}
    RETURN              ${data}

confirm order snappfood
    [Arguments]         ${data}
    Confirm Order       ${data}

call biker from dakhl
    [Arguments]         ${data}
    Call Biker          ${data}
