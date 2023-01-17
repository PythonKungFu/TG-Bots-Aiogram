import requests
from config import TOKEN
from time import sleep
from pprint import pp


API_CAT_URL: str = 'https://aws.random.cat/meow'
API_URL: str = 'https://api.telegram.org/bot'
ERROR_TEXT: str = 'Здесь должна была быть картинка с котиком :('
MAX_COUNT: int = 100

counter: int = 0
offset: int = -2

while counter < MAX_COUNT:
    print('Counter :', counter)
    updates = requests.get(f'{API_URL}{TOKEN}/getUpdates?offset={offset + 1}').json()
    if updates['result']:
        for update in updates['result']:
            offset = update['update_id']
            chat_id = update['message']['chat']['id']
            res = requests.get(API_CAT_URL)
            if res.ok:
                cat_img = res.json()['file']
                requests.get(f'{API_URL}{TOKEN}/sendPhoto?chat_id={chat_id}&photo={cat_img}')
            else:
                requests.get(f'{API_URL}{TOKEN}/sendMessage?chat_id={chat_id}&text={ERROR_TEXT}')

    sleep(1)
    counter += 1
