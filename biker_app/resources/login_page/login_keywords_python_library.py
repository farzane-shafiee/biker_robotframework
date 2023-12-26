import requests
import http.client
from unidecode import unidecode

BASE_URL_EXPRESS = "https://express-api-staging.snappfood.dev"


def get_token_from_api(username, mobile_number_valid):
    url = f"{BASE_URL_EXPRESS}/mobile/user/api-login"

    payload = f'password={mobile_number_valid}&username={username}'
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://express-ui-staging.zoodfood.com',
        'Referer': 'https://express-ui-staging.zoodfood.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'sec-ch-ua-mobile': '?0',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['token']
    return token


def get_otp_from_api(token):
    url = F"{BASE_URL_EXPRESS}/biker/show-biker-last-otps/6875"

    payload = {}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Authorization': F'Bearer {token}',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Origin': 'https://express-ui-staging.zoodfood.com',
        'Referer': 'https://express-ui-staging.zoodfood.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
        'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()['lastOtps']


def get_part_of_text(text):
    return unidecode(text[27:38])


def change_state_biker(biker_id, state_biker):
    conn = http.client.HTTPSConnection("express-api-staging.snappfood.dev")
    payload = f'bikerId={biker_id}&reason=%D9%85%D9%88%D8%B1%D8%AF%20%D8%A7%D9%86%D8%B8%D8%A8%D8%A7%D8%B7%DB%8C-%D8%AA%D9%88%D9%87%DB%8C%D9%86%20%D9%88%20%D9%81%D8%AD%D8%A7%D8%B4%DB%8C&until=&description=&status={state_biker}'
    headers = {
        'authority': 'express-api-staging.snappfood.dev',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImYuc2hhZmllZSIsImlwX2ZpbHRlciI6ZmFsc2UsInN1cGVyX2FjY2VzcyI6ZmFsc2UsImxhc3RfZ3JhbnRlZF9hdCI6bnVsbCwiaWF0IjoxNzAyOTkwMjg4LCJleHAiOjE3MzQ1MjYyODh9.0iRs3wCoojiaXa47E_VB5HewlTrE9-D2BSEy3CZUgEUyQDMh6K1EYq3g46PEXcWYq8Ngf16m3HUjWXr-itgTAbbRzpOsii95bM_Nnw_-KCSYXJ6DTi3vskTl0pX1rhpfzevPbYZilPO1NB_4BhiFZi3J7_l6SMTAY-gwVS-rtb38smO00gnp_0OrCO9XCH3X8TqHpZNAks-o8vYtd5Lv-hcLfkXgCyL30WJneOk6-aEsWAM_kZeMURu_WMpMMv_tXfe7VSXjPptawbRMBtcXvvgO6iKwwZq-EBszQrQ-fYhWppSKYVJD0194-VRh_qZjtw1ZlYz0hExRMf3aXMlpKzHZ7BWU1tYFmasXmOLnZWs_X7FgRdWBLu2436QOA2FfjX1mXgNlfzF7R_QDzHmbx2DYYjierRleGvbxdXf_YHIaHn1hsZRcCoXxiQ7fF67p87WXs_NqzDHyCYPJeWdIZ0J3__AF395886vBQgUSZ5y1Vlr4e9tRQDUVNqvNp6wQktgSr4BtjfOw7n6ku4E9NpFxMVoKEt839TJOn0sY9G687Wz9Yvk3VawdO5xRkTANmsSblxoauhIEfFa3030FyaAurMKTO9KOFEhPD7OGu-Pf9K_qjSMq1mKH_FjtRVnYcJenB2dcGKNeURsl-2fX0SLnIo-MUesJKbIyVFA6uic',
        'content-type': 'application/x-www-form-urlencoded',
        'origin': 'https://express-ui-staging.zoodfood.com',
        'referer': 'https://express-ui-staging.zoodfood.com/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
    }
    conn.request("POST", "/mobile/biker/update-user-status", payload, headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
