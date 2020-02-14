from pandas import read_csv
from datetime import datetime


# https://www.datacamp.com/community/tutorials/lstm-python-stock-market
# https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/
#  https://machinelearningmastery.com/multivariate-time-series-forecasting-lstms-keras/


class CleanData():


    def ParseTime(self, x):
        return datetime.strptime(x, '%Y %m %d %H')


    def RunCleanProcess(self, csv):
        csvDataset = read_csv(csv, parse_dates=[['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
        csvDataset.drop('No', axis=1, inplace=True)
        csvDataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
        csvDataset.index.name = 'date'
        csvDataset['pollution'].fillna(0, inplace=True)  # mark all NA values with
        # dataset = dataset[24:] # drop the first 24 hours
        return csv


    def PrintDataframe(self, dataset):
        print(dataset.head(5))


    def SaveDataset(self, dataset, filename):
        dataset.to_csv(filename)


    def Test(self, csv):
        csvDataset = read_csv(csv, parse_dates=[['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)


    def ConvertFromCSVToDataFrame(self, csv):
        return read_csv(csv, index_col = 2)


    def ViewDataframeSample(self, dataframe):
        print(dataframe.tail(10))


    def MarkNAwithZero(self, dataframe):
        # return dataframe['pollution'].fillna(0, inplace=True)
        # mark all NA values with 0
        # dataset['pollution'].fillna(0, inplace=True)
        pass


    def Label(self, dataframe):
        dataframe.index.name = 'date'
        dataframe.columns = ['book', 'shares', 'price']



# 0.00207900,94.69000000,30-11-2019 03:54:34,0.00208060

cleanData = CleanData()

dataframe = cleanData.ConvertFromCSVToDataFrame('OrderBook.csv')

cleanData.Label(dataframe)
cleanData.ViewDataframeSample(dataframe)



'''
# load data
def parse(x):
   return datetime.strptime(x, '%Y %m %d %H')
dataset = read_csv('raw.csv',  parse_dates = [['year', 'month', 'day', 'hour']], index_col=0, date_parser=parse)
dataset.drop('No', axis=1, inplace=True)
# manually specify column names
dataset.columns = ['pollution', 'dew', 'temp', 'press', 'wnd_dir', 'wnd_spd', 'snow', 'rain']
dataset.index.name = 'date'
# mark all NA values with 0
dataset['pollution'].fillna(0, inplace=True)
# drop the first 24 hours
dataset = dataset[24:]
# summarize first 5 rows
print(dataset.head(5))
# save to file
dataset.to_csv('pollution.csv')
'''
