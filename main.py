from model import Coins

#We initialize the process
real_time_coins = Coins(mode = True) #True = Coingeko, False = Coinmarketcap

#We extract the data in real time
real_time_coins.extraction()

#We pull the data in Google Spreadsheet
real_time_coins.upload()


