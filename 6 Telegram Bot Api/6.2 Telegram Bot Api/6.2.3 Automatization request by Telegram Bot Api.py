import requests
import time
from config import TOKEN
from pprint import pp


API_URL: str = 'https://api.telegram.org/bot'
TEXT: str = 'Ура! Классный апдейт!'
MAX_COUNTER: int = 100

offset: int = -2
counter: int = 0
chat_id: int

while counter < MAX_COUNTER:
    print('attempt =', counter)  # Чтобы видеть в консоли, что код живет
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for result in updates['result']:
            offset = result['update_id']
            chat_id = result['message']['from']['id']
            requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={TEXT}')
    time.sleep(1)
    counter += 1
