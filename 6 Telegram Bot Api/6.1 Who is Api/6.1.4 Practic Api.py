import requests
from pprint import pp


url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)
if response.ok:
    pp(response.text)
else:
    pp(f'Status code: {response.status_code}')
