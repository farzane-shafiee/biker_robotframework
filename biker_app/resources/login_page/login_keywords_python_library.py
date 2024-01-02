import requests
from unidecode import unidecode
from data_variables import username, mobile_number_valid

BASE_URL_EXPRESS = "https://express-api-staging.snappfood.dev"


def get_token_from_api():
    url = f"{BASE_URL_EXPRESS}/mobile/user/api-login"

    payload = f'password={mobile_number_valid}&username={username}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['token']
    return token


def get_otp_from_api(token):
    url = F"{BASE_URL_EXPRESS}/biker/show-biker-last-otps/6875"

    payload = {}
    headers = {
        'Authorization': F'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()['lastOtps']


def get_part_of_text(text):
    return unidecode(text[27:38])


