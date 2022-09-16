import requests
import json
import csv

def build_url(url, key, apiFunction, apiParams = None):
    if apiParams == None:
        apiParams = {}

def get_key():
    with open('./alphavantage_Key.txt', 'r') as keyFile:
        key = keyFile.readline()
    
    key = key.strip()
    return key

def get_stock_data(symbol, url, key):
    data = requests.get(f'{url}TIME_SERIES_DAILY&symbol={symbol}&apikey={key}')
    print(json.loads(data.text))

def get_active_stocks(url, key):
    apiUrl = f'{url}LISTING_STATUS&state=active&apikey={key}'
    with requests.Session() as s:
        download = s.get(apiUrl)
        decodedContent = download.content.decode('utf-8')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        myList = list(cr)
        for row in myList:
            print(row)

#main
url = 'https://www.alphavantage.co/query?function='
key = get_key()
get_active_stocks(url, key)
# symbol = input('Please enter a stock symbol: ')
# get_stock_data(symbol, url, key)


