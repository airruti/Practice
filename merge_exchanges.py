import requests
import json
import sys #for CLI input
from pprintpp import pprint as pp ####I like using prettyprint for testing####
from decimal import * #attempt to avoid floating-point error
import time

def main():
    #variable initialization
    sumPrice = 0.0
    totalAmount = sys.argv[1]
    totalAmount = Decimal(totalAmount)
    sumPrice = Decimal(sumPrice)

    coinbaseurl = "https://api.pro.coinbase.com/products/BTC-USD/book?level=2"
    geminiurl = "https://api.gemini.com/v1/book/BTCUSD"
    krakenurl = "https://api.kraken.com/0/public/Depth?pair=XBTUSD"

    headers = {"Accept": "application/json"}

    #json for easy formatting
    responseCB = requests.request("GET", coinbaseurl, headers=headers).json()
    responseGem = requests.request("GET", geminiurl, headers=headers).json()
    responseKraken = requests.request("GET", krakenurl, headers=headers).json()

    #seperate bids and asks
    CBbids = responseCB['bids']
    CBasks = responseCB['asks']

    gemBids = responseGem['bids']
    gemAsks = responseGem['asks']

    krakenBids = responseKraken['result']['XXBTZUSD']['bids']
    krakenAsks = responseKraken['result']['XXBTZUSD']['asks']

    #Convert Gemini list of dict to list of lists
    gemBids = [[row['price'], row['amount']] for row in gemBids]
    gemAsks = [[row['price'], row['amount']] for row in gemAsks]

    #combine and sort
    combinedBids = CBbids + gemBids + krakenBids
    combinedBids = sorted(combinedBids, key=lambda x: float(x[0]), reverse=True) #bids sorted highest first

    combinedAsks = CBasks + gemAsks + krakenAsks
    combinedAsks = sorted(combinedAsks, key=lambda x: float(x[0]))

    # pp(combinedBids)
    # pp(combinedAsks)

    # calculate the total offer price for X BTC
    for i in range(len(combinedAsks)):
        if(totalAmount - Decimal(combinedAsks[i][1]) <= 0):
            sumPrice += Decimal(combinedAsks[i][0]) * Decimal(totalAmount)
            totalAmount -= totalAmount
            break
        totalAmount -= Decimal(combinedAsks[i][1])
        sumPrice += Decimal(combinedAsks[i][0]) * Decimal(combinedAsks[i][1])
        
            
    print(f"total buy price for {sys.argv[1]} BTC: {sumPrice}\nremaining BTC: {totalAmount}")

    #reinitialize variables
    sumPrice = 0.0
    totalAmount = sys.argv[1]
    sumPrice = Decimal(sumPrice)
    totalAmount = Decimal(totalAmount)

    #calculate the total bid price for X BTC
    for i in range(len(combinedBids)):
        if(totalAmount - Decimal(combinedBids[i][1]) <= 0):
            sumPrice += Decimal(combinedBids[i][0]) * Decimal(totalAmount)
            totalAmount -= totalAmount
            break
        totalAmount -= Decimal(combinedBids[i][1])
        sumPrice += Decimal(combinedBids[i][0]) * Decimal(combinedBids[i][1])
        
            
    print(f"total sell price for {sys.argv[1]} BTC: {sumPrice}\nremaining BTC: {totalAmount}\n")
    print('---------------------')
    #time.sleep(5)
    print()

main()
    