import requests
import json

def get_key():
    with open('./alphavantage_Key.txt', 'r') as keyFile:
        key = keyFile.readline()
    
    key = key.strip()
    return key

def get_stock_data(symbol, url, key):
    data = requests.get(f'{url}TIME_SERIES_DAILY&symbol={symbol}&apikey={key}')
    print(json.loads(data.text))

#main
url = 'https://www.alphavantage.co/query?function='
key = get_key()
symbol = input('Please enter a stock symbol: ')
get_stock_data(symbol, url, key)


