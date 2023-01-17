import requests
from config import TOKEN
import time


API_URL: str = 'https://api.telegram.org/bot'
offset: int = -2
updates: dict


def do_something() -> None:
    print('Был апдейт')


while True:
    start = time.time()
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for update in updates['result']:
            offset = update['update_id']
            do_something()
    time.sleep(3)
    print(f'Время между запросами к Telegram Bot API: {time.time() - start}')
