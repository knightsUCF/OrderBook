import json
import requests
import csv
import time

# binance api documentation: https://github.com/binance-exchange/binance-official-api-docs/blob/master/rest-api.md




class Broker():


    def GetBook(self, symbol):
        # todo: self.book = requests.get()
        return requests.get('https://www.binance.com/api/v3/depth', params = (('symbol', symbol),)).json()



    def GetPrice(self, symbol):
        self.price = requests.get('https://www.binance.com/api/v3/ticker/price', params = (('symbol', symbol),) ).json()['price']



############# Format data methods, can later be refactored to separate class ############################################################################################################


    def AddTimeToData(self, data):
        for row in data:
            lastColumn = row[-1]
            now = time.strftime('%d-%m-%Y %H:%M:%S')
            row.append(now)
        return data



    def AddPriceToData(self, data):
        for row in data:
            lastColumn = row[-1]
            row.append(self.price)
        return data



    def WriteToCSV(self, data):
        with open("OrderBook.csv", "a") as my_csv:  # w+ instead of a is overrite
            csvWriter = csv.writer(my_csv, delimiter=',')
            csvWriter.writerows(data)



    def WriteData(self):
        withoutPrice = self.AddTimeToData(self.GetBook('ETHBTC')['bids'])
        time.sleep(.1)
        self.GetPrice('ETHBTC')
        withPrice = self.AddPriceToData(withoutPrice)
        self.WriteToCSV(withPrice)














# orderbook = OrderBook()

# print(orderbook.GetPrice('BNBBTC'))

# orderbook = OrderBook()

# orderbook.WriteData()


# orderbook.WriteToCSV(orderbook.AddTimeToData(orderbook.Get('BNBBTC')['bids']))


# orderBookData = GetOrderBook('BNBBTC')
# csvData = AddTimeToData(orderBookData['bids'])
# WriteToCSV(csvData)



'''
def GetOrderBook(symbol):
    url = 'https://www.binance.com/api/v3/depth'
    params = (('symbol', symbol),)
    return requests.get(url, params = params).json()



def AddTimeToData(data):
    for row in data:
        lastColumn = row[-1]
        now = time.strftime('%d-%m-%Y %H:%M:%S')
        row.append(now)
    return data



def WriteToCSV(data):
    with open("OrderBook.csv", "a") as my_csv: # w+ instead of a is overrite
        csvWriter = csv.writer(my_csv, delimiter=',')
        csvWriter.writerows(data)



orderBookData = GetOrderBook('BNBBTC')
csvData = AddTimeToData(orderBookData['bids'])
WriteToCSV(csvData)




'''






key = 'aAtY5wKsVqmYbnWFdla7BRqzrjEzYSZOk42xWgct4Z8vmlRTCzQiEnxJU7gomI0n'
secret = '4R11ucFus53tuCbSHnHOtURRttokHD7wgDBt3Ev4123YOUEtMBdklx8xh9keXh0h'


'''
import csv

a = [[1,2,3,4],[5,6,7,8]]

with open("new_file.csv","w+") as my_csv:
    csvWriter = csv.writer(my_csv,delimiter=',')
    csvWriter.writerows(a)
'''

'''
def get_total_longs(self):
        longs = self.depth['bids']
        total = 0
        for x in longs:
            total += float(x[1])
        return total
    '''


# get first bid: ['bids'][0]
