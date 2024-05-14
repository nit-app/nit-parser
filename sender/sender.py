import requests


def send(title, description, origin):
    body = {
        "title": title,
        "plainDescription": f"{description}\n\n{origin}",
        "isMachineGenerated": True
    }
    requests.post('https://nit.upfolio.ru/v1/eventAdmin/create', body)
