import requests

def get_key():
    with open('./alphavantage_Key.txt', 'r') as keyFile:
        key = keyFile.readline()
    
    key = key.strip()
    return key