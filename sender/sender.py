import json

import requests


def send(title, description, origin):
    body = {
        "title": title,
        "plainDescription": f"{description}\n\n{origin}",
        "isMachineGenerated": True,
        "priceLow": 1,
        "priceHigh": 2,
        "ageLimitLow": 1,
        "ageLimitHigh": 100,
        "location": "ю",
        "ownerInfo": origin,
        "hasCertificate": False,
        "tags": ["ИТ", "ИБ"]
    }
    res = requests.post('nit')
    print(res.status_code, res.json()['text'])
