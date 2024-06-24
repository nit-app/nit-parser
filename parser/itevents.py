from store.store import itevents, save_store

from bs4 import BeautifulSoup
import requests
from sender.sender import send


def run():
    while True:
        new_post_id = itevents['last_post'] + 1
        origin = f"https://it-events.com/events/{new_post_id}"

        try:
            result = requests.get(origin)

        except Exception:
            new_post_id['last_post'] = new_post_id - 1
            break

        soup = BeautifulSoup(result.text, 'html.parser')
        name = soup.find('h1', {'class': 'event-header__title'}).text.strip('\n')
        location = soup.find('div', {
            'class': 'event-header__line event-header__line_addr'}).text.strip('\n')

        description = soup.find('div', {'class': 'user-generated'}).text.strip('\n')

        send(name, description if description else '', origin, location)
        save_store()
