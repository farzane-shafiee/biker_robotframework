import requests


# import EnvVar

def get_otp_from_api():
    url = "https://express-api-staging.snappfood.dev/biker/show-biker-last-otps/6875"

    payload = {}
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'en-US,en;q=0.9,fa;q=0.8',
        'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJ1c2VybmFtZSI6ImYuc2hhZmllZSIsImlwX2ZpbHRlciI6ZmFsc2UsInN1cGVyX2FjY2VzcyI6ZmFsc2UsImxhc3RfZ3JhbnRlZF9hdCI6bnVsbCwiaWF0IjoxNjk4NTY5NDkzLCJleHAiOjE3MzAxMDU0OTN9.j-Sx9MgoTGPlJjfra9eQL3_k80QyhyhCFASCofWS7MGE_DLyxVf4xGA8iMeHlgIy12uOww-r5BJ5OzG3O2GKwfcLatjXnLO4Zc23u7HjsF-NPpuL4e31YicAGbidWaXCcgLW6jdGWl9AFUCWTGwt4YLKPC9T-fFe7osFBwtvBjISFVjw7ITkVsI2VhicuVjOs9tYyTQZcNFpfv1qPwF0EWoDSMe-foRMqXS0hXjQBqiB3ZYhwNyk6JBKZUDLwS2C0dgJkObLz9XHBR2LuAu5vX4giICbdeIZWPM7kz-2qttjuLmanBzlwsDAyev2L_SMrUn6nEnmAjWGSSdYatg-LHZWlU9z3YqZ460cY2fHrZjkax6Kyh9zOi_aeZShyrDugWmw450MigoAX2nynGpOQLZQC2g_ksHdXCTZ_9bEheLn-6oqP4UC7NEZ6viWBXnjaDSiG_TwvC3eXHWtQw4OR9TDutMPd1YHWedkjVTKlZrJ8-YNyontPTuECpqnNtsCOdiEO3UyrN8MPydnBxJs7THUkYHqgQHYrqjZL5891WW1e_O2FtJy6F9bczSMNsyCIkw3NIl8MvAhxLaAH5SnmlzXhFP6WrFV0z9OIksvpNlINMx8S3ym33DOJ8DT67XzBcwtwd09RNSXvD3GLI6j8kVgDLBcK31Md9shg4dBkJo',
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
    # return EnvVar.getOtpApi()
