import requests


# Simple example Api
url = 'https://cdn.jsdelivr.net/gh/fawazahmed0/currency-api@1/latest/currencies/btc.json'
response = requests.get(url).json()
print(response['btc']['rub'])

# Link publics API
# https://github.com/public-apis/public-apis
