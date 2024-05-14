from store.store import channels
from bs4 import BeautifulSoup
import requests
import schedule
from threading import Thread
# from checker.checker import checker, VALID_EVENT_THRESHOLD
from sender.sender import send


def run():
    print(channels)
    for index, channel in enumerate(channels):
        name = channel['name']
        last_try = 0
        while True:
            new_post_id = channel['last_post'] + 1
            origin = f"https://t.me/{name}/{new_post_id}"

            try:
                result = requests.get(origin)
            except Exception:
                channels[index]['last_post'] = new_post_id - 1
                break

            soup = BeautifulSoup(result.content, 'html.parser')

            has_message = soup.find('div', {"class": 'tgme_page_widget'})
            if not has_message:
                last_try += 1
                channels[index]['last_post'] = new_post_id
                if last_try > 10:
                    channels[index]['last_post'] = new_post_id - 10
                    break
                continue
            channels[index]['last_post'] = new_post_id
            title = soup.find('meta', property="og:title").attrs['content']

            print(title, new_post_id)
            description = soup.find('meta', property="og:description").attrs['content']
            # coef, name, date = checker(f"{title}\n{description}")
            # if coef >= VALID_EVENT_THRESHOLD:
            #     send(title, description, origin)
