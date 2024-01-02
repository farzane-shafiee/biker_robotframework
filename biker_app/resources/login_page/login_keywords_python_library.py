import requests

BASE_URL_EXPRESS = "https://express-api-staging.snappfood.dev"


def get_token(username, mobile_number_valid):
    url = f"{BASE_URL_EXPRESS}/mobile/user/api-login"

    payload = f'password={mobile_number_valid}&username={username}'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    token = response.json()['token']
    return token


def get_otp(token, biker_id):
    url = f"{BASE_URL_EXPRESS}/biker/show-biker-last-otps/{biker_id}"

    payload = {}
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/x-www-form-urlencoded'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()['lastOtps']
