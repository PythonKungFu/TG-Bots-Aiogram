import requests
from config import TOKEN
from pprint import pp

# getMe  getUpdates  sendMessage
METHOD_NAME = 'sendMessage'
data = {
    'chat_id': 448569572,
    'text': 'Hi!'
}
url = f'https://api.telegram.org/bot{TOKEN}/{METHOD_NAME}'
res = requests.get(url, params=data)
pp(res.json())
