import requests
import json

url ='https://bittrex.com/api/v1.1/public/getmarketsummaries'


results = requests.get(url)
dic = json.loads(results.text)

# print(results_dict)
last_price = {}
# this is a dict that has keys of tickers (ex. ETH-NEO) and values of the exchange rate.

cur_exch = []
# list of all the kinds of tickers (ex. ETH-NEO)

for price in dic['result']:
    last_price.setdefault(price['MarketName'],price['Last'])
    cur_exch.append(price['MarketName'])

# print(last_price.items())
# print(last_price)
dollars = 500


arb = (( ( dollars / last_price['USDT-ETH'] ) / last_price['ETH-NEO'] ) * last_price['USDT-NEO'])
profit = ((arb) - dollars)

