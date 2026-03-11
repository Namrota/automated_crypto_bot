
# Trading Tickers Default (comma-separated)
SPOT_TICKERS=['BTCUSDT','ETHUSDT','SOLUSDT','XRPUSDT','BNBUSDT']


# Base Endpoints:
# All endpoints return either a JSON object or array
# Data is returned in Ascennding order (oldest to newest)
BASE_URL= "https://fapi.binance.com"
TESTNET_REST_URL= "https://demo-fapi.binance.com"
TESTNET_WEBSOCKET_URL= "wss://fstream.binancefuture.com"

#URLs:
EXCHANGE_INFO= "/fapi/v1/exchangeInfo"
TICKER_24HR = "/fapi/v1/ticker/24hr"
#latest prce for a symbol or symbols
SYMBOL_PRICE= "/fapi/v2/ticker/price"