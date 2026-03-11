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

#load environment variables from local .env file:
load_dotenv()
binance_base_url= os.getenv("BASE_URL")
exchange_url= os.getenv("EXCHANGE_INFO")
#logger= logging.getlogger()

# Simple function: GET Current exchange trading rules and symbol information
def get_contracts():
    response_obj= requests.get(f"{binance_base_url}{exchange_url}")
    symbol=[s['symbol'] for s in response_obj.json()['symbols']]
    #print(response_obj.status_code)
    #pprint.pprint([s['symbol'] for s in response_obj.json()['symbols']], compact= True)
    return symbol


print(get_contracts())