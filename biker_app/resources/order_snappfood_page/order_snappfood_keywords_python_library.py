import requests
import json

BASE_URL_ZOODFOOD = "https://express-api-staging.zoodfood.com"
BASE_URL = "https://express-api-staging.snappfood.dev"


def create_order(string_code, number_code, time_stamp):
    """
    Creates an order
    :return: order_id
    """
    url = f"{BASE_URL_ZOODFOOD}/client/trip/create"

    payload = json.dumps({
        "preOrder": True,
        "code": string_code,
        "source": {
            "title": "وندور تست اتومیشن",
            "address": "آدرس وندور",
            "location": {
                "latitude": 35.74451,
                "longitude": 51.47685
            },
            "logo": None,
            "phone": "2188198740"
        },
        "destination": {
            "address": "آدرس مشتری",
            "location": {
                "latitude": 35.773312,
                "longitude": 51.4183466
            }
        },
        "customer": {
            "phone": "0912 839 9442",
            "name": "فرزان",
            "customerId": 407548,
            "rank": "برنز"
        },
        "order": "تست کباب-1-13000",
        "orderId": number_code,
        "time_to_arrive": time_stamp,
        "statusDate": time_stamp,
        "creationTime": time_stamp,
        "description": "descripttion",
        "sourceCode": "0m7dq0",
        "sourceId": 100977,
        "cityCode": "tehran",
        "paymentType": "ONLINE",
        "expectedDeliveryTime": time_stamp
    })
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJjbGllbnQiOiJzbmFwcGZvb2QiLCJleHAiOjE4NjIyOTY2OTIsImlhdCI6MTU0NjY3NzQ5Mn0.LeDJ5VHKE5mvsrvp-nAef1X-N9FTO_38FyazrjSMcpIRXkDYXtZ9Axr7mxKsnWtnnCneKKJmDsrm7yOgfwOpIIznVkaqT--UJPVsR0sQy8DtZkX2Spr2F4VCz8XyFw5sOhSsWDE5ag-IK31WMRwxNL1_Iksh_5Y56QwLgndWG-p30gMrYbyfWTMldGeLOE9D2l6Pmg5Ih1NM19dOcqLPubvHI9z2Gm8xYrpquXBT0GsQQVYAMI2g26RFnDTgVALm8yZr88vdIh7qrNKeouR_BHqeZUBASKChfCvGN4sRGmJgFvCYGUrsgvq25MhTrqUADAZx6HQDGRrRNhQJ8Hm3mO14nyuLRBu9zoJXs-cFxupEZWN0wnxyVZdg-nId0Z_vGOv9l_yg8DMESv7fMPWsYGmoaFb1QmhcUS9LHQw4xWmJZjYLy22i-2gXDUmLFCC2EjaHv-wa1bfNd5DMTLUySLy7wUrhO10rMM10sT4n75NTHd6pGbHumzaDTVidJwcyx_ilDn6PScy0NFbsmJf8xqvriY6HBxPo-QK8UGtJpJWZYzGeiD81fVE3rx169FnP9xgO-n-Ar3Lw7LWgAr-fSnQzZmxY8b0hf5MOy2K3t09zCy66kclcJRtyGkBemDwQ3oxL7JEsxgOTTFwBOTw438KqZvQT74NofEbR8WzXqVg'
    }
    requests.request("POST", url, headers=headers, data=payload)
    return number_code


def order_list_dispatch(order_id, token):
    """
    check orders list and return order_id
    :param token
    :param order_id
    :return: order_id
    """
    url = f"{BASE_URL}/trip/trip-status"

    payload = 'currentPage=0&tripStatus=REQUESTED'
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    for item in response.json()["trips"]:  # بررسی لیست سفرها و پیدا کردن order_id
        if str(item["zfOrderId"]) == order_id:
            return item['id']
        else:
            continue
    else:
        return False


def biker_free_list(trip_id, biker_mobile, token_dispatch):
    """
    check biker free list and return biker_id
    :param token_dispatch
    :param trip_id
    :param biker_mobile: get from data_variables file
    :return: biker_id
    """
    url = f"{BASE_URL}/biker/show-free-bikers-light"

    payload = f'tripId={trip_id}'
    headers = {
        'authorization': f'Bearer {token_dispatch}',
        'content-type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.json()['bikers']['FREE'])
    for item in response.json()['bikers']['FREE']:  # بررسی لیست بایکرهای فری و پیدا کردن بایکر مورد نظر
        if item['phone'] == biker_mobile:
            return item['id']
        else:
            continue
    else:
        return False


def assign_trip(trip_id, token_dispatch, biker_id):
    """
    Assign trip to biker free
    :param biker_id
    :param token_dispatch
    :param trip_id
    """
    url = f"{BASE_URL}/trip/assign-trip"

    payload = f'tripId={trip_id}&userId={biker_id}&canAssignTripToBikerAgain=false'
    headers = {
        'authorization': f'Bearer {token_dispatch}',
        'content-type': 'application/x-www-form-urlencoded'
    }
    requests.request("POST", url, headers=headers, data=payload)
