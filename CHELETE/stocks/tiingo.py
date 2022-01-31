# from chelete.settings import TIINGO_KEY
import requests


headers = {
    'Content-Type': 'application/json',
    'Authorization' : 'Token 0a57332230419084055e23b90c15ba830ba35d19'
}

def get_meta_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()


def get_price_data(ticker):
    url = "https://api.tiingo.com/tiingo/daily/{}/prices".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]

def get_history_data(ticker):
    today = time.now
    # url = https://api.tiingo.com/tiingo/daily/<ticker>/prices?startDate=2012-1-1&endDate=2016-1-1 
    
    url = "https://api.tiingo.com/tiingo/daily/{}/prices/prices?startDate=2012-1-1&endDate=2016-1-1".format(ticker)
    response = requests.get(url, headers=headers)
    return response.json()[0]