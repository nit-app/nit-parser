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
    res = requests.post('https://nit-api.upfolio.ru/v1/eventAdmin/create', json.dumps(body), headers={
        'cookie': 'isomiso='
    })
    print(res.status_code, res.json())

