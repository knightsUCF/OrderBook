import os
import time
import Broker

'''
API Rate Limit
At the current time Binance rate limits are: 1200 requests per minute. 10 orders per second. 100,000 orders per 24hrs.
'''


orderbook = Broker.Broker()


#######################################################################################################


run = True



def CollectData():
    count = 0

    while run:
        time.sleep(1)
        orderbook.WriteData()




CollectData()
