from store.store import itc2go, save_store

from bs4 import BeautifulSoup
import requests
from sender.sender import send


def run():
    while True:
        new_post_id = itc2go['last_post'] + 1
        origin = f"https://ict2go.ru/events/{new_post_id}"

        try:
            result = requests.get(origin)

        except Exception:
            new_post_id['last_post'] = new_post_id - 1
            break

        soup = BeautifulSoup(result.text, 'html.parser')
        name = soup.find('h1', {'class': 'event-h1'}).text.strip('\n')
        location = soup.find('p', {
            'class': 'place-info'}).find('a').text.strip('\n')

        description = soup.find('div', {'class': 'tab-item description-info'}).text.strip('\n')

        send(name, description if description else '', origin, location)
        save_store()

