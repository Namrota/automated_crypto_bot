'''
This module provides an interface to the Binance API for cryptocurrency trading for both demo and live trading. 
The module is designed to be used in a larger application, such as a trading bot, and can be easily integrated with other components.
It includes functions for fetching market data, placing orders, and managing account information. 

1. Fetches real-time market data for specified cryptocurrency pairs.
2. Fetch a list of symbols on the Binance exchange.
3. Place buy and sell orders on the Binance exchange.
4. Get all the current account information, including balances and open orders.
5. Cancel open orders on the Binance exchange.
6. Handle API responses and errors gracefully, providing useful feedback to the user.

------------- methods to implement ----------------
* get_contracts(): Fetches a list of all available trading pairs (contracts) on the Binance exchange.
'''
import logging
import os
from dotenv import load_dotenv
import requests
import pprint
import sys #appending a path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import settings






#load environment variables from local .env file:
#load_dotenv()

#--------------------- variables from settings.py --------------------------------#
binance_base_url= settings.BASE_URL
exchange_url= settings.EXCHANGE_INFO
price_24hr= settings.TICKER_24HR
#---------------------------------------------------------------------------------#
#logger= logging.getlogger()

# Simple function: GET Current exchange trading rules and symbol information
def get_contracts():
    response_obj= requests.get(f"{binance_base_url}{exchange_url}")
    symbol=[s['symbol'] for s in response_obj.json()['symbols']]
    #print(response_obj.status_code)
    #pprint.pprint([s['symbol'] for s in response_obj.json()['symbols']], compact= True)
    return symbol

def get_24hr_ticker(symbol:str)-> dict:
    '''
    GET 24 hour roliing window price change statistics
    ARGS:
    symbol: Trading pair symbol
    RETURNS:
    Dictionary
    Example for a symbol 'BTCUSDT':
    {
    "symbol": "BTCUSDT",
    "priceChange": "-1137.30",
    "priceChangePercent": "-1.614",
    "weightedAvgPrice": "70140.32",
    "lastPrice": "69319.00",
    "lastQty": "0.002",
    "openPrice": "70456.30",
    "highPrice": "71748.10",
    "lowPrice": "68932.90",
    "volume": "214975.045",
    "quoteVolume": "15078417861.83",
    "openTime": 1773147540000,
    "closeTime": 1773233999388,
    "firstId": 7414325067,
    "lastId": 7419918350,
    "count": 5586555
    }

    
    '''
    response_obj= requests.get(f'{binance_base_url}{price_24hr}', params={'symbol': symbol.upper()})
    response_obj.raise_for_status()
    return response_obj.json()

print(get_24hr_ticker(symbol="PAXGUSDT"))