import requests
import json
import csv

from dbInterface import StockDatabase

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
    """Returns the list of currently active stocks"""
    apiUrl = f'{url}LISTING_STATUS&state=active&apikey={key}'
    with requests.Session() as s:
        download = s.get(apiUrl)
        decodedContent = download.content.decode('utf-8')
        cr = csv.reader(decodedContent.splitlines(), delimiter=',')
        myList = list(cr)
    return myList[1::]

#main
url = 'https://www.alphavantage.co/query?function='
key = get_key()
activeStocks = get_active_stocks(url, key)
db = StockDatabase('sqlite:///activestocks.db')
for row in activeStocks:
    db.add_listing(row[0], row[1], row[2], row[3])
db.commit()
db.close()
print('done')
# symbol = input('Please enter a stock symbol: ')
# get_stock_data(symbol, url, key)


