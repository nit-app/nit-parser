import json

import requests


def send(title, description, origin, location):
    body = {
        "title": title,
        "plainDescription": f"{description}\n\n{origin}",
        "isMachineGenerated": True,
        "priceLow": 1,
        "priceHigh": 2,
        "ageLimitLow": 1,
        "ageLimitHigh": 80,
        "location": location if location else '.',
        "ownerInfo": origin,
        "hasCertificate": False,
        "tags": ["ИТ", "ИБ"]
    }
    try:
        res = requests.post('https://nit-api.upfolio.ru/v1/eventAdmin/create', json.dumps(body), headers=get_auth())
        log_success(res)
    except Exception as e:
        log_error(e)


def get_auth():
    return {
        'cookie': 'isomiso='
    }


def log_success(res):
    print(res.status_code, res.json())


def log_error(error: Exception):
    print(error)
