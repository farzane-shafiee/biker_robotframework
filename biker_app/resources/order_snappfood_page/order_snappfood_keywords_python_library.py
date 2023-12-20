import json
import http.client
import requests

BASE_URL_SNAPPFOOD_FRONT = "https://staging.snappfood.ir"
BASE_URL_SNAPPFOOD_BACKEND = "https://staging-backend.snappfood.dev"


def create_order():
    conn = http.client.HTTPSConnection("staging.snappfood.ir")
    payload = 'vendorCode=0mwyzz&vendorId=31755&bankCode=AP_Web&voucherCode=&paymentType=ONLINE&addressId=10001437&products=%5B%7B%22id%22%3A3993141%2C%22count%22%3A1%2C%22quantity%22%3A1%2C%22price%22%3A10000%2C%22isSpecial%22%3Atrue%7D%5D&paidByCredit=1&paidByCashback=0&isSpecial=1&expeditionType=DELIVERY&preorderDate=&dealProjectCode=q0976p&click_id=&client=PSA&customerComment=&appVersion=5.6.6&deviceType=PSA&storeName=Bazzar&platform=PSA&couponId=&packageId=&sourceOS=Android&reserverIdentity=user-547952831755&local='
    headers = {
        'authority': 'staging.snappfood.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6IjYyMjQ2ZmRlMTRhMWI1NDhjNWJkYTc4MTJkOWZhMGI4M2Q2N2RjNWMzOTIyOTk4YzA0N2ExOTRlNzM5YmJlMzI4OTg2MDVkZmVkNDU0MmJkIn0.eyJhdWQiOiJzbmFwcGZvb2RfcHdhIiwianRpIjoiNjIyNDZmZGUxNGExYjU0OGM1YmRhNzgxMmQ5ZmEwYjgzZDY3ZGM1YzM5MjI5OThjMDQ3YTE5NGU3MzliYmUzMjg5ODYwNWRmZWQ0NTQyYmQiLCJpYXQiOjE3MDIxMjM2MjEsIm5iZiI6MTcwMjEyMzYyMSwiZXhwIjoxNzA0ODAyMTQxLCJzdWIiOiIwOTE5MzYxOTQ2ODoyZTdjNTlmMzBiM2JjMjk5N2Q4MjNhZmUxMmE0OGJlYSIsInNjb3BlcyI6WyJtb2JpbGVfdjIiLCJtb2JpbGVfdjEiLCJ3ZWJ2aWV3IiwiYXBpX2RvbWFpbiJdfQ.XZA0zv33yRQHLa6GB0Y-AAL-uYIRtqMnWC_gPJ8imZthhjtW-L1hMDf_icQIbdeleVMv_xaQo9e5-mIGSjFFVJrFvYZ126LJ9hddtlvSMRWQRw7yJXqey1wsznoxrcDAfoZcYKLspD0oNnL-NoFET-1jTDixl4V-mmom8DJfM2x0mYVNns_px3UbVYt_992TJG1KWqI1lcnWJl5tsqSU39O7v_SABCWe2ymx9HxVlNHAmSbgQQuS6FJmDrzXUbOtO2liI_T3mv_hUDCSxHDj4WCUslXY1seiKshE7ljeu5TD3Gr6QEBUvOOmjXsRZYn0AUYXFPT26izCSUquaBkuhg',
        'content-type': 'application/x-www-form-urlencoded',
        'cookie': 'rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2Bn7osoML0xF54X7pNpOt9YddQ%2BdH4va08EranCvq9Bfplz8hcjpOiCMNloFSKCL70%2FLERpgGkA4Xsr2fevSqDNTWvjLu5c4x4%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19WQ5mgtbzX83ESiDiB%2BWFwNe41PPOUht48pwRYvaydhKACEQPZkB1q; _hjSessionUser_3300609=eyJpZCI6ImQwYzNlNGQzLWQ5OWMtNWJmYi04NjkwLTdmYzk2ZjY2YjVkNSIsImNyZWF0ZWQiOjE2OTUxMjcyNzkyNDMsImV4aXN0aW5nIjp0cnVlfQ==; REMEMBERME=Qm9kb0Zvb2RcVXNlckJ1bmRsZVxFbnRpdHlcVXNlcjpNRGt4T1RNMk1UazBOamc9OjE3MzA4ODkwODU6NTdiYzhjMzNiYzNiMmI2YzFkNGYwN2NjMzdiODZiZWNjZmI4ZjAwMWM2ODk5YjgyOTAxMmUzYjJlNzMxZGY1Zg%3D%3D; _ga_VMGHDLHM5Z=GS1.1.1699800525.12.1.1699801078.0.0.0; _ga_Z1TVJRJYR1=GS1.1.1701587126.6.1.1701592975.0.0.0; PHPSESSID=ff1ffffdab6c4b214f1b24e61657552c; _clck=mjp9cc%7C2%7Cfhn%7C0%7C1363; _ga_3N06GT6SP5=GS1.1.1702887907.6.1.1702887967.0.0.0; _gid=GA1.2.1074031708.1702892433; _gcl_au=1.1.1877110466.1702904255; _hjIncludedInSessionSample_3300609=0; _ga_S8BD3BVGB1=GS1.2.1702981433.13.1.1702983830.60.0.0; _hjSession_3300609=eyJpZCI6IjA2MjExYmI5LTFhNWUtNGNhOS05NWQzLTc5ZWY0NzllM2UxYiIsImMiOjE3MDI5ODkwOTA3ODQsInMiOjAsInIiOjAsInNiIjowfQ==; _hjAbsoluteSessionInProgress=0; rl_user_id=RudderEncrypt%3AU2FsdGVkX19bsov41A5f9Rnq7vT3%2BqgUgWm%2FrJW2PHE%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX19TFWMvStCvc3tpsu83jLfV5yPONTSek9qx%2F9BF7CvRUug7XwOWTOUZWDIQIDwbaaEBuwViGtKao0Fv1ksmAqIWcGIsqk4EYyQokkk1YkAo7LkftqaevkyBiqwn5180XOn%2FL6wNfqs%2Bl%2BpHNF3vjaBRGIrNtzwwWLf%2FdT4pm4xd28R3I%2FFEEL9zlXUV1E6KlRLSgV9Co037cNOoXh1l%2F2pYrp1jfytZUWBFtniWKpKoSUdNJlUmuaF4FOnf42fa0hLPYknEGhDASg%3D%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX1%2B4xl05NGwoYiI0BtvtmvzA%2BY4%2BmUjPuqk%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2B%2FEgdeuKKzP7yVOk7bKWeFRbp%2FzuSXQQ8%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2FDvErNwmN9gNy0DiiZvNrd9jS214VdYsXGqJa8enR3%2B5GuUfkF%2FmExoSFfxjGBXsGxD7e4%2Fo2h%2Fw%3D%3D; _ga=GA1.2.408329106.1694932124; _ga_G5J9VQQMGL=GS1.1.1702989090.91.1.1702993092.46.0.0; _ga_DLKJDL41ZH=GS1.1.1702989091.88.1.1702993097.36.0.0; rl_session=RudderEncrypt%3AU2FsdGVkX1%2BdZ9ClwFDC9Lh3kFvtiEsD6GGHbgTeA3ptqHWuyRiWX7SE6ubD6sNfpYCyzoFtv9tThs%2BL8UwrTTIThdDMFVS1GPCC%2FeB8h7clKuAdkS29zNEnBo9d8oh3MILsr3%2BoL8XypGOfwREzVw%3D%3D; PHPSESSID=ebcce45884bb2e007e2422f484649978',
        'origin': 'https://stagingm.snappfood.ir',
        'referer': 'https://stagingm.snappfood.ir/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?1',
        'sec-ch-ua-platform': '"Android"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G955U Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
    }
    conn.request("POST",
                 "/mobile/v1/order/new?client=PSA&optionalClient=PSA&deviceType=PSA&appVersion=5.6.6&optionalVersion=5.6.6&UDID=6899282c-a57f-4c5d-813f-5ff1947bf924",
                 payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode("utf-8"))
    return response['data']['code']


def orders_list(code_order):
    url = f"{BASE_URL_SNAPPFOOD_BACKEND}/order/index/?filter%5BorderId%5D=&filter%5BorderCode%5D=&filter%5BbatchOrderId%5D=&filter%5BstartDate%5D=&filter%5BendDate%5D=&filter%5BcustomerName%5D=&filter%5BorderCoupon%5D=&filter%5BrestaurantName%5D=&filter%5BvendorId%5D=0mwyzz&filter%5BuserId%5D=&filter%5BcurrentPage%5D=0&filter%5BnumberOfPages%5D=0&filter%5BpageSize%5D=100&filter%5BorderStatus%5D=&filter%5BpaymentType%5D=&filter%5BbankCode%5D=&filter%5BpaymentStatus%5D=&filter%5Boperatror%5D=&filter%5BorderSource%5D=&filter%5BorderType%5D=all&filter%5BpriceBottom%5D=&filter%5BpriceTop%5D=&filter%5BdeliveryPriceBottom%5D=&filter%5BdeliveryPriceTop%5D=&filter%5BpriceChangeBottom%5D=&filter%5BpriceChangeTop%5D=&filter%5Bcompany%5D=&filter%5BexpeditionType%5D=&filter%5BvendorSubType%5D=&_=1702971868060"

    payload = {}
    headers = {
        'authority': 'staging-backend.snappfood.dev',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'cookie': 'PHPSESSID=9cb9b55059911d4c9541ffffabc8e203; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BWpa6cgcV6KA8rfX4a4jd9p%2FLBf%2BbnEfE%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19N%2BWRBj6brrzfIeXBVXVy%2Fu4eJer6IYWQ%3D; _hjSessionUser_3300609=eyJpZCI6ImFjYzg5MmRjLWEyYjktNTJhMS04ZmViLWMwODJjNzhkOWY0MyIsImNyZWF0ZWQiOjE3MDExNzM1MzE3NDIsImV4aXN0aW5nIjp0cnVlfQ==; rl_group_id=RudderEncrypt%3AU2FsdGVkX18jV90rsANsEYJFb29y%2FeWwmiQTr8FCVqI%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18uHn7dpWXdeppx4yI6XKXscO0cK8Ct5Gs%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BxPn3skqq2V02kPIPJeVLrA7B3UWDfSjIl8ps8bE8ETSPEV0KjE1ahBgn7QZ7ayTAoOu9JWDTrMQ%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FiDCFyjt6W%2BFj1OIZrT0Nx946xsJ7exQ%2FG6jU%2FR23yGSxzEL%2FQCgxa; rl_trait=RudderEncrypt%3AU2FsdGVkX182hReJriXqruWUwkrQ%2ByXnE5dA2l0sEq6zbHOgl6%2FhqHv11VLqqtDyX8ir3Fd3RzS9zcLIZQD5owXe%2FhhSSSdR0brDXme2vwX144chYE70BzLIFWK1Ic8m; rl_session=RudderEncrypt%3AU2FsdGVkX18STqGJaIBIFQDqwaXzarbzZq99UbNG3WdyKw3mbfVZ8%2FjAS42EXodtEvfVXrn32gswpvb8xQuMfvsDxhI2jW9LrjJfJNQQPBMwVbRxtfeE6l4lsIdvjPb5sZVhJkT7IHFIaLh%2Fv%2FHWWw%3D%3D; _ga_DGFBLVBRPW=GS1.1.1702219035.46.1.1702219036.0.0.0; _gid=GA1.2.1470308214.1702892606; _ga=GA1.1.306838201.1701173151; _ga_VMGHDLHM5Z=GS1.1.1702970198.30.1.1702971867.0.0.0',
        'referer': f'{BASE_URL_SNAPPFOOD_BACKEND}/order/index/?vendor=0mwyzz',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    for item in response.json()['orders']:
        if item["0"]["code"] == code_order:
            return (item["0"]["id"],
                    item["0"]["products"][0]["food"]["id"],
                    item["0"]["products"][0]["food"]["productVariationId"],
                    item["0"]["products"][0]["food"]["price"],
                    item["0"]["products"][0]["food"]["total_price"],
                    item["0"]["newDeliveryFee"],
                    item["0"]["vmsPrice"])
        else:
            print("dont exist product")


def confirm_order(data):
    url = f"{BASE_URL_SNAPPFOOD_BACKEND}/order/{data[0]}/edit"
    payload = f"orderProduct%5B0%5D%5Bid%5D={data[1]}&orderProduct%5B0%5D%5BproductId%5D={data[2]}&orderProduct%5B0%5D%5Bquantity%5D=1&orderProduct%5B0%5D%5Bprice%5D={data[3]}&orderProduct%5B0%5D%5BchangePrice%5D=false&productsTotalPrice={data[4]}&deliveryFee={data[5]}&containerPrice=0&newOrderStatus=1&declineReasonId=&customerId=5479528&addressId=10001437&subscribeCode=&vendorId=31755&deliveryTime=42&orderComment=&vendorSPComment=&voucherValue=0&containerCb=1&deliveryCb=1&orderTotalValue={data[6]}&deltaOrderPrice=0&sendEmail=1&sendSMS=1&declineDetail=-1&declineComment=&payback=0&bankno=&bankcardno=&bankname=&paybackdesc=&paybackpaidat=&continue=0&riderPickupTime=0&setVendorUpdateStatus=&zoodfoodComment=&oldStatusCode=42&couponId="
    headers = {
        'authority': f'{BASE_URL_SNAPPFOOD_BACKEND}',
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'cookie': 'PHPSESSID=9cb9b55059911d4c9541ffffabc8e203; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX1%2BWpa6cgcV6KA8rfX4a4jd9p%2FLBf%2BbnEfE%3D; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19N%2BWRBj6brrzfIeXBVXVy%2Fu4eJer6IYWQ%3D; _hjSessionUser_3300609=eyJpZCI6ImFjYzg5MmRjLWEyYjktNTJhMS04ZmViLWMwODJjNzhkOWY0MyIsImNyZWF0ZWQiOjE3MDExNzM1MzE3NDIsImV4aXN0aW5nIjp0cnVlfQ==; rl_group_id=RudderEncrypt%3AU2FsdGVkX18jV90rsANsEYJFb29y%2FeWwmiQTr8FCVqI%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX18uHn7dpWXdeppx4yI6XKXscO0cK8Ct5Gs%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BxPn3skqq2V02kPIPJeVLrA7B3UWDfSjIl8ps8bE8ETSPEV0KjE1ahBgn7QZ7ayTAoOu9JWDTrMQ%3D%3D; rl_user_id=RudderEncrypt%3AU2FsdGVkX1%2FiDCFyjt6W%2BFj1OIZrT0Nx946xsJ7exQ%2FG6jU%2FR23yGSxzEL%2FQCgxa; rl_trait=RudderEncrypt%3AU2FsdGVkX182hReJriXqruWUwkrQ%2ByXnE5dA2l0sEq6zbHOgl6%2FhqHv11VLqqtDyX8ir3Fd3RzS9zcLIZQD5owXe%2FhhSSSdR0brDXme2vwX144chYE70BzLIFWK1Ic8m; rl_session=RudderEncrypt%3AU2FsdGVkX18STqGJaIBIFQDqwaXzarbzZq99UbNG3WdyKw3mbfVZ8%2FjAS42EXodtEvfVXrn32gswpvb8xQuMfvsDxhI2jW9LrjJfJNQQPBMwVbRxtfeE6l4lsIdvjPb5sZVhJkT7IHFIaLh%2Fv%2FHWWw%3D%3D; _ga_DGFBLVBRPW=GS1.1.1702219035.46.1.1702219036.0.0.0; _gid=GA1.2.1470308214.1702892606; _gat_gtag_UA_120962988_1=1; _ga_VMGHDLHM5Z=GS1.1.1702970198.30.1.1702971804.0.0.0; _ga=GA1.1.306838201.1701173151',
        'origin': f'{BASE_URL_SNAPPFOOD_BACKEND}',
        'referer': f'{BASE_URL_SNAPPFOOD_BACKEND}/order/{data[0]}?orderAccessible=1&redirected_from_pickup=0',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest'
    }
    requests.request("POST", url, headers=headers, data=payload)


def call_biker(data):
    conn = http.client.HTTPSConnection("staging.snappfood.ir")
    payload = ''
    headers = {
        'authority': 'staging.snappfood.ir',
        'accept': 'application/json, text/plain, */*',
        'accept-language': 'en-US,en;q=0.9,fa;q=0.8',
        'authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJzbmFwcGZvb2Rfdm1zIiwiZXhwIjoxNzAzNTg5MjI1LCJpYXQiOjE3MDI5NjI4MjUsImlzcyI6ImF1dGguc25hcHBmb29kLmlyIiwianRpIjoiOWY0ODNjY2I4MDIwMTIxM2FlZmRkOWRjOWMwYTJjM2UxNzQ5ODI3NCIsInNjb3BlcyI6WyJ2bW8iLCJ2bXMiXSwic3ViIjoiMDkxOTM2MTk0Njg6MmU3YzU5ZjMwYjNiYzI5OTdkODIzYWZlMTJhNDhiZWEifQ.hfTfOUeuX7fjKdG7V-vkQw8FT9JR0wuQXGj8qKGigvJ0xSgXogTgSspO8HQFPDWgLtU6Qi8dzyg_ax6VGDHvrVogKoCv2yzGpIJU184XDamxZa4rMWKgaeaDSpAH5QFIU63gEbZn2oY4-dV8H9LBSWdvbV-3uYP-vrah9ES46I-XJP5H9UX4MY-T1REeBMs8EDg8iJ4s8XL1gisr_h837Hr26kmhql-BZsQwgWO5G94jjFoNNhWMbRoSMf2sJK08yazwGgI7f3h_3xuDPnIeN4f5LzslBGvwtnQkOripgZWUNlaRJc7e7_FT25GSZpGUmIgBjepne87CNY-h73w44A',
        'content-length': '0',
        'origin': 'https://dakhl-ordering-staging.snappfood.dev',
        'referer': 'https://dakhl-ordering-staging.snappfood.dev/',
        'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Linux"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
        'Cookie': 'PHPSESSID=ebcce45884bb2e007e2422f484649978'
    }
    conn.request("POST", f"/vms/v1/order/create-on-demand-express-trips?orderId={data[0]}", payload, headers)
    res = conn.getresponse()
    data = res.read()
    response = json.loads(data.decode("utf-8"))
    print(response)
