import pandas as pd
import os
from os import walk


path = os.getcwd()
stocks_path = path + "/StockData/stocks/"


_, _, stock_names = next(walk(stocks_path))


'''
print(len(stock_names))
for filename in  stock_names:
	print(filename)
'''

start_date = '2010-01-22'
end_date = '2020-01-26'
dates = pd.date_range(start_date, end_date)

df = pd.DataFrame(index=dates)
#print(df)

'''

df = df.join(join_stock_data(stocks_path, stock_names[0]))


def join_stock_data(path, filename):
	df_stock = pd.read_csv(path+filename)
	return df

'''
for symbol in stock_names:
	df_temp = pd.read_csv('StockData/stocks/{}'.format(symbol), index_col="Date", parse_dates=True, usecols=["Date", "Adj Close"], na_values=['nan'])
	df = df.join(df_temp, how = 'inner', lsuffix = symbol)