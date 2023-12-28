import random
import string
import time
import calendar
import requests
import json

BASE_URL_ZOODFOOD = "https://express-api-staging.zoodfood.com"
BASE_URL = "https://express-api-staging.snappfood.dev"
BASE_URL_DISPATCH = "https://express-ui-staging.zoodfood.com"


def create_order():
    """
    Creates an order
    :return: order_id
    """
    current_GMT = time.gmtime()
    time_stamp = calendar.timegm(current_GMT)  # create time stamp

    code = ''.join(random.choices(string.ascii_lowercase +
                                  string.digits, k=7))  # create code from characters 7
    order_id = ''.join(["{}".format(random.randint(1, 9)) for num in range(1, 8)])  # create order_id 8 number

    url = f"{BASE_URL_ZOODFOOD}/client/trip/create"

    payload = json.dumps({
        "preOrder": True,
        "code": code,
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
        "orderId": order_id,
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
    return order_id


def order_list_dispatch(order_id):
    """
    check orders list and return order_id
    :param order_id
    :return: order_id
    """
    url = f"{BASE_URL}/trip/trip-status"

    payload = 'currentPage=0&tripStatus=REQUESTED'
    headers = {
        'authority': 'express-api-staging.snappfood.dev',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImYuc2hhZmllZSIsImlwX2ZpbHRlciI6ZmFsc2UsInN1cGVyX2FjY2VzcyI6ZmFsc2UsImxhc3RfZ3JhbnRlZF9hdCI6bnVsbCwiaWF0IjoxNzAyOTkwMjg4LCJleHAiOjE3MzQ1MjYyODh9.0iRs3wCoojiaXa47E_VB5HewlTrE9-D2BSEy3CZUgEUyQDMh6K1EYq3g46PEXcWYq8Ngf16m3HUjWXr-itgTAbbRzpOsii95bM_Nnw_-KCSYXJ6DTi3vskTl0pX1rhpfzevPbYZilPO1NB_4BhiFZi3J7_l6SMTAY-gwVS-rtb38smO00gnp_0OrCO9XCH3X8TqHpZNAks-o8vYtd5Lv-hcLfkXgCyL30WJneOk6-aEsWAM_kZeMURu_WMpMMv_tXfe7VSXjPptawbRMBtcXvvgO6iKwwZq-EBszQrQ-fYhWppSKYVJD0194-VRh_qZjtw1ZlYz0hExRMf3aXMlpKzHZ7BWU1tYFmasXmOLnZWs_X7FgRdWBLu2436QOA2FfjX1mXgNlfzF7R_QDzHmbx2DYYjierRleGvbxdXf_YHIaHn1hsZRcCoXxiQ7fF67p87WXs_NqzDHyCYPJeWdIZ0J3__AF395886vBQgUSZ5y1Vlr4e9tRQDUVNqvNp6wQktgSr4BtjfOw7n6ku4E9NpFxMVoKEt839TJOn0sY9G687Wz9Yvk3VawdO5xRkTANmsSblxoauhIEfFa3030FyaAurMKTO9KOFEhPD7OGu-Pf9K_qjSMq1mKH_FjtRVnYcJenB2dcGKNeURsl-2fX0SLnIo-MUesJKbIyVFA6uic',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': f'{BASE_URL_DISPATCH}',
        'referer': f'{BASE_URL_DISPATCH}/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    for item in response.json()["trips"]:  # بررسی لیست سفرها و پیدا کردن order_id
        if str(item["zfOrderId"]) == order_id:
            return item['id']
        else:
            continue
    else:
        return False


def biker_free_list(trip_id, biker_mobile):
    """
    check biker free list and return biker_id
    :param trip_id:
    :param biker_mobile: get from data_variables file
    :return: biker_id
    """
    url = f"{BASE_URL}/biker/show-free-bikers-light"

    payload = f'tripId={trip_id}'
    headers = {
        'authority': 'express-api-staging.snappfood.dev',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImYuc2hhZmllZSIsImlwX2ZpbHRlciI6ZmFsc2UsInN1cGVyX2FjY2VzcyI6ZmFsc2UsImxhc3RfZ3JhbnRlZF9hdCI6bnVsbCwiaWF0IjoxNzAyOTkwMjg4LCJleHAiOjE3MzQ1MjYyODh9.0iRs3wCoojiaXa47E_VB5HewlTrE9-D2BSEy3CZUgEUyQDMh6K1EYq3g46PEXcWYq8Ngf16m3HUjWXr-itgTAbbRzpOsii95bM_Nnw_-KCSYXJ6DTi3vskTl0pX1rhpfzevPbYZilPO1NB_4BhiFZi3J7_l6SMTAY-gwVS-rtb38smO00gnp_0OrCO9XCH3X8TqHpZNAks-o8vYtd5Lv-hcLfkXgCyL30WJneOk6-aEsWAM_kZeMURu_WMpMMv_tXfe7VSXjPptawbRMBtcXvvgO6iKwwZq-EBszQrQ-fYhWppSKYVJD0194-VRh_qZjtw1ZlYz0hExRMf3aXMlpKzHZ7BWU1tYFmasXmOLnZWs_X7FgRdWBLu2436QOA2FfjX1mXgNlfzF7R_QDzHmbx2DYYjierRleGvbxdXf_YHIaHn1hsZRcCoXxiQ7fF67p87WXs_NqzDHyCYPJeWdIZ0J3__AF395886vBQgUSZ5y1Vlr4e9tRQDUVNqvNp6wQktgSr4BtjfOw7n6ku4E9NpFxMVoKEt839TJOn0sY9G687Wz9Yvk3VawdO5xRkTANmsSblxoauhIEfFa3030FyaAurMKTO9KOFEhPD7OGu-Pf9K_qjSMq1mKH_FjtRVnYcJenB2dcGKNeURsl-2fX0SLnIo-MUesJKbIyVFA6uic',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': f'{BASE_URL_DISPATCH}',
        'referer': f'{BASE_URL_DISPATCH}/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
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


def assign_trip(trip_id):
    """
    Assign trip to biker free
    :param trip_id
    """
    url = f"{BASE_URL}/trip/assign-trip"

    payload = f'tripId={trip_id}&userId=6875&canAssignTripToBikerAgain=false'
    headers = {
        'authority': 'express-api-staging.snappfood.dev',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImYuc2hhZmllZSIsImlwX2ZpbHRlciI6ZmFsc2UsInN1cGVyX2FjY2VzcyI6ZmFsc2UsImxhc3RfZ3JhbnRlZF9hdCI6bnVsbCwiaWF0IjoxNzAyOTkwMjg4LCJleHAiOjE3MzQ1MjYyODh9.0iRs3wCoojiaXa47E_VB5HewlTrE9-D2BSEy3CZUgEUyQDMh6K1EYq3g46PEXcWYq8Ngf16m3HUjWXr-itgTAbbRzpOsii95bM_Nnw_-KCSYXJ6DTi3vskTl0pX1rhpfzevPbYZilPO1NB_4BhiFZi3J7_l6SMTAY-gwVS-rtb38smO00gnp_0OrCO9XCH3X8TqHpZNAks-o8vYtd5Lv-hcLfkXgCyL30WJneOk6-aEsWAM_kZeMURu_WMpMMv_tXfe7VSXjPptawbRMBtcXvvgO6iKwwZq-EBszQrQ-fYhWppSKYVJD0194-VRh_qZjtw1ZlYz0hExRMf3aXMlpKzHZ7BWU1tYFmasXmOLnZWs_X7FgRdWBLu2436QOA2FfjX1mXgNlfzF7R_QDzHmbx2DYYjierRleGvbxdXf_YHIaHn1hsZRcCoXxiQ7fF67p87WXs_NqzDHyCYPJeWdIZ0J3__AF395886vBQgUSZ5y1Vlr4e9tRQDUVNqvNp6wQktgSr4BtjfOw7n6ku4E9NpFxMVoKEt839TJOn0sY9G687Wz9Yvk3VawdO5xRkTANmsSblxoauhIEfFa3030FyaAurMKTO9KOFEhPD7OGu-Pf9K_qjSMq1mKH_FjtRVnYcJenB2dcGKNeURsl-2fX0SLnIo-MUesJKbIyVFA6uic',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': f'{BASE_URL_DISPATCH}',
        'referer': f'{BASE_URL_DISPATCH}/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    requests.request("POST", url, headers=headers, data=payload)
