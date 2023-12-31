import requests
from unidecode import unidecode
from data_variables import username, mobile_number_valid

BASE_URL_EXPRESS = "https://express-api-staging.snappfood.dev"


def get_token_from_api():
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


